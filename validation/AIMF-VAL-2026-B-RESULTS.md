# AIMF held-out validation result — `AIMF-VAL-2026-B`

**Author:** CEO (Paperclip, PRA-6431 → PRA-6447)
**Date:** 2026-10-18 (runs 18:07–18:16Z; comparisons computed 18:50Z by the CEO from the raw score files)
**Requirement:** A10 (internal requirements document, not published, §4.1) — *no reproducibility number may be quoted externally until it is measured on a case the anchors were never written against, with both pair types.*
**Verdict:** **A10 is answered, and it fails on one of its two pair types.** Cross-vendor agreement on the held-out case is **43/72 (59.7%)**. Same-model, two-independent-session agreement is **65/72 (90.3%)**.

---

## 1. What was measured, and the integrity of the measurement

| Item | Value | How it was fixed |
|---|---|---|
| Fixture | `AIMF-VAL-2026-B` — Northwind Precision Components (precision manufacturing, B3 baseline, 3 plants, 6 registered AI systems) | pack committed in `dc0d8e1` at 11:01 PDT (18:01Z), **before any case-B score existed** |
| Pack sha256 | `2513cb0afe87a0f4a9b50192883529f8eaabe81223a3ec33eb742041414c6a91` | `dc0d8e1` message; identical in all four case-B score files |
| Question bank sha256 | `b6f9a6a19bfd25381657d33776812edf6f524e9ab9edd35727cb57c4600915bd` | identical in all six score files **and** in the shipped v1.0.9 / v1.0.10 zip → **zero anchor edits between freeze and scoring** |
| Scoring conditions | `temperature 0.0`, transport `openrouter`, 72/72 controls scored in every file, blind (assessors did not see each other's sheets) | score-file metadata, per-assessor batch logs `runB/log-*.txt` |
| Harness | `validation/compare_scores.py` (implements Scoring Protocol P4 agreement and P5 adjudication rules 1–4) **and** an independent recomputation by the CEO over the per-control `score` fields | both agree to the control |

Nothing about the instrument was changed for this run. The pack was frozen first, the scores are the first scores that exist for case B, and the bank is byte-identical to the one that shipped.

## 2. The four results that matter

| Case | Pair type | Models | Sessions | Agreement |
|---|---|---|---|---|
| **B (held-out)** | cross-vendor | `anthropic/claude-sonnet-5.5` vs `openai/gpt-4.1` | 1 each | **43/72 (59.7%)** — 29 disagreements |
| **B (held-out)** | same model, two sessions | `deepseek/deepseek-chat` | 2 independent | **65/72 (90.3%)** — 7 disagreements |
| A (fitting case) | same model, two sessions, **re-run on the current bank** | `deepseek/deepseek-chat` | 2 independent | **68/72 (94.4%)** — 4 disagreements |
| A (fitting case) | cross-vendor, on the current bank | as run 6 | 1 each | 65/72 (90.3%) — *fitted; carried forward from the v0.8 record, not re-measured here* |

Comparisons: `runB/comparison-BAB.{json,md}` (cross-vendor, shipped by the assessor harness), `runB/cmp-BD1BD2.{json,md}`, `runB/cmp-AD1AD2.{json,md}` (computed by the CEO this beat, kept beside the source sheets).

### 2.1 The headline finding: reproducibility is **model-family-scoped**

On the same held-out case, with the same pack and the same frozen bank:

- two **different vendors** agree on **59.7%** of controls;
- the **same model** in two independent sessions agrees on **90.3%**.

That gap (30.6 points) is the finding, not the individual numbers. The anchor library makes the instrument reproducible *within a toolchain* and much less so *across toolchains*. Two consequences follow directly:

1. **The cross-vendor number is unmoved by the remediation work.** The pre-fix in-sample cross-vendor results were 62.5% and 59.7% (run 3); the post-fix held-out cross-vendor result is 59.7%. Five anchor passes, 28 controls rewritten, three releases — and cross-vendor agreement on a fresh case is where it started. That is what fitting looks like from the outside: the in-sample number moved (62.5% → 90.3%), the held-out number did not.
2. **The within-model number is real, and it survived the held-out test.** `D1/D2` was the worst pair in the record at **43/72 (59.7%)** with a 26/44 core and had never been re-run. Re-run on the current bank it is **68/72 (94.4%)** on case A and **65/72 (90.3%)** on held-out case B. So the anchor work did buy something genuine: one model, given the same protocol, now reproduces its own judgement at ~90–94%, including on a case it was never tuned on.

### 2.2 What the 7 case-B within-model disagreements actually are

By adjudication rule: `{1: 4, 2: 3}` — four are rule-1 (differ by one level, same deciding artefact → lower score stands), three are rule-2 (different deciding artefacts → need a third adjudicator). **Four of the seven disagreements share the same deciding artefact**, i.e. the two sessions looked at the same evidence and reached different verdicts. That is judgement variance, not evidence dispute, and it is the kind that a delivered assessment has to absorb rather than argue.

Three controls (`GOV-5.2`, `MAN-3.2`, `MAP-2.3`) are **unresolved without an adjudicator**. For any per-control effort model this is the datum A9 was waiting for: **~4–10% of controls require adjudication** (7/72 observed, 3/72 requiring a third party), in addition to double-scoring all 72.

## 3. Verdicts against the written acceptance tests

| Requirement | Test as written | Result |
|---|---|---|
| **A3** reproducibility | 72/72 on a tagged, in-zip artifact with a fresh blind pair | **NOT MET.** Best held-out single-pair result is 65/72; best same-model result is 68/72 (case A). |
| **A10** held-out validation | ≥90% on **each** pair type | **NOT MET.** Same-model: 65/72 (90.3%, met by one control). Cross-vendor: 43/72 (59.7%, fails by 22 controls). |
| **A9** bounded effort | hours/control reconciled against one real engagement | Now estimable, not yet measured: 2×72 blind scores per engagement **plus** ~7 adjudication decisions per case. |

Neither requirement should be re-worded to fit the result. A3 and A10 stay open as written.

## 4. What this record supports, and what it does not

This follows directly from the measurement.

**May say** (held-out, cited): *"Two independent blind assessments produced by two PraeSyn assessors using the standard AIMF instrument and tooling agreed on 65 of 72 controls (90.3%) on a held-out case the instrument had never been applied to. Seven controls required adjudication; four of those were resolved by rule, three by a third assessor."*

**May say with care**: the same claim on `AIMF-VAL-2026-A` is 68/72 (94.4%) — but A is the case the anchors were fitted against, so it is a **regression figure, not a validation figure**, and must be labelled as such wherever it appears.

**May not say**: that "any two assessors agree", that the framework is "vendor-independent", or that AIMF assessments are "reproducible" without the within-toolchain qualifier. 59.7% cross-vendor on a held-out case is what would be measured against us.

**Scope consequence:** the same-model result is defensible **for a PraeSyn-delivered engagement using the standard instrument** — the 90.3% held-out same-model agreement supports exactly that. It is not defensible as an open-market, any-assessor instrument: the cross-vendor case measures 59.7% agreement, so a claim made outside the PraeSyn toolchain is not supported by this record.

**One number to stop using entirely:** 90.3% is met with a margin of **one control**, and the record's own run-to-run noise is **one control**. It is at the threshold, not above it, and it should be quoted as "65 of 72" with the adjudication tail attached, never as a percentage in a marketing line.

## 5. Open items this result creates

1. **A11 (new): cross-vendor reproducibility is a separate, unsolved problem.** If AIMF is ever delivered by a third party, or assessed by a regulator's choice of tool, ~60% agreement is the honest expectation. Either state that AIMF assessments are PraeSyn-toolchain-specific wherever the claim is made, or run targeted work on the ~29 cross-vendor disagreement classes — a remediation sized like the anchor programme (five passes, one release each), not a quick fix.
2. **Adjudication cost is now a real line in the delivery model** (§2.2) and belongs in the effort-per-control figure A9 asks for.
3. **The 44-control never-edited core is the most stable part of the instrument** — it was 95.5% reproducible cross-vendor before any editing — but §1 of the cross-vendor analysis shows that stability does not hold out of sample (27/44). The 28 rewritten controls are where the cross-vendor disagreement concentrates.
