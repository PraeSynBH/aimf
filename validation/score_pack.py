#!/usr/bin/env python3
"""Score one AIMF evidence pack with an independent assessor model.

Instrument validation harness for the AIMF blind double-scoring protocol.
Each invocation is one assessor: it receives ONLY the frozen evidence pack and
the per-control anchors. It never sees another assessor's output, and each batch
runs in a fresh model session (no shared conversation state).

Two transports:
  --via hermes      one-shot `hermes -z` session (uses the locally configured
                    provider credentials; each call is its own session)
  --via openrouter  direct HTTPS call with OPENROUTER_API_KEY

Usage:
  python3 score_pack.py --via hermes --model anthropic/claude-sonnet-5.5 \
      --assessor A --pack AIMF-VAL-2026-A-EVIDENCE-PACK.md --out scores-A.json
"""
import argparse
import hashlib
import json
import os
import re
import subprocess
import sys
import tempfile
import time
import urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
BANK = os.path.join(
    HERE, "..", "documents", "AIMF-Full-Documentation",
    "implementation", "AIMF-ASSESSMENT-QUESTION-BANK.csv",
)

SYSTEM = """You are an AIMF assessor. You score AI-management controls from a frozen
evidence pack, using the control's written behavioural anchors.

Scale: 0 = ML1 Initial, 1 = ML2 Developing, 2 = ML3 Defined, 3 = ML4 Managed,
4 = ML5 Optimizing.

Scoring rules you must follow:
1. Score = the HIGHEST level whose anchor is FULLY satisfied by named, dated artefacts
   in the pack. Partial satisfaction of a level means the level below.
2. Two-level rule: if the evidence supports both level n and n+1, score n unless the
   artefact that distinguishes n+1 from n (the measurement, review cadence, or
   decision-change artefact named in the anchor) is itself present, current and named.
   Record the boundary in boundary_note.
3. Absence scores 0 only when the control is in scope AND the pack shows the absence was
   established (the artefact does not exist). If the pack simply does not address the
   control, or the artefact is withheld, conflicting, or applicability is undetermined,
   score "NA" — never 0.
4. Do not reward intent, assertion or verbal assurance. Reward artefacts.
5. deciding_artefact = the EV-id that decided the score (or "" for NA).

Four definitions decide the phrases the anchors repeat:
- COVERAGE: "every in-scope system/role/policy/period" means 100% of the register and the whole
  period. A pilot, a subset, "most", or an open exception is NOT coverage: score 1.
- CADENCE: "reviewed on cadence" needs a stated interval with at least TWO minuted occurrences
  in the last 12 months and a recorded next date. One occurrence is not a cadence: level-3 fails.
- MEASURE: "measured/tracked/against target" needs a named metric, a recorded value, a stated
  target, and a report to a named body at the cadence. A one-off study or a value with no
  target does not satisfy a level-3 clause.
- ONE ARTEFACT, ONE CLAUSE: each anchor clause needs its own artefact; a clause supported only
  by inference from another clause's artefact is unevidenced and scores the level below.

Procedure for every control — follow it mechanically, do not weigh holistically:
1. Read anchors 0-4 for the control. Write out, for each level 1..4, the clauses that level adds.
2. Test the HIGHEST level first: for each of its clauses, name the artefact that evidences it.
   A clause fails if no named artefact evidences it, or if the coverage/cadence/measure test fails.
3. On the first level where any clause fails, the score is that level minus 1. Do not "mostly"
   satisfy a level, do not average, do not give credit for effort, maturity, or intent.
4. If level 1's clause also fails, score 0 — but only if the pack establishes the absence.
5. If the pack cannot decide a clause because the evidence is missing, withheld, conflicting, or
   applicability is undetermined, score "NA".

Return ONLY a JSON array, no prose, no code fence:
[{"control":"GOV-1.1","score":2,"deciding_artefact":"EV-014",
  "failed_clause":"level 3 needs obligation-coverage measure reviewed against target; none named",
  "boundary_note":"..."}]
"""


def sha(path):
    return hashlib.sha256(open(path, "rb").read()).hexdigest()


def load_anchors():
    import csv
    rows = {}
    with open(BANK, newline="") as fh:
        for r in csv.DictReader(fh):
            rows[r["control"]] = r
    return rows


def load_pack(path):
    txt = open(path).read()
    blocks = {}
    for chunk in re.split(r"^### ", txt, flags=re.M)[1:]:
        cid = chunk.split(" ")[0].strip()
        body = chunk.split("\n", 1)[1].strip() if "\n" in chunk else ""
        blocks[cid] = body
    return blocks


BINDING_RULE = """EVIDENCE BINDING (this run only): each control below carries a MANDATORY
EVIDENCE SET. Decide the score from that set and nothing else. For every level you
consider awarding, name the artefact from the set that evidences it (level_evidence).
deciding_artefact must be a member of the mandatory set. If the set cannot decide the
control, score "NA" and name what is missing in failed_clause -- do not reach for an
artefact outside the set."""


def build_prompt(controls, anchors, pack, binding=None):
    parts = [SYSTEM, "\n--- controls to score ---\n"]
    if binding:
        parts.append(BINDING_RULE + "\n")
    for cid in controls:
        a = anchors[cid]
        block = (
            f"### {cid}\n"
            f"Question: {a['question']}\n"
            f"Evidence expected: {a['evidence']}\n"
            f"Anchor 0: {a['anchor_0']}\n"
            f"Anchor 1: {a['anchor_1']}\n"
            f"Anchor 2: {a['anchor_2']}\n"
            f"Anchor 3: {a['anchor_3']}\n"
            f"Anchor 4: {a['anchor_4']}\n"
        )
        if binding:
            b = binding["controls"][cid]
            block += (
                "MANDATORY EVIDENCE SET: " + ", ".join(b["mandatory"]) + "\n"
                f"Primary artefact: {b['primary']}\n"
            )
        block += f"--- evidence pack ---\n{pack[cid]}\n"
        parts.append(block)
    parts.append(
        "\nReturn the JSON array now, one row per control, same order as above."
    )
    return "\n".join(parts)


def call_openrouter(model, user, temperature):
    key = os.environ.get("OPENROUTER_API_KEY")
    if not key:
        sys.exit("OPENROUTER_API_KEY not set")
    body = json.dumps({
        "model": model,
        "temperature": temperature,
        "messages": [
            {"role": "system", "content": SYSTEM},
            {"role": "user", "content": user},
        ],
    }).encode()
    req = urllib.request.Request(
        "https://openrouter.ai/api/v1/chat/completions",
        data=body,
        headers={
            "Authorization": f"Bearer {key}",
            "Content-Type": "application/json",
            "X-Title": "AIMF inter-rater validation",
        },
    )
    with urllib.request.urlopen(req, timeout=300) as resp:
        payload = json.load(resp)
    return payload["choices"][0]["message"]["content"]


def call_hermes(model, user, timeout=420):
    """One-shot hermes session: fresh process, no tools, no shared state."""
    with tempfile.NamedTemporaryFile("w", suffix=".txt", delete=False) as fh:
        fh.write(user)
        prompt_path = fh.name
    try:
        prompt = open(prompt_path).read()
        proc = subprocess.run(
            ["hermes", "-m", model, "-z", prompt, "--ignore-rules", "-t", ""],
            capture_output=True, text=True, timeout=timeout,
        )
        if proc.returncode != 0:
            raise RuntimeError(proc.stderr[-800:])
        return proc.stdout
    finally:
        os.unlink(prompt_path)


def call(model, user, transport, temperature, retries=2):
    last = None
    for attempt in range(retries):
        try:
            if transport == "hermes":
                return call_hermes(model, user)
            return call_openrouter(model, user, temperature)
        except Exception as exc:  # noqa: BLE001
            last = exc
            time.sleep(3 * (attempt + 1))
    raise SystemExit(f"model {model} failed after {retries} attempts: {last}")


def parse(raw):
    txt = raw.strip()
    txt = re.sub(r"^```(?:json)?|```$", "", txt, flags=re.M).strip()
    start, end = txt.find("["), txt.rfind("]")
    if start == -1 or end == -1:
        raise ValueError(f"no JSON array in response: {txt[:300]}")
    return json.loads(txt[start:end + 1])


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", required=True)
    ap.add_argument("--assessor", required=True)
    ap.add_argument("--pack", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--via", default="hermes", choices=["hermes", "openrouter"])
    ap.add_argument("--batch", type=int, default=12)
    ap.add_argument("--temperature", type=float, default=0.0)
    ap.add_argument("--fixture", default="AIMF-VAL-2026-A",
                    help="fixture id recorded in the output (A or B)")

    ap.add_argument("--limit", type=int, default=0, help="debug: score first N controls")
    ap.add_argument("--binding", default="",
                    help="evidence binding JSON (see runB/evidence_binding.py); "
                         "enforces a per-control mandatory evidence set")
    args = ap.parse_args()

    anchors = load_anchors()
    pack = load_pack(args.pack)

    binding = None
    if args.binding:
        binding = json.load(open(args.binding))
        if binding.get("pack_sha256") != sha(args.pack):
            sys.exit("binding was derived from a different pack "
                     f"({binding.get('pack_sha256','?')[:12]} vs {sha(args.pack)[:12]}); "
                     "re-derive it with runB/evidence_binding.py")
        missing_b = [c for c in pack if c not in binding["controls"]]
        if missing_b:
            sys.exit(f"pack controls absent from binding: {missing_b}")
        print(f"binding {args.binding}: {binding['control_count']} controls, "
              f"sha256 {binding.get('sha256','')[:12]}", file=sys.stderr)
    controls = sorted(pack)
    if args.limit:
        controls = controls[:args.limit]
    missing = [c for c in controls if c not in anchors]
    if missing:
        sys.exit(f"pack has controls not in the bank: {missing}")

    scores, raw_log = {}, {}
    started = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    for i in range(0, len(controls), args.batch):
        batch = controls[i:i + args.batch]
        user = build_prompt(batch, anchors, pack, binding)
        raw = call(args.model, user, args.via, args.temperature)
        raw_log[f"batch_{i // args.batch + 1}"] = raw
        try:
            rows = parse(raw)
        except Exception as exc:  # noqa: BLE001
            print(f"batch {i // args.batch + 1} parse failure: {exc}", file=sys.stderr)
            print(raw[:2000], file=sys.stderr)
            raise
        for row in rows:
            cid = str(row.get("control", "")).strip()
            if cid not in batch:
                continue
            s = row.get("score")
            s = "NA" if str(s).strip().upper() in ("NA", "N/A", "NOT ASSESSABLE") else int(s)
            dec = (row.get("deciding_artefact") or "").strip()
            ok = None
            if binding and s != "NA":
                ok = dec in binding["controls"][cid]["mandatory"]
            scores[cid] = {
                "score": s,
                "deciding_artefact": dec,
                "boundary_note": (row.get("boundary_note") or "").strip(),
                "failed_clause": (row.get("failed_clause") or "").strip(),
                "binding_ok": ok,
            }
        print(f"{args.assessor}: {len(scores)}/{len(controls)} scored",
              file=sys.stderr)

    violations = sorted(c for c, v in scores.items() if v.get("binding_ok") is False)
    if binding:
        print(f"{args.assessor}: binding violations {len(violations)}/{len(scores)} {violations}",
              file=sys.stderr)

    absent = [c for c in controls if c not in scores]
    if absent:
        print(f"{args.assessor}: MISSING {absent}", file=sys.stderr)

    out = {
        "fixture": args.fixture,
        "assessor": args.assessor,
        "model": args.model,
        "transport": args.via,
        "temperature": args.temperature,
        "pack_sha256": sha(args.pack),
        "bank_sha256": sha(BANK),
        "started": started,
        "finished": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "controls_scored": len(scores),
        "binding": ({"file": os.path.basename(args.binding),
                     "sha256": binding.get("sha256", ""),
                     "pack_sha256": binding.get("pack_sha256", ""),
                     "violations": violations} if binding else None),
        "scores": scores,
        "raw": raw_log,
    }
    with open(args.out, "w") as fh:
        json.dump(out, fh, indent=1, sort_keys=True)
    print(f"wrote {args.out}: {len(scores)} controls")


if __name__ == "__main__":
    main()
