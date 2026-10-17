# AI Management Framework (AIMF) by PraeSyn
## ISO/IEC 27001:2022 Mapping

**© 2026 PraeSyn, LLC. All rights reserved.**
Licensed under CC BY-NC-ND 4.0

**Standard Title**: Information security, cybersecurity and privacy protection — Information security management systems — Requirements
**Version**: 1.0
**Publication Date**: January 29, 2026
**Standard Version**: ISO/IEC 27001:2022
**Status**: Research Required - Detailed mapping needed

**Purpose**: This document maps ISO/IEC 27001:2022 information security controls applicable to AI systems to the AI Management Framework (AIMF).

**Completeness**: Incomplete. This document is a research skeleton and does not yet
contain a control-by-control mapping. In the control catalog,
`core/AIMF-CONTROL-CATALOG.csv`, 34 of 72 controls carry an ISO 27001 reference, and
those references mix ISO/IEC 27001:2022 theme IDs (A.5, A.6, A.8) with retired
ISO/IEC 27001:2013 IDs (A.9.2, A.18.1, A.18.2). See `AIMF-MAPPING-COMPLETENESS.md`.

---

## Standard Overview

ISO 27001 provides requirements for establishing, implementing, maintaining and continually improving an information security management system. While not AI-specific, its security controls are essential for AI systems handling sensitive data.

### Key Components

1. **Context of the Organization** (Clause 4)
2. **Leadership** (Clause 5)
3. **Planning** (Clause 6)
4. **Support** (Clause 7)
5. **Operation** (Clause 8)
6. **Performance Evaluation** (Clause 9)
7. **Improvement** (Clause 10)
8. **Annex A Controls** (93 security controls)

---

## AI-Relevant Security Controls

### Annex A.5: Organizational Controls
- A.5.1: Policies for information security
- A.5.2: Information security roles and responsibilities
- A.5.7: Threat intelligence
- A.5.10: Acceptable use of information

### Annex A.8: Technological Controls
- A.8.1: User endpoint devices (AI workstations)
- A.8.2: Privileged access rights (model access)
- A.8.5: Secure authentication
- A.8.16: Monitoring activities (AI system monitoring)

[Additional relevant controls to be identified during research]

---

## Maturity Level Mapping

### Level 1: Initial - ISO 27001 Gaps for AI

**Gap Analysis**:
- No ISMS adapted for AI systems
- AI data not classified or protected
- No access controls for AI models
- AI development environments unsecured
- No monitoring of AI system activities

**Required Research**:
- [ ] Identify which Annex A controls are critical for AI systems
- [ ] Determine baseline security for AI at Level 1
- [ ] Map security gaps to framework characteristics

---

### Level 2: Developing - ISO 27001 Basic Controls

**Partial Implementation**:
- Basic data classification for AI
- Initial access controls for sensitive data
- Basic authentication for AI systems
- Initial logging and monitoring
- Security awareness training started

**Required Research**:
- [ ] Define minimum security controls for Level 2
- [ ] Identify acceptable interim security measures
- [ ] Document typical Level 2 security posture

---

### Level 3: Defined - ISO 27001 Comprehensive Controls

**Substantial Implementation**:
- Comprehensive ISMS covering AI systems
- All applicable Annex A controls implemented
- Regular security audits of AI systems
- Incident response procedures for AI
- Security integrated into AI lifecycle

**Required Research**:
- [ ] Map all AI-relevant controls to Level 3
- [ ] Define evidence requirements for each control
- [ ] Document typical Level 3 security implementations

---

### Level 4: Managed - ISO 27001 Metrics and Optimization

**Advanced Implementation**:
- Security metrics for AI systems
- Predictive threat analytics
- Automated security monitoring
- Real-time anomaly detection
- Security performance dashboards

**Required Research**:
- [ ] Identify security metrics from standard
- [ ] Define advanced security indicators
- [ ] Document measurement methodologies

---

### Level 5: Optimizing - ISO 27001 Innovation

**Continuous Improvement**:
- AI-powered security operations
- Autonomous threat response
- Security innovation for AI systems
- Industry leadership in AI security
- Research contributions

**Required Research**:
- [ ] Define security excellence beyond compliance
- [ ] Identify innovation opportunities
- [ ] Document leadership indicators

---

## AI-Specific Security Considerations

### Data Security for AI

**Training Data Protection**:
- Classification of training datasets
- Access controls for data lakes
- Encryption of sensitive training data
- Data poisoning prevention
- Privacy-preserving ML techniques

**Required Research**:
- [ ] Map data security controls to maturity levels
- [ ] Identify AI-specific data protection measures
- [ ] Document best practices for training data security

---

### Model Security

**Model Protection**:
- Model intellectual property protection
- Model access controls
- Model versioning security
- Adversarial attack prevention
- Model extraction prevention

**Required Research**:
- [ ] Identify model security requirements
- [ ] Map model protection to maturity levels
- [ ] Document model security best practices

---

### Infrastructure Security

**AI Infrastructure Protection**:
- GPU/TPU security
- Container security for ML
- ML platform security
- Cloud AI service security
- MLOps pipeline security

**Required Research**:
- [ ] Map infrastructure controls to AI environments
- [ ] Identify cloud-specific AI security considerations
- [ ] Document infrastructure security maturity

---

### Monitoring and Detection

**AI System Monitoring**:
- Model behavior monitoring
- Anomaly detection in predictions
- Data drift detection
- Model performance degradation detection
- Security event logging for AI

**Required Research**:
- [ ] Define monitoring requirements per level
- [ ] Identify AI-specific security events
- [ ] Document monitoring maturity progression

---

## Detailed Control Mapping

### A.5: Organizational Controls

[Detailed mapping of each control to maturity levels required]

### A.8: Technological Controls

[Detailed mapping of each control to maturity levels required]

[Additional control sections as identified during research]

---

## Research Tasks

### Phase 1: Standard Review
- [ ] Obtain ISO 27001:2022 standard document
- [ ] Review all Annex A controls
- [ ] Identify AI-relevant controls (estimated 40-50 of 93)
- [ ] Note implementation guidance

### Phase 2: AI Security Analysis
- [ ] Research AI-specific security vulnerabilities
- [ ] Identify AI threat landscape
- [ ] Review AI security frameworks (MITRE ATLAS, etc.)
- [ ] Document AI security best practices

### Phase 3: Detailed Mapping
- [ ] Map each relevant control to maturity levels
- [ ] Align with capability dimensions
- [ ] Document evidence requirements
- [ ] Create assessment questions

### Phase 4: Content Development
- [ ] Extract executive-friendly security language
- [ ] Develop video content on AI security
- [ ] Create security assessment rubrics
- [ ] Validate with security SMEs

---

## References

- ISO/IEC 27001:2022 - Information security management systems — Requirements
- ISO/IEC 27002:2022 - Information security controls
- ISO/IEC 27005:2022 - Information security risk management
- MITRE ATLAS - Adversarial Threat Landscape for AI Systems
- OWASP ML Security Top 10

---

**Next Steps**: Acquire ISO 27001:2022 and begin identifying AI-relevant security controls.
