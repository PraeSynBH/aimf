# AI Management Framework (AIMF) by PraeSyn
## Changelog

**© 2026 PraeSyn, LLC. All rights reserved.**
Licensed under CC BY-NC-ND 4.0

**Version**: 1.0.6
**Publication Date**: October 18, 2026
**Status**: Pre-Publication (Working Draft)

---

All notable changes to the AI Management Framework (AIMF) by PraeSyn will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [1.0.6] - 2026-10-18 (Assessment Question Bank: one instrument document, per-control anchors)

**Change Type**: Instrument completion (buyer-facing assessment)
**Rationale**: v1.0.5 closed the *coverage* gap — 72 questions for 72 controls — but the
questions lived as four hand-maintained tables inside the Assessment Guide, carried no
role for the assessor to ask, had no written answer-anchors, and stated their coverage
counts in prose that a hand edit could contradict. A question says what to look for; only an
anchor says what a given answer scores. Without anchors the 0-4 scale is applied from
recollection, so two assessors can look at the same evidence and write two different
numbers — which is precisely the claim a fixed-price assessment sells.

#### Added

- **`implementation/AIMF-ASSESSMENT-QUESTION-BANK.md`** — the instrument as a first-class
  document: one row per control for all 72 catalog controls, with `Control`, `Question`,
  `Evidence`, `Role`, `Audience` and **`Anchor 0` … `Anchor 4`** (360 behavioural anchors),
  grouped by audience. Anchor 0 describes absence, anchor 1 a partial artefact, anchor 2 the
  artefact in force organization-wide, anchor 3 adds a measurement of whether the control
  works, anchor 4 adds improvement driven by that measurement and repeated across cycles. The
  ladder is monotone by construction — every anchor 3 opens "Level 2 evidence plus…", every
  anchor 4 "Level 3 evidence plus…" — so a level cannot be awarded without the evidence for
  the level below.
- **`implementation/AIMF-ASSESSMENT-QUESTION-BANK.csv`** — the authored source of the bank
  (question, evidence, role and the five anchors per control).
- **`scripts/aimf_question_bank.py`** — generator and validator. It joins the authored source
  to `core/AIMF-CONTROL-CATALOG.csv`, **derives every row's audience from the catalog
  dimension** (D1 Leadership, D2 Governance, D3 Technical, D4 Change Agent) with a documented
  four-control override table, and renders both the bank document and the compact question
  tables in the Assessment Guide. Coverage counts in both documents are generated, not typed:
  `report` and the tally are computed from the catalog.
- Row-level `Role` for every control — the role accountable for producing the evidence
  (24 distinct roles across the four audiences).

#### Changed

- **`implementation/AIMF-ASSESSMENT-GUIDE.md`** § Assessment Questions is now a generated
  region: the compact tables (control, question, evidence, role) and the coverage statement
  are rendered by `scripts/aimf_question_bank.py`, replacing the hand-written tables and the
  hand-written routing paragraph. The guide keeps the scale, the decision tree, the process
  and the interpretation; the anchors live in the bank it now points to.
- `scripts/aimf_mappings.py` delegates to `aimf_question_bank.validate`, so
  `check` now also fails on: a missing or unknown control row, an empty question, evidence,
  role or anchor, a repeated anchor within a row, a broken anchor ladder, a coverage count
  that disagrees with the catalog, or generated-region drift between the bank and the guide.
- Version stamps: README, Assessment Guide, QA report and CHANGELOG at 1.0.6.

#### Verification

- `python3 scripts/aimf_mappings.py check` → `OK: mapping documents, catalog and generated
  tables are consistent` (exit 0); `python3 scripts/aimf_question_bank.py check` →
  `OK: question bank covers 72/72 controls with 5 anchors each and no drift`.
- Both checks were run from the packaged directory **and from inside the unpacked v1.0.6
  zip**, and were exercised by mutation before the cut: deleting a row (caught as "no row for
  catalog control"), blanking an anchor or a role, breaking the ladder on one row, and
  editing a generated table by hand (caught as drift) each produced a non-zero exit.
- Bank rows in the shipped bundle: 72 distinct catalog control ids, set-equal to the catalog
  (no extras, no misses); 360 anchors, none empty.

#### Not claimed

- **Inter-rater reliability is not measured.** The anchors are specified; no blind
  double-scoring run has been recorded against them, so the bank is a decisive instrument in
  form but not a validated psychometric one. The bank document says so where a buyer will
  read it, and both copies state it.
- Nothing published or pushed: publication is a board decision (STARTINGPOINT §7, D2).

## [1.0.5] - 2026-10-18 (Complete Assessment Question Bank: 12 → 72 Controls)

**Change Type**: Completeness correction (buyer-facing assessment instrument)
**Rationale**: `implementation/AIMF-ASSESSMENT-GUIDE.md` carried **12 questions for 72
controls**. Twelve worked examples are a marketing artifact, not an instrument: an assessor
would write the other 60 controls' questions on the client's clock, which is exactly the
unbilled work a fixed-price done-for-you assessment cannot absorb. v1.0.4 made the gap
honest (the guide said "12 of the 72 controls", named them, and gave the derivation path
for the rest); this release closes it.

#### Added

- **60 new control questions with evidence expectations** in
  `implementation/AIMF-ASSESSMENT-GUIDE.md` § Assessment Questions, sourced from each
  control's statement and implementation levels in `core/AIMF-CONTROL-CATALOG.csv` and its
  objective in `core/AIMF-CONTROL-CATALOG.md`. The bank now has **72 rows for 72
  controls**, grouped by audience:
  - Leadership **24** — governance policy, accountability, oversight, resourcing, strategy,
    benefit/cost/impact cases, risk response and third-party risk decisions.
  - Technical **30** — system characterization, testing and measurement, production
    monitoring, model and post-deployment management.
  - Governance **6** — compliance monitoring, risk tolerance, requirements traceability,
    independent evaluation, privacy, incident communication.
  - Change Agent **12** — training/competency, team composition and representation, culture,
    transparency communication, external engagement, stakeholder feedback.
- Questions are written to be answered from an artefact an auditor could be shown (no "is
  the culture good?" items), and each row names the artefact that carries a score above
  ML1. **The twelve v1.0.4 rows are unchanged**, so assessments already run against them
  stay comparable; the sections are no longer headed "(Sample)".
- **`scripts/aimf_mappings.py` validates the bank.** `check` (and `generate`) now parses the
  Assessment Questions tables and fails, non-zero, on: a catalog control with no question,
  a duplicate row, an id absent from the catalog, an empty question or evidence cell, a
  question that does not end in `?`, a coverage statement that does not state `72/72`, or a
  stale "N of the 72 controls" claim. `report` prints the bank count.

#### Changed

- The partial-coverage statement is replaced by a complete-bank statement: 72/72 controls,
  one question each, the audience-routing rule (default from the catalog `Dimension`, with
  `GOV-1.4`, `MEA-1.3`, `MAP-1.5` and `MAN-4.3` held with Governance as compliance
  records), and a short scoring note binding the 0-4 scale to the evidence the interviewee
  produces in the session.
- **Version stamps**: Assessment Guide header `1.0` → `1.0.5` (it had never been stamped
  since v1.0.0), README title block and Framework Information, `QA-VERIFICATION-REPORT.md`
  framework version and QA date, and this header.

#### Not in this release

- Nothing pushed or published. Publication remains the D2 decision on PRA-6431.
- The bank is **coverage-complete, not psychometrically validated**. No inter-rater study
  has been run; the guide's requirement to record the artefact scored is the mechanism that
  makes two assessors comparable, and it is untested with real assessors. Do not quote this
  release as validated reliability.

#### Verified

```
$ cd documents/AIMF-Full-Documentation
$ python3 scripts/aimf_mappings.py check          # exit 0
OK: mapping documents, catalog and generated tables are consistent
$ python3 scripts/aimf_mappings.py report
controls: 72
question bank: 72 of 72 controls have a question
$ python3 -c "...parse the section..."            # 72 rows, 72 distinct ids, 24/30/6/12
$ # drift detection exercised by mutation in a scratch copy:
$ #   drop a row        -> FAIL: AIMF-ASSESSMENT-GUIDE.md: no question for MEA-4.3 (exit 1)
$ #   duplicate a row   -> FAIL: ... duplicate question row for MEA-4.3 (exit 1)
$ #   reinstate "12 of the 72" claim -> FAIL: ... stale partial-coverage claim (exit 1)
$ # check also exits 0 from an unpacked copy of the v1.0.5 zip
```

Both zips are rebuilt from the packaged directory of this release, with dotfiles excluded
(`zip -X -r … -x '*/.*'`), and are byte-identical to each other; sha256 and size are stated
in the release comment and the git commit message.

#### Distribution

- `documents/AIMF-Full-Documentation-v1.0.5.zip` and the rolling
  `documents/AIMF-Full-Documentation.zip` are rebuilt from the packaged directory of this
  release and are byte-identical to each other. Both supersede the v1.0.4 bundles.

---

## [1.0.4] - 2026-10-18 (Assessment Scale Unification: 0-3 → 0-4 / ML1-ML5)

**Change Type**: Correctness correction (documentation, buyer-facing assessment instrument)
**Rationale**: The bundle shipped **two live assessment scales**. `implementation/AIMF-ASSESSMENT-GUIDE.md`
defined 0-4 points / ML1-ML5, and the four function documents plus three implementation
documents still defined a 0-3 / four-level lens (`0 Not Present, 1 Ad-Hoc, 2 Developing,
3 Established`). This is not two views of one model: the framework decided the 0-4 scale in
`[1.0.0]` (`0-3 assessment scale (replaced by 0-4 scale with explicit maturity levels)`,
`change-control/QUICK-REFERENCE-WHATS-CHANGED.md` OLD → NEW table) and the migration was
never finished. The live 0-3 lens could not express **ML4 (Managed)** or **ML5 (Optimizing)**
at all — a control scored from `functions/` was structurally capped at "Established" (ML3).

This matters commercially, not cosmetically: the fixed-price assessment is the recommended
paid rung, and its defensibility rests on two assessors producing one number. Two scales and
a cap at ML3 make that impossible.

#### Changed

- **The four function documents now score on the canonical 0-4 / ML1-ML5 scale**, each with
  the same five rows as the Assessment Guide and a pointer to it:
  `functions/AIMF-FUNCTION-GOVERN.md`, `-MAP.md`, `-MEASURE.md`, `-MANAGE.md`.
  - GOVERN's `Tier Alignment` table became `Baseline Alignment`, re-expressed against the
    five scores (0 ML1 = below B1 … 4 ML5 = appropriate for B3) instead of the retired
    0-1 / 1-2 / 2-3 tier ranges.
  - Each document states that the retired 0-3 lens capped its controls at ML3.
- **`implementation/AIMF-ASSESSMENT-GUIDE.md` gained `Scale Retirement and Conversion (0-3 → 0-4)`**:
  a single conversion table (`old 0-3 score → old level name → 0-4 score → maturity level`)
  and the statement that 0-3 is retired, so old audit notes stay readable. Two cautions are
  stated: old `0` and old `1` both convert to 0 (ML1), and an old `3 "Established"` is
  ML3 = 2 — it must be **re-assessed**, not promoted to ML4.
- **The three transition guides' readiness quizzes were migrated** rather than left as a
  third scale: `MATURITY-LEVEL-1-TO-2-GUIDE.md` (32 per-question rubric ladders rebuilt as
  0-4: old "absent" and old "informal/undocumented" merged into ML1, old 2 → ML2, old 3 →
  ML3, plus ML4/ML5 steps), `MATURITY-LEVEL-2-TO-3-GUIDE.md`, `MATURITY-LEVEL-3-TO-4-GUIDE.md`.
  Targets were re-expressed on the canonical scale (ML2 target = 1, ML3 target = 2, ML4
  readiness = 3); the L3→4 guide's "3+ means ML4 emerging" workaround is gone because ML4
  is now its own score.
- **Live references corrected**: `AIMF-V1.0-REVIEW-PLAN.md` and `assets/README.md`
  ("Assessment methodology and scoring (0-3 scale)" → 0-4 / ML1-ML5);
  `profiles/implementation-profiles/profile-implementation-template.md` fill-in prompt.
- **Historical occurrences labelled as history**: the `[1.0.0] - 2026-01-25` migration note
  now reads "maintains 0-3 scoring scale (superseded in [1.0.0] - 2026-01-29 …; 0-3 is
  retired)". `change-control/**` and the earlier `CHANGELOG` entries keep 0-3 only as
  `OLD`-column history; no row presents it as current.
- **The archive no longer ships agent tooling.** v1.0.1–v1.0.3 included
  `AIMF-Full-Documentation/.claude/settings.local.json` (a local permissions file for an
  AI coding assistant). v1.0.4 is built with dotfiles excluded: 80 regular files and 16
  directory entries, down from 81/17. Nothing a reader consumes changed by removing it.
- **Version stamps**: README 1.0.3 → 1.0.4 (title block and Framework Information),
  `QA-VERIFICATION-REPORT.md` framework version and QA date, and this header.

#### Not in this release

- **Defect B — the question bank.** The Assessment Guide still carries 12 sample questions
  for 72 controls. That is a separate, larger gap (writing 60 controls' worth of questions
  and evidence expectations) and is tracked as its own card against this release, not
  mixed into a scale correction. The guide now states its coverage explicitly (12 of 72,
  with the 12 named IDs and the derivation path for the remaining 60) so the "Sample"
  heading can no longer be read as an implied complete bank.
- The legacy `#### Implementation by Tier` headings inside the function documents (content
  is `Baseline 1/2/3`) are untouched here; that is a naming cleanup, not a scale defect.

#### Verified

```
$ cd documents/AIMF-Full-Documentation
$ grep -rn '0-3' --include='*.md' . | grep -viE '\$[0-9]|[0-9]-[0-9]{1,3}[%K]|hours|FTE'
   # only: CHANGELOG history, change-control OLD columns, and the explicit
   # "retired / conversion" statements introduced by this release
$ grep -rn '0-4 point scale' implementation/AIMF-ASSESSMENT-GUIDE.md | wc -l
$ python3 scripts/aimf_mappings.py check   # exit 0, from the packaged dir and from an
                                           # unpacked copy of the rebuilt zip
```

Both zips were rebuilt from the packaged directory of this release and are byte-identical
to each other; sha256 and size are stated in the release comment and the git commit message.

#### Distribution

- `documents/AIMF-Full-Documentation-v1.0.4.zip` and the rolling
  `documents/AIMF-Full-Documentation.zip` are rebuilt from the packaged directory of this
  release and are byte-identical to each other. Both supersede the v1.0.3 bundles.
- Not pushed, not published, no public repository — that still waits on the D2 decision on
  PRA-6431.

---

## [1.0.3] - 2026-10-18 (L2 Taxonomy / Catalog Reconciliation)

**Change Type**: Correctness correction (documentation)
**Rationale**: `core/AIMF-DOMAIN-TAXONOMY.md` defined **20** L2 category names while
`core/AIMF-CONTROL-CATALOG.csv` carries **19** distinct `Domain_L2` values. The two
documents agreed on every control (the same 72 `Control_ID`s, function split
19/18/22/13), so this was a layer-name disagreement rather than a control disagreement —
but a buyer comparing the taxonomy to the catalog saw two different category structures
for the same framework. The divergence was disclosed in `[1.0.2]` above and deliberately
not papered over there. This release reconciles the layer.

The unmatched pair was found by comparing the taxonomy's (L1 domain, L2 category) map to
the catalog's `(Domain_L1, Domain_L2)` groups: **"Data Lifecycle Management"** under
Data Management & Privacy — a category defined in the taxonomy with the placeholder row
`(Covered by other controls) | - | -` and **`Total Controls: 0`** — has no counterpart in
the catalog, because no catalog row carries that `Domain_L2` value. Every other category
matched exactly, control for control.

#### Changed

- **Removed the empty "Data Lifecycle Management" L2 category** from
  `core/AIMF-DOMAIN-TAXONOMY.md`. The CSV is authoritative for the control set and the
  taxonomy is authoritative for how that set is grouped; a category that groups no
  controls is not part of the shipped grouping. Data Management & Privacy now defines 3 L2
  categories (Data Quality & Integrity, Data Privacy & Protection, Third-Party Data
  Governance) and the taxonomy total is 19.
- **The lifecycle subject matter is retained, as prose rather than a phantom category.** A
  *Category note — data lifecycle management* under Third-Party Data Governance records
  that collection, curation, storage, retention and disposal are cross-cutting practices
  in this domain and points to the controls that actually carry them: `GOV-1.3 AI
  Lifecycle Governance` and `GOV-1.6 AI System Decommissioning Policies` (Policies &
  Procedures) and `MAP-4.1` / `MAP-4.2` (Third-Party Data Governance).
- **Rejected alternative**: adding `Data Lifecycle Management` to the catalog. That would
  have required creating a 73rd control, or reassigning existing controls out of
  categories that the catalog, the human-readable catalog guide and the generated mapping
  tables already use. Neither is a layer-name correction, and the first would break the
  72-control set that every other document and mapping depends on.
- **Counts corrected in the taxonomy**: overview "20 mid-level categories" → 19; Summary
  Statistics Data Management & Privacy 4 → 3 L2 categories and TOTAL 20 → 19. Per-domain
  control counts are unchanged (19 / 6 / 31 / 16 = 72).
- **Stale "17 controls" corrected in `core/AIMF-CONTROL-CATALOG.md`** — the quick
  navigation and the Domain L4 section intro said 17 while the same file's own summary
  and the catalog say 16. `[1.0.2]` claimed this correction; the file had not fully
  received it. Fixed here (adjacent correction, disclosed because it is the same class of
  defect).
- **Version stamps**: README 1.0.2 → 1.0.3 (title block and Framework Information),
  `QA-VERIFICATION-REPORT.md` framework version, and this header.

#### Verified

Both layers now name the same 19 categories, and the control set is untouched:

```
$ cd documents/AIMF-Full-Documentation
$ grep -E "^### L2 Category:" core/AIMF-DOMAIN-TAXONOMY.md | sed 's/^### L2 Category: //' | sort -u | wc -l
19
$ python3 -c "import csv;print(len({r['Domain_L2'] for r in csv.DictReader(open('core/AIMF-CONTROL-CATALOG.csv'))}))"
19
$ python3 -c "import csv;print(len({r['Control_ID'] for r in csv.DictReader(open('core/AIMF-CONTROL-CATALOG.csv'))}))"
72
```

Beyond the counts, the taxonomy's `(L1, L2) → control IDs` map was parsed out of the two
documents and compared group by group: **19 categories on each side, identical
membership, no category present on one side only, 72 distinct control IDs on both sides.**
`core/AIMF-CONTROL-CATALOG.csv` itself is byte-unchanged in this release, as are the
NIST / ISO 42001 / ISO 27001 / EO 14179 mappings. `python3 scripts/aimf_mappings.py check`
was run from an unpacked v1.0.3 bundle root and exits 0.

#### Distribution

- `documents/AIMF-Full-Documentation-v1.0.3.zip` and the rolling
  `documents/AIMF-Full-Documentation.zip` are rebuilt from the packaged directory of this
  release and are byte-identical to each other. Both supersede the v1.0.2 bundles.
- Tagged `aimf-v1.0.3` locally. Not pushed, not published, no public repository — that
  still waits on the D2 decision on PRA-6431.

---

## [1.0.2] - 2026-10-18 (Control Count, Release Status and Header Correction)

**Change Type**: Correctness correction (documentation)
**Rationale**: v1.0.1's own notes recorded "Control counts corrected in the QA checklist:
73 → 72 rows / 72 controls / MAP 18", but the shipped README, the human-readable catalog
guide, the architecture document, the framework overview and the taxonomy summary still
told a reader 73 controls, and the README's release status said "Published" above this
file's "Pre-Publication (Working Draft)". A bundle that contradicts itself on its control
count and on whether it is published is a credibility defect for an asset sold on
standards fidelity. Every number below was taken from `core/AIMF-CONTROL-CATALOG.csv`
(72 data rows: GOVERN 19, MAP 18, MEASURE 22, MANAGE 13; 22 columns) and cross-checked
against the control IDs listed in the taxonomy and the catalog guide.

#### Fixed

- **Control count corrected to 72 wherever it was still stated as 73** — README.md
  (profile tables, "72 Controls" section heading, catalog entry), core/AIMF-ARCHITECTURE.md,
  core/AIMF-FRAMEWORK-OVERVIEW.md, core/AIMF-CONTROL-CATALOG.md (overview, document
  information, profile system), core/AIMF-DOMAIN-TAXONOMY.md (overview, summary
  statistics, domain-to-function totals).
- **Per-function split corrected to GOVERN 19 / MAP 18 / MEASURE 22 / MANAGE 13** —
  README's function list and the catalog guide's coverage block said MAP 19, which no
  catalog row supports.
- **Catalog column count corrected** — README described the CSV as "20 columns"; it has 22.
- **Domain distribution corrected** — Organizational Culture & Capabilities is 16 controls
  (22%), not 17 (23%), in the catalog guide and in both taxonomy summary tables; the
  taxonomy's domain-to-function row for that domain is now 0/10/1/5 and its TOTAL row is
  19/18/22/13 = 72.
- **Mid-level category count corrected** — the control guide described "16 mid-level
  categories" while listing 19; the taxonomy described 16 while defining 20.
- **Release status reconciled** — README and this changelog now both state
  `Pre-Publication (Working Draft)`, and the README version block reads 1.0.2 /
  October 18, 2026. There is no remote and no public copy of this bundle, so "Published"
  was not supportable (see the D2 decision on PRA-6431).
- **Changelog header version corrected** — `**Version**: 1.0` → `1.0.2`, matching the
  release entries it actually contains.

#### Known remaining (not corrected here, tracked separately)

- `change-control/20260129143000-*.md` (the January 2026 baseline change plans and
  questionnaire) still state `B3 = 73 controls`. Those are dated planning records of what
  was decided before the change was completed — the completed outcome (72 controls) is
  recorded in the same folder — so they are left as history rather than rewritten.
- Profile control counts in the README are approximate by design (~35, ~50, ~55, ~60) and
  are not part of this correction.

#### Distribution

- Both `documents/AIMF-Full-Documentation-v1.0.2.zip` and the rolling
  `documents/AIMF-Full-Documentation.zip` are rebuilt from the packaged directory of this
  release and are byte-identical to each other.
- Tagged `aimf-v1.0.2` locally. Not pushed, not published, no public repository — that
  still waits on the D2 decision on PRA-6431.

---

### Carried into this release: standards-completeness correction (2026-10-17)

**Change Type**: Correctness correction (documentation)
**Rationale**: v1.0 asserted standards-mapping completeness that the files did not
support. For an IP asset sold on standards alignment, an unsupported completeness claim
is a credibility defect.

#### Fixed

- **Overstated standards-completeness claims removed**: README.md,
  QA-VERIFICATION-REPORT.md and QUALITY-ASSURANCE-CHECKLIST.md no longer claim that the
  dedicated standard-mapping documents are complete. `QA-VERIFICATION-REPORT.md` now
  states what was actually checked, by what command, and has withdrawn the claims it
  could not substantiate (including the publication-readiness "all criteria met"
  posture, now "publication-ready with disclosed exceptions").
- **NIST AI RMF subcategory count corrected from 59 to 72**: NIST AI RMF 1.0
  (NIST AI 100-1) defines 72 subcategories (GOVERN 19, MAP 18, MEASURE 22, MANAGE 13),
  not 59. Corrected in README.md, QA-VERIFICATION-REPORT.md,
  QUALITY-ASSURANCE-CHECKLIST.md, core/AIMF-FRAMEWORK-OVERVIEW.md,
  core/AIMF-ARCHITECTURE.md, supplemental/AIMF-REFERENCES.md, supplemental/AIMF-FAQ.md,
  mappings/MANAGE-FUNCTION-MATURITY-MAPPING.md, and the standards-integration diagrams
  (.md, .mmd, .svg). Framework-wide coverage was verified to be complete (72/72) and to
  reside in `core/AIMF-CONTROL-CATALOG.csv` and the four function maturity mappings.
- **Mapping file headers reconciled**: `AIMF-NIST-RMF-MAPPING.md`,
  `AIMF-ISO42001-MAPPING.md`, `AIMF-ISO27001-MAPPING.md` and
  `AIMF-EXECUTIVE-ORDER-14179-MAPPING.md` now carry a single, accurate `**Status**`
  (`Research Required - Detailed mapping needed`) and a `**Completeness**` line stating
  what the file actually contains. Duplicate, contradictory header stanzas removed.
- **EO 14179 header corrected**: title and date corrected to "Removing Barriers to
  American Leadership in Artificial Intelligence" (January 23, 2025); EO 14110
  rescission (January 20, 2025) recorded.
- **Broken README link fixed**: the Standards Mappings table referenced a non-existent
  `AIMF-REGULATORY-MAPPING.md`; replaced with the actual EO mapping documents.
- **Control counts corrected in the QA checklist**: 73 → 72 rows / 72 controls / MAP 18.

#### Added

- **AIMF-MAPPING-COMPLETENESS.md**: verified register of every mapping artifact
  (file | standard | status | evidence), with the reproducible command output behind
  each status. This register supersedes the completeness claims elsewhere in the doc set.
- **Completeness register re-verified against v1.0.1**: after v1.0.1 completed the four
  dedicated mapping documents, the register, the README mapping table, the QA report and
  the QA checklist were re-checked and updated so that every status matches the per-file
  `**Status**` header. The register now records 72/72 NIST AI RMF coverage in three
  agreeing sources (catalog, four function maturity mappings, dedicated NIST mapping),
  19 ISO 42001 clauses, and ISO 27001 as the single partial item (54/72 referenced,
  18 no-analogue, 0 pre-2022 IDs).

#### Distribution

- **The mapping generator now ships in the bundle**: `scripts/aimf_mappings.py` is
  packaged as `AIMF-Full-Documentation/scripts/aimf_mappings.py`, so the packaged
  documents that cite it as the source and validator of their generated tables describe
  a tool the recipient actually has. From an unpacked bundle root,
  `python3 scripts/aimf_mappings.py check` reproduces the drift check the mapping
  headers, this changelog and the QA report claim; `generate` and `report` also work
  there. The packaged directory is auto-detected from the script's own location, so the
  same file runs from the repository as well; the repository-root `scripts/aimf_mappings.py`
  remains as a delegating shim.
- **Distribution bundles re-cut**: both `documents/AIMF-Full-Documentation-v1.0.1.zip`
  and the rolling `documents/AIMF-Full-Documentation.zip` were rebuilt from the packaged
  directory at v1.0.1 and were byte-identical to each other. Both are superseded by the
  v1.0.2 bundles described above.

---

## [1.0.1] - 2026-10-17 (Standards Mapping Completion)

**Change Type**: Content completion + catalog correction
**Rationale**: v1.0 shipped four standards-mapping documents that were research
skeletons behind completed-looking filenames, and a control catalog whose ISO 27001
column was both incomplete and numbered across two editions. This release completes
the mappings from data already held in the catalog, normalises the catalog, and makes
the mappings machine-generated so the claim cannot drift from the data again.

#### Added

- **NIST AI RMF 1.0 mapping completed**: `mappings/AIMF-NIST-RMF-MAPPING.md` now
  carries all 19 categories and all 72 subcategories, each attributed to exactly one
  AIMF control, with the per-control maturity floor/target and the baseline, defined
  and advanced implementation statements.
- **ISO/IEC 42001:2023 mapping completed**: `mappings/AIMF-ISO42001-MAPPING.md` maps
  all 19 clause references the catalog attributes to the 72 controls, at the standard's
  own clause-heading level (no licensed body text reproduced).
- **ISO/IEC 27001:2022 mapping completed at public control-theme level**:
  `mappings/AIMF-ISO27001-MAPPING.md` carries the Annex A 2022 attribution for every
  one of the 72 controls, plus an explicit, reasoned list of the controls that were
  reviewed and found to have no ISMS analogue. Deep Annex A fidelity remains open
  pending a licensed copy of the 2022 edition and is not claimed.
- **EO 14179 mapping authored**: `mappings/AIMF-EXECUTIVE-ORDER-14179-MAPPING.md`
  maps every provision of the order and its three follow-on federal actions
  (the AI Action Plan and OMB M-25-21 / M-25-22) to the AIMF controls that support
  readiness, and states plainly that the order creates no private-sector obligation.
- **DIMENSION mapping regenerated**: `mappings/AIMF-DIMENSION-MAPPING.md` derives every
  dimension table and every count from the catalog's `Dimension` /
  `Dimension_Secondary` columns.
- **`scripts/aimf_mappings.py`**: generator and drift validator. It renders the
  generated tables from `core/AIMF-CONTROL-CATALOG.csv`, owns the ISO/IEC 27001:2022
  Annex A attribution, and fails (`check`) on any drift between catalog, script and
  documents, on an unknown control reference, on a pre-2022 ISO 27001 reference, or on
  a placeholder/unchecked task in any mapping document. **This script ships inside the
  distribution bundle** at `scripts/aimf_mappings.py`, so a bundle recipient can
  reproduce the drift guarantee the mapping documents cite: unpack the bundle and run
  `python3 scripts/aimf_mappings.py check` from its root.

#### Fixed

- **ISO/IEC 27001 numbering normalised to the 2022 edition**: the three superseded
  2013-edition references in `core/AIMF-CONTROL-CATALOG.csv` were replaced with their
  2022 equivalents, and the 38 controls that carried no reference at all were reviewed
  so that every one of the 72 controls now carries either a 2022 Annex A reference or
  an explicit no-analogue finding.
- **Documented control counts corrected**: the GOVERN / MAP / MEASURE / MANAGE tallies
  and the DIMENSION per-dimension counts now come from the catalog (19/18/22/13 = 72)
  rather than from hand-maintained lists.
- **`core/AIMF-CONTROL-CATALOG.md`** standards metadata lines are synchronised with the
  CSV by the generator.
- **GOVERN function status**: `mappings/GOVERN-FUNCTION-MATURITY-MAPPING.md` validated
  (all 19 GOVERN subcategories present, no placeholders) and its status corrected from
  working draft to complete.

#### Notes

- This release supersedes the four mapping-document `**Status**` values recorded in the
  [Unreleased] standards-completeness correction above; those files are now complete and
  the header statuses say so.
- `AIMF-MAPPING-COMPLETENESS.md` was first issued against the v1.0 baseline (`78d9089`)
  and is re-verified here against the v1.0.1 tree (`e46481d`); it is the register of
  record and its statuses match the per-file `**Status**` headers.

---

## [1.0.0] - 2026-01-29 (Pre-Publication Revision)

### Major Conceptual Refinement: Tier-to-Baseline Revision

**Change Control**: CP-2026-001
**Change Type**: Major Conceptual Revision (Pre-Publication)
**Rationale**: Separation of risk-based control scoping from implementation quality assessment

#### Changed

**Core Conceptual Model**:
- **Baselines replace Tiers** for control scoping
  - B1 (Low Risk): 23 foundational controls (32% of framework)
  - B2 (Moderate Risk): 61 comprehensive controls (85% of framework)
  - B3 (High Risk): All 72 controls (100% of framework)
- **Maturity Levels** now explicitly defined with 0-4 scoring scale
  - ML1 (Initial) = 0 points (ad-hoc, undocumented)
  - ML2 (Developing) = 1 point (documented but inconsistent)
  - ML3 (Defined) = 2 points (standardized, organization-wide) — *Default target*
  - ML4 (Managed) = 3 points (quantitatively measured)
  - ML5 (Optimizing) = 4 points (continuous improvement)
- **Scoring Architecture** enhanced with multi-tier scoring model
  - Profile Score: Actual vs. Target (meeting obligations?)
  - Baseline-Relative Score: Coverage of full baseline
  - Framework-Relative Score: Universal benchmark
  - Hierarchical Profile Support: Parent-child attribution (single/distributed/weighted)

**Control Catalog** (AIMF-CONTROL-CATALOG.csv):
- Renamed columns: T1/T2/T3_Requirements → Implementation_Basic/Defined/Advanced
- Added: Baseline_Applicability column (B1|B2|B3, B2|B3, or B3)
- Added: Default_Target_Maturity column (typically 3, some 2 or 4)
- All 72 controls assigned to appropriate baselines

**Risk Assessment**:
- Added 6-dimension risk characterization questionnaire
- Clear baseline assignment rules based on autonomy, reversibility, impact, consequences, data sensitivity, and regulatory environment
- 5 validated example scenarios demonstrating baseline selection

#### Added

**New Documents**:
- **AIMF-RISK-BASELINES.md**: Complete baseline selection methodology (replaces IMPLEMENTATION-TIERS.md)
- **AIMF-MATURITY-LEVELS.md**: Detailed ML1-5 definitions with evidence criteria
- **Baseline Selection Questionnaire**: Risk characterization tool
- **Maturity Level Progression Guides**: Renamed from tier-transition-guides (content unchanged)

**New Concepts**:
- Profile Attribution for hierarchical scoring
- Per-Control Target Maturity specification
- Composite scoring for nested profiles
- Framework-relative benchmarking

#### Removed

**Deprecated Concepts**:
- "Tier" as organizational maturity stage (replaced by Maturity Levels)
- "Tier progression" as organizational journey (replaced by maturity progression)
- 0-3 assessment scale (replaced by 0-4 scale with explicit maturity levels)
- Implicit maturity assessment (now explicit ML1-5 scale)

**Removed Files**:
- AIMF-IMPLEMENTATION-TIERS.md (replaced by AIMF-RISK-BASELINES.md)
- tier-transition-guides/ directory (renamed to maturity-level-guides/)

#### Fixed

- **Control Count**: Corrected from 59 to 72 total controls
- **NIST Mapping**: Clarified that 72 NIST AI RMF subcategories map to 72 AIMF controls (some NIST subcategories map to multiple controls)
- **Terminology Consistency**: Unified terminology across all 50+ documents

#### Documentation Updates

**50 Files Updated**:
- 3 core definition documents (overview, baselines, maturity levels)
- 1 control catalog (structure and all 72 rows)
- 2 assessment/profile guides (scoring model, attribution)
- 9 profile documents (6 framework + template + 2 examples)
- 6 maturity level guides (renamed and updated)
- 4 function documents (terminology)
- 10 mapping documents (terminology)
- 4 supplemental documents (glossary with new terms, FAQ, references)
- 5 diagrams (renamed baseline-comparison, updated all)
- 5 root documents (README, CHANGELOG, QA docs)

#### Internal Changes

**Change Control Documentation**:
- Created change-control/ directory
- Comprehensive change plan (CP-2026-001)
- Change tracking document
- Baseline distribution analysis
- Phase completion summaries

---

## [1.0.0] - 2026-01-25 (Original Draft)

### Initial Release

**AI Management Framework (AIMF) by PraeSyn - Version 1.0**

This is the inaugural public release of AIMF, establishing the framework as an open-source standard for AI governance and risk management.

### Added

#### Core Framework
- **Maturity Model**: 5-level maturity progression (Initial → Developing → Defined → Managed → Optimizing)
- **4 Capability Dimensions**: Governance & Accountability, Data Management & Privacy, Technical Operations & MLOps, Organizational Culture & Capabilities
- **3 Implementation Tiers**: T1 (Initial), T2 (Mature), T3 (High-Risk) for scalable control rigor
- **73 Controls**: Complete control catalog across 4 NIST AI RMF functions (GOVERN, MAP, MEASURE, MANAGE)

#### Enhanced Control Catalog
- **Hierarchical Structure**: 3-level domain taxonomy (L1 high-level domains → L2 mid-level categories → L3 detailed subcategories)
- **20-Column CSV Format**: Comprehensive control metadata including domain hierarchy, maturity associations, tier requirements, and standards mappings
- **Standards Integration**: Complete mappings to ISO 42001, NIST AI RMF (all 72 subcategories), ISO 27001, and Executive Orders 14110/14179
- **Profile Tagging**: Controls tagged for applicability across framework profiles

#### Framework Profiles System (NIST CSF-Style)
- **Foundational Profile**: ~35 controls for minimal viable AI governance
- **Balanced Profile**: ~50 controls for standard enterprise AI programs
- **High-Assurance Profile**: All 73 controls for high-risk/critical AI systems
- **Financial Services Profile**: ~55 controls tailored for regulated financial sector
- **Healthcare Profile**: ~55 controls for healthcare and patient-facing AI
- **Government Profile**: ~60 controls for public sector transparency and accountability

#### Documentation Suite
- **Core Documentation**: Framework overview, architecture guide, control catalog (CSV + human-readable)
- **Implementation Guidance**: Tier definitions, assessment methodology, profile selection guide, tier transition guides
- **Function Guides**: Detailed guidance for GOVERN, MAP, MEASURE, and MANAGE functions
- **Standards Mappings**: Cross-references to ISO 42001, NIST AI RMF, ISO 27001, regulatory frameworks
- **Profile Resources**: 6 framework profiles, implementation template, example profiles, selection guide
- **Supplemental Materials**: Glossary, FAQ, references, future profiles research

#### Licensing and IP
- **Open-Source Framework**: CC BY-NC-ND 4.0 license for framework documentation
- **Proprietary Tools**: Reserved rights for assessment tools, certification programs, commercial implementations
- **Clear Attribution**: Usage guidelines and attribution requirements

### Framework Characteristics

**Standards-Based Foundation**:
- Primary alignment with ISO/IEC 42001:2023 (AI Management System)
- Full integration of NIST AI Risk Management Framework 1.0
- Compatibility with ISO/IEC 27001:2022 security controls
- Compliance support for Executive Orders 14110 and 14179

**Practical Implementation**:
- Maturity-based progression enables staged implementation
- Flexible tier system adapts to organizational risk tolerance
- Profile-driven approach allows industry and context customization
- Assessment methodology supports capability measurement and gap analysis

**Multi-Audience Design**:
- Executive and leadership guidance (governance, strategy, oversight)
- Technical team guidance (MLOps, development, monitoring)
- Governance and compliance guidance (policies, audit, risk management)
- Organizational change guidance (culture, training, stakeholder engagement)

### Technical Details

**Control Catalog Structure**:
- **Domain L1**: 4 high-level domains (business-friendly taxonomy)
- **Domain L2**: ~12-16 mid-level categories
- **Domain L3**: ~73 detailed subcategories (1:1 with controls)
- **Maturity Associations**: Each control has minimum and target maturity levels
- **Profile Tags**: Supports filtering and customization (foundational, balanced, high-assurance, financial, healthcare, government)

**CSV Column Schema**:
Control_ID, Domain_L1, Domain_L2, Domain_L3, Function, Category, Subcategory, Control_Name, Control_Description, T1_Requirements, T2_Requirements, T3_Requirements, Maturity_Level_Min, Maturity_Level_Target, Dimension, Dimension_Secondary, ISO42001_Clauses, NIST_RMF_Subcategory, ISO27001_Controls, Profile_Tags

**Profile Coverage**:
- Foundational: ~48% control coverage (35/73 controls)
- Balanced: ~68% control coverage (50/73 controls)
- High-Assurance: 100% control coverage (73/73 controls)
- Industry profiles: ~75-82% coverage (55-60 controls)

### Known Limitations

- **Visual Assets**: Initial release includes text-based diagrams; visual infographics planned for v1.1
- **Assessment Tools**: Framework provides assessment methodology; interactive assessment tools are proprietary (available separately)
- **Sector Coverage**: v1.0 includes 3 industry profiles; additional sectors planned for future releases
- **Use Case Profiles**: Technology-specific profiles (Generative AI, Computer Vision, etc.) deferred to v1.1+

### Migration Notes

**For Existing AIMF Users** (from internal/development versions):
- Control IDs remain stable (no breaking changes)
- CSV format expanded from 12 to 20 columns (backward compatible for core columns)
- Profile system is new; previous implementations can map to Balanced or High-Assurance profiles
- Assessment methodology enhanced but maintains 0-3 scoring scale (superseded in [1.0.0] - 2026-01-29 by the 0-4 / ML1-ML5 scale; 0-3 is retired and must not be used for new assessments — see `implementation/AIMF-ASSESSMENT-GUIDE.md#scale-retirement-and-conversion-03--04`)

### Credits and Acknowledgments

**Developed by**: PraeSyn, LLC (Washington State Limited Liability Company)

**Standards References**:
- ISO/IEC 42001:2023 - Artificial Intelligence Management System
- NIST AI Risk Management Framework 1.0 (AI RMF 1.0, January 2023)
- ISO/IEC 27001:2022 - Information Security Management
- Executive Order 14110 - Safe, Secure, and Trustworthy Development and Use of Artificial Intelligence
- Executive Order 14179 - Government AI Innovation and Risk Management

**Framework Foundations**:
- Maturity model inspired by CMMI (Capability Maturity Model Integration)
- Profile system adapted from NIST Cybersecurity Framework 2.0
- Control structure aligned with NIST AI RMF and ISO 42001

### License

This release is licensed under Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International (CC BY-NC-ND 4.0).

Full license: [LICENSE.md](LICENSE.md)

### Contact

**PraeSyn, LLC**
- Website: https://www.praesyn.com
- Email: info@praesyn.com
- Licensing: licensing@praesyn.com

---

## Version History

| Version | Release Date | Status | Key Changes |
|---------|--------------|--------|-------------|
| 1.0.3   | 2026-10-18   | Current | L2 taxonomy/catalog reconciliation — 20 L2 names → 19, matching the 19 `Domain_L2` values in the catalog; empty "Data Lifecycle Management" category removed |
| 1.0.2   | 2026-10-18   | Superseded | Control count, release status and header corrections |
| 1.0.1   | 2026-10-17   | Superseded | Standards mapping completion; ISO/IEC 27001:2022 catalog normalisation; generated mapping tables with a drift validator |
| 1.0.0   | 2026-01-25   | Superseded | Initial public release |

---

## Planned Future Releases

### v1.1 (Planned: Q2 2026)
- Additional industry profiles (Manufacturing, Education, Retail, Energy)
- Use-case profiles (Generative AI, Computer Vision, NLP)
- Visual asset library (diagrams, infographics, flowcharts)
- Enhanced assessment workbook templates

### v1.2 (Planned: Q3 2026)
- Organization size profiles (SMB, Mid-Market, Enterprise)
- Supply Chain AI Risk Profile
- Technology-specific guidance expansions
- Case studies and implementation examples

### v2.0 (Planned: 2027)
- Integration with emerging AI regulations (EU AI Act, state-level laws)
- Enhanced maturity model (potential sub-levels)
- Certification program documentation
- Advanced assessment tooling specifications

See [AIMF-FUTURE-PROFILES.md](supplemental/AIMF-FUTURE-PROFILES.md) for detailed research on future profile development.

---

**Last Updated**: October 18, 2026
**Framework Version**: 1.0.3 (Pre-Publication)
**Maintained by**: PraeSyn, LLC
