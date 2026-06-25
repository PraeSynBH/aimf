# AI Management Framework (AIMF) by PraeSyn
## Dimension Mapping

**© 2026 PraeSyn, LLC. All rights reserved.**
Licensed under CC BY-NC-ND 4.0

**Version**: 1.0
**Publication Date**: January 29, 2026
**Status**: Pre-Publication (Working Draft)
**Document Type**: Cross-Reference Guide

---

## Overview

This document maps the four AIMF capability dimensions to the 72 framework controls, providing a cross-reference view for dimension-focused assessments and improvements.

---

## The Four Capability Dimensions

| ID | Dimension | Description | Primary Focus |
|----|-----------|-------------|---------------|
| **D1** | AI Governance & Risk Management | Strategic oversight, policies, accountability | Leadership, compliance, risk |
| **D2** | Data Governance & Management | Data quality, privacy, security, lifecycle | Data practices, privacy |
| **D3** | Technical Operations (MLOps) | Development, deployment, monitoring, maintenance | Engineering, operations |
| **D4** | Organizational Culture & Change | Skills, awareness, collaboration, ethics | People, culture |

---

## Dimension 1: AI Governance & Risk Management

### Description

Dimension 1 addresses the strategic and organizational aspects of AI management, including governance structures, policies, risk management frameworks, and leadership engagement.

### Scope

- Executive sponsorship and accountability
- Policy frameworks and compliance
- Risk appetite and tolerance
- Strategic alignment
- Resource allocation
- Third-party governance

### Control Mapping

| Control ID | Control Name | Function | Primary/Secondary |
|------------|--------------|----------|-------------------|
| GOV-1.1 | Legal/Regulatory Compliance | GOVERN | Primary |
| GOV-1.2 | AI Use Scope Definition | GOVERN | Primary |
| GOV-1.3 | AI Lifecycle Governance | GOVERN | Primary |
| GOV-1.4 | Compliance Verification | GOVERN | Primary |
| GOV-1.5 | Environmental Stewardship | GOVERN | Primary |
| GOV-1.6 | Decommissioning Policies | GOVERN | Primary |
| GOV-1.7 | Third-Party Management | GOVERN | Primary |
| GOV-2.1 | Accountability Assignment | GOVERN | Primary |
| GOV-2.3 | Executive Oversight | GOVERN | Primary |
| GOV-6.1 | Resource Allocation | GOVERN | Primary |
| GOV-6.2 | Capability Building | GOVERN | Primary |
| MAP-1.1 | Purpose Characterization | MAP | Primary |
| MAP-1.3 | Strategic Alignment | MAP | Primary |
| MAP-1.4 | Business Value | MAP | Primary |
| MAP-1.5 | Risk Tolerance | MAP | Primary |
| MAP-3.1 | Benefits Analysis | MAP | Primary |
| MAP-3.2 | Cost Analysis | MAP | Primary |
| MAP-4.1 | Third-Party Risk Assessment | MAP | Primary |
| MAP-4.2 | Third-Party Risk Controls | MAP | Primary |
| MAP-5.1 | Impact Assessment | MAP | Primary |
| MAN-1.1 | Go/No-Go Decision | MANAGE | Primary |
| MAN-1.2 | Risk Prioritization | MANAGE | Primary |
| MAN-1.3 | Response Development | MANAGE | Primary |
| MAN-1.4 | Residual Documentation | MANAGE | Primary |
| MAN-2.1 | Alternative Analysis | MANAGE | Primary |
| MAN-3.1 | Third-Party Monitoring | MANAGE | Primary |

**Total Primary Controls: 26**

### Key Assessment Questions

1. Is there documented executive sponsorship for AI governance?
2. Are AI policies approved and maintained by leadership?
3. Is AI risk integrated into enterprise risk management?
4. Are risk tolerances defined and approved for AI systems?
5. Are resources appropriately allocated for AI governance?

---

## Dimension 2: Data Governance & Management

### Description

Dimension 2 addresses the management of data used in AI systems, including data quality, privacy, security, lineage, and lifecycle management.

### Scope

- Data quality frameworks
- Privacy protection
- Data security
- Data lineage and provenance
- Data lifecycle management
- Regulatory compliance (privacy laws)

### Control Mapping

| Control ID | Control Name | Function | Primary/Secondary |
|------------|--------------|----------|-------------------|
| MAP-1.6 | Requirements | MAP | Primary |
| MAP-2.3 | Scientific Integrity | MAP | Primary |
| MEA-2.1 | Test Documentation | MEASURE | Secondary |
| MEA-2.2 | Human Evaluation | MEASURE | Primary |
| MEA-2.10 | Privacy Assessment | MEASURE | Primary |
| MEA-2.11 | Fairness Assessment | MEASURE | Secondary |
| MAN-3.2 | Model Monitoring | MANAGE | Secondary |

**Total Primary Controls: 4**
**Total Secondary Controls: 3**

### Key Assessment Questions

1. Are data quality requirements defined for AI systems?
2. Is data lineage tracked for AI training data?
3. Are privacy impact assessments performed?
4. Is there a data governance framework integrated with AI?
5. Are human subject protections applied in evaluations?

### Note on Data Governance

While Dimension 2 has fewer dedicated controls, data governance is implicitly embedded in many other controls. Organizations should also consider:

- Integration with enterprise data governance
- Compliance with privacy regulations (GDPR, CCPA, etc.)
- Data quality monitoring in production
- Synthetic data and data augmentation governance

---

## Dimension 3: Technical Operations (MLOps)

### Description

Dimension 3 addresses the technical aspects of AI system development, deployment, monitoring, and maintenance throughout the lifecycle.

### Scope

- Development practices
- Testing and validation
- Deployment pipelines
- Production monitoring
- Model management
- Incident response
- System control mechanisms

### Control Mapping

| Control ID | Control Name | Function | Primary/Secondary |
|------------|--------------|----------|-------------------|
| MAP-2.1 | Task Classification | MAP | Primary |
| MAP-2.2 | Knowledge Limits | MAP | Primary |
| MAP-3.3 | Scope Definition | MAP | Primary |
| MAP-3.5 | Human Oversight | MAP | Primary |
| MEA-1.1 | Measurement Selection | MEASURE | Primary |
| MEA-1.2 | Metric Validation | MEASURE | Primary |
| MEA-1.3 | Independent Evaluation | MEASURE | Primary |
| MEA-2.1 | Test Documentation | MEASURE | Primary |
| MEA-2.3 | Performance Measurement | MEASURE | Primary |
| MEA-2.4 | Production Monitoring | MEASURE | Primary |
| MEA-2.5 | Validity Testing | MEASURE | Primary |
| MEA-2.6 | Safety Assessment | MEASURE | Primary |
| MEA-2.7 | Security Assessment | MEASURE | Primary |
| MEA-2.8 | Transparency Assessment | MEASURE | Primary |
| MEA-2.9 | Explainability | MEASURE | Primary |
| MEA-2.11 | Fairness Assessment | MEASURE | Primary |
| MEA-2.12 | Environmental Assessment | MEASURE | Primary |
| MEA-2.13 | TEVV Effectiveness | MEASURE | Primary |
| MEA-3.1 | Continuous Monitoring | MEASURE | Primary |
| MEA-3.2 | Complex Settings | MEASURE | Primary |
| MEA-4.1 | Context Connection | MEASURE | Primary |
| MEA-4.2 | Expert Validation | MEASURE | Primary |
| MEA-4.3 | Performance Trends | MEASURE | Primary |
| MAN-2.2 | Value Sustainment | MANAGE | Primary |
| MAN-2.3 | Unknown Risk Response | MANAGE | Primary |
| MAN-2.4 | System Control | MANAGE | Primary |
| MAN-3.2 | Model Monitoring | MANAGE | Primary |
| MAN-4.1 | Post-Deployment | MANAGE | Primary |
| MAN-4.2 | Continuous Improvement | MANAGE | Primary |
| MAN-4.3 | Incident Communication | MANAGE | Primary |

**Total Primary Controls: 30**

### Key Assessment Questions

1. Is there systematic production monitoring for AI systems?
2. Are TEVV processes defined and documented?
3. Can AI systems be safely deactivated if needed?
4. Are model changes tracked and validated?
5. Is there continuous improvement integration?

---

## Dimension 4: Organizational Culture & Change

### Description

Dimension 4 addresses the human and cultural aspects of AI adoption, including workforce capabilities, diversity, stakeholder engagement, and organizational change.

### Scope

- Workforce development
- Training and awareness
- Team diversity
- Stakeholder engagement
- Communication practices
- Risk culture
- External engagement

### Control Mapping

| Control ID | Control Name | Function | Primary/Secondary |
|------------|--------------|----------|-------------------|
| GOV-2.2 | Workforce Training | GOVERN | Primary |
| GOV-3.1 | Cross-Functional Teams | GOVERN | Primary |
| GOV-3.2 | Demographic Representation | GOVERN | Primary |
| GOV-4.1 | Risk Culture | GOVERN | Primary |
| GOV-4.2 | Stakeholder Feedback | GOVERN | Primary |
| GOV-4.3 | Transparency Communication | GOVERN | Primary |
| GOV-5.1 | Ecosystem Engagement | GOVERN | Primary |
| GOV-5.2 | Research Collaboration | GOVERN | Primary |
| MAP-1.2 | Team Diversity | MAP | Primary |
| MAP-3.4 | Operator Proficiency | MAP | Primary |
| MAP-5.2 | Stakeholder Engagement | MAP | Primary |
| MEA-2.2 | Human Evaluation | MEASURE | Secondary |
| MEA-3.3 | Feedback Integration | MEASURE | Primary |

**Total Primary Controls: 12**
**Total Secondary Controls: 1**

### Key Assessment Questions

1. Is AI risk awareness integrated into organizational culture?
2. Are AI teams composed of diverse perspectives?
3. Are stakeholder feedback mechanisms in place?
4. Is there systematic training for AI-related roles?
5. Does the organization engage with the external AI ecosystem?

---

## Cross-Dimensional Dependencies

### Dependency Matrix

| From → To | D1 Governance | D2 Data | D3 Technical | D4 Culture |
|-----------|---------------|---------|--------------|------------|
| **D1 Governance** | - | Policies enable data governance | Risk tolerance guides technical decisions | Sponsorship enables culture change |
| **D2 Data** | Data quality informs risk assessment | - | Data enables ML operations | Privacy awareness requires culture |
| **D3 Technical** | Monitoring provides governance data | Technical controls protect data | - | Technical tools need skilled users |
| **D4 Culture** | Culture enables governance adoption | Culture drives data stewardship | Culture enables technical excellence | - |

### Key Integration Points

1. **Governance ↔ Technical**: Risk tolerance determines monitoring requirements; monitoring provides compliance evidence

2. **Governance ↔ Culture**: Executive sponsorship enables cultural change; culture determines governance effectiveness

3. **Data ↔ Technical**: Data quality determines model quality; technical processes protect data

4. **Culture ↔ Technical**: Skilled workforce enables technical excellence; technical tools require training

---

## Dimension-Focused Improvement Planning

### Starting with Governance (D1)

Organizations often start with Dimension 1 because governance provides the foundation for other dimensions.

**Recommended sequence**:
1. Establish executive sponsorship (GOV-2.3)
2. Define accountability (GOV-2.1)
3. Develop policies (GOV-1.x)
4. Set risk tolerance (MAP-1.5)
5. Allocate resources (GOV-6.1)

### Building Technical Capabilities (D3)

Technical capabilities should be built on governance foundations.

**Recommended sequence**:
1. Establish testing standards (MEA-2.x)
2. Implement production monitoring (MEA-2.4)
3. Define control mechanisms (MAN-2.4)
4. Build continuous improvement (MAN-4.2)

### Enabling Through Culture (D4)

Culture change takes time and should run parallel to other improvements.

**Recommended approach**:
1. Training and awareness (GOV-2.2)
2. Team composition (GOV-3.x, MAP-1.2)
3. Feedback mechanisms (GOV-4.2, MEA-3.3)
4. Risk culture (GOV-4.1)

### Integrating Data Governance (D2)

Data governance should integrate with existing enterprise data management.

**Key considerations**:
1. Leverage existing data governance frameworks
2. Add AI-specific requirements
3. Ensure privacy compliance
4. Build data quality monitoring

---

## Summary Statistics

### Control Distribution by Dimension

| Dimension | Primary Controls | Secondary Controls | Total Related |
|-----------|-----------------|-------------------|---------------|
| D1: Governance & Risk | 26 | 0 | 26 |
| D2: Data Governance | 4 | 3 | 7 |
| D3: Technical Operations | 30 | 0 | 30 |
| D4: Culture & Change | 12 | 1 | 13 |

### Control Distribution by Function

| Function | Controls | Primary Dimensions |
|----------|----------|-------------------|
| GOVERN | 18 | D1, D4 |
| MAP | 14 | D1, D3, D4 |
| MEASURE | 17 | D2, D3 |
| MANAGE | 10 | D1, D3 |

---

## References

- ISO/IEC 42001:2023 - Mapping to management system structure
- NIST AI RMF 1.0 - Profile and tier concepts
- CMMI for Development - Process area groupings

---

**Related Documents**: [Framework Overview](AIMF-FRAMEWORK-OVERVIEW.md) | [Control Catalog](AIMF-CONTROL-CATALOG.csv) | [Assessment Guide](AIMF-ASSESSMENT-GUIDE.md)
