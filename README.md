# AI Management Framework (AIMF) — PraeSyn, LLC

The AIMF is a control-based instrument for assessing and improving how an organisation governs,
manages, maps and measures its AI systems. Version 1.0.12 ships 72 controls across four dimensions
(GOVERN / MANAGE / MAP / MEASURE), six selection profiles, a five-level maturity scale (ML1–ML5) with
per-control behavioural anchors, a full question bank, and standards mappings to NIST AI RMF 1.0,
ISO/IEC 42001:2023, ISO/IEC 27001:2022 (partial — see limitations) and Executive Order 14179.

## Publisher of record

| | |
|---|---|
| Publisher | PraeSyn, LLC (Washington State LLC) |
| Repository | https://github.com/PraeSynBH/aimf |
| Page | https://www.praesyn.com/aimf |
| Licence | Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International (CC BY-NC-ND 4.0) |
| Latest release | `aimf-v1.0.12` (2026-10-21) |
| Download | https://www.praesyn.com/aimf/releases/aimf-v1.0.12/AIMF-Full-Documentation-v1.0.12.zip |
| Bundle sha256 | `e99c07d1402f812c4618119bbab9cf16c6a583d46b2693af8c92aba9507c7e6d` |
| Bundle size | 1,196,412 bytes |

The full framework ships as a single documentation bundle attached to the
[`aimf-v1.0.12` release](https://github.com/PraeSynBH/aimf/releases/tag/aimf-v1.0.12). The source of
that bundle is `documents/AIMF-Full-Documentation/` in this repository, byte-identical to the shipped
archive (84 files); the archive itself is a release asset rather than tree content so the repository
stays diffable.

## Attribution

Using, referencing or citing the AIMF requires attribution in this form (from
[`documents/AIMF-Full-Documentation/LICENSE.md`](documents/AIMF-Full-Documentation/LICENSE.md)):

```
This work uses the AI Management Framework (AIMF) by PraeSyn, LLC,
licensed under CC BY-NC-ND 4.0.
https://www.praesyn.com/aimf
```

For academic or professional citations:

```
PraeSyn, LLC. (2026). AI Management Framework (AIMF), Version 1.0.
https://www.praesyn.com/aimf. Licensed under CC BY-NC-ND 4.0.
```

## Honest limitations

These are measured results and stated scope limits, not marketing caveats:

- **The ISO/IEC 27001:2022 mapping is Partial.** 54 of 72 AIMF controls carry an ISO 27001 mapping
  tag; 18 are recorded as no-analogue. It is not clause-complete and is not presented as a statement
  of conformity.
- **Reproducibility holds within one model family, not across vendors.** On the held-out case
  `AIMF-VAL-2026-B`, two independent blind assessments by two sessions of one model agreed on 65 of
  72 controls (90.3%); two different vendors agreed on 43 of 72 (59.7%). Quote 65 of 72 with the
  qualifier; never a bare percentage.
- **The AIMF is not a certification and produces no attestation.** It is an assessment instrument.
  No certificate, audit opinion or ISO certification is issued or implied, and neither PraeSyn nor
  the framework is an accredited certification body.

The measurement record, the splitting controls and the limits of the method are in
[`documents/AIMF-Full-Documentation/implementation/AIMF-INSTRUMENT-VALIDATION.md`](documents/AIMF-Full-Documentation/implementation/AIMF-INSTRUMENT-VALIDATION.md).

## Repository layout

| Path | What it is |
|---|---|
| `documents/AIMF-Full-Documentation/` | the framework itself — core model, control catalog, functions, profiles, mappings, implementation guides, licence, changelog |
| `scripts/` | the shipped tooling (`aimf_mappings.py`) that regenerates and checks the mapping tables |
| `validation/` | the validation harness, synthetic fixtures, scoring runs and the publication gate record |

Not published here, by design: licensed third-party standards text, client material, and internal
strategy/agent-instruction files. The repository history was rewritten before its first push so that
no licensed text appears in any commit.

## Release provenance

`aimf-v1.0.12` is tagged on the commit that carries its own publication gate record
(`validation/aimf-publication-gate-record-2026-10-23.json`: gate **CLEAR** under the publication
amendment) and the source tree the shipped bundle was built from. Release cadence is content-driven:
a release happens when the framework's content changes, and is complete only when the tag, the
bundle, the changelog and the gate record agree.

## Licence and contact

See [`documents/AIMF-Full-Documentation/LICENSE.md`](documents/AIMF-Full-Documentation/LICENSE.md).
Commercial licensing, proprietary assessment tooling and certification-programme enquiries:
licensing@praesyn.com.
