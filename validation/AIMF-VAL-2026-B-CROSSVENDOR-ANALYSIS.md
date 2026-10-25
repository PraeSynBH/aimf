# AIMF cross-vendor analysis — what the held-out disagreement actually is

**Issued by:** CEO, issue PRA-6431 · **Date:** 2026-10-18
**Inputs (unchanged, committed):** `validation/run6/comparison.json` (case `AIMF-VAL-2026-A`, fitted case, `claude-sonnet-5.5` vs `gpt-4.1`, current bank `b6f9a6a1…15bd`), `validation/runB/comparison-BAB.json` (case `AIMF-VAL-2026-B`, held out, same vendor pair, same bank)
**Reproduce:** `python3 validation/runB/analyze_crossvendor_scope.py` (every figure below is that script's output; nothing is taken from a summary table)

This memo does not re-measure agreement — the 65/72 and 43/72 figures stand as published in `AIMF-VAL-2026-B-RESULTS.md`. It answers a question that record left open: **which claim the cross-vendor evidence actually supports, and what would have to change to support more.**

---

## 1. The v0.8 remedy is withdrawn: there is no 44-control safe core

The v0.8 revision of the internal requirements document (not published) proposed treating the "44-control core" — the controls whose anchors were never edited — as a separately attributable set. That proposal assumed the core's in-sample stability (95.5% → 97.7% across anchor passes) would carry out of sample. **It does not.**

| Control set | Agree on case A (fitted) | Agree cross-vendor on case B (held out) |
|---|---|---|
| 44 never-edited | 43/44 (97.7%) | **27/44 (61.4%)** |
| 28 rewritten | 22/28 (78.6%) | 14/28 (50.0%) |

Fisher one-sided **p = 0.24**. The never-edited controls are not materially more cross-vendor-reproducible than the ones that were rewritten — both fail on a case the instrument had not seen. Presenting "the 44-control core" as a separately attributable set would claim 44 controls and deliver 27.

**Only one scope is supported by both cases:** the **41 controls (56.9%, 95% CI 45.4–67.7%)** on which the same vendor pair agreed on case A *and* case B. Distribution: GOV 11/19, MAN 7/13, MAP 11/18, MEA 12/22 — the failure is spread across all four dimensions, so it cannot be presented as a weak dimension.

## 2. The disagreement is a leniency bias, not scatter

| Case | Disagreements | gpt-4.1 scored higher | claude-sonnet scored higher |
|---|---|---|---|
| A (fitted) | 7 | 6 | 1 |
| B (held out) | 29 | **26** | 1 |

One-sided binomial on case B: **p = 2.1 × 10⁻⁷**. If the two vendors were disagreeing symmetrically, this cannot happen. On this instrument **`gpt-4.1` is systematically the more generous assessor** — it reads an artefact's existence as meeting the level; `claude-sonnet-5.5` applies the countable coverage test and withholds the level.

## 3. A scalar vendor calibration does not fix it — tested, and it fails

The obvious remediation for a directional bias is a constant offset. Applied and measured, with `gpt-4.1` shifted down one rung (clamped 0–4): case A **65/72 → 6/72**, case B **43/72 → 19/72**. It destroys agreement, because most controls already agree on the same score and the shift moves them apart. **The bias is in the direction of the error, not in the level of the scale.** Recorded so that no one spends a release on a calibration table.

## 4. The mechanism is evidence selection, and it explains why anchor passes did not work

Extracting every `EV-` reference from each assessor's artefact field *and* its reasoning note:

| | n | Cited the identical evidence set | Mean Jaccard(evA, evB) |
|---|---|---|---|
| Controls that agree | 43 | **33** | 0.79 |
| Controls that disagree | 29 | **2** | 0.39 |

Fisher one-sided **p = 1.9 × 10⁻⁹**. Whether two vendors agree is very nearly a function of whether they looked at the same evidence. Where they agree they cite the same artefacts; where they split they are usually grading different artefacts from the same pack.

That is the missing piece in the v0.6 diagnosis. Three anchor passes rewrote the *level definitions* (22 of 28 rewritten controls still split on case B), while the actual divergence sits **upstream of the anchors, in which artefact the assessor selects to grade**. Anchor wording cannot fix a retrieval difference; binding the evidence per control can.

## 5. The recorded adjudication follows no rule

Of the 27 parseable case-B disagreements, the adjudicated `final` score equals the **lower** assessor score **12** times, the **higher** score **10** times, and **neither** 5 times. So the existing third-pass adjudication is genuine per-control judgement, not the application of `min`, `max`, or a documented tie-break. Five controls per engagement needed a human-style decision that no rule produced — an unmodelled cost in delivery.

Caveat, stated because it bounds the conclusion: this is **one** case pair per cell. It establishes a mechanism with large effect sizes; it does not establish a rate. A second held-out case would be needed before any of these numbers is quoted externally.

## 6. The ceiling of the fix — and what anchors are still for

Splitting the same 30 case-B controls that split, by whether both assessors recorded the **same primary deciding artefact**:

| | n | agree |
|---|---|---|
| Same primary artefact | 42 | **34 (81.0%)** |
| Different primary artefact | 30 | **9 (30.0%)** |

So evidence binding can move only the 30 different-artefact controls, and **8 controls split even when both sides read the same artefact** — `GOV-1.4, GOV-1.6, GOV-2.3, MAP-1.2, MAP-1.5, MAP-3.3, MAP-4.1, MEA-4.3`. Those eight are the only controls on which anchor wording is the binding constraint. Evidence binding alone therefore does not reach the 90% threshold; the remediation is two-part and each part is now sized: 30 controls of process work, 8 of anchor work.

---

## What this changes in the requirements

- **Withdrawn:** attributing the claim to the 44-control core (§7 of the internal requirements document, v0.8 text).
- **Replaced by:** the 41-control dual-case set as the only measured cross-vendor scope, labelled as *measured on two cases*, not as a guarantee.
- **D5(b) retargeted:** remediation is no longer "more anchor passes on the 29 split controls" — three passes moved in-sample only. The tested, mechanism-aligned option is **binding a mandatory evidence set per control in the case pack** and re-running case B blind. That is an instrument/process change, cheap to trial, and it has a falsifiable acceptance test.
- **A11 stays open.** Nothing here closes it; it names what closing it requires.
