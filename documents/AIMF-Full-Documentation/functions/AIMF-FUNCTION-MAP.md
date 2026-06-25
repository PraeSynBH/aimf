# AI Management Framework (AIMF) by PraeSyn
## MAP Function

**© 2026 PraeSyn, LLC. All rights reserved.**
Licensed under CC BY-NC-ND 4.0

**Version**: 1.0
**Publication Date**: January 29, 2026
**Status**: Pre-Publication (Working Draft)
**Function Identifier**: MAP
**Controls**: MAP-1.1 through MAP-5.2 (19 controls)

---

## Function Overview

The **MAP** function establishes context to frame risks related to AI systems. It is the foundation for risk identification and assessment activities that feed into MEASURE and MANAGE functions.

### Purpose

The MAP function ensures organizations understand:

- The intended purposes and beneficial uses of AI systems
- The laws, norms, and deployment settings relevant to AI systems
- The business value and strategic alignment of AI initiatives
- The capabilities, limitations, and risks of AI systems
- The potential impacts on individuals, groups, and society

### Standards Alignment

| Standard | Alignment |
|----------|-----------|
| **ISO 42001** | Clauses 4.1 (Context), 4.2 (Interested Parties), 6 (Planning), 8.2 (Impact Assessment) |
| **NIST AI RMF** | MAP 1.1-1.6, 2.1-2.3, 3.1-3.5, 4.1-4.2, 5.1-5.2 |

---

## Category Structure

### MAP 1: Context Establishment

Understanding the context in which AI systems are developed and deployed.

| Control | Name | Description |
|---------|------|-------------|
| MAP-1.1 | Purpose Characterization | Intended purposes, beneficial uses, laws/norms, deployment settings documented |
| MAP-1.2 | Team Diversity | Interdisciplinary AI actors with diverse competencies involved |
| MAP-1.3 | Strategic Alignment | Organization's mission and goals for AI technology documented |
| MAP-1.4 | Business Value | Business value or context of business use clearly defined |
| MAP-1.5 | Risk Tolerance | Organizational risk tolerances determined and documented |
| MAP-1.6 | Requirements | System requirements including socio-technical implications elicited |

### MAP 2: System Categorization

Categorizing AI systems by their characteristics and requirements.

| Control | Name | Description |
|---------|------|-------------|
| MAP-2.1 | Task Classification | Specific tasks and methods of AI systems defined and categorized |
| MAP-2.2 | Knowledge Limits | Knowledge limits and human oversight requirements documented |
| MAP-2.3 | Scientific Integrity | Scientific integrity and TEVV considerations documented |

### MAP 3: Capabilities Assessment

Assessing AI system capabilities, benefits, and costs.

| Control | Name | Description |
|---------|------|-------------|
| MAP-3.1 | Benefits Analysis | Potential benefits examined and documented |
| MAP-3.2 | Cost Analysis | Potential costs including trustworthiness impacts examined |
| MAP-3.3 | Scope Definition | Targeted application scope specified and documented |
| MAP-3.4 | Operator Proficiency | Operator/practitioner proficiency requirements documented |
| MAP-3.5 | Human Oversight | Human oversight processes documented and aligned with policies |

### MAP 4: Third-Party Risk

Identifying risks from third-party AI components and services.

| Control | Name | Description |
|---------|------|-------------|
| MAP-4.1 | Risk Mapping | Approaches for mapping AI technology and legal risks from third parties |
| MAP-4.2 | Internal Controls | Internal risk controls for third-party AI components identified |

### MAP 5: Impact Assessment

Assessing impacts to individuals, groups, communities, and society.

| Control | Name | Description |
|---------|------|-------------|
| MAP-5.1 | Impact Analysis | Likelihood and magnitude of impacts assessed |
| MAP-5.2 | Stakeholder Engagement | Practices for engaging relevant AI actors to understand impacts |

---

## Control Details

### MAP-1.1: AI System Purpose Characterization

**Purpose**: Ensure comprehensive documentation of AI system purposes, uses, legal context, and deployment settings.

**Control Objective**: All AI systems have documented intended purposes, beneficial uses, applicable laws/norms, and deployment context.

#### Implementation by Tier

**Baseline 1 (Initial)**:
- Basic purpose documentation for major AI systems
- General awareness of applicable laws
- High-level deployment context description

**Baseline 2 (Mature)**:
- Comprehensive documentation for all AI systems
- Legal/regulatory review completed
- Stakeholder input incorporated
- User types and expectations documented
- TEVV metrics defined

**Baseline 3 (High-Risk)**:
- Exhaustive documentation meeting regulatory standards
- Independent review of documentation
- Continuous validation and updates
- Public transparency on purposes (where appropriate)
- Research-grade documentation methodology

#### Evidence Examples

- AI system purpose documentation
- Legal/regulatory applicability analysis
- Deployment context documentation
- User analysis documentation
- TEVV planning documentation

---

### MAP-1.5: AI Risk Tolerance Definition

**Purpose**: Establish clear organizational risk tolerance levels for AI systems.

**Control Objective**: Risk tolerance and appetite for AI systems are formally defined, documented, and approved by appropriate governance bodies.

#### Implementation by Tier

**Baseline 1 (Initial)**:
- Basic risk awareness
- Informal tolerance expectations
- Risk discussions occur when issues arise

**Baseline 2 (Mature)**:
- Formal risk tolerance statements
- Quantified where possible
- Governance approval obtained
- Risk tolerance communicated to AI teams
- Regular review and updates

**Baseline 3 (High-Risk)**:
- Comprehensive risk appetite framework
- Quantified tolerances for all risk categories
- Real-time monitoring against tolerances
- Board approval required
- Public transparency on risk tolerance approach

#### Evidence Examples

- Risk tolerance/appetite statements
- Governance approval records
- Risk tolerance communication materials
- Monitoring reports showing tolerance adherence
- Board meeting minutes (for B3)

---

### MAP-2.2: AI System Boundaries

**Purpose**: Document AI system knowledge limits and human oversight requirements.

**Control Objective**: All AI systems have documented knowledge boundaries with defined human oversight mechanisms.

#### Implementation by Tier

**Baseline 1 (Initial)**:
- Basic awareness of system limitations
- General human oversight expectations
- High-level boundary description

**Baseline 2 (Mature)**:
- Comprehensive documentation of system limits
- Human oversight systematically planned
- Decision support context provided
- Clear escalation for edge cases
- Regular boundary review

**Baseline 3 (High-Risk)**:
- Exhaustive boundary documentation
- Automated limit detection mechanisms
- Real-time human oversight capabilities
- Independent validation of boundaries
- Continuous boundary monitoring

#### Evidence Examples

- System limitation documentation
- Human oversight procedures
- Escalation procedures
- Boundary testing results
- Oversight effectiveness reports

---

### MAP-3.2: AI Cost Documentation

**Purpose**: Ensure comprehensive examination of AI system costs including trustworthiness impacts.

**Control Objective**: All costs associated with AI systems, including non-monetary trustworthiness impacts, are documented and connected to risk tolerance.

#### Implementation by Tier

**Baseline 1 (Initial)**:
- Basic cost awareness
- Financial costs tracked
- General awareness of non-monetary impacts

**Baseline 2 (Mature)**:
- Comprehensive cost analysis
- Non-monetary costs included (reputational, trust, ethical)
- Connection to organizational risk tolerance
- Cost-benefit analysis performed
- Regular cost review

**Baseline 3 (High-Risk)**:
- Rigorous cost quantification
- Total cost of ownership calculated
- Trustworthiness impact monetization where possible
- Public reporting on cost considerations
- Continuous cost monitoring and optimization

#### Evidence Examples

- Cost analysis documentation
- Cost-benefit analysis reports
- Trustworthiness impact assessments
- Risk tolerance connection documentation
- Cost monitoring reports

---

### MAP-4.1: Third-Party AI Risk Assessment

**Purpose**: Establish approaches for identifying and mapping risks from third-party AI components and services.

**Control Objective**: Systematic approaches exist for assessing AI technology and legal risks from third-party sources.

#### Implementation by Tier

**Baseline 1 (Initial)**:
- Basic third-party risk awareness
- Key third-party dependencies identified
- General risk considerations documented

**Baseline 2 (Mature)**:
- Systematic third-party risk mapping
- Legal risk assessment included
- Documented assessment approaches
- Regular third-party review
- IP risk consideration

**Baseline 3 (High-Risk)**:
- Comprehensive third-party risk program
- Continuous monitoring capabilities
- Independent assessment engagement
- Supply chain visibility
- Real-time risk monitoring

#### Evidence Examples

- Third-party risk assessment methodology
- Third-party inventory with risk ratings
- Legal risk assessments
- Supply chain documentation
- Independent assessment reports (for B3)

---

### MAP-5.1: AI Impact Assessment

**Purpose**: Assess the likelihood and magnitude of impacts from AI systems on individuals, groups, and society.

**Control Objective**: Comprehensive impact assessments are performed for all AI systems, considering both beneficial and harmful impacts.

#### Implementation by Tier

**Baseline 1 (Initial)**:
- Basic impact awareness
- Major impacts considered
- Qualitative impact assessment

**Baseline 2 (Mature)**:
- Comprehensive impact assessment
- Stakeholder input incorporated
- Quantified where possible
- Past uses and incidents reviewed
- External feedback considered

**Baseline 3 (High-Risk)**:
- Rigorous impact assessment methodology
- Independent validation
- Continuous impact monitoring
- Public impact reporting
- Research-grade methodology

#### Evidence Examples

- Impact assessment documentation
- Stakeholder input records
- Quantitative impact analysis
- Incident review documentation
- Public impact reports (for B3)

---

## Implementation Guidance

### Getting Started with MAP

1. **Inventory AI Systems**: Create comprehensive list of all AI systems
2. **Document Purposes**: Establish basic purpose documentation for each system
3. **Identify Stakeholders**: Determine who is affected by each AI system
4. **Assess Risks**: Conduct initial risk assessment for high-priority systems
5. **Establish Context**: Document deployment context and applicable regulations

### Context Establishment Process

```
Step 1: Define Scope
├── Identify AI system boundaries
├── Determine applicable regulations
└── Document deployment settings

Step 2: Gather Input
├── Engage stakeholders
├── Review similar systems/incidents
└── Consult domain experts

Step 3: Document Context
├── Purpose and beneficial uses
├── User types and expectations
├── Known limitations and risks
└── TEVV approach

Step 4: Validate and Approve
├── Review with governance
├── Obtain required approvals
└── Establish review cycle
```

### Integration with Other Functions

The MAP function provides context for:

- **GOVERN**: Risk tolerance and strategic alignment inform governance policies
- **MEASURE**: Identified risks determine what to measure; context guides interpretation
- **MANAGE**: Impact assessment and risk mapping inform risk response prioritization

---

## Assessment Criteria

### Scoring Methodology

Each MAP control is assessed on a 0-3 scale:

| Score | Level | Description |
|-------|-------|-------------|
| 0 | Not Present | No capability exists |
| 1 | Ad-Hoc | Informal, inconsistent implementation |
| 2 | Developing | Documented but not consistently applied |
| 3 | Established | Documented, consistent, organization-wide |

### Key Assessment Questions

**MAP-1.1**: Can you provide documentation of AI system purposes for all deployed systems?

**MAP-1.5**: Are risk tolerances formally defined and approved for AI systems?

**MAP-2.2**: Are system limitations and human oversight requirements documented?

**MAP-5.1**: Are impact assessments performed and documented for AI systems?

---

## References

- ISO/IEC 42001:2023 Clauses 4, 6, 8.2
- NIST AI RMF 1.0 MAP function
- IEEE 7010-2020 Recommended Practice for AI Well-being Impact Assessment

---

**Next Document**: [MEASURE Function Controls](AIMF-FUNCTION-MEASURE.md) | [GOVERN Function Controls](AIMF-FUNCTION-GOVERN.md)
