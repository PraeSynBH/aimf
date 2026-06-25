# AI Management Framework (AIMF) by PraeSyn
## MANAGE Function

**© 2026 PraeSyn, LLC. All rights reserved.**
Licensed under CC BY-NC-ND 4.0

**Version**: 1.0
**Publication Date**: January 29, 2026
**Status**: Pre-Publication (Working Draft)
**Function Identifier**: MANAGE
**Controls**: MAN-1.1 through MAN-4.3 (13 controls)

---

## Function Overview

The **MANAGE** function allocates risk resources to mapped and measured risks on a regular basis. It translates risk understanding into action through prioritization, response planning, and continuous risk treatment.

### Purpose

The MANAGE function ensures organizations can:

- Prioritize and respond to identified AI risks
- Maximize benefits while minimizing negative impacts
- Manage risks from third-party AI components and services
- Implement risk treatments with response, recovery, and communication plans

### Standards Alignment

| Standard | Alignment |
|----------|-----------|
| **ISO 42001** | Clauses 6.1 (Risk Actions), 8 (Operation), 10 (Improvement) |
| **NIST AI RMF** | MANAGE 1.1-1.4, 2.1-2.4, 3.1-3.2, 4.1-4.3 |

---

## Category Structure

### MANAGE 1: Risk Response

AI risks are prioritized, responded to, and managed.

| Control | Name | Description |
|---------|------|-------------|
| MAN-1.1 | Go/No-Go Decision | Determination on whether AI system achieves intended purposes |
| MAN-1.2 | Risk Prioritization | Risk treatments prioritized based on impact, likelihood, resources |
| MAN-1.3 | Response Development | Responses developed for high priority AI risks |
| MAN-1.4 | Residual Documentation | Negative residual risks documented for stakeholders |

### MANAGE 2: Benefit Optimization

Strategies to maximize benefits and minimize negative impacts.

| Control | Name | Description |
|---------|------|-------------|
| MAN-2.1 | Alternative Analysis | Resources and alternative approaches including non-AI considered |
| MAN-2.2 | Value Sustainment | Mechanisms to sustain AI system value over time |
| MAN-2.3 | Unknown Risk Response | Procedures for responding to emergent risks |
| MAN-2.4 | System Control | Mechanisms to supersede, disengage, or deactivate AI systems |

### MANAGE 3: Third-Party Management

AI risks and benefits from third-party entities managed.

| Control | Name | Description |
|---------|------|-------------|
| MAN-3.1 | Third-Party Monitoring | Third-party AI risks regularly monitored and controlled |
| MAN-3.2 | Model Monitoring | Pre-trained models monitored as part of system maintenance |

### MANAGE 4: Treatment Plans

Risk treatments, response, recovery, and communication plans.

| Control | Name | Description |
|---------|------|-------------|
| MAN-4.1 | Post-Deployment | Post-deployment monitoring, appeal, decommissioning, incident response |
| MAN-4.2 | Continuous Improvement | Measurable improvements integrated into AI system updates |
| MAN-4.3 | Incident Communication | Incidents and errors communicated to stakeholders and tracked |

---

## Control Details

### MAN-1.1: AI Go/No-Go Decision

**Purpose**: Ensure formal determination of whether AI systems achieve intended purposes before deployment.

**Control Objective**: All AI systems undergo formal go/no-go evaluation with documented criteria and governance approval.

#### Implementation by Tier

**Baseline 1 (Initial)**:
- Basic go/no-go consideration for major systems
- General assessment of whether objectives are met
- Informal decision process

**Baseline 2 (Mature)**:
- Formal decision process for all AI systems
- Documented criteria for proceeding
- Governance approval required
- Decision rationale documented
- Regular review of decision effectiveness

**Baseline 3 (High-Risk)**:
- Comprehensive decision framework with predictive success modeling
- Independent validation of go/no-go decisions
- Public decision criteria (where appropriate)
- Continuous decision quality monitoring
- Board-level decisions for critical systems

#### Evidence Examples

- Go/no-go decision criteria documentation
- Decision records with rationale
- Governance approval records
- Decision effectiveness review reports
- Predictive model documentation (for B3)

---

### MAN-1.2: AI Risk Prioritization

**Purpose**: Ensure systematic prioritization of risk treatments based on impact, likelihood, and available resources.

**Control Objective**: All identified AI risks are prioritized using a consistent framework that considers impact, likelihood, and resource constraints.

#### Implementation by Tier

**Baseline 1 (Initial)**:
- Basic prioritization of major risks
- Qualitative consideration of impact and likelihood
- General resource awareness

**Baseline 2 (Mature)**:
- Comprehensive prioritization framework
- Quantified risk analysis where possible
- Resource allocation tied to risk priority
- Regular review and reprioritization
- Treatment method evaluation

**Baseline 3 (High-Risk)**:
- Advanced prioritization with AI-powered optimization
- Automated resource allocation optimization
- Predictive risk treatment effectiveness modeling
- Continuous reprioritization based on real-time data
- ROI analysis for risk treatments

#### Evidence Examples

- Risk prioritization methodology
- Risk register with priority rankings
- Resource allocation documentation
- Treatment effectiveness analysis
- ROI calculations (for B3)

---

### MAN-2.4: AI System Control Mechanisms

**Purpose**: Ensure mechanisms exist to supersede, disengage, or deactivate AI systems when necessary.

**Control Objective**: All AI systems have tested mechanisms for safe disengagement, deactivation, or replacement.

#### Implementation by Tier

**Baseline 1 (Initial)**:
- Basic awareness of shutdown procedures
- General deactivation capability
- Manual intervention possible

**Baseline 2 (Mature)**:
- Comprehensive control mechanisms for all systems
- Documented and tested procedures
- Clear responsibilities assigned
- Failover and rollback procedures defined
- Performance inconsistencies addressed systematically

**Baseline 3 (High-Risk)**:
- Advanced failsafe systems with automated response
- Predictive performance inconsistency detection
- Self-healing capabilities where appropriate
- Real-time system health monitoring
- Independent validation of control mechanisms

#### Evidence Examples

- Deactivation procedure documentation
- Failover/rollback procedures
- Responsibility assignments
- Control mechanism testing results
- System health monitoring dashboards (for B3)

---

### MAN-4.1: AI Post-Deployment Monitoring

**Purpose**: Ensure comprehensive post-deployment management including monitoring, appeals, decommissioning, and incident response.

**Control Objective**: All deployed AI systems have comprehensive post-deployment plans covering monitoring, user appeals, planned decommissioning, and incident response.

#### Implementation by Tier

**Baseline 1 (Initial)**:
- Basic post-deployment monitoring
- General awareness of incident response needs
- Basic user feedback channels

**Baseline 2 (Mature)**:
- Comprehensive monitoring plans for all systems
- User input systematically captured and evaluated
- Appeal and override mechanisms established
- Decommissioning comprehensively planned
- Incident response procedures defined and tested
- Recovery procedures documented
- Change management established

**Baseline 3 (High-Risk)**:
- Advanced post-deployment management with AI-powered capabilities
- Automated incident response where appropriate
- Predictive decommissioning planning
- Real-time user input analysis
- Continuous optimization of post-deployment processes
- Public transparency on post-deployment practices

#### Evidence Examples

- Post-deployment monitoring plans
- User appeal process documentation
- Decommissioning plans
- Incident response procedures
- Recovery procedure documentation
- Testing/exercise results
- Post-deployment effectiveness reports

---

### MAN-4.3: AI Incident and Error Communication

**Purpose**: Ensure incidents and errors are systematically communicated to stakeholders with appropriate tracking.

**Control Objective**: All AI incidents and errors are tracked, communicated to relevant stakeholders, and lessons learned are captured.

#### Implementation by Tier

**Baseline 1 (Initial)**:
- Basic incident reporting capability
- Major incidents communicated
- Basic tracking of significant issues

**Baseline 2 (Mature)**:
- Comprehensive incident program
- Systematic communication to all affected parties
- Full incident tracking system
- Root cause analysis performed
- Lessons learned captured and applied

**Baseline 3 (High-Risk)**:
- Advanced incident management with AI-powered detection
- Automated communication to stakeholders
- Predictive incident occurrence modeling
- Public incident transparency
- Research contribution to incident management
- Automated lessons learned integration

#### Evidence Examples

- Incident management procedures
- Incident tracking system/logs
- Communication records
- Root cause analysis reports
- Lessons learned documentation
- Public incident reports (for B3)

---

## Risk Response Options

The MANAGE function supports four primary risk response strategies:

| Strategy | Description | When to Use |
|----------|-------------|-------------|
| **Mitigate** | Implement controls to reduce risk | When risk can be reduced to acceptable level |
| **Transfer** | Shift risk to another party | When third party can better manage risk |
| **Avoid** | Eliminate the risk by not proceeding | When risk exceeds tolerance and cannot be reduced |
| **Accept** | Acknowledge and document residual risk | When risk is within tolerance or cost/benefit favors acceptance |

### Response Selection Framework

```
Risk Assessment
├── Above Tolerance?
│   ├── Can Risk Be Reduced? → Mitigate
│   ├── Can Risk Be Transferred? → Transfer
│   └── Neither Viable? → Avoid
└── Within Tolerance?
    ├── Cost-Effective to Reduce? → Mitigate
    └── No Further Action Needed → Accept (Document)
```

---

## Implementation Guidance

### Risk Management Process

```
Step 1: Prioritize Risks
├── Assess impact and likelihood
├── Consider resource constraints
├── Apply prioritization framework
└── Document prioritization rationale

Step 2: Select Response Strategy
├── Evaluate mitigation options
├── Consider transfer possibilities
├── Assess avoidance implications
├── Document acceptance decisions
└── Assign response owners

Step 3: Implement Treatments
├── Develop treatment plans
├── Allocate resources
├── Execute treatments
└── Monitor implementation

Step 4: Monitor and Review
├── Track treatment effectiveness
├── Monitor residual risks
├── Identify emergent risks
└── Update risk register

Step 5: Communicate
├── Report to governance
├── Inform stakeholders
├── Document lessons learned
└── Update procedures
```

### Incident Response Framework

```
Detection
├── Automated monitoring alerts
├── User reports
└── External notification

Assessment
├── Severity classification
├── Impact analysis
└── Stakeholder identification

Response
├── Immediate containment
├── Investigation
└── Resolution

Recovery
├── Service restoration
├── Validation testing
└── Stakeholder communication

Review
├── Root cause analysis
├── Lessons learned
├── Process improvement
└── Documentation update
```

---

## Integration with Other Functions

### From MAP

MAP function provides:
- Identified risks requiring management
- Impact assessment for prioritization
- Stakeholder identification for communication
- Context for response selection

### From MEASURE

MEASURE function provides:
- Quantified risk data for prioritization
- Performance trends for decision-making
- Effectiveness data for response optimization
- Compliance evidence for governance

### To GOVERN

MANAGE function provides:
- Risk management effectiveness data
- Incident reports for governance review
- Continuous improvement recommendations
- Resource requirement insights

---

## Continuous Improvement Cycle

```
┌─────────────────────────────────────────────────┐
│                                                 │
│  Plan → Do → Check → Act → Plan → ...          │
│                                                 │
│  Plan: Identify improvements from:             │
│        - Incident analysis                     │
│        - Performance data                      │
│        - Stakeholder feedback                  │
│        - Best practice review                  │
│                                                 │
│  Do:   Implement improvements:                 │
│        - Update procedures                     │
│        - Enhance controls                      │
│        - Upgrade capabilities                  │
│        - Train personnel                       │
│                                                 │
│  Check: Evaluate effectiveness:                │
│         - Measure outcomes                     │
│         - Compare to targets                   │
│         - Assess stakeholder satisfaction      │
│         - Review incidents                     │
│                                                 │
│  Act:  Take action based on results:           │
│        - Standardize successful improvements   │
│        - Address gaps                          │
│        - Update plans                          │
│        - Share best practices                  │
│                                                 │
└─────────────────────────────────────────────────┘
```

---

## Assessment Criteria

### Scoring Methodology

Each MANAGE control is assessed on a 0-3 scale:

| Score | Level | Description |
|-------|-------|-------------|
| 0 | Not Present | No risk management capability exists |
| 1 | Ad-Hoc | Reactive, inconsistent risk management |
| 2 | Developing | Documented but inconsistently applied |
| 3 | Established | Systematic, organization-wide risk management |

### Key Assessment Questions

**MAN-1.1**: Is there a formal go/no-go decision process for AI systems?

**MAN-1.2**: Are risks systematically prioritized using a defined framework?

**MAN-2.4**: Are there tested mechanisms to deactivate AI systems if needed?

**MAN-4.1**: Are post-deployment monitoring and incident response plans in place?

---

## References

- ISO/IEC 42001:2023 Clauses 6.1, 8, 10
- NIST AI RMF 1.0 MANAGE function
- ISO 31000:2018 Risk Management Guidelines
- ITIL 4 Incident Management

---

**Related Documents**: [GOVERN Function Controls](AIMF-FUNCTION-GOVERN.md) | [MEASURE Function Controls](AIMF-FUNCTION-MEASURE.md) | [Framework Overview](AIMF-FRAMEWORK-OVERVIEW.md)
