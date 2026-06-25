# AI Management Framework (AIMF) by PraeSyn

**Version 1.0** | **© 2026 PraeSyn, LLC** | Licensed under [CC BY-NC-ND 4.0](LICENSE.md)

---

## Welcome to AIMF

The **AI Management Framework (AIMF)** is a comprehensive, standards-based framework for establishing and maturing AI governance, risk management, and operational capabilities. Built on ISO 42001 and fully aligned with the NIST AI Risk Management Framework, AIMF provides practical, actionable guidance for organizations deploying artificial intelligence systems.

### What Makes AIMF Unique?

- **Maturity-Based**: Progress through 5 maturity levels (Initial → Developing → Defined → Managed → Optimizing)
- **Multi-Dimensional**: Addresses 4 key dimensions (Governance, Data, Technical Operations, Culture)
- **Flexible Implementation**: 3 implementation tiers (B1/B2/B3) scale rigor based on AI system risk
- **Profile-Driven**: 6 framework profiles enable customization for industries and risk levels
- **Standards-Integrated**: Complete mappings to ISO 42001, NIST AI RMF, ISO 27001, and Executive Orders
- **Open-Source**: Free to use with proper attribution; proprietary tools available commercially

---

## Quick Start

### 1. Understand Your Context

**Who should use AIMF?**
- Organizations deploying AI systems
- AI governance and compliance teams
- Risk management professionals
- Technical teams building AI systems
- Leadership establishing AI strategy

### 2. Choose Your Path

**By Role**:
- **Executives & Leadership** → Start with [AIMF-FRAMEWORK-OVERVIEW.md](core/AIMF-FRAMEWORK-OVERVIEW.md)
- **Governance & Compliance** → Review [AIMF-RISK-BASELINES.md](implementation/AIMF-RISK-BASELINES.md)
- **Technical Teams** → Explore [AIMF-FUNCTION-GOVERN.md](functions/AIMF-FUNCTION-GOVERN.md) and other function guides
- **Assessors** → Begin with [AIMF-ASSESSMENT-GUIDE.md](implementation/AIMF-ASSESSMENT-GUIDE.md)

**By Objective**:
- **Assess current maturity** → [AIMF-ASSESSMENT-GUIDE.md](implementation/AIMF-ASSESSMENT-GUIDE.md)
- **Select controls** → [AIMF-PROFILES-GUIDE.md](implementation/AIMF-PROFILES-GUIDE.md)
- **Implement governance** → [Tier Transition Guides](implementation/maturity-level-guides/)
- **Map to standards** → [Standards Mappings](mappings/)

### 3. Select a Profile

Choose a framework profile that matches your context:

| Profile | Control Count | Best For |
|---------|---------------|----------|
| **[Foundational](profiles/framework-profiles/profile-foundational.md)** | ~35 | Small orgs, low-risk AI, starting point |
| **[Balanced](profiles/framework-profiles/profile-balanced.md)** | ~50 | Standard enterprise AI programs |
| **[High-Assurance](profiles/framework-profiles/profile-high-assurance.md)** | 73 (all) | High-risk AI, critical infrastructure |
| **[Financial Services](profiles/framework-profiles/profile-financial-services.md)** | ~55 | Regulated financial sector |
| **[Healthcare](profiles/framework-profiles/profile-healthcare.md)** | ~55 | Healthcare, patient-facing AI |
| **[Government](profiles/framework-profiles/profile-government.md)** | ~60 | Public sector, transparency requirements |

See [Profile Selection Guide](profiles/framework-profiles/profile-selection-guide.md) for detailed guidance.

---

## Framework Structure

### Core Framework Components

#### 5 Maturity Levels
1. **Initial** - Ad-hoc, reactive approaches
2. **Developing** - Foundational processes established
3. **Defined** - Standardized, documented practices
4. **Managed** - Quantitatively measured and controlled
5. **Optimizing** - Continuous improvement and innovation

#### 4 Capability Dimensions
1. **Governance & Accountability** - Policies, oversight, compliance
2. **Data Management & Privacy** - Data quality, privacy, lifecycle
3. **Technical Operations & MLOps** - Development, deployment, monitoring
4. **Organizational Culture & Capabilities** - Skills, ethics, collaboration

#### 3 Risk Baselines
- **Baseline 1 (B1)**: Initial implementation for low-risk AI
- **Baseline 2 (B2)**: Mature implementation for moderate-risk AI
- **Baseline 3 (B3)**: High-rigor implementation for high-risk AI

#### 73 Controls
Organized across 4 NIST AI RMF functions:
- **GOVERN** (19 controls) - Governance foundations
- **MAP** (19 controls) - Context establishment and categorization
- **MEASURE** (22 controls) - Trustworthy AI characteristics assessment
- **MANAGE** (13 controls) - Risk response and mitigation

---

## Document Navigation

### Core Framework Documentation

| Document | Purpose | Audience |
|----------|---------|----------|
| **[AIMF-FRAMEWORK-OVERVIEW.md](core/AIMF-FRAMEWORK-OVERVIEW.md)** | High-level introduction to framework structure | All audiences |
| **[AIMF-ARCHITECTURE.md](core/AIMF-ARCHITECTURE.md)** | Detailed framework design and relationships | Technical, Governance |
| **[AIMF-CONTROL-CATALOG.csv](core/AIMF-CONTROL-CATALOG.csv)** | Complete control catalog (20 columns, 73 rows) | Assessors, Implementers |
| **[AIMF-CONTROL-CATALOG.md](core/AIMF-CONTROL-CATALOG.md)** | Human-readable control guide | All audiences |

### Implementation Guidance

| Document | Purpose | Audience |
|----------|---------|----------|
| **[AIMF-RISK-BASELINES.md](implementation/AIMF-RISK-BASELINES.md)** | B1/B2/B3 tier definitions and selection | Governance, Technical |
| **[AIMF-ASSESSMENT-GUIDE.md](implementation/AIMF-ASSESSMENT-GUIDE.md)** | Assessment methodology and scoring | Assessors, Auditors |
| **[AIMF-PROFILES-GUIDE.md](implementation/AIMF-PROFILES-GUIDE.md)** | Profile selection and customization | All audiences |
| **[Tier Transition Guides](implementation/maturity-level-guides/)** | Step-by-step tier advancement guidance | Implementers |

### Function Guides (NIST AI RMF Alignment)

| Document | Function | Key Topics |
|----------|----------|------------|
| **[AIMF-FUNCTION-GOVERN.md](functions/AIMF-FUNCTION-GOVERN.md)** | GOVERN | Policies, accountability, culture, resources |
| **[AIMF-FUNCTION-MAP.md](functions/AIMF-FUNCTION-MAP.md)** | MAP | Context, categorization, risks/benefits |
| **[AIMF-FUNCTION-MEASURE.md](functions/AIMF-FUNCTION-MEASURE.md)** | MEASURE | Trustworthy AI characteristics, metrics |
| **[AIMF-FUNCTION-MANAGE.md](functions/AIMF-FUNCTION-MANAGE.md)** | MANAGE | Risk response, mitigation, third-party |

### Standards Mappings

| Document | Standard | Purpose |
|----------|----------|---------|
| **[AIMF-DIMENSION-MAPPING.md](mappings/AIMF-DIMENSION-MAPPING.md)** | Internal | Cross-reference of 4 dimensions |
| **[AIMF-ISO42001-MAPPING.md](mappings/AIMF-ISO42001-MAPPING.md)** | ISO 42001 | Map AIMF to ISO 42001 clauses |
| **[AIMF-NIST-RMF-MAPPING.md](mappings/AIMF-NIST-RMF-MAPPING.md)** | NIST AI RMF | All 59 subcategories mapped |
| **[AIMF-ISO27001-MAPPING.md](mappings/AIMF-ISO27001-MAPPING.md)** | ISO 27001 | Security control alignment |
| **[AIMF-REGULATORY-MAPPING.md](mappings/AIMF-REGULATORY-MAPPING.md)** | Various | Executive Orders, regulations |

### Framework Profiles

| Profile | Controls | Description |
|---------|----------|-------------|
| **[Foundational](profiles/framework-profiles/profile-foundational.md)** | ~35 | Minimal viable AI governance |
| **[Balanced](profiles/framework-profiles/profile-balanced.md)** | ~50 | Standard enterprise implementation |
| **[High-Assurance](profiles/framework-profiles/profile-high-assurance.md)** | 73 | Maximum rigor for high-risk AI |
| **[Financial Services](profiles/framework-profiles/profile-financial-services.md)** | ~55 | Regulated financial sector |
| **[Healthcare](profiles/framework-profiles/profile-healthcare.md)** | ~55 | Healthcare and patient-facing AI |
| **[Government](profiles/framework-profiles/profile-government.md)** | ~60 | Public sector and transparency |
| **[Selection Guide](profiles/framework-profiles/profile-selection-guide.md)** | N/A | How to choose the right profile |

### Implementation Profile Resources

| Document | Purpose |
|----------|---------|
| **[Implementation Template](profiles/implementation-profiles/profile-implementation-template.md)** | Template for organization-specific profiles |
| **[Example: Mid-Market Tech](profiles/implementation-profiles/examples/example-mid-market-tech.md)** | Sample implementation profile |
| **[Example: Healthcare Provider](profiles/implementation-profiles/examples/example-healthcare-provider.md)** | Sample implementation profile |

### Supplemental Resources

| Document | Purpose |
|----------|---------|
| **[AIMF-GLOSSARY.md](supplemental/AIMF-GLOSSARY.md)** | Terms and definitions |
| **[AIMF-FAQ.md](supplemental/AIMF-FAQ.md)** | Frequently asked questions |
| **[AIMF-REFERENCES.md](supplemental/AIMF-REFERENCES.md)** | Bibliography and standards |
| **[AIMF-FUTURE-PROFILES.md](supplemental/AIMF-FUTURE-PROFILES.md)** | Research on additional profiles |

---

## How to Use This Framework

### Step 1: Assess Your Current State

Use the [AIMF Assessment Guide](implementation/AIMF-ASSESSMENT-GUIDE.md) to:
1. Evaluate your organization across 4 dimensions
2. Determine your current maturity level (1-5)
3. Identify strengths and gaps

### Step 2: Select Your Profile

Use the [Profile Selection Guide](profiles/framework-profiles/profile-selection-guide.md) to:
1. Consider your industry and regulatory requirements
2. Evaluate your AI system risk level
3. Choose an appropriate framework profile
4. Customize with organization-specific controls

### Step 3: Determine Implementation Tier

Use the [Risk Baselines Guide](implementation/AIMF-RISK-BASELINES.md) to:
1. Assess AI system impact and autonomy
2. Evaluate error consequences
3. Select appropriate tier (B1, B2, or B3)

### Step 4: Create Implementation Roadmap

Use [Tier Transition Guides](implementation/maturity-level-guides/) to:
1. Identify priority controls from your selected profile
2. Plan implementation phases
3. Allocate resources and set timelines
4. Track progress

### Step 5: Implement and Monitor

1. Implement controls according to selected tier requirements
2. Document evidence and implementation status
3. Conduct periodic assessments
4. Advance maturity levels over time

---

## Standards Integration

AIMF is designed to complement and integrate with established standards:

### Primary Foundation
- **ISO/IEC 42001:2023** - AI Management System
  - AIMF structure aligns with ISO 42001 clauses
  - All ISO 42001 requirements mapped to AIMF controls
  - Can be used as implementation guide for ISO 42001 certification

### Full Alignment
- **NIST AI Risk Management Framework 1.0**
  - All 59 subcategories across 4 functions (GOVERN, MAP, MEASURE, MANAGE)
  - 7 trustworthy AI characteristics fully integrated
  - Compatible with NIST terminology and approach

### Additional Integration
- **ISO/IEC 27001:2022** - Information Security Management
- **Executive Order 14110** - Safe, Secure, and Trustworthy AI
- **Executive Order 14179** - Government AI Innovation
- **Various sector-specific regulations** (HIPAA, GLBA, FCRA, etc.)

---

## Licensing and Usage

### Open-Source Framework

AIMF is licensed under **CC BY-NC-ND 4.0**, which means:

✅ **You CAN**:
- Use the framework to guide your AI governance implementation
- Reference AIMF in research, publications, and training
- Provide consulting services using AIMF (with attribution)
- Create implementation profiles specific to your organization

❌ **You CANNOT**:
- Create modified or derivative versions of the framework
- Use AIMF for commercial products without permission
- Remove or alter copyright and attribution notices

### Attribution Requirement

When using AIMF, provide attribution:

```
This work uses the AI Management Framework (AIMF) by PraeSyn, LLC,
licensed under CC BY-NC-ND 4.0.
https://www.praesyn.com/aimf
```

### Commercial Tools

Proprietary assessment tools, certification programs, and implementation tools are available separately.

For full license details, see [LICENSE.md](LICENSE.md).

---

## Support and Community

### Questions or Feedback?

- **General inquiries**: info@praesyn.com
- **Licensing questions**: licensing@praesyn.com
- **Commercial services**: consulting@praesyn.com

### Contributing

While the framework itself is not accepting contributions (NoDerivatives license), we welcome:
- Feedback and suggestions
- Bug reports (errors, typos, inconsistencies)
- Use case examples and implementation stories
- Requests for additional profiles or guidance

### Staying Updated

- **Website**: https://www.praesyn.com/aimf
- **Version history**: See [CHANGELOG.md](CHANGELOG.md)
- **Future enhancements**: See [AIMF-FUTURE-PROFILES.md](supplemental/AIMF-FUTURE-PROFILES.md)

---

## About PraeSyn

**PraeSyn, LLC** is a Washington State Limited Liability Company specializing in AI governance, risk management, and responsible AI implementation. We developed AIMF to provide practical, actionable guidance for organizations navigating the complex landscape of AI governance and compliance.

Our mission is to make AI governance accessible, practical, and effective for organizations of all sizes.

**Learn more**: https://www.praesyn.com

---

## Framework Information

- **Version**: 1.0
- **Release Date**: January 29, 2026
- **License**: CC BY-NC-ND 4.0
- **Copyright**: © 2026 PraeSyn, LLC
- **Status**: Published

---

**AI Management Framework (AIMF) by PraeSyn**
Making AI Governance Practical, Accessible, and Effective.
