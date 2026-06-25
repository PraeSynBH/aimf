# AI Management Framework (AIMF) by PraeSyn
## Profiles Guide - Selection and Customization

**© 2026 PraeSyn, LLC. All rights reserved.**
Licensed under Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International (CC BY-NC-ND 4.0)

Framework Version: 1.0
Publication Date: January 29, 2026
Document Status: Pre-Publication (Working Draft)

PraeSyn, LLC | Washington State Limited Liability Company
www.praesyn.com

---

## Table of Contents

1. [What is a Profile?](#what-is-a-profile)
2. [Profile Types](#profile-types)
3. [Relationship to Tiers and Maturity](#relationship-to-tiers-and-maturity)
4. [Available Framework Profiles](#available-framework-profiles)
5. [Profile Selection Methodology](#profile-selection-methodology)
6. [Creating Implementation Profiles](#creating-implementation-profiles)
7. [Profile Usage Examples](#profile-usage-examples)

---

## What is a Profile?

A **profile** is a customized selection and prioritization of AIMF controls based on organizational context, risk tolerance, regulatory obligations, and industry requirements. Profiles enable tailored implementation while maintaining alignment with the complete AIMF structure.

### Key Concepts

**Purpose**: Profiles allow organizations to implement AIMF in a way that matches their specific needs without implementing all 73 controls immediately.

**Flexibility**: Organizations can:
- Start with a pre-defined framework profile
- Add or remove controls based on specific needs
- Adjust implementation tier requirements
- Document their unique implementation decisions

**Standards Alignment**: Profiles maintain full traceability to NIST AI RMF, ISO 42001, and other standards regardless of control selection.

---

## Profile Types

AIMF supports two distinct profile types:

### 1. Framework Profiles (Template-Based)

**Created by**: PraeSyn, LLC
**Purpose**: Pre-defined control selections for common scenarios
**Status**: Published as part of AIMF

**Characteristics**:
- Ready-to-use control selections
- Documented rationale for inclusion/exclusion
- Industry best practices incorporated
- Regular updates with framework versions

**Available Framework Profiles** (v1.0):
1. **Foundational Profile** (~35 controls, ~48% coverage)
2. **Balanced Profile** (~50 controls, ~68% coverage)
3. **High-Assurance Profile** (73 controls, 100% coverage)
4. **Financial Services Profile** (~55 controls, ~75% coverage)
5. **Healthcare Profile** (~55 controls, ~75% coverage)
6. **Government Profile** (~60 controls, ~82% coverage)

### 2. Implementation Profiles (Organization-Specific)

**Created by**: Individual organizations
**Purpose**: Document actual implementation decisions and status
**Status**: Internal organizational document

**Characteristics**:
- Based on a framework profile (starting point)
- Customized for organizational context
- Tracks implementation status
- Documents deviations and rationale
- Updated as implementation progresses

**Key Difference**: Framework profiles are templates; implementation profiles are actual implementation documentation.

---

## Relationship to Baselines, Profiles, and Maturity

Understanding how baselines, profiles, and maturity levels interact is critical for effective AIMF implementation.

### The Three Dimensions

| Dimension | Question | Determines | Driven By |
|-----------|----------|------------|-----------|
| **Baseline (B1/B2/B3)** | WHICH controls are required? | Control scope based on risk | AI system risk characteristics |
| **Profile** | WHICH controls are selected? | Control selection within/across baselines | Organizational context, regulations, priorities |
| **Maturity Level (ML1-5)** | HOW WELL implemented? | Implementation quality (0-4 points) | Assessment of current state |

### How They Work Together

```
1. ASSESS RISK → DETERMINE BASELINE
   ↓
   Risk characterization (6 dimensions) → B1, B2, or B3
   Defines controls in scope (23, 61, or 72 controls)

2. SELECT/CUSTOMIZE PROFILE
   ↓
   Choose controls from baseline (can be subset or superset)
   Set target maturity per control (default: ML3)

3. ASSESS MATURITY
   ↓
   Evaluate each control: ML1-5 (scored as 0-4 points)
   Collect evidence for each rating

4. CALCULATE SCORES
   ↓
   - Profile Score: Actual / Target (are we meeting obligations?)
   - Baseline-Relative: Coverage of full baseline
   - Framework-Relative: Universal benchmark

5. GAP ANALYSIS & ROADMAP
   ↓
   Identify ML1-2 gaps, prioritize ML→ML3, plan ML3→ML4 selectively
```

### Example Scenario

**Organization**: Regional healthcare provider deploying diagnostic AI

**Step 1 - Risk Assessment → Baseline**:
- Autonomy: 1 (human decision), Reversibility: 4 (difficult), Impact: 3 (organization)
- Consequence: 5 (severe - patient harm), Data: 5 (PHI), Regulatory: 4 (HIPAA, FDA)
- **Total Risk**: 22/30 → **B3 (High Risk)** (consequence ≥ 4 triggers B3)
- **Controls in Scope**: All 72 controls

**Step 2 - Profile Selection**:
- Selected: Healthcare Profile (customized from B2/B3 controls)
- **Controls**: 52 controls selected (patient safety focus)
- **Target Maturity**: ML3 (Defined) default; ML4 for critical safety controls

**Step 3 - Maturity Assessment**:
- **Current State**: Mixed ML1-3
  - 8 controls at ML1 (0 points each) = 0 points
  - 18 controls at ML2 (1 point each) = 18 points
  - 26 controls at ML3+ (2-4 points each) = 64 points
- **Actual Score**: 82 points

**Step 4 - Score Calculation**:
- Profile Target: (48 controls × 2) + (4 critical × 3) = 108 points
- Profile Achievement: 82/108 = 76% ⚠️ Below target
- Baseline Max: 72 × 4 = 288 points
- Baseline Coverage: 82/288 = 28%

**Step 5 - Gap Analysis & Roadmap**:
- **Critical Gaps**: 8 controls at ML1 (production monitoring, risk tracking, safety validation)
- **Phase 1** (3 months): Move 8 ML1 controls → ML2 (document and assign)
- **Phase 2** (6 months): Move 18 ML2 controls → ML3 (standardize)
- **Phase 3** (12 months): Advance 4 critical controls → ML4 (measure)
- **Target**: 100% profile achievement within 12 months

---

## Profile Attribution in Hierarchical Structures

When organizations create nested profiles (e.g., enterprise profile with department sub-profiles), they must specify how control assessments aggregate from child to parent profiles.

### Attribution Types

| Type | Use Case | Score Flow |
|------|----------|------------|
| **Direct** | Control assessed at this profile level | No delegation; assessed directly |
| **Single** | One child profile fully owns the control | Child's score → Parent (100% attribution) |
| **Distributed (Equal)** | Multiple children share equally | Average of children's scores |
| **Distributed (Weighted)** | Children share by factor (revenue, headcount, etc.) | Weighted average of children's scores |

### Attribution Specification

Profile definitions must explicitly declare attribution for each control:

```yaml
# Example: Enterprise AI Governance Profile
profile:
  name: "Enterprise AI Governance"
  baseline: B2
  controls:
    - id: GOV-1.1  # Legal/Regulatory Compliance
      target_maturity: 3
      attribution:
        type: single
        owner: "child:legal-department-profile"

    - id: MEA-2.4  # Production Monitoring
      target_maturity: 3
      attribution:
        type: distributed
        method: revenue_weighted
        children:
          - profile: "business-unit-a"
            weight: 0.60  # 60% of revenue
          - profile: "business-unit-b"
            weight: 0.30  # 30% of revenue
          - profile: "business-unit-c"
            weight: 0.10  # 10% of revenue

    - id: GOV-2.3  # Executive Oversight
      target_maturity: 4  # Critical control
      attribution:
        type: direct  # Assessed at enterprise level
```

### Composite Scoring Example

**Enterprise with 3 Business Units**:

```
Enterprise Profile: 50 controls
├── 15 controls: Direct (enterprise-level governance)
├── 25 controls: Distributed equal (3 BUs share equally)
└── 10 controls: Distributed weighted (by revenue: 60%, 30%, 10%)

Business Unit A (60% revenue):
- Implements 35 controls from enterprise profile
- Average maturity: ML3.2 (2.2 points per control)

Business Unit B (30% revenue):
- Implements 35 controls from enterprise profile
- Average maturity: ML2.8 (1.8 points per control)

Business Unit C (10% revenue):
- Implements 35 controls from enterprise profile
- Average maturity: ML2.5 (1.5 points per control)

Enterprise Composite Calculation:
- Direct controls (15): Assessed at enterprise = 35 points
- Equal controls (25): (2.2 + 1.8 + 1.5) / 3 = 1.83 avg × 25 = 46 points
- Weighted controls (10): (2.2×0.6) + (1.8×0.3) + (1.5×0.1) = 1.98 avg × 10 = 20 points
- Total: 35 + 46 + 20 = 101 points

Enterprise Profile Score: 101/100 = 101% ✅ Meeting target
├── BU-A contribution (60%): Above average (2.2 vs 2.0 target)
├── BU-B contribution (30%): Slightly below (1.8 vs 2.0)
└── BU-C contribution (10%): Below (1.5 vs 2.0) ← Focus area
```

**Key Principle**: Profile builders own attribution design; scoring model executes it.

---

## Available Framework Profiles

### Core Profiles (Risk-Based)

#### 1. Foundational Profile

**Control Count**: ~23 controls (~32% of full framework)
**Target Audience**: Organizations with low-risk AI systems
**Baseline Applicability**: B1 (Low Risk baseline controls)
**Default Target Maturity**: ML3 (Defined)
**Use Cases**:
- Small organizations with limited resources
- Low-risk AI applications (internal productivity tools, simple recommendations)
- Pilot AI programs with limited scope
- Starting point for AI governance journey

**Key Characteristics**:
- Essential GOVERN controls for accountability and basic policies
- Core MAP controls for purpose documentation and categorization
- Basic MEASURE controls for testing, performance, monitoring, safety
- Minimal MANAGE controls for go/no-go decisions and risk response

**Typical Industries**: Small business, startups, low-risk internal applications

**Profile Document**: [profile-foundational.md](../profiles/framework-profiles/profile-foundational.md)

---

#### 2. Balanced Profile

**Control Count**: ~50-55 controls (~69-76% of full framework)
**Target Audience**: Standard enterprise AI programs
**Baseline Applicability**: Primarily B2 (Moderate Risk), select B3 controls
**Default Target Maturity**: ML3 (Defined)
**Use Cases**:
- Mid-market to large enterprises
- Moderate-risk AI systems
- Customer-facing AI with moderate autonomy
- Standard enterprise AI governance with regulatory compliance

**Key Characteristics**:
- Comprehensive GOVERN controls (formal committees, systematic processes)
- Substantial MAP controls for context, requirements, and impact assessment
- Strong MEASURE controls for trustworthy AI (fairness, privacy, explainability)
- Standard MANAGE controls for risk treatment and incident response

**Typical Industries**: Technology, retail, professional services, manufacturing, standard financial services

**Profile Document**: [profile-balanced.md](../profiles/framework-profiles/profile-balanced.md)

---

#### 3. High-Assurance Profile

**Control Count**: 72 controls (100% of framework)
**Target Audience**: High-risk and critical AI systems
**Baseline Applicability**: B3 (High Risk - all controls)
**Default Target Maturity**: ML3 (Defined); ML4 for critical safety/fairness controls
**Use Cases**:
- Autonomous AI systems with limited human oversight
- Critical infrastructure and life-safety applications
- High-risk decision-making (credit, employment, law enforcement)
- Regulated medical devices (FDA)
- Maximum regulatory compliance environments

**Key Characteristics**:
- All GOVERN, MAP, MEASURE, and MANAGE controls (100% coverage)
- Independent assessment and external validation requirements
- Public transparency and stakeholder engagement
- Research-grade methodologies and industry leadership expectations

**Typical Industries**: Autonomous vehicles, medical devices, critical infrastructure, high-risk regulated sectors

**Profile Document**: [profile-high-assurance.md](../profiles/framework-profiles/profile-high-assurance.md)

---

### Industry Profiles (Sector-Specific)

#### 4. Financial Services Profile

**Control Count**: ~52-58 controls (~72-81% of full framework)
**Target Audience**: Regulated financial institutions
**Baseline Applicability**: B2-B3 (risk-dependent on AI application)
**Default Target Maturity**: ML3 (Defined); ML4 for fairness and model risk controls
**Use Cases**:
- Algorithmic trading
- Credit decisioning (typically B3)
- Fraud detection
- Risk management AI
- Customer service AI

**Key Characteristics**:
- Strong emphasis on fairness (MEA-2.11) - fair lending compliance
- Third-party risk management (MAN-3.1, MAN-3.2) - vendor model risk
- Explainability and transparency (MEA-2.8, MEA-2.9) - regulatory expectations
- Model risk management controls - SR 11-7 alignment
- Audit and compliance readiness

**Regulatory Drivers**: GLBA, FCRA, Fair Lending Laws, SEC regulations, SR 11-7 (Model Risk Management), Consumer Financial Protection Bureau

**Profile Document**: [profile-financial-services.md](../profiles/framework-profiles/profile-financial-services.md)

---

#### 5. Healthcare Profile

**Control Count**: ~50-56 controls (~69-78% of full framework)
**Target Audience**: Healthcare organizations deploying AI
**Baseline Applicability**: B2-B3 (risk-dependent; diagnostic AI typically B3)
**Default Target Maturity**: ML3 (Defined); ML4 for safety and privacy controls
**Use Cases**:
- Diagnostic AI (typically B3)
- Patient-facing applications
- Clinical decision support
- Healthcare operations AI
- Protected health information processing

**Key Characteristics**:
- Privacy protection (MEA-2.10) - HIPAA compliance mandatory
- Safety evaluation (MEA-2.6) - patient safety paramount
- Explainability (MEA-2.9) - clinical decision transparency
- Data quality (MAP-1.6, MEA-2.5) - diagnostic accuracy requirements
- Human oversight (MAP-3.5) - clinician-in-the-loop

**Regulatory Drivers**: HIPAA, FDA regulations (medical device software), patient safety requirements, clinical ethics standards

**Profile Document**: [profile-healthcare.md](../profiles/framework-profiles/profile-healthcare.md)

---

#### 6. Government Profile

**Control Count**: ~58-64 controls (~81-89% of full framework)
**Target Audience**: Public sector organizations
**Baseline Applicability**: B2-B3 (application-dependent; benefits/law enforcement often B3)
**Default Target Maturity**: ML3 (Defined); ML4 for transparency and civil rights controls
**Use Cases**:
- Public-facing AI services
- Administrative decision support
- Law enforcement AI (requires B3 + additional safeguards)
- Public safety applications
- Benefits administration and eligibility determination

**Key Characteristics**:
- Transparency (MEA-2.8, GOV-4.3) - public accountability mandatory
- Stakeholder engagement (GOV-4.2, MAP-5.2) - citizen input and appeals
- Civil rights protections (MEA-2.11) - fairness and non-discrimination
- Accountability (GOV-2.1, GOV-2.3) - clear public responsibility
- Public reporting and disclosure requirements

**Regulatory Drivers**: Executive Orders 14110 & 14179, OMB AI guidance, civil rights laws, state AI laws (CO, CA, etc.)

**Profile Document**: [profile-government.md](../profiles/framework-profiles/profile-government.md)

---

## Profile Selection Methodology

Use this step-by-step methodology to select the appropriate framework profile for your organization.

### Step 1: Industry/Sector Assessment

**Question**: What industry does your organization operate in?

**Decision Logic**:
```
IF healthcare sector with patient-facing AI
   → Start with Healthcare Profile

ELSE IF financial services with regulated AI
   → Start with Financial Services Profile

ELSE IF government/public sector
   → Start with Government Profile

ELSE IF none of the above
   → Proceed to Step 2 (Risk-Based Evaluation)
```

**Action**: If industry profile exists, use it as starting point. If not, continue to risk-based evaluation.

---

### Step 2: Risk-Based Baseline Determination

Use the [Risk Characterization Questionnaire](../../change-control/20260129143000-BASELINE-SELECTION-QUESTIONNAIRE.md) to assess AI system risk and determine baseline:

**Key Risk Dimensions** (scored 1-5 each):

| Dimension | Low (1-2) | Moderate (3) | High (4-5) |
|-----------|-----------|--------------|------------|
| **Autonomy** | Human decision | Human-in/on-loop | Supervised to full autonomy |
| **Reversibility** | Fully reversible | Moderate effort | Difficult to irreversible |
| **Impact Scale** | Individual/internal | Organizational/large group | Society-wide/vulnerable populations |
| **Consequences** | Negligible/low | Moderate | Significant to severe |
| **Data Sensitivity** | Public/general | Confidential/PII | Regulated/highly sensitive |
| **Regulatory** | General | Sector-specific | High regulatory/critical |

**Baseline Assignment**:
- **Total Score ≥ 21** OR **Any dimension = 5** OR **Consequence/Regulatory ≥ 4** → **B3** (High Risk)
- **Total Score ≥ 13** OR **Any dimension ≥ 4** OR **Two+ dimensions ≥ 3** → **B2** (Moderate Risk)
- **Total Score ≤ 12** AND **All dimensions ≤ 3** → **B1** (Low Risk)

**Profile Guidance by Baseline**:
```
IF B1 (Low Risk) determined
   → Select Foundational Profile

ELSE IF B2 (Moderate Risk) determined
   → Select Balanced Profile or Industry-Specific Profile

ELSE IF B3 (High Risk) determined
   → Select High-Assurance Profile or Industry-Specific with B3 enhancements
```

**Note**: Organizations often have multiple AI systems at different risk levels. Assess each system independently and create separate profiles if needed.

---

### Step 3: Regulatory Requirements Check

**Question**: What regulations apply to your AI systems?

**Common Regulatory Requirements**:

| Regulation | Minimum Profile | Key Controls |
|------------|-----------------|--------------|
| **HIPAA** (Healthcare) | Healthcare Profile (T2) | Privacy, Security, Safety |
| **GLBA** (Financial) | Financial Services Profile (T2) | Privacy, Third-Party, Compliance |
| **FCRA** (Credit Decisions) | Financial Services Profile (T2-T3) | Fairness, Explainability, Accuracy |
| **Executive Order 14110** | Balanced minimum, High-Assurance for high-risk | Comprehensive requirements |
| **State AI Laws** (e.g., Colorado, California) | Balanced minimum | Transparency, Impact Assessment |

**Action**: If subject to specific regulations, ensure selected profile includes all required controls. Add controls if necessary.

---

### Step 4: Organizational Readiness

**Question**: What is your organization's current AI governance maturity?

**Readiness Assessment**:

| Current State | Recommended Starting Profile | Rationale |
|---------------|------------------------------|-----------|
| **No formal AI governance** | Foundational → Balanced (phased) | Build foundation first |
| **Basic governance in place** | Balanced | Mature implementation |
| **Mature governance program** | Balanced or Industry-Specific | Optimize for context |
| **Advanced/Certified** | High-Assurance or Industry + Custom | Maximum rigor |

**Action**: Be realistic about implementation capacity. Starting with Foundational and advancing to Balanced is often more successful than attempting High-Assurance immediately.

---

### Step 5: Resource Availability

**Question**: What resources (budget, personnel, time) are available?

**Resource Considerations**:

| Profile | Implementation Effort | Timeline | Personnel |
|---------|----------------------|----------|-----------|
| **Foundational** | Low | 3-6 months | Part-time team |
| **Balanced** | Moderate | 6-12 months | Dedicated team |
| **High-Assurance** | High | 12-24 months | Full team + external support |
| **Industry Profiles** | Moderate-High | 9-18 months | Dedicated team + specialists |

**Action**: Select a profile that matches available resources. Phased implementation (Foundational → Balanced → High-Assurance) is often more sustainable.

---

### Step 6: Customization Decision

**Question**: Does the selected framework profile need customization?

**Customization Scenarios**:

**Add Controls** when:
- Unique organizational policies require additional controls
- Specific risks not addressed by framework profile
- Additional regulatory requirements
- Stakeholder expectations exceed profile

**Remove Controls** when:
- Organization does not engage in activities covered by control
- Alternative compensating controls exist
- Documented risk acceptance with approval

**Adjust Target Maturity** when:
- Certain controls are more critical (raise target from ML3 to ML4)
- Phased implementation planned (start with ML2 target, increase later)
- Resource constraints require realistic targets (ML2 acceptable short-term)

**Action**: Document all customizations in implementation profile with clear rationale.

---

### Step 7: Validation and Approval

**Question**: Has the profile selection been validated and approved?

**Validation Checklist**:
- [ ] All regulatory requirements covered
- [ ] Risk-based control selection justified
- [ ] Resource constraints considered
- [ ] Stakeholder input obtained (legal, compliance, risk, IT)
- [ ] Implementation timeline realistic
- [ ] Customizations documented with rationale

**Approval Requirements**:
- **Governance Team**: Validate control selection
- **Legal/Compliance**: Confirm regulatory coverage
- **Risk Management**: Approve risk-based decisions
- **Executive Sponsor**: Final approval

**Action**: Obtain formal approval before creating implementation profile and beginning implementation.

---

## Creating Implementation Profiles

Implementation profiles are organization-specific documents that translate a framework profile into actual implementation plans and status tracking.

### Implementation Profile Template

Use the template at [profile-implementation-template.md](../profiles/implementation-profiles/profile-implementation-template.md)

### Key Components

#### 1. Organization Context
- AI portfolio description
- Regulatory environment
- Risk tolerance
- Current maturity assessment results

#### 2. Profile Selection Rationale
- Selected framework profile (with justification)
- Industry and risk considerations
- Regulatory drivers

#### 3. Profile Customizations
- Controls added (with rationale)
- Controls removed (with risk acceptance)
- Tier adjustments (with justification)

#### 4. Implementation Status
- Control-by-control implementation status
- Evidence and documentation links
- Implementation dates
- Notes on challenges or blockers

#### 5. Gap Analysis
- Current state vs target state
- Priority gaps
- Resource requirements
- Timeline estimates

#### 6. Implementation Roadmap
- Phased implementation plan
- Milestones and deadlines
- Dependencies and sequencing
- Resource allocation

---

## Profile Usage Examples

### Example 1: Small Tech Startup

**Context**:
- 50-employee SaaS company
- AI-powered product recommendations
- Low-risk application (recommendations, not decisions)
- Limited AI governance resources

**Profile Selection Process**:
1. **Industry**: Technology (no specific profile)
2. **Risk**: Low (recommendations, human oversight)
3. **Regulations**: General data protection (GDPR/CCPA)
4. **Readiness**: No formal AI governance
5. **Resources**: Part-time team, 6-month timeline

**Selected Profile**: **Foundational Profile**

**Customizations**:
- Added: Data privacy controls (GDPR compliance)
- Removed: None
- Tier: T1 for all controls

**Implementation Approach**: 3-phase rollout over 6 months, focus on essential governance and basic monitoring.

---

### Example 2: Regional Bank

**Context**:
- $10B regional bank
- AI for credit decisioning, fraud detection, customer service
- Regulated by OCC, subject to FCRA, GLBA, SR 11-7
- Mature risk management program

**Profile Selection Process**:
1. **Industry**: Financial Services → Financial Services Profile
2. **Risk**: Moderate-High (credit decisions = high impact)
3. **Regulations**: FCRA, GLBA, SR 11-7, fair lending
4. **Readiness**: Mature risk program, basic AI governance
5. **Resources**: Dedicated team, 12-month timeline

**Selected Profile**: **Financial Services Profile**

**Customizations**:
- Added: Additional fair lending controls
- Added: SR 11-7 model risk management controls
- Tier: T2 for most, T3 for credit decisioning
- Removed: None

**Implementation Approach**: 4 phases aligned with model risk management lifecycle; external validation required for T3 controls.

---

### Example 3: Academic Medical Center

**Context**:
- 500-bed academic hospital
- AI for diagnostic imaging, clinical decision support, patient scheduling
- Subject to HIPAA, FDA regulations
- Research institution with IRB oversight

**Profile Selection Process**:
1. **Industry**: Healthcare → Healthcare Profile
2. **Risk**: Moderate-High (diagnostic support, clinical decisions)
3. **Regulations**: HIPAA, FDA (for diagnostic AI), patient safety
4. **Readiness**: Mature compliance program, emerging AI governance
5. **Resources**: Dedicated team with clinical expertise, 18-month timeline

**Selected Profile**: **Healthcare Profile**

**Customizations**:
- Added: FDA compliance controls (for diagnostic AI)
- Added: IRB oversight for research AI
- Added: Clinical validation controls
- Tier: T2 for scheduling, T3 for diagnostic AI
- Removed: None

**Implementation Approach**: Separate implementation tracks for diagnostic AI (high-risk, T3) vs operational AI (moderate-risk, T2); clinical validation integrated throughout.

---

### Example 4: State Government Agency

**Context**:
- State benefits administration agency
- AI for fraud detection, eligibility determination, document processing
- Subject to Executive Orders, state AI laws, civil rights requirements
- Public transparency mandated

**Profile Selection Process**:
1. **Industry**: Government → Government Profile
2. **Risk**: Moderate-High (impacts public benefits, large scale)
3. **Regulations**: Executive Order 14110, state AI laws, civil rights
4. **Readiness**: Established governance, new to AI-specific requirements
5. **Resources**: Dedicated team, external advisors, 15-month timeline

**Selected Profile**: **Government Profile**

**Customizations**:
- Added: State-specific AI law compliance controls
- Added: Public comment/appeal process controls
- Added: Legislative reporting requirements
- Tier: T2-T3 (T3 for eligibility decisions)
- Removed: None

**Implementation Approach**: Phased with public engagement milestones; external civil rights review; transparency reports published quarterly.

---

## Profile Maintenance and Updates

### When to Review Your Profile

**Triggers for Profile Review**:
- New AI systems deployed
- Regulatory changes
- Significant risk events or incidents
- Organizational changes (merger, acquisition, restructuring)
- Maturity advancement
- Annual review cycle

### Updating Implementation Profiles

**Process**:
1. Review current profile against new requirements
2. Assess implementation status and gaps
3. Identify needed changes (add/remove controls, adjust tiers)
4. Obtain approvals for changes
5. Update implementation profile document
6. Communicate changes to stakeholders
7. Adjust implementation roadmap

**Version Control**: Maintain version history of implementation profile to track evolution over time.

---

## Questions and Support

### Common Questions

**Q: Can I use multiple framework profiles?**
A: Yes, if you have AI systems at different risk levels or in different business units, you can create separate implementation profiles based on different framework profiles.

**Q: Must I implement 100% of the selected profile?**
A: For self-assessment, 80%+ is reasonable with documented risk acceptance for gaps. For certification (if/when available), 90%+ may be required.

**Q: Can I skip Foundational and start with Balanced?**
A: Yes, if you have sufficient resources and existing governance maturity. However, phased implementation is often more successful.

**Q: How do I handle controls that don't apply to my organization?**
A: Document in implementation profile with rationale (e.g., "Control MAP-3.5 not applicable - no autonomous AI systems deployed"). Obtain approval for exclusions.

**Q: Can I create a custom profile not based on a framework profile?**
A: Yes, but starting with a framework profile is strongly recommended to ensure comprehensive coverage and standards alignment.

---

### For More Information

- **Framework Overview**: [AIMF-FRAMEWORK-OVERVIEW.md](../core/AIMF-FRAMEWORK-OVERVIEW.md)
- **Risk Baselines**: [AIMF-RISK-BASELINES.md](AIMF-RISK-BASELINES.md)
- **Maturity Levels**: [AIMF-MATURITY-LEVELS.md](AIMF-MATURITY-LEVELS.md)
- **Control Catalog**: [AIMF-CONTROL-CATALOG.csv](../core/AIMF-CONTROL-CATALOG.csv)
- **Assessment Guide**: [AIMF-ASSESSMENT-GUIDE.md](AIMF-ASSESSMENT-GUIDE.md)

For questions or support:
- Email: info@praesyn.com
- Licensing inquiries: licensing@praesyn.com

---

**AI Management Framework (AIMF) by PraeSyn**
Making AI Governance Practical, Accessible, and Effective.
