# Publication amendment — PRA-6323

**Decision**: publish
**Task comment**: f7aa6f1e-071c-44ba-afae-d69780ca2d3b (body: "approved")
**Comment date**: 2026-10-23
**Issue**: PRA-6323 — AIMF v1.0 Review, Final Report & Publication Decision
**Supersedes**: publish_after_iso27001 (Ben, 2026-10-21)
**Shipping version**: 1.0.12
**ISO 27001 disclosure**: Partial
**Recorded by**: CEO, run adf44dd1-e24c-415b-8f3d-42e3a17be32e

## What this amendment does

Ben's 2026-10-21 ruling held publication until the ISO/IEC 27001 mapping reached
clause-level fidelity against a licensed copy of the 2022 text. The only file
delivered for that purpose (`storage/ISO 27001-Controls-10202026.csv`, 2026-10-21)
is a Drata Control Framework export: 344 `DCF-###` rows, zero Annex A control
identifiers, no clauses 4-10. Clause-level fidelity cannot be built from it.

On 2026-10-23 Ben answered the publication decision issue with a single comment,
"approved". Read against the only open question in the AIMF lane — the
`ask_user_questions` card "How should the ISO 27001 gate be cleared?" on PRA-6702,
whose third option is *Publish now with the ISO 27001 mapping labelled Partial* —
that is a reversal of `publish_after_iso27001`: ship the release with the mapping
as it stands, labelled Partial, rather than wait for or buy the standard.

This file is the auditable record of that reversal. It is deliberately a file the
gate reads, not a code change to the gate's predicate, so a release can never
clear on a silent edit to the checker.

## What it does NOT do

- It does **not** upgrade the mapping claim. `AIMF-ISO27001-MAPPING.md` still
  reads `Status: Partial - ... 54 of 72 AIMF controls ... 18 were reviewed as
  having no ISMS analogue`, and its scope limitation paragraph stays intact. The
  gate fails if the shipped status ever reads `Complete` under this amendment.
- It does **not** make the Drata export distributable. That file stays out of the
  bundle and untracked; the mapping cites public Annex A numbers and titles only.
- It does **not** authorise a push. No git remote exists. A public remote is a
  separate decision, because the repository's history still carries the licensed
  ISO/IEC 42001:2023 PDF and EPUB from the initial commit — a push publishes
  history, not just the current tree. Distribution by bundle (the zip) avoids it.

## Reversal

One comment from Ben on PRA-6323 or PRA-6702 restores the hold: delete this file
and the gate returns to requiring `Status: Complete` on the mapping.
