# Instrument validation record — case AIMF-VAL-2026-A

**Current result (v1.0.8): 65/72 controls agreed (90.3%). The ≥90% publication threshold in P6 is met.**
**The 72/72 target in requirement A3 is not met.** Baselines on the same case and harness:
**v1.0.6 45/72 (62.5%)**, **v1.0.7 51/72 (70.8%)**.

Published as measured on 2026-10-18. §1-§7 record the v1.0.6 measurement and its diagnosis, §8 the
v1.0.7 re-run, §9 the first v1.0.8 pass (87.5%) and §10 the second (90.3%). All of them are published
because the sequence is the evidence: three anchor rewrites under one edit rule moved agreement from
62.5% to 90.3%, and no change to the protocol text moved it at all.

This record exists because an unmeasured claim of reproducibility is worthless. The runs below are
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

**Disposition.** The 1↔2 anchor wording for the controls named in §8.4 was carried by the follow-up
instrument-revision pass recorded in §9-§10. The not-validated sentence applied to the v1.0.6 and
v1.0.7 anchor sets; it is discharged for v1.0.8 at 65/72 (90.3%), and it must be reinstated for any
later version whose own double-scoring falls below the P6 threshold.

---

## 8. Run 4 — the v1.0.7 anchors (2026-10-18)

### 8.1 What changed, and only that

Run 4 repeats run 3 exactly — same frozen case (`AIMF-VAL-2026-A`, sha256 `c643fd60…121b0e`), same
models (`anthropic/claude-sonnet-5.5` as A4, `openai/gpt-4.1` as B4), same scoring brief, same
harness (`score_pack.py`), temperature 0. The single input that changed is the anchor text of 12
controls, edited in `implementation/AIMF-ASSESSMENT-QUESTION-BANK.csv`:

> `GOV-1.1`, `GOV-1.3`, `GOV-2.3`, `GOV-3.2`, `MAN-4.3`, `MAP-1.6`, `MAP-3.1`, `MAP-3.2`,
> `MAP-3.4`, `MEA-2.2`, `MEA-2.6`, `MEA-3.1`

The edit applies one rule to every one of them. Anchor 1 now states which **countable** test the
artefact fails — coverage of the population in the dated scope register, approval and currency, or a
named missing element — and anchor 2 states the same artefact passing those tests with no open
exception. The words *partial*, *unevenly* and *comprehensive* were removed from the level-1 and
level-2 cells, because those were the words the assessors were splitting on.

New anchor set: `implementation/AIMF-ASSESSMENT-QUESTION-BANK.csv`, sha256
`afd2bbbaa4a93b36ea914da842e7ba373fb80555b60a7684369280a7ced9977a`.

### 8.2 Result

| Measure | Run 3 (v1.0.6 anchors) | Run 4 (v1.0.7 anchors) |
|---|---|---|
| Agreement, A vs B | 45/72 (62.5%) | **51/72 (70.8%)** |
| Disagreements | 27 | 21 |
| Differ by one level | 41 of 49 non-unanimous | 17 of 21 |
| On the 1↔2 edge | dominant | 12 of 21 |
| Adjudicated, none unresolved | 27/27 | 21/21 |
| **Agreement, the 12 rewritten controls** | **0/12 (0.0%)** | **6/12 (50.0%)** |
| **Agreement, the 60 untouched controls** | **45/60 (75.0%)** | **45/60 (75.0%)** |

The control group is what makes this a finding rather than a fluctuation: the untouched 60 scored
identically in both runs, so the +8.3 point movement is attributable to the 12 rows whose text
changed, and to nothing else in the instrument.

### 8.3 Adjudication (run 4)

All 21 disagreements adjudicated under P5, third session `deepseek/deepseek-chat` (D4), which never
saw A4 or B4: rule 1 → 9, rule 2 → 8, rule 3 → 3, rule 4 → 1. **None left unresolved.** Final
distribution over the 21 disputed controls: 3 at 0, 7 at 1, 7 at 2, 3 at 3, 1 at 4.

### 8.4 What still disagrees, and why

Eighteen controls disagreed in both runs — these are the instrument's remaining judgement, listed
rather than averaged away:

| Boundary | Controls |
|---|---|
| 1 ↔ 2 | `GOV-1.3`, `GOV-2.3`, `MAN-1.1`, `MAN-3.2`, `MAN-4.2`, `MAP-1.3`, `MAP-3.5`, `MEA-2.6`, `MEA-2.8`, `MEA-2.11`, `MEA-3.1`, `MEA-3.3` |
| 2 ↔ 3 / 3 ↔ 4 | `GOV-1.4`, `MEA-1.2`, `MEA-2.1`, `MEA-2.4`, `MEA-4.3` |
| `NA` vs numeric | `GOV-3.2`, `MEA-2.2` |

Nine of the eighteen are in the MEA dimension. Two patterns carry most of the residual: assessors
reading the *same* artefact entry and reaching different levels because the entry itself bundles a
measurement with a governance decision (e.g. `GOV-1.3`: an approved appetite statement exists, but
whether it covers every risk category in the register is not stated in the pack), and cases where
the pack's evidence is a single artefact that could evidence either clause (`MEA-2.8`).

### 8.5 What this licenses

- The instrument is **not** validated: 70.8% against a 90% publication threshold and a 72/72 target.
- The direction of the fix is now evidenced, not assumed: anchor wording moves agreement and
  protocol wording does not (runs 2 and 3 vs run 4). The next pass is the same edit on the MEA
  dimension and the 2↔3 clause, not more procedure.
- The probe carried by this run pointed at 18 named controls. Those are a pricing input: they can be
  sold as discovery, not as a fixed-price percentage, until they score decisively.

### 8.6 Reproduce run 4

```bash
cd framework-and-training/validation
python3 score_pack.py --via openrouter --model anthropic/claude-sonnet-5.5 \
    --assessor A4 --pack AIMF-VAL-2026-A-EVIDENCE-PACK.md --out run4/scores-A4.json
python3 score_pack.py --via openrouter --model openai/gpt-4.1 \
    --assessor B4 --pack AIMF-VAL-2026-A-EVIDENCE-PACK.md --out run4/scores-B4.json
python3 score_pack.py --via openrouter --model deepseek/deepseek-chat \
    --assessor D4 --pack AIMF-VAL-2026-A-EVIDENCE-PACK.md --out run4/scores-D4.json
python3 compare_scores.py run4/scores-A4.json run4/scores-B4.json \
    --adjudicator run4/scores-D4.json --json run4/comparison-adjudicated.json \
    --md run4/comparison-adjudicated.md
```

Sheets, logs and the comparison are in `framework-and-training/validation/run4/`. The anchor edit is
reproducible from `framework-and-training/validation/fix_1_2_boundary_anchors.py`, which contains
the exact before/after text for all 12 controls.

---

## 9. Run 5 — the v1.0.8 first pass, the 21 controls that still split (2026-10-18)

### 9.1 What changed

Run 5 applied the run-4 edit rule to every control that still split in run 4: **21 controls**, chosen
from the run-4 adjudication table rather than from a hypothesis.

| Boundary | Controls |
|---|---|
| 1 ↔ 2 (12) | `GOV-1.3`, `GOV-2.3`, `MAN-1.1`, `MAN-3.2`, `MAN-4.2`, `MAP-1.3`, `MAP-3.5`, `MEA-2.6`, `MEA-2.8`, `MEA-2.11`, `MEA-3.1`, `MEA-3.3` |
| 2 ↔ 3 / 3 ↔ 4 (6) | `GOV-1.4`, `MEA-1.1`, `MEA-1.2`, `MEA-2.1`, `MEA-2.4`, `MEA-4.3` |
| `NA` vs numeric (2) | `GOV-3.2`, `MEA-2.2` |
| 0 ↔ 1 (1) | `GOV-5.2` |

The rule was unchanged from run 4: anchor 1 names the countable test the artefact fails (a stated
population not fully covered, a dated record missing for one member of it, or a required element
absent), anchor 2 names the same artefact passing every one of those tests. Anchor 0 was edited for
`GOV-3.2`, `MEA-2.2` and `GOV-5.2` because those splits were 0↔1 or `NA`↔0 and the level-0 clause
itself was the ambiguous one.

Two of the card's named defects were fixed where they occur: the bundled measurement-plus-decision
(`GOV-1.3`, anchor 2 now names the appetite statement as the artefact that settles category coverage
and the dated register entry that settles escalation) and one artefact evidencing either clause
(`MEA-2.8`, anchor 2 now names two artefacts and requires both).

Bank sha256 after the edit: `872d4b7a968f1231…`. Nothing outside those 21 rows and the generated
question-bank table changed.

### 9.2 Result

| Measure | Run 4 (v1.0.7) | Run 5 (pass 1) |
|---|---|---|
| Agreement | 51/72 (70.8%) | **63/72 (87.5%)** |
| Disagreements | 21 | 9 |
| Delta histogram | — | 0: 63, 1: 7, 2: 2, `NA` mismatch: 0 |
| The 21 edited controls | 13/21 | **13/21** |
| The 51 untouched controls | 50/51 | **50/51 (98.0%)** |
| Unresolved after adjudication | none | none |

9 disagreements, adjudicated under P5: 3 by rule 1, 4 by rule 2, 2 by rule 3. Final scores over those
9: one 0, three 1, three 2, one 3, one 4. Sheet and comparison: `validation/run5/`.

The control group did not move (50/51 both runs), so the 12-control movement is attributable to the
21 edited rows. Pass 1 fixed 13 of run 4's 21 splits and produced one new one (`MAP-2.2`, unedited
and agreeing in run 4), leaving 9 and 87.5% — three controls short of the 90% threshold, which is why
a second pass was run rather than the number being published as final.

### 9.3 The nine that still split, and why

| Control | Cause in the anchor text |
|---|---|
| `MEA-2.1`, `MEA-1.2`, `MAN-4.2` | **clause blending** — anchor 2 required a level-3 measure ("a third party could rerun it", "revision history", "measured effect per release"), so one reader scored 1 where the other scored 2 |
| `MEA-2.4`, `MEA-4.3` | **unreachable rung** — one reader scored level 4 (resp. 3) from a top-rung artefact while the rung below was unevidenced |
| `MAP-2.2`, `MEA-2.6` | **population not stated** — anchor 2 said "every system" in one control and not in the other |
| `MAP-1.3` | **assertion vs minute** — an asserted annual cadence was read as satisfying an anchor that requires a minuted review |
| `GOV-5.2` | **absence boundary** — level 0 said "no collaboration of any kind" while the pack contains informal individual contact, which is what level 1 describes |

## 10. Run 6 — the v1.0.8 second pass, final measurement (2026-10-18)

### 10.1 What changed

Nine rows, one per cause in §9.3. No protocol text (P1-P6) was touched, in either pass.

Bank sha256 after the edit: `b6f9a6a19bfd25381657d33776812edf6f524e9ab9edd35727cb57c4600915bd`.

### 10.2 Result

| Measure | Run 5 | **Run 6 (final)** |
|---|---|---|
| Agreement | 63/72 (87.5%) | **65/72 (90.3%)** |
| Disagreements | 9 | **7** |
| Delta histogram | 0: 63, 1: 7, 2: 2 | **0: 65, 1: 6, 2: 1** |
| The 21 edited controls | 13/21 | **15/21** |
| The 51 untouched controls | 50/51 | **50/51 (98.0%)** |
| Unresolved after adjudication | none | **none** |

7 disagreements, adjudicated under P5: 3 by rule 1, 3 by rule 2, 1 by rule 3. Final scores over those
7: one 0, three 1, two 3, one 4. **Adjudication survival: 7/7 resolved; 2 of the 7 adjudicated to a
score neither assessor gave** (`MAN-2.4` → 3 against 1 and 2; `MEA-2.1` → 3 against 1 and 2), which
is the residual signal that those two anchors still carry a judgement. Sheets and comparison:
`validation/run6/`.

Three controls were fixed by pass 2 (`MAP-1.3`, `MAP-2.2`, `MEA-1.2`); six split in both passes.

### 10.3 The seven that still split, and the rule a third assessor would apply

| Control | A | B | Rule | Final | The rule a third assessor would apply |
|---|---|---|---|---|---|
| `GOV-5.2` | 1 | 0 | 2 | 0 | Level 0 needs the pack to show **no** academic contact of any kind. Where a named researcher has a dated record of external university correspondence (`EV-171`), the score is 1 even though a summary entry (`EV-170`) states a general absence — the level-1 clause describes informal individual contact exactly. |
| `MAN-2.4` | 1 | 2 | 2 | 3 | Level 2 needs named shutdown responsibility for **each** system in the dated scope register, not only the one whose runbook is in the pack: responsibility evidenced for a subset is 1 even where mechanisms and tests cover all systems. A drill metric with a value and a target but **no named reporting body and no stated cadence** is 2, not 3. |
| `MAN-4.2` | 1 | 2 | 1 | 1 | Level 2 is the **citation** test: every release in the dated log cites the finding that triggered it. Measured-effect coverage (7 of 9 releases) is the level-3 test and must not be used to withhold level 2; a release with no cited finding is level 1. |
| `MEA-2.1` | 1 | 2 | 2 | 3 | Count the register. Level 2 is 2 only when the number of evaluations carrying a complete manifest (dataset version, environment, seed, metric code) **equals** the number in the register. Where an audit records a defect against 3 of 12 runs, 9/12 carry manifests and the score is 1; the 9/12 reproducibility share is a level-3 artefact and cannot lift a failed level 2. |
| `MEA-2.4` | 2 | 4 | 3 | 4 | Level 4 is unreachable without the level-3 dated report: detection precision, recall and alert-to-action time **per monitored system**, reviewed by a named body at a stated cadence. A threshold change dated **before** the incident said to motivate it, with no per-system report, is level 2. |
| `MEA-2.6` | 1 | 2 | 1 | 1 | Level 2 needs the count of systems carrying a safety evaluation to **equal** the count in the dated scope register, and every residual risk to carry an accepting role **and** date. Fail-safe testing on some systems plus residual-risk entries with no acceptance date is level 1. |
| `MEA-4.3` | 1 | 2 | 1 | 1 | Level 2 needs every detected change in the dated change log to carry a root-cause analysis and a corrective action. Where the pack reports 6 systems with documented change events against 2 declines and does not reconcile them, the count is not shown complete: level 1. A median latency with no stated target and no named reviewing body is a level-3 failure and cannot lift it. |

### 10.4 What this licenses, and what it does not

- **Licensed:** the ≥90% threshold in P6 is met on this case, `65/72 (90.3%)`, with every
  disagreement adjudicated and none unresolved. The guide's P7 states that result and no longer
  carries the not-validated sentence.
- **Not licensed:** a claim of 72/72. Seven controls still split. One of them (`MAN-2.4`) was edited
  in neither pass and split only in run 6, which puts the run-to-run noise of this harness at about
  one control — so the margin over 90% is inside that noise. The honest statement is "measured at
  65/72 on one case", not "reproducible".
- **Not a claim about humans.** Both assessors are model sessions. This remains a lower bound on
  ambiguity for trained human assessors, and the first human double-scoring is still owed.
- **The measurement is of this anchor set.** Any later anchor edit invalidates the number until it is
  re-run. Each figure in this record describes the text that was scored.

### 10.5 Reproduce runs 5 and 6

```bash
cd framework-and-training/validation
# pass 1 and pass 2 anchor edits (exact before/after text for every row)
python3 fix_disputed_anchors_v2.py
python3 fix_split_anchors_v3.py

# one fresh session per assessor; A/B are the blind pair, D adjudicates
python3 score_pack.py --via openrouter --model anthropic/claude-sonnet-5.5 \
    --assessor A6 --pack AIMF-VAL-2026-A-EVIDENCE-PACK.md --out run6/scores-A6.json
python3 score_pack.py --via openrouter --model openai/gpt-4.1 \
    --assessor B6 --pack AIMF-VAL-2026-A-EVIDENCE-PACK.md --out run6/scores-B6.json
python3 score_pack.py --via openrouter --model deepseek/deepseek-chat \
    --assessor D6 --pack AIMF-VAL-2026-A-EVIDENCE-PACK.md --out run6/scores-D6.json
python3 compare_scores.py run6/scores-A6.json run6/scores-B6.json \
    --adjudicator run6/scores-D6.json --json run6/comparison.json --md run6/comparison.md
```
