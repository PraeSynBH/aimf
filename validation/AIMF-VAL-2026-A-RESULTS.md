# Instrument validation record — case AIMF-VAL-2026-A

**Result: 51/72 controls agreed (70.8%) on the anchor set in this version. The 72/72 target in
requirement A3 is not met.** Measured 2026-10-18, four runs, one frozen evidence pack.

This record exists because an unmeasured claim of reproducibility is worthless. It contains the
runs, the disagreements, the adjudications and the parts that failed.

---

## 1. What was measured

Whether two assessors, given the same evidence and the same instrument, produce the same score for
the same control — requirement **A3 (scoring reproducibility)** in STARTINGPOINT §4.1.

The instrument is the shipped question bank plus the Scoring Protocol:

- `implementation/AIMF-ASSESSMENT-QUESTION-BANK.csv` — 72 controls, 5 behavioural anchors each
  (sha256 `afd2bbbaa4a93b36ea914da842e7ba373fb80555b60a7684369280a7ced9977a` for the anchor set
  scored in run 4).
- `implementation/AIMF-ASSESSMENT-GUIDE.md` → **Scoring Protocol P1-P7** — evidence sufficiency,
  the coverage / cadence / measure / one-clause tests, the two-level rule, the `NA` verdict, blind
  double scoring and adjudication.

## 2. Method

| Element | Value |
|---|---|
| Case | `AIMF-VAL-2026-A-EVIDENCE-PACK.md`, frozen before scoring; sha256 `c643fd60d973aa043331c7d10ce48949f314c0218ed966edd7a5a6fae8121b0e` |
| Case content | 72 controls, 2-4 dated artefacts each, one organisation (Calder Ridge Health Plan), B2 baseline, 14 AI systems in scope |
| Assessors | A: `anthropic/claude-sonnet-5.5`; B: `openai/gpt-4.1` — separate sessions, no shared context, neither saw the other's sheet |
| Extra sessions | independent repeats of the same protocol on other models, used to test whether divergence is reader-specific and as the third adjudicator (never having seen A or B) |
| Output per control | score or `NA`, deciding artefact, failing clause, boundary note |
| Agreement | identical score, or `NA` with the same reason code |
| Adjudication | protocol P5 rules 1-4, mechanically where the rule decides, by the third independent session where it does not |

## 3. Result

### 3.1 Four runs, same case

| Run | Instrument | Scoring brief | Agreement |
|---|---|---|---|
| 1 | v1.0.6 anchors | P1 without the four tests | 50/72 (69.4%) |
| 2 | v1.0.6 anchors | P1 plus coverage, cadence, measure and one-clause tests | 44/72 (61.1%) |
| 3 | v1.0.6 anchors | run-2 protocol plus a clause-by-clause scoring brief | 45/72 (62.5%) |
| **4** | **anchors with the level 1↔2 rewrite for 12 controls** | run-3 protocol, unchanged | **51/72 (70.8%)** |

Run 4 changed exactly one input — the anchor text for 12 controls. Agreement on those 12 moved
from **0/12 to 6/12**; agreement on the 60 untouched controls stayed at **45/60 (75.0%)**. The
judgement moved where the text changed and nowhere else. That is the argument for rewriting anchors
rather than adding more procedure.

### 3.2 Divergence is in the instrument, not the reader

Run-3 checks, all on the same frozen pack:

| Pair | Agreement | Rate |
|---|---|---|
| A - B (cross-vendor) | 45/72 | 62.5% |
| Same model, two independent sessions | 43/72 | 59.7% |
| A - D1 | 44/72 | 61.1% |
| A - D2 | 33/72 | 45.8% |
| B - D1 | 46/72 | 63.9% |
| B - D2 | 50/72 | 69.4% |

A same-model pair agreed no better than the cross-vendor pair, so "different vendors read
differently" does not explain the gap.

### 3.3 Disagreements and adjudication (run 4)

21 disagreements: 9 resolved by rule 1 (same deciding artefact, lower score stands), 8 by rule 2
(third adjudicator's score stands), 3 by rule 3 (two levels apart, mandatory adjudication), 1 by
rule 4 (`NA` vs numeric). **All 21 resolved; none left unresolved.** Final scores over those 21:
3 at 0, 7 at 1, 7 at 2, 3 at 3, 1 at 4. The adjudication table is
`validation/run4/comparison-adjudicated.md`.

## 4. Diagnosis

1. **The level 1↔2 boundary carries almost all of the damage.** 17 of the 21 remaining
   disagreements differ by exactly one level, and 12 of them sit on the 1↔2 edge. Level 2 asks for
   the artefact "in force organization-wide"; the evidence an assessor actually meets is nearly
   always *mostly* in force.
2. **Protocol definitions do not fix anchor wording.** Runs 2 and 3 added the coverage, cadence and
   measure tests to the protocol and the rate did not move (69.4% → 61.1% → 62.5%), because the
   anchors that use those words did not carry the definitions. Rewriting the anchors (run 4) is the
   first change that moved the number.
3. **The controls that stay judgemental are named, not excused.** 18 controls disagreed in both run
   3 and run 4: `GOV-1.3`, `GOV-1.4`, `GOV-2.3`, `GOV-3.2`, `GOV-5.2`, `MAN-3.2`, `MAN-4.2`,
   `MAP-1.3`, `MAP-3.5`, `MEA-1.1`, `MEA-2.1`, `MEA-2.11`, `MEA-2.2`, `MEA-2.4`, `MEA-2.6`,
   `MEA-2.8`, `MEA-3.1`, `MEA-4.3`. Nine are in the MEASURE dimension, which is the next anchor
   rewrite.

## 5. What this means

- **A3 is not met.** 70.8% against a 72/72 target and a 90% published threshold. The assessment must
  not be sold as reproducible on this anchor set.
- **The instrument is specified and enforced, not validated.** 360 anchors, the Scoring Protocol
  P1-P7, the `NA` verdict and validator enforcement now exist and ship; what is missing is anchor
  wording that removes the 1↔2 judgement, and that is now a measured, targeted job rather than a
  guess.
- **The next pass is MEASURE anchors.** Nine of the eighteen controls that disagree in every run are
  MEA; rewriting those first gives the largest measured gain per unit of writing.

## 6. Limits of this measurement

- **Models, not humans.** Independent model sessions are a reproducible proxy and a lower bound on
  ambiguity, not two trained human assessors. The first human double-scoring should be run on the
  next real engagement and recorded in this format.
- **The case is deliberately mid-band.** The evidence pack was written with realistic partial
  artefacts, so many controls sit on the 1↔2 boundary. The rate measures the difficult half of the
  instrument.
- **No dialogue.** A live assessor can ask the client a follow-up question; a frozen pack cannot,
  and some disagreements would have been settled by one question.
- **Calibration history.** Runs 2-4 changed the instrument after seeing the previous run's
  disagreements, so the four rates are not independent samples.
- **The anchor set is moving.** Run 4 measured the 12-control rewrite; further rewrites are
  unmeasured until the next run. Each figure describes the anchor text that was scored.

## 7. Reproduction

```bash
cd framework-and-training/validation
python3 score_pack.py --via hermes --model anthropic/claude-sonnet-5.5 \
    --assessor A --pack AIMF-VAL-2026-A-EVIDENCE-PACK.md --out scores-A.json
python3 score_pack.py --via hermes --model openai/gpt-4.1 \
    --assessor B --pack AIMF-VAL-2026-A-EVIDENCE-PACK.md --out scores-B.json
python3 compare_scores.py scores-A.json scores-B.json \
    --adjudicator scores-D1.json --json comparison-final.json --md comparison-final.md
```

Artifacts in `framework-and-training/validation/`: the frozen pack, the scoring sheets for every
session, the archived comparison output for each run, `run4/` (the level 1↔2 rewrite run) and
`verify_release.sh` (the P8 in-zip release gate).

**Disposition.** The remaining judgemental controls are carried by the next instrument-revision pass
(MEASURE first). Until a run scores at or above 90%, any assessment report produced with this
version must carry the sentence: *inter-rater agreement has been measured at 70.8% on the
validation case (2026-10-18); the instrument is not yet validated.*
