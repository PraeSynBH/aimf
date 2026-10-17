# AI Management Framework (AIMF) by PraeSyn
## Framework Overview

**© 2026 PraeSyn, LLC. All rights reserved.**
Licensed under CC BY-NC-ND 4.0

**Version**: 1.0
**Publication Date**: January 29, 2026
**Framework Identifier**: AIMF 1.0
**Status**: Pre-Publication (Working Draft)

---

## Executive Summary

The **AI Management Framework (AIMF)** provides a comprehensive, standards-based approach for organizations to assess, develop, and continuously improve their artificial intelligence capabilities across governance, data management, technical operations, and organizational culture.

AIMF integrates internationally recognized standards including **ISO/IEC 42001:2023** (AI Management Systems), the **NIST AI Risk Management Framework 1.0**, and best practices from **ISO/IEC 27001:2022** (Information Security).

---

## Framework Purpose

The AIMF enables organizations to:

1. **Assess** current AI maturity across multiple capability dimensions
2. **Plan** structured improvement pathways with clear milestones
3. **Implement** controls and practices aligned with international standards
4. **Demonstrate** compliance with regulatory requirements and industry expectations
5. **Continuously improve** AI capabilities through measured performance

---

## Framework Structure

### Core Components

| Component | Description |
|-----------|-------------|
| **Dimensions** | 4 capability areas that comprehensively cover AI maturity |
| **Baselines** | 3 risk-based control scoping levels (Low, Moderate, High) determining which controls apply |
| **Functions** | 4 core functions (GOVERN, MAP, MEASURE, MANAGE) from NIST AI RMF |
| **Controls** | 72 specific control requirements mapped across all functions |
| **Maturity Levels** | 5 progressive implementation quality stages (Initial to Optimizing) |
| **Profiles** | Customized control selections based on organizational context and risk tolerance |

### Four Capability Dimensions

| ID | Dimension | Focus Area | Primary Standards Alignment |
|----|-----------|------------|----------------------------|
| D1 | AI Governance & Risk Management | Policies, oversight, accountability, compliance | ISO 42001 Clauses 4-6, NIST GOVERN |
| D2 | Data Governance & Management | Data quality, privacy, security, lifecycle | ISO 42001 Clause 8.3, NIST MAP 2.3 |
| D3 | Technical Operations (MLOps) | Development, deployment, monitoring, maintenance | ISO 42001 Clause 8, NIST MEASURE/MANAGE |
| D4 | Organizational Culture & Change | Skills, awareness, collaboration, ethics | ISO 42001 Clause 7, NIST GOVERN 3-5 |

### Five Maturity Levels

Maturity levels measure the **quality of control implementation** for each control in an organization's profile. These levels are based on the CMMI (Capability Maturity Model Integration) framework and apply consistently across all controls.

| Level | Name | Description | Assessment Score |
|-------|------|-------------|------------------|
| 1 | **Initial** | Ad-hoc, unpredictable processes; individual-dependent; no documentation | 0 points |
| 2 | **Developing** | Documented processes emerging; inconsistent implementation | 1 point |
| 3 | **Defined** | Standardized, organization-wide processes; consistently applied | 2 points |
| 4 | **Managed** | Quantitatively measured and controlled; data-driven decisions | 3 points |
| 5 | **Optimizing** | Continuous improvement and innovation; industry leadership | 4 points |

**Key Principle**: Maturity levels answer *"How well is this control implemented?"* while baselines answer *"Which controls must we implement?"*

### Three Risk Baselines

The AIMF defines three risk baselines that determine **which controls apply** based on AI system characteristics such as autonomy, impact, reversibility, scale, data sensitivity, and regulatory environment.

| Baseline | Risk Level | Control Scope | Typical Applications |
|----------|------------|---------------|---------------------|
| B1 | **Low Risk** | 23 foundational controls (~32% of framework) | Internal productivity tools; low-impact recommendations; easily reversible outputs |
| B2 | **Moderate Risk** | 61 comprehensive controls (~85% of framework) | Customer-facing AI; moderate autonomy; significant business impact; regulated industries |
| B3 | **High Risk** | All 72 controls (100% of framework) | Autonomous systems; life-safety; civil rights impact; critical infrastructure; stringent regulatory |

**Selection Method**: Organizations use a [risk characterization questionnaire](../implementation/AIMF-RISK-BASELINES.md#risk-characterization) to determine the appropriate baseline for each AI system or system category. A single organization may have AI systems across multiple baselines.

---

## Framework Scoring Architecture

### How Baselines, Profiles, and Maturity Create Objective Scores

AIMF uses a multi-layered scoring model that enables objective measurement and continuous improvement:

```
Framework (73 controls, ML5 max)
    └── Baseline (scoped controls based on risk)
            └── Profile (selected controls, ML3 default target)
                    └── Entity Assessment (actual maturity ratings)
```

### Score Types

| Score Type | Formula | Purpose |
|------------|---------|---------|
| **Profile Score** | (Actual Score / Profile Target Score) × 100% | Are we meeting our obligations? |
| **Profile Maximum** | (Actual Score / Profile Max Score) × 100% | How much headroom for growth? |
| **Baseline-Relative** | (Actual Score / Baseline Max Score) × 100% | Coverage of risk baseline |
| **Framework-Relative** | (Actual Score / Framework Max Score) × 100% | Universal benchmark |

### Scoring Example

**Scenario**: Healthcare organization with moderate-risk diagnostic AI

```
Baseline: B2 (Moderate Risk, 50 controls applicable)
Profile: Healthcare profile (48 controls selected from B2)
Target Maturity: ML3 (Defined) per control

Calculations:
- Profile Max Score: 48 controls × 4 points = 192 points
- Profile Target Score: 48 controls × 2 points = 96 points (ML3 = 2 on 0-4 scale)
- Actual Score: Assessed maturity sum = 104 points

Results:
- Profile Score: 104/96 = 108% ✅ Exceeding target
- Profile Maximum: 104/192 = 54% (room to grow to ML4-5)
- Baseline-Relative: 104/244 = 43% (baseline max: 61×4)
- Framework-Relative: 104/288 = 36% (framework max: 72×4)
```

### Profile Targets and Progression

- **Default target**: ML3 (Defined - standardized, organization-wide implementation)
- **Profiles can customize**: Set higher targets (ML4) for critical controls or lower (ML2) for less critical
- **Maturity progression**: Organizations can increase target maturity over time without changing control scope
- **Hierarchical profiles**: Parent profiles can aggregate scores from child profiles using explicit attribution rules

---

## Standards Integration

### Primary Foundation: ISO/IEC 42001:2023

AIMF is built on the ISO 42001 Artificial Intelligence Management System (AIMS) structure:

| ISO 42001 Clause | AIMF Integration |
|------------------|------------------|
| 4. Context of the organization | Dimension 1, NIST MAP 1 |
| 5. Leadership | Dimension 1, NIST GOVERN 2 |
| 6. Planning | All Dimensions, NIST MAP/GOVERN |
| 7. Support | Dimension 4, NIST GOVERN 3-5 |
| 8. Operation | Dimensions 2-3, NIST MEASURE/MANAGE |
| 9. Performance evaluation | All Dimensions, Level 4+ characteristics |
| 10. Improvement | All Dimensions, Level 5 characteristics |

### Supporting Framework: NIST AI RMF 1.0

AIMF integrates all NIST AI RMF subcategories across four functions (72 subcategories mapped to 72 controls):

| Function | Categories | Subcategories | Primary Dimension |
|----------|------------|---------------|-------------------|
| GOVERN | 6 | 19 | D1, D4 |
| MAP | 5 | 18 | D1, D2 |
| MEASURE | 4 | 22 | D3 |
| MANAGE | 4 | 13 | D1, D3 |
| **Total** | **19** | **72** | All |

---

## Framework Application

### For Assessment

Organizations use AIMF to:
- **Determine risk baseline** using risk characterization methodology (B1/B2/B3)
- **Select or customize profile** based on industry, regulations, and organizational context
- **Assess maturity** for each control in the profile (ML1-5 scale)
- **Calculate scores** across profile, baseline-relative, and framework-relative dimensions
- **Identify gaps** between current state and target maturity levels
- **Prioritize improvements** based on gap analysis and risk prioritization

### For Implementation

Organizations use AIMF to:
- **Implement controls** appropriate to their baseline and profile
- **Define maturity targets** per control (default: ML3, customizable to ML2-5)
- **Establish evidence requirements** for each maturity level
- **Track progression** toward target maturity using objective scoring
- **Manage hierarchical profiles** with clear attribution rules for composite scoring

### For Compliance

Organizations use AIMF to:
- Demonstrate alignment with **ISO 42001** structure and requirements
- Map to **NIST AI RMF** functions and subcategories (100% coverage)
- Address **regulatory expectations** through baseline and profile selection
- Support **certification efforts** with comprehensive control catalog and maturity evidence
- Provide **audit-ready documentation** of AI governance maturity

---

## Document Set

The AIMF formal documentation includes:

| Document | Description |
|----------|-------------|
| **AIMF-FRAMEWORK-OVERVIEW.md** | This document - high-level framework introduction |
| **AIMF-CONTROL-CATALOG.csv** | Complete control catalog in spreadsheet format |
| **AIMF-RISK-BASELINES.md** | Risk-based baseline definitions and selection methodology |
| **AIMF-ASSESSMENT-GUIDE.md** | Assessment methodology, maturity scoring, and gap analysis |
| **AIMF-PROFILES-GUIDE.md** | Profile selection, customization, and hierarchical scoring |
| **AIMF-FUNCTION-GOVERN.md** | GOVERN function controls and guidance |
| **AIMF-FUNCTION-MAP.md** | MAP function controls and guidance |
| **AIMF-FUNCTION-MEASURE.md** | MEASURE function controls and guidance |
| **AIMF-FUNCTION-MANAGE.md** | MANAGE function controls and guidance |
| **AIMF-DIMENSION-MAPPING.md** | Dimension-to-control cross-reference |

---

## Relationship to Other Frameworks

| Framework | Relationship to AIMF |
|-----------|---------------------|
| ISO 42001 | Primary foundation; structural basis |
| NIST AI RMF | Core functions and subcategories integrated |
| ISO 27001 | Security controls referenced for AI systems |
| NIST CSF | Complementary cybersecurity alignment |
| NIST 800-53 | Security control mapping available |
| EU AI Act | High-risk AI requirements mapped |

---

## Versioning and Maintenance

The AIMF is maintained and updated to reflect:
- Updates to referenced standards (ISO 42001, NIST AI RMF)
- Emerging regulatory requirements
- Industry best practices evolution
- Community feedback and real-world validation

**Version History**:
| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-01-29 | Pre-publication conceptual refinement: Tier-to-Baseline revision, maturity scoring model, hierarchical profile support |

---

## References

1. ISO/IEC 42001:2023 - Artificial intelligence management system
2. NIST AI RMF 1.0 - AI Risk Management Framework (January 2023)
3. ISO/IEC 27001:2022 - Information security management systems
4. NIST Cybersecurity Framework 2.0
5. CMMI for Development (capability maturity model integration)

---

**Next Document**: [AIMF Control Catalog](AIMF-CONTROL-CATALOG.csv) | [Risk Baselines](../implementation/AIMF-RISK-BASELINES.md) | [Assessment Guide](../implementation/AIMF-ASSESSMENT-GUIDE.md)
