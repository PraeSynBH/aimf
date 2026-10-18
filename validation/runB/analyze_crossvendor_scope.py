#!/usr/bin/env python3
"""A11 evidence: what the held-out cross-vendor disagreement actually is.

Reads only the committed comparison artifacts, never a summary table:
  validation/run6/comparison.json          case A (fitted),  claude-sonnet-5.5 vs gpt-4.1, current bank
  validation/runB/comparison-BAB.json      case B (held-out), same vendor pair, same bank

Emits, in order:
  1. the dual-case agreement set (agrees on BOTH cases) and its size
  2. the 44-never-edited vs 28-rewritten split measured on the held-out case
     (falsifies "scope the sold claim to the 44-control core")
  3. the direction of every disagreement (leniency bias vs symmetric scatter)
  4. whether a scalar vendor calibration would rescue agreement (it does not)
  5. whether the two sides graded the same evidence on the controls that split
  6. what the recorded adjudication actually did (min / max / neither)

Usage: python3 validation/runB/analyze_crossvendor_scope.py
"""
import csv
import json
import math
import os
import re
import subprocess
from typing import Optional, Tuple

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
BANK = 'documents/AIMF-Full-Documentation/implementation/AIMF-ASSESSMENT-QUESTION-BANK.csv'
BASE = 'f288b19'       # v1.0.6, the first bank with per-control anchors (pre-edit)
EDITED_AT = 'be653a7'  # v1.0.8, the last anchor rewrite
EV = re.compile(r'EV-\d+')


def load_rows(path):
    with open(os.path.join(ROOT, path)) as fh:
        d = json.load(fh)
    return d, {r['control']: r for r in d['rows']}


def edited_controls():
    def parse(sha):
        txt = subprocess.run(['git', '-C', ROOT, 'show', '%s:./%s' % (sha, BANK)],
                             capture_output=True, text=True, check=True).stdout
        return {r['control']: r for r in csv.DictReader(txt.splitlines())}
    a, b = parse(BASE), parse(EDITED_AT)
    anc = [c for c in next(iter(a.values())) if c.startswith('anchor_')]
    return {k for k in b if k in a and any(a[k][c] != b[k][c] for c in anc)}


def pair(row) -> Optional[Tuple[int, int]]:
    """(assessor A score, assessor B score) or None when either is NA/unparseable."""
    try:
        return int(row['A']), int(row['B'])
    except (KeyError, TypeError, ValueError):
        return None


def one_sided_binomial(k: int, n: int) -> float:
    return sum(math.comb(n, i) for i in range(k, n + 1)) / 2 ** n


def fisher(a, b, c, d):
    """One-sided Fisher exact, P(first cell >= observed)."""
    n = a + b + c + d
    def f(i):
        return math.comb(a + b, i) * math.comb(c + d, a + c - i) / math.comb(n, a + c)
    return sum(f(i) for i in range(a, min(a + b, a + c) + 1))


def wilson(k, n, z=1.96):
    p = k / n
    d = 1 + z * z / n
    c = p + z * z / (2 * n)
    m = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n))
    return (c - m) / d, (c + m) / d


def evidence_set(row, side):
    out = set()
    for key in ('%s_artefact' % side, '%s_note' % side):
        v = row.get(key)
        if v is None:
            continue
        out |= {str(x) for x in v} if isinstance(v, list) else set(EV.findall(str(v)))
    return out


def main():
    dA, ra = load_rows('validation/run6/comparison.json')
    dB, rb = load_rows('validation/runB/comparison-BAB.json')
    controls = sorted(ra)
    assert set(controls) == set(rb), 'control sets differ between cases'

    both = [c for c in controls if ra[c]['agree'] and rb[c]['agree']]
    a_only = [c for c in controls if ra[c]['agree'] and not rb[c]['agree']]
    ci = wilson(len(both), 72)
    print('1. agreement sets')
    print('   case A (fitted)   %d/72 = %.1f%%' % (dA['summary']['agree'], 100 * dA['summary']['agreement_rate']))
    print('   case B (held-out) %d/72 = %.1f%%' % (dB['summary']['agree'], 100 * dB['summary']['agreement_rate']))
    print('   agree on BOTH     %d/72 = %.1f%%   95%% CI %.1f-%.1f%%'
          % (len(both), 100 * len(both) / 72, 100 * ci[0], 100 * ci[1]))
    print('   case-A only       %d' % len(a_only))
    for dim in ('GOV', 'MAN', 'MAP', 'MEA'):
        t = [c for c in controls if c.startswith(dim)]
        g = [c for c in both if c.startswith(dim)]
        print('     %s %d/%d' % (dim, len(g), len(t)))

    edited = edited_controls()
    never = set(controls) - edited
    print('\n2. 44-never-edited vs 28-rewritten, measured on the HELD-OUT case')
    print('   edited controls found by diffing the bank %s..%s: %d' % (BASE, EDITED_AT, len(edited)))
    nb = len(set(both) & never)
    eb = len(set(both) & edited)
    print('   never-edited agree on both cases %d/%d = %.1f%%' % (nb, len(never), 100 * nb / len(never)))
    print('   rewritten    agree on both cases %d/%d = %.1f%%' % (eb, len(edited), 100 * eb / len(edited)))
    print('   Fisher one-sided p = %.2f  -> the core is NOT materially better out of sample'
          % fisher(nb, len(never) - nb, eb, len(edited) - eb))
    print('   never-edited controls that split on B: %s'
          % ', '.join(sorted(never - set(both))))

    print('\n3. direction of disagreement (A=claude-sonnet-5.5, B=gpt-4.1)')
    for label, rows in (('case A', ra), ('case B', rb)):
        dis = [c for c in rows if not rows[c]['agree']]
        pairs = [p for p in (pair(rows[c]) for c in dis) if p]
        hi = sum(1 for a, b in pairs if b > a)
        lo = sum(1 for a, b in pairs if a > b)
        print('   %s: %d disagreements, gpt-4.1 higher %d, claude higher %d' % (label, len(dis), hi, lo))
    pairs = [p for p in (pair(rb[c]) for c in rb if not rb[c]['agree']) if p]
    hi = sum(1 for a, b in pairs if b > a)
    print('   case B one-sided binomial p = %.2e (symmetric scatter rejected)'
          % one_sided_binomial(hi, len(pairs)))

    print('\n4. would a scalar vendor calibration fix it?  (shift gpt-4.1 by -1, clamp 0..4)')
    for label, rows in (('case A', ra), ('case B', rb)):
        scored = [p for p in (pair(rows[c]) for c in rows) if p]
        fixed = sum(1 for a, b in scored if a == max(0, min(4, b - 1)))
        raw = sum(1 for c in rows if rows[c]['agree'])
        print('   %s: %d/72 after shift (raw %d/72) -> a constant offset makes it worse, '
              'because most controls already agree' % (label, fixed, raw))

    print('\n5. did the two sides grade the same evidence?')
    ident_by_group = {}
    for label, subset in (('agreements', [c for c in rb if rb[c]['agree']]),
                          ('disagreements', [c for c in rb if not rb[c]['agree']])):
        ident = 0
        jac = []
        for c in subset:
            a, b = evidence_set(rb[c], 'A'), evidence_set(rb[c], 'B')
            if not a or not b:
                continue
            if a == b:
                ident += 1
            jac.append(len(a & b) / len(a | b))
        ident_by_group[label] = (ident, len(subset))
        print('   %-13s n=%2d identical evidence %2d  mean Jaccard %.2f'
              % (label, len(subset), ident, sum(jac) / len(jac)))
    ag, agn = ident_by_group['agreements']
    dg, dgn = ident_by_group['disagreements']
    print('   Fisher identical-evidence agreements vs disagreements p = %.2e'
          % fisher(ag, agn - ag, dg, dgn - dg))

    print('\n6. what the recorded adjudication actually did')
    fmin = fmax = fneither = 0
    for c in rb:
        if rb[c]['agree']:
            continue
        p = pair(rb[c])
        try:
            final = int(rb[c]['final'])
        except (KeyError, TypeError, ValueError):
            continue
        if not p:
            continue
        a, b = p
        if final == min(a, b):
            fmin += 1
        elif final == max(a, b):
            fmax += 1
        else:
            fneither += 1
    print('   final == lower score %d, == higher score %d, neither %d (of %d parseable)'
          % (fmin, fmax, fneither, fmin + fmax + fneither))


if __name__ == '__main__':
    main()
