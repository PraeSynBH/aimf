# AIMF — D5(b) evidence-binding test on the held-out case: falsified

**Fixture**: AIMF-VAL-2026-B (frozen, pack sha256 `2513cb0a…6a91`)
**Question**: does binding a mandatory evidence set per control raise cross-vendor
reproducibility, as v0.10 proposed as the only surviving remediation?
**Answer**: no. Cross-vendor agreement fell from 43/72 (59.7%) to 41/72 (56.9%),
and the mechanism the fix targets — two vendors citing the same deciding artefact —
did not move at all (8/29 of the split controls before and after).
**Verdict on A11 / D5(b)**: the remediation is closed. D5 stays **(a) — disclaim**.

## What was built

An instrument change, not an anchor edit, exactly as v0.10 specified:

- `runB/evidence_binding.py` derives a per-control **mandatory evidence set**
  mechanically from the frozen pack — it reads the `- **EV-nnn**` bullets under each
  `### <control>` heading and nothing else, so the binding cannot be tuned against a
  score sheet. Output: `runB/evidence-bindings-B.json`, 72 controls, 246 artefacts,
  binding sha256 `aeb3bc10f802…`, no artefact bound to more than one control.
- `validation/score_pack.py` gains `--binding`: the assessor prompt now names the
  mandatory set per control and requires `deciding_artefact` to be a member; a
  decision taken from outside the set is recorded as a binding violation. The flag is
  refused if the binding's `pack_sha256` does not match the pack being scored, so a
  binding cannot be silently reused across packs.
- Compliance was **total**: 0 violations across all 144 control-decisions in the two
  bound runs. The assessors did what they were told. This is not a test of a rule that
  was ignored — it is a test of a rule that was followed and did not help.

Both bound runs are one fresh blind session per assessor, `temperature 0.0`,
`transport openrouter`, same pack hash `2513cb0a…6a91` as the original pair, bank
`b6f9a6a1…15bd` unchanged, so **no anchor was edited between the two measurements**.

## Result

| measurement | unbound pair | bound pair | change |
|---|---|---|---|
| cross-vendor agreement | **43/72 (59.7%)** | **41/72 (56.9%)** | −2 |
| controls fixed | — | 5 (4 real, 1 is NA/NA) | |
| controls broken | — | 7 | |
| paired sign test (ties excluded, n=12) | — | | **p = 0.77** |
| same deciding artefact, all 72 | 42 (58.3%) | 40 (55.6%) | −2 |
| same deciding artefact, the 29 splits | **8** | **8** | 0 |
| agreement where both cited the same artefact | 34/42 (81.0%) | 30/40 (75.0%) | −6.0 pts |
| agreement where they cited different artefacts | 9/30 (30.0%) | 11/32 (34.4%) | +4.4 pts |
| NA decisions (BA / BB) | 3 / 1 | 6 / 2 | +4 |
| mean score (BA / BB) | 1.46 / 1.93 | 1.45 / 1.89 | unchanged |

Recomputed twice: by `runB/analyze_binding.py` from the per-control `score` field, and
by `validation/compare_scores.py` (which reports the same 41/72 and 31 disagreements).
Both agree. Comparison artifact: `runB/comparison-BAB-bind.json`.

## What the numbers mean

**1. The binding did not bind.** On the population the fix was aimed at — the 29
controls that split without binding — the two vendors cited *the same* deciding
artefact on 8 controls both before and after. The intervention was designed to force
artefact convergence; artefact convergence is exactly what did not change.
The assessed scores moved around inside a still-different artefact choice.

**2. The movement it did cause is noise plus a nudge to `NA`.** Five splits resolved
and seven appeared, which is a coin flip (p = 0.77) — and one of the five is
`MEA-2.7`, where both assessors moved to `NA` (the red-team report is withheld by a
customer confidentiality agreement; that is the *correct* verdict and it is agreement
by refusal, not by reproducibility). `NA` decisions rose from 4 to 8 across the two
assessors, which is the prompt telling them to say `NA` when the set cannot decide —
behaviour worth having, but it is not agreement.

**3. The leniency bias is untouched.** `gpt-4.1` still scores ~0.45 of a level above
`claude-sonnet-5.5` on the same pack (means 1.89 vs 1.45). A rule about which
artefacts to read does not address a difference in how strictly a level is read.

**4. It also fails against the ceiling already measured (A29).** Even where both
vendors cite the same artefact, case-B agreement is 81.0% — below A10's 90%
threshold. Binding cannot reach 90% because it can only work on the sub-population
that already converges. Measured under binding, that sub-population's agreement fell
to 75.0%, so the fix did not even hold its own ceiling.

## Honest limits of this test

- The binding is the **strongest one derivable mechanically**: the whole listed
  artefact set for each control (2–4 artefacts). A hand-authored binding that names
  one decisive artefact per control would constrain choice harder, and was not
  tested. It is not worth funding: the ceiling above caps it below the acceptance
  test, and this run's failure mode (vendors obeying the set and still diverging) is
  the one a stricter set would inherit.
- One case pair. This is a mechanism result on 72 controls, not a rate. But the
  acceptance test was specific ("agreement on the 29 split controls rises without any
  anchor edit"), the population is fixed, and the answer is 5/29 of which 1 is NA/NA.
  There is no reading on which the test passed.
- `alpha`/threshold discipline: no p-value in this memo is used to claim an effect;
  the sign test is reported only to show the observed movement is indistinguishable
  from chance.

## Consequence for the offer

D5 stays **(a) — disclaim now**. Two remedies have now been tested and both failed on
the same held-out pack: anchor work (five passes, moved in-sample only) and evidence
binding (this memo, no effect, compliance total). What remains true and sellable is
the same-model result — 65/72 (90.3%) case B, 68/72 (94.4%) case A — which is a
*PraeSyn-toolchain* claim. A11 stays open with its requirement named and its only
funded candidate now closed. Nothing in D1–D4 moves: D1 stays (a) at $7,500.

No anchor was edited to produce this memo. The bindings, the bound sheets, the logs
and the analysis script are committed beside the pack.
