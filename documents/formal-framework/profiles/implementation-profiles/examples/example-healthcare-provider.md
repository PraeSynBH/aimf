# AI Management Framework (AIMF) by PraeSyn
## Implementation Profile Example: Metro Regional Health System

**© 2026 PraeSyn, LLC. All rights reserved.**
Licensed under CC BY-NC-ND 4.0

**Organization Name**: Metro Regional Health System (fictional example)
**Profile Name**: MRHS Clinical AI Governance Implementation Profile v1.0
**Version**: 1.0
**Date Created**: February 1, 2026
**Last Updated**: February 1, 2026
**Owner**: Dr. Maria Rodriguez, Chief Medical Information Officer (CMIO)
**Status**: Active

---

## Profile Overview

### Purpose
This implementation profile establishes AI governance for Metro Regional Health System (MRHS), a 4-hospital regional health system serving 800,000 patients annually with 5,000 employees. Our AI systems support clinical decision-making, diagnostic imaging analysis, and operational efficiency. Patient safety and HIPAA compliance are paramount.

### Scope
- **Business Units**: Clinical Operations, Radiology, Emergency Department, IT/Informatics, Quality & Safety
- **AI Systems Covered**:
  - **Radiology AI** (chest X-ray, CT scan analysis) - FDA-cleared Class II medical device
  - **Sepsis prediction model** (ICU early warning system) - high-risk clinical decision support
  - **Patient no-show prediction** (scheduling optimization) - moderate risk, operational
  - **Clinical documentation assistant** (ambient AI scribe) - moderate risk, PHI-processing
- **Implementation Timeline**: 18 months (Q1 2026 - Q2 2027)
- **Resource Allocation**: 5 FTE (2 clinical informatics, 1 IT, 1 quality/safety, 1 compliance), $400K budget, external clinical AI consultant

### Profile Foundation
**Based on Framework Profile(s)**:
- Primary: **Healthcare Profile** (patient safety, HIPAA, clinical validation)
- Secondary influences: **High-Assurance Profile** for sepsis prediction system (life-safety critical)

**Customizations**:
- Added all MEASURE controls from High-Assurance for sepsis model (B3 requirements)
- De-prioritized GOV-1.5 (Environmental Impact) - not a strategic priority for health system
- Enhanced MEA-2.2 (Human Subject Testing) to align with IRB (Institutional Review Board) procedures
- Enhanced GOV-4.2 (Stakeholder Feedback) to include patient advisory council

---

## Control Selection

### Control Selection by AI System

Different AI systems have different control requirements based on risk:

| AI System | Risk Level | Profile Basis | baseline | Controls |
|-----------|-----------|---------------|------|----------|
| **Sepsis Prediction Model** | **High** | High-Assurance | **B3** | All 72 controls |
| **Radiology AI (FDA-cleared)** | **Moderate-High** | Healthcare | **B2-B3** | 62 controls (Healthcare profile) |
| **Clinical Documentation Assistant** | **Moderate** | Healthcare | **B2** | 62 controls (Healthcare profile) |
| **No-Show Prediction** | **Low** | Foundational | **B1** | 35 controls (Foundational) |

**Note**: This profile documents requirements for **Sepsis Prediction** (B3) and **Radiology AI** (B2-B3). Other systems follow simplified profiles.

### Control Summary (Sepsis Prediction System)

| Function | Healthcare Profile | High-Assurance Additions | Total for Sepsis Model |
|----------|-------------------|-------------------------|----------------------|
| GOVERN   | 16                | 3 (GOV-1.5, GOV-5.2, GOV-6.2) | 19                   |
| MAP      | 16                | 3 (MAP-1.2, MAP-2.3, MAP-4.2) | 19                   |
| MEASURE  | 19                | 3 (MEA-1.3, MEA-2.12, MEA-4.1) | 22                   |
| MANAGE   | 11                | 2 (MAN-2.1, MAN-2.3) | 13                   |
| **Total**| **62**            | **11**              | **72 (100% coverage)** |

### Controls Enhanced Beyond Healthcare Profile

| Control ID | Enhancement | Rationale |
|------------|-------------|-----------|
| MEA-2.6 (Safety Evaluation) | Independent clinical validation by external experts + FDA post-market surveillance | Sepsis model is life-safety critical; require highest rigor |
| MEA-2.2 (Human Subject Testing) | Full IRB oversight for all clinical AI research and validation | Align with Common Rule and institutional research standards |
| GOV-2.3 (Executive Oversight) | Board of Trustees quarterly AI safety review | High-risk AI warrants board-level accountability |
| GOV-4.2 (Stakeholder Feedback) | Patient advisory council for AI systems affecting care | Patient-centered care principles require patient input |

### Controls De-prioritized

| Control ID | Framework Profile | Rationale | Risk Acceptance |
|------------|------------------|-----------|-----------------|
| GOV-1.5 (Environmental Impact) | Healthcare | Not strategic priority; health system focuses on clinical outcomes. Future consideration for sustainability initiatives. | Dr. Maria Rodriguez (CMIO), Feb 2026 |

---

## Implementation Strategy

### Implementation baseline Selection

**baseline Alignment by AI System**:

| AI System | Clinical Risk | HIPAA Risk | baseline | Rationale |
|-----------|--------------|-----------|------|-----------|
| Sepsis Prediction Model | **High** (life-safety) | **High** (PHI) | **B3** | Autonomous alerts; directly affects clinical decisions; potential patient harm if incorrect |
| Radiology AI | **Moderate-High** (diagnostic) | **High** (PHI) | **B2-B3** | FDA-cleared; clinician review required; significant diagnostic impact |
| Clinical Documentation Assistant | **Moderate** (documentation quality) | **High** (PHI) | **B2** | Ambient AI processes patient conversations; HIPAA-critical but not life-safety |
| Patient No-Show Prediction | **Low** (operational) | **Moderate** (demographics) | **B1** | Scheduling optimization; no clinical decisions; limited PHI |

**Default baseline**: B2 for any new clinical AI systems unless risk assessment determines B3 required

### Phased Implementation Plan

#### Phase 1: Clinical Governance Foundation (Q1-Q2 2026 - Months 1-6)
**Focus**: Establish clinical AI committee, patient safety integration, HIPAA baseline

**Priority Controls**:
1. **GOV-2.1**: Clinical AI Committee charter (clinician-led, multidisciplinary)
2. **GOV-1.1**: Legal/Regulatory Compliance (HIPAA, FDA, state laws)
3. **GOV-2.3**: Board-level oversight for high-risk AI (sepsis model)
4. **MAP-5.1**: Clinical impact assessment framework
5. **GOV-1.4**: Integration with hospital quality/safety committee
6. **MEA-2.10**: HIPAA privacy impact assessments for all AI systems

**Deliverables**:
- Clinical AI Committee operational (monthly meetings)
- AI safety integration with existing patient safety reporting
- HIPAA-compliant AI data governance policies
- Risk stratification framework (link AI risk to patient safety risk categories)
- Board AI safety report (quarterly)

**Resources Required**:
- 2 FTE (clinical informatics lead + compliance officer)
- $80K (external consultant for governance design, HIPAA assessment)

**FDA Coordination**: Engage FDA for post-market surveillance planning (radiology AI, sepsis model)

#### Phase 2: Clinical Validation & Safety (Q2-Q4 2026 - Months 6-12)
**Focus**: Rigorous clinical validation, safety evaluation, explainability for clinicians

**Priority Controls**:
1. **MEA-2.6**: Safety evaluation with clinical experts (independent validation)
2. **MEA-2.5**: Validity/reliability assessment (clinical validation studies)
3. **MEA-2.2**: IRB oversight for clinical AI research
4. **MEA-2.9**: Clinician-appropriate model explanations
5. **MEA-2.11**: Fairness assessment across patient demographics
6. **MAP-3.5**: Human oversight requirements (clinician in the loop)
7. **MEA-2.3**: Clinical performance metrics (sensitivity, specificity, PPV, NPV)

**Deliverables**:
- **Sepsis Model**: Prospective clinical validation study (IRB-approved, 6-month study)
- **Radiology AI**: Retrospective validation with diverse patient population (race, age, imaging quality)
- Fairness analysis by patient demographics (age, sex, race, insurance status)
- Explainability interface for clinicians (feature importance, prediction rationale)
- Human oversight protocols (when clinician must review AI recommendations)

**Resources Required**:
- 3 FTE (2 clinical informatics + 1 data analyst)
- $150K (IRB submission, clinical validation study costs, external statistical consultant)

**Key Milestone**: Sepsis model validation complete before production deployment (Q4 2026 target)

#### Phase 3: Operational Deployment & Monitoring (Q1-Q2 2027 - Months 12-18)
**Focus**: Production deployment, continuous monitoring, incident response

**Priority Controls**:
1. **MAN-4.1**: Post-deployment monitoring (model performance + clinical outcomes)
2. **MAN-1.3**: AI incident response integrated with patient safety event reporting
3. **MEA-3.1**: Real-time clinical performance dashboards
4. **MAN-2.4**: Emergency disengage procedures (clinician override)
5. **MAN-4.2**: Continuous improvement (quarterly model reviews)
6. **GOV-6.2**: Clinical AI training for physicians, nurses, IT staff

**Deliverables**:
- Real-time dashboards: model performance, clinical outcomes (sepsis mortality rate, radiology diagnostic accuracy)
- AI incident response playbook (integrated with patient safety event system)
- Emergency override procedures tested and documented
- Quarterly clinical AI safety report to Medical Executive Committee
- Staff training program (500+ clinicians trained on AI systems)

**Resources Required**:
- 2 FTE (MLOps engineer + clinical quality analyst)
- $170K (monitoring platform, training development, dashboards)

**FDA Post-Market**: Quarterly post-market surveillance reports for FDA-cleared AI (radiology)

---

## Regulatory and Standards Alignment

### Regulatory Drivers

**Primary Regulations**:
- **HIPAA Privacy Rule**: All AI systems process protected health information (PHI)
- **HIPAA Security Rule**: Security risk analysis required for AI infrastructure
- **FDA 21 CFR Part 880**: Radiology AI is FDA-cleared Class II medical device; sepsis model may require Software as Medical Device (SaMD) clearance
- **CLIA**: Clinical Laboratory Improvement Amendments (if diagnostic AI used for patient care decisions)
- **State Medical Practice Acts**: AI must not practice medicine without physician oversight

**Secondary Considerations**:
- **The Joint Commission Standards**: Patient safety standards apply to AI systems
- **CMS Conditions of Participation**: Medicare/Medicaid compliance for AI in covered services
- **42 CFR Part 2**: Substance use disorder records (if AI processes SUD data)
- **Executive Order 14110**: Federal AI safety requirements (if accepting federal research funding for AI)

### Standards Compliance Mapping

| Standard | Requirements | AIMF Controls Addressing |
|----------|-------------|-------------------------|
| **HIPAA Privacy Rule** | PHI minimum necessary, patient access, accounting of disclosures | MEA-2.10, GOV-1.1, MAP-1.3 |
| **HIPAA Security Rule** | Risk analysis, access controls, audit logging, encryption | MEA-2.7, GOV-1.4, MAN-4.1 |
| **FDA Total Product Lifecycle** | Design controls, validation, post-market surveillance | MEA-2.1, MEA-2.5, MEA-2.6, MAN-4.1 |
| **ISO 42001 (target cert)** | AI management system (future certification goal) | All 72 controls for sepsis model |
| **NIST AI RMF** | GOVERN, MAP, MEASURE, MANAGE functions | All controls map to NIST subcategories |
| **Joint Commission (LD.04.03.05)** | Patient safety culture, event reporting | GOV-4.1, MAN-1.3 |

---

## Current Maturity Assessment

### Maturity Baseline (as of February 1, 2026)

**Assessment Methodology**: Self-assessment with external clinical AI consultant validation

| Dimension | Current Level | Target Level (Q2 2027) | Gap |
|-----------|--------------|----------------------|-----|
| Governance & Accountability | **Level 2** (Developing) | **Level 4** (Managed) | Need clinical AI committee, board oversight, formal policies |
| Data Management & Privacy | **Level 3** (Defined) | **Level 4** (Managed) | Strong HIPAA compliance; formalize AI-specific data quality controls |
| Technical Operations & MLOps | **Level 2** (Developing) | **Level 4** (Managed) | Limited MLOps; need rigorous TEVV, monitoring, incident response |
| Organizational Culture & Capabilities | **Level 2** (Developing) | **Level 3** (Defined) | Clinical awareness varies; need systematic training, risk culture |
| **Overall Maturity** | **Level 2.25** | **Level 3.75** | **Large gap; 18-month implementation justified** |

### Key Gaps Identified

1. **Clinical Validation Rigor**: Radiology AI deployed without prospective validation; retrospective analysis only
   - **Impact**: Unknown real-world performance; potential patient safety risk
   - **Priority**: **Critical**
   - **Controls Addressing**: MEA-2.5, MEA-2.6, MEA-2.2
   - **Mitigation**: Immediate retrospective validation; prospective study for sepsis model before deployment

2. **Sepsis Model Not Yet Validated**: Under development; no clinical validation or safety evaluation
   - **Impact**: Cannot deploy until rigorous validation complete (IRB study required)
   - **Priority**: **Critical**
   - **Controls Addressing**: MEA-2.6, MEA-2.2, MEA-2.5, GOV-2.3
   - **Mitigation**: Phase 2 clinical validation study (6 months); independent expert review

3. **No Fairness Testing Across Patient Demographics**: AI systems not tested for disparities by race, age, insurance
   - **Impact**: Potential health equity issues; bias could harm vulnerable populations
   - **Priority**: **High**
   - **Controls Addressing**: MEA-2.11, MAP-1.2 (team diversity)
   - **Mitigation**: Retrospective fairness analysis (Q2 2026); prospective monitoring in Phase 3

4. **Limited Post-Deployment Monitoring**: Manual quarterly reviews; no real-time clinical outcome tracking
   - **Impact**: Model degradation or patient safety issues may go undetected
   - **Priority**: **High**
   - **Controls Addressing**: MAN-4.1, MEA-3.1
   - **Mitigation**: Automated dashboards in Phase 3; interim monthly manual reviews

5. **No AI Incident Response Procedures**: Relies on general IT incident response; no clinical AI-specific protocols
   - **Impact**: Delayed response to AI safety events; potential patient harm
   - **Priority**: **Medium**
   - **Controls Addressing**: MAN-1.3, MAN-2.4
   - **Mitigation**: Draft playbook in Phase 1; full integration in Phase 3

---

## Organization-Specific Considerations

### Unique Requirements

**Clinical Context**:
- **Patient safety culture**: AI governance must integrate with existing Just Culture and patient safety event reporting
- **Clinician autonomy**: Physicians must have final decision authority; AI as decision support, not decision replacement
- **Health equity focus**: Serve diverse community (40% minority patients); fairness and bias testing critical
- **Regulatory complexity**: FDA (devices), HIPAA (privacy), state medical boards (practice of medicine), Joint Commission (accreditation)

**Technical Environment**:
- **Epic EHR system**: AI must integrate with Epic workflows; use Epic's AI governance tools where applicable
- **On-premises data center**: PHI cannot leave data center; cloud AI services limited to de-identified data
- **Vendor AI reliance**: Radiology AI is third-party vendor; limited control over model updates

### Stakeholder Engagement

**Key Stakeholders**:
| Stakeholder Group | Role in Implementation | Engagement Frequency |
|------------------|----------------------|---------------------|
| **Clinical AI Committee** (CMIO-led) | Policy approval, risk oversight, clinical validation | Monthly |
| **Board of Trustees** | High-risk AI oversight (sepsis model) | Quarterly |
| **Medical Executive Committee** | Physician engagement, credentialing for AI use | Quarterly |
| **Quality & Patient Safety Committee** | Incident review, safety integration | Monthly |
| **IT Steering Committee** | Technical architecture, budget | Monthly |
| **Privacy/Compliance (HIPAA Officer)** | HIPAA compliance, risk assessment | Bi-weekly (Phase 1-2), monthly (Phase 3) |
| **Legal Counsel** | Regulatory compliance, liability | As needed |
| **IRB (Institutional Review Board)** | Human subjects research oversight | Per study protocol |
| **Patient Advisory Council** | Patient perspective on AI systems | Quarterly |

### Change Management

**Communication Strategy**:
- **Physician communication**: Medical staff meetings, one-on-one CMIO discussions, Champions program (early adopters)
- **Nurse communication**: Nursing leadership meetings, unit huddles, nursing AI champions
- **Patient communication**: Website transparency about AI use, consent process for AI-involved care
- **Staff training**: Role-based (physicians, nurses, IT), hands-on simulations, ongoing education

**Resistance Mitigation**:
- **Physician concern**: "AI will replace clinical judgment or increase liability"
  - **Mitigation**: Emphasize decision support role; malpractice insurance consultation; clinician override always available
- **Nurse concern**: "More technology burden, less patient time"
  - **Mitigation**: Demonstrate workflow efficiency gains (documentation assistant); involve nurses in design
- **Patient concern**: "AI making decisions about my care without my knowledge"
  - **Mitigation**: Transparency in consent process; patient advisory council input; opt-out option where clinically appropriate
- **IT concern**: "Complex integration, support burden"
  - **Mitigation**: Phased deployment; vendor support agreements; MLOps investment

---

## Success Criteria and Metrics

### Profile Implementation Complete When:

- [ ] All 72 controls implemented at B3 baseline for sepsis prediction model
- [ ] All 62 controls implemented at B2-B3 baseline for radiology AI
- [ ] Clinical validation studies complete with independent expert review
- [ ] IRB approval obtained for sepsis model validation study
- [ ] Fairness testing demonstrates no significant disparities (>5% difference) across patient demographics
- [ ] Post-deployment monitoring operational with real-time dashboards
- [ ] Zero preventable patient harm events attributed to AI systems
- [ ] FDA post-market surveillance compliant for radiology AI
- [ ] Maturity Level 3.75+ achieved (target: Level 4 for governance and technical)
- [ ] Board of Trustees and Medical Executive Committee sign-off

### Key Performance Indicators (KPIs)

**Patient Safety KPIs** (Primary):
- **AI-related patient safety events**: 0 high-severity events (target)
- **Sepsis mortality rate**: Maintain or improve vs. baseline (measure AI impact)
- **Radiology diagnostic accuracy**: ≥95% sensitivity/specificity vs. radiologist ground truth
- **Clinician override rate**: <5% (indicates appropriate AI recommendations)

**Clinical Quality KPIs**:
- **Sepsis early detection**: Detect 80% of sepsis cases >6 hours before current standard of care
- **Radiology turnaround time**: 20% reduction in report turnaround (AI efficiency)
- **Documentation quality**: 90% completeness for AI-assisted clinical notes

**Governance KPIs**:
- **Clinical AI Committee meetings**: 100% monthly cadence, quorum achieved
- **Board reporting**: Quarterly AI safety reports to Board (100% on-time)
- **Incident response time**: <1 hour for high-severity AI incidents (clinician notification + system review)

**Compliance KPIs**:
- **HIPAA audits**: 100% pass rate for AI systems (annual audit)
- **FDA post-market surveillance**: 100% on-time reporting (quarterly)
- **IRB compliance**: 100% protocol adherence for clinical validation studies

**Fairness/Equity KPIs**:
- **Demographic performance parity**: <5% difference in model performance across race, age, sex, insurance status
- **Health equity monitoring**: Quarterly review of AI impact on vulnerable populations

### Progress Tracking

**Reporting Cadence**:
- **Clinical AI Committee**: Monthly
- **Medical Executive Committee**: Quarterly
- **Board of Trustees**: Quarterly (high-risk AI)
- **Quality & Patient Safety**: Monthly incident reports

**Report Recipients**: CMIO, CMO, CIO, CEO, General Counsel, Board Quality Committee

**Escalation Path**:
- **Clinical safety concerns**: CMIO → CMO → CEO → Board (immediate)
- **Regulatory compliance**: Compliance Officer → General Counsel → CEO
- **Technical issues**: IT Director → CIO → CMIO

---

## Risk Management

### Residual Risks

| Risk ID | Risk Description | Controls Applied | Residual Risk Level | Acceptance |
|---------|-----------------|------------------|-------------------|------------|
| R-001 | **Sepsis model false negatives** (missed sepsis cases despite AI alert) | MEA-2.6, MEA-2.5, MAN-4.1, MAP-3.5 (clinician oversight) | **Medium** | Dr. Maria Rodriguez (CMIO), Feb 2026. Clinical validation targets 80% sensitivity; accept 20% miss rate given current standard of care limitations. Continuous monitoring required. |
| R-002 | **Radiology AI vendor model updates** without our validation | MAP-4.1, MAN-3.1, contractual audit rights | **Medium** | Dr. James Lee (Chief of Radiology), Feb 2026. Contract requires notification + validation data; accept vendor-driven updates with post-deployment validation. |
| R-003 | **Fairness bias in radiology AI** (vendor-trained model may not represent our patient population) | MEA-2.11, MEA-2.5 (local validation) | **Medium** | Dr. Rodriguez (CMIO), Feb 2026. Local retrospective validation in Phase 2 addresses; accept until validation complete (monitor for disparities). |
| R-004 | **Patient consent complexity** for AI-involved care | GOV-1.1, GOV-4.2 (patient advisory), MAP-1.3 | **Low** | General Counsel, Feb 2026. General consent includes AI language; specific consent for research; accept standard consent for clinical AI. |

### Implementation Risks

| Risk | Likelihood | Impact | Mitigation Strategy |
|------|-----------|--------|-------------------|
| **Sepsis model validation fails to meet safety targets** | **Medium** | **Critical** | Extend validation study; engage external experts; have fallback plan to delay deployment |
| **Physician resistance to AI adoption** | **Medium** | **High** | Champions program; involve physicians in design; demonstrate clinical value early; voluntary adoption initially |
| **HIPAA breach from AI system misconfiguration** | **Low** | **Critical** | Security risk analysis (Phase 1); penetration testing; access controls; audit logging; incident response readiness |
| **FDA enforcement action on sepsis model** (if SaMD determination) | **Low** | **High** | Proactive FDA engagement; consider 510(k) clearance pathway; maintain rigorous documentation |
| **Budget overrun** | **Medium** | **Medium** | Prioritize sepsis and radiology AI; defer clinical documentation assistant if needed; seek external funding (grants) |
| **IRB delays for clinical validation study** | **Medium** | **Medium** | Early IRB engagement; experienced research coordinator; have contingency timeline |

---

## Maintenance and Review

### Review Schedule

**Profile Review**: Annually (Q1 each year, aligned with strategic planning)
**Control Effectiveness Review**: Quarterly (Clinical AI Committee)
**Maturity Re-assessment**: Annually (external assessment every 2 years)
**Clinical Validation Refresh**: Every 2 years or upon major model changes

### Update Triggers

Profile will be updated when:
- New high-risk AI systems introduced (e.g., surgical robotics AI, medication dosing AI)
- Regulatory requirements change (FDA guidance updates, new HIPAA rules, state AI laws)
- Material AI-related patient safety event occurs
- AIMF framework updates released (align with PraeSyn releases)
- FDA clearance obtained or denied for sepsis model
- Organizational strategic changes (merger, new service lines)
- Health equity analysis identifies significant disparities requiring new controls

### Version History

| Version | Date | Changes | Approved By |
|---------|------|---------|-------------|
| 1.0 | February 1, 2026 | Initial profile based on Healthcare Profile + High-Assurance additions for sepsis model | Dr. Maria Rodriguez (CMIO), Dr. Sarah Kim (CMO), Board Quality Committee |

---

## Appendices

### Appendix A: AI System Risk Stratification

**Sepsis Prediction Model**:
- **Risk Category**: High (life-safety, autonomous alerts, ICU critical decisions)
- **baseline**: B3 (High-Risk)
- **FDA Status**: Under evaluation for SaMD classification
- **IRB Status**: Protocol submitted Q2 2026 for validation study
- **Controls**: All 72 AIMF controls at B3 rigor

**Radiology AI (Chest X-ray, CT Scan)**:
- **Risk Category**: Moderate-High (diagnostic impact, clinician review required)
- **baseline**: B2-B3
- **FDA Status**: FDA-cleared Class II medical device (vendor-owned 510(k))
- **Post-Market Surveillance**: Quarterly reports required
- **Controls**: 62 Healthcare Profile controls at B2-B3

**Clinical Documentation Assistant**:
- **Risk Category**: Moderate (documentation quality, PHI processing)
- **baseline**: B2
- **FDA Status**: Not a medical device (administrative function)
- **HIPAA**: Business Associate Agreement with vendor
- **Controls**: 62 Healthcare Profile controls at B2

**Patient No-Show Prediction**:
- **Risk Category**: Low (operational, no clinical decisions)
- **baseline**: B1
- **PHI**: Limited (demographics, appointment history)
- **Controls**: 35 Foundational Profile controls at B1

### Appendix B: Clinical Validation Study Design (Sepsis Model)

**Study Design**: Prospective observational cohort study
**Setting**: MRHS ICUs (4 hospitals, 120 total ICU beds)
**Duration**: 6 months (Q2-Q4 2026)
**Sample Size**: Estimated 800 ICU admissions (powered for 80% sensitivity detection)
**Primary Endpoint**: Sensitivity and specificity for sepsis detection >6 hours before clinical diagnosis
**Secondary Endpoints**: False positive rate, clinician alert fatigue, time to treatment
**Comparator**: Standard of care (clinical judgment + SIRS criteria)
**IRB Approval**: Required before study start
**External Validation**: Independent statistician review + clinical expert panel

### Appendix C: Related Documents

- [MRHS Clinical AI Committee Charter] - internal
- [HIPAA Risk Analysis for AI Systems (2026)] - compliance
- [IRB Protocol: Sepsis Prediction Model Validation] - research
- [FDA Post-Market Surveillance Plan: Radiology AI] - regulatory
- [Patient Safety Event Reporting Policy] - quality
- [AI Incident Response Playbook] - IT/clinical operations
- [AIMF Healthcare Profile](../../framework-profiles/profile-healthcare.md) - foundation
- [AIMF High-Assurance Profile](../../framework-profiles/profile-high-assurance.md) - sepsis model reference

---

**AI Management Framework (AIMF) by PraeSyn**

*This is a fictional example demonstrating how a regional health system might customize the Healthcare Profile (with High-Assurance elements) for clinical AI governance with patient safety and regulatory compliance as primary drivers.*
