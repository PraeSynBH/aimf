# AI Management Framework (AIMF) by PraeSyn
## Control Catalog - Human-Readable Guide

**© 2026 PraeSyn, LLC. All rights reserved.**
Licensed under Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International (CC BY-NC-ND 4.0)

Framework Version: 1.0
Publication Date: January 25, 2026
Document Status: Final

PraeSyn, LLC | Washington State Limited Liability Company
www.praesyn.com

---

## Overview

This document provides a human-readable guide to all 73 AIMF controls. Controls are organized by the 4 high-level domains and 16 mid-level categories defined in the domain taxonomy.

For the machine-readable version, see [AIMF-CONTROL-CATALOG.csv](AIMF-CONTROL-CATALOG.csv).

### Quick Navigation

**Domain L1: Governance & Accountability** (19 controls)
- [Policies & Procedures](#policies--procedures) (7 controls)
- [Organizational Structure & Roles](#organizational-structure--roles) (3 controls)
- [Workforce Diversity & Inclusion](#workforce-diversity--inclusion) (2 controls)
- [Organizational Culture & Ethics](#organizational-culture--ethics) (5 controls)
- [Implementation Resources](#implementation-resources) (2 controls)

**Domain L2: Data Management & Privacy** (6 controls)
- [Data Quality & Integrity](#data-quality--integrity) (2 controls)
- [Data Privacy & Protection](#data-privacy--protection) (1 control)
- [Third-Party Data Governance](#third-party-data-governance) (3 controls)

**Domain L3: Technical Operations & MLOps** (31 controls)
- [Development & Testing](#development--testing) (7 controls)
- [Deployment & Operations](#deployment--operations) (6 controls)
- [Monitoring & Maintenance](#monitoring--maintenance) (5 controls)
- [Security & Resilience](#security--resilience) (4 controls)
- [Measurement & Evaluation](#measurement--evaluation) (5 controls)
- [Trustworthy AI Characteristics](#trustworthy-ai-characteristics) (4 controls)

**Domain L4: Organizational Culture & Capabilities** (17 controls)
- [Workforce Development & Training](#workforce-development--training) (2 controls)
- [Stakeholder Engagement & Communication](#stakeholder-engagement--communication) (2 controls)
- [Strategic Alignment & Context](#strategic-alignment--context) (4 controls)
- [Impact Assessment & Decision-Making](#impact-assessment--decision-making) (5 controls)
- [Risk Management & Response](#risk-management--response) (3 controls)

---

## Reading Control Entries

Each control includes:

- **Control ID**: Unique identifier (e.g., GOV-1.1)
- **Control Name**: Short descriptive name
- **NIST AI RMF**: Aligned function and subcategory
- **Description**: What the control addresses
- **Implementation Requirements**:
  - **T1 (Initial)**: Minimum requirements for low-risk AI
  - **T2 (Mature)**: Standard requirements for moderate-risk AI
  - **T3 (High-Risk)**: Comprehensive requirements for high-risk AI
- **Maturity Levels**: Minimum maturity to start, target maturity for full implementation
- **Standards Mappings**: ISO 42001 clauses, NIST AI RMF subcategories, ISO 27001 controls
- **Applicable Profiles**: Which framework profiles include this control

---

# Domain L1: Governance & Accountability

*19 controls establishing policies, accountability structures, culture, and resources for AI governance*

---

## Policies & Procedures

*7 controls defining documented governance requirements, compliance, and operational standards*

### GOV-1.1: Legal/Regulatory Compliance Policies

**NIST AI RMF**: GOVERN 1.1 - Legal and Regulatory Awareness

**Description**: Policies recognize relevant AI laws, regulations, guidance, standards, and norms

**Implementation Requirements**:
- **T1**: Awareness of key AI regulations; basic compliance documentation
- **T2**: Formal policy document addressing all applicable regulations; regular legal review
- **T3**: Comprehensive legal framework with continuous monitoring; external legal counsel engagement; regulatory change management process

**Maturity**: Min Level 2 → Target Level 3
**ISO 42001**: 4.1, 4.2, 6.1 | **ISO 27001**: A.5.1, A.5.31
**Profiles**: foundational, balanced, high-assurance, financial, healthcare, government

---

### GOV-1.2: AI Use Scope Definition

**NIST AI RMF**: GOVERN 1.2 - AI Use Characterization

**Description**: Policies define and differentiate AI system purposes, uses, and risks

**Implementation Requirements**:
- **T1**: Basic documentation of AI system purposes
- **T2**: Formal categorization of all AI systems by purpose, use case, and risk level; documented approval process
- **T3**: Comprehensive AI system registry with risk ratings; board-level approval for high-risk systems; regular review and updates

**Maturity**: Min Level 2 → Target Level 3
**ISO 42001**: 6.1 | **ISO 27001**: A.5.1
**Profiles**: foundational, balanced, high-assurance, financial, healthcare, government

---

### GOV-1.3: AI Lifecycle Governance

**NIST AI RMF**: GOVERN 1.3 - Lifecycle Integration

**Description**: Policies integrate AI risk management into organizational risk management framework

**Implementation Requirements**:
- **T1**: AI risks acknowledged in risk framework; basic escalation procedures
- **T2**: AI risk management fully integrated with enterprise risk; defined risk appetite statements for AI
- **T3**: Quantitative AI risk thresholds; automated risk monitoring; real-time risk dashboards; independent risk validation

**Maturity**: Min Level 2 → Target Level 4
**ISO 42001**: 6.1 | **ISO 27001**: A.5.1, A.8.32
**Profiles**: balanced, high-assurance, financial, healthcare, government

---

### GOV-1.4: AI Governance Compliance Monitoring

**NIST AI RMF**: GOVERN 1.4 - Compliance Verification

**Description**: Mechanisms to verify compliance with AI policies and monitor governance effectiveness

**Implementation Requirements**:
- **T1**: Basic compliance checklists; periodic manual reviews
- **T2**: Systematic compliance monitoring; defined KPIs for governance effectiveness; regular audits
- **T3**: Continuous compliance monitoring; automated policy enforcement; independent audit program; regulatory liaison function

**Maturity**: Min Level 2 → Target Level 4
**ISO 42001**: 9.1, 9.2 | **ISO 27001**: A.5.15, A.5.35
**Profiles**: balanced, high-assurance, financial, healthcare, government

---

### GOV-1.5: AI Environmental Impact Management

**NIST AI RMF**: GOVERN 1.5 - Environmental Stewardship

**Description**: Policies address environmental impacts of AI development and deployment

**Implementation Requirements**:
- **T1**: Awareness of environmental considerations
- **T2**: Environmental impact assessment for major AI systems; basic sustainability guidelines
- **T3**: Comprehensive sustainability program; carbon footprint tracking; efficiency optimization targets; public reporting

**Maturity**: Min Level 1 → Target Level 3
**ISO 42001**: 6.1 | **ISO 27001**: A.5.1
**Profiles**: balanced, high-assurance

---

### GOV-1.6: AI System Decommissioning Policies

**NIST AI RMF**: GOVERN 1.6 - Decommissioning

**Description**: Policies define processes for AI system retirement and responsible decommissioning

**Implementation Requirements**:
- **T1**: Basic end-of-life considerations documented
- **T2**: Formal decommissioning procedures; data retention/disposal requirements; stakeholder notification process
- **T3**: Comprehensive decommissioning playbook; impact assessment requirements; knowledge preservation; regulatory compliance verification

**Maturity**: Min Level 2 → Target Level 3
**ISO 42001**: 8.1 | **ISO 27001**: A.8.10, A.8.11
**Profiles**: balanced, high-assurance, financial, healthcare, government

---

### GOV-1.7: Third-Party AI Risk Management

**NIST AI RMF**: GOVERN 1.7 - Third-Party Management

**Description**: Policies address AI risks from third-party components, services, and data

**Implementation Requirements**:
- **T1**: Basic third-party awareness; vendor list maintained
- **T2**: Third-party risk assessment requirements; contractual AI provisions; ongoing monitoring
- **T3**: Comprehensive third-party risk program; independent vendor audits; supply chain security; real-time monitoring

**Maturity**: Min Level 2 → Target Level 4
**ISO 42001**: 8.1 | **ISO 27001**: A.5.19, A.5.20, A.5.21
**Profiles**: balanced, high-assurance, financial, healthcare, government

---

## Organizational Structure & Roles

*3 controls establishing accountability, role definitions, and executive oversight*

### GOV-2.1: AI Accountability Assignment

**NIST AI RMF**: GOVERN 2.1 - Role Definition

**Description**: Roles and responsibilities for AI risk management are established and assigned

**Implementation Requirements**:
- **T1**: Key AI responsibilities identified; informal assignments
- **T2**: Formal RACI matrix for AI governance; documented role descriptions; clear escalation paths
- **T3**: Comprehensive organizational structure; independent AI oversight function; board-level accountability; external advisory mechanisms

**Maturity**: Min Level 2 → Target Level 3
**ISO 42001**: 5.1, 5.3 | **ISO 27001**: A.5.1, A.5.2
**Profiles**: foundational, balanced, high-assurance, financial, healthcare, government

---

### GOV-2.2: AI Competency Development

**NIST AI RMF**: GOVERN 2.2 - Workforce Training

**Description**: Training and awareness programs for AI risk and governance are established

**Implementation Requirements**:
- **T1**: Basic AI awareness training available
- **T2**: Role-based training programs; competency assessments; regular refresher training
- **T3**: Comprehensive certification programs; continuous professional development; specialized expertise development; external training validation

**Maturity**: Min Level 2 → Target Level 3
**ISO 42001**: 7.2, 7.3 | **ISO 27001**: A.6.3
**Profiles**: foundational, balanced, high-assurance, financial, healthcare, government

---

### GOV-2.3: Executive AI Oversight

**NIST AI RMF**: GOVERN 2.3 - Executive Engagement

**Description**: Senior leadership engagement and oversight of AI risk management is established

**Implementation Requirements**:
- **T1**: Executive sponsorship identified; periodic briefings
- **T2**: Formal executive oversight committee; regular reporting to leadership; strategic AI review sessions
- **T3**: Board-level AI committee; independent risk function reporting; external advisory board; shareholder communication

**Maturity**: Min Level 2 → Target Level 4
**ISO 42001**: 5.1, 5.2 | **ISO 27001**: A.5.1, A.5.4
**Profiles**: foundational, balanced, high-assurance, financial, healthcare, government

---

## Workforce Diversity & Inclusion

*2 controls promoting diverse teams and demographic representation*

### GOV-3.1: Interdisciplinary AI Teams

**NIST AI RMF**: GOVERN 3.1 - Cross-Functional Teams

**Description**: AI teams include diverse perspectives and interdisciplinary expertise

**Implementation Requirements**:
- **T1**: Awareness of diversity importance; some cross-functional involvement
- **T2**: Required diverse team composition; documented expertise requirements; inclusion metrics
- **T3**: Comprehensive diversity program; measurable targets; independent diversity audits; public reporting on team composition

**Maturity**: Min Level 2 → Target Level 3
**ISO 42001**: 7.1, 7.2 | **ISO 27001**: A.6.2
**Profiles**: balanced, high-assurance, healthcare, government

---

### GOV-3.2: Demographic Diversity in AI

**NIST AI RMF**: GOVERN 3.2 - Demographic Representation

**Description**: Policies promote demographic diversity in AI development and deployment teams

**Implementation Requirements**:
- **T1**: Basic diversity awareness; non-discrimination policies
- **T2**: Active diversity programs; representation monitoring; bias in hiring assessed
- **T3**: Industry-leading diversity initiatives; external partnerships; public diversity commitments; inclusion effectiveness measured

**Maturity**: Min Level 1 → Target Level 3
**ISO 42001**: 7.1 | **ISO 27001**: —
**Profiles**: balanced, high-assurance, government

---

## Organizational Culture & Ethics

*5 controls building AI risk culture, stakeholder engagement, and transparency*

### GOV-4.1: AI Risk Culture Development

**NIST AI RMF**: GOVERN 4.1 - Risk Culture

**Description**: Culture of AI risk awareness and responsible AI practices is fostered

**Implementation Requirements**:
- **T1**: Basic awareness communications; leadership statements
- **T2**: Systematic culture program; risk awareness integrated into performance; recognition programs
- **T3**: Mature risk culture; embedded in values; external recognition; industry thought leadership; culture metrics tracked

**Maturity**: Min Level 2 → Target Level 4
**ISO 42001**: 5.2, 7.3 | **ISO 27001**: A.5.1
**Profiles**: balanced, high-assurance, financial, healthcare, government

---

### GOV-4.2: AI Feedback Integration

**NIST AI RMF**: GOVERN 4.2 - Stakeholder Feedback

**Description**: Processes capture and integrate stakeholder feedback on AI systems

**Implementation Requirements**:
- **T1**: Basic feedback channels exist; ad-hoc response
- **T2**: Systematic feedback collection; defined response processes; feedback influences decisions
- **T3**: Comprehensive stakeholder engagement; real-time feedback integration; public transparency on feedback; external validation

**Maturity**: Min Level 2 → Target Level 3
**ISO 42001**: 7.4 | **ISO 27001**: A.5.6
**Profiles**: balanced, high-assurance, healthcare, government

---

### GOV-4.3: AI Transparency Communication

**NIST AI RMF**: GOVERN 4.3 - Communication

**Description**: Organizational communication practices support AI transparency and accountability

**Implementation Requirements**:
- **T1**: Basic internal communications; reactive external communication
- **T2**: Proactive communication program; transparency reports; stakeholder engagement strategy
- **T3**: Industry-leading transparency; real-time communication; public AI governance reporting; external stakeholder councils

**Maturity**: Min Level 2 → Target Level 4
**ISO 42001**: 7.4 | **ISO 27001**: A.5.6
**Profiles**: balanced, high-assurance, government

---

### GOV-5.1: AI Ecosystem Engagement

**NIST AI RMF**: GOVERN 5.1 - External Partnerships

**Description**: Engagement with external AI ecosystem including regulators, standards bodies, and peers

**Implementation Requirements**:
- **T1**: Awareness of ecosystem; periodic participation
- **T2**: Active ecosystem participation; standards body involvement; regulatory engagement
- **T3**: Leadership in ecosystem; standards development contribution; regulatory dialogue; industry coalition participation

**Maturity**: Min Level 1 → Target Level 3
**ISO 42001**: 4.2 | **ISO 27001**: —
**Profiles**: balanced, high-assurance, government

---

### GOV-5.2: AI Research Collaboration

**NIST AI RMF**: GOVERN 5.2 - Academic Collaboration

**Description**: Partnerships with academic and research institutions for AI advancement

**Implementation Requirements**:
- **T1**: Awareness of research opportunities; occasional engagement
- **T2**: Formal research partnerships; knowledge exchange programs; publication support
- **T3**: Comprehensive research program; joint appointments; research funding; public research contribution

**Maturity**: Min Level 1 → Target Level 3
**ISO 42001**: 4.2 | **ISO 27001**: —
**Profiles**: balanced, high-assurance

---

## Implementation Resources

*2 controls ensuring adequate resources and capability building*

### GOV-6.1: AI Governance Resourcing

**NIST AI RMF**: GOVERN 6.1 - Resource Allocation

**Description**: Adequate resources (budget, personnel, tools) are allocated for AI governance

**Implementation Requirements**:
- **T1**: Basic resources identified; informal allocation
- **T2**: Formal budget allocation; dedicated personnel; governance tools deployed
- **T3**: Comprehensive resourcing; independent governance function; advanced tooling; external expertise engagement

**Maturity**: Min Level 2 → Target Level 3
**ISO 42001**: 7.1, 7.5 | **ISO 27001**: A.5.1
**Profiles**: foundational, balanced, high-assurance, financial, healthcare, government

---

### GOV-6.2: AI Governance Capability Development

**NIST AI RMF**: GOVERN 6.2 - Capability Building

**Description**: Investments in building and maintaining AI governance capabilities

**Implementation Requirements**:
- **T1**: Foundational capabilities recognized; basic investment
- **T2**: Systematic capability building; technology investments; process improvement programs
- **T3**: Industry-leading capabilities; continuous innovation; research investment; capability sharing

**Maturity**: Min Level 2 → Target Level 4
**ISO 42001**: 7.2, 10.2 | **ISO 27001**: A.6.3
**Profiles**: balanced, high-assurance, financial, healthcare

---

# Domain L2: Data Management & Privacy

*6 controls for data quality, privacy, and third-party data governance*

---

## Data Quality & Integrity

*2 controls ensuring data validity and fitness for purpose*

### MAP-1.6: AI System Requirements

**NIST AI RMF**: MAP 1.6 - Requirements

**Description**: System requirements including socio-technical implications are elicited

**Implementation Requirements**:
- **T1**: Basic technical requirements gathered
- **T2**: Comprehensive requirements including socio-technical; stakeholder input; requirements traceability
- **T3**: Exhaustive requirements engineering; independent validation; continuous requirements management; impact assessment

**Maturity**: Min Level 2 → Target Level 3
**ISO 42001**: 6.2, 8.2 | **ISO 27001**: A.5.1
**Profiles**: balanced, high-assurance, financial, healthcare, government

---

### MEA-2.5: AI Validity and Reliability

**NIST AI RMF**: MEASURE 2.5 - Validity Testing

**Description**: System validity and reliability are demonstrated and documented

**Implementation Requirements**:
- **T1**: Basic validation performed
- **T2**: Comprehensive validity/reliability testing; generalizability documented; continuous validation
- **T3**: Advanced validation science; statistical rigor; continuous reliability tracking; public validation reports

**Maturity**: Min Level 2 → Target Level 3
**ISO 42001**: 8.2 | **ISO 27001**: A.8.29
**Profiles**: balanced, high-assurance, financial, healthcare, government

---

## Data Privacy & Protection

*1 control for privacy risk assessment and protection*

### MEA-2.10: AI Privacy Evaluation

**NIST AI RMF**: MEASURE 2.10 - Privacy Assessment

**Description**: Privacy risks are examined and documented

**Implementation Requirements**:
- **T1**: Basic privacy assessment
- **T2**: Comprehensive privacy evaluation; privacy-preserving techniques assessed; privacy documentation
- **T3**: Advanced privacy program; privacy-by-design; continuous privacy monitoring; independent privacy audit

**Maturity**: Min Level 2 → Target Level 4
**ISO 42001**: 6.1, 8.2 | **ISO 27001**: A.5.33, A.5.34, A.8.10, A.8.11
**Profiles**: balanced, high-assurance, financial, healthcare, government

---

## Third-Party Data Governance

*3 controls managing data risks from external sources*

### MAP-4.1: Third-Party AI Risk Assessment

**NIST AI RMF**: MAP 4.1 - Risk Mapping

**Description**: Approaches for mapping AI technology and legal risks from third parties are in place

**Implementation Requirements**:
- **T1**: Basic third-party risk awareness
- **T2**: Systematic third-party risk mapping; legal risk assessment; documented approaches
- **T3**: Comprehensive third-party risk program; continuous monitoring; independent assessment; supply chain visibility

**Maturity**: Min Level 2 → Target Level 3
**ISO 42001**: 4.2, 8.1 | **ISO 27001**: A.5.19, A.5.20
**Profiles**: balanced, high-assurance, financial, healthcare, government

---

### MAP-4.2: Third-Party Risk Controls

**NIST AI RMF**: MAP 4.2 - Internal Controls

**Description**: Internal risk controls for third-party AI components are identified and implemented

**Implementation Requirements**:
- **T1**: Basic controls identified
- **T2**: Comprehensive risk controls; documented implementation; effectiveness monitoring
- **T3**: Advanced control framework; automated controls; real-time monitoring; independent validation

**Maturity**: Min Level 2 → Target Level 4
**ISO 42001**: 6.1, 8.1 | **ISO 27001**: A.5.19, A.5.21
**Profiles**: balanced, high-assurance, financial, healthcare, government

---

### MAN-3.1: Third-Party AI Ongoing Monitoring

**NIST AI RMF**: MANAGE 3.1 - Third-Party Monitoring

**Description**: AI risks and benefits from third parties are regularly monitored and controlled

**Implementation Requirements**:
- **T1**: Basic third-party awareness
- **T2**: Systematic third-party monitoring; controls applied; performance tracked
- **T3**: Advanced third-party management; real-time monitoring; automated controls; supply chain visibility

**Maturity**: Min Level 2 → Target Level 4
**ISO 42001**: 4.2, 8.1 | **ISO 27001**: A.5.19, A.5.20, A.5.21
**Profiles**: balanced, high-assurance, financial, healthcare, government

---

# Domain L3: Technical Operations & MLOps

*31 controls for development, deployment, monitoring, security, and measurement*

---

## Development & Testing

*7 controls for AI development, testing, and validation*

### MAP-2.1: AI System Task Categorization

**NIST AI RMF**: MAP 2.1 - Task Classification

**Description**: Specific tasks and methods of AI systems are defined and categorized

**Implementation Requirements**:
- **T1**: Basic categorization of major systems
- **T2**: Formal taxonomy applied; comprehensive categorization; method documentation
- **T3**: Comprehensive classification system; automated categorization; independent validation; continuous classification

**Maturity**: Min Level 2 → Target Level 3
**ISO 42001**: 6.2 | **ISO 27001**: —
**Profiles**: foundational, balanced, high-assurance, financial, healthcare, government

---

### MAP-2.2: AI System Boundaries

**NIST AI RMF**: MAP 2.2 - Knowledge Limits

**Description**: Knowledge limits and human oversight requirements are documented

**Implementation Requirements**:
- **T1**: Basic awareness of system limits
- **T2**: Comprehensive documentation of limits; human oversight planned; decision support context
- **T3**: Exhaustive boundary documentation; automated limit detection; real-time oversight; independent validation

**Maturity**: Min Level 2 → Target Level 3
**ISO 42001**: 8.1, 8.2 | **ISO 27001**: —
**Profiles**: balanced, high-assurance, financial, healthcare, government

---

### MAP-2.3: AI Scientific Rigor

**NIST AI RMF**: MAP 2.3 - Scientific Integrity

**Description**: Scientific integrity and TEVV considerations are documented

**Implementation Requirements**:
- **T1**: Basic testing approach defined
- **T2**: Comprehensive TEVV planning; scientific methodology documented; validation planned
- **T3**: Rigorous scientific standards; independent validation; research-grade methodology; public methodology

**Maturity**: Min Level 2 → Target Level 4
**ISO 42001**: 8.2, 9.1 | **ISO 27001**: —
**Profiles**: balanced, high-assurance, healthcare

---

### MEA-2.1: AI Testing Documentation

**NIST AI RMF**: MEASURE 2.1 - Test Documentation

**Description**: Test sets, metrics, and tools used in evaluation are documented

**Implementation Requirements**:
- **T1**: Basic test documentation
- **T2**: Comprehensive TEVV documentation; version control; methodology documentation
- **T3**: Exhaustive documentation; automated documentation; public methodology; research-grade practices

**Maturity**: Min Level 2 → Target Level 3
**ISO 42001**: 8.2 | **ISO 27001**: A.5.37
**Profiles**: balanced, high-assurance, financial, healthcare, government

---

### MEA-2.2: AI Human Subject Testing

**NIST AI RMF**: MEASURE 2.2 - Human Evaluation

**Description**: Human subject evaluations follow ethical standards and representative sampling

**Implementation Requirements**:
- **T1**: Basic ethical consideration
- **T2**: Formal ethics review; representative sampling; participant protections
- **T3**: Comprehensive human research program; IRB oversight; external ethics review; public protocols

**Maturity**: Min Level 2 → Target Level 4
**ISO 42001**: 8.2 | **ISO 27001**: A.5.34
**Profiles**: balanced, high-assurance, healthcare, government

---

### MEA-2.3: AI Performance Measurement

**NIST AI RMF**: MEASURE 2.3 - Performance Criteria

**Description**: Performance and assurance criteria are measured and demonstrated

**Implementation Requirements**:
- **T1**: Basic performance metrics
- **T2**: Comprehensive performance measurement; deployment-like testing; criteria documentation
- **T3**: Advanced performance validation; automated measurement; continuous demonstration; public performance reports

**Maturity**: Min Level 2 → Target Level 3
**ISO 42001**: 8.2, 9.1 | **ISO 27001**: A.8.16
**Profiles**: foundational, balanced, high-assurance, financial, healthcare, government

---

### MEA-2.13: AI Testing Effectiveness

**NIST AI RMF**: MEASURE 2.13 - TEVV Effectiveness

**Description**: TEVV effectiveness is evaluated

**Implementation Requirements**:
- **T1**: Basic TEVV review
- **T2**: Systematic TEVV evaluation; metrics effectiveness assessed; continuous improvement
- **T3**: Advanced TEVV optimization; meta-evaluation; automated effectiveness assessment; research contribution

**Maturity**: Min Level 3 → Target Level 4
**ISO 42001**: 9.1, 10.2 | **ISO 27001**: A.8.29
**Profiles**: high-assurance, healthcare

---

## Deployment & Operations

*6 controls for production deployment and operational management*

### MAP-3.3: AI Application Scope

**NIST AI RMF**: MAP 3.3 - Scope Definition

**Description**: Targeted application scope is specified and documented

**Implementation Requirements**:
- **T1**: Basic scope defined
- **T2**: Comprehensive scope specification; clear boundaries; scope change management
- **T3**: Precise scope specification; automated scope monitoring; real-time drift detection; independent validation

**Maturity**: Min Level 2 → Target Level 3
**ISO 42001**: 6.2 | **ISO 27001**: —
**Profiles**: foundational, balanced, high-assurance, financial, healthcare, government

---

### MAP-3.5: Human Oversight Design

**NIST AI RMF**: MAP 3.5 - Human Oversight

**Description**: Human oversight processes are documented and aligned with policies

**Implementation Requirements**:
- **T1**: Basic oversight mechanisms
- **T2**: Comprehensive oversight processes; policy alignment; oversight effectiveness assessment
- **T3**: Advanced oversight design; automated assistance; real-time oversight monitoring; independent validation

**Maturity**: Min Level 2 → Target Level 3
**ISO 42001**: 8.1, 8.2 | **ISO 27001**: A.5.3
**Profiles**: foundational, balanced, high-assurance, financial, healthcare, government

---

### MEA-2.4: AI Production Monitoring

**NIST AI RMF**: MEASURE 2.4 - Production Monitoring

**Description**: AI system functionality is monitored in production

**Implementation Requirements**:
- **T1**: Basic production monitoring
- **T2**: Comprehensive production monitoring; component behavior tracked; anomaly detection
- **T3**: Advanced MLOps monitoring; AI-powered monitoring; predictive alerting; real-time dashboards

**Maturity**: Min Level 2 → Target Level 4
**ISO 42001**: 8.1, 9.1 | **ISO 27001**: A.8.15, A.8.16
**Profiles**: foundational, balanced, high-assurance, financial, healthcare, government

---

### MAN-2.4: AI System Disengage/Deactivate

**NIST AI RMF**: MANAGE 2.4 - System Control

**Description**: Mechanisms to supersede, disengage, or deactivate AI systems are in place

**Implementation Requirements**:
- **T1**: Basic shutdown awareness
- **T2**: Comprehensive control mechanisms; tested procedures; clear responsibilities
- **T3**: Advanced failsafe systems; automated disengage; predictive intervention; self-healing capabilities

**Maturity**: Min Level 2 → Target Level 3
**ISO 42001**: 8.1 | **ISO 27001**: A.5.30
**Profiles**: balanced, high-assurance, financial, healthcare, government

---

### MAN-3.2: Pre-trained Model Management

**NIST AI RMF**: MANAGE 3.2 - Model Monitoring

**Description**: Pre-trained models are monitored as part of AI system maintenance

**Implementation Requirements**:
- **T1**: Basic model awareness
- **T2**: Comprehensive model monitoring; change tracking; performance assessment
- **T3**: Advanced model management; automated model monitoring; predictive drift detection; continuous validation

**Maturity**: Min Level 2 → Target Level 4
**ISO 42001**: 8.1 | **ISO 27001**: A.5.9, A.8.32
**Profiles**: balanced, high-assurance, financial, healthcare, government

---

### MAN-4.1: AI Post-Deployment Monitoring

**NIST AI RMF**: MANAGE 4.1 - Post-Deployment

**Description**: Post-deployment monitoring, appeal, decommissioning, and incident response plans implemented

**Implementation Requirements**:
- **T1**: Basic post-deployment consideration
- **T2**: Comprehensive post-deployment plans; all elements addressed; tested procedures
- **T3**: Advanced post-deployment management; AI-powered monitoring; automated response; continuous optimization

**Maturity**: Min Level 2 → Target Level 4
**ISO 42001**: 8.1, 10.1 | **ISO 27001**: A.5.24, A.5.25
**Profiles**: balanced, high-assurance, financial, healthcare, government

---

## Monitoring & Maintenance

*5 controls for continuous monitoring and system maintenance*

### MEA-3.1: AI Continuous Risk Tracking

**NIST AI RMF**: MEASURE 3.1 - Continuous Monitoring

**Description**: Mechanisms for tracking existing, unanticipated, and emergent AI risks over time

**Implementation Requirements**:
- **T1**: Basic ongoing monitoring
- **T2**: Comprehensive risk tracking; dedicated personnel; emergent risk detection
- **T3**: Advanced risk intelligence; predictive risk monitoring; automated tracking; real-time risk dashboards

**Maturity**: Min Level 2 → Target Level 4
**ISO 42001**: 8.1, 9.1 | **ISO 27001**: A.5.7
**Profiles**: balanced, high-assurance, financial, healthcare, government

---

### MEA-3.2: AI Risk Assessment in Complex Contexts

**NIST AI RMF**: MEASURE 3.2 - Complex Settings

**Description**: Risk tracking approaches for difficult-to-assess settings are defined

**Implementation Requirements**:
- **T1**: Basic awareness of challenges
- **T2**: Alternative assessment approaches; documented limitations; multiple methods
- **T3**: Advanced measurement innovation; research into novel methods; comprehensive alternative approaches; public methodology

**Maturity**: Min Level 3 → Target Level 4
**ISO 42001**: 9.1 | **ISO 27001**: —
**Profiles**: high-assurance, healthcare

---

### MEA-4.3: AI Performance Change Detection

**NIST AI RMF**: MEASURE 4.3 - Performance Trends

**Description**: Performance improvements or declines are identified and documented

**Implementation Requirements**:
- **T1**: Basic trend awareness
- **T2**: Systematic trend tracking; root cause analysis; performance documentation
- **T3**: Advanced analytics; predictive performance modeling; automated change detection; real-time performance intelligence

**Maturity**: Min Level 2 → Target Level 4
**ISO 42001**: 9.1, 10.1 | **ISO 27001**: A.8.16, A.8.32
**Profiles**: balanced, high-assurance, financial, healthcare, government

---

### MAN-2.2: AI Value Preservation

**NIST AI RMF**: MANAGE 2.2 - Value Sustainment

**Description**: Mechanisms to sustain AI system value over time are in place

**Implementation Requirements**:
- **T1**: Basic maintenance
- **T2**: Comprehensive value sustainment program; active monitoring; maintenance strategy
- **T3**: Advanced value optimization; predictive value modeling; self-sustaining mechanisms; continuous optimization

**Maturity**: Min Level 2 → Target Level 4
**ISO 42001**: 8.1, 10.2 | **ISO 27001**: —
**Profiles**: balanced, high-assurance, financial, healthcare

---

### MAN-4.2: AI Continuous Improvement Integration

**NIST AI RMF**: MANAGE 4.2 - Continuous Improvement

**Description**: Measurable improvements are integrated into AI system updates

**Implementation Requirements**:
- **T1**: Basic improvement awareness
- **T2**: Systematic improvement integration; stakeholder engagement; best practices captured
- **T3**: Advanced improvement optimization; AI-powered improvement identification; automated integration; industry leadership

**Maturity**: Min Level 3 → Target Level 5
**ISO 42001**: 10.2 | **ISO 27001**: A.5.37
**Profiles**: balanced, high-assurance, financial, healthcare

---

## Security & Resilience

*4 controls for security, safety, and incident response*

### MEA-2.6: AI Safety Evaluation

**NIST AI RMF**: MEASURE 2.6 - Safety Assessment

**Description**: Safety risks are evaluated and residual risks documented

**Implementation Requirements**:
- **T1**: Basic safety assessment
- **T2**: Comprehensive safety evaluation; fail-safe testing; residual risk documentation
- **T3**: Advanced safety program; independent safety validation; continuous safety monitoring; public safety reports

**Maturity**: Min Level 2 → Target Level 4
**ISO 42001**: 6.1, 8.2 | **ISO 27001**: A.5.1
**Profiles**: balanced, high-assurance, healthcare, government

---

### MEA-2.7: AI Security and Resilience

**NIST AI RMF**: MEASURE 2.7 - Security Assessment

**Description**: Security and resilience against adversarial attacks are evaluated

**Implementation Requirements**:
- **T1**: Basic security assessment
- **T2**: Comprehensive security evaluation; adversarial testing; resilience documentation
- **T3**: Advanced security program; red team testing; continuous security monitoring; independent penetration testing

**Maturity**: Min Level 2 → Target Level 4
**ISO 42001**: 6.1, 8.2 | **ISO 27001**: A.8.1, A.8.2, A.8.8
**Profiles**: balanced, high-assurance, financial, healthcare, government

---

### MAN-2.3: AI Emergent Risk Response

**NIST AI RMF**: MANAGE 2.3 - Unknown Risk Response

**Description**: Procedures for responding to previously unknown or emergent risks are established

**Implementation Requirements**:
- **T1**: Basic response awareness
- **T2**: Comprehensive emergent risk procedures; recovery processes; lessons learned
- **T3**: Advanced emergent risk management; predictive detection; automated response; real-time adaptation

**Maturity**: Min Level 2 → Target Level 4
**ISO 42001**: 8.1, 10.1 | **ISO 27001**: A.5.24, A.5.25, A.5.26
**Profiles**: balanced, high-assurance, financial, healthcare, government

---

### MAN-4.3: AI Incident and Error Reporting

**NIST AI RMF**: MANAGE 4.3 - Incident Communication

**Description**: Incidents and errors are communicated to relevant stakeholders and tracked

**Implementation Requirements**:
- **T1**: Basic incident reporting
- **T2**: Comprehensive incident program; systematic communication; recovery documentation
- **T3**: Advanced incident management; AI-powered detection; automated communication; public incident transparency

**Maturity**: Min Level 2 → Target Level 3
**ISO 42001**: 10.1, 9.1 | **ISO 27001**: A.5.24, A.5.25, A.5.26
**Profiles**: foundational, balanced, high-assurance, financial, healthcare, government

---

## Measurement & Evaluation

*5 controls for metrics, measurement approaches, and evaluation*

### MEA-1.1: AI Risk Measurement Selection

**NIST AI RMF**: MEASURE 1.1 - Measurement Approaches

**Description**: Appropriate approaches and metrics for measuring AI risks are selected and implemented

**Implementation Requirements**:
- **T1**: Basic metrics for major risks identified
- **T2**: Comprehensive measurement framework; validated metrics; documented approach
- **T3**: Advanced measurement science; automated measurement; predictive metrics; industry-leading practices

**Maturity**: Min Level 2 → Target Level 4
**ISO 42001**: 9.1 | **ISO 27001**: A.8.16
**Profiles**: balanced, high-assurance, financial, healthcare, government

---

### MEA-1.2: AI Metric Validation

**NIST AI RMF**: MEASURE 1.2 - Metric Effectiveness

**Description**: Appropriateness and effectiveness of AI metrics is assessed and updated

**Implementation Requirements**:
- **T1**: Periodic metric review
- **T2**: Systematic metric assessment; effectiveness validation; regular updates based on data
- **T3**: Continuous metric optimization; AI-powered metric assessment; automated effectiveness tracking; research contribution

**Maturity**: Min Level 3 → Target Level 4
**ISO 42001**: 9.1 | **ISO 27001**: A.5.36
**Profiles**: balanced, high-assurance, healthcare

---

### MEA-1.3: AI Independent Evaluation

**NIST AI RMF**: MEASURE 1.3 - Independent Assessment

**Description**: Internal experts and independent assessors are involved in AI evaluation

**Implementation Requirements**:
- **T1**: Some expert involvement
- **T2**: Required independent assessment; diverse expert input; documented assessment process
- **T3**: Comprehensive independent program; external assessors; public assessment reports; industry certification

**Maturity**: Min Level 2 → Target Level 4
**ISO 42001**: 9.2, 9.3 | **ISO 27001**: A.5.35
**Profiles**: balanced, high-assurance, financial, healthcare, government

---

### MEA-4.1: AI Measurement-Context Alignment

**NIST AI RMF**: MEASURE 4.1 - Context Connection

**Description**: Measurement approaches are connected to deployment context

**Implementation Requirements**:
- **T1**: Basic context consideration
- **T2**: Systematic context alignment; domain expert input; end user input
- **T3**: Advanced context-aware measurement; automated alignment; predictive context modeling; continuous adaptation

**Maturity**: Min Level 2 → Target Level 3
**ISO 42001**: 9.1 | **ISO 27001**: —
**Profiles**: balanced, high-assurance, financial, healthcare, government

---

### MEA-4.2: AI Results Expert Review

**NIST AI RMF**: MEASURE 4.2 - Expert Validation

**Description**: Measurement results are informed and validated by domain experts

**Implementation Requirements**:
- **T1**: Some expert review
- **T2**: Systematic expert validation; AI actor input; consistency validation
- **T3**: Comprehensive expert program; automated expert consultation; validated by external experts; public validation

**Maturity**: Min Level 2 → Target Level 3
**ISO 42001**: 9.1, 9.3 | **ISO 27001**: A.5.35
**Profiles**: balanced, high-assurance, healthcare, government

---

## Trustworthy AI Characteristics

*4 controls evaluating transparency, explainability, fairness, and environmental impact*

### MEA-2.8: AI Transparency Evaluation

**NIST AI RMF**: MEASURE 2.8 - Transparency Assessment

**Description**: Transparency and accountability risks are examined

**Implementation Requirements**:
- **T1**: Basic transparency review
- **T2**: Comprehensive transparency assessment; accountability mechanisms evaluated; documentation review
- **T3**: Advanced transparency program; explainability metrics; public transparency reports; independent review

**Maturity**: Min Level 2 → Target Level 3
**ISO 42001**: 8.2 | **ISO 27001**: —
**Profiles**: balanced, high-assurance, financial, government

---

### MEA-2.9: AI Model Explanation

**NIST AI RMF**: MEASURE 2.9 - Explainability

**Description**: AI model is explained, validated, documented for output interpretation

**Implementation Requirements**:
- **T1**: Basic model description
- **T2**: Comprehensive model explanation; validation documentation; interpretation guidance
- **T3**: Advanced explainability; user-appropriate explanations; continuous validation; public model documentation

**Maturity**: Min Level 2 → Target Level 3
**ISO 42001**: 8.2 | **ISO 27001**: —
**Profiles**: balanced, high-assurance, financial, healthcare, government

---

### MEA-2.11: AI Fairness and Bias Testing

**NIST AI RMF**: MEASURE 2.11 - Fairness Assessment

**Description**: Fairness and bias in AI systems are evaluated

**Implementation Requirements**:
- **T1**: Basic bias testing
- **T2**: Comprehensive fairness evaluation; multiple metrics; demographic analysis; mitigation assessment
- **T3**: Advanced fairness program; intersectional analysis; continuous bias monitoring; public fairness reports

**Maturity**: Min Level 2 → Target Level 4
**ISO 42001**: 8.2 | **ISO 27001**: —
**Profiles**: balanced, high-assurance, financial, healthcare, government

---

### MEA-2.12: AI Environmental Impact

**NIST AI RMF**: MEASURE 2.12 - Environmental Assessment

**Description**: Environmental impact and sustainability of AI are assessed

**Implementation Requirements**:
- **T1**: Basic environmental awareness
- **T2**: Comprehensive environmental assessment; energy tracking; sustainability consideration
- **T3**: Advanced sustainability program; carbon tracking; efficiency optimization; public environmental reports

**Maturity**: Min Level 1 → Target Level 3
**ISO 42001**: 6.1 | **ISO 27001**: —
**Profiles**: balanced, high-assurance

---

# Domain L4: Organizational Culture & Capabilities

*17 controls for workforce development, stakeholder engagement, strategy, and risk response*

---

## Workforce Development & Training

*2 controls for team diversity and operator proficiency*

### MAP-1.2: AI Development Team Composition

**NIST AI RMF**: MAP 1.2 - Team Diversity

**Description**: Interdisciplinary AI actors with diverse competencies are involved in development

**Implementation Requirements**:
- **T1**: Some cross-functional involvement; basic diversity awareness
- **T2**: Required diverse team composition; documented competency requirements; team composition review
- **T3**: Comprehensive diversity requirements; measurable outcomes; external expertise; team effectiveness measured

**Maturity**: Min Level 2 → Target Level 3
**ISO 42001**: 7.1 | **ISO 27001**: A.6.2
**Profiles**: balanced, high-assurance, healthcare, government

---

### MAP-3.4: AI Operator Requirements

**NIST AI RMF**: MAP 3.4 - Operator Proficiency

**Description**: Operator/practitioner proficiency requirements are documented

**Implementation Requirements**:
- **T1**: Basic proficiency expectations
- **T2**: Formal proficiency requirements; assessment processes; certification requirements
- **T3**: Comprehensive competency framework; continuous assessment; independent certification; proficiency tracking

**Maturity**: Min Level 2 → Target Level 3
**ISO 42001**: 7.2, 7.3 | **ISO 27001**: A.6.3
**Profiles**: balanced, high-assurance, financial, healthcare, government

---

## Stakeholder Engagement & Communication

*2 controls for stakeholder feedback and user engagement*

### MAP-5.2: AI Stakeholder Feedback

**NIST AI RMF**: MAP 5.2 - Stakeholder Engagement

**Description**: Practices for engaging relevant AI actors to understand impacts are in place

**Implementation Requirements**:
- **T1**: Basic engagement mechanisms
- **T2**: Systematic engagement program; feedback integration; engagement effectiveness tracked
- **T3**: Comprehensive engagement ecosystem; real-time feedback; external advisory; public engagement reports

**Maturity**: Min Level 2 → Target Level 3
**ISO 42001**: 4.2, 7.4 | **ISO 27001**: A.5.6
**Profiles**: balanced, high-assurance, healthcare, government

---

### MEA-3.3: AI User Feedback Processes

**NIST AI RMF**: MEASURE 3.3 - Feedback Integration

**Description**: End user and community feedback processes are established

**Implementation Requirements**:
- **T1**: Basic feedback channels
- **T2**: Comprehensive feedback program; problem reporting; appeal processes; feedback integration
- **T3**: Advanced feedback ecosystem; real-time feedback; AI-powered analysis; public feedback transparency

**Maturity**: Min Level 2 → Target Level 3
**ISO 42001**: 7.4, 9.1 | **ISO 27001**: A.5.6
**Profiles**: balanced, high-assurance, healthcare, government

---

## Strategic Alignment & Context

*4 controls for purpose, strategy, value, and risk tolerance*

### MAP-1.1: AI System Purpose Characterization

**NIST AI RMF**: MAP 1.1 - Purpose Documentation

**Description**: Intended purposes, beneficial uses, laws/norms, and deployment settings are documented

**Implementation Requirements**:
- **T1**: Basic purpose documentation for major systems
- **T2**: Comprehensive documentation for all AI systems; legal/regulatory review; stakeholder input
- **T3**: Exhaustive documentation; independent review; continuous validation; public transparency on purposes

**Maturity**: Min Level 2 → Target Level 3
**ISO 42001**: 4.1, 6.2 | **ISO 27001**: A.5.1
**Profiles**: foundational, balanced, high-assurance, financial, healthcare, government

---

### MAP-1.3: AI Strategic Alignment

**NIST AI RMF**: MAP 1.3 - Strategic Alignment

**Description**: Organization's mission and goals for AI technology are understood and documented

**Implementation Requirements**:
- **T1**: Basic strategic alignment acknowledged
- **T2**: Formal strategic alignment documentation; regular review against mission; clear AI strategy
- **T3**: Strategic AI integration; board-level strategy review; public AI strategy; strategic KPIs tracked

**Maturity**: Min Level 2 → Target Level 3
**ISO 42001**: 4.1, 6.2 | **ISO 27001**: A.5.1
**Profiles**: balanced, high-assurance, financial, healthcare, government

---

### MAP-1.4: AI Business Value Documentation

**NIST AI RMF**: MAP 1.4 - Business Value

**Description**: Business value or context of business use is clearly defined

**Implementation Requirements**:
- **T1**: Basic value proposition documented
- **T2**: Comprehensive business case requirements; value metrics defined; ROI tracking
- **T3**: Quantified value realization; continuous value monitoring; value optimization; public value reporting

**Maturity**: Min Level 2 → Target Level 3
**ISO 42001**: 6.2 | **ISO 27001**: —
**Profiles**: balanced, high-assurance, financial, healthcare

---

### MAP-1.5: AI Risk Tolerance Definition

**NIST AI RMF**: MAP 1.5 - Risk Tolerance

**Description**: Organizational risk tolerances for AI systems are determined and documented

**Implementation Requirements**:
- **T1**: Basic risk awareness; informal tolerance
- **T2**: Formal risk tolerance statements; quantified where possible; governance approval
- **T3**: Comprehensive risk appetite framework; quantified tolerances; real-time monitoring; board approval

**Maturity**: Min Level 2 → Target Level 3
**ISO 42001**: 6.1 | **ISO 27001**: A.5.1
**Profiles**: foundational, balanced, high-assurance, financial, healthcare, government

---

## Impact Assessment & Decision-Making

*5 controls for benefits, costs, impacts, and go/no-go decisions*

### MAP-3.1: AI Benefits Documentation

**NIST AI RMF**: MAP 3.1 - Benefits Analysis

**Description**: Potential benefits are examined and documented

**Implementation Requirements**:
- **T1**: Basic benefits identified
- **T2**: Comprehensive benefits analysis; quantified where possible; validation approach
- **T3**: Rigorous benefit quantification; independent validation; continuous benefit tracking; public benefit reporting

**Maturity**: Min Level 2 → Target Level 3
**ISO 42001**: 6.2 | **ISO 27001**: —
**Profiles**: balanced, high-assurance, financial, healthcare

---

### MAP-3.2: AI Cost Documentation

**NIST AI RMF**: MAP 3.2 - Cost Analysis

**Description**: Potential costs including trustworthiness impacts are examined

**Implementation Requirements**:
- **T1**: Basic cost awareness
- **T2**: Comprehensive cost analysis; non-monetary costs included; risk tolerance connection
- **T3**: Rigorous cost quantification; total cost of ownership; trustworthiness impact monetization; public reporting

**Maturity**: Min Level 2 → Target Level 3
**ISO 42001**: 6.1 | **ISO 27001**: —
**Profiles**: balanced, high-assurance, financial, healthcare

---

### MAP-5.1: AI Impact Assessment

**NIST AI RMF**: MAP 5.1 - Impact Analysis

**Description**: Likelihood and magnitude of impacts to individuals, groups, and society are assessed

**Implementation Requirements**:
- **T1**: Basic impact awareness
- **T2**: Comprehensive impact assessment; stakeholder input; quantified where possible
- **T3**: Rigorous impact assessment; independent validation; continuous monitoring; public impact reporting

**Maturity**: Min Level 2 → Target Level 3
**ISO 42001**: 8.2, 6.1 | **ISO 27001**: A.5.31
**Profiles**: balanced, high-assurance, financial, healthcare, government

---

### MAN-1.1: AI Go/No-Go Decision

**NIST AI RMF**: MANAGE 1.1 - Proceed Determination

**Description**: Determination on whether AI system achieves intended purposes and should proceed

**Implementation Requirements**:
- **T1**: Basic go/no-go consideration
- **T2**: Formal decision process; documented criteria; governance approval
- **T3**: Comprehensive decision framework; predictive success modeling; independent validation; public decision criteria

**Maturity**: Min Level 2 → Target Level 3
**ISO 42001**: 6.1, 8.1 | **ISO 27001**: A.5.1
**Profiles**: foundational, balanced, high-assurance, financial, healthcare, government

---

### MAN-2.1: AI Alternative Evaluation

**NIST AI RMF**: MANAGE 2.1 - Alternative Analysis

**Description**: Resources and alternative approaches including non-AI alternatives are considered

**Implementation Requirements**:
- **T1**: Basic alternatives considered
- **T2**: Systematic alternative analysis; cost-benefit comparison; documented rationale
- **T3**: Comprehensive options analysis; AI-powered alternative evaluation; optimization modeling; public methodology

**Maturity**: Min Level 2 → Target Level 3
**ISO 42001**: 6.1 | **ISO 27001**: —
**Profiles**: balanced, high-assurance, financial, healthcare

---

## Risk Management & Response

*3 controls for risk prioritization, response planning, and residual risk*

### MAN-1.2: AI Risk Prioritization

**NIST AI RMF**: MANAGE 1.2 - Treatment Prioritization

**Description**: Risk treatments are prioritized based on impact, likelihood, and resources

**Implementation Requirements**:
- **T1**: Basic prioritization
- **T2**: Comprehensive prioritization framework; quantified where possible; resource allocation
- **T3**: Advanced prioritization science; AI-powered prioritization; automated resource optimization; continuous reprioritization

**Maturity**: Min Level 2 → Target Level 3
**ISO 42001**: 6.1 | **ISO 27001**: A.5.1
**Profiles**: foundational, balanced, high-assurance, financial, healthcare, government

---

### MAN-1.3: AI Risk Response Planning

**NIST AI RMF**: MANAGE 1.3 - Response Development

**Description**: Responses are developed for high priority AI risks

**Implementation Requirements**:
- **T1**: Basic responses for major risks
- **T2**: Comprehensive response plans; all options evaluated; response owners assigned
- **T3**: Advanced response optimization; predictive response effectiveness; automated response generation; continuous improvement

**Maturity**: Min Level 2 → Target Level 3
**ISO 42001**: 6.1, 8.1 | **ISO 27001**: A.5.1
**Profiles**: balanced, high-assurance, financial, healthcare, government

---

### MAN-1.4: AI Residual Risk Documentation

**NIST AI RMF**: MANAGE 1.4 - Residual Documentation

**Description**: Negative residual risks are documented for downstream stakeholders

**Implementation Requirements**:
- **T1**: Basic residual risk awareness
- **T2**: Comprehensive residual risk documentation; impact on stakeholders documented; acceptance documented
- **T3**: Predictive residual risk modeling; automated documentation; public residual risk transparency; continuous tracking

**Maturity**: Min Level 2 → Target Level 3
**ISO 42001**: 6.1 | **ISO 27001**: A.5.1
**Profiles**: balanced, high-assurance, financial, healthcare, government

---

## Document Information

**Total Controls**: 73
**Domain Distribution**:
- Governance & Accountability: 19 controls (26%)
- Data Management & Privacy: 6 controls (8%)
- Technical Operations & MLOps: 31 controls (42%)
- Organizational Culture & Capabilities: 17 controls (23%)

**NIST AI RMF Coverage**:
- GOVERN: 19 controls
- MAP: 19 controls
- MEASURE: 22 controls
- MANAGE: 13 controls

**Implementation Tiers**:
- All controls have T1, T2, and T3 requirements
- Tier selection based on AI system risk and impact

**Profile System**:
- Foundational: ~35 controls (48%)
- Balanced: ~50 controls (68%)
- High-Assurance: 73 controls (100%)
- Industry profiles: 55-60 controls (75-82%)

---

For CSV version with all metadata: [AIMF-CONTROL-CATALOG.csv](AIMF-CONTROL-CATALOG.csv)

For domain taxonomy reference: [AIMF-DOMAIN-TAXONOMY.md](AIMF-DOMAIN-TAXONOMY.md)

---

**AI Management Framework (AIMF) by PraeSyn**
Making AI Governance Practical, Accessible, and Effective.
