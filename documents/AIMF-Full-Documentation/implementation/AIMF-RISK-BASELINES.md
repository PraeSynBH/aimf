# AI Management Framework (AIMF) by PraeSyn
## Risk Baselines - Control Scoping Based on AI System Risk

**© 2026 PraeSyn, LLC. All rights reserved.**
Licensed under CC BY-NC-ND 4.0

**Version**: 1.0
**Publication Date**: January 29, 2026
**Document Type**: Baseline Definition Guide
**Status**: Pre-Publication (Working Draft)

---

## Overview

The AIMF defines three **risk baselines** that determine which controls apply to an AI system based on its risk characteristics. Baselines provide risk-appropriate control scoping while maintaining standards alignment and enabling proportional governance.

### Key Principle

**Baselines answer**: *"Which controls must we implement for this AI system?"*

**Maturity levels answer**: *"How well have we implemented those controls?"*

These are orthogonal dimensions—a low-risk AI system (B1) can be implemented at high maturity (ML5), and a high-risk AI system (B3) may currently be at low maturity (ML1-2), revealing critical gaps.

---

## The Three Risk Baselines

| Baseline | Risk Level | Control Count | % of Framework | Purpose |
|----------|------------|---------------|----------------|---------|
| **B1** | Low Risk | 23 controls | 32% | Essential governance for low-impact AI systems |
| **B2** | Moderate Risk | 61 controls | 85% | Comprehensive controls for standard enterprise AI |
| **B3** | High Risk | 72 controls | 100% | Maximum rigor for critical/regulated AI systems |

### Portfolio Approach

**Important**: Organizations typically have AI systems across multiple risk levels. A single organization may use:
- **B1** for internal productivity tools
- **B2** for customer-facing applications
- **B3** for autonomous or regulated systems

Each AI system or system category should be assessed independently to determine its appropriate baseline.

---

## Risk Characterization Methodology

### Six Risk Dimensions

Baseline assignment is determined by assessing AI systems across six risk dimensions:

| Dimension | Measures | Range |
|-----------|----------|-------|
| **1. Autonomy Level** | Degree of human involvement in AI decisions | 1 (Human decides) to 5 (Full autonomy) |
| **2. Decision Reversibility** | Ease of reversing AI outcomes | 1 (Fully reversible) to 5 (Irreversible) |
| **3. Impact Scale** | Number of people/entities affected | 1 (Individual) to 5 (Society-wide) |
| **4. Consequence Severity** | Potential harm from errors | 1 (Negligible) to 5 (Severe/life-safety) |
| **5. Data Sensitivity** | Sensitivity of processed data | 1 (Public) to 5 (Highly sensitive/regulated) |
| **6. Regulatory Environment** | Applicable compliance obligations | 1 (General) to 5 (Critical regulated) |

**Total Risk Score Range**: 6 (minimum) to 30 (maximum)

### Assessment Questions

**See**: [Baseline Selection Questionnaire](../../change-control/20260129143000-BASELINE-SELECTION-QUESTIONNAIRE.md) for detailed scoring criteria.

---

## Baseline Assignment Rules

### Rule 1: High-Risk Baseline (B3)

**Assign B3 if ANY of the following are true**:

- ✓ Any individual dimension scores **5** (maximum severity)
- ✓ Consequence Severity (Q4) scores **≥ 4** (significant or severe harm)
- ✓ Regulatory Environment (Q6) scores **≥ 4** (critical regulatory requirements)
- ✓ Total risk score **≥ 21** (consistently high risk across dimensions)

**Rationale**: High-consequence, high-regulation, or maximum-severity systems require all controls regardless of other factors.

---

### Rule 2: Moderate-Risk Baseline (B2)

**If not B3, assign B2 if ANY of the following are true**:

- ✓ Any individual dimension scores **≥ 4** (high severity in any dimension)
- ✓ Two or more dimensions score **≥ 3** (multiple moderate-high factors)
- ✓ Total risk score **≥ 13** (aggregate moderate risk)

**Rationale**: Moderate risk systems require comprehensive controls even if not at maximum rigor.

---

### Rule 3: Low-Risk Baseline (B1)

**If not B3 or B2, assign B1**:

- ✓ All dimensions score **≤ 3** (no high-severity factors)
- ✓ Majority of dimensions score **≤ 2** (mostly low risk)
- ✓ Total risk score **≤ 12** (aggregate low risk)

**Rationale**: Low-risk systems need foundational governance without unnecessary overhead.

---

## Baseline Definitions

### Baseline 1 (B1): Low Risk

**Control Scope**: Approximately 35 foundational controls (~48% of framework)

**Characteristics**:
- **AI Systems**: Internal tools, productivity applications, low-impact recommendations
- **Autonomy**: Human makes all decisions; AI provides information/support
- **Reversibility**: Outcomes easily reversible with minimal cost
- **Impact**: Limited to individuals or small internal groups
- **Consequences**: Errors cause minor inconvenience, no lasting harm
- **Data**: Public or general business data, minimal PII
- **Regulation**: Standard business regulations only

**Control Focus**:
- ✓ Core governance (policies, basic accountability)
- ✓ Essential purpose documentation and categorization
- ✓ Basic testing and safety validation
- ✓ Fundamental risk awareness and assessment
- ✓ Go/no-go decision processes

**Excluded Controls**:
- ✗ Advanced measurement and analytics
- ✗ Comprehensive third-party management
- ✗ External validation and independent assessment
- ✗ Public transparency and reporting
- ✗ Research-grade TEVV methodologies

**Typical Applications**:
- Email categorization and filtering
- Internal chatbots for employee support
- Document summarization tools
- Search and retrieval systems
- Non-binding product recommendations

**Example**: Internal employee chatbot providing HR policy information. Low autonomy (information only), fully reversible, limited to employees, minimal consequences if wrong, general business data, no special regulations.

**Baseline Assignment**: B1 (Total risk score: 10-12)

---

### Baseline 2 (B2): Moderate Risk

**Control Scope**: Approximately 50 comprehensive controls (~68% of framework)

**Characteristics**:
- **AI Systems**: Customer-facing applications, moderate-autonomy systems, business-critical AI
- **Autonomy**: Human-in-loop or human-on-loop; some autonomous action with oversight
- **Reversibility**: Reversal possible but requires effort, cost, or time
- **Impact**: Large customer bases, organization-wide, or significant groups
- **Consequences**: Moderate to significant (financial loss, reputational harm, regulatory risk)
- **Data**: PII, financial data, or regulated data categories
- **Regulation**: Sector-specific requirements (GLBA, general HIPAA, employment laws)

**Control Focus**:
- ✓ All B1 controls PLUS:
- ✓ Formal governance committees and systematic processes
- ✓ Comprehensive data governance and privacy controls
- ✓ Full trustworthiness evaluation (fairness, explainability, transparency)
- ✓ Systematic risk management and incident response
- ✓ Production monitoring with anomaly detection
- ✓ Third-party risk assessment and management

**Excluded Controls**:
- ✗ Independent external validation (internal audit sufficient)
- ✗ Public transparency reporting (internal reporting sufficient)
- ✗ Research-grade methodologies
- ✗ Real-time predictive analytics
- ✗ Industry leadership requirements

**Typical Applications**:
- Fraud detection systems
- Credit scoring and underwriting
- Customer service chatbots
- Personalized marketing and recommendations (large scale)
- Automated claims processing
- Resume screening and candidate ranking

**Example**: E-commerce fraud detection system. Moderate autonomy (auto-flags for review), moderately reversible (account restoration process), large scale (thousands of transactions), moderate consequences (customer friction, lost revenue), regulated payment data, sector-specific compliance.

**Baseline Assignment**: B2 (Total risk score: 13-20)

---

### Baseline 3 (B3): High Risk

**Control Scope**: All 72 controls (100% of framework)

**Characteristics**:
- **AI Systems**: Autonomous decision-making, life-safety, civil rights impact, critical infrastructure
- **Autonomy**: Supervised autonomy to full autonomy; minimal human review
- **Reversibility**: Difficult to reverse or irreversible consequences
- **Impact**: Society-wide, vulnerable populations, or critical systems
- **Consequences**: Severe harm potential (physical, financial, civil rights, life-safety)
- **Data**: PHI, biometric, children's data, special category data
- **Regulation**: Life-safety regulation, civil rights mandates, FDA, critical infrastructure protection

**Control Focus**:
- ✓ All B1 and B2 controls PLUS:
- ✓ Independent oversight and external validation
- ✓ Real-time monitoring with predictive analytics
- ✓ Public transparency and stakeholder engagement
- ✓ Research-grade TEVV with independent assessment
- ✓ Advanced security (red team testing, continuous monitoring)
- ✓ Comprehensive supply chain risk management
- ✓ Board-level accountability and external advisory

**No Exclusions**: All framework controls apply at maximum rigor

**Typical Applications**:
- Autonomous vehicle navigation
- Medical diagnostic AI (FDA-regulated)
- Automated medical treatment decisions
- Law enforcement facial recognition
- Automated employment decisions (high volume)
- Critical infrastructure control systems
- Autonomous weapons systems
- Child welfare algorithmic screening

**Example**: Medical diagnostic AI for radiology. Low autonomy (doctor decides) but severe consequences (misdiagnosis = wrong treatment), highly sensitive data (PHI), high regulatory (HIPAA, potentially FDA), large impact scope.

**Baseline Assignment**: B3 (Consequence severity ≥ 4 triggers B3)

---

## Baseline Selection Decision Tree

```
START: Assess AI system using 6 risk dimensions (Q1-Q6)
   |
   ├─→ ANY dimension = 5?  ────────────────────→ B3 (High Risk)
   |
   ├─→ Consequence (Q4) ≥ 4?  ─────────────────→ B3 (High Risk)
   |
   ├─→ Regulatory (Q6) ≥ 4?  ──────────────────→ B3 (High Risk)
   |
   ├─→ Total score ≥ 21?  ─────────────────────→ B3 (High Risk)
   |
   ├─→ Any dimension ≥ 4?  ────────────────────→ B2 (Moderate Risk)
   |
   ├─→ Two+ dimensions ≥ 3?  ──────────────────→ B2 (Moderate Risk)
   |
   ├─→ Total score ≥ 13?  ─────────────────────→ B2 (Moderate Risk)
   |
   └─→ Otherwise  ───────────────────────────────→ B1 (Low Risk)
```

---

## Baseline Comparison Matrix

### Control Implementation Requirements

| Control Category | B1 (Low Risk) | B2 (Moderate Risk) | B3 (High Risk) |
|------------------|---------------|-------------------|----------------|
| **Governance** | Basic policies, assigned roles | Formal committees, RACI matrices | Board oversight, independent function |
| **Risk Assessment** | Qualitative, high-level | Quantified, systematic | Real-time, predictive modeling |
| **Testing (TEVV)** | Functionality testing | Comprehensive bias/fairness testing | Independent validation, research-grade |
| **Monitoring** | Basic availability monitoring | Systematic with anomaly detection | Real-time with AI-powered analytics |
| **Security** | Standard security controls | Comprehensive assessment | Red team testing, continuous monitoring |
| **Data Governance** | Basic quality checks | Privacy impact assessments, lineage | Advanced governance, differential privacy |
| **Training** | General awareness | Role-based with competency assessment | Certification programs, continuous development |
| **External Validation** | Self-assessment | Internal audit | Independent third-party audit |
| **Transparency** | Internal documentation | Stakeholder communication | Public transparency reports |
| **Incident Response** | Basic procedures | Systematic response, root cause | Automated detection, public disclosure |

---

## Control Distribution Across Baselines

### Function Distribution

| Function | B1 Controls | B2 Controls | B3 Controls (All) |
|----------|-------------|-------------|-------------------|
| **GOVERN** | 6 | 14 | 19 |
| **MAP** | 7 | 17 | 18 |
| **MEASURE** | 5 | 18 | 22 |
| **MANAGE** | 5 | 12 | 13 |
| **TOTAL** | **23** | **61** | **72** |

### Dimension Distribution

| Dimension | B1 Controls | B2 Controls | B3 Controls |
|-----------|-------------|-------------|-------------|
| **D1: Governance & Risk** | 15-18 | 25-28 | 35 |
| **D2: Data Governance** | 6-8 | 10-12 | 15 |
| **D3: Technical Operations** | 10-12 | 14-16 | 20 |
| **D4: Culture & Change** | 4-6 | 8-10 | 13 |

**Note**: Exact control assignments per baseline are defined in the control catalog column `Baseline_Applicability`.

---

## Baseline Selection Examples

### Example 1: Low-Risk Assignment (B1)

**AI System**: Internal employee chatbot for HR policy questions

**Risk Assessment**:
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Autonomy | 2 | Human-in-loop (employee decides whether to follow advice) |
| Reversibility | 1 | Fully reversible (information only, no binding action) |
| Impact Scale | 3 | Organization-wide (all employees have access) |
| Consequence | 2 | Low (incorrect answer causes minor confusion) |
| Data Sensitivity | 3 | Confidential (employee questions may contain personal info) |
| Regulatory | 1 | General (standard employment law compliance) |
| **TOTAL** | **12** | |

**Assignment Logic**: Total score 12 ≤ 12, all dimensions ≤ 3 → **B1 (Low Risk)**

**Controls Required**: 23 foundational controls focusing on basic governance, purpose documentation, testing, and monitoring

---

### Example 2: Moderate-Risk Assignment (B2)

**AI System**: E-commerce fraud detection with automated transaction blocking

**Risk Assessment**:
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Autonomy | 3 | Human-on-loop (auto-flags suspicious transactions, human reviews queue) |
| Reversibility | 3 | Moderate (account can be restored, but customer friction and lost sales) |
| Impact Scale | 4 | Large scale (thousands of daily transactions) |
| Consequence | 3 | Moderate (false positives frustrate customers, false negatives = fraud loss) |
| Data Sensitivity | 4 | Regulated (payment card data, customer PII) |
| Regulatory | 3 | Sector-specific (PCI-DSS, consumer protection laws) |
| **TOTAL** | **20** | |

**Assignment Logic**: Impact Scale ≥ 4, Data Sensitivity ≥ 4, Total score 20 ≥ 13 → **B2 (Moderate Risk)**

**Controls Required**: 61 comprehensive controls including data governance, privacy, fairness testing, systematic risk management

---

### Example 3: High-Risk Assignment (B3) - Consequence Trigger

**AI System**: Credit decisioning AI for consumer loan applications

**Risk Assessment**:
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Autonomy | 4 | Supervised autonomy (periodic sampling review, not every decision) |
| Reversibility | 4 | Difficult (appeals possible but credit harm, reputational impact) |
| Impact Scale | 4 | Large scale (thousands of applicants monthly) |
| Consequence | 4 | Significant (unfair denial = financial harm, civil rights concerns) |
| Data Sensitivity | 4 | Regulated (credit reports, financial history, employment data) |
| Regulatory | 5 | Critical (FCRA, ECOA, fair lending laws, regulatory examinations) |
| **TOTAL** | **25** | |

**Assignment Logic**: Consequence ≥ 4, Regulatory = 5, Total score 25 ≥ 21 → **B3 (High Risk)**

**Controls Required**: All 72 controls including independent validation, public transparency, comprehensive fairness testing, external audit

---

### Example 4: High-Risk Assignment (B3) - Safety Trigger

**AI System**: Radiology diagnostic support AI (image analysis for cancer detection)

**Risk Assessment**:
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Autonomy | 1 | Human decision (radiologist makes final diagnosis, AI is support) |
| Reversibility | 4 | Difficult (diagnosis influences treatment pathway, delays costly) |
| Impact Scale | 3 | Organization-wide (hospital patient population) |
| Consequence | 5 | Severe (missed cancer = delayed treatment, potential death) |
| Data Sensitivity | 5 | Highly sensitive (PHI, medical imaging data) |
| Regulatory | 4 | High regulatory (HIPAA, potentially FDA as medical device) |
| **TOTAL** | **22** | |

**Assignment Logic**: Consequence = 5, Regulatory ≥ 4, Data Sensitivity = 5 → **B3 (High Risk)**

**Controls Required**: All 72 controls despite low autonomy—consequence severity requires maximum rigor

**Key Insight**: Even with "human-in-loop" design (low autonomy), severe safety consequences and regulatory requirements trigger B3.

---

### Example 5: Moderate-Risk Assignment (B2) - Scale Considerations

**AI System**: Content recommendation engine for streaming media platform

**Risk Assessment**:
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Autonomy | 4 | Supervised autonomy (recommendations auto-generated, periodic sampling) |
| Reversibility | 1 | Fully reversible (user can ignore recommendations) |
| Impact Scale | 5 | Society-wide (millions of users) |
| Consequence | 2 | Low (poor recommendation = minor user annoyance) |
| Data Sensitivity | 3 | Confidential (viewing history, user preferences) |
| Regulatory | 2 | Industry standards (content rating, age-appropriate content) |
| **TOTAL** | **17** | |

**Assignment Logic**: Autonomy ≥ 4, Impact Scale = 5, Total score 17 ≥ 13 → **B2 (Moderate Risk)**

**Controls Required**: 61 controls—despite low consequences, high scale and autonomy require comprehensive governance

**Key Insight**: Scale and autonomy drive moderate-risk designation even when individual consequences are low.

---

## Baseline Escalation and De-escalation

### When to Escalate Baseline

**Triggers for moving from B1→B2 or B2→B3**:
- System scope expands (more users, broader deployment)
- Autonomy increases (reduced human oversight)
- New regulatory requirements apply
- Incidents reveal higher risk than initially assessed
- Integration into critical workflows
- Stakeholder concerns or public scrutiny increases

**Process**:
1. Re-assess using risk characterization questions
2. Document changed risk factors
3. Identify new controls required from higher baseline
4. Create implementation plan for gap controls
5. Obtain governance approval for baseline change
6. Update profile and reassess maturity

---

### When to De-escalate Baseline

**Rare, but consider if**:
- System scope significantly reduced
- Human oversight substantially increased
- System retired from high-impact use cases
- Compensating controls reduce risk profile

**Requirements**:
- Formal risk assessment demonstrating reduced risk
- Governance approval required
- Documentation of compensating controls
- Bias toward maintaining baseline (de-escalation should be exceptional)

---

## Baseline Control Scope Details

### B1 (Low Risk) - Essential Controls (23)

**GOVERN Function** (10-12 controls):
- GOV-1.1: Legal/Regulatory Compliance Policies
- GOV-1.2: AI Use Scope Definition
- GOV-2.1: AI Accountability Assignment
- GOV-2.2: AI Competency Development (basic)
- GOV-2.3: Executive AI Oversight (basic)
- GOV-6.1: AI Governance Resourcing
- Plus select additional foundational governance controls

**MAP Function** (8-10 controls):
- MAP-1.1: AI System Purpose Documentation
- MAP-1.3: AI Strategic Alignment
- MAP-1.5: AI Risk Tolerance Definition
- MAP-1.6: AI System Requirements
- MAP-2.1: AI System Task Categorization
- MAP-3.3: AI Application Scope
- MAP-5.1: AI Impact Assessment (basic)
- Plus select foundational mapping controls

**MEASURE Function** (8-10 controls):
- MEA-1.1: AI Risk Measurement Selection
- MEA-2.1: AI Testing Documentation
- MEA-2.3: AI Performance Measurement
- MEA-2.4: AI Production Monitoring (basic)
- MEA-2.6: AI Safety Evaluation (basic)
- MEA-3.1: AI Continuous Risk Tracking (basic)
- MEA-4.3: AI Performance Change Detection
- Plus select core measurement controls

**MANAGE Function** (6-8 controls):
- MAN-1.1: AI Go/No-Go Decision
- MAN-1.2: AI Risk Prioritization
- MAN-1.3: AI Risk Response Planning
- MAN-1.4: AI Residual Risk Documentation
- MAN-4.1: AI Post-Deployment Monitoring
- MAN-4.3: AI Incident and Error Reporting
- Plus select essential management controls

---

### B2 (Moderate Risk) - Comprehensive Controls (61)

**All B1 controls PLUS**:

**GOVERN** (+5-6 controls):
- GOV-1.4: AI Governance Compliance Monitoring
- GOV-1.7: Third-Party AI Risk Management
- GOV-3.1: Interdisciplinary AI Teams
- GOV-4.1: AI Risk Culture Development
- GOV-4.2: AI Feedback Integration
- GOV-6.2: AI Governance Capability Development

**MAP** (+4-5 controls):
- MAP-1.2: AI Development Team Composition
- MAP-2.2: AI System Boundaries
- MAP-3.4: AI Operator Requirements
- MAP-3.5: Human Oversight Design
- MAP-4.1: Third-Party AI Risk Assessment
- MAP-4.2: Third-Party Risk Controls

**MEASURE** (+6-7 controls):
- MEA-1.3: AI Independent Evaluation (internal)
- MEA-2.2: AI Human Subject Testing
- MEA-2.5: AI Validity and Reliability
- MEA-2.7: AI Security and Resilience
- MEA-2.8: AI Transparency Evaluation
- MEA-2.9: AI Model Explanation
- MEA-2.10: AI Privacy Evaluation
- MEA-2.11: AI Fairness and Bias Testing
- MEA-3.3: AI User Feedback Processes
- MEA-4.1: AI Measurement-Context Alignment

**MANAGE** (+2-3 controls):
- MAN-2.1: AI Alternative Evaluation
- MAN-2.2: AI Value Preservation
- MAN-2.4: AI System Disengage/Deactivate
- MAN-3.1: Third-Party AI Ongoing Monitoring

---

### B3 (High Risk) - All Controls (72)

**All B1 and B2 controls PLUS**:

**GOVERN** (+2-3 controls):
- GOV-1.5: AI Environmental Impact Management
- GOV-1.6: AI System Decommissioning Policies
- GOV-3.2: Demographic Diversity in AI
- GOV-4.3: AI Transparency Communication
- GOV-5.1: AI Ecosystem Engagement
- GOV-5.2: AI Research Collaboration

**MAP** (+1-2 controls):
- MAP-2.3: AI Scientific Rigor
- MAP-3.1: AI Benefits Documentation (comprehensive)
- MAP-3.2: AI Cost Documentation (comprehensive)
- MAP-4.2: Third-Party Risk Controls (advanced)

**MEASURE** (+2-3 controls):
- MEA-1.2: AI Metric Validation
- MEA-2.12: AI Environmental Assessment
- MEA-2.13: AI Testing Effectiveness (meta-evaluation)
- MEA-3.2: AI Risk Assessment in Complex Contexts
- MEA-4.2: AI Results Expert Review (external)

**MANAGE** (+1-2 controls):
- MAN-2.3: AI Emergent Risk Response
- MAN-3.2: Pre-trained Model Management (advanced)
- MAN-4.2: AI Continuous Improvement Integration

---

## Special Baseline Considerations

### Multi-System Organizations

Organizations with diverse AI portfolios should:

1. **Assess each AI system independently** using risk characterization
2. **Assign baselines per system** based on risk profile
3. **Implement appropriate controls** for each baseline
4. **Track separately** in AI system registry

**Example Portfolio**:
```
Regional Hospital AI Portfolio:
├── B1: Staff scheduling optimization (internal, low risk)
├── B2: Patient appointment chatbot (customer-facing, moderate autonomy)
├── B2: Billing code suggestion (financial, moderate consequences)
└── B3: Radiology diagnostic support (patient safety, severe consequences)
```

Each system has its own baseline, control scope, and maturity assessment.

---

### Baseline Changes Over Time

**System Lifecycle Triggers**:
- **Pilot → Production**: May escalate baseline as scale increases
- **Limited → Expanded scope**: Escalate if impact/scale grows
- **Assisted → Autonomous**: Escalate if autonomy increases
- **General → Regulated domain**: Escalate if regulations apply

**Documentation Required**:
- Original baseline assignment with risk scores
- Trigger event description
- Updated risk assessment
- New baseline assignment
- Gap analysis (new controls required)
- Implementation timeline

---

## Integration with Profiles and Maturity

### Baseline → Profile → Maturity

**Step 1**: Determine baseline(s) using risk characterization
- Output: B1, B2, or B3 for each AI system

**Step 2**: Select or create profile
- Profiles select controls from one or more baselines
- Example: Healthcare profile selects 48 controls from B2 baseline
- Profiles can add controls beyond baseline minimum

**Step 3**: Assess maturity for each control
- ML1-5 assessment for every control in the profile
- Generates actual maturity score

**Step 4**: Calculate scores
- Profile Score: actual/target (target typically = ML3 per control)
- Baseline-Relative: actual/baseline maximum
- Framework-Relative: actual/framework maximum

---

## Baseline Validation and Approval

### Required Documentation

For each baseline assignment:
- [ ] Completed risk characterization questionnaire
- [ ] Score for each of 6 risk dimensions
- [ ] Total risk score calculation
- [ ] Baseline assignment logic applied
- [ ] Special considerations noted (escalation factors, regulatory drivers)
- [ ] Approver name and approval date

### Review and Reassessment

| Event | Action |
|-------|--------|
| **Annual review** | Re-assess all AI systems using questionnaire |
| **Significant system changes** | Immediate reassessment (scope, autonomy, data, deployment) |
| **Regulatory changes** | Review if new regulations affect risk profile |
| **Post-incident** | Reassess if incident reveals higher risk than assumed |
| **Audit findings** | Reassess if auditors identify risk underestimation |

---

## Common Baseline Selection Questions

### Q: Can different teams use different baselines for similar AI systems?

**A**: No—baseline should be consistent for AI systems with similar risk profiles. If Team A's chatbot is B1, Team B's similar chatbot should also be B1 unless material differences exist. Consistency ensures equitable governance.

### Q: Should we "round up" to a higher baseline to be safe?

**A**: Use the risk characterization methodology objectively. Over-scoping creates unnecessary overhead; under-scoping creates risk. The questionnaire is designed to assign appropriate baselines. Document your rationale either way.

### Q: What if we're uncertain between two baselines?

**A**: When uncertain between B1/B2 or B2/B3, choose the higher baseline. Risk tolerance should favor more comprehensive governance when ambiguous. Document the uncertainty and plan to reassess after operational experience.

### Q: Can we start with B1 and escalate to B2 later?

**A**: Yes, but only if the AI system's risk profile genuinely qualifies for B1 initially. Don't use B1 as a "training wheels" approach for a system that should be B2/B3 from the start. Assess risk honestly from day one.

### Q: How do pre-trained models affect baseline selection?

**A**: Assess the system as deployed, including the pre-trained model. A high-risk foundation model (e.g., GPT-4) deployed in a low-risk application (internal summarization) can still be B1. The deployment risk determines the baseline, not the model's inherent capabilities.

---

## References

- ISO/IEC 42001:2023 - Risk-based approach to AI management
- NIST AI RMF 1.0 - Risk assessment and management
- NIST 800-53 Rev. 5 - Security control baselines (low/moderate/high)
- NIST Cybersecurity Framework 2.0 - Profile methodology
- EU AI Act - Risk-based regulatory classification

---

**Next Document**: [Control Catalog](../core/AIMF-CONTROL-CATALOG.csv) | [Assessment Guide](AIMF-ASSESSMENT-GUIDE.md) | [Profiles Guide](AIMF-PROFILES-GUIDE.md)
