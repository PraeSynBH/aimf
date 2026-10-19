#!/usr/bin/env python3
"""Derive a per-control mandatory evidence binding from a frozen AIMF evidence pack.

Why this exists (STARTINGPOINT v0.10, D5(b), A28/A29):
  Cross-vendor disagreement on the held-out case is not anchor wording and not a
  level offset. On the 29 case-B splits the two vendors cited the *same* deciding
  artefact only twice, versus 33 of 43 agreements (Fisher p = 1.9e-9). The
  mechanism is evidence selection: each assessor picks a different artefact out of
  the same pack block and then grades it. Anchor passes cannot move that.

  D5(b) therefore binds the evidence set per control: the assessor may decide only
  from a fixed, named set of artefacts for that control, and must say which artefact
  carried each level it awards. This script builds that binding mechanically from
  the pack itself -- it reads the `- **EV-nnn**` bullets under each control heading
  and nothing else, so the binding cannot be tuned against any score sheet.

Usage:
  python3 evidence_binding.py --pack ../AIMF-VAL-2026-B-EVIDENCE-PACK.md \
      --out evidence-bindings-B.json

The output is the artifact that gets frozen and hashed; score_pack.py --binding
consumes it and refuses to let a deciding artefact fall outside the set.
"""
import argparse
import hashlib
import json
import os
import re
import sys

EV_RE = re.compile(r"^-\s+\*\*(EV-\d+)\*\*\s*(.*)$", re.M)


def sha(path):
    return hashlib.sha256(open(path, "rb").read()).hexdigest()


def parse_pack(txt):
    """Return {control: [{id, text}]} in pack order, plus the dimension headings."""
    out = {}
    order = []
    dims = {}
    for chunk in re.split(r"^### ", txt, flags=re.M)[1:]:
        head, _, body = chunk.partition("\n")
        cid = head.split(" ")[0].strip()
        if not re.match(r"^[A-Z]{3}-\d+\.\d+$", cid):
            continue
        evs = [{"id": m.group(1), "text": m.group(2).strip()}
               for m in EV_RE.finditer(body)]
        out[cid] = evs
        order.append(cid)
        dims[cid] = cid.split("-")[0]
    return out, order, dims


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--pack", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--fixture", default="AIMF-VAL-2026-B")
    args = ap.parse_args()

    raw = open(args.pack).read()
    evs, order, dims = parse_pack(raw)

    controls = {}
    for cid in order:
        items = evs[cid]
        if not items:
            print(f"FATAL: {cid} lists no EV artefacts; a binding cannot be empty",
                  file=sys.stderr)
            sys.exit(1)
        ids = [i["id"] for i in items]
        controls[cid] = {
            "dimension": dims[cid],
            "mandatory": ids,
            # First-listed artefact is the pack's own primary evidence for the
            # control; the rest are the corroborating and maturity-level artefacts.
            "primary": ids[0],
            # Artefacts that establish a *level* rather than the control's existence:
            # the pack convention puts policy/design first and measurement/cadence
            # later, so anything after the first is a level-carrying artefact.
            "level_artefacts": ids[1:],
        }

    doc = {
        "fixture": args.fixture,
        "pack": os.path.basename(args.pack),
        "pack_sha256": sha(args.pack),
        "derivation": "mechanical: EV bullets under each '### <control>' heading, "
                      "pack order preserved; no score sheet was read",
        "control_count": len(controls),
        "controls": controls,
        "sha256": "",
    }
    body = json.dumps(doc, indent=1, sort_keys=True)
    doc["sha256"] = hashlib.sha256(body.encode()).hexdigest()

    with open(args.out, "w") as fh:
        json.dump(doc, fh, indent=1, sort_keys=True)

    # Sanity report
    total = sum(len(c["mandatory"]) for c in controls.values())
    by_dim = {}
    for cid, c in controls.items():
        by_dim.setdefault(c["dimension"], [0, 0])
        by_dim[c["dimension"]][0] += 1
        by_dim[c["dimension"]][1] += len(c["mandatory"])
    print(f"{args.out}: {len(controls)} controls, {total} bound artefacts, "
          f"binding sha256 {doc['sha256'][:12]}")
    for d in sorted(by_dim):
        print(f"  {d}: {by_dim[d][0]} controls, {by_dim[d][1]} artefacts")
    # Duplicate EV ids reused across controls would mean one artefact is doing
    # double duty -- legal, but worth seeing.
    seen = {}
    for cid, c in controls.items():
        for e in c["mandatory"]:
            seen.setdefault(e, []).append(cid)
    reuse = {e: v for e, v in seen.items() if len(v) > 1}
    print(f"  artefacts bound to >1 control: {len(reuse)}")
    for e, v in sorted(reuse.items()):
        print(f"    {e}: {', '.join(v)}")


if __name__ == "__main__":
    main()
