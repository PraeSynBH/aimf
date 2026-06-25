# AI Management Framework (AIMF) by PraeSyn
## MEASURE Function

**© 2026 PraeSyn, LLC. All rights reserved.**
Licensed under CC BY-NC-ND 4.0

**Version**: 1.0
**Publication Date**: January 29, 2026
**Status**: Pre-Publication (Working Draft)
**Function Identifier**: MEASURE
**Controls**: MEA-1.1 through MEA-4.3 (22 controls)

---

## Function Overview

The **MEASURE** function employs quantitative, qualitative, or mixed-method tools, techniques, and methodologies to analyze, assess, benchmark, and monitor AI risks and trustworthiness characteristics.

### Purpose

The MEASURE function ensures organizations can:

- Select and implement appropriate measurement methods and metrics
- Evaluate AI systems for trustworthiness characteristics
- Track risks over time including emergent and unanticipated risks
- Obtain feedback on measurement efficacy and continuously improve

### Standards Alignment

| Standard | Alignment |
|----------|-----------|
| **ISO 42001** | Clause 9 (Performance Evaluation), 8.2 (Impact Assessment), 8.3 (Data) |
| **NIST AI RMF** | MEASURE 1.1-1.3, 2.1-2.13, 3.1-3.3, 4.1-4.3 |

---

## Category Structure

### MEASURE 1: Methods and Metrics

Appropriate methods and metrics are selected for measuring AI risks.

| Control | Name | Description |
|---------|------|-------------|
| MEA-1.1 | Measurement Selection | Appropriate approaches and metrics for measuring AI risks selected |
| MEA-1.2 | Metric Validation | Appropriateness and effectiveness of AI metrics assessed and updated |
| MEA-1.3 | Independent Evaluation | Internal experts and independent assessors involved in evaluation |

### MEASURE 2: Trustworthiness Evaluation

AI systems evaluated for trustworthy characteristics.

| Control | Name | Description |
|---------|------|-------------|
| MEA-2.1 | Test Documentation | Test sets, metrics, and tools documented |
| MEA-2.2 | Human Evaluation | Human subject evaluations follow ethical standards |
| MEA-2.3 | Performance Measurement | Performance and assurance criteria measured |
| MEA-2.4 | Production Monitoring | AI system functionality monitored in production |
| MEA-2.5 | Validity Testing | System validity and reliability demonstrated |
| MEA-2.6 | Safety Assessment | Safety risks evaluated and residual risks documented |
| MEA-2.7 | Security Assessment | Security and resilience against adversarial attacks evaluated |
| MEA-2.8 | Transparency Assessment | Transparency and accountability risks examined |
| MEA-2.9 | Explainability | AI model explained, validated, documented |
| MEA-2.10 | Privacy Assessment | Privacy risks examined and documented |
| MEA-2.11 | Fairness Assessment | Fairness and bias evaluated |
| MEA-2.12 | Environmental Assessment | Environmental impact and sustainability assessed |
| MEA-2.13 | TEVV Effectiveness | TEVV process effectiveness evaluated |

### MEASURE 3: Risk Tracking

Mechanisms for tracking AI risks over time.

| Control | Name | Description |
|---------|------|-------------|
| MEA-3.1 | Continuous Monitoring | Mechanisms for tracking existing, unanticipated, and emergent risks |
| MEA-3.2 | Complex Settings | Risk tracking approaches for difficult-to-assess settings |
| MEA-3.3 | Feedback Integration | End user and community feedback processes established |

### MEASURE 4: Measurement Feedback

Feedback about efficacy of measurement approaches.

| Control | Name | Description |
|---------|------|-------------|
| MEA-4.1 | Context Connection | Measurement approaches connected to deployment context |
| MEA-4.2 | Expert Validation | Results informed and validated by domain experts |
| MEA-4.3 | Performance Trends | Performance improvements or declines identified |

---

## Control Details

### MEA-2.4: AI Production Monitoring

**Purpose**: Ensure continuous monitoring of AI system functionality in production environments.

**Control Objective**: All deployed AI systems have production monitoring that tracks functionality, detects anomalies, and alerts on significant changes.

#### Implementation by Tier

**Baseline 1 (Initial)**:
- Basic production monitoring for system availability
- Manual review of outputs on periodic basis
- Key error conditions logged

**Baseline 2 (Mature)**:
- Systematic production monitoring infrastructure
- Component behavior tracking
- Anomaly detection capabilities
- Defined alerting and response procedures
- Regular monitoring review

**Baseline 3 (High-Risk)**:
- Real-time production monitoring
- AI-powered anomaly detection
- Predictive alerting
- Comprehensive dashboards
- Automated response capabilities
- Independent monitoring validation

#### Evidence Examples

- Monitoring system documentation
- Dashboard screenshots
- Alert configuration documentation
- Anomaly detection methodology
- Response procedure documentation
- Monitoring effectiveness reports

---

### MEA-2.6: AI Safety Evaluation

**Purpose**: Ensure comprehensive evaluation of AI safety risks with documented residual risks.

**Control Objective**: All AI systems are evaluated for safety risks including fail-safe capabilities, knowledge limits, and residual risks are documented.

#### Implementation by Tier

**Baseline 1 (Initial)**:
- Basic safety assessment for major systems
- Key safety risks identified
- General fail-safe consideration

**Baseline 2 (Mature)**:
- Comprehensive safety evaluation for all systems
- Fail-safe testing performed
- Residual safety risks documented
- Safety metrics defined
- Knowledge limit behavior evaluated

**Baseline 3 (High-Risk)**:
- Advanced safety program with independent validation
- Continuous safety monitoring
- Predictive safety risk modeling
- Public safety reports
- Research-grade safety methodology
- Real-time safety metrics

#### Evidence Examples

- Safety assessment documentation
- Fail-safe testing results
- Residual risk documentation
- Safety metric definitions and results
- Independent safety validation reports (for B3)
- Safety monitoring dashboards

---

### MEA-2.11: AI Fairness and Bias Testing

**Purpose**: Ensure comprehensive evaluation of fairness and bias in AI systems.

**Control Objective**: All AI systems are evaluated for bias using appropriate fairness metrics with documented results and mitigation effectiveness.

#### Implementation by Tier

**Baseline 1 (Initial)**:
- Basic bias testing for high-risk systems
- Awareness of fairness considerations
- Initial bias assessment performed

**Baseline 2 (Mature)**:
- Comprehensive fairness evaluation using multiple metrics
- Demographic analysis across relevant groups
- Bias mitigation effectiveness assessed
- Regular fairness review cycle
- Documentation of fairness methodology and results

**Baseline 3 (High-Risk)**:
- Advanced fairness program with intersectional analysis
- Continuous bias monitoring
- Predictive bias emergence detection
- Public fairness reports
- Research-grade fairness methodology
- Industry-leading fairness practices

#### Evidence Examples

- Fairness evaluation methodology
- Bias testing results by demographic group
- Fairness metric definitions
- Intersectional analysis results (for B3)
- Mitigation effectiveness documentation
- Public fairness reports (for B3)

---

### MEA-3.1: AI Continuous Risk Tracking

**Purpose**: Establish mechanisms for ongoing tracking of AI risks including emergent and unanticipated risks.

**Control Objective**: Continuous risk tracking mechanisms are in place with dedicated resources and processes for identifying emergent risks.

#### Implementation by Tier

**Baseline 1 (Initial)**:
- Basic ongoing monitoring for major risks
- Periodic risk review
- Reactive identification of new risks

**Baseline 2 (Mature)**:
- Comprehensive risk tracking for all systems
- Dedicated personnel for risk monitoring
- Intended vs. actual performance comparison
- Proactive emergent risk identification
- Risk trend analysis

**Baseline 3 (High-Risk)**:
- Advanced risk intelligence capabilities
- Predictive risk monitoring
- Automated risk tracking
- Real-time risk dashboards
- Independent risk validation
- Research contribution to risk science

#### Evidence Examples

- Risk tracking methodology
- Risk monitoring reports
- Personnel assignment documentation
- Performance comparison analyses
- Risk trend reports
- Real-time dashboard screenshots (for B3)

---

## Trustworthiness Characteristics

The MEASURE function evaluates AI systems across key trustworthiness characteristics:

### Characteristics Overview

| Characteristic | Control(s) | Description |
|----------------|------------|-------------|
| **Safety** | MEA-2.6 | Freedom from unacceptable risk; fail-safe behavior |
| **Security** | MEA-2.7 | Resilience to adversarial attacks and malicious use |
| **Transparency** | MEA-2.8, MEA-2.9 | Understandable operation and output interpretation |
| **Privacy** | MEA-2.10 | Protection of personal and sensitive information |
| **Fairness** | MEA-2.11 | Equitable treatment across groups; bias mitigation |
| **Validity** | MEA-2.5 | Accurate and reliable performance |
| **Accountability** | MEA-2.8 | Clear responsibility and recourse mechanisms |

### Measurement Approaches by Characteristic

| Characteristic | Quantitative Methods | Qualitative Methods |
|----------------|---------------------|---------------------|
| Safety | Error rates, fail-safe testing, boundary testing | Expert review, scenario analysis |
| Security | Penetration testing, adversarial testing scores | Red team exercises, threat modeling |
| Transparency | Explainability metrics, documentation coverage | User comprehension studies |
| Privacy | Privacy risk scores, data leakage testing | Privacy impact assessment |
| Fairness | Fairness metrics (demographic parity, equalized odds) | Stakeholder feedback, impact studies |
| Validity | Accuracy, precision, recall, F1 scores | Expert validation, user acceptance |
| Accountability | Response time metrics, documentation completeness | Audit review, process assessment |

---

## Implementation Guidance

### TEVV (Test, Evaluation, Verification, and Validation) Framework

```
Test
├── Functional Testing: Does the system work as intended?
├── Performance Testing: Does it meet performance criteria?
└── Robustness Testing: Does it handle edge cases?

Evaluation
├── Trustworthiness: Assess safety, fairness, privacy, etc.
├── Comparison: Benchmark against alternatives
└── Trade-off Analysis: Balance competing objectives

Verification
├── Requirements: Does implementation match specification?
├── Standards: Does it meet required standards?
└── Process: Was development process followed?

Validation
├── Stakeholder: Does it meet stakeholder needs?
├── Context: Is it appropriate for deployment context?
└── Impact: Are impacts acceptable?
```

### Measurement Selection Process

1. **Identify Risks**: From MAP function outputs
2. **Select Metrics**: Choose appropriate metrics for each risk
3. **Define Methods**: Determine measurement methodology
4. **Establish Baselines**: Set baseline measurements
5. **Implement Monitoring**: Deploy continuous measurement
6. **Review and Update**: Regularly assess metric effectiveness

### Common Metrics by Risk Category

| Risk Category | Example Metrics |
|---------------|-----------------|
| Performance Degradation | Accuracy over time, latency, throughput |
| Bias/Fairness | Demographic parity, equalized odds, calibration |
| Safety | Error rate, fail-safe activation rate, boundary violations |
| Security | Attack success rate, vulnerability count, resilience score |
| Privacy | Data leakage risk score, privacy attack success rate |
| Transparency | Explanation fidelity, user comprehension rate |

---

## Integration with Other Functions

### From MAP

MAP function provides:
- Identified risks requiring measurement
- Context for interpreting measurements
- Stakeholder groups for impact assessment
- Risk tolerance levels for threshold setting

### To MANAGE

MEASURE function provides:
- Quantified risk data for prioritization
- Performance trend data for response planning
- Compliance evidence for governance
- Feedback for continuous improvement

---

## Assessment Criteria

### Scoring Methodology

Each MEASURE control is assessed on a 0-3 scale:

| Score | Level | Description |
|-------|-------|-------------|
| 0 | Not Present | No measurement capability exists |
| 1 | Ad-Hoc | Informal, inconsistent measurement |
| 2 | Developing | Documented measurement but inconsistent application |
| 3 | Established | Systematic, organization-wide measurement |

### Key Assessment Questions

**MEA-2.4**: Is there production monitoring for all deployed AI systems?

**MEA-2.6**: Are safety risks evaluated with documented residual risks?

**MEA-2.11**: Is bias testing performed with documented fairness metrics?

**MEA-3.1**: Are there mechanisms for tracking emergent AI risks?

---

## References

- ISO/IEC 42001:2023 Clause 9 (Performance Evaluation)
- NIST AI RMF 1.0 MEASURE function
- NIST SP 1270 Towards a Standard for Identifying and Managing Bias in AI
- IEEE 7000-2021 Model Process for Addressing Ethical Concerns

---

**Next Document**: [MANAGE Function Controls](AIMF-FUNCTION-MANAGE.md) | [MAP Function Controls](AIMF-FUNCTION-MAP.md)
