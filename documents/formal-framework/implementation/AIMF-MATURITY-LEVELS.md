# AI Management Framework (AIMF) by PraeSyn
## Maturity Levels - Implementation Quality Assessment

**© 2026 PraeSyn, LLC. All rights reserved.**
Licensed under CC BY-NC-ND 4.0

**Version**: 1.0
**Publication Date**: January 29, 2026
**Document Type**: Maturity Assessment Guide
**Status**: Pre-Publication (Working Draft)

---

## Overview

Maturity levels measure the **quality of control implementation** using a five-level CMMI-based scale. These levels apply consistently across all AIMF controls, regardless of baseline or profile selection.

### Key Principle

**Maturity levels answer**: *"How well is this control implemented?"*

This is distinct from and orthogonal to:
- **Baseline**: Which controls apply (based on AI system risk)
- **Profile**: Which controls are selected (based on organizational context)

A control can be in scope (baseline/profile) but poorly implemented (low maturity), or excellently implemented (high maturity).

---

## The Five Maturity Levels

### Scoring Scale

| Level | Name | Score | Description |
|-------|------|-------|-------------|
| **ML1** | Initial | 0 points | Ad-hoc, individual-dependent; no documentation |
| **ML2** | Developing | 1 point | Documented but inconsistent implementation |
| **ML3** | Defined | 2 points | Standardized, organization-wide; consistently applied |
| **ML4** | Managed | 3 points | Quantitatively measured and controlled |
| **ML5** | Optimizing | 4 points | Continuous improvement and innovation |

**Note**: ML1 scores as 0 to incentivize moving beyond ad-hoc processes. The scale is 0-4, with a maximum of 4 points per control.

---

## Maturity Level Definitions

### ML1: Initial (0 points)

**Definition**: Capability exists but is ad-hoc, undocumented, and dependent on individual knowledge or initiative. Success depends on specific people rather than organizational processes.

**Characteristics**:
- ✗ No written procedures or documentation
- ✗ No assigned ownership or accountability
- ✗ No training or guidance materials
- ✗ Inconsistent—varies by person, team, or time
- ✗ Success depends on heroic individual effort
- ✗ Knowledge exists only in people's heads
- ✗ No evidence trail or audit capability

**Evidence Indicators**:
- Someone can describe how something is done, but it's not written down
- "We do this, but it's not formal"
- "It depends on who's working on it"
- "We've been meaning to document this"
- Documentation search yields nothing
- No artifacts from last 90 days

**Common ML1 States**:
- Policy exists as an idea but isn't written
- Risk assessment done verbally but not documented
- Testing happens but no test plans or results documented
- Someone monitors production but no formal process
- Training happens informally ("we tell new people about it")

**When to Score ML1**:
- Capability demonstrably exists (people are doing it)
- But cannot produce documentation within 10 minutes
- Process knowledge resides with individuals, not organization

**When NOT to Score ML1**:
- If the capability doesn't exist at all → Score 0 (same as ML1 on our scale)
- If documentation exists but is incomplete → Consider ML2

---

### ML2: Developing (1 point)

**Definition**: Capability is documented and recognized, but implementation is inconsistent across the organization. Processes exist on paper but aren't reliably followed.

**Characteristics**:
- ✓ Written documentation exists (policies, procedures, templates)
- ✓ Ownership assigned (someone is responsible)
- ✓ Organizational awareness (people know it exists)
- ~ Inconsistent application (some teams follow, others don't)
- ~ Variable quality (depends on team or project)
- ~ Incomplete implementation (documented but gaps in practice)
- ✗ No systematic measurement of effectiveness
- ✗ Limited enforcement or accountability

**Evidence Indicators**:
- Policy document dated within last 24 months
- Procedure exists but "we don't always follow it"
- Template created but optional usage
- Training materials exist but completion is voluntary
- Examples of compliance exist, but also examples of non-compliance
- Documentation gaps (some systems documented, others not)

**Common ML2 States**:
- AI governance policy approved but not consistently applied
- Risk assessment template exists, used for some projects but not all
- Testing procedures documented but adherence varies by team
- Monitoring dashboards created but not actively watched
- Training available but completion rates < 80%

**When to Score ML2**:
- Documentation exists and is accessible
- At least some evidence of implementation
- But clear inconsistency across organization
- Recent adoption (< 6 months) should typically score ML2 until proven sustainable

**When NOT to Score ML2**:
- If no documentation exists → ML1
- If documentation is consistently followed → ML3

---

### ML3: Defined (2 points)

**Definition**: Capability is standardized and consistently applied organization-wide. Everyone follows the same process, training is mandatory, and implementation is the norm.

**Characteristics**:
- ✓ Comprehensive written procedures and policies
- ✓ Clear ownership and accountability
- ✓ Mandatory compliance (not optional)
- ✓ Consistent implementation across all teams/projects
- ✓ Training is required and completion tracked
- ✓ Regular usage with documented evidence
- ✓ Audit capability (can show compliance)
- ~ Some measurement exists but may not be comprehensive
- ✗ Not yet data-driven or quantitatively managed

**Evidence Indicators**:
- Policy/procedure current (reviewed within 12 months)
- Compliance rate > 90% (all teams, all projects)
- Training completion > 95% for required personnel
- Regular artifact generation (assessments, reports, reviews)
- Process enforced through gates or approvals
- Exceptions are rare and documented
- Can demonstrate consistent practice across 6+ months

**Common ML3 States**:
- AI governance policy consistently applied to all new AI projects
- Risk assessment mandatory for all AI systems, documented in registry
- Testing checklist required for deployment, evidence in project records
- Production monitoring standard for all deployed systems
- Onboarding includes AI governance training, 100% completion

**When to Score ML3**:
- Process is "the way we do things" organization-wide
- New employees/teams automatically follow the process
- Can demonstrate sustained consistent application (6+ months)
- Audit would find compliance across random sampling

**When NOT to Score ML3**:
- If inconsistent application → ML2
- If not yet sustained (< 6 months) → ML2
- If no measurement exists but everything else present → Still ML3 (measurement is ML4)

---

### ML4: Managed (3 points)

**Definition**: Capability is quantitatively measured, controlled, and managed using data. Decisions about the capability are data-driven, and performance is predictable.

**Characteristics**:
- ✓ All ML3 characteristics present
- ✓ Quantitative metrics defined and collected
- ✓ Performance targets established
- ✓ Regular measurement and reporting
- ✓ Data-driven improvement decisions
- ✓ Predictable outcomes (process capability understood)
- ✓ Metrics reviewed by leadership
- ✗ Improvement is reactive or periodic, not continuous

**Evidence Indicators**:
- KPIs/metrics dashboards exist and are current
- Metrics reviewed in regular management meetings
- Trend data available (6+ months of measurements)
- Performance against targets documented
- Decisions reference metric data ("we changed X because metric Y showed...")
- Statistical process control or similar rigor
- Variance analysis when targets missed

**Common ML4 States**:
- AI governance: Metrics on policy compliance, time-to-approval, coverage tracked monthly
- Risk assessment: Mean time to assessment, risk score distributions, high-risk system count tracked
- Testing: Test coverage metrics, defect rates, bias test results tracked and trended
- Monitoring: SLA metrics, alert response times, incident counts tracked with statistical analysis
- Training: Completion rates, competency scores, time-to-proficiency measured

**When to Score ML4**:
- Quantitative data exists for control effectiveness
- Data is actively used for management decisions
- Can show trends over 6+ months
- Leadership reviews performance data regularly

**When NOT to Score ML4**:
- If metrics exist but aren't used → ML3 (compliance without management)
- If measurement is ad-hoc or sporadic → ML3
- If no targets or comparison baseline → ML3

---

### ML5: Optimizing (4 points)

**Definition**: Capability is continuously improved through innovation, automation, and industry leadership. The organization is actively optimizing and contributing to field advancement.

**Characteristics**:
- ✓ All ML4 characteristics present
- ✓ Continuous improvement process in place
- ✓ Innovation in methods and tools
- ✓ Automation of routine activities
- ✓ Predictive capabilities (proactive, not reactive)
- ✓ Industry contribution (standards, research, thought leadership)
- ✓ Peer recognition or external validation
- ✓ Demonstrable improvement over time

**Evidence Indicators**:
- Documented improvements over past 12 months with measurable results
- Automation of previously manual processes
- Predictive analytics or AI-powered optimization
- Published thought leadership (whitepapers, conference talks, blog posts)
- Contribution to industry standards or frameworks
- External recognition (awards, certifications, case studies)
- Regular innovation cycles (quarterly improvement initiatives)
- Research partnerships or academic collaboration

**Common ML5 States**:
- AI governance: Automated policy checking, AI-powered compliance monitoring, published best practices
- Risk assessment: Predictive risk modeling, automated risk score generation, industry-leading methodology
- Testing: Automated test generation, AI-powered bias detection, research publications on TEVV methods
- Monitoring: Self-healing systems, predictive anomaly detection, open-source monitoring tools released
- Training: Adaptive learning paths, AI-powered competency assessment, certification programs offered externally

**When to Score ML5**:
- Clear evidence of continuous improvement culture
- Innovation is systematic, not one-time
- External validation or industry recognition
- Can demonstrate trend of improvements with measurable impact

**When NOT to Score ML5**:
- If just meeting ML4 with good metrics → Still ML4
- If improvement is planned but not demonstrated → ML4
- If innovation is isolated rather than systematic → ML4

---

## Maturity Assessment Decision Tree

```
Does the control capability exist at all?
   |
   ├─→ NO → ML1 (Score: 0)
   |
   └─→ YES → Is there written documentation (policy, procedure, template)?
          |
          ├─→ NO → ML1 (Score: 0)
          |
          └─→ YES → Is it consistently applied organization-wide?
                 |
                 ├─→ NO → ML2 (Score: 1) [Documented but inconsistent]
                 |
                 └─→ YES → Are there quantitative metrics measuring effectiveness?
                        |
                        ├─→ NO → ML3 (Score: 2) [Standardized]
                        |
                        └─→ YES → Is there systematic continuous improvement?
                               |
                               ├─→ NO → ML4 (Score: 3) [Measured]
                               |
                               └─→ YES → ML5 (Score: 4) [Optimizing]
```

---

## Evidence Requirements by Maturity Level

### What Evidence Proves Each Level?

| Maturity | Governance Control Example | Technical Control Example | Data Control Example |
|----------|---------------------------|---------------------------|---------------------|
| **ML1** | "We talk about AI risk in meetings" (no documentation) | "We test before deploying" (no test plans) | "We check data quality" (no process) |
| **ML2** | AI policy exists (6 months old, not referenced) | Test checklist created (used on 2 of 5 projects) | Data quality SOP documented (varies by team) |
| **ML3** | AI policy mandated for all projects, 95% compliance | All deployments require documented test results, 100% compliance | Data quality process in SDLC, all projects follow |
| **ML4** | Governance metrics: 98% compliance, 3.2 days average approval time, tracked monthly | Test coverage 87%, defect density 0.03/KLOC, bias metrics < threshold | Data quality score 94%, data lineage 100%, monthly quality reports |
| **ML5** | AI-powered policy compliance checking, quarterly policy innovation reviews, published best practices | Automated test generation, predictive defect detection, open-source testing framework | Self-healing data pipelines, automated quality improvement, research publications |

---

## Control-Specific Maturity Examples

### Governance Control: GOV-1.1 (Legal/Regulatory Compliance Policies)

| ML | Implementation State | Evidence |
|----|---------------------|----------|
| **ML1** | Awareness of regulations exists; informal discussion | No written policy; verbal acknowledgment only |
| **ML2** | Policy document created acknowledging key regulations | Policy exists but dated, not referenced in practice |
| **ML3** | Comprehensive policy addressing all applicable regulations; reviewed annually; mandatory compliance | Current policy (< 12 months old), legal review sign-off, referenced in project gates |
| **ML4** | Policy compliance tracked with metrics; regulatory change monitoring; effectiveness measured | Compliance dashboard, regulatory scan process, metrics in leadership reports |
| **ML5** | Automated regulatory monitoring; AI-powered compliance checking; industry thought leadership | Automated alerts for regulatory changes, compliance AI tools, published regulatory guidance |

---

### Technical Control: MEA-2.4 (AI Production Monitoring)

| ML | Implementation State | Evidence |
|----|---------------------|----------|
| **ML1** | Someone checks logs occasionally; no systematic monitoring | Manual log review; no dashboards or alerts |
| **ML2** | Monitoring dashboard created; alerting configured | Dashboard exists but not actively used; alerts not responded to consistently |
| **ML3** | Production monitoring standard for all AI systems; defined SLAs; on-call rotation | All systems monitored, alert response documented, SLAs met 95%+ |
| **ML4** | Monitoring metrics tracked; performance trends analyzed; capacity planning data-driven | MTTD/MTTR metrics, trend analysis, predictive alerting tuned using data |
| **ML5** | AI-powered anomaly detection; automated remediation; self-healing systems | ML-based anomaly detection, auto-scaling, published monitoring framework |

---

### Data Control: MEA-2.10 (AI Privacy Evaluation)

| ML | Implementation State | Evidence |
|----|---------------------|----------|
| **ML1** | Privacy considerations discussed informally | No privacy assessment documentation |
| **ML2** | Privacy impact assessment template created; used on some projects | PIA template exists, 3 of 7 projects have completed PIAs |
| **ML3** | Privacy assessment mandatory for all AI systems with PII; legal/DPO review required | 100% of applicable projects have approved PIAs; legal sign-off documented |
| **ML4** | Privacy risk scores calculated; privacy metrics tracked; effectiveness measured | Privacy risk quantified, privacy incident metrics, quarterly privacy reviews |
| **ML5** | Privacy-enhancing technologies systematically evaluated; differential privacy implemented; privacy research | Advanced PETs deployed, published privacy methodologies, external privacy audits |

---

### Culture Control: GOV-4.1 (AI Risk Culture Development)

| ML | Implementation State | Evidence |
|----|---------------------|----------|
| **ML1** | Some individuals are risk-aware; no organizational culture program | Leadership mentions risk culture in meetings; no formal program |
| **ML2** | Risk culture communications initiated; awareness campaigns launched | Risk culture materials created, some training completed, initiatives started |
| **ML3** | Risk culture embedded in onboarding; regular communications; leadership reinforcement | All employees receive risk training, quarterly communications, leadership messages |
| **ML4** | Culture surveys measure risk awareness; metrics tracked; improvement initiatives data-driven | Annual culture surveys, risk awareness scores tracked, programs adjusted based on data |
| **ML5** | Risk culture is organizational identity; external recognition; continuous culture innovation | Industry awards for risk culture, employee engagement highest quartile, published culture research |

---

## Common Assessment Pitfalls

### Pitfall 1: Aspiration Inflation

**Mistake**: Scoring based on plans, intentions, or "what we're about to do"

**Example**:
- "We're rolling out our AI policy next month" → Scored as ML3
- **Correct**: If not yet deployed → ML1 or ML2 (policy drafted)

**Mitigation**: Ask "Can you show me evidence this exists **today**?" If answer is "not yet" or "soon," score current state only.

---

### Pitfall 2: Best-Case Bias

**Mistake**: Scoring based on best team, best project, or ideal scenario

**Example**:
- "Our AI Center of Excellence team does comprehensive testing" → Scored as ML3
- But: Other teams don't follow the same standard
- **Correct**: ML2 (documented for some, not organization-wide)

**Mitigation**: Score reflects **organization-wide norm**, not best case. If capability isn't consistent across 90%+ of applicable situations, it's not ML3.

---

### Pitfall 3: Documentation ≠ Implementation

**Mistake**: Assuming that documented = done

**Example**:
- "We have a risk assessment template" → Scored as ML3
- But: Template created 2 years ago, used on 1 of 10 recent projects
- **Correct**: ML2 (documented but not consistently applied)

**Mitigation**: Documentation alone is ML2 at best. ML3 requires evidence of consistent implementation.

---

### Pitfall 4: Confusing Compliance with Measurement

**Mistake**: Scoring ML4 because "we track whether it's done" without actual performance metrics

**Example**:
- "We track which projects completed risk assessments" → Scored as ML4
- **Correct**: This is compliance tracking (ML3), not performance measurement
- **For ML4**: Need metrics like "average risk score," "time to complete assessment," "high-risk system percentage," with trend analysis

**Mitigation**: ML4 requires measuring **how well** the control performs, not just **whether** it was done.

---

### Pitfall 5: One-Time Innovation

**Mistake**: Scoring ML5 for a single innovation or improvement

**Example**:
- "We just implemented automated testing" → Scored as ML5
- **Correct**: Innovation is good but ML5 requires **continuous** improvement culture
- **For ML5**: Need evidence of systematic innovation over time (multiple improvements, regular cadence)

**Mitigation**: ML5 requires sustained pattern of innovation with external validation/recognition, not a single achievement.

---

## Maturity Progression Characteristics

### What Changes at Each Level

| Aspect | ML1 | ML2 | ML3 | ML4 | ML5 |
|--------|-----|-----|-----|-----|-----|
| **Documentation** | None | Exists but incomplete | Comprehensive, current | Includes metrics/targets | Includes innovation roadmap |
| **Consistency** | Individual-dependent | Varies by team | Organization-wide | Statistically controlled | Continuously optimizing |
| **Ownership** | Unclear or informal | Assigned | Clear RACI | Performance-managed | Strategic leadership |
| **Training** | None or ad-hoc | Available | Mandatory, tracked | Competency-based | Certification programs |
| **Evidence** | Verbal only | Some documentation | Complete documentation | Metrics and trends | Research and publications |
| **Enforcement** | None | Voluntary | Required | Measured | Continuously improved |
| **Decision-Making** | Intuition | Experience | Process-driven | Data-driven | Predictive/optimized |

---

## Maturity Assessment Best Practices

### 10-Minute Evidence Test

**For any control, ask**: "If I asked for evidence of this control right now, what could you produce in 10 minutes?"

| Response | Likely Maturity |
|----------|----------------|
| "Nothing—we don't have that written down" | ML1 |
| "A policy document or template, but not sure if it's current" | ML2 |
| "Current policy, recent examples from multiple projects, training records" | ML3 |
| "All of the above plus dashboard showing metrics and trends" | ML4 |
| "All of the above plus innovation roadmap and external publications" | ML5 |

---

### Cross-Validation Across Assessors

When multiple assessors rate the same control:

**Variance < 1 level** (e.g., one says ML2, another says ML3):
- Acceptable—discuss and reach consensus
- Usually means organization is "between" levels

**Variance ≥ 2 levels** (e.g., one says ML2, another says ML4):
- Red flag—assessors seeing different realities
- Investigate: Different teams? Different evidence? Misunderstanding criteria?
- Require evidence-based resolution

**Resolution Process**:
1. Each assessor presents evidence for their score
2. Group evaluates evidence against maturity criteria
3. Consensus score based on objective evidence
4. Note any areas of uncertainty for follow-up

---

## Maturity Level Roadmaps

### ML1 → ML2: Document and Assign

**Focus**: Create documentation and assign ownership

**Key Activities**:
- Write policies, procedures, and templates
- Assign clear ownership (RACI)
- Create awareness materials
- Initial training delivery

**Timeline**: 1-3 months per control
**Investment**: Low (documentation effort, minimal tooling)

**Success Indicator**: You can point to written documentation and an owner for each control.

---

### ML2 → ML3: Standardize and Enforce

**Focus**: Achieve organization-wide consistency

**Key Activities**:
- Make compliance mandatory (not optional)
- Integrate into project gates and approval processes
- Achieve 90%+ adoption rates
- Sustain for 6+ months
- Build enforcement mechanisms

**Timeline**: 6-12 months per control
**Investment**: Moderate (change management, training, process integration)

**Success Indicator**: New projects/teams automatically follow the standard without prompting.

---

### ML3 → ML4: Measure and Control

**Focus**: Implement quantitative management

**Key Activities**:
- Define KPIs and performance targets
- Implement measurement tooling
- Establish regular reporting
- Use data for improvement decisions
- Build predictive capability

**Timeline**: 12-18 months per control
**Investment**: Significant (analytics tooling, data infrastructure, analyst time)

**Success Indicator**: Leadership makes decisions based on metric trends, not anecdotes.

---

### ML4 → ML5: Optimize and Innovate

**Focus**: Continuous improvement and industry leadership

**Key Activities**:
- Systematic innovation process
- Automation of manual activities
- Research and development
- External contributions (standards, publications)
- Industry recognition pursuit

**Timeline**: 18-36 months per control
**Investment**: High (R&D, automation tools, external engagement)

**Success Indicator**: External validation of leadership; demonstrable competitive advantage from maturity.

---

## Relationship to Baselines and Profiles

### How Maturity Interacts with Baselines

**Baseline determines scope** (which controls):
- B1: ~35 controls
- B2: ~50 controls
- B3: 73 controls

**Maturity determines quality** (how well implemented):
- Each control assessed ML1-5 independently
- Same control can be ML1 in one organization, ML5 in another

**Example**:
```
Organization A (B2 baseline, 50 controls):
- GOV-1.1: ML3 (policy defined and applied)
- MEA-2.4: ML2 (monitoring documented but inconsistent)
- MAN-1.1: ML4 (go/no-go process measured and managed)

Organization B (B2 baseline, 50 controls):
- GOV-1.1: ML4 (policy with compliance metrics)
- MEA-2.4: ML5 (AI-powered monitoring, continuous innovation)
- MAN-1.1: ML3 (standardized decision process)
```

Both organizations have B2 baseline (same 50 controls), but different maturity levels per control.

---

### How Maturity Interacts with Profiles

**Profiles set target maturity** per control:
- Default target: ML3 (Defined)
- Profiles can customize: ML2-5 per control
- Critical controls may target ML4
- Lower-priority controls may target ML2

**Example Profile**:
```yaml
profile:
  name: "Healthcare - Moderate Risk AI"
  baseline: B2
  controls:
    - id: GOV-1.1
      target_maturity: 3  # Standard target
    - id: MEA-2.6  # Safety Assessment
      target_maturity: 4  # Critical for patient safety
    - id: GOV-1.5  # Environmental Impact
      target_maturity: 2  # Lower priority for healthcare
```

**Scoring**:
```
Profile Target Score = (35 controls × 2) + (1 control × 3) + (1 control × 1) = 74 points
Profile Max Score = 37 controls × 4 = 148 points
```

---

## Maturity Assessment Frequency

| Maturity Level | Recommended Reassessment |
|----------------|-------------------------|
| **ML1** | Every 3-6 months (rapid improvement expected) |
| **ML2** | Every 6 months (actively building consistency) |
| **ML3** | Annually (stable, monitoring for drift) |
| **ML4** | Annually (metrics provide continuous visibility) |
| **ML5** | Annually (innovation tracking, not compliance checking) |

**Triggers for Immediate Reassessment**:
- Major process changes or improvements
- Organizational changes (restructuring, M&A)
- Significant incidents or audit findings
- Regulatory changes requiring new controls
- Technology platform changes

---

## Common Questions

### Q: Can an organization be ML5 on one control and ML1 on another?

**A**: Yes—maturity is assessed per control. Organizations often have pockets of excellence (ML4-5) alongside gaps (ML1-2). This reveals prioritization and focus areas.

---

### Q: How long does it take to progress one maturity level?

**A**: Varies by starting point and control:
- ML1→ML2: 1-3 months (documentation effort)
- ML2→ML3: 6-12 months (standardization and adoption)
- ML3→ML4: 12-18 months (measurement infrastructure)
- ML4→ML5: 18-36 months (innovation culture)

Earlier levels are faster; higher levels require deeper organizational change.

---

### Q: Must we achieve ML3 on all controls before attempting ML4 on any?

**A**: No—maturity progression doesn't need to be uniform. Organizations can achieve ML4-5 on critical controls while others remain ML2-3. However, dependencies exist (e.g., can't have ML4 monitoring if ML1 governance—no one reviews the metrics).

---

### Q: If we're "between" levels, how do we score?

**A**: Use the lower level. "Between ML2 and ML3" means you're advancing toward ML3 but haven't achieved it yet → Score ML2. The criteria for ML3 include sustained, consistent, organization-wide application.

---

### Q: Does maturity level affect which baseline we need?

**A**: No—baseline is determined by AI system risk characteristics, not organizational maturity. However, low-maturity organizations deploying high-risk AI (B3 baseline, ML1-2 maturity) face significant risk and should either:
- Accelerate maturity improvement, or
- Defer high-risk AI deployment until mature capabilities exist

---

## References

- CMMI for Development v2.0 - Maturity level definitions
- ISO/IEC 33002:2015 - Process assessment model
- ISO/IEC 42001:2023 - AI management system maturity
- NIST Cybersecurity Framework - Implementation tier progression

---

**Related Documents**:
- [Framework Overview](../core/AIMF-FRAMEWORK-OVERVIEW.md)
- [Risk Baselines](AIMF-RISK-BASELINES.md)
- [Assessment Guide](AIMF-ASSESSMENT-GUIDE.md)
- [Maturity Level Progression Guides](maturity-level-guides/)

---

**Next Steps**: See [Maturity Level 1-to-2 Guide](maturity-level-guides/MATURITY-LEVEL-1-TO-2-GUIDE.md) for detailed roadmap from Initial to Developing maturity.
