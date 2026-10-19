#!/usr/bin/env python3
"""Did binding the evidence set move cross-vendor agreement? (D5(b), case B)

Compares the unbound cross-vendor pair (runB/scores-BA.json vs scores-BB.json)
with the bound pair (runB/scores-BA-bind.json vs scores-BB-bind.json) on the
frozen pack AIMF-VAL-2026-B.

Reads only the per-control `score` and `deciding_artefact` fields of the four
sheets plus the frozen comparison written by compare_scores.py; it never trusts a
summary table for a number it can recompute.

Reported:
 - overall agreement, both ways
 - agreement on the 29 unbound split controls (the D5(b) acceptance population)
 - artefact-identity rate (did the two vendors name the same deciding artefact),
   which is the mechanism the binding targets
 - binding compliance (deciding artefact inside the mandatory set)
 - exact McNemar / sign test on the paired change, because 72 controls is small

Usage: python3 analyze_binding.py
"""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))


def load(name):
    return json.load(open(os.path.join(HERE, name)))


def scores(sheet):
    return {c: v for c, v in sheet["scores"].items()}


def pair(a, b):
    out = {}
    for c in sorted(set(a) & set(b)):
        sa, sb = a[c]["score"], b[c]["score"]
        out[c] = {
            "a": sa, "b": sb,
            "agree": sa == sb,
            "art_a": a[c].get("deciding_artefact", ""),
            "art_b": b[c].get("deciding_artefact", ""),
            "same_art": a[c].get("deciding_artefact", "") == b[c].get("deciding_artefact", ""),
        }
    return out


def exact_binom_two_sided(k, n):
    """Two-sided exact binomial test against p=0.5 for k successes of n."""
    from math import comb
    if n == 0:
        return 1.0
    pmf = [comb(n, i) / 2 ** n for i in range(n + 1)]
    obs = pmf[k]
    return min(1.0, sum(p for p in pmf if p <= obs + 1e-12))


def main():
    ba, bb = load("scores-BA.json"), load("scores-BB.json")
    bad, bbd = load("scores-BA-bind.json"), load("scores-BB-bind.json")

    unbound = pair(scores(ba), scores(bb))
    bound = pair(scores(bad), scores(bbd))

    if set(unbound) != set(bound):
        sys.exit(f"control sets differ: {set(unbound) ^ set(bound)}")

    n = len(bound)
    ua = sum(1 for r in unbound.values() if r["agree"])
    b_agree = sum(1 for r in bound.values() if r["agree"])
    ua_art = sum(1 for r in unbound.values() if r["same_art"])
    b_art = sum(1 for r in bound.values() if r["same_art"])

    splits = [c for c, r in unbound.items() if not r["agree"]]
    fix = [c for c in splits if bound[c]["agree"]]
    broke = [c for c, r in unbound.items() if r["agree"] and not bound[c]["agree"]]
    shift = len(fix) - len(broke)

    print(f"controls: {n}")
    print(f"unbound cross-vendor agreement : {ua}/{n} ({ua/n:.1%})")
    print(f"bound   cross-vendor agreement : {b_agree}/{n} ({b_agree/n:.1%})")
    print(f"  fixed by binding  ({len(fix)}): {', '.join(fix) if fix else '-'}")
    print(f"  broken by binding ({len(broke)}): {', '.join(broke) if broke else '-'}")
    print(f"  paired change: {shift:+d}, exact two-sided sign test p = "
          f"{exact_binom_two_sided(min(len(fix), len(broke)), len(fix)+len(broke)):.4f}"
          f" (ties excluded, n={len(fix)+len(broke)})")
    print()
    print(f"same deciding artefact, unbound: {ua_art}/{n} ({ua_art/n:.1%})")
    print(f"same deciding artefact, bound  : {b_art}/{n} ({b_art/n:.1%})")
    print()
    print(f"D5(b) acceptance population = the {len(splits)} unbound splits:")
    print(f"  agreement on those controls: "
          f"{sum(1 for c in splits if bound[c]['agree'])}/{len(splits)}")
    for c in splits:
        r, q = unbound[c], bound[c]
        mark = "AGREE-NOW" if q["agree"] else "still split"
        print(f"  {c:9s} unbound {r['a']}v{r['b']} ({r['art_a']} / {r['art_b']}) -> "
              f"bound {q['a']}v{q['b']} ({q['art_a']} / {q['art_b']})  {mark}")

    for label, sheet in (("BA-bind", bad), ("BB-bind", bbd)):
        b = sheet.get("binding") or {}
        v = b.get("violations") or []
        print(f"\n{label}: {sheet['controls_scored']}/{n} scored, binding sha "
              f"{b.get('sha256','')[:12]}, violations {len(v)}"
              + (f" {v}" if v else ""))


if __name__ == "__main__":
    main()
