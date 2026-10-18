# Instrument validation record — case AIMF-VAL-2026-A

**Result: 45/72 controls agreed (62.5%). The 72/72 target in requirement A3 is not met.**
Published as measured on 2026-10-18, against AIMF v1.0.6.

This record exists because an unmeasured claim of reproducibility is worthless. The run below is
the measurement, including the parts that failed.

---

## 1. What was measured

Whether two assessors, given the same evidence and the same instrument, produce the same score for
the same control — requirement **A3 (scoring reproducibility)** in STARTINGPOINT §4.1.

The instrument scored was the one shipped in v1.0.6:

- `implementation/AIMF-ASSESSMENT-QUESTION-BANK.csv` — 72 controls, 5 behavioural anchors each
  (sha256 `cc41c3d6e8d53c10c1ad5c724377a70cfd9c546d676e0c6c74f02a4e08b03773`).
- `implementation/AIMF-ASSESSMENT-GUIDE.md` → **Scoring Protocol P1-P6** — evidence sufficiency,
  the two-level rule, the `NA` verdict, blind double scoring and adjudication.

## 2. Method

| Element | Value |
|---|---|
| Case | `AIMF-VAL-2026-A-EVIDENCE-PACK.md`, frozen before scoring; sha256 `c643fd60d973aa043331c7d10ce48949f314c0218ed966edd7a5a6fae8121b0e` |
| Case content | 72 controls, 2-4 dated artefacts each, one organisation (Calder Ridge Health Plan), B2 baseline, 14 AI systems in scope |
| Assessors | A: `anthropic/claude-sonnet-5.5`; B: `openai/gpt-4.1` — separate sessions, no shared context, neither saw the other's sheet |
| Extra sessions | D1 and D2: `deepseek/deepseek-chat`, independent repeats of the same protocol (D1 doubles as the third adjudicator, having never seen A or B) |
| Output per control | score or `NA`, deciding artefact, failing clause, boundary note |
| Agreement | identical score, or `NA` with the same reason code |
| Adjudication | protocol P5 rules 1-4, mechanically where the rule decides, by the third independent session where it does not |

## 3. Result

### 3.1 Agreement across independent sessions

| Pair | Agreement | Rate |
|---|---|---|
| **A - B (the double-scoring pair)** | **45/72** | **62.5%** |
| A - D1 | 44/72 | 61.1% |
| A - D2 | 33/72 | 45.8% |
| B - D1 | 46/72 | 63.9% |
| B - D2 | 50/72 | 69.4% |
| D1 - D2 (same model, two sessions) | 43/72 | 59.7% |

Controls where all four sessions returned the same score: **23 of 72 (31.9%)**.

The same-model pair (D1-D2, two independent sessions of one model at temperature 0) agrees no
better than the cross-vendor pair. That rules out "different vendors read differently" as the
explanation: the divergence is in the instrument and the case, not in the reader's personality.

### 3.2 Disagreements and adjudication (A vs B)

27 disagreements: 9 resolved by rule 1 (same deciding artefact, lower score stands), 13 by rule 2
(third adjudicator's score stands), 3 by rule 3 (two levels apart, mandatory adjudication), 2 by
rule 4 (`NA` vs numeric). **All 27 resolved; none left unresolved.**

| Control | A | B | Rule | Final | Deciding artefacts (A / B) |
|---|---|---|---|---|---|
| GOV-1.1 | 1 | 2 | 2 | 2 | EV-016 / EV-014 |
| GOV-1.3 | 1 | 2 | 2 | 2 | EV-033 / EV-031 |
| GOV-1.4 | 2 | 3 | 1 | 2 | EV-044 / EV-044 |
| GOV-2.3 | 1 | 2 | 2 | 2 | EV-103 / EV-100 |
| GOV-3.2 | NA | 1 | 4 | 0 | — / EV-121 |
| GOV-5.2 | 1 | 0 | 2 | 0 | EV-171 / EV-170 |
| MAN-3.2 | 1 | 3 | 3 | 3 | EV-711 / EV-713 |
| MAN-4.2 | 2 | 3 | 1 | 2 | EV-732 / EV-732 |
| MAN-4.3 | 1 | 2 | 2 | 1 | EV-741 / EV-740 |
| MAP-1.3 | 1 | 2 | 1 | 1 | EV-221 / EV-221 |
| MAP-1.6 | 1 | 2 | 2 | 1 | EV-251 / EV-250 |
| MAP-2.2 | 2 | 1 | 2 | 2 | EV-271 / EV-270 |
| MAP-3.1 | 1 | 2 | 2 | 1 | EV-292 / EV-290 |
| MAP-3.2 | 1 | 2 | 2 | 1 | EV-301 / EV-300 |
| MAP-3.3 | 2 | 3 | 1 | 2 | EV-312 / EV-312 |
| MAP-3.4 | 1 | 2 | 2 | 1 | EV-322 / EV-320 |
| MAP-3.5 | 1 | 2 | 1 | 1 | EV-330 / EV-330 |
| MEA-1.1 | 2 | 3 | 1 | 2 | EV-403 / EV-403 |
| MEA-2.1 | 1 | 3 | 3 | 3 | EV-432 / EV-432 |
| MEA-2.11 | 1 | 2 | 2 | 3 | EV-534 / EV-533 |
| MEA-2.2 | NA | 0 | 4 | 0 | — / EV-440 |
| MEA-2.3 | 3 | 4 | 1 | 3 | EV-453 / EV-453 |
| MEA-2.4 | 2 | 4 | 3 | 3 | EV-462 / EV-463 |
| MEA-2.6 | 1 | 2 | 2 | 1 | EV-480 / EV-481 |
| MEA-2.8 | 2 | 1 | 1 | 1 | EV-500 / EV-500 |
| MEA-3.1 | 1 | 2 | 2 | 1 | EV-561 / EV-560 |
| MEA-4.3 | 2 | 3 | 1 | 2 | EV-612 / EV-612 |

Final distribution over the 27 disputed controls after adjudication: 3 at 0, 10 at 1, 9 at 2,
5 at 3.

## 4. Diagnosis

The run was repeated three times; the rate did not move, which is the useful finding.

| Run | Protocol / brief | Agreement |
|---|---|---|
| 1 | P1 v1 — no coverage, cadence or measure definitions | 50/72 (69.4%) |
| 2 | P1 v2 — four tests added (coverage, cadence, measure, one-artefact-one-clause) | 44/72 (61.1%) |
| 3 | P1 v2 + clause-by-clause scoring brief | 45/72 (62.5%) |

Three things the disagreements show:

1. **The level 1↔2 boundary carries almost all of the damage.** 41 of the 49 non-unanimous controls
   differ by exactly one level; 5 differ by two; 3 involve `NA`. The anchors describe level 2 as
   "the artefact in force organization-wide" but the evidence packs an assessor meets in practice
   is nearly always *mostly* in force. Whether "mostly" is 1 or 2 is the single largest source of
   variance in the instrument.
2. **The unstable words are `coverage`, `cadence`, `measure` and `defined`.** Adding definitions to
   the protocol (run 2) did not help, because the anchors that use those words do not themselves
   carry the definition — an assessor reading the anchor alone can still resolve them either way.
3. **This is not a reader artefact.** The same-model pair disagrees at the same rate as the
   cross-vendor pair (59.7% vs 62.5%).

## 5. What this means

- **A3 is not met.** The measured rate is 62.5% on the double-scoring pair, against a 72/72 target
  and a 90% published threshold. The assessment must not be sold as reproducible until a re-run
  passes.
- **The instrument is better than it was, but not yet decisive.** 360 anchors, a written protocol,
  a "not assessable" verdict and a validator that enforces coverage now exist — v1.0.5 had none of
  these. What is missing is anchor wording that removes the 1↔2 judgement, not more procedure.
- **The next pass is anchor work, not protocol work.** The controls to rewrite first are the 27 in
  §3.2, in this order: `GOV-1.1`, `GOV-2.3`, `MAN-4.3`, `MAP-1.6`, `MAP-3.1`, `MAP-3.2`,
  `MAP-3.4`, `MEA-2.6`, `MEA-3.1` (split 1 vs 2 in every run), then the `NA` cases
  (`GOV-3.2`, `MEA-2.2`, `MEA-2.7`).

## 6. Limits of this measurement

- **Models, not humans.** Four independent model sessions are a reproducible proxy and a lower bound
  on ambiguity. They are not two trained human assessors, and this record does not claim they are.
  The first human double-scoring should be run on the next real engagement and recorded in this
  format.
- **The case is deliberately mid-band.** The evidence pack was written with realistic partial
  artefacts, so many controls sit on the 1↔2 boundary. That makes the test hard rather than easy;
  it also means the 62.5% rate measures the difficult half of the instrument, not its average.
- **No dialogue.** A live assessor can ask the client a follow-up question; a frozen pack cannot.
  Some disagreements would have been resolved by one question (e.g. whether two planned engagement
  sessions were held).
- **Calibration history.** Runs 2 and 3 changed the protocol after seeing run 1's disagreements, so
  the three rates are not independent samples of the same instrument.
- **The anchors moved after the run.** The level 1↔2 anchors for 12 controls (`GOV-1.1`, `GOV-1.3`,
  `GOV-2.3`, `GOV-3.2`, `MAN-4.3`, `MAP-1.6`, `MAP-3.1`, `MAP-3.2`, `MAP-3.4`, `MEA-2.2`,
  `MEA-2.6`, `MEA-3.1`) were tightened after this measurement and are **unmeasured**. The 62.5%
  figure describes the anchor text that was scored, not the text now in the bundle; a re-run is the
  only thing that can move the number.

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

Artifacts in `framework-and-training/validation/`: the frozen pack, the scoring sheets for A, B,
D1 and D2 (plus the archived sheets from the three runs), `comparison-final.json` /
`comparison-final.md`, and `verify_release.sh` (the P8 in-zip release gate).

**Disposition.** Findings are carried by a follow-up instrument-revision issue (the 1↔2 anchor
wording on the controls listed in §5). Until that work lands and a fresh double-scoring passes,
any assessment report produced with this version must carry the sentence: *inter-rater agreement
has been measured at 62.5% on the validation case (2026-10-18); the instrument is not yet
validated.*
