# AI Management Framework (AIMF) by PraeSyn
## Domain Taxonomy - 3-Level Hierarchical Structure

**© 2026 PraeSyn, LLC. All rights reserved.**
Licensed under Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International (CC BY-NC-ND 4.0)

Framework Version: 1.0
Publication Date: January 25, 2026
Document Status: Final

PraeSyn, LLC | Washington State Limited Liability Company
www.praesyn.com

---

## Overview

This document defines the 3-level domain taxonomy used to organize the 72 AIMF controls. The taxonomy provides a business-friendly organizational structure that complements the NIST AI RMF function-based organization.

**Taxonomy Levels**:
- **Level 1 (L1)**: 4 high-level domains aligned with the 4 AIMF capability dimensions
- **Level 2 (L2)**: 19 mid-level categories representing key capability areas
- **Level 3 (L3)**: 72 detailed subcategories (1:1 mapping with individual controls)

The 19 L2 category names below are exactly the 19 distinct `Domain_L2` values carried by
`core/AIMF-CONTROL-CATALOG.csv`, and the controls listed under each category are exactly
the catalog's controls for that `Domain_L2` value. The L2 layer is reconciled: a category
appears here only if the catalog files controls under it.

---

## Domain L1: Governance & Accountability

**Description**: Policies, organizational structures, accountability mechanisms, and compliance processes that establish the foundation for responsible AI governance.

**Aligned with AIMF Dimension**: D1 (Governance & Risk Management)

### L2 Category: Policies & Procedures

**Description**: Documented policies and procedures that define AI governance requirements, compliance obligations, and operational standards.

| L3 Subcategory | Control ID | Control Name |
|----------------|------------|--------------|
| Legal and Regulatory Compliance | GOV-1.1 | Legal/Regulatory Compliance Policies |
| AI Use Characterization | GOV-1.2 | AI Use Scope Definition |
| Lifecycle Integration | GOV-1.3 | AI Lifecycle Governance |
| Compliance Verification | GOV-1.4 | AI Governance Compliance Monitoring |
| Environmental Stewardship | GOV-1.5 | AI Environmental Impact Management |
| Decommissioning | GOV-1.6 | AI System Decommissioning Policies |
| Third-Party Management | GOV-1.7 | Third-Party AI Risk Management |

**Total Controls**: 7

### L2 Category: Organizational Structure & Roles

**Description**: Organizational accountability structures, role definitions, and executive oversight mechanisms for AI risk management.

| L3 Subcategory | Control ID | Control Name |
|----------------|------------|--------------|
| Role Definition | GOV-2.1 | AI Accountability Assignment |
| Workforce Training | GOV-2.2 | AI Competency Development |
| Executive Engagement | GOV-2.3 | Executive AI Oversight |

**Total Controls**: 3

### L2 Category: Workforce Diversity & Inclusion

**Description**: Programs and policies promoting diversity, cross-functional collaboration, and diverse perspectives in AI development.

| L3 Subcategory | Control ID | Control Name |
|----------------|------------|--------------|
| Cross-Functional Teams | GOV-3.1 | Interdisciplinary AI Teams |
| Demographic Representation | GOV-3.2 | Demographic Diversity in AI |

**Total Controls**: 2

### L2 Category: Organizational Culture & Ethics

**Description**: Culture-building activities, stakeholder engagement, and ethical AI practices embedded in organizational values.

| L3 Subcategory | Control ID | Control Name |
|----------------|------------|--------------|
| Risk Culture | GOV-4.1 | AI Risk Culture Development |
| Stakeholder Feedback | GOV-4.2 | AI Feedback Integration |
| Communication | GOV-4.3 | AI Transparency Communication |
| External Partnerships | GOV-5.1 | AI Ecosystem Engagement |
| Academic Collaboration | GOV-5.2 | AI Research Collaboration |

**Total Controls**: 5

### L2 Category: Implementation Resources

**Description**: Resource allocation, capability building, and investments supporting AI governance program execution.

| L3 Subcategory | Control ID | Control Name |
|----------------|------------|--------------|
| Resource Allocation | GOV-6.1 | AI Governance Resourcing |
| Capability Building | GOV-6.2 | AI Governance Capability Development |

**Total Controls**: 2

**Domain L1 Total**: 19 controls

---

## Domain L2: Data Management & Privacy

**Description**: Data quality, privacy protection, lifecycle management, and third-party data governance practices.

**Aligned with AIMF Dimension**: D2 (Data Governance & Management)

### L2 Category: Data Quality & Integrity

**Description**: Processes ensuring data validity, reliability, and fitness for AI system purposes.

| L3 Subcategory | Control ID | Control Name |
|----------------|------------|--------------|
| Requirements Engineering | MAP-1.6 | AI System Requirements |
| Validity Testing | MEA-2.5 | AI Validity and Reliability |

**Total Controls**: 2

### L2 Category: Data Privacy & Protection

**Description**: Privacy risk assessment, privacy-preserving techniques, and data protection controls.

| L3 Subcategory | Control ID | Control Name |
|----------------|------------|--------------|
| Privacy Assessment | MEA-2.10 | AI Privacy Evaluation |

**Total Controls**: 1

### L2 Category: Third-Party Data Governance

**Description**: Management of data risks from third-party sources, vendors, and external datasets.

| L3 Subcategory | Control ID | Control Name |
|----------------|------------|--------------|
| Third-Party Risk Assessment | MAP-4.1 | Third-Party AI Risk Assessment |
| Third-Party Risk Controls | MAP-4.2 | Third-Party Risk Controls |
| Third-Party Monitoring | MAN-3.1 | Third-Party AI Ongoing Monitoring |

**Total Controls**: 3

*Category note — data lifecycle management.* Collection, curation, storage, retention and
disposal are treated in this taxonomy as cross-cutting practices within the domain rather
than as a separate L2 category, because no AIMF control is scoped to lifecycle management
alone and inventing one would change the 72-control set. The lifecycle controls that do
exist are filed where their subject matter sits: `GOV-1.3 AI Lifecycle Governance` and
`GOV-1.6 AI System Decommissioning Policies` under Governance & Accountability →
Policies & Procedures, and `MAP-4.1` / `MAP-4.2` under Third-Party Data Governance above.
Before v1.0.3 this taxonomy carried a separate "Data Lifecycle Management" category with
zero controls, which is why the taxonomy listed 20 L2 names against the catalog's 19.

**Domain L2 Total**: 6 controls

---

## Domain L3: Technical Operations & MLOps

**Description**: AI system development, testing, deployment, monitoring, security, and operational excellence practices.

**Aligned with AIMF Dimension**: D3 (Technical Operations & MLOps)

### L2 Category: Development & Testing

**Description**: AI model development, testing methodologies, validation approaches, and scientific rigor.

| L3 Subcategory | Control ID | Control Name |
|----------------|------------|--------------|
| Task Classification | MAP-2.1 | AI System Task Categorization |
| Knowledge Limits | MAP-2.2 | AI System Boundaries |
| Scientific Integrity | MAP-2.3 | AI Scientific Rigor |
| Test Documentation | MEA-2.1 | AI Testing Documentation |
| Human Evaluation | MEA-2.2 | AI Human Subject Testing |
| Performance Criteria | MEA-2.3 | AI Performance Measurement |
| TEVV Effectiveness | MEA-2.13 | AI Testing Effectiveness |

**Total Controls**: 7

### L2 Category: Deployment & Operations

**Description**: Production deployment, operational monitoring, and system control mechanisms.

| L3 Subcategory | Control ID | Control Name |
|----------------|------------|--------------|
| Application Scope | MAP-3.3 | AI Application Scope |
| Human Oversight | MAP-3.5 | Human Oversight Design |
| Production Monitoring | MEA-2.4 | AI Production Monitoring |
| System Control | MAN-2.4 | AI System Disengage/Deactivate |
| Pre-trained Model Management | MAN-3.2 | Pre-trained Model Management |
| Post-Deployment Monitoring | MAN-4.1 | AI Post-Deployment Monitoring |

**Total Controls**: 6

### L2 Category: Monitoring & Maintenance

**Description**: Continuous monitoring, performance tracking, risk tracking, and system maintenance activities.

| L3 Subcategory | Control ID | Control Name |
|----------------|------------|--------------|
| Continuous Risk Tracking | MEA-3.1 | AI Continuous Risk Tracking |
| Complex Settings Assessment | MEA-3.2 | AI Risk Assessment in Complex Contexts |
| Performance Trends | MEA-4.3 | AI Performance Change Detection |
| Value Sustainment | MAN-2.2 | AI Value Preservation |
| Continuous Improvement | MAN-4.2 | AI Continuous Improvement Integration |

**Total Controls**: 5

### L2 Category: Security & Resilience

**Description**: Cybersecurity controls, adversarial robustness, resilience mechanisms, and incident response.

| L3 Subcategory | Control ID | Control Name |
|----------------|------------|--------------|
| Safety Assessment | MEA-2.6 | AI Safety Evaluation |
| Security Assessment | MEA-2.7 | AI Security and Resilience |
| Emergent Risk Response | MAN-2.3 | AI Emergent Risk Response |
| Incident Communication | MAN-4.3 | AI Incident and Error Reporting |

**Total Controls**: 4

### L2 Category: Measurement & Evaluation

**Description**: Metrics selection, measurement methodologies, independent assessment, and evaluation effectiveness.

| L3 Subcategory | Control ID | Control Name |
|----------------|------------|--------------|
| Measurement Approaches | MEA-1.1 | AI Risk Measurement Selection |
| Metric Effectiveness | MEA-1.2 | AI Metric Validation |
| Independent Assessment | MEA-1.3 | AI Independent Evaluation |
| Measurement-Context Alignment | MEA-4.1 | AI Measurement-Context Alignment |
| Expert Validation | MEA-4.2 | AI Results Expert Review |

**Total Controls**: 5

### L2 Category: Trustworthy AI Characteristics

**Description**: Evaluation of AI trustworthiness dimensions including transparency, explainability, fairness, and environmental impact.

| L3 Subcategory | Control ID | Control Name |
|----------------|------------|--------------|
| Transparency Assessment | MEA-2.8 | AI Transparency Evaluation |
| Explainability | MEA-2.9 | AI Model Explanation |
| Fairness Assessment | MEA-2.11 | AI Fairness and Bias Testing |
| Environmental Assessment | MEA-2.12 | AI Environmental Impact |

**Total Controls**: 4

**Domain L3 Total**: 31 controls

---

## Domain L4: Organizational Culture & Capabilities

**Description**: Workforce development, stakeholder engagement, communication, collaboration, and human-centric AI practices.

**Aligned with AIMF Dimension**: D4 (Organizational Culture & Change Management)

### L2 Category: Workforce Development & Training

**Description**: Training programs, competency development, operator proficiency, and team composition.

| L3 Subcategory | Control ID | Control Name |
|----------------|------------|--------------|
| Team Diversity | MAP-1.2 | AI Development Team Composition |
| Operator Proficiency | MAP-3.4 | AI Operator Requirements |

**Total Controls**: 2

### L2 Category: Stakeholder Engagement & Communication

**Description**: Stakeholder feedback, communication practices, user engagement, and transparency reporting.

| L3 Subcategory | Control ID | Control Name |
|----------------|------------|--------------|
| Stakeholder Engagement | MAP-5.2 | AI Stakeholder Feedback |
| User Feedback Processes | MEA-3.3 | AI User Feedback Processes |

**Total Controls**: 2

### L2 Category: Strategic Alignment & Context

**Description**: Strategic planning, purpose documentation, business value, risk tolerance, and organizational alignment.

| L3 Subcategory | Control ID | Control Name |
|----------------|------------|--------------|
| Purpose Documentation | MAP-1.1 | AI System Purpose Characterization |
| Strategic Alignment | MAP-1.3 | AI Strategic Alignment |
| Business Value | MAP-1.4 | AI Business Value Documentation |
| Risk Tolerance | MAP-1.5 | AI Risk Tolerance Definition |

**Total Controls**: 4

### L2 Category: Impact Assessment & Decision-Making

**Description**: Impact analysis, benefits assessment, cost analysis, and go/no-go decision frameworks.

| L3 Subcategory | Control ID | Control Name |
|----------------|------------|--------------|
| Benefits Analysis | MAP-3.1 | AI Benefits Documentation |
| Cost Analysis | MAP-3.2 | AI Cost Documentation |
| Impact Analysis | MAP-5.1 | AI Impact Assessment |
| Proceed Determination | MAN-1.1 | AI Go/No-Go Decision |
| Alternative Analysis | MAN-2.1 | AI Alternative Evaluation |

**Total Controls**: 5

### L2 Category: Risk Management & Response

**Description**: Risk prioritization, response development, residual risk documentation, and treatment planning.

| L3 Subcategory | Control ID | Control Name |
|----------------|------------|--------------|
| Treatment Prioritization | MAN-1.2 | AI Risk Prioritization |
| Response Development | MAN-1.3 | AI Risk Response Planning |
| Residual Documentation | MAN-1.4 | AI Residual Risk Documentation |

**Total Controls**: 3

**Domain L4 Total**: 16 controls

---

## Summary Statistics

| Domain L1 | L2 Categories | Total Controls | Percentage |
|-----------|---------------|----------------|------------|
| **Governance & Accountability** | 5 | 19 | 26% |
| **Data Management & Privacy** | 3 | 6 | 8% |
| **Technical Operations & MLOps** | 6 | 31 | 43% |
| **Organizational Culture & Capabilities** | 5 | 16 | 22% |
| **TOTAL** | **19** | **72** | **100%** |

---

## Domain-to-Function Mapping

### Cross-Reference: L1 Domains to NIST AI RMF Functions

| Domain L1 | GOVERN | MAP | MEASURE | MANAGE | Total |
|-----------|--------|-----|---------|--------|-------|
| **Governance & Accountability** | 19 | 0 | 0 | 0 | 19 |
| **Data Management & Privacy** | 0 | 3 | 1 | 2 | 6 |
| **Technical Operations & MLOps** | 0 | 5 | 19 | 7 | 31 |
| **Organizational Culture & Capabilities** | 0 | 10 | 1 | 5 | 16 |
| **TOTAL** | **19** | **18** | **22** | **13** | **72** |

*Note: Some controls serve multiple domains/functions and are counted in their primary domain.*

---

## Usage in Enhanced Control Catalog

The enhanced control catalog CSV includes three new columns populated from this taxonomy:

- **Domain_L1**: High-level domain name
- **Domain_L2**: Mid-level category name
- **Domain_L3**: Detailed subcategory name (typically matches the NIST AI RMF subcategory or control name)

This hierarchical organization enables:
- **Business-friendly navigation** for non-technical stakeholders
- **Filtering and grouping** controls by domain
- **Gap analysis** by domain area
- **Resource allocation** aligned with business priorities
- **Profile development** based on domain emphasis

---

## Taxonomy Maintenance

This taxonomy is version-controlled with the framework. Changes to the taxonomy require a framework version update:

- **Minor version** (e.g., 1.0 → 1.1): Adding L3 subcategories or clarifying descriptions
- **Major version** (e.g., 1.0 → 2.0): Restructuring L1/L2 hierarchy or moving controls between domains

For questions about taxonomy application or proposed changes, contact:
licensing@praesyn.com

---

**AI Management Framework (AIMF) by PraeSyn**
Making AI Governance Practical, Accessible, and Effective.
