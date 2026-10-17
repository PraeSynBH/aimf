# AI Management Framework (AIMF) by PraeSyn
## Changelog

**© 2026 PraeSyn, LLC. All rights reserved.**
Licensed under CC BY-NC-ND 4.0

**Version**: 1.0
**Publication Date**: January 29, 2026
**Status**: Pre-Publication (Working Draft)

---

All notable changes to the AI Management Framework (AIMF) by PraeSyn will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [Unreleased] - 2026-10-17 (Standards-Completeness Correction)

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
  a placeholder/unchecked task in any mapping document.

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
- `AIMF-MAPPING-COMPLETENESS.md` describes the pre-1.0.1 state of those four files and
  is superseded by them.

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
- Assessment methodology enhanced but maintains 0-3 scoring scale

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
| 1.0.1   | 2026-10-17   | Current | Standards mapping completion; ISO/IEC 27001:2022 catalog normalisation; generated mapping tables with a drift validator |
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

**Last Updated**: October 17, 2026
**Framework Version**: 1.0.1 (Pre-Publication)
**Maintained by**: PraeSyn, LLC
