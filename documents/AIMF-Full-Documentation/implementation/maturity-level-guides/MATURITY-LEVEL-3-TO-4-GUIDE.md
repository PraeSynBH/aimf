# AI Management Framework (AIMF) by PraeSyn

## Maturity Level 3→4 Implementation Guide

### From Enterprise Standards to Data-Driven Management

**© 2026 PraeSyn, LLC. All rights reserved.**
Licensed under CC BY-NC-ND 4.0

**Target Audience**: Organizations at **Maturity Level 3 (Defined)** working toward **Maturity Level 4 (Managed)**
**Version**: 1.0
**Publication Date**: January 29, 2026
**Status**: Pre-Publication (Working Draft)
**Date**: 2025-10-23

---

## Executive Summary

**Current State**: Your organization is at Maturity Level 3 - You have enterprise-wide AI standards, automated governance platforms, and consistent processes across all AI projects. AI governance is embedded and systematic.

**Target State**: Maturity Level 4 - Achieve data-driven management where AI performance, risks, and value are **quantitatively measured, predicted, and optimized**. Move from reactive monitoring to proactive management.

**Timeline**: **12-24 months** to solidly achieve Maturity Level 4 (varies by data maturity and analytics capability)

**Investment Level**: **Advanced**
- 1-2 FTE dedicated to AI metrics, analytics, and optimization
- $100-300K in advanced analytics, AI observability platforms, and BI tools
- Significant data engineering and MLOps platform enhancement

**Key Priorities**:
1. **Measurement**: Establish comprehensive metrics for AI performance, risk, and business value
2. **Analytics**: Build analytics capability to understand AI system behavior and trends
3. **Prediction**: Use data to predict issues before they occur
4. **Optimization**: Continuously improve AI systems and governance based on measured effectiveness
5. **Transparency**: Provide real-time visibility to stakeholders at all levels

**Success Indicator**: Within 24 months, leadership sees real-time dashboards of AI health, you predict and prevent issues before customer impact, and AI governance effectiveness is measured and improving.

---

## 1. Current State Context: Understanding Maturity Level 3

### Where You Are and Why You're in the Elite

**You're at Maturity Level 3 if**:
- Enterprise MLOps platform operational with high adoption
- AI governance fully integrated into enterprise frameworks
- All AI projects follow standardized processes automatically
- Model documentation, risk assessment, and deployment approvals are automated
- Organization-wide AI literacy and cross-functional collaboration
- Regular audits show high compliance rates
- Leadership receives systematic AI governance reporting

**This is exceptional**. According to industry surveys, fewer than 15% of organizations reach Maturity Level 3 AI maturity. You're in rare company.

### The Maturity Level 3 Reality: Systematic But Not Optimal

**What's working**:
- You have visibility, control, and consistency
- AI scales confidently across the organization
- Governance is embedded and mostly invisible
- You can demonstrate compliance to auditors and regulators
- Technical debt is managed systematically

**What you're noticing**:
- **Reactive monitoring**: You detect problems, but after they start affecting users
- **One-size-fits-all governance**: Same controls for all systems, regardless of actual risk profile
- **Limited insight into "why"**: You know *what* happened, but not always *why* or *how to prevent recurrence*
- **Manual optimization**: Improving models and governance requires human analysis of logs and metrics
- **Lagging indicators**: Most metrics tell you about past performance, not future risk

**This is the Maturity Level 3 plateau**. You've achieved systematic governance. Now it's time to make it intelligent.

### Common Maturity Level 3 Questions

**Question A: "How do we know our governance is actually working?"**
Reality: At Maturity Level 3, you measure compliance (did teams follow processes?), but not effectiveness (did processes achieve intended outcomes?). Maturity Level 4 measures both.

**Question B: "Why do we still have incidents if we have so much governance?"**
Reality: Even good processes miss edge cases. Maturity Level 4 uses predictive analytics to catch issues before they become incidents.

**Question C: "How do we balance governance rigor with AI innovation?"**
Reality: At Maturity Level 3, governance controls are often uniform. Maturity Level 4 tailors controls to measured risk, reducing friction for low-risk systems while tightening high-risk systems.

**Question D: "What's the business value of all this AI investment?"**
Reality: Maturity Level 3 may track project-level ROI, but not portfolio-level value or opportunity cost. Maturity Level 4 provides enterprise-wide AI value visibility.

### Why Maturity Level 3→4 Is Different from Earlier Transitions

**Maturity Level 1→2**: Documentation and structure (foundational capability)
**Maturity Level 2→3**: Standardization and automation (enterprise scaling)
**Maturity Level 3→4**: **Quantitative management and prediction** (intelligence and optimization)

**This requires different capabilities**:
- **Data engineering**: Collecting, structuring, and analyzing AI system telemetry at scale
- **Analytics**: Statistical analysis, trend detection, predictive modeling
- **Tooling**: Advanced observability, BI platforms, ML for MLOps (meta-ML)
- **Culture**: Data-driven decision-making mindset across organization

If your organization already operates at high data maturity (e.g., sophisticated analytics, data-driven culture), Maturity Level 3→4 will be natural. If data culture is still maturing, this will be challenging but transformative.

---

## 2. The Case for Change: Why Move to Maturity Level 4?

### Benefits of Maturity Level 4 Data-Driven Management

**Proactive Risk Management**:
- **Predict incidents** before they impact customers (e.g., detect model drift accelerating before accuracy drops)
- **Anticipate compliance issues** before audits find them
- **Forecast resource needs** for AI infrastructure to avoid outages

**Optimization and Efficiency**:
- **Continuous improvement**: Automatically identify underperforming models and governance bottlenecks
- **Right-sized governance**: Apply heavy controls only where data shows risk, reducing friction elsewhere
- **Resource optimization**: Allocate infrastructure, people, and budget based on measured value and risk

**Business Value Visibility**:
- **Portfolio management**: See which AI investments deliver value and which don't
- **ROI tracking**: Measure AI business impact systematically
- **Strategic decisions**: Data-driven prioritization of AI initiatives

**Competitive Advantage**:
- **Faster iteration**: Data-driven feedback loops accelerate model improvement
- **Higher reliability**: Predictive management reduces downtime and incidents
- **Stakeholder confidence**: Demonstrate AI performance and risk management quantitatively

### Risks of Remaining at Maturity Level 3

Maturity Level 3 is sustainable, but **Maturity Level 4 competitors will outpace you**:

**Innovation Speed**:
- Maturity Level 4 organizations iterate faster because data tells them what to improve
- Your manual analysis and reactive approach will feel slow in comparison

**Incident Prevention**:
- Maturity Level 3 detects incidents; Maturity Level 4 prevents them
- When competitors have fewer AI failures, customers notice

**Resource Efficiency**:
- Maturity Level 4 organizations optimize resource allocation based on measured value
- Your one-size-fits-all approach is more expensive and less effective

**Regulatory Pressure**:
- Future AI regulations will likely require demonstrable effectiveness measurement
- Maturity Level 3 compliance reporting is backward-looking; Maturity Level 4 is predictive

### Challenges You'll Face Moving to Maturity Level 4

1. **Data Infrastructure Investment**
   - Challenge: Requires sophisticated data pipelines, warehouses, and analytics platforms
   - Reality: This is enterprise data engineering work, potentially $100-300K investment
   - Mitigation: Leverage existing enterprise data infrastructure where possible; build incrementally

2. **Analytics Skills Gap**
   - Challenge: Requires data scientists/analysts focused on "AI operations analytics" (not just model building)
   - Reality: This is specialized skillset combining MLOps, data engineering, and analytics
   - Mitigation: Upskill existing team, hire specialists, or partner with analytics CoE

3. **Metric Definition Complexity**
   - Challenge: What should you measure? How do you measure "governance effectiveness" or "AI business value"?
   - Reality: Metrics design is hard and requires iteration to get right
   - Mitigation: Start with obvious metrics (accuracy, latency, incident rates), expand to sophisticated metrics over time

4. **Cultural Shift to Data-Driven**
   - Challenge: Moving from "we think this is working" to "data shows this is working" requires mindset change
   - Reality: Data-driven decision-making is cultural, not just technical
   - Mitigation: Leadership must model data-driven decisions; celebrate data-informed improvements

5. **Analysis Paralysis Risk**
   - Challenge: Too much data can be overwhelming ("we have dashboards but no insights")
   - Reality: Data without interpretation is noise
   - Mitigation: Start with key questions, build metrics to answer them, iterate

6. **Tool Proliferation**
   - Challenge: Risk of adding another platform (observability, BI) to already complex stack
   - Reality: Maturity Level 4 requires integration, not just addition
   - Mitigation: Architectural planning to integrate AI observability with existing enterprise BI and monitoring

### Time Realities

**What happens in 6-12 months**:
- Metrics framework designed and instrumentation implemented
- Data pipelines operational
- Initial dashboards and reports available
- Pilot use cases show predictive analytics value

**What takes 12-24 months**:
- Comprehensive metrics across all AI systems
- Predictive models for incident prevention operational
- Organization-wide adoption of data-driven AI decision-making
- Demonstrated ROI from Maturity Level 4 investment

**Maturity Level 3→4 requires sustained investment in data capabilities**. This is not a one-time project; it's building new organizational muscle.

---

## 3. Target State Vision: What Maturity Level 4 and Maturity Level 5 Look Like

### Maturity Level 4 (Your Goal): Quantitatively Managed

**You'll know you've reached Maturity Level 4 when**:

✅ **Comprehensive Measurement**
- **AI System Performance**: Accuracy, latency, availability, drift tracked in real-time for all production systems
- **Governance Effectiveness**: Compliance rates, policy exceptions, audit findings, time-to-approval tracked and trended
- **Business Value**: AI ROI, opportunity realization, cost savings measured at portfolio level
- **Risk Metrics**: Incident rates, mean-time-to-detection, mean-time-to-resolution, risk score trends
- **Trustworthy AI Metrics**: Bias, fairness, explainability, privacy measured quantitatively

✅ **Predictive Analytics**
- **Incident Prediction**: Models predict which AI systems are likely to fail before they do
- **Drift Detection**: Early warning systems catch data/concept drift before accuracy degrades
- **Capacity Forecasting**: Predict infrastructure needs based on AI usage trends
- **Risk Forecasting**: Identify emerging risks based on system behavior patterns

✅ **Automated Optimization**
- **Performance Optimization**: Automatically trigger model retraining when performance degrades below thresholds
- **Resource Optimization**: Auto-scale infrastructure based on measured demand
- **Governance Optimization**: Adjust control rigor based on measured risk (lighter for low-risk, heavier for high-risk)
- **Process Optimization**: Identify governance bottlenecks and automatically suggest improvements

✅ **Real-Time Visibility**
- **Executive Dashboards**: Leadership sees AI portfolio health, risk, and value in real-time
- **Operational Dashboards**: Technical teams see system performance and get proactive alerts
- **Governance Dashboards**: Risk/compliance teams see policy compliance and emerging risks
- **Business Dashboards**: Product teams see AI-driven business metrics and ROI

✅ **Continuous Improvement**
- **Feedback Loops**: Measured outcomes drive rapid iteration on models and governance
- **Benchmarking**: Compare your AI performance against industry standards and internal baselines
- **A/B Testing**: Systematically test governance approaches and measure effectiveness
- **Learning Organization**: Insights from data become organizational knowledge

**Maturity Level 4 is about making AI governance and operations intelligent**. You don't just have data - you use it to predict, optimize, and improve continuously.

### Maturity Level 5 (

The Future): Continuous Innovation and Industry Leadership

**Looking ahead to Maturity Level 5** (24-36 months from now):

At Maturity Level 5, quantitative management (Maturity Level 4) enables **continuous innovation and industry leadership**:
- **Self-optimizing AI systems**: Meta-learning systems automatically improve governance and model performance
- **Industry thought leadership**: Your organization contributes to AI standards and best practices
- **Innovation acceleration**: Culture of experimentation with rapid, safe learning cycles
- **Regulatory influence**: You help shape AI regulations based on demonstrated best practices
- **AI-driven transformation**: AI capabilities drive fundamental business model evolution

**Why show you Maturity Level 5 now?** When you're building Maturity Level 4 data infrastructure, design it to enable Maturity Level 5 innovation. The foundation you lay now determines future possibilities.

---

## 4. Communication Strategy for Implementation Leaders

### Framing Maturity Level 4: From Control to Intelligence

As the change agent, your messaging challenge is:
- **Maturity Level 3 established control**: "We have governance and it works"
- **Maturity Level 4 adds intelligence**: "Now let's make governance smart and AI highly reliable"

### Key Messages by Audience

**To Executives**:
*"We've built systematic AI governance [Maturity Level 3]. Now we're making it intelligent [Maturity Level 4]. This means we'll predict and prevent AI issues before they impact customers, optimize our AI investments based on measured ROI, and make data-driven decisions about where to innovate next. The investment in analytics and observability will pay for itself through reduced incidents and better resource allocation."*

**To Technical Teams**:
*"You've been building great AI systems [Maturity Level 3]. Now we're giving you the data to make them even better [Maturity Level 4]. You'll have real-time performance insights, predictive alerts before things break, and automated feedback loops so you can iterate faster. This isn't more oversight - it's better tools to make your work more effective and less reactive firefighting."*

**To Risk/Governance Teams**:
*"We've established compliance processes [Maturity Level 3]. Now we're measuring whether they actually reduce risk [Maturity Level 4]. You'll see which controls are effective and which are just overhead, so we can optimize governance to be both safer and more efficient. Plus, predictive risk analytics will shift you from reactive to proactive."*

**To Business Leaders**:
*"We've scaled AI across the organization [Maturity Level 3]. Now we're measuring which AI investments deliver value and which don't [Maturity Level 4]. You'll have visibility into AI ROI, opportunity costs, and portfolio performance - so we can double down on what works and cut what doesn't. This is bringing the same data-driven rigor to AI that we use for other investments."*

### Addressing the "We Already Have Dashboards" Objection

**Objection**: "We already have monitoring and dashboards. Why do we need more?"

**Response**: "You're right that we have dashboards [Maturity Level 3]. But right now, most of them are **descriptive** - they tell us what *happened*. Maturity Level 4 makes them **predictive and prescriptive** - they tell us what's *about to happen* and what *to do about it*. That's the difference between knowing your model failed yesterday and predicting it will fail tomorrow so you can fix it before customers notice. That shift from reactive to proactive is the ROI."

---

## 5. Multi-Audience Assessments

### Assessment Instructions

Use these assessments to validate Maturity Level 3 maturity and plan Maturity Level 4 progression.

**Scoring**: canonical 0-4 / ML1-ML5 scale (see `../AIMF-ASSESSMENT-GUIDE.md`):
- 0 = ML1 - Initial
- 1 = ML2 - Developing
- 2 = ML3 - Defined (this guide's starting point)
- 3 = ML4 - Managed (this guide's target)
- 4 = ML5 - Optimizing
- **Use +/- modifiers** for partial levels: 2+ means "solidly ML3 - Defined, with some ML4 capabilities emerging"

**Maturity Level 4 Readiness**: If most questions score 3 (ML4 - Managed), you're ready for Maturity Level 4 progression.

> **Scale note**: the retired 0-3 lens scored this quiz 0-3 with "3 = Established" and used
> "3+" for emerging ML4 capability. On the canonical scale "Established" is ML3 = **2** and
> ML4 is its own score, **3** — which is why ML4 readiness is now stated as score 3 rather
> than "3+". Old quiz notes convert with the table in `../AIMF-ASSESSMENT-GUIDE.md`.

---

### Leadership Assessment

#### L1. Data-Driven AI Decision Making

**Question**: Does leadership make AI investment and risk decisions based on quantitative data and measured outcomes?

**Maturity Level 4 Target**:
- Investment decisions use measured AI ROI data
- Risk decisions use quantitative risk metrics
- Resource allocation based on measured value and strategic importance
- Post-decision reviews compare actual outcomes to projections

**Evidence to Look For**: Investment business cases with measured outcomes, decision records citing the metrics used, post-decision reviews comparing projection to result

**Your Score**: ___ (0-4)

---

#### L2. Real-Time AI Portfolio Visibility

**Question**: Does leadership have real-time visibility into AI portfolio performance, risks, and business value?

**Maturity Level 4 Target**:
- Executive dashboard with key AI metrics (updated at least daily)
- Portfolio-level view of AI systems, not just project-by-project
- Alerts for portfolio-level issues (e.g., multiple systems underperforming)
- Historical trends show AI maturity progression

**Evidence to Look For**: The executive dashboard itself, its refresh configuration, a portfolio-level inventory view, alert configuration and the response record for the last portfolio alert

**Your Score**: ___ (0-4)

---

#### L3. AI Value Accountability

**Question**: Is the value delivered by AI measured, attributed and reviewed with the same discipline as the case that justified the investment?

**Maturity Level 4 Target**:
- Every AI initiative has a baseline and a measured outcome, recorded in a standard form
- Attribution is stated explicitly, including where the AI contribution cannot be isolated
- Underperforming initiatives are re-scoped or stopped on evidence, not quietly continued
- Portfolio-level value is reported in business units (revenue, cost, cycle time, risk avoided) and reconciled with finance

**Evidence to Look For**: Baseline and outcome records, financial reconciliation, stop/re-scope decisions with rationale

**Your Score**: ___ (0-4)

---

#### L4. Quantitative Risk Appetite for AI

**Question**: Has leadership set explicit, quantified risk appetite for AI that governs how much risk each system class may carry?

**Maturity Level 4 Target**:
- Risk appetite is stated in measurable terms (incident rates, error tolerances, exposure limits) by system class
- Every AI system is compared against the appetite for its class, with breaches visible
- Appetite breaches trigger a defined response, including business-owner accountability
- Appetite is revisited on evidence, and changes are recorded with their rationale

**Evidence to Look For**: Risk appetite statement, system-to-appetite comparison, breach response records, revision history

**Your Score**: ___ (0-4)

---

#### L5. Portfolio Rebalancing on Evidence

**Question**: Does leadership rebalance AI investment between exploitation and exploration based on measured returns and risk, on a set cadence?

**Maturity Level 4 Target**:
- A defined allocation exists between running existing AI, extending it, and exploratory work
- Rebalancing decisions are made on measured performance, not on seniority of the sponsor
- Protected allocation exists for exploratory work so it is not crowded out by operational demand
- Rebalancings and their outcomes are recorded, including where the decision was wrong

**Evidence to Look For**: Allocation targets, portfolio review minutes, reallocation records, outcome reviews

**Your Score**: ___ (0-4)

---

#### L6. Quantitative Reporting to the Board

**Question**: Does the board or equivalent receive AI performance and risk in quantitative, comparable form rather than narrative assurance?

**Maturity Level 4 Target**:
- A standing board pack section carries a stable set of AI measures with trends, not one-off figures
- Measures are defined once and do not change definition between periods without explanation
- Risk measures include leading indicators, not only incidents that already happened
- The board's questions and decisions are recorded and tracked to answer

**Evidence to Look For**: Board packs across periods, metric definitions register, question/action log

**Your Score**: ___ (0-4)

**Leadership Assessment Total**: ___/24 points (6 questions × 4)
**Leadership Score**: (Total/24) × 100 = ___%

---

### Technical Assessment

**Instructions for Technical**: Rate the measurement capability that exists in operation today — instrumentation, thresholds, and whether the numbers are trusted.

#### T1. Metrics Instrumentation

**Question**: Are AI system metrics collected automatically into a durable store, with defined definitions and lineage to business outcomes?

**Maturity Level 4 Target**:
- Metrics are emitted by the system or its platform, not compiled by hand
- Each metric has a written definition, unit, owner and known limitations
- Metrics are retained long enough to compare periods and to support audit
- Business-outcome metrics are linked to system metrics so the causal chain can be examined

**Evidence to Look For**: Metric definitions register, instrumentation code/config, retention configuration, linkage documentation

**Your Score**: ___ (0-4)

---

#### T2. Performance and Business-KPI Linkage

**Question**: Can the team demonstrate the relationship between model performance and the business KPI the model exists to move?

**Maturity Level 4 Target**:
- Each production model has at least one business KPI it is expected to affect, agreed with the business owner
- The relationship is measured (correlation, controlled test or modelled attribution) and its strength is stated
- Degradation in the model metric is interpreted in business terms, not just engineering terms
- Known confounders are documented rather than assumed away

**Evidence to Look For**: KPI linkage records, analysis notebooks or reports, confounder documentation

**Your Score**: ___ (0-4)

---

#### T3. Thresholded Drift and Degradation Management

**Question**: Are drift and degradation thresholds defined, alerting, and tied to a defined response — including automatic retraining where that is safe?

**Maturity Level 4 Target**:
- Thresholds are set per system from baseline data and reviewed after each retraining
- Alerts distinguish noise from signal, and alert precision is measured
- Retraining triggers are defined, with validation gates before promotion
- Automated retraining, where used, has a documented safety boundary and a rollback path

**Evidence to Look For**: Threshold register, alert history with precision measure, retraining policy, automation guardrails

**Your Score**: ___ (0-4)

---

#### T4. Cost and Capacity Management

**Question**: Are AI running costs measured per system and per transaction, with forecasts used in planning?

**Maturity Level 4 Target**:
- Cost is attributed per system, and where feasible per unit of business volume
- Unit economics are tracked over time and compared across systems
- Forecasts exist for volume growth, with the cost curve of the main drivers stated
- Cost anomalies alert to an owner, not discovered at quarter end

**Evidence to Look For**: Cost attribution reports, unit economics trends, forecasts, anomaly alerting

**Your Score**: ___ (0-4)

---

#### T5. Experimental Discipline

**Question**: Are changes to models and prompts evaluated through controlled experiments with pre-registered hypotheses and decision rules?

**Maturity Level 4 Target**:
- A hypothesis, success measure and decision rule are written before the experiment runs
- Experiments run against a control, with sample sizing that can detect the effect claimed
- Results — including inconclusive and negative results — are recorded in one place
- Ship/no-ship decisions cite the experiment, not the opinion of the most senior person present

**Evidence to Look For**: Experiment register, pre-registration records, analysis outputs, decision log

**Your Score**: ___ (0-4)

---

#### T6. Predictive Incident Forecasting

**Question**: Are leading indicators used to forecast incidents before they occur, with the forecast evaluated after the fact?

**Maturity Level 4 Target**:
- Candidate leading indicators are identified from incident history rather than guessed
- Forecasts are scored against outcomes, and forecast accuracy is published
- Forecasts trigger preventive action with an owner, not just a warning
- Indicators that fail to predict are retired rather than retained for comfort

**Evidence to Look For**: Indicator analysis, forecast-versus-actual records, preventive action log, retired indicators list

**Your Score**: ___ (0-4)

---

#### T7. Automation with Human Oversight

**Question**: Where remediation is automated, is there a documented automation boundary with human authority preserved and exercised?

**Maturity Level 4 Target**:
- The automation boundary is written per system: what may be changed automatically and what requires approval
- Automated actions are logged with before/after state and the triggering condition
- A human override exists, is reachable, and has been exercised in a drill
- Automation effectiveness is measured, and autonomy is increased only on evidence

**Evidence to Look For**: Automation boundary document, action logs, override drill records, effectiveness review

**Your Score**: ___ (0-4)

---

#### T8. Measurement Integrity

**Question**: Is there a control over the metrics themselves — so a reported number can be trusted, reproduced and defended?

**Maturity Level 4 Target**:
- Metric definitions are versioned, with changes announced and restated where they alter history
- Metric pipelines are tested, and failures are visible rather than silently producing nulls
- A sample of reported metrics is reconciled against source data each period
- Known limitations of each metric are stated wherever the metric is reported

**Evidence to Look For**: Definition version history, pipeline tests, reconciliation records, limitation statements

**Your Score**: ___ (0-4)

**Technical Assessment Total**: ___/32 points (8 questions × 4)
**Technical Score**: (Total/32) × 100 = ___%

---

### Governance Assessment

**Instructions for Governance**: Rate whether governance can demonstrate effectiveness in numbers, rather than demonstrating activity.

#### G1. Governance Effectiveness Measures

**Question**: Are there measures that show whether governance is reducing risk, rather than whether governance activity is being performed?

**Maturity Level 4 Target**:
- Effectiveness measures exist (incident prevention rate, early-detection rate, time-to-approval trend, audit finding severity trend)
- Baselines were set before the measures were used for reporting, so improvement is measurable
- Measures are reviewed quarterly and are used to change the control set
- Activity measures (reviews completed, policies issued) are reported separately and never presented as effectiveness

**Evidence to Look For**: Effectiveness measure definitions, baselines, quarterly review records, control changes attributed to the data

**Your Score**: ___ (0-4)

---

#### G2. Risk-Based Control Tailoring in Operation

**Question**: Are control depth and approval paths actually differentiated by measured risk, or does every system get the same process?

**Maturity Level 4 Target**:
- Control requirements are defined per risk tier and are enforced by workflow, not by convention
- Tier assignment is data-driven (impact, incident history, regulatory exposure) and recorded
- High-risk systems show lower incident rates and low-risk systems show shorter approval times — the signature of working tailoring
- Tier drift is monitored: a system whose risk profile changed is re-tiered

**Evidence to Look For**: Tier definitions, workflow configuration, measures by tier, re-tiering records

**Your Score**: ___ (0-4)

---

#### G3. Quantitative Control Testing

**Question**: Is control testing sampled and measured, so that assurance coverage and failure rates are known numbers?

**Maturity Level 4 Target**:
- Each control has a test method and a sample basis that can be re-performed
- Test results are recorded as pass/fail with evidence references, in a form that can be aggregated
- Coverage is measured: which controls were tested, how often, and which were never tested
- Failure rates by control and by team drive where the next cycle's effort goes

**Evidence to Look For**: Test plans, result records, coverage report, failure-rate trend by control

**Your Score**: ___ (0-4)

---

#### G4. Predictive Compliance Monitoring

**Question**: Are leading compliance indicators monitored so that drift toward non-compliance is detected before an audit or incident finds it?

**Maturity Level 4 Target**:
- Leading indicators are defined per obligation (training currency, review backlog age, exception accumulation, evidence gaps)
- Thresholds trigger action with an owner and a deadline
- Indicator performance is reviewed: did the indicator in fact precede the finding?
- Indicators that never move are retired

**Evidence to Look For**: Indicator definitions, threshold breach records, action closure, indicator performance review

**Your Score**: ___ (0-4)

---

#### G5. Automated Policy Enforcement

**Question**: Is policy enforced by system controls where it can be, with manual review reserved for judgement calls?

**Maturity Level 4 Target**:
- Each policy requirement is classified as enforceable by system, checkable by review, or dependent on judgement
- Enforceable requirements are implemented in tooling, with the enforcement point documented
- Exceptions are recorded with an expiry and are reported as a trend
- Enforcement effectiveness is measured by exception volume and by whether violations recur

**Evidence to Look For**: Policy-to-enforcement map, tool configurations, exception register, recurrence analysis

**Your Score**: ___ (0-4)

---

#### G6. Continuous Assurance and Audit Analytics

**Question**: Does assurance use continuous or frequent data sampling rather than annual snapshots?

**Maturity Level 4 Target**:
- Key controls are monitored continuously or on a short cycle from system data
- Analytics identify anomalies (unreviewed approvals, missing evidence, out-of-band deployments) without waiting for a review cycle
- Findings are raised as they appear, with remediation tracked from the moment of detection
- External auditors are given access to the same evidence stream, reducing annual effort

**Evidence to Look For**: Monitoring rules, anomaly case log, remediation tracking, auditor access records

**Your Score**: ___ (0-4)

---

#### G7. Metric Governance

**Question**: Is there an owner and a change process for the metrics used in governance reporting?

**Maturity Level 4 Target**:
- Every reported governance metric has a named owner and a written definition
- Changes to definitions are approved and restated, so trends remain comparable
- Disputes about a number are resolved through the definition, not through escalation
- Metric owners attest to the accuracy of their metrics each reporting period

**Evidence to Look For**: Metric ownership register, change approvals, restatement records, attestation records

**Your Score**: ___ (0-4)

**Governance Assessment Total**: ___/28 points (7 questions × 4)
**Governance Score**: (Total/28) × 100 = ___%

---

### Change Agent Assessment

**Instructions for Change Agent**: Rate whether the organization decides on evidence — the cultural precondition for Maturity Level 4 to mean anything.

#### C1. Data and Metric Fluency

**Question**: Can the people making AI decisions read, question and interpret the metrics they are shown?

**Maturity Level 4 Target**:
- Role-based training covers the metrics each role is accountable for, including their limitations
- Decision-makers routinely ask for the definition and sample behind a number
- Interpretation errors are treated as a capability gap to close, not a personal failing
- A shared metric glossary exists and is used in meetings

**Evidence to Look For**: Training records, glossary, meeting minutes showing definition-level questions

**Your Score**: ___ (0-4)

---

#### C2. Experiment-Driven Working

**Question**: Do teams treat experiments as the normal way to decide, including when the answer is "no"?

**Maturity Level 4 Target**:
- Teams can run low-cost experiments without a lengthy approval cycle for low-risk changes
- Negative and inconclusive results are shared, not buried
- Decision records cite evidence, and the absence of evidence is stated plainly
- Experiment throughput and cycle time are tracked as a capability measure

**Evidence to Look For**: Experiment register including negative results, decision records, throughput metrics

**Your Score**: ___ (0-4)

---

#### C3. Feedback Loops into Product Decisions

**Question**: Do operational findings (incidents, drift, user feedback) actually change the roadmap within a defined cycle?

**Maturity Level 4 Target**:
- A defined route exists from operational finding to roadmap decision, with a timeframe
- Findings are triaged with the business owner, not only within engineering
- Changes made in response are recorded and linked back to the finding
- Findings that produce no change are explicitly closed with a reason

**Evidence to Look For**: Triage records, roadmap change log linked to findings, closure decisions

**Your Score**: ___ (0-4)

---

#### C4. Dashboard-to-Decision Adoption

**Question**: Are the dashboards that exist actually used in decisions, or do they exist to demonstrate measurement?

**Maturity Level 4 Target**:
- Dashboard usage is measured (viewers, decisions referencing the data, actions triggered)
- Dashboards with no decision attached are retired rather than maintained
- Each dashboard has a named decision it supports and an owner who uses it
- Reviews ask "what did this data change?" and record the answer

**Evidence to Look For**: Usage analytics, dashboard inventory with decision linkage, retirement records

**Your Score**: ___ (0-4)

---

#### C5. Incentives Aligned to Measured Outcomes

**Question**: Are team and individual incentives aligned to measured outcomes and honest reporting, rather than to favourable numbers?

**Maturity Level 4 Target**:
- Objectives include outcome and quality measures, not only delivery volume
- Reporting quality is itself assessed, so there is no reward for a flattering number
- Corrections to previously reported figures are treated as good practice
- Incentive design is reviewed after each cycle for gaming behaviour

**Evidence to Look For**: Objective definitions, appraisal criteria, reporting-error handling records, incentive review

**Your Score**: ___ (0-4)

---

#### C6. Analytical Capability Building

**Question**: Is analytical capability being built in the teams that own AI outcomes, not concentrated in a single reporting function?

**Maturity Level 4 Target**:
- Analytical skills are defined in role expectations for AI owners, not only for analysts
- Embedded analysis support exists with a plan to transfer capability over time
- Capability gaps are identified from work products (quality of experiment design, interpretation)
- Progression paths exist for analytical roles

**Evidence to Look For**: Role expectations, embedded support plan, capability assessment, progression framework

**Your Score**: ___ (0-4)

**Change Agent Assessment Total**: ___/24 points (6 questions × 4)
**Change Agent Score**: (Total/24) × 100 = ___%

---

### Assessment Summary and Next Steps

| Audience | Score | What a 75-100% score (average ML4) means here |
|---|---|---|
| Leadership | ___% | Decisions are made on measured value and quantified risk appetite, not narrative |
| Technical | ___% | The numbers are instrumented, thresholded, and their integrity is itself controlled |
| Governance | ___% | Effectiveness is measured, controls are tiered and tested, and enforcement is automated where it can be |
| Change Agent | ___% | Decisions cite evidence, and honest reporting is safe |

**Readiness rule**: Maturity Level 4 is claimed on measured effectiveness, not on the existence of dashboards. Before declaring it, confirm three things from evidence: a control set that has been *tested* with a published failure rate, a portfolio in which at least one initiative was stopped or re-scoped on measured evidence, and a board pack whose measures are defined, versioned and comparable period over period. An organization with dashboards and none of those three is at Maturity Level 3 with better reporting.

---

## 6. Multi-Audience Implementation Playbooks

### Leadership Playbook: Data-Driven Governance

#### Priority Actions (Months 1-6)

**Action 1: Define AI Metrics Framework**

**What**: Establish comprehensive framework for measuring AI performance, risk, and value

**Key Metric Categories**:

1. **AI System Performance Metrics** (Technical)
   - Model accuracy, precision, recall (vs. baseline)
   - Latency (p50, p95, p99)
   - Availability/uptime
   - Throughput/capacity utilization
   - Data quality scores
   - Model drift indicators

2. **Governance Effectiveness Metrics**
   - Policy compliance rate (% projects compliant)
   - Time-to-approval for AI projects
   - Audit findings (count, severity trends)
   - Policy exception rate and reasons
   - Training completion rates
   - Risk assessment coverage

3. **Business Value Metrics**
   - AI project ROI (measured, not projected)
   - Business KPIs influenced by AI (revenue, cost, customer satisfaction)
   - Time-to-value for AI projects
   - Adoption/usage rates of AI systems
   - Opportunity realization vs. projected value

4. **Risk and Incident Metrics**
   - AI incident count and severity
   - Mean-time-to-detection (MTTD)
   - Mean-time-to-resolution (MTTR)
   - Incident recurrence rates
   - Risk score trends by system and portfolio

5. **Trustworthy AI Metrics** (NIST AI RMF Characteristics)
   - Bias/fairness metrics (demographic parity, equalized odds)
   - Explainability scores (% of predictions explainable)
   - Privacy risk scores
   - Security vulnerability counts
   - Robustness (adversarial test results)

**How**:
1. Workshop with stakeholders to define what matters
2. Prioritize metrics (start with 10-15 key metrics, expand over time)
3. Define calculation methodology and data sources
4. Establish baselines and targets
5. Document metrics framework and socialize

**Timeline**: Month 1-3
**Investment**: Workshop facilitation + documentation

---

**Action 2: Establish AI Analytics Team/Capability**

**What**: Build dedicated capability for AI operations analytics

**Options**:
- **Dedicated Team**: 1-2 FTE (Data Engineer + ML Analyst) focused on AI observability
- **Augmented Team**: Add AI analytics responsibility to existing analytics CoE
- **Hybrid**: Core resource plus rotational assignments from technical teams

**Responsibilities**:
- Instrument AI systems for metrics collection
- Build data pipelines and analytics infrastructure
- Develop dashboards and reports
- Conduct analyses to identify optimization opportunities
- Build predictive models for incident prevention

**Timeline**: Month 2-4 (hiring or allocation)
**Investment**: 1-2 FTE ($150-300K annual)

---

**Action 3: Invest in Advanced AI Observability Platform**

**What**: Augment existing monitoring with AI-specific observability tools

**Platform Capabilities**:
- AI-specific metrics (drift, bias, explainability)
- Trace and lineage for AI predictions
- Anomaly detection on AI system behavior
- Alerting with root cause analysis
- Integration with existing enterprise monitoring

**Platform Options**:
- Purpose-built AI observability (e.g., Arize, Fiddler, WhyLabs, Arthur)
- Enhanced general observability (DataDog AI, New Relic AI, Dynatrace AI)
- Open source (Evidently, Alibi, custom on Prometheus/Grafana)

**Timeline**: Month 3-6 (evaluation, procurement, implementation)
**Investment**: $50-150K annual subscription + implementation effort

---

#### Ongoing Responsibilities (Months 6-24)

**Monthly**:
- Review AI metrics dashboard and investigate trends
- Data-driven resource allocation decisions
- Approve or redirect AI initiatives based on measured value

**Quarterly**:
- Review metrics framework and adjust based on learnings
- Benchmarking: Compare AI performance against internal baselines and industry
- Strategic planning informed by AI portfolio analytics

**Annually**:
- Validate Maturity Level 4 maturity using assessments
- Set AI metrics targets for next year
- Invest in next-generation analytics capabilities

---

### Technical Playbook: Metrics Implementation and Predictive Operations

#### Priority Actions (Months 1-6)

**Action 1: Instrument All AI Systems for Metrics Collection**

**What**: Systematically add telemetry to every production AI system

**Instrumentation Checklist** (per system):
- [ ] Model performance metrics (accuracy, precision, recall)
- [ ] Prediction latency and throughput
- [ ] Input data characteristics (distributions, missing values)
- [ ] Prediction outputs (distributions, confidence scores)
- [ ] Resource utilization (CPU, GPU, memory)
- [ ] Errors and exceptions
- [ ] Business metrics (conversion, revenue, customer satisfaction)

**How**:
1. Create instrumentation library/package for consistent implementation
2. Update deployment templates to include instrumentation by default
3. Retrofit existing systems (prioritize by business impact)
4. Test instrumentation in non-production first
5. Roll out to production with monitoring of metrics pipeline itself

**Timeline**: Month 2-6 (incremental rollout)
**Investment**: 40-80 hours per system (faster with reusable components)

---

**Action 2: Build AI Data Pipeline and Warehouse**

**What**: Infrastructure to collect, store, and analyze AI system telemetry at scale

**Architecture**:
1. **Collection**: Agents/SDKs in AI systems emit metrics
2. **Transport**: Streaming (Kafka, Kinesis) or batching
3. **Storage**: Time-series database (InfluxDB, TimescaleDB) or data warehouse (Snowflake, BigQuery)
4. **Processing**: ETL/ELT for metric aggregation and analysis
5. **Access**: APIs and BI tools query processed metrics

**How**:
1. Design data pipeline architecture
2. Implement collection and transport layer
3. Set up storage (leverage existing enterprise data platform if possible)
4. Build initial processing jobs (aggregations, trend calculations)
5. Validate data quality and completeness

**Timeline**: Month 3-8
**Investment**: 200-400 hours data engineering + infrastructure costs

---

**Action 3: Develop Predictive Models for AI Operations**

**What**: Use ML to predict AI system issues before they impact users

**Predictive Use Cases**:

1. **Model Drift Prediction**
   - Predict when model performance will degrade below threshold
   - Early warning (e.g., "accuracy likely to drop 5% within 2 weeks")

2. **Incident Prediction**
   - Predict which systems are at risk of failure based on patterns
   - Proactive investigation and mitigation

3. **Capacity Forecasting**
   - Predict resource needs based on usage trends
   - Right-size infrastructure proactively

4. **Anomaly Detection**
   - Identify unusual patterns in AI system behavior that may indicate issues
   - Faster root cause analysis

**How**:
1. Start with one high-value use case (e.g., drift prediction for most critical model)
2. Collect historical data (need 6-12 months typically)
3. Build predictive model (ironically, using ML for MLOps)
4. Validate predictions against holdout data
5. Deploy in shadow mode (predict but don't alert) to validate
6. Promote to production with alerting
7. Expand to other use cases

**Timeline**: Month 6-12 (pilot), Month 12-24 (expansion)
**Investment**: 120-240 hours per use case

---

**Action 4: Implement Automated Remediation**

**What**: Automatically respond to predicted or detected issues

**Automation Examples**:
- **Drift Response**: Auto-trigger model retraining when drift detected
- **Performance Response**: Auto-scale infrastructure when latency increases
- **Data Quality Response**: Auto-quarantine poor-quality data and alert data owners
- **Security Response**: Auto-disable models if security vulnerability detected

**How**:
1. Start with low-risk automation (e.g., alerting is automatic; remediation requires human approval)
2. Implement automation logic with clear logging and audit trails
3. Test thoroughly in non-production
4. Deploy to production with kill switch (human can override)
5. Monitor automation effectiveness
6. Gradually increase automation autonomy based on proven reliability

**Timeline**: Month 9-18 (phased approach)
**Investment**: 80-160 hours per automation

---

### Governance Playbook: Effectiveness Measurement

#### Priority Actions (Months 1-6)

**Action 1: Define Governance Effectiveness Metrics**

**What**: Establish metrics to measure whether governance is actually reducing risk (not just whether it's being followed)

**Effectiveness Metrics**:
- **Incident Prevention**: Incidents per AI system (trending down?)
- **Early Detection**: % of issues caught before customer impact (increasing?)
- **Audit Performance**: Audit findings (decreasing? lower severity?)
- **Policy Impact**: Correlation between policy compliance and incident rates
- **Time Efficiency**: Time-to-approval trending (efficient governance should get faster, not slower, over time)

**How**:
1. Define metrics aligned to governance objectives
2. Establish data collection (may require new instrumentation)
3. Set baselines
4. Create dashboard for governance effectiveness
5. Quarterly review and adjustment

**Timeline**: Month 2-4
**Investment**: 40-60 hours + dashboard development

---

**Action 2: Implement Risk-Based Control Tailoring**

**What**: Adjust governance controls based on measured risk rather than one-size-fits-all

**Risk-Based Approach**:
- **Low-Risk AI Systems**: Lightweight controls, automated approvals, quarterly reviews
- **Medium-Risk**: Standard controls, documented approvals, bi-annual reviews
- **High-Risk**: Enhanced controls, committee approvals, continuous monitoring, quarterly reviews

**How**:
1. Define risk classification criteria (use measured incident rates, business impact, regulatory requirements)
2. Classify all AI systems by risk
3. Document differentiated control requirements by risk level
4. Update approval workflows to enforce risk-based controls
5. Measure impact: High-risk systems should have lower incident rates; low-risk systems should move faster

**Timeline**: Month 4-8
**Investment**: 60-100 hours policy work + system updates

---

### Change Agent Playbook: Building an Evidence Culture

**Your Role**: Maturity Level 4 is a decision-making change before it is a technical one. Dashboards do not change decisions; people who trust and interrogate numbers do. Your job is to make measurement the ordinary way a decision is made — and to make honest numbers safe to report.

#### Priority Actions (Months 1-6)

**Action 1: Make Metric Definitions a Shared Artefact**

**What**: Publish one metric glossary, owned per metric, and use it in every forum where AI performance is discussed.

**How**:
1. Collect every metric currently reported to leadership, governance or customers
2. For each, write the definition, the calculation, the population covered, the owner and the known limitation
3. Resolve contradictions openly — two teams reporting "accuracy" with different definitions is the normal starting state, not a scandal
4. Present the glossary at the first review meeting and require definition-level questions to be answered from it
5. Keep it versioned; a silent redefinition is how a trend becomes a fiction

**Deliverable**: Versioned metric glossary used in governance forums

**Timeline**: Month 1-3
**Investment**: 60-100 hours

---

**Action 2: Establish Decision Records for AI Changes**

**What**: Make the evidence behind a decision retrievable, so the organization can learn from it later.

**How**:
1. Adopt a lightweight decision record: decision, evidence cited, alternatives considered, who decided, review date
2. Apply it to material model, prompt, threshold and roadmap changes
3. Record decisions that were made *without* evidence as such — this is the measure of the culture, not a confession
4. Review a sample monthly: are decisions citing the experiment or the opinion?
5. Publish the aggregate (share of decisions with cited evidence) as a culture measure

**Deliverable**: Decision log in use, with an evidence-citation rate reported monthly

**Timeline**: Month 2-5
**Investment**: 40-60 hours plus per-decision time (10-20 minutes each)

---

**Action 3: Build Experiment Capability in the Teams**

**What**: Give teams the ability to test cheaply, so evidence becomes faster than opinion.

**How**:
1. Define a low-risk experiment path that does not require the full approval cycle
2. Provide templates: hypothesis, success measure, sample, decision rule, cost ceiling
3. Train teams in experiment design — sample sizing and decision rules are the common gaps
4. Reserve a small standing budget for experiments so they are not funded project by project
5. Report throughput and cycle time; celebrate informative failures as well as wins

**Deliverable**: Experiment path in use, with throughput and cycle time tracked

**Timeline**: Month 2-6
**Investment**: 80-120 hours

---

**Action 4: Retire the Dashboards Nobody Decides With**

**What**: Reduce measurement surface area to what is used, so the numbers that remain are trusted.

**How**:
1. Inventory dashboards and reports, and name the decision each supports and who makes it
2. Measure usage over a quarter rather than assuming it
3. Retire the unused ones, and record what was retired so it can be revived if needed
4. For the survivors, add the definition and limitation notes from the glossary
5. Re-check annually — dashboards accumulate the way meetings do

**Deliverable**: Dashboard inventory with decision linkage and a retirement record

**Timeline**: Month 3-5, then annually
**Investment**: 40-60 hours

---

#### Ongoing Responsibilities (Months 6-24)

**Monthly**:
- Review the evidence-citation rate on material decisions
- Review the metric glossary for unannounced changes

**Quarterly**:
- Review experiment throughput and where evidence changed a decision
- Review dashboard usage and retire what is no longer used

**Annually**:
- Re-baseline data and metric fluency across decision-making roles
- Review incentives for gaming behaviour observed in the year

---

**Change Agent Playbook Success Metrics**:
By Month 24, you should be able to answer "yes" to:
- A versioned metric glossary exists and is cited in governance forums
- Material AI decisions carry a decision record citing evidence, and the citation rate is reported
- Teams can run low-risk experiments without a full approval cycle, and negative results are shared
- Dashboards have named decisions and owners, and unused ones have been retired
- Appraisal and incentives do not reward a favourable number over an honest one

---

## 7. Cross-Functional Elements

### Dashboard Architecture

**Executive Dashboard** (Board/C-Suite):
- **Refresh**: Daily or real-time
- **Key Metrics** (10-15 max):
  - AI portfolio health score (composite)
  - High-severity incidents (count, trend)
  - AI ROI (portfolio-level)
  - Top 3 risks and mitigation status
  - Governance compliance rate
  - AI business value delivered ($ or %)
- **Format**: High-level, visual, mobile-accessible

**Operational Dashboard** (AI/ML Teams):
- **Refresh**: Real-time
- **Key Metrics**:
  - System-level performance (accuracy, latency, errors)
  - Drift indicators
  - Data quality scores
  - Alerts and incidents (open, resolution time)
  - Resource utilization
- **Format**: Detailed, drill-down capability, alerts

**Governance Dashboard** (Risk/Compliance):
- **Refresh**: Daily
- **Key Metrics**:
  - Policy compliance by system and team
  - Risk scores and trends
  - Audit findings and remediation status
  - Training completion rates
  - Exception requests and approvals
- **Format**: Audit-trail oriented, exportable

**Business Dashboard** (Product/Business Leaders):
- **Refresh**: Daily or weekly
- **Key Metrics**:
  - AI-driven business KPIs (revenue, conversion, NPS)
  - AI project ROI
  - Adoption/usage rates
  - Time-to-value
  - A/B test results
- **Format**: Business-friendly, linked to strategic objectives

---

### Timeline and Effort Estimates

**Overall Timeline**: 24 months from Maturity Level 3 to solidly achieving Maturity Level 4

**Phasing**:
- **Months 1-6** (Foundation): Metrics framework, instrumentation, initial dashboards
- **Months 7-12** (Analytics): Comprehensive data pipelines, analytics capability, predictive pilots
- **Months 13-18** (Intelligence): Predictive models operational, automated optimization
- **Months 19-24** (Maturity): Full adoption, proven effectiveness, readiness for Maturity Level 5

**Total Investment**:
- **People**: 1-2 FTE + 20-30% time from existing teams
- **Technology**: $100-300K (observability platform, data infrastructure, BI tools)
- **Total**: $250-600K over 24 months

---

## 8. Practical Tools and Resources

### Maturity Level 4 Metrics Library

These are the measures a Maturity Level 4 organization actually runs on. Every row is written so that two assessors computing it from the same data would get the same number — that is the test a metric has to pass before it belongs in a governance dashboard.

| Category | Metric | Definition | Cadence | Typical owner |
|---|---|---|---|---|
| **Performance** | Task accuracy (per system) | Correct outcomes ÷ total outcomes on the current evaluation set, with the evaluation set version recorded | Per release + weekly | Technical owner |
| | Service reliability | Successful responses ÷ total requests, excluding client errors, over the window | Daily | Technical owner |
| | Latency percentile | p50 / p95 / p99 response time in ms | Continuous | Technical owner |
| | Evaluation coverage | Share of production systems with an evaluation run in the last 90 days | Monthly | Technical owner |
| **Drift** | Input distribution drift | Population stability index (PSI) between the reference window and the last 7 days, per monitored feature group | Weekly | Technical owner |
| | Output behaviour drift | Change in the distribution of model outputs or decisions vs the reference window | Weekly | Technical owner |
| | Retraining currency | Days since last validated retraining, against the system's stated retraining interval | Monthly | Technical owner |
| **Risk** | Incidents per system per quarter | Count of AI incidents attributed to the system, by severity | Quarterly | Risk owner |
| | Early-detection rate | Incidents detected before customer or business impact ÷ all incidents | Quarterly | Risk owner |
| | Mean time to contain | Median time from incident detection to containment | Quarterly | Operations owner |
| | Control test failure rate | Failed control tests ÷ control tests performed, by control | Per assurance cycle | Governance |
| | Risk appetite breach count | Systems exceeding their risk-appetite measures, with the measure named | Monthly | Governance |
| **Governance** | Time-to-approval | Median elapsed time from review request to decision, by risk tier | Monthly | Governance |
| | Review backlog age | Age of oldest open review, in days | Weekly | Governance |
| | Exception volume and expiry | Open exceptions, and those past their expiry date | Monthly | Governance |
| | Evidence completeness | Controls with current evidence in the evidence map ÷ controls in scope | Monthly | Governance |
| | Repeat findings | Findings recurring from a previous cycle ÷ total findings | Per assurance cycle | Governance |
| **Cost** | Cost per system | Total run cost (compute, API, licences, support) attributed to the system, per period | Monthly | Finance + technical owner |
| | Unit cost | Cost per 1,000 inferences or per business transaction, trended | Monthly | Finance + technical owner |
| | Forecast variance | Actual vs forecast cost, with the main driver named | Monthly | Finance |
| **Value** | Realised benefit | Measured benefit against the baseline recorded at approval | Quarterly | Business owner |
| | Value attribution confidence | Stated confidence in the attribution (measured / modelled / estimated) — a required field, not a footnote | Quarterly | Business owner |
| | Adoption of AI-assisted workflow | Share of eligible transactions or users actually using the AI capability | Monthly | Business owner |
| **Data** | Data quality pass rate | Automated quality checks passing ÷ checks run, by dataset | Daily | Data owner |
| | Lineage coverage | Production models with complete lineage records ÷ all production models | Monthly | Data owner |
| | Deletion compliance | Deletion requests completed within the required period ÷ requests received | Monthly | Data owner |
| **People** | Capability coverage | Roles meeting their defined AI capability requirement ÷ roles in scope | Quarterly | Change Agent |
| | Training currency | Staff with current required training ÷ staff in scope | Monthly | Change Agent |

**Rules for using this library**:
- Adopt a subset. Twenty monitored measures with owners beat sixty on a wall.
- Every measure must have a named owner and a written definition before it appears in a governance forum.
- Report leading and lagging measures together; a dashboard of only lagging indicators tells you what has already gone wrong.

### Predictive Analytics Cookbook

Recipes for the four predictive questions a Maturity Level 4 AI operation actually asks. Each one states what it needs, what it gives you, and where it can mislead you.

| # | Question | Inputs | Method | Output | Where it misleads |
|---|---|---|---|---|---|
| 1 | **Which system will breach its performance threshold next?** | Time series of task accuracy and drift measures per system; threshold definitions | Trend extrapolation with change-point detection; compare against the system's own history, not the portfolio's | Ranked list of systems with expected breach date and confidence | Seasonal business cycles read as drift; a change in data collection looks identical to a change in the world |
| 2 | **Which model should be retrained first?** | Drift measures, retraining history, incident history, cost to retrain | Score by risk exposure × drift severity ÷ cost to retrain; validate against last quarter's incidents | Ordered retraining queue | Retraining on drifted data launders the drift into the training set; always validate on a held-out, current window |
| 3 | **Where will cost exceed budget next quarter?** | Cost per system per period, volume forecasts, provider price changes | Driver-based forecast (volume × unit cost) with a scenario band | Per-system forecast with variance band and the driver that dominates | Provider price and model-mix changes invalidate history-based unit costs; re-estimate after any model change |
| 4 | **Which controls are drifting toward non-compliance?** | Review backlog age, exception accumulation, evidence gaps, training currency | Composite leading-indicator score with thresholds set from prior findings | Controls ranked by predicted finding risk | The indicator becomes a target and stops measuring anything (Goodhart); rotate and re-validate annually |
| 5 | **Which incident class is growing?** | Incident records with class, severity, system, cause | Rate-of-change analysis on class-level counts; separate systemic causes from noise | Growing classes with the underlying systems named | Small counts produce volatile rates; require a minimum count before acting |

**Discipline that makes any of these usable**: record the forecast, record the outcome, and publish the hit rate. A predictive capability without a published accuracy track record is a narrative, and at Maturity Level 4 the whole point is that the narrative can be checked.

### Dashboard Templates

Each template below states the audience, the refresh rate, the measures (by name from the library above), and the decision it is meant to support. A dashboard with no decision attached should be retired — see the Change Agent playbook, Action 4.

**Executive / board dashboard**
- **Refresh**: Monthly (with a daily operational view available for incidents)
- **Measures**: Risk appetite breach count; incidents per system; early-detection rate; realised benefit vs baseline; forecast variance; evidence completeness; repeat findings
- **Decision supported**: Whether the AI portfolio is within appetite, and where to reallocate
- **Sample query shape** (illustrative, warehouse-neutral):
  `SELECT measure, period, value, target, variance FROM ai_metrics WHERE audience = 'board' AND period >= :last_12_months ORDER BY measure, period`

**Operational dashboard (AI/ML teams)**
- **Refresh**: Real time
- **Measures**: Service reliability; latency percentiles; task accuracy; input and output drift; alert volume and precision; retraining currency
- **Decision supported**: Whether to intervene now on a specific system
- **Query shape**: `SELECT system, metric, window_end, value FROM ai_system_metrics WHERE system = :system AND window_end >= now() - interval '24 hours'`

**Governance dashboard (risk/compliance)**
- **Refresh**: Daily
- **Measures**: Time-to-approval by tier; review backlog age; exception volume and expiry; evidence completeness; control test failure rate; repeat findings; training currency
- **Decision supported**: Where governance is the bottleneck, and which controls need attention
- **Query shape**: `SELECT control, tier, tests_run, tests_failed, last_tested FROM control_tests WHERE cycle = :current_cycle`

**Business value dashboard (product/business owners)**
- **Refresh**: Weekly
- **Measures**: Realised benefit vs baseline; value attribution confidence; adoption of AI-assisted workflow; unit cost; experiment results and decisions
- **Decision supported**: Whether to scale, re-scope or stop a capability
- **Query shape**: `SELECT initiative, baseline_value, measured_value, attribution_confidence, period FROM ai_value WHERE initiative = :initiative`

**Chart hygiene that stops a dashboard lying**: fixed axis scales on trend charts; always show the comparison period; label the sample size; show the definition and limitation (hover or footnote) on every measure; never show a percentage without its denominator.

---

## Conclusion: Your Journey from Maturity Level 3 to Maturity Level 4

You've built systematic, enterprise-wide AI governance at Maturity Level 3. Now you're making it **intelligent and predictive** at Maturity Level 4.

This is the transition from **control** to **optimization**. From **knowing what happened** to **predicting what will happen** and **automatically improving**.

By achieving Maturity Level 4, you:
- **Prevent incidents** instead of just detecting them
- **Optimize resources** based on measured value and risk
- **Accelerate innovation** through data-driven feedback loops
- **Demonstrate value** quantitatively to all stakeholders

**You're moving from elite (Maturity Level 3) to cutting-edge (Maturity Level 4)**. Welcome to the frontier.

---

**Return to**: [Assessment Method](../AIMF-ASSESSMENT-GUIDE.md) | [Maturity Levels](../AIMF-MATURITY-LEVELS.md) | [Maturity Level 2→3 Guide](MATURITY-LEVEL-2-TO-3-GUIDE.md)
**Next Guide**: [Maturity Level 4→5 Implementation Guide](MATURITY-LEVEL-4-TO-5-GUIDE.md) (use when you've solidified Maturity Level 4)
