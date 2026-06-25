# Baseline Distribution Summary

**Change Control ID**: CP-2026-001
**Date**: 2026-01-29
**Status**: Phase 2 Complete

---

## Control Catalog Updates Complete

**Total Controls**: 72 (not 59 as originally stated, not 73 as initially updated)

### Column Structure Updated

**Renamed Columns**:
- `T1_Requirements` → `Implementation_Basic` (ML1-2 examples)
- `T2_Requirements` → `Implementation_Defined` (ML3 examples)
- `T3_Requirements` → `Implementation_Advanced` (ML4-5 examples)

**New Columns Added**:
- `Baseline_Applicability` (B1|B2|B3, B2|B3, or B3 only)
- `Default_Target_Maturity` (typically 3, some 2 or 4)

---

## Baseline Distribution

### Overall Framework Distribution

| Baseline | Controls | % of Framework | Control Applicability |
|----------|----------|----------------|-----------------------|
| **B1** (Low Risk) | 23 controls | 32% | B1\|B2\|B3 |
| **B2** (Moderate Risk) | 61 controls | 85% | B1\|B2\|B3 + B2\|B3 |
| **B3** (High Risk) | 72 controls | 100% | All controls |

**Breakdown**:
- 23 controls apply to **all baselines** (B1|B2|B3) — foundational/essential
- 38 controls apply to **B2 and B3 only** (B2|B3) — comprehensive/systematic
- 11 controls apply to **B3 only** (B3) — maximum rigor/external validation

---

## Function Distribution by Baseline

| Function | B1 Controls | B2 Controls | B3 Controls |
|----------|-------------|-------------|-------------|
| **GOVERN** | 6 | 14 | 19 |
| **MAP** | 7 | 17 | 18 |
| **MEASURE** | 5 | 18 | 22 |
| **MANAGE** | 5 | 12 | 13 |
| **TOTAL** | **23** | **61** | **72** |

### Observations

**B1 (Low Risk) - 23 controls (32%)**:
- Heavily weighted toward GOVERN and MAP functions (6+7 = 13 controls, 57% of B1)
- MEASURE and MANAGE have minimal requirements (5+5 = 10 controls, 43% of B1)
- Focus on **foundational governance and basic technical practices**

**B2 adds 38 controls (B2 total: 61 controls, 85%)**:
- Largest additions in MEASURE function (+13 controls)
- Significant MAP additions (+10 controls)
- Moderate GOVERN additions (+8 controls)
- Moderate MANAGE additions (+7 controls)
- Focus on **trustworthy AI characteristics, data governance, comprehensive risk management**

**B3 adds 11 controls (B3 total: 72 controls, 100%)**:
- Scattered across all functions (5+1+4+1)
- Focus on **external validation, public transparency, industry leadership, research-grade rigor**

---

## Baseline Assignment Logic Summary

### B1|B2|B3 (All Baselines) - 23 Foundational Controls

**Rationale**: Essential governance regardless of risk level

**Examples**:
- GOV-1.1: Legal/Regulatory Compliance Policies
- GOV-1.2: AI Use Scope Definition
- GOV-2.1: AI Accountability Assignment
- GOV-2.2: AI Competency Development
- GOV-2.3: Executive AI Oversight
- MAP-1.1: AI System Purpose Documentation
- MAP-1.3: AI Strategic Alignment
- MAP-1.5: AI Risk Tolerance Definition
- MEA-2.1: AI Testing Documentation
- MEA-2.3: AI Performance Measurement
- MEA-2.4: AI Production Monitoring
- MEA-2.6: AI Safety Evaluation
- MAN-1.1: AI Go/No-Go Decision
- MAN-1.2: AI Risk Prioritization
- MAN-4.3: AI Incident and Error Reporting

**Characteristics**: Basic policies, accountability, purpose documentation, testing, monitoring, safety, risk decisions

---

### B2|B3 Only - 38 Additional Controls

**Rationale**: Needed for moderate to high risk systems but not essential for low-risk

**Examples**:
- GOV-1.3: AI Lifecycle Governance (enterprise risk integration)
- GOV-1.4: AI Governance Compliance Monitoring (systematic)
- GOV-1.7: Third-Party AI Risk Management
- GOV-3.1: Interdisciplinary AI Teams
- MAP-4.1/4.2: Third-Party Risk Assessment and Controls
- MAP-5.1: AI Impact Assessment (comprehensive)
- MEA-2.7: AI Security and Resilience (adversarial testing)
- MEA-2.8: AI Transparency Evaluation
- MEA-2.9: AI Model Explanation (explainability)
- MEA-2.10: AI Privacy Evaluation
- MEA-2.11: AI Fairness and Bias Testing
- MAN-2.1: AI Alternative Evaluation
- MAN-2.4: AI System Disengage/Deactivate
- MAN-3.1: Third-Party AI Ongoing Monitoring

**Characteristics**: Data governance, privacy, fairness, security, explainability, third-party management, systematic processes

---

### B3 Only - 11 Specialized Controls

**Rationale**: Maximum rigor for high-risk/regulated systems only

**Examples**:
- GOV-1.5: AI Environmental Impact Management
- GOV-3.2: Demographic Diversity in AI
- GOV-4.3: AI Transparency Communication (public)
- GOV-5.1: AI Ecosystem Engagement (industry leadership)
- GOV-5.2: AI Research Collaboration
- MAP-2.3: AI Scientific Rigor (research-grade)
- MEA-1.2: AI Metric Validation (meta-evaluation)
- MEA-2.12: AI Environmental Assessment
- MEA-2.13: AI Testing Effectiveness (TEVV meta-evaluation)
- MEA-3.2: AI Risk Assessment in Complex Contexts
- MAN-4.2: AI Continuous Improvement Integration (systematic innovation)

**Characteristics**: Environmental impact, external validation, public transparency, research collaboration, industry leadership, meta-evaluation, continuous innovation

---

## Review Considerations

### B1 at 32% — Too Lean?

**Current State**: Only 23 controls for low-risk AI systems

**Pros**:
- Truly minimal overhead for low-risk applications
- Focuses on essential governance and accountability
- Allows small organizations/startups to adopt AI responsibly
- Prevents over-engineering for simple use cases

**Cons**:
- May be insufficient for comprehensive governance
- Only 5 MEASURE controls (limited quality assurance)
- Only 5 MANAGE controls (limited risk management)
- Organizations might struggle with only 32% of best practices

**Consideration**: Should more B2|B3 controls be moved to B1|B2|B3?

**Candidates for B1 inclusion**:
- MAP-5.1 (AI Impact Assessment) — currently B2|B3, arguably foundational
- MEA-2.5 (AI Validity and Reliability) — currently B2|B3, arguably essential for any AI
- MEA-2.9 (AI Model Explanation) — currently B2|B3, basic explainability could be foundational
- MAN-2.4 (AI System Disengage/Deactivate) — currently B2|B3, arguably essential safety control

**If these 4 moved to B1**: B1 would have 27 controls (~38%), B2 would have 65 controls (~90%)

---

### B2 at 85% — Very Comprehensive

**Current State**: 61 of 72 controls for moderate-risk AI

**Pros**:
- Comprehensive governance for customer-facing AI
- Strong data privacy, fairness, security coverage
- Addresses most regulatory expectations

**Cons**:
- High implementation burden (85% of framework)
- Small differentiation from B3 (only 11 controls difference)
- May be more than needed for true "moderate" risk

**Consideration**: Is 85% appropriate for moderate risk, or should more controls be B3-only?

**Candidates for B3-only**:
- Some of the "advanced" measurement controls with Maturity_Level_Min = 3
- Controls focused on "public reporting" or "external" validation
- Controls with "comprehensive" or "systematic" at B2 level might be optional

---

## Recommendations

### Option 1: Keep Current Distribution

Accept the 23/61/72 distribution as intentionally rigorous for B2:
- B1 is truly minimal (only essential governance)
- B2 is comprehensive (ready for serious enterprise AI)
- B3 adds only industry-leading/external validation

**Update documentation** to reflect this intentional design.

---

### Option 2: Rebalance to Target Distribution

Move select controls to achieve more balanced distribution:
- B1 target: 30-35 controls (~42-49%)
- B2 target: 50-55 controls (~69-76%)
- B3 remains: 72 controls (100%)

**Move 7-12 B2|B3 controls to B1|B2|B3**:
- Impact assessment, validity testing, explainability, disengage mechanisms
- Creates more gradual progression between baselines

---

### Option 3: Hybrid Approach

Keep B1 lean but add "B1+" variant:
- B1: 23 controls (minimum viable governance)
- B1+: 35 controls (recommended for B1, adds quality assurance)
- B2: 61 controls (comprehensive)
- B3: 72 controls (maximum)

**Uses existing B2|B3 controls** but makes some "highly recommended" for B1.

---

## Next Steps

**Decision Required**: Accept current 23/61/72 distribution or rebalance?

**If Accept**:
- Proceed to Phase 3 (Assessment Guide updates)
- Update profile documents to reference actual counts
- Document rationale for lean B1 approach

**If Rebalance**:
- Identify specific controls to move
- Update control catalog baseline applicability
- Recalculate distribution
- Update all documentation
- Re-run validation

---

**Current Status**: Awaiting decision before proceeding to Phase 3
