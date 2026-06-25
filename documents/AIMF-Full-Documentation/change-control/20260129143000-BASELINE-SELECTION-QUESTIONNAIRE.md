# AIMF Baseline Selection Questionnaire
## Risk Characterization for Baseline Assignment

**Version**: 1.0 (Draft)
**Date**: 2026-01-29
**Purpose**: Determine appropriate baseline (B1/B2/B3) based on AI system risk characteristics

---

## Overview

This questionnaire assesses AI system characteristics across six risk dimensions to determine the appropriate control baseline. Organizations should complete this for each AI system or system category.

**Baseline Outcomes**:
- **B1 (Low Risk)**: 30-35 foundational controls
- **B2 (Moderate Risk)**: 45-50 comprehensive controls
- **B3 (High Risk)**: All 73 controls with maximum rigor

---

## Risk Assessment Questions

### Question 1: Autonomy Level

**What level of human involvement exists in AI-driven decisions?**

| Score | Level | Description | Examples |
|-------|-------|-------------|----------|
| **1** | Human Decision | AI provides information/recommendations; human makes all decisions | Diagnostic support tool (doctor decides), product recommendations (user chooses) |
| **2** | Human-in-the-Loop | AI suggests action, human must approve before execution | Loan application screening (requires approval), resume screening (recruiter reviews) |
| **3** | Human-on-the-Loop | AI acts autonomously with human oversight; human can intervene | Fraud detection (auto-flags with review queue), automated trading (with circuit breakers) |
| **4** | Supervised Autonomy | AI acts autonomously with periodic human review | Automated content moderation (periodic audits), chatbot responses (sampled review) |
| **5** | Full Autonomy | AI acts independently without human review or approval | Autonomous vehicle navigation, automated medical dosing, automated credit decisions |

**Your Score**: _____

---

### Question 2: Decision Reversibility

**How easily can AI-driven outcomes be reversed or corrected?**

| Score | Level | Description | Examples |
|-------|-------|-------------|----------|
| **1** | Fully Reversible | Immediate, cost-free reversal | Email categorization, search rankings, content recommendations |
| **2** | Easily Reversible | Reversal possible with minimal cost/effort | Product returns, promotional offers, non-binding recommendations |
| **3** | Moderately Reversible | Reversal requires effort, cost, or time | Credit card fraud blocks (can be appealed), account suspensions (can be restored) |
| **4** | Difficult to Reverse | Significant cost, time, or reputational impact | Employment decisions (appeal process), insurance claims (dispute process) |
| **5** | Irreversible | Cannot be undone or has permanent consequences | Medical treatment decisions, autonomous vehicle actions, physical safety events |

**Your Score**: _____

---

### Question 3: Impact Scale & Scope

**How many people or entities are directly affected by AI decisions?**

| Score | Level | Description | Examples |
|-------|-------|-------------|----------|
| **1** | Individual/Internal | Single users or internal employees only | Personal productivity tool, internal workflow automation |
| **2** | Small Group | Defined small group (<100 people) | Department tool, small customer segment |
| **3** | Organization-Wide | All employees or substantial customer base (100-10,000) | Enterprise AI tool, mid-market customer base |
| **4** | Large Scale | Significant public or large customer base (10,000-1M) | Major platform, large enterprise, regional deployment |
| **5** | Society-Wide | Broad public impact or vulnerable populations at scale (>1M) | Public-facing government AI, critical infrastructure, mass consumer applications |

**Your Score**: _____

---

### Question 4: Consequence Severity

**What is the potential harm if the AI system makes errors?**

| Score | Level | Description | Examples |
|-------|-------|-------------|----------|
| **1** | Negligible | Minor inconvenience, no lasting impact | Music playlist errors, minor UI annoyances |
| **2** | Low | Temporary inconvenience, easily remedied | Incorrect product suggestion, misfiled document |
| **3** | Moderate | Financial loss, wasted time, frustration | Incorrect billing, service delays, customer complaints |
| **4** | Significant | Substantial financial loss, reputational harm, regulatory consequences | Unfair credit denial, discriminatory hiring, privacy breach |
| **5** | Severe | Physical harm, major financial loss, civil rights violation, life-safety impact | Medical diagnosis errors, autonomous vehicle accidents, wrongful arrests |

**Your Score**: _____

---

### Question 5: Data Sensitivity

**What is the sensitivity level of data processed by the AI system?**

| Score | Level | Description | Examples |
|-------|-------|-------------|----------|
| **1** | Public | Publicly available data only | Weather data, public records, general knowledge |
| **2** | General Business | Non-sensitive business data | Product catalogs, general customer preferences, anonymized analytics |
| **3** | Confidential | Proprietary or personal data | Email content, customer contact info, business confidential data |
| **4** | Regulated Personal | PII, financial data, or regulated data | SSN, credit scores, financial records, employment records |
| **5** | Highly Sensitive | PHI, biometric, children's data, or special category data | Medical records, genetic data, children's information, protected class data |

**Your Score**: _____

---

### Question 6: Regulatory Environment

**What regulatory or compliance obligations apply to the AI system?**

| Score | Level | Description | Examples |
|-------|-------|-------------|----------|
| **1** | General | Standard business regulations only | General consumer protection, basic data protection |
| **2** | Industry Standards | Industry best practices or voluntary standards | Industry codes of conduct, certification programs |
| **3** | Sector-Specific | Specific regulatory requirements | GLBA (financial), general HIPAA (healthcare), employment laws |
| **4** | High Regulatory | Stringent regulatory oversight or government scrutiny | FDA-regulated medical devices, fair lending laws, government AI |
| **5** | Critical Regulated | Life-safety regulation, civil rights mandates, or critical infrastructure | Medical device safety, autonomous vehicle regulation, law enforcement AI, critical infrastructure protection |

**Your Score**: _____

---

## Scoring & Baseline Assignment

### Step 1: Calculate Total Score

Sum your scores from all six questions:

```
Question 1 (Autonomy):        _____
Question 2 (Reversibility):   _____
Question 3 (Impact Scale):    _____
Question 4 (Consequence):     _____
Question 5 (Data Sensitivity):_____
Question 6 (Regulatory):      _____

TOTAL SCORE:                  _____  (out of 30)
```

---

### Step 2: Apply Baseline Assignment Rules

#### Rule 1: High-Risk Threshold (B3 Assignment)

**Assign B3 (High Risk) if ANY of the following are true:**

- [ ] **Any individual question score ≥ 5** (maximum severity in any dimension)
- [ ] **Question 4 (Consequence) ≥ 4** (significant or severe harm potential)
- [ ] **Question 6 (Regulatory) ≥ 4** (critical regulatory requirements)
- [ ] **Total Score ≥ 21** (consistently high risk across dimensions)

**If any box is checked → Baseline B3 (High Risk)**

---

#### Rule 2: Moderate-Risk Threshold (B2 Assignment)

**If not B3, assign B2 (Moderate Risk) if ANY of the following are true:**

- [ ] **Any individual question score ≥ 4** (high severity in any dimension)
- [ ] **Two or more questions score ≥ 3** (multiple moderate-high risk factors)
- [ ] **Total Score ≥ 13** (aggregate moderate risk)

**If any box is checked → Baseline B2 (Moderate Risk)**

---

#### Rule 3: Low-Risk Assignment (B1 Assignment)

**If not B3 or B2, assign B1 (Low Risk):**

- [ ] **All questions score ≤ 3** (no high-severity factors)
- [ ] **Majority of questions score ≤ 2** (mostly low risk)
- [ ] **Total Score ≤ 12** (aggregate low risk)

**If conditions met → Baseline B1 (Low Risk)**

---

## Baseline Determination

**Your AI System**: _________________________________

**Total Risk Score**: _____ / 30

**Baseline Assignment**:

- [ ] **B1 (Low Risk)** - 30-35 foundational controls
- [ ] **B2 (Moderate Risk)** - 45-50 comprehensive controls
- [ ] **B3 (High Risk)** - All 73 controls

**Rationale**: _______________________________________________________________

_______________________________________________________________

---

## Example Scenarios

### Example 1: Internal Chatbot for Employee HR Questions

| Question | Score | Rationale |
|----------|-------|-----------|
| Autonomy | 2 | Human-in-loop (employee decides whether to follow advice) |
| Reversibility | 1 | Fully reversible (just information) |
| Impact Scale | 3 | Organization-wide (all employees) |
| Consequence | 2 | Low (incorrect info causes minor confusion) |
| Data Sensitivity | 3 | Confidential (employee questions may be personal) |
| Regulatory | 1 | General (standard employment law) |
| **TOTAL** | **12** | **→ B1 (Low Risk)** |

---

### Example 2: Credit Decisioning AI for Consumer Loans

| Question | Score | Rationale |
|----------|-------|-----------|
| Autonomy | 4 | Supervised autonomy (periodic review, not every decision) |
| Reversibility | 4 | Difficult (appeals exist but reputational harm) |
| Impact Scale | 4 | Large scale (thousands of applicants) |
| Consequence | 4 | Significant (unfair denial = financial harm) |
| Data Sensitivity | 4 | Regulated (credit data, financial history) |
| Regulatory | 5 | Critical (FCRA, ECOA, fair lending laws) |
| **TOTAL** | **25** | **→ B3 (High Risk)** - Regulatory ≥4, Total ≥21 |

---

### Example 3: Medical Diagnostic Support Tool (Radiology)

| Question | Score | Rationale |
|----------|-------|-----------|
| Autonomy | 1 | Human decision (radiologist makes final diagnosis) |
| Reversibility | 4 | Difficult (diagnosis influences treatment, delays) |
| Impact Scale | 3 | Organization-wide (hospital patient population) |
| Consequence | 5 | Severe (misdiagnosis = wrong treatment, harm) |
| Data Sensitivity | 5 | Highly sensitive (PHI, medical images) |
| Regulatory | 4 | High regulatory (HIPAA, potentially FDA) |
| **TOTAL** | **22** | **→ B3 (High Risk)** - Consequence ≥4, Total ≥21 |

---

### Example 4: Fraud Detection for E-Commerce Platform

| Question | Score | Rationale |
|----------|-------|-----------|
| Autonomy | 3 | Human-on-loop (auto-flags for review) |
| Reversibility | 3 | Moderate (account restoration, some customer friction) |
| Impact Scale | 4 | Large scale (thousands of daily transactions) |
| Consequence | 3 | Moderate (false positives = customer frustration, lost sales) |
| Data Sensitivity | 4 | Regulated (payment data, PII) |
| Regulatory | 3 | Sector-specific (PCI-DSS, consumer protection) |
| **TOTAL** | **20** | **→ B2 (Moderate Risk)** - Multiple scores ≥3, Total ≥13 |

---

### Example 5: Content Recommendation Engine (Streaming Service)

| Question | Score | Rationale |
|----------|-------|-----------|
| Autonomy | 4 | Supervised autonomy (recommendations auto-generated, sampled review) |
| Reversibility | 1 | Fully reversible (user can ignore) |
| Impact Scale | 5 | Society-wide (millions of users) |
| Consequence | 2 | Low (bad recommendation = user annoyance) |
| Data Sensitivity | 3 | Confidential (viewing history, preferences) |
| Regulatory | 2 | Industry standards (content rating compliance) |
| **TOTAL** | **17** | **→ B2 (Moderate Risk)** - Autonomy ≥4, Scale ≥4, Total ≥13 |

---

## Special Considerations

### Portfolio Approach

Organizations with multiple AI systems should:
1. Assess each AI system or system category separately
2. Assign baselines per system based on risk
3. An organization may have systems across all three baselines simultaneously

**Example**: A hospital might have:
- B1: Internal staff scheduling AI
- B2: Patient chatbot for appointment booking
- B3: Diagnostic imaging AI

---

### Baseline Escalation Triggers

**Consider upgrading to next baseline if:**
- System use expands beyond initial scope (more users, more autonomy)
- New regulatory requirements emerge
- Incidents or near-misses reveal higher risk than anticipated
- Stakeholder concerns indicate reputational risk
- System integrated into critical workflows

---

### Baseline De-escalation

**Rare, but consider if:**
- System scope reduced significantly (fewer users, less autonomy)
- System retired from high-impact use cases
- Compensating controls reduce risk (e.g., human review added)

**Requires documentation and approval** - bias should be toward maintaining or escalating baseline, not de-escalating.

---

## Validation & Documentation

### Required Documentation

For each baseline assignment, document:
- [ ] Completed questionnaire with scores
- [ ] Rationale for each question's score
- [ ] Baseline determination logic applied
- [ ] Any special considerations or escalation factors
- [ ] Approver name and date

### Review Frequency

- **Annual review** of baseline assignments
- **Immediate review** if system changes significantly
- **Triggered review** after incidents or regulatory changes

---

## Appendix: Baseline Control Summaries

### B1 (Low Risk) - 30-35 Controls

**Focus**: Foundational governance, basic risk awareness, minimal TEVV

**Key Controls**:
- Basic AI policies and accountability
- Purpose documentation and categorization
- Basic testing and monitoring
- Essential risk assessment
- Go/no-go decision processes

**Suitable For**:
- Internal productivity tools
- Low-impact recommendations
- Non-autonomous systems
- Easily reversible outcomes
- Limited scope deployments

---

### B2 (Moderate Risk) - 45-50 Controls

**Focus**: Comprehensive governance, systematic processes, trustworthy AI characteristics

**Key Controls**:
- Formal governance committees and RACI
- Data governance and privacy controls
- Comprehensive TEVV and fairness testing
- Risk management and incident response
- Production monitoring and maintenance

**Suitable For**:
- Customer-facing AI systems
- Moderate autonomy with oversight
- Regulated industries (standard requirements)
- Large-scale deployments
- Significant business impact

---

### B3 (High Risk) - 73 Controls (All)

**Focus**: Maximum rigor, external validation, public transparency, research-grade practices

**Key Controls**:
- Independent oversight and external validation
- Real-time monitoring with predictive analytics
- Public transparency and reporting
- Advanced TEVV with independent assessment
- Comprehensive third-party and supply chain risk management

**Suitable For**:
- Autonomous decision-making systems
- Life-safety or health applications
- Civil rights impact (employment, credit, law enforcement)
- Critical infrastructure
- Stringent regulatory environments

---

**End of Questionnaire**
