# AI Management Framework (AIMF) by PraeSyn
## Implementation Tiers

**© 2026 PraeSyn, LLC. All rights reserved.**
Licensed under CC BY-NC-ND 4.0

**Version**: 1.0
**Publication Date**: January 25, 2026
**Document Type**: Tier Definition Guide

---

## Overview

The AIMF defines three implementation tiers that specify the rigor of control implementation. Organizations select their implementation tier based on their AI system portfolio characteristics, risk profile, regulatory environment, and organizational context.

---

## Tier Selection Criteria

### Factors Determining Tier Selection

| Factor | T1 Initial | T2 Mature | T3 High-Risk |
|--------|------------|-----------|--------------|
| **AI System Impact** | Limited impact; internal use | Moderate impact; customer-facing | High impact; critical decisions |
| **Regulatory Environment** | Minimal AI-specific regulation | Moderate regulatory oversight | High regulatory scrutiny |
| **Data Sensitivity** | Non-sensitive data | Sensitive personal data | Highly sensitive; regulated data |
| **Automation Level** | Human-in-the-loop | Human-on-the-loop | Autonomous decisions |
| **Error Consequences** | Reversible; low cost | Moderate consequences | Irreversible; severe consequences |
| **Stakeholder Exposure** | Internal stakeholders | Direct customer impact | Public/vulnerable populations |

### Risk-Based Tier Assignment

Organizations should assess their AI systems against these criteria and assign the highest applicable tier. A portfolio approach is recommended where different AI systems may warrant different tiers.

---

## Tier 1: Initial

### Profile

Tier 1 is appropriate for organizations beginning their AI journey or operating AI systems with limited impact and low risk.

### Characteristics

- **AI Portfolio**: Limited AI use; experimental or pilot programs; internal productivity tools
- **Risk Profile**: Low-risk applications; human oversight on all decisions; easily reversible outputs
- **Maturity Stage**: Building foundational capabilities; establishing initial governance
- **Typical Organizations**: SMBs entering AI; large organizations with isolated AI pilots

### Implementation Requirements

#### Governance (T1)

| Requirement | Implementation Standard |
|-------------|------------------------|
| Policy Framework | Basic AI policy acknowledging AI use and risks; documented in existing governance framework |
| Accountability | AI responsibilities assigned to existing roles; basic escalation procedures defined |
| Training | General AI awareness training for relevant personnel; foundational understanding of AI risks |
| Documentation | Basic documentation of AI system purposes and intended uses |

#### Technical (T1)

| Requirement | Implementation Standard |
|-------------|------------------------|
| Testing | Basic functionality testing before deployment; documented test results |
| Monitoring | Basic production monitoring for system availability; manual review of outputs |
| Security | Standard security controls applied to AI systems; basic access management |
| Data Management | Basic data quality checks; documented data sources |

#### Organizational (T1)

| Requirement | Implementation Standard |
|-------------|------------------------|
| Risk Awareness | Basic awareness of AI risks among stakeholders |
| Feedback | Basic feedback channels for AI system users |
| Communication | Internal communication on AI system purposes |

### Evidence Requirements

For Tier 1 compliance, organizations should maintain:

1. Written AI policy or policy acknowledgment within existing policies
2. List of AI systems with documented purposes
3. Basic risk assessment documentation
4. Training completion records for relevant personnel
5. Basic test documentation for deployed AI systems

---

## Tier 2: Mature

### Profile

Tier 2 is appropriate for organizations with established AI programs, moderate-impact AI systems, or customer-facing AI applications.

### Characteristics

- **AI Portfolio**: Multiple production AI systems; customer-facing applications; established AI operations
- **Risk Profile**: Moderate-risk applications; significant business impact; regulatory compliance needs
- **Maturity Stage**: Defined processes; systematic governance; measured effectiveness
- **Typical Organizations**: Enterprises with AI programs; regulated industries; B2C AI applications

### Implementation Requirements

#### Governance (T2)

| Requirement | Implementation Standard |
|-------------|------------------------|
| Policy Framework | Formal AI governance policy approved by leadership; comprehensive coverage of AI lifecycle; regular policy review and updates |
| Accountability | Formal RACI matrix for AI governance; dedicated AI governance personnel or function; clear escalation paths documented and tested |
| Training | Role-based AI training programs; competency assessments; specialized training for AI developers; regular refresher training |
| Documentation | Comprehensive documentation of all AI systems; business cases; risk assessments; impact assessments |

#### Technical (T2)

| Requirement | Implementation Standard |
|-------------|------------------------|
| Testing | Comprehensive TEVV processes; documented test methodology; performance criteria defined and validated; bias and fairness testing |
| Monitoring | Systematic production monitoring; component behavior tracking; anomaly detection; defined alerting and response procedures |
| Security | Comprehensive security assessment for AI systems; adversarial robustness testing; vulnerability management |
| Data Management | Data quality frameworks; data lineage tracking; privacy impact assessments; data governance integration |

#### Risk Management (T2)

| Requirement | Implementation Standard |
|-------------|------------------------|
| Risk Assessment | Formal AI risk assessment methodology; quantified risk analysis; risk tolerance alignment |
| Risk Response | Documented risk response plans; defined response owners; effectiveness tracking |
| Third-Party Risk | Third-party AI risk assessment; contractual requirements; ongoing monitoring |
| Incident Management | Formal incident response procedures; root cause analysis; lessons learned integration |

#### Organizational (T2)

| Requirement | Implementation Standard |
|-------------|------------------------|
| Culture | Systematic risk culture program; risk awareness in performance criteria; leadership engagement |
| Stakeholder Engagement | Regular stakeholder feedback collection; defined response processes; feedback integration |
| Team Composition | Documented diversity requirements for AI teams; multiple disciplines required; competency tracking |

### Evidence Requirements

For Tier 2 compliance, organizations should maintain:

1. Approved AI governance policy with leadership sign-off
2. RACI matrix for AI governance roles
3. AI system registry with risk classifications
4. Training records with competency assessments
5. Comprehensive test documentation and results
6. Production monitoring dashboards and reports
7. Risk assessment documentation for all AI systems
8. Incident logs and root cause analysis reports
9. Third-party risk assessments
10. Stakeholder feedback analysis reports

---

## Tier 3: High-Risk

### Profile

Tier 3 is appropriate for organizations operating AI systems that make high-impact decisions, serve vulnerable populations, or operate in highly regulated environments.

### Characteristics

- **AI Portfolio**: Critical decision-making systems; autonomous operations; high-impact AI applications
- **Risk Profile**: High-risk applications; significant consequences for errors; regulatory compliance mandatory
- **Maturity Stage**: Industry-leading practices; continuous improvement; external validation
- **Typical Organizations**: Financial services; healthcare; critical infrastructure; government; autonomous systems

### Implementation Requirements

#### Governance (T3)

| Requirement | Implementation Standard |
|-------------|------------------------|
| Policy Framework | Comprehensive AI governance framework with board-level oversight; integration with enterprise risk management; continuous policy monitoring and adaptation |
| Accountability | Independent AI governance function; board-level AI committee; external advisory mechanisms; personal accountability for senior leaders |
| Training | Comprehensive certification programs; continuous professional development; specialized expertise development; external training validation |
| Documentation | Exhaustive documentation meeting regulatory standards; audit-ready; version-controlled; publicly accessible where appropriate |

#### Technical (T3)

| Requirement | Implementation Standard |
|-------------|------------------------|
| Testing | Rigorous TEVV with independent validation; research-grade methodology; continuous validation; comprehensive bias testing with intersectional analysis |
| Monitoring | Real-time production monitoring; AI-powered anomaly detection; predictive alerting; comprehensive dashboards; automated response capabilities |
| Security | Independent security assessment; red team testing; continuous security monitoring; advanced adversarial testing; supply chain security |
| Data Management | Advanced data governance; real-time data quality monitoring; comprehensive privacy protection; differential privacy where applicable |

#### Risk Management (T3)

| Requirement | Implementation Standard |
|-------------|------------------------|
| Risk Assessment | Quantitative risk modeling; independent risk validation; real-time risk monitoring; predictive risk analytics |
| Risk Response | Comprehensive response playbooks; automated response capabilities; validated recovery procedures; continuous improvement |
| Third-Party Risk | Comprehensive third-party risk program; independent vendor audits; supply chain visibility; real-time monitoring |
| Incident Management | Advanced incident management; AI-powered detection; automated communication; public incident transparency |

#### Organizational (T3)

| Requirement | Implementation Standard |
|-------------|------------------------|
| Culture | Mature risk culture embedded in values; external recognition; industry thought leadership; culture effectiveness measured |
| Stakeholder Engagement | Comprehensive stakeholder ecosystem; external advisory boards; public transparency reports; real-time engagement |
| Team Composition | Industry-leading diversity; measurable outcomes; external diversity audits; public diversity commitments |

#### External Validation (T3)

| Requirement | Implementation Standard |
|-------------|------------------------|
| Independent Audit | Annual independent AI audit by qualified third party; public audit summary |
| Certification | Relevant certifications obtained and maintained (ISO 42001 where applicable) |
| Regulatory Engagement | Proactive regulatory dialogue; participation in regulatory consultations |
| Public Transparency | Public AI governance reports; model cards for high-impact systems; algorithmic impact assessments |

### Evidence Requirements

For Tier 3 compliance, organizations should maintain:

1. Board-approved AI governance framework
2. Independent AI oversight function charter
3. External advisory board meeting minutes
4. Comprehensive AI system registry with detailed risk documentation
5. Certification records for AI personnel
6. Independent TEVV validation reports
7. Real-time monitoring system documentation
8. Security assessment reports including penetration testing
9. Independent audit reports
10. Regulatory compliance documentation
11. Public transparency reports
12. Third-party audit results
13. Incident response exercises and results
14. Stakeholder engagement reports
15. Diversity and inclusion metrics with external validation

---

## Tier Comparison Matrix

### Control Implementation Depth

| Control Area | T1 Initial | T2 Mature | T3 High-Risk |
|--------------|------------|-----------|--------------|
| Policy Documentation | Basic policy statement | Comprehensive policy framework | Exhaustive, audit-ready documentation |
| Risk Assessment | Qualitative, high-level | Quantified, systematic | Real-time, predictive modeling |
| Testing | Functionality testing | Comprehensive TEVV | Independent validation, research-grade |
| Monitoring | Basic availability | Systematic with anomaly detection | Real-time with AI-powered analytics |
| Security | Standard controls | Comprehensive assessment | Independent testing, continuous monitoring |
| Training | Awareness level | Role-based with assessment | Certification with continuous development |
| External Validation | Self-assessment | Internal audit | Independent third-party audit |
| Transparency | Internal documentation | Stakeholder communication | Public reporting |

### Measurement and Metrics

| Metric Category | T1 Initial | T2 Mature | T3 High-Risk |
|-----------------|------------|-----------|--------------|
| Control Effectiveness | Manual assessment | Defined KPIs | Real-time dashboards |
| Incident Tracking | Basic logging | Systematic tracking | Predictive analytics |
| Performance Monitoring | Periodic review | Regular monitoring | Continuous real-time |
| Stakeholder Feedback | Ad-hoc collection | Systematic collection | Real-time integration |

---

## Tier Progression

### Advancing from T1 to T2

Organizations progressing from T1 to T2 should focus on:

1. **Formalizing governance**: Move from ad-hoc to documented, approved policies
2. **Systematic processes**: Establish repeatable, documented processes across AI lifecycle
3. **Defined accountability**: Create formal roles and RACI matrices
4. **Comprehensive testing**: Implement full TEVV methodology
5. **Stakeholder integration**: Establish systematic feedback and engagement

### Advancing from T2 to T3

Organizations progressing from T2 to T3 should focus on:

1. **Independent validation**: Engage external auditors and validators
2. **Real-time capabilities**: Implement continuous monitoring and alerting
3. **Predictive analytics**: Move from reactive to predictive risk management
4. **Public transparency**: Establish public reporting and engagement
5. **Industry leadership**: Contribute to standards and best practices

---

## Tier Assessment

### Self-Assessment Questions

**For T1 Eligibility**:
- Do we have documented purposes for all AI systems?
- Is there basic awareness of AI risks among relevant personnel?
- Are AI systems subject to basic testing before deployment?
- Do we have basic feedback mechanisms for AI system users?

**For T2 Eligibility**:
- Do we have a formal, approved AI governance policy?
- Are AI governance roles formally assigned and documented?
- Do we conduct systematic risk assessments for AI systems?
- Is there comprehensive testing including bias and fairness?
- Do we have production monitoring with anomaly detection?

**For T3 Eligibility**:
- Is there independent oversight of AI governance?
- Do we engage external validators and auditors?
- Is there real-time monitoring with predictive capabilities?
- Do we publish public transparency reports?
- Is there board-level accountability for AI governance?

---

## References

- ISO/IEC 42001:2023 - Implementation guidance
- NIST AI RMF 1.0 - Organizational profiles
- NIST CSF 2.0 - Implementation tiers
- CMMI for Development - Capability levels

---

**Next Document**: [GOVERN Function Controls](../functions/AIMF-FUNCTION-GOVERN.md) | [Control Catalog](AIMF-CONTROL-CATALOG.csv)
