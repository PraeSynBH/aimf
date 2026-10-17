# AIMF Architecture

**Version**: 1.0 • **Publication Date**: January 29, 2026
**Status**: Pre-Publication (Working Draft)
© 2026 PraeSyn, LLC | Licensed under CC BY-NC-ND 4.0

---

## Purpose

This document explains the structural design of the AI Management Framework (AIMF): the entities it manages, the relationships between them, and the operational flow that connects governance, technical operations, and assurance. It is meant for technical leads, governance architects, and auditors who want to understand why the framework looks the way it does before diving into specific controls or implementation guides.

## Architectural Layers

1. **Foundation: Standards & Principles**
   - AIMF is rooted in **ISO/IEC 42001:2023**, with the clauses of that standard anchoring the four capability dimensions (Governance, Data, Technical, Culture). The framework surface is also traced across **NIST AI RMF 1.0** (four functions, 72 subcategories) and **ISO/IEC 27001:2022** for security coverage. See [AIMF-FRAMEWORK-OVERVIEW.md](AIMF-FRAMEWORK-OVERVIEW.md) for the full standards alignment tables.
   - These standards define the high-level success criteria, compliance obligations, and the vocabulary that downstream artifacts reuse (controls, baselines, maturity, profiles).

2. **Control Engine**
   - AIMF defines **73 controls** spread across four functions (GOVERN, MAP, MEASURE, MANAGE) and mapped to the four capability dimensions. Controls are described in both [AIMF-CONTROL-CATALOG.csv](AIMF-CONTROL-CATALOG.csv) (machine-friendly) and [AIMF-CONTROL-CATALOG.md](AIMF-CONTROL-CATALOG.md) (human-readable). The catalog is the schema that every implementation artifact refers to.
   - **Baselines (B1/B2/B3)** scope the relevant subset of controls for a risk tier; they are the risk filter. Baseline definitions and the risk-characterization decision tree live in [implementation/AIMF-RISK-BASELINES.md](../implementation/AIMF-RISK-BASELINES.md).

3. **Profiles & Maturity**
   - Profiles are curated combinations of controls tailored to industries, risk appetites, or organizational roles. The profile selection and customization logic is captured in [implementation/AIMF-PROFILES-GUIDE.md](../implementation/AIMF-PROFILES-GUIDE.md).
   - Each control in a profile has an associated **target maturity level** (default ML3). Implementation teams assess their actual maturity along the ML1–ML5 scale described in [AIMF-FRAMEWORK-OVERVIEW.md](AIMF-FRAMEWORK-OVERVIEW.md) and in [implementation/AIMF-ASSESSMENT-GUIDE.md](../implementation/AIMF-ASSESSMENT-GUIDE.md).
   - Scoring happens in layers: baseline max → profile max → profile target → entity assessment. The architecture is intentionally hierarchical so assessments can roll up from detailed evidence to executive dashboards.

4. **Operational Guidance & Playbooks**
   - Function guides ([functions/AIMF-FUNCTION-*.md](../functions/)) and implementation tier manuals ([implementation/maturity-level-guides/](../implementation/maturity-level-guides/)) prescribe the processes that bring the static control catalog to life. They describe workflows for governance, risk management, MLOps, measurement, and mitigation.
   - Supplemental resources (glossary, FAQ, references, future profiles) link the operations back to shared terminology and forward-looking research.

5. **Document Topology & Navigation**
   - The architecture relies on a predictable folder layout: `core/` stores foundational artifacts (overviews, architecture, control catalogs), `implementation/` captures playbooks, `functions/` covers control families, `mappings/` houses standard cross-references, `profiles/` holds profile definitions, and `supplemental/` provides supporting references.
   - Each artifact cross-links carefully so that readers can start at the high-level overview, follow the architecture described here, jump to a specific control in the catalog, and then see how the implementation guides treat that control.

---

## Architectural Relationships

- **Standards ↔ Controls**: Every control entry references ISO 42001 clauses, NIST AI RMF functions/subcategories, and (where relevant) ISO 27001 sections, ensuring that compliance artifacts can be traced back to real-world regulation.
- **Controls ↔ Baselines ↔ Profiles**: Baselines filter the catalog; profiles select a subset from the filtered set; maturity targets determine how controls are scored.
- **Profiles ↔ Assessments**: Profiles become the scope for assessor questionnaires, while maturity scores answer execution quality. Score formulas are documented in [implementation/AIMF-ASSESSMENT-GUIDE.md](../implementation/AIMF-ASSESSMENT-GUIDE.md#scoring-model).
- **Governance & Technical Workflows**: The function guides prescribe how different teams own controls. For example, `functions/AIMF-FUNCTION-GOVERN.md` owns policy creation; `functions/AIMF-FUNCTION-MEASURE.md` owns model validation; `functions/AIMF-FUNCTION-MANAGE.md` covers incident response. This separation supports least-privilege ownership and clear lifecycle handoffs.
- **Document Navigation**: The architecture diagram (implicit in this document) guides readers from the high-level overview to implementation guides, then to function playbooks, and finally to evidence collection templates (e.g., profile templates under `profiles/implementation-profiles`). Each path documents who owns what and how maturity is reported.

---

## Why This Architecture Matters

- **Composable & Traceable**: Teams can plug in new profiles or controls without refactoring existing workflows because the architecture clearly separates scope (what to do) from execution quality (how well it is done).
- **Standards-Aligned**: Starting with ISO 42001 keeps the framework consistent with global expectations, reducing anxiety during audits.
- **Operational Ready**: The architecture stitches documentation, scoring, and function ownership together so that CTOs, compliance teams, and assessors can collaborate without second-guessing how artifacts relate.
- **Referenceable**: With this architecture documented, external partners and regulators have a reliable map of the framework before reviewing deeper evidence.

---

## Next Steps

- Keep this architecture aligned with future profile releases and tier guides.
- Update any referenced documents if new controls, baselines, or functions are introduced.
- Use this document as the foundation for briefing technical and governance stakeholders on AIMF’s design.
