#!/usr/bin/env python3
"""Compare two blind AIMF scoring sheets and adjudicate per the Scoring Protocol.

Implements P4 (agreement) and P5 (adjudication rules 1-4) exactly as written in
AIMF-ASSESSMENT-GUIDE.md:

  Rule 1  differ by 1, same deciding artefact        -> lower score stands
  Rule 2  differ by 1, different deciding artefacts  -> third adjudicator's score stands
  Rule 3  differ by >=2                             -> adjudication + defect note
  Rule 4  NA vs numeric                             -> adjudicator decides whether absence
                                                       was established

Usage:
  python3 compare_scores.py scores-A.json scores-B.json [--adjudicator scores-C.json] \
      [--json out.json] [--md out.md]
"""
import argparse
import json
import sys
from collections import Counter


def load(path):
    d = json.load(open(path))
    return d["scores"], d


def val(entry):
    s = entry["score"]
    return "NA" if s == "NA" else int(s)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("a")
    ap.add_argument("b")
    ap.add_argument("--adjudicator")
    ap.add_argument("--json", default=None)
    ap.add_argument("--md", default=None)
    args = ap.parse_args()

    a, da = load(args.a)
    b, db = load(args.b)
    controls = sorted(set(a) & set(b))
    missing = sorted(set(a) ^ set(b))
    if missing:
        print(f"WARNING: sheets disagree on control set: {missing}", file=sys.stderr)

    adj = {}
    if args.adjudicator:
        adj, _ = load(args.adjudicator)

    rows, disagreements = [], []
    agree = 0
    for c in controls:
        va, vb = val(a[c]), val(b[c])
        same = va == vb
        agree += 1 if same else 0
        row = {
            "control": c,
            "A": va,
            "B": vb,
            "A_artefact": a[c]["deciding_artefact"],
            "B_artefact": b[c]["deciding_artefact"],
            "agree": same,
        }
        if not same:
            na_case = "NA" in (va, vb)
            diff = None if na_case else abs(va - vb)
            if na_case:
                rule = 4
            elif diff == 1 and a[c]["deciding_artefact"] == b[c]["deciding_artefact"]:
                rule = 1
                row["final"] = min(va, vb)
            elif diff == 1:
                rule = 2
            else:
                rule = 3
            row["rule"] = rule
            if rule in (2, 3, 4):
                if c in adj:
                    row["final"] = val(adj[c])
                    row["adjudicator_artefact"] = adj[c]["deciding_artefact"]
                else:
                    row["final"] = None
            row["A_note"] = a[c]["boundary_note"][:400]
            row["B_note"] = b[c]["boundary_note"][:400]
            disagreements.append(row)
        rows.append(row)

    unresolved = [d for d in disagreements if d.get("final") is None]
    by_rule = Counter(d["rule"] for d in disagreements)
    by_rule_final = Counter(str(d.get("final")) for d in disagreements)

    summary = {
        "controls_scored": len(controls),
        "agree": agree,
        "agreement_rate": round(agree / len(controls), 4) if controls else None,
        "disagreements": len(disagreements),
        "by_rule": dict(sorted(by_rule.items())),
        "final_after_adjudication": dict(sorted(by_rule_final.items())),
        "unresolved": [d["control"] for d in unresolved],
        "assessors": {
            "A": {"model": da["model"], "transport": da.get("transport"),
                  "pack_sha256": da["pack_sha256"]},
            "B": {"model": db["model"], "transport": db.get("transport"),
                  "pack_sha256": db["pack_sha256"]},
        },
    }
    out = {"summary": summary, "rows": rows, "disagreements": disagreements}

    if args.json:
        json.dump(out, open(args.json, "w"), indent=1)
    if args.md:
        lines = [
            "# Blind double-scoring result — AIMF-VAL-2026-A",
            "",
            f"- Controls scored: {summary['controls_scored']}",
            f"- Agreement: {agree}/{summary['controls_scored']} "
            f"({summary['agreement_rate'] * 100:.1f}%)",
            f"- Disagreements: {summary['disagreements']} "
            f"(by rule: {summary['by_rule']})",
            f"- Unresolved after adjudication: {summary['unresolved'] or 'none'}",
            "",
            "| Control | A | B | Rule | Final | A artefact | B artefact |",
            "|---|---|---|---|---|---|---|",
        ]
        for d in disagreements:
            lines.append(
                f"| {d['control']} | {d['A']} | {d['B']} | {d['rule']} | "
                f"{d.get('final')} | {d['A_artefact']} | {d['B_artefact']} |"
            )
        open(args.md, "w").write("\n".join(lines) + "\n")

    print(json.dumps(summary, indent=1))
    if unresolved:
        print("\nControls needing adjudication:", " ".join(summary["unresolved"]))
        sys.exit(0)


if __name__ == "__main__":
    main()
