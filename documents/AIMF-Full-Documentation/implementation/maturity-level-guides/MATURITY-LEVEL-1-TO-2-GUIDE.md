# AI Management Framework (AIMF) by PraeSyn
## Maturity Level 1→2 Implementation Guide
### From Ad-Hoc AI Usage to Foundational Structure

**© 2026 PraeSyn, LLC. All rights reserved.**
Licensed under CC BY-NC-ND 4.0

**Target Audience**: Organizations at **Maturity Level 1 (Initial)** working toward **Maturity Level 2 (Developing)**
**Version**: 1.0
**Publication Date**: January 29, 2026
**Status**: Pre-Publication (Working Draft)
**Date**: 2025-10-23

---

## Executive Summary

**Current State**: Your organization is at Maturity Level 1 - AI usage is ad-hoc, uncoordinated, and largely ungoverned. Teams may be experimenting with AI tools, but there's no central visibility, documentation, or oversight.

**Target State**: Maturity Level 2 - Establish foundational structure with documented policies, assigned responsibilities, and emerging organizational awareness. Not perfection, but **visibility and control**.

**Timeline**: **6-12 months** to solidly achieve Maturity Level 2 (varies by organizational size and maturity)

**Investment Level**: **Moderate**
- 0.5-1 FTE dedicated to AI governance/coordination
- $50-150K in tools and infrastructure (depending on existing capabilities)
- 10-20% time allocation from key stakeholders (leadership, technical leads, risk/compliance)

**Key Priorities**:
1. **Visibility**: Create inventory of AI usage across organization
2. **Governance Foundation**: Establish basic AI governance structure and policies
3. **Technical Foundation**: Document AI development and deployment processes
4. **Risk Awareness**: Identify and begin tracking AI-related risks

**Success Indicator**: Within 12 months, you can answer "Who is using AI?", "What are they using it for?", "Who's responsible for oversight?", and "What policies apply?"

---

## 1. Current State Context: Understanding Maturity Level 1

### Where You Are and Why That's Okay

**You're at Maturity Level 1 if**:
- AI usage exists but is **undocumented and uncoordinated**
- No central inventory of AI tools or models in use
- Teams are experimenting with ChatGPT, AI coding assistants, or building models, but **each team doing their own thing**
- No AI-specific policies or governance structure
- Leadership knows "AI is happening" but lacks visibility into **where, how, and with what risks**
- AI projects succeed or fail based on individual initiative, not organizational process

**This is normal**. Most organizations start here. You're not behind - you're **beginning a journey** that most of your competitors haven't even started.

### Common Maturity Level 1 Scenarios

**Scenario A: Shadow AI**
Teams are using AI tools (ChatGPT, Copilot, Claude) without IT or leadership knowing. Productivity gains happen, but risks accumulate invisibly.

**Scenario B: Pilot Paralysis**
Several AI pilots have run successfully, but none moved to production. Each pilot was treated as a one-off experiment with no lessons captured for reuse.

**Scenario C: Data Science Isolation**
A small data science team builds models, but they're disconnected from IT operations, data governance, and business stakeholders. Models sit unused or deployment is manual and fragile.

**Scenario D: Early Adopter Chaos**
Your organization actively encourages AI experimentation ("everyone should try AI!"), but with no guard rails. Innovation is happening, but risks and coordination are lacking.

### Why Organizations Are at Maturity Level 1

**It's not lack of talent or ambition**. Maturity Level 1 is typically caused by:

1. **Speed of AI Evolution**: AI capabilities evolved faster than governance could keep up
2. **Lack of Precedent**: Your organization's existing IT, risk, and compliance frameworks weren't designed for AI
3. **Distributed Innovation**: AI tools are accessible to anyone (not just IT), making central control harder
4. **Organizational Maturity**: If your broader organization operates at Maturity Level 1-2 maturity (ad-hoc processes, limited documentation), AI will mirror that
5. **Resource Constraints**: Governance and structure require dedicated people and time you may not have had

**None of this is your fault**. But it is your **opportunity**.

---

## 2. The Case for Change: Why Move to Maturity Level 2?

### Risks of Remaining at Maturity Level 1

If your organization stays at Maturity Level 1 indefinitely, you face accumulating risks:

**Compliance & Legal Risks**:
- **Regulatory exposure**: AI regulations (EU AI Act, state-level AI laws) require governance. Ad-hoc AI won't pass audits.
- **Liability**: When an AI system causes harm (bias, error, privacy breach), who's responsible? At Maturity Level 1, accountability is unclear.
- **Contractual risk**: Customers or partners may require AI governance certification (ISO 42001, SOC 2 AI controls). You can't provide it.

**Operational Risks**:
- **Undetected failures**: Models degrade in production and no one notices until customer impact
- **Technical debt**: Ad-hoc AI creates "AI spaghetti" that's expensive to maintain or replace
- **Vendor lock-in**: Teams adopt tools without enterprise evaluation, creating fragmented vendor relationships

**Business Risks**:
- **Missed opportunities**: Without coordination, teams duplicate efforts or miss adjacent use cases
- **Competitive disadvantage**: Competitors who govern AI can scale it confidently; you're stuck in pilot mode
- **Talent attrition**: Good AI practitioners want structure and support, not chaos

**Reputational Risks**:
- **AI incidents**: Bias, hallucinations, or privacy breaches make headlines. Maturity Level 1 organizations can't demonstrate due diligence.
- **Stakeholder distrust**: Board, customers, or employees lose confidence in organization's AI capability

### Challenges You'll Face Moving to Maturity Level 2

**Let's be honest about what's hard**:

1. **Organizational Maturity Friction**
   - If your org struggles with basic documentation and process in general, adding AI governance won't be easy
   - Requires discipline your culture may not naturally have
   - **Mitigation**: Start small. Document one AI use case thoroughly to prove value.

2. **Resource Scarcity**
   - You need dedicated people (at least 0.5 FTE) to drive this
   - Budget for tools may compete with feature development
   - **Mitigation**: Frame as risk mitigation, not just "nice to have." Quantify current risks in dollar terms.

3. **Resistance to "Bureaucracy"**
   - Teams currently moving fast may see governance as slowing them down
   - "We don't have time for paperwork" mentality
   - **Mitigation**: Emphasize that Maturity Level 2 is lightweight structure, not enterprise bureaucracy. Show how visibility reduces duplicate work.

4. **Ambiguity About AI**
   - What counts as "AI"? Does Excel =FORECAST() count? What about rules engines?
   - **Mitigation**: Start with obviously-AI systems (ML models, LLMs, GenAI) and expand scope later.

5. **Skills and Knowledge Gaps**
   - Your team may not know what "good" AI governance looks like
   - Legal, risk, and compliance teams may not understand AI risks
   - **Mitigation**: Invest in education (workshops, bringing in experts, industry associations).

6. **Executive Skepticism**
   - Leadership may not see the urgency if no AI incident has happened yet
   - "Why invest in governance when we're still figuring out if AI is valuable?"
   - **Mitigation**: Present case studies of AI failures. Emphasize that governance enables scaling, not just prevents harm.

### Time Realities

**Some things happen quickly** (1-3 months):
- Creating an AI inventory
- Drafting an AI acceptable use policy
- Appointing an interim AI governance lead
- Running a risk assessment workshop

**Some things take longer** (6-12 months):
- Building stakeholder buy-in across organization
- Documenting existing technical processes
- Training teams on new policies
- Establishing regular governance meetings and rhythms
- Seeing behavior change become habitual

**Don't expect overnight transformation**. Maturity Level 1→2 is measured in quarters, not weeks. That's normal and okay.

---

## 3. Target State Vision: What Maturity Level 2 and Maturity Level 3 Look Like

### Maturity Level 2 (Your Immediate Goal): Foundational Structure

**You'll know you've reached Maturity Level 2 when**:

✅ **Visibility**
- You have an **inventory** of AI systems in use (even if incomplete)
- You know who's responsible for each AI system or use case
- Executive leadership receives regular AI updates (at least quarterly)

✅ **Governance Foundation**
- You have **documented AI policies** (even if simple)
  - AI acceptable use policy
  - AI ethics principles or guidelines
  - High-level AI risk management approach
- An **AI governance committee or working group** meets regularly (at least quarterly)
- Roles and responsibilities for AI oversight are assigned (even if shared with other duties)

✅ **Technical Foundation**
- AI development and deployment processes are **documented** (even if not automated)
- Basic data quality checks are performed
- You know where training data comes from and have basic lineage
- Model changes are tracked (even if in spreadsheets or wikis)

✅ **Risk Awareness**
- You've conducted at least one **AI risk assessment**
- High-risk AI systems are identified and tracked differently
- Basic incident response plan exists (even if not tested)

**Maturity Level 2 is not perfection**. It's **"we have a system, even if it's still maturing."** Policies may be followed inconsistently. Processes may be manual. But the foundation exists.

### Maturity Level 3 (The Future Vision): Enterprise Standards

**Looking ahead to Maturity Level 3** (18-36 months from now):

At Maturity Level 3, what's documented at Maturity Level 2 becomes **standardized and organization-wide**:
- AI governance is **embedded** in organization's risk and compliance frameworks
- AI systems follow enterprise-wide standards (model cards, documentation templates, deployment checklists)
- **MLOps platforms** automate deployment, monitoring, and governance
- AI training is part of onboarding for all relevant roles
- Regular audits confirm policy compliance

**Why show you Maturity Level 3 now?** Because when you're convincing stakeholders to invest in Maturity Level 2, you'll need to paint the **long-term vision**. Maturity Level 2 is the foundation for Maturity Level 3 scalability.

---

## 4. Communication Strategy for Implementation Leaders

### Your Challenge as the Change Agent

As the person driving this maturity progression, you need to:
- **Be clear** about what Maturity Level 2 requires (foundational structure)
- **Articulate benefits** of Maturity Level 2 (visibility, reduced risk, scalability foundation)
- **Paint the vision** of Maturity Level 3 (enterprise standards, automation, competitive advantage)
- **Never confuse** Maturity Level 2 requirements with Maturity Level 3 requirements when asking for resources or action

### How to Talk About Maturity Level 2 Requirements

**With Executives**:
- ❌ Don't say: "We need enterprise-wide AI standards and MLOps platforms"
- ✅ Do say: "We need to establish foundational AI governance - policies, inventory, and assigned responsibilities - as the first step toward scaling AI safely."

**With Technical Teams**:
- ❌ Don't say: "We're implementing full MLOps automation now"
- ✅ Do say: "We need to document our current AI development process so we can identify what to improve and automate later."

**With Risk/Compliance**:
- ❌ Don't say: "We need comprehensive AI audit frameworks"
- ✅ Do say: "We need to conduct our first AI risk assessment and create a basic tracking system."

### How to Use Maturity Level 3 Vision

**Maturity Level 3 is your "North Star"** for stakeholder buy-in:

"Right now [Maturity Level 2], we need to document our AI policies and create an inventory. This lays the foundation so that in 2-3 years [Maturity Level 3], we can scale AI across the enterprise with automated governance and enterprise-wide standards. Companies that skip the foundation work end up with technical debt and governance gaps that slow them down later."

**Frame Maturity Level 2 as enabling Maturity Level 3**, not as the end goal. But be honest that Maturity Level 2 is the current focus.

### Handling Resistance

**Resistance Type**: "Governance will slow us down"
**Response**: "Maturity Level 2 is lightweight - we're talking about documenting what you're already doing, not adding heavy process. The goal is visibility, not bureaucracy. Later [Maturity Level 3], we'll automate governance so it's invisible."

**Resistance Type**: "We need to focus on business value, not governance"
**Response**: "Governance enables business value. Without an AI inventory and basic oversight [Maturity Level 2], we can't scale AI to more use cases. We're building the foundation for enterprise-wide AI [Maturity Level 3 vision], which is where the big business value is."

**Resistance Type**: "We don't have the resources"
**Response**: "Maturity Level 2 requires 0.5-1 FTE and modest budget. Not doing this means our AI risks keep growing invisibly. We're either going to invest in governance proactively [Maturity Level 2] or pay for an AI incident reactively. The proactive path is cheaper."

---

## 5. Multi-Audience Assessments

### How to Use These Assessments

Before starting implementation, have each audience complete their assessment independently:
- **Leadership**: Focus on governance and oversight capabilities
- **Technical**: Focus on AI system development and deployment
- **Governance**: Focus on policies, controls, and risk management
- **Change Agent** (you): Focus on organizational readiness and culture

Each question is scored on the canonical **0-4 point scale / ML1-ML5** used throughout the framework (see `../AIMF-ASSESSMENT-GUIDE.md`):

- **0 = ML1 - Initial**: Capability doesn't exist, or exists informally and undocumented
- **1 = ML2 - Developing**: Documented but inconsistent
- **2 = ML3 - Defined**: Organization-wide and consistent
- **3 = ML4 - Managed**: All of ML3, plus quantitative metrics tracked and reviewed
- **4 = ML5 - Optimizing**: All of ML4, plus systematic continuous improvement

**Maturity Level 2 Target**: Most questions should score **1** (ML2 - Developing). A few may score 0 (still working on documentation). Scores of 2 or higher mean the organization is already past this guide's target on that question.

If most questions currently score 0 (ML1), you're solidly Maturity Level 1 and this guide is right for you.

> **Scale note**: the retired 0-3 lens scored this quiz 0-3 with "3 = Established". Under the
> canonical scale "Established, organization-wide" is ML3 = **2**, which is why the ML2 target
> above is **1**, not 2. Old quiz notes convert with the table in `../AIMF-ASSESSMENT-GUIDE.md`.

---

### Leadership Assessment (Maturity Level 1 Baseline)

**Instructions for Leadership**: Rate your organization's current state (not plans) on AI governance and oversight.

#### L1. AI Strategy and Prioritization

**Question**: Has leadership established an organizational AI strategy that identifies priority use cases and resource allocation?

**Scoring Rubric**:
- **Score 0 (ML1 - Initial)**: No AI strategy. AI use is uncoordinated and ad-hoc. At most informal discussions about AI priorities, but no documented strategy.
- **Score 1 (ML2 - Developing)**: AI strategy documented, but not yet communicated organization-wide or under active review.
- **Score 2 (ML3 - Defined)**: AI strategy documented, communicated, and guides resource allocation decisions.
- **Score 3 (ML4 - Managed)**: All of the above, plus tracked quantitative metrics on this capability, reviewed on a defined cadence and used in decisions.
- **Score 4 (ML5 - Optimizing)**: All of ML4, plus systematic continuous improvement of this capability, with external benchmarking or recognized industry leadership.

**Evidence to Look For**: Strategy document, executive presentation, resource allocation decisions tied to AI priorities

**Your Score**: ___ (0-4)
**Notes**:

---

#### L2. AI Governance Structure

**Question**: Has the organization established governance structures (committee, working group, or designated role) for AI oversight?

**Scoring Rubric**:
- **Score 0 (ML1 - Initial)**: No AI governance structure. No one is formally responsible for AI oversight. At most informal accountability (someone cares about AI governance), but no formal structure or charter.
- **Score 1 (ML2 - Developing)**: Governance structure exists (committee or role) with charter, but meetings are inconsistent or attendance is poor.
- **Score 2 (ML3 - Defined)**: Governance structure meets regularly with consistent attendance and documented decisions.
- **Score 3 (ML4 - Managed)**: All of the above, plus tracked quantitative metrics on this capability, reviewed on a defined cadence and used in decisions.
- **Score 4 (ML5 - Optimizing)**: All of ML4, plus systematic continuous improvement of this capability, with external benchmarking or recognized industry leadership.

**Evidence to Look For**: Charter document, meeting calendar, meeting minutes, role descriptions

**Your Score**: ___ (0-4)
**Notes**:

---

#### L3. Resource Allocation for AI

**Question**: Has leadership allocated dedicated budget and FTE for AI capabilities (not just AI projects, but the infrastructure and governance)?

**Scoring Rubric**:
- **Score 0 (ML1 - Initial)**: No dedicated AI resources. AI work happens in spare time or within project budgets. At most informal resource allocation (borrowed time from other roles), but not dedicated in budget.
- **Score 1 (ML2 - Developing)**: Budget allocated for AI, but FTE assignments are partial or shared.
- **Score 2 (ML3 - Defined)**: Dedicated AI budget and at least 0.5 FTE formally assigned to AI program management or governance.
- **Score 3 (ML4 - Managed)**: All of the above, plus tracked quantitative metrics on this capability, reviewed on a defined cadence and used in decisions.
- **Score 4 (ML5 - Optimizing)**: All of ML4, plus systematic continuous improvement of this capability, with external benchmarking or recognized industry leadership.

**Evidence to Look For**: Budget line items, job descriptions, org chart showing AI roles

**Your Score**: ___ (0-4)
**Notes**:

---

#### L4. AI Accountability

**Question**: Are there clear accountability structures for AI system outcomes (success, failure, incidents)?

**Scoring Rubric**:
- **Score 0 (ML1 - Initial)**: No one is accountable for AI outcomes. It's unclear who would be responsible if an AI system caused harm. At most implicit accountability (team that built it is probably responsible), but not documented.
- **Score 1 (ML2 - Developing)**: Accountability is documented for some AI systems, but not consistently applied.
- **Score 2 (ML3 - Defined)**: All AI systems have documented owners/sponsors who are accountable for outcomes.
- **Score 3 (ML4 - Managed)**: All of the above, plus tracked quantitative metrics on this capability, reviewed on a defined cadence and used in decisions.
- **Score 4 (ML5 - Optimizing)**: All of ML4, plus systematic continuous improvement of this capability, with external benchmarking or recognized industry leadership.

**Evidence to Look For**: System ownership records, incident response plan with escalation paths, RACI matrix

**Your Score**: ___ (0-4)
**Notes**:

---

#### L5. AI Risk Awareness

**Question**: Does leadership regularly receive updates on AI-related risks and incidents?

**Scoring Rubric**:
- **Score 0 (ML1 - Initial)**: Leadership receives no AI risk information. Risks are invisible. At most AI risks mentioned informally in meetings, but no structured reporting.
- **Score 1 (ML2 - Developing)**: Risk reporting exists but is infrequent (less than quarterly) or inconsistent in format.
- **Score 2 (ML3 - Defined)**: Structured AI risk reporting to leadership occurs at least quarterly with consistent format.
- **Score 3 (ML4 - Managed)**: All of the above, plus tracked quantitative metrics on this capability, reviewed on a defined cadence and used in decisions.
- **Score 4 (ML5 - Optimizing)**: All of ML4, plus systematic continuous improvement of this capability, with external benchmarking or recognized industry leadership.

**Evidence to Look For**: Executive dashboard, board/leadership meeting agenda items, risk register

**Your Score**: ___ (0-4)
**Notes**:

---

#### L6. Stakeholder Engagement

**Question**: Does leadership actively engage with external stakeholders (customers, partners, regulators) on AI trust and transparency?

**Scoring Rubric**:
- **Score 0 (ML1 - Initial)**: No external engagement on AI. Organization doesn't communicate about AI practices. At most ad-hoc responses to customer questions, but no proactive transparency.
- **Score 1 (ML2 - Developing)**: Some transparency (website disclosures, FAQs), but not comprehensive or regularly updated.
- **Score 2 (ML3 - Defined)**: Regular external communication about AI practices, policies, and principles.
- **Score 3 (ML4 - Managed)**: All of the above, plus tracked quantitative metrics on this capability, reviewed on a defined cadence and used in decisions.
- **Score 4 (ML5 - Optimizing)**: All of ML4, plus systematic continuous improvement of this capability, with external benchmarking or recognized industry leadership.

**Evidence to Look For**: Public AI transparency page, customer-facing AI documentation, regulatory filings

**Your Score**: ___ (0-4)
**Notes**:

---

**Leadership Assessment Total**: ___/24 points
**Leadership Score**: (Total/24) × 100 = ___%

**Interpretation**:
- **0-24%** (average ML1 - Initial): Significant leadership gaps - AI governance not yet prioritized
- **25-49%** (average ML2 - Developing): Early leadership awareness - commitment emerging
- **50-74%** (average ML3 - Defined): Developing leadership support - structure taking shape
- **75-100%** (average ML4 - Managed or above): Strong leadership foundation - ready for Maturity Level 3

---

### Technical Assessment (Maturity Level 1 Baseline)

**Instructions for Technical Teams**: Rate your current AI/ML development and deployment practices.

#### T1. AI System Inventory

**Question**: Does the organization maintain an inventory of AI systems in use (including models, tools, and SaaS AI services)?

**Framework Mapping**: NIST AI RMF MAP 1.1

**Scoring Rubric**:
- **Score 0 (ML1 - Initial)**: No inventory. Organization doesn't know what AI systems are in use. At most informal awareness (people know what they're using), but no centralized list or database.
- **Score 1 (ML2 - Developing)**: Inventory exists and is documented, but it's incomplete or not regularly updated.
- **Score 2 (ML3 - Defined)**: Comprehensive, maintained AI inventory with regular updates and completeness validation.
- **Score 3 (ML4 - Managed)**: All of the above, plus tracked quantitative metrics on this capability, reviewed on a defined cadence and used in decisions.
- **Score 4 (ML5 - Optimizing)**: All of ML4, plus systematic continuous improvement of this capability, with external benchmarking or recognized industry leadership.

**Evidence to Look For**: Inventory spreadsheet/database, update process, validation procedures

**Your Score**: ___ (0-4)
**Notes**:

---

#### T2. AI Development Process Documentation

**Question**: Are AI/ML development processes documented (requirements, design, testing, validation)?

**Framework Mapping**: ISO 42001 Clause 8, NIST AI RMF GOVERN 1.1

**Scoring Rubric**:
- **Score 0 (ML1 - Initial)**: No documented process. Each team/individual follows their own approach. At most some teams have documented their process informally (wikis, READMEs), but no org-wide standard.
- **Score 1 (ML2 - Developing)**: Organization-wide process documented, but adoption is inconsistent.
- **Score 2 (ML3 - Defined)**: Documented process followed consistently with enforcement mechanisms (code reviews, checklists).
- **Score 3 (ML4 - Managed)**: All of the above, plus tracked quantitative metrics on this capability, reviewed on a defined cadence and used in decisions.
- **Score 4 (ML5 - Optimizing)**: All of ML4, plus systematic continuous improvement of this capability, with external benchmarking or recognized industry leadership.

**Evidence to Look For**: Process documentation, templates, completed examples from recent projects

**Your Score**: ___ (0-4)
**Notes**:

---

#### T3. Data Management for AI

**Question**: Are there documented processes for managing training data (sourcing, quality, lineage, versioning)?

**Framework Mapping**: ISO 42001 Clause 8.2, NIST AI RMF MAP 3.2

**Scoring Rubric**:
- **Score 0 (ML1 - Initial)**: No data management process. Data is ad-hoc and undocumented. At most teams track their own data informally, but no standardized approach.
- **Score 1 (ML2 - Developing)**: Data management processes documented, but tooling and compliance are inconsistent.
- **Score 2 (ML3 - Defined)**: Standardized data management with tooling support and regular audits.
- **Score 3 (ML4 - Managed)**: All of the above, plus tracked quantitative metrics on this capability, reviewed on a defined cadence and used in decisions.
- **Score 4 (ML5 - Optimizing)**: All of ML4, plus systematic continuous improvement of this capability, with external benchmarking or recognized industry leadership.

**Evidence to Look For**: Data catalog, data lineage documentation, data quality metrics

**Your Score**: ___ (0-4)
**Notes**:

---

#### T4. Model Deployment Process

**Question**: Is there a documented process for deploying AI models to production (testing, approval, deployment)?

**Framework Mapping**: NIST AI RMF MANAGE 2.3

**Scoring Rubric**:
- **Score 0 (ML1 - Initial)**: No deployment process. Models move to production ad-hoc or don't make it to production at all. At most teams have informal deployment practices, but no documented standard.
- **Score 1 (ML2 - Developing)**: Deployment process documented, but not yet automated or consistently followed.
- **Score 2 (ML3 - Defined)**: Deployment process documented and consistently followed, with approvals and gating.
- **Score 3 (ML4 - Managed)**: All of the above, plus tracked quantitative metrics on this capability, reviewed on a defined cadence and used in decisions.
- **Score 4 (ML5 - Optimizing)**: All of ML4, plus systematic continuous improvement of this capability, with external benchmarking or recognized industry leadership.

**Evidence to Look For**: Deployment checklists, approval workflows, deployment logs

**Your Score**: ___ (0-4)
**Notes**:

---

#### T5. Model Monitoring

**Question**: Are AI models monitored in production for performance, accuracy, and drift?

**Framework Mapping**: NIST AI RMF MEASURE 2.1, 2.11

**Scoring Rubric**:
- **Score 0 (ML1 - Initial)**: No monitoring. Once deployed, models run until they break visibly. At most ad-hoc monitoring (someone checks occasionally), but no systematic approach.
- **Score 1 (ML2 - Developing)**: Monitoring implemented for some models, but not all, and alerts may not be actionable.
- **Score 2 (ML3 - Defined)**: Systematic monitoring for all production models with alerting and response procedures.
- **Score 3 (ML4 - Managed)**: All of the above, plus tracked quantitative metrics on this capability, reviewed on a defined cadence and used in decisions.
- **Score 4 (ML5 - Optimizing)**: All of ML4, plus systematic continuous improvement of this capability, with external benchmarking or recognized industry leadership.

**Evidence to Look For**: Monitoring dashboards, alerting configuration, incident response logs

**Your Score**: ___ (0-4)
**Notes**:

---

#### T6. Model Documentation

**Question**: Are AI models documented (purpose, architecture, training data, performance, limitations)?

**Framework Mapping**: NIST AI RMF GOVERN 1.6, MAP 5.1

**Scoring Rubric**:
- **Score 0 (ML1 - Initial)**: No model documentation beyond code comments, if that. At most some documentation exists (READMEs, notebooks), but inconsistent and incomplete.
- **Score 1 (ML2 - Developing)**: Documentation standard exists (model cards or similar), but adoption is inconsistent.
- **Score 2 (ML3 - Defined)**: All models have standardized documentation created as part of development workflow.
- **Score 3 (ML4 - Managed)**: All of the above, plus tracked quantitative metrics on this capability, reviewed on a defined cadence and used in decisions.
- **Score 4 (ML5 - Optimizing)**: All of ML4, plus systematic continuous improvement of this capability, with external benchmarking or recognized industry leadership.

**Evidence to Look For**: Model card examples, documentation templates, repository standards

**Your Score**: ___ (0-4)
**Notes**:

---

#### T7. Version Control and Reproducibility

**Question**: Are models, code, and data versioned to enable reproducibility?

**Framework Mapping**: ISO 42001 Clause 8.5

**Scoring Rubric**:
- **Score 0 (ML1 - Initial)**: No version control. Can't reproduce past model versions. At most code is versioned (Git), but data and models are not consistently tracked.
- **Score 1 (ML2 - Developing)**: Code, data, and models are versioned, but reproducibility is not regularly validated.
- **Score 2 (ML3 - Defined)**: Full version control with validated reproducibility (can recreate any production model).
- **Score 3 (ML4 - Managed)**: All of the above, plus tracked quantitative metrics on this capability, reviewed on a defined cadence and used in decisions.
- **Score 4 (ML5 - Optimizing)**: All of ML4, plus systematic continuous improvement of this capability, with external benchmarking or recognized industry leadership.

**Evidence to Look For**: Git repositories, data versioning system, model registry

**Your Score**: ___ (0-4)
**Notes**:

---

#### T8. AI Testing and Validation

**Question**: Are AI models tested for performance, bias, robustness, and security before deployment?

**Framework Mapping**: NIST AI RMF MEASURE 2.1-2.13

**Scoring Rubric**:
- **Score 0 (ML1 - Initial)**: No testing beyond basic accuracy on training data. At most some testing (accuracy, basic performance), but not systematic or comprehensive.
- **Score 1 (ML2 - Developing)**: Testing framework documented (what to test, acceptance criteria), but not consistently applied.
- **Score 2 (ML3 - Defined)**: Comprehensive testing consistently applied with documented results and approval gates.
- **Score 3 (ML4 - Managed)**: All of the above, plus tracked quantitative metrics on this capability, reviewed on a defined cadence and used in decisions.
- **Score 4 (ML5 - Optimizing)**: All of ML4, plus systematic continuous improvement of this capability, with external benchmarking or recognized industry leadership.

**Evidence to Look For**: Test plans, test results, bias assessment reports, security scan results

**Your Score**: ___ (0-4)
**Notes**:

---

#### T9. Incident Response for AI

**Question**: Is there a defined process for responding to AI system failures or incidents?

**Framework Mapping**: NIST AI RMF MANAGE 4.1-4.3

**Scoring Rubric**:
- **Score 0 (ML1 - Initial)**: No incident response plan. Issues are handled reactively with no process. At most teams handle incidents informally, but no documented process or escalation path.
- **Score 1 (ML2 - Developing)**: Incident response process documented, but not tested or regularly updated.
- **Score 2 (ML3 - Defined)**: Incident response process documented, tested, and integrated with broader IT incident management.
- **Score 3 (ML4 - Managed)**: All of the above, plus tracked quantitative metrics on this capability, reviewed on a defined cadence and used in decisions.
- **Score 4 (ML5 - Optimizing)**: All of ML4, plus systematic continuous improvement of this capability, with external benchmarking or recognized industry leadership.

**Evidence to Look For**: Incident response playbook, recent incident records, tabletop exercise results

**Your Score**: ___ (0-4)
**Notes**:

---

#### T10. AI/ML Skills and Training

**Question**: Does the organization provide training on AI/ML best practices, responsible AI, and relevant tools?

**Framework Mapping**: ISO 42001 Clause 7.2

**Scoring Rubric**:
- **Score 0 (ML1 - Initial)**: No AI/ML training provided. Skills developed through individual initiative only. At most informal knowledge sharing (lunch-and-learns, Slack channels), but no structured training.
- **Score 1 (ML2 - Developing)**: Training program exists (courses, workshops), but participation is optional and inconsistent.
- **Score 2 (ML3 - Defined)**: Structured training program with required courses for AI practitioners and broad awareness training for others.
- **Score 3 (ML4 - Managed)**: All of the above, plus tracked quantitative metrics on this capability, reviewed on a defined cadence and used in decisions.
- **Score 4 (ML5 - Optimizing)**: All of ML4, plus systematic continuous improvement of this capability, with external benchmarking or recognized industry leadership.

**Evidence to Look For**: Training curriculum, completion records, onboarding materials

**Your Score**: ___ (0-4)
**Notes**:

---

**Technical Assessment Total**: ___/40 points
**Technical Score**: (Total/40) × 100 = ___%

**Interpretation**:
- **0-24%** (average ML1 - Initial): Significant technical gaps - foundational MLOps work needed
- **25-49%** (average ML2 - Developing): Early technical practices - documentation and process emerging
- **50-74%** (average ML3 - Defined): Developing technical capability - ready to scale with tooling
- **75-100%** (average ML4 - Managed or above): Strong technical foundation - ready for automation and enterprise standards

---

### Governance Assessment (Maturity Level 1 Baseline)

**Instructions for Governance/Compliance Teams**: Rate your organization's AI governance policies and controls.

#### G1. AI Policy Framework

**Question**: Does the organization have documented AI policies (acceptable use, ethics principles, risk management approach)?

**Framework Mapping**: ISO 42001 Clause 5.2, NIST AI RMF GOVERN 1.1

**Scoring Rubric**:
- **Score 0 (ML1 - Initial)**: No AI-specific policies exist. General IT policies may apply but aren't tailored for AI. At most some AI policy thinking has occurred (principles drafted), but nothing formally approved.
- **Score 1 (ML2 - Developing)**: AI policies documented and approved, but not yet communicated organization-wide or enforced.
- **Score 2 (ML3 - Defined)**: AI policies documented, communicated, and actively enforced with compliance checks.
- **Score 3 (ML4 - Managed)**: All of the above, plus tracked quantitative metrics on this capability, reviewed on a defined cadence and used in decisions.
- **Score 4 (ML5 - Optimizing)**: All of ML4, plus systematic continuous improvement of this capability, with external benchmarking or recognized industry leadership.

**Evidence to Look For**: Policy documents, approval records, policy acknowledgment tracking

**Your Score**: ___ (0-4)
**Notes**:

---

#### G2. AI Risk Assessment

**Question**: Has the organization conducted an AI-specific risk assessment?

**Framework Mapping**: ISO 42001 Clause 6.1, NIST AI RMF MAP function

**Scoring Rubric**:
- **Score 0 (ML1 - Initial)**: No AI risk assessment conducted. AI risks are not formally identified. At most AI risks have been discussed informally, but no structured assessment.
- **Score 1 (ML2 - Developing)**: AI risk assessment conducted once, but not yet integrated into ongoing risk management.
- **Score 2 (ML3 - Defined)**: AI risk assessment conducted and integrated into regular enterprise risk management cycles.
- **Score 3 (ML4 - Managed)**: All of the above, plus tracked quantitative metrics on this capability, reviewed on a defined cadence and used in decisions.
- **Score 4 (ML5 - Optimizing)**: All of ML4, plus systematic continuous improvement of this capability, with external benchmarking or recognized industry leadership.

**Evidence to Look For**: Risk assessment report, risk register entries, treatment plans

**Your Score**: ___ (0-4)
**Notes**:

---

#### G3. AI Ethics Framework

**Question**: Does the organization have AI ethics principles or responsible AI guidelines?

**Framework Mapping**: NIST AI RMF GOVERN 1.2, 3.1

**Scoring Rubric**:
- **Score 0 (ML1 - Initial)**: No AI ethics consideration. Ethics is not formally part of AI decision-making. At most some teams or individuals consider ethics, but no organizational framework.
- **Score 1 (ML2 - Developing)**: Ethics principles documented, but not yet operationalized (no implementation guidance or enforcement).
- **Score 2 (ML3 - Defined)**: Ethics principles documented with implementation guidance and integrated into AI development lifecycle.
- **Score 3 (ML4 - Managed)**: All of the above, plus tracked quantitative metrics on this capability, reviewed on a defined cadence and used in decisions.
- **Score 4 (ML5 - Optimizing)**: All of ML4, plus systematic continuous improvement of this capability, with external benchmarking or recognized industry leadership.

**Evidence to Look For**: Ethics framework document, ethics review process, ethics checklist

**Your Score**: ___ (0-4)
**Notes**:

---

#### G4. Data Governance for AI

**Question**: Are there data governance policies specific to AI training data (privacy, security, quality, lineage)?

**Framework Mapping**: ISO 42001 Clause 8.2, NIST AI RMF MAP 3.3-3.4

**Scoring Rubric**:
- **Score 0 (ML1 - Initial)**: No data governance for AI. Training data is used without formal governance. At most general data governance exists, but not adapted for AI-specific concerns (training data, lineage, bias).
- **Score 1 (ML2 - Developing)**: AI-specific data governance policies documented, but enforcement is inconsistent.
- **Score 2 (ML3 - Defined)**: AI data governance policies documented, enforced, and integrated with technical data management practices.
- **Score 3 (ML4 - Managed)**: All of the above, plus tracked quantitative metrics on this capability, reviewed on a defined cadence and used in decisions.
- **Score 4 (ML5 - Optimizing)**: All of ML4, plus systematic continuous improvement of this capability, with external benchmarking or recognized industry leadership.

**Evidence to Look For**: Data governance policy, data classification scheme, data access controls

**Your Score**: ___ (0-4)
**Notes**:

---

#### G5. Compliance Tracking

**Question**: Does the organization track AI-related compliance obligations (regulations, contractual requirements, industry standards)?

**Framework Mapping**: NIST AI RMF GOVERN 1.1

**Scoring Rubric**:
- **Score 0 (ML1 - Initial)**: No tracking of AI compliance obligations. Organization may not be aware of what applies. At most informal awareness of some obligations (EU AI Act, customer requirements), but no tracking system.
- **Score 1 (ML2 - Developing)**: Compliance obligations documented, but gap analysis and remediation plans are incomplete.
- **Score 2 (ML3 - Defined)**: Compliance obligations tracked with gap analysis, remediation plans, and regular reviews.
- **Score 3 (ML4 - Managed)**: All of the above, plus tracked quantitative metrics on this capability, reviewed on a defined cadence and used in decisions.
- **Score 4 (ML5 - Optimizing)**: All of ML4, plus systematic continuous improvement of this capability, with external benchmarking or recognized industry leadership.

**Evidence to Look For**: Compliance register, gap analysis, remediation project plans

**Your Score**: ___ (0-4)
**Notes**:

---

#### G6. Third-Party AI Risk Management

**Question**: Are there processes to assess risks from third-party AI systems or vendors?

**Framework Mapping**: NIST AI RMF GOVERN 6.1-6.2

**Scoring Rubric**:
- **Score 0 (ML1 - Initial)**: No evaluation of third-party AI risks. Vendors are onboarded without AI-specific review. At most some awareness of third-party AI risks, but no formal assessment process.
- **Score 1 (ML2 - Developing)**: Third-party AI assessment process documented, but not yet consistently applied.
- **Score 2 (ML3 - Defined)**: All third-party AI vendors and systems assessed using documented process with risk acceptance/mitigation.
- **Score 3 (ML4 - Managed)**: All of the above, plus tracked quantitative metrics on this capability, reviewed on a defined cadence and used in decisions.
- **Score 4 (ML5 - Optimizing)**: All of ML4, plus systematic continuous improvement of this capability, with external benchmarking or recognized industry leadership.

**Evidence to Look For**: Vendor assessment questionnaire, vendor risk register, contract AI clauses

**Your Score**: ___ (0-4)
**Notes**:

---

#### G7. AI Documentation Requirements

**Question**: Are there requirements for documenting AI systems (model cards, impact assessments, risk assessments)?

**Framework Mapping**: NIST AI RMF GOVERN 1.6, MAP 5.1

**Scoring Rubric**:
- **Score 0 (ML1 - Initial)**: No documentation requirements for AI systems. At most informal expectation that systems should be documented, but no standard or enforcement.
- **Score 1 (ML2 - Developing)**: Documentation requirements exist (templates provided), but compliance is inconsistent.
- **Score 2 (ML3 - Defined)**: Documentation requirements mandated with compliance checks before production deployment.
- **Score 3 (ML4 - Managed)**: All of the above, plus tracked quantitative metrics on this capability, reviewed on a defined cadence and used in decisions.
- **Score 4 (ML5 - Optimizing)**: All of ML4, plus systematic continuous improvement of this capability, with external benchmarking or recognized industry leadership.

**Evidence to Look For**: Documentation standards, templates, completed examples, approval gates

**Your Score**: ___ (0-4)
**Notes**:

---

#### G8. AI Transparency and Explainability

**Question**: Are there requirements for AI systems to be explainable and transparent to stakeholders?

**Framework Mapping**: NIST AI RMF Trustworthy AI Characteristic: Accountable and Transparent

**Scoring Rubric**:
- **Score 0 (ML1 - Initial)**: No transparency or explainability requirements. Black box models are acceptable. At most some discussion of explainability, but no formal requirements.
- **Score 1 (ML2 - Developing)**: Explainability requirements documented, but not yet consistently applied or validated.
- **Score 2 (ML3 - Defined)**: Explainability requirements enforced based on risk level with validation before deployment.
- **Score 3 (ML4 - Managed)**: All of the above, plus tracked quantitative metrics on this capability, reviewed on a defined cadence and used in decisions.
- **Score 4 (ML5 - Optimizing)**: All of ML4, plus systematic continuous improvement of this capability, with external benchmarking or recognized industry leadership.

**Evidence to Look For**: Explainability standards, risk-based thresholds, explainability validation reports

**Your Score**: ___ (0-4)
**Notes**:

---

**Governance Assessment Total**: ___/32 points
**Governance Score**: (Total/32) × 100 = ___%

**Interpretation**:
- **0-24%** (average ML1 - Initial): Significant governance gaps - policy and framework work needed
- **25-49%** (average ML2 - Developing): Early governance foundation - policies emerging
- **50-74%** (average ML3 - Defined): Developing governance capability - enforcement and consistency needed
- **75-100%** (average ML4 - Managed or above): Strong governance foundation - ready for enterprise integration

---

### Change Agent Assessment (Maturity Level 1 Baseline)

**Instructions for Implementation Leader**: Rate your organization's readiness for AI maturity progression.

#### C1. Organizational AI Awareness

**Question**: Is there broad organizational awareness of AI opportunities, risks, and responsibilities?

**Framework Mapping**: ISO 42001 Clause 7.3, NIST AI RMF GOVERN 4.1

**Scoring Rubric**:
- **Score 0 (ML1 - Initial)**: Very limited awareness. AI is understood only by small teams actively using it. At most growing awareness among early adopters, but most of organization is unaware.
- **Score 1 (ML2 - Developing)**: Organization-wide awareness campaign has occurred, but retention and behavior change are inconsistent.
- **Score 2 (ML3 - Defined)**: Broad, sustained organizational awareness with AI literacy integrated into onboarding and training.
- **Score 3 (ML4 - Managed)**: All of the above, plus tracked quantitative metrics on this capability, reviewed on a defined cadence and used in decisions.
- **Score 4 (ML5 - Optimizing)**: All of ML4, plus systematic continuous improvement of this capability, with external benchmarking or recognized industry leadership.

**Evidence to Look For**: Training attendance records, survey results, communication campaigns

**Your Score**: ___ (0-4)
**Notes**:

---

#### C2. Cross-Functional Collaboration

**Question**: Do AI initiatives involve cross-functional teams (business, tech, risk, legal, ethics)?

**Framework Mapping**: NIST AI RMF MAP 1.2

**Scoring Rubric**:
- **Score 0 (ML1 - Initial)**: AI projects are siloed within technical teams with minimal business or governance involvement. At most some cross-functional engagement happens reactively (legal consulted when there's an issue).
- **Score 1 (ML2 - Developing)**: Cross-functional teams are assembled for AI projects, but collaboration is ad-hoc and not formalized.
- **Score 2 (ML3 - Defined)**: Cross-functional collaboration is standard practice with defined roles and regular touchpoints.
- **Score 3 (ML4 - Managed)**: All of the above, plus tracked quantitative metrics on this capability, reviewed on a defined cadence and used in decisions.
- **Score 4 (ML5 - Optimizing)**: All of ML4, plus systematic continuous improvement of this capability, with external benchmarking or recognized industry leadership.

**Evidence to Look For**: Project team rosters, collaboration frameworks, RACI matrices

**Your Score**: ___ (0-4)
**Notes**:

---

#### C3. AI Change Sponsorship

**Question**: Is there visible executive sponsorship for AI maturity improvements (not just AI projects)?

**Framework Mapping**: ISO 42001 Clause 5.1

**Scoring Rubric**:
- **Score 0 (ML1 - Initial)**: No executive sponsorship. AI maturity work happens bottom-up without leadership backing. At most an executive cares about AI maturity, but hasn't publicly committed resources or time.
- **Score 1 (ML2 - Developing)**: Executive sponsor identified and has committed to supporting AI maturity work.
- **Score 2 (ML3 - Defined)**: Executive sponsor is visibly championing AI maturity with regular communication and resource allocation.
- **Score 3 (ML4 - Managed)**: All of the above, plus tracked quantitative metrics on this capability, reviewed on a defined cadence and used in decisions.
- **Score 4 (ML5 - Optimizing)**: All of ML4, plus systematic continuous improvement of this capability, with external benchmarking or recognized industry leadership.

**Evidence to Look For**: Executive communications, resource allocation decisions, executive participation in governance

**Your Score**: ___ (0-4)
**Notes**:

---

#### C4. AI Innovation Culture

**Question**: Does the organizational culture encourage AI experimentation while managing risks?

**Framework Mapping**: NIST AI RMF GOVERN 4.2

**Scoring Rubric**:
- **Score 0 (ML1 - Initial)**: Culture either discourages AI experimentation OR encourages unconstrained experimentation without risk consideration. At most culture is permissive, but no active encouragement or framework for safe experimentation.
- **Score 1 (ML2 - Developing)**: Organization encourages AI experimentation and has provided some guidance, but risk management is inconsistent.
- **Score 2 (ML3 - Defined)**: Balanced culture: active encouragement of AI innovation with clear risk guardrails and support.
- **Score 3 (ML4 - Managed)**: All of the above, plus tracked quantitative metrics on this capability, reviewed on a defined cadence and used in decisions.
- **Score 4 (ML5 - Optimizing)**: All of ML4, plus systematic continuous improvement of this capability, with external benchmarking or recognized industry leadership.

**Evidence to Look For**: Innovation programs, sandboxes for experimentation, experimentation policies

**Your Score**: ___ (0-4)
**Notes**:

---

#### C5. Lessons Learned and Knowledge Sharing

**Question**: Does the organization capture and share lessons learned from AI projects?

**Framework Mapping**: ISO 42001 Clause 10.2

**Scoring Rubric**:
- **Score 0 (ML1 - Initial)**: No knowledge sharing. Teams repeat each other's mistakes and solutions. At most informal knowledge sharing (Slack, hallway conversations), but nothing structured.
- **Score 1 (ML2 - Developing)**: Knowledge sharing mechanisms exist (wikis, communities of practice), but participation is inconsistent.
- **Score 2 (ML3 - Defined)**: Structured knowledge management with post-project reviews, documented lessons, and active communities.
- **Score 3 (ML4 - Managed)**: All of the above, plus tracked quantitative metrics on this capability, reviewed on a defined cadence and used in decisions.
- **Score 4 (ML5 - Optimizing)**: All of ML4, plus systematic continuous improvement of this capability, with external benchmarking or recognized industry leadership.

**Evidence to Look For**: Knowledge repository, community of practice meeting records, retrospective documentation

**Your Score**: ___ (0-4)
**Notes**:

---

#### C6. Stakeholder Engagement

**Question**: Are key stakeholders (customers, partners, employees, regulators) engaged in AI governance discussions?

**Framework Mapping**: NIST AI RMF GOVERN 5.1-5.2

**Scoring Rubric**:
- **Score 0 (ML1 - Initial)**: No stakeholder engagement. AI decisions made internally without external input. At most reactive engagement (respond to stakeholder questions), but no proactive outreach.
- **Score 1 (ML2 - Developing)**: Proactive engagement planned or beginning, but not yet systematic or comprehensive.
- **Score 2 (ML3 - Defined)**: Systematic stakeholder engagement with regular touchpoints and feedback integration.
- **Score 3 (ML4 - Managed)**: All of the above, plus tracked quantitative metrics on this capability, reviewed on a defined cadence and used in decisions.
- **Score 4 (ML5 - Optimizing)**: All of ML4, plus systematic continuous improvement of this capability, with external benchmarking or recognized industry leadership.

**Evidence to Look For**: Stakeholder engagement plan, customer advisory board, survey results

**Your Score**: ___ (0-4)
**Notes**:

---

#### C7. AI Maturity Roadmap

**Question**: Does the organization have a roadmap for progressing AI maturity over time?

**Framework Mapping**: ISO 42001 Clause 6.2

**Scoring Rubric**:
- **Score 0 (ML1 - Initial)**: No roadmap. AI maturity progression is not planned. At most informal ideas about what to improve, but no documented roadmap.
- **Score 1 (ML2 - Developing)**: Roadmap documented, but not yet socialized or approved for resource allocation.
- **Score 2 (ML3 - Defined)**: AI maturity roadmap documented, approved, and tracked with regular progress reviews.
- **Score 3 (ML4 - Managed)**: All of the above, plus tracked quantitative metrics on this capability, reviewed on a defined cadence and used in decisions.
- **Score 4 (ML5 - Optimizing)**: All of ML4, plus systematic continuous improvement of this capability, with external benchmarking or recognized industry leadership.

**Evidence to Look For**: Roadmap document, project plans, governance review of progress

**Your Score**: ___ (0-4)
**Notes**:

---

#### C8. Diversity and Inclusion in AI

**Question**: Is diversity and inclusion considered in AI team composition and system design?

**Framework Mapping**: NIST AI RMF GOVERN 3.1-3.2

**Scoring Rubric**:
- **Score 0 (ML1 - Initial)**: No consideration of diversity in AI teams or system design. At most awareness that diversity matters, but no formal approach to achieving it.
- **Score 1 (ML2 - Developing)**: Diversity goals set for AI teams, but progress is slow or inconsistent.
- **Score 2 (ML3 - Defined)**: Active diversity initiatives for AI teams with representation in decision-making and system design reviews.
- **Score 3 (ML4 - Managed)**: All of the above, plus tracked quantitative metrics on this capability, reviewed on a defined cadence and used in decisions.
- **Score 4 (ML5 - Optimizing)**: All of ML4, plus systematic continuous improvement of this capability, with external benchmarking or recognized industry leadership.

**Evidence to Look For**: Diversity metrics, inclusive design practices, diverse review panels

**Your Score**: ___ (0-4)
**Notes**:

---

**Change Agent Assessment Total**: ___/32 points
**Change Agent Score**: (Total/32) × 100 = ___%

**Interpretation**:
- **0-24%** (average ML1 - Initial): Significant cultural gaps - stakeholder engagement and awareness work needed
- **25-49%** (average ML2 - Developing): Early cultural readiness - sponsorship and collaboration emerging
- **50-74%** (average ML3 - Defined): Developing change capability - ready to scale initiatives
- **75-100%** (average ML4 - Managed or above): Strong change foundation - ready for enterprise-wide transformation

---

## Assessment Summary and Next Steps

### Calculate Your Overall Maturity Level 1 Baseline

**Audience Scores**:
- Leadership: ___%
- Technical: ___%
- Governance: ___%
- Change Agent: ___%

**Overall maturity level Determination**:
Your organization is at **Maturity Level 1** if most scores are **below 25%** (average ML1 - Initial: capability absent or informal and undocumented for most questions).

**Current maturity level**: Maturity Level 1 (Initial)

**Target**: Bring all audience scores to the **25-49% range** (average ML2 - Developing: documented but inconsistent) to solidly achieve Maturity Level 2; 50-74% (ML3 - Defined) means the organization is past this guide's target.

**Priorities**: Focus implementation efforts on the **lowest-scoring audience(s)** first, as they're the limiting factor for overall maturity.

---

## 6. Multi-Audience Implementation Playbooks

Now that you've assessed your baseline, here's how each audience should proceed to build Maturity Level 2 capabilities.

---

### Leadership Playbook: Governance and Sponsorship

**Your Role**: As a leader, you're responsible for **establishing the foundation** - creating structures, allocating resources, and demonstrating commitment.

#### Priority Actions (Months 1-3)

**Action 1: Appoint an AI Governance Lead**

**What**: Designate a person (0.5-1 FTE) responsible for driving AI governance and maturity progression.

**Who**: Could be:
- Chief AI Officer or Chief Data Officer
- VP/Director of AI/ML
- Risk Officer with AI expertise
- Program Manager with change management skills

**Why**: Someone needs to own this work. Without a designated owner, AI governance becomes "everyone's job = no one's job."

**How**:
1. Define role scope (governance, not just project delivery)
2. Ensure role has authority to convene stakeholders and access leadership
3. Allocate sufficient time (at least 50% FTE for this work)
4. Announce the appointment organization-wide

**Timeline**: Month 1
**Investment**: Reallocate existing FTE or hire (approx. $75-150K annual for mid-senior level)

---

**Action 2: Form an AI Governance Working Group**

**What**: Cross-functional committee to oversee AI governance development and monitor risks.

**Who**: Representatives from:
- Leadership (sponsor)
- AI/ML technical leads
- Risk management
- Legal/compliance
- Data governance
- IT operations
- Business stakeholders

**Why**: AI governance requires diverse perspectives. This group provides oversight and cross-functional alignment.

**How**:
1. Draft charter (purpose, scope, membership, meeting cadence)
2. Invite members and secure commitment (at least quarterly attendance)
3. Schedule first meeting with clear agenda
4. Document decisions and track action items

**Meeting Cadence**: Monthly initially (as you build foundation), then quarterly (once established)

**Timeline**: Month 2
**Investment**: ~10 hours/quarter per member

---

**Action 3: Allocate AI Governance Budget**

**What**: Dedicated budget for AI governance and maturity work (not just AI projects).

**Budget Components**:
- **Personnel**: 0.5-1 FTE governance lead ($75-150K)
- **Tools**: Inventory/catalog systems, policy management ($10-30K)
- **Training**: Workshops, certifications, external expertise ($15-40K)
- **External Support**: Consultants for policy development or risk assessment ($25-75K)
- **Contingency**: 20% buffer

**Total Budget Range**: $50-150K for first year (lower end for smaller orgs, higher for enterprise)

**How**:
1. Build business case (risk mitigation + scalability enablement)
2. Present to CFO/budget authority
3. Secure approval for current fiscal year + commitment for future years

**Timeline**: Month 2-3
**Investment**: Time to build business case, then budget allocation

---

**Action 4: Commission AI Risk Assessment**

**What**: Conduct first formal AI risk assessment to identify current risks and priorities.

**Why**: You can't manage risks you haven't identified. This assessment builds the risk register that guides future work.

**How**:
1. Engage internal risk team or external consultant
2. Conduct stakeholder interviews and system reviews
3. Document identified risks with severity and likelihood
4. Present findings to leadership and governance working group
5. Create risk treatment plans for high-priority risks

**Timeline**: Month 3-4
**Investment**: $15-50K (depending on use of external consultants vs. internal team)

---

#### Ongoing Responsibilities (Months 4-12)

**Monthly**:
- Attend AI Governance Working Group meetings
- Review AI project pipeline and resource allocation
- Monitor AI-related risks and incidents

**Quarterly**:
- Receive AI maturity progress update from governance lead
- Review and approve major policy or process changes
- Assess need for additional resources or course corrections

**Annually**:
- Review and approve AI strategy and maturity roadmap
- Participate in board/executive-level AI governance reporting
- Allocate budget for next year's AI maturity work

---

**Leadership Playbook Success Metrics**:
By Month 12, you should be able to answer "yes" to:
- [ ] We have a designated AI governance lead with sufficient time and authority
- [ ] Our AI governance working group meets regularly and is making decisions
- [ ] We've allocated budget for AI governance and maturity work
- [ ] We've conducted at least one AI risk assessment and are tracking high-priority risks
- [ ] I receive regular updates on AI governance progress and risks
- [ ] We're ready to move toward Maturity Level 3 (enterprise standards)

---

### Technical Playbook: MLOps Foundation

**Your Role**: As technical practitioners, you're responsible for **documenting processes, building systems, and establishing repeatability**.

#### Priority Actions (Months 1-3)

**Action 1: Create AI System Inventory**

**What**: Centralized list of all AI systems currently in use or development.

**Why**: You can't govern what you can't see. The inventory provides visibility for leadership and governance teams.

**How**:
1. **Define scope**: What counts as "AI"? (Recommendation: Start with ML models, LLMs/GenAI, AI SaaS tools)
2. **Gather data**: Survey teams, review project lists, check procurement records
3. **Create inventory structure** (spreadsheet or database):
   - System name and description
   - Business owner and technical owner
   - Current status (development, pilot, production, retired)
   - Risk level (high, medium, low - based on impact)
   - Data sources
   - Model type and architecture
   - Last update date
4. **Establish update process**: Who updates it and how often?

**Timeline**: Month 1-2
**Investment**: 20-40 hours initial creation, 2-4 hours/month ongoing

**Tool Options**:
- **Simple**: Shared spreadsheet (Google Sheets, Excel)
- **Better**: Internal wiki or database (Notion, Confluence, Airtable)
- **Advanced**: Model registry tool (MLflow, W&B, proprietary)

---

**Action 2: Document Current AI Development Process**

**What**: Write down how AI/ML development currently works (even if it's ad-hoc).

**Why**: You can't improve what you don't understand. Documentation is the first step toward standardization.

**How**:
1. **Choose a recent AI project** as the example
2. **Document end-to-end process**:
   - How did the project start? (requirements gathering)
   - Where did training data come from? (data sourcing)
   - How was the model developed? (experimentation, tooling)
   - How was the model tested? (validation approach)
   - How was the model deployed? (deployment process)
   - How is the model monitored? (monitoring approach)
3. **Identify gaps**: Where did things break down? What was missing?
4. **Create process diagram** (flowchart or swim lanes)
5. **Share with team for feedback** and refinement

**Timeline**: Month 2
**Investment**: 15-30 hours

**Deliverable**: Process documentation (PDF or wiki page) that can serve as template for future projects

---

**Action 3: Establish Basic Model Documentation Standard**

**What**: Create template for documenting AI models (model card or equivalent).

**Why**: Model documentation enables governance, compliance, and knowledge sharing.

**How**:
1. **Adopt an existing template**:
   - Google's Model Cards (https://modelcards.withgoogle.com/)
   - HuggingFace Model Cards
   - NIST AI RMF-aligned template
2. **Customize for your context** (remove sections that don't apply, add org-specific fields)
3. **Create 2-3 examples** using existing models
4. **Socialize with team** and incorporate feedback
5. **Make it easy**: Provide template in formats developers use (Markdown, Jupyter notebook, internal wiki)

**Timeline**: Month 2-3
**Investment**: 10-20 hours to create template, 2-4 hours per model to complete

**Deliverable**: Model card template + 2-3 completed examples

---

**Action 4: Implement Basic Model Monitoring**

**What**: Set up monitoring for at least one production AI model (performance, errors, drift).

**Why**: Proves the value of monitoring and creates a template for other models.

**How**:
1. **Choose highest-risk production model** (most business impact or most customer-facing)
2. **Define metrics to monitor**:
   - **Performance**: Accuracy, precision, recall, latency
   - **Operational**: Error rates, timeouts, resource usage
   - **Data drift**: Input distribution changes
3. **Implement monitoring**:
   - Use existing observability platform (DataDog, New Relic, Prometheus)
   - Add model-specific metrics
   - Set up alerting for threshold breaches
4. **Test alerting**: Validate that alerts fire and reach the right people
5. **Document monitoring setup** so it can be replicated for other models

**Timeline**: Month 3-4
**Investment**: 20-40 hours depending on existing tooling

**Tool Options**:
- **Use existing observability platform** + custom metrics
- **Open source**: Evidently AI, Alibi Detect, WhyLabs
- **Commercial**: Arthur, Fiddler, WhyLabs, Arize

---

#### Ongoing Activities (Months 4-12)

**Monthly**:
- Update AI system inventory with new projects or retirements
- Monitor production models and investigate alerts
- Hold AI technical community of practice meetings

**Quarterly**:
- Review and update AI development process documentation based on lessons learned
- Conduct retrospectives on completed AI projects
- Assess MLOps tooling gaps and build business case for investments

**By Month 6-9** (Mid-term milestones):
- [ ] All new AI projects use model documentation template
- [ ] At least 3 production models have monitoring implemented
- [ ] Development process is documented and socialized, even if not fully standardized

**By Month 12** (Maturity Level 2 Target):
- [ ] Comprehensive AI system inventory (80%+ completeness)
- [ ] AI development process documented and mostly followed
- [ ] Model documentation standard adopted (50%+ of models documented)
- [ ] Basic monitoring in place for production models
- [ ] Ready to invest in MLOps platform and automation (Maturity Level 3)

---

**Technical Playbook Success Metrics**:
- AI system inventory exists and is maintained
- Development process is documented
- Model documentation template exists and is being adopted
- At least one production model has comprehensive monitoring
- Technical debt is being tracked and managed
- Team has basic AI/ML best practices training

---

### Governance Playbook: Policy and Risk Framework

**Your Role**: As governance/compliance professionals, you're responsible for **policy development, risk assessment, and compliance tracking**.

#### Priority Actions (Months 1-3)

**Action 1: Draft AI Acceptable Use Policy**

**What**: Document defining acceptable and unacceptable uses of AI within the organization.

**Why**: Sets clear expectations for employees and reduces risk of misuse.

**How**:
1. **Review existing policies** (IT acceptable use, data security, code of conduct) for applicable principles
2. **Draft AI-specific policy** covering:
   - **Scope**: What AI systems/tools does this cover?
   - **Acceptable uses**: Approved AI use cases and tools
   - **Prohibited uses**: High-risk or banned applications (e.g., facial recognition, hiring decisions without human review)
   - **Data restrictions**: What data can/cannot be used for AI training
   - **Third-party AI tools**: Approval process for new tools
   - **Transparency requirements**: When AI use must be disclosed
   - **Accountability**: Who is responsible for compliance
3. **Socialize draft** with stakeholders (legal, IT, HR, business leaders)
4. **Finalize and get executive approval**
5. **Communicate policy** to organization and make it easily accessible

**Timeline**: Month 1-3
**Investment**: 30-50 hours policy development + legal review time

**Template Sources**:
- Stanford HAI AI Policy Toolkit
- Microsoft Responsible AI Resources
- Industry association templates (if available)

---

**Action 2: Establish AI Risk Assessment Process**

**What**: Documented process for assessing risks of new or existing AI systems.

**Why**: Enables proactive risk management rather than reactive incident response.

**How**:
1. **Define risk assessment framework**:
   - **When** is assessment required? (new AI projects, major changes, annually for production systems)
   - **Who** conducts it? (project team, risk team, cross-functional review)
   - **What** is assessed? (Use NIST AI RMF categories: bias, privacy, security, safety, transparency, explainability, accountability)
   - **How** are risks rated? (likelihood × impact matrix)
   - **What** happens after assessment? (risk acceptance, mitigation, escalation)
2. **Create risk assessment template/questionnaire**
3. **Conduct pilot assessment** on an existing AI system
4. **Refine process** based on pilot feedback
5. **Document and socialize** the process

**Timeline**: Month 2-3
**Investment**: 25-40 hours process development, 4-8 hours per system assessed

**Deliverable**: Risk assessment process document + template + completed pilot example

---

**Action 3: Create AI Risk Register**

**What**: Centralized tracking system for identified AI risks and their treatment status.

**Why**: Provides visibility into risk landscape and enables prioritization of mitigation efforts.

**How**:
1. **Choose tracking system**: Spreadsheet, risk management software, or integrated into existing enterprise risk register
2. **Define risk register fields**:
   - Risk ID and description
   - AI system affected
   - Risk category (bias, privacy, security, etc.)
   - Likelihood and impact (initial and residual)
   - Risk owner
   - Mitigation approach (accept, mitigate, transfer, avoid)
   - Status and target completion date
3. **Populate with risks** from initial AI risk assessment (Action 4 from Leadership Playbook)
4. **Establish review cadence**: Monthly review by risk team, quarterly review by governance working group
5. **Integrate with incident management**: New risks identified from incidents are added

**Timeline**: Month 3-4
**Investment**: 15-25 hours initial setup, 2-4 hours/month ongoing

---

**Action 4: Map Compliance Obligations**

**What**: Inventory of AI-related compliance obligations applicable to your organization.

**Why**: Ensures you're aware of what you need to comply with and can plan accordingly.

**How**:
1. **Identify applicable regulations and standards**:
   - **Geographic**: EU AI Act, state AI laws (e.g., Colorado AI Act, California ADPEA), country-specific
   - **Industry**: Financial (FCRA, ECOA), Healthcare (HIPAA), etc.
   - **Contractual**: Customer AI requirements, SLAs
   - **Voluntary**: ISO 42001, NIST AI RMF, industry frameworks
2. **Document obligations** in a compliance matrix:
   - Requirement description
   - Source (regulation, contract, standard)
   - Applicability (which AI systems)
   - Current status (compliant, gap, not assessed)
   - Gap description and remediation plan
   - Owner and target date
3. **Conduct initial gap analysis** against current state
4. **Prioritize remediation** based on risk and timeline (e.g., EU AI Act deadlines)
5. **Present to governance working group** for awareness and prioritization

**Timeline**: Month 2-4
**Investment**: 30-50 hours research and documentation

**Deliverable**: Compliance obligations matrix with gap analysis

---

#### Ongoing Activities (Months 4-12)

**Monthly**:
- Review AI risk register and update mitigation progress
- Conduct risk assessments for new AI projects
- Monitor regulatory landscape for new AI obligations

**Quarterly**:
- Report AI risk status to governance working group
- Update compliance obligations matrix with new requirements
- Review and refresh AI policies based on lessons learned

**By Month 6-9** (Mid-term milestones):
- [ ] AI acceptable use policy is approved and communicated
- [ ] Risk assessment process is established and being used for new projects
- [ ] AI risk register exists and is actively maintained
- [ ] Compliance obligations are mapped and gap remediation is in progress

**By Month 12** (Maturity Level 2 Target):
- [ ] Core AI policies documented and enforced
- [ ] Risk assessment is standard part of AI project lifecycle
- [ ] AI risk register integrated into enterprise risk management
- [ ] Compliance gaps are identified and remediation plans are on track
- [ ] Ready for policy enforcement automation and audit frameworks (Maturity Level 3)

---

**Governance Playbook Success Metrics**:
- AI policies documented and approved
- Risk assessment process established
- Risk register actively maintained
- Compliance obligations mapped
- No major compliance violations or incidents due to AI
- Governance oversight integrated into AI project lifecycle

---

### Change Agent Playbook: Stakeholder Engagement and Change Management

**Your Role**: As the implementation leader/change agent, you're the **orchestrator** - driving progress across all other audiences while managing stakeholders and demonstrating value.

#### Priority Actions (Months 1-3)

**Action 1: Build Stakeholder Map and Engagement Plan**

**What**: Identify all key stakeholders for AI maturity work and plan how to engage them.

**Why**: AI maturity requires cross-functional buy-in. Without stakeholder engagement, initiatives stall.

**How**:
1. **Identify stakeholders**:
   - **Champions**: Executives who sponsor AI maturity (target: 1-2)
   - **Advocates**: Leaders who support AI maturity and will help drive it (target: 3-5)
   - **Implementers**: Teams who will do the work (technical, governance, business)
   - **Skeptics**: Those who may resist (understand their concerns)
   - **Affected**: Teams whose work will change due to new governance
2. **Map stakeholders**: Create a power/interest matrix (high power + high interest = key players)
3. **Define engagement approach** for each:
   - Champions: Regular 1:1 updates, ask for visible support
   - Advocates: Involve in working groups, ask them to communicate to their teams
   - Implementers: Provide clear expectations, solicit feedback, recognize contributions
   - Skeptics: Understand concerns, address them proactively, find common ground
   - Affected: Communicate early and often, show benefits, provide training
4. **Create engagement calendar**: When will you communicate with each stakeholder group?
5. **Document in stakeholder map template**

**Timeline**: Month 1
**Investment**: 10-15 hours

**Deliverable**: Stakeholder map + engagement plan

---

**Action 2: Develop AI Maturity Roadmap**

**What**: Visual roadmap showing the journey from Maturity Level 1 to Maturity Level 2 (and beyond).

**Why**: Stakeholders need to see the path forward, understand timelines, and know what success looks like.

**How**:
1. **Define phases**:
   - **Phase 1** (Months 1-3): Foundation (governance structure, policies, inventory)
   - **Phase 2** (Months 4-6): Process (documentation, risk assessment, basic monitoring)
   - **Phase 3** (Months 7-9): Integration (policies enforced, processes adopted, cross-functional collaboration)
   - **Phase 4** (Months 10-12): Maturity (Maturity Level 2 solidified, planning for Maturity Level 3)
2. **Map initiatives to phases** (pull from other playbooks)
3. **Define milestones and success metrics** for each phase
4. **Show dependencies**: What must happen before what?
5. **Create visual** (Gantt chart, timeline, or roadmap infographic)
6. **Socialize with governance working group** and refine
7. **Present to leadership** for approval

**Timeline**: Month 1-2
**Investment**: 15-25 hours

**Deliverable**: AI Maturity Roadmap (presentation + project plan)

---

**Action 3: Launch AI Awareness Campaign**

**What**: Organization-wide communication campaign to build AI literacy and awareness of new governance efforts.

**Why**: Change fails when people don't understand why it's happening or what's expected of them.

**How**:
1. **Define campaign objectives**:
   - Build general AI literacy (what is AI, how is it used, what are risks)
   - Communicate new AI governance approach and policies
   - Encourage responsible AI use and discourage shadow AI
   - Make it easy for teams to get help and ask questions
2. **Create campaign content**:
   - **Announcement**: Email from executive sponsor explaining AI maturity initiative
   - **Educational content**: FAQ, lunch-and-learn sessions, video explainers
   - **Policy rollout**: Summary of new AI policies with "what this means for you"
   - **Resources**: Where to go for help, how to report concerns, tools and templates
3. **Choose channels**:
   - Email announcements
   - Intranet/wiki pages
   - Team meetings (ask managers to discuss with their teams)
   - Town halls or all-hands meetings
   - Slack/Teams channels for ongoing Q&A
4. **Launch in phases**:
   - **Month 2**: Executive announcement + initial education
   - **Month 3-4**: Policy rollout + training
   - **Ongoing**: Regular updates on progress and success stories

**Timeline**: Month 2-6 (campaign runs over multiple months)
**Investment**: 30-50 hours campaign planning and content creation, ongoing execution

**Deliverable**: Communication plan + content library + metrics (email open rates, training attendance, Q&A engagement)

---

**Action 4: Establish AI Community of Practice**

**What**: Regular forum for AI practitioners (technical, governance, business) to share knowledge and collaborate.

**Why**: Breaks down silos, accelerates learning, and builds community around AI maturity.

**How**:
1. **Define community scope**: Who's invited? (AI developers, data scientists, business analysts using AI, governance professionals)
2. **Set meeting cadence**: Monthly or biweekly (60-90 minutes)
3. **Plan agenda format**:
   - Updates on AI maturity initiatives
   - Spotlight on a recent AI project (lessons learned)
   - Technical deep-dive or guest speaker
   - Open forum for Q&A and problem-solving
4. **Create supporting infrastructure**:
   - Slack/Teams channel for ongoing discussion
   - Wiki or shared drive for resources
   - Calendar invites and regular reminders
5. **Launch first meeting** with clear value proposition
6. **Solicit feedback** and iterate on format

**Timeline**: Month 3 (launch), ongoing
**Investment**: 5-10 hours/month to organize and facilitate

**Deliverable**: Community of practice with 10-20 active members meeting regularly

---

#### Ongoing Responsibilities (Months 4-12)

**Weekly**:
- Monitor progress on roadmap initiatives (check in with workstream leads)
- Unblock obstacles and escalate issues
- Communicate progress to governance working group

**Monthly**:
- Send AI maturity update to stakeholders (progress, wins, challenges, next steps)
- Facilitate AI community of practice meeting
- Review stakeholder engagement plan and adjust as needed
- Track and report metrics (see below)

**Quarterly**:
- Present AI maturity progress to leadership and governance working group
- Refresh roadmap based on progress and new priorities
- Conduct retrospective with implementation team to identify improvements
- Update stakeholder map based on organizational changes

**By Month 6** (Mid-term assessment):
- Conduct mid-point assessment using Maturity Level 1 baseline assessments (see Section 5)
- Identify areas ahead of plan and areas behind plan
- Adjust roadmap and resource allocation as needed

**By Month 12** (Maturity Level 2 Target):
- Conduct full Maturity Level 2 assessment (see separate Maturity Level 2 Assessment document)
- Celebrate achievements and recognize contributors
- Present Maturity Level 2 achievement to leadership
- Begin planning Maturity Level 2→3 progression

---

**Change Agent Playbook Success Metrics**:

Track these metrics monthly to demonstrate progress:

**Visibility Metrics**:
- AI system inventory: % completeness (target: 80%+ by month 12)
- Organization-wide AI awareness: % of employees who have completed AI literacy training (target: 60%+ by month 12)

**Governance Metrics**:
- Policies documented and approved (target: 3-5 core policies by month 6)
- Governance working group: % meeting attendance (target: 80%+ attendance)
- Risk assessments conducted: # of AI systems assessed (target: 100% of high-risk systems by month 12)

**Technical Metrics**:
- Models documented: % using model card template (target: 50%+ by month 12)
- Production models monitored: % with monitoring in place (target: 100% by month 12)
- Development process adoption: % projects following documented process (target: 75%+ by month 12)

**Engagement Metrics**:
- Community of practice: # of active members and meeting attendance
- Stakeholder satisfaction: Survey or feedback on AI maturity initiative (target: 70%+ positive)

**Outcome Metrics**:
- AI incidents: # and severity (target: decrease in severity or zero high-severity incidents)
- Time to deploy AI models: baseline → track improvement (may increase initially due to new processes, then decrease)
- AI project success rate: % projects that move from pilot to production (target: increase over time)

---

## 7. Cross-Functional Elements

### Relationships and Support Structures

AI maturity progression requires **collaboration across organizational boundaries**. Here are the key relationships to establish:

#### Executive Sponsor ↔ Implementation Leader
**Nature**: Regular 1:1 updates, ask for visible support when needed
**Cadence**: Biweekly or monthly
**Purpose**: Keep sponsor informed, get advice on obstacles, secure resources and advocacy

#### Governance Working Group ↔ Implementation Team
**Nature**: Oversight and decision-making body provides direction to implementation teams
**Cadence**: Monthly governance meetings + ad-hoc as needed
**Purpose**: Decision-making, prioritization, issue escalation

#### Technical Teams ↔ Governance Teams
**Nature**: Collaborative partnership (governance provides requirements, technical provides implementation)
**Cadence**: Regular touchpoints during AI project lifecycle
**Purpose**: Ensure technical implementation meets governance requirements without unnecessary friction

#### Business Stakeholders ↔ AI Teams
**Nature**: Business provides use cases and requirements, AI teams deliver solutions
**Cadence**: Project-based engagement + representation in governance working group
**Purpose**: Ensure AI initiatives deliver business value and align with priorities

#### Internal ↔ External Support
**Nature**: Bring in external expertise where internal knowledge gaps exist
**When Needed**:
- AI governance best practices (consultants, industry associations)
- Legal/regulatory interpretation (law firms specializing in AI)
- Technical platform evaluation (vendors, analysts)
- Training and education (workshops, certifications)

---

### Timeline and Effort Estimates

**Overall Timeline**: 12 months from Maturity Level 1 to solidly achieving Maturity Level 2

**Effort by Audience** (cumulative over 12 months):

| Audience | Effort (Hours) | FTE Equivalent | Cost Estimate |
|----------|----------------|----------------|---------------|
| **Leadership** | 60-100 hours | 0.05 FTE (5%) | Opportunity cost of leadership time |
| **Technical** | 400-600 hours | 0.2-0.3 FTE (20-30%) | May be absorbed by existing team + $10-50K tooling |
| **Governance** | 300-500 hours | 0.15-0.25 FTE (15-25%) | May be absorbed by existing team + $25-75K consulting |
| **Change Agent** | 600-800 hours | 0.3-0.4 FTE (30-40%) | Dedicated role: $75-150K annual |

**Total Investment**: $50-150K + 1360-2000 hours (approximately 0.65-1.0 FTE across organization)

**Phasing**:
- **Months 1-3** (Heavy): Foundation-building (governance structure, policies, inventory)
- **Months 4-6** (Moderate): Process implementation and adoption
- **Months 7-9** (Moderate): Integration and enforcement
- **Months 10-12** (Light): Maturity solidification and planning for Maturity Level 3

---

### Success Metrics and Checkpoints

**Month 3 Checkpoint**: Foundation Complete
- [ ] AI governance lead appointed
- [ ] Governance working group formed and met at least once
- [ ] AI system inventory created (even if incomplete)
- [ ] At least one AI policy drafted

**Month 6 Checkpoint**: Process Documented
- [ ] AI policies approved and communicated
- [ ] AI development process documented
- [ ] Risk assessment process established
- [ ] Community of practice active

**Month 9 Checkpoint**: Adoption Emerging
- [ ] New AI projects following documented processes
- [ ] Risk assessments conducted for new projects
- [ ] Model documentation being adopted
- [ ] Basic monitoring in place for at least one production model

**Month 12 Checkpoint**: Maturity Level 2 Achieved
- [ ] All baseline assessments (Section 5) show scores in 40-60% range
- [ ] Governance structure operational and meeting regularly
- [ ] Policies documented and mostly enforced
- [ ] AI inventory comprehensive and maintained
- [ ] Development and deployment processes documented and mostly followed
- [ ] Risk register active and integrated into governance
- [ ] Organization-wide awareness of AI governance
- [ ] Ready to begin Maturity Level 2→3 progression

---

## 8. Practical Tools and Resources

### Templates Referenced in This Guide

1. **AI System Inventory Template** (Spreadsheet)
2. **Stakeholder Map Template** (PowerPoint or Miro)
3. **AI Maturity Roadmap Template** (Gantt chart or visual timeline)
4. **AI Acceptable Use Policy Template** (Word document)
5. **AI Risk Assessment Template** (Questionnaire + risk rating matrix)
6. **AI Risk Register Template** (Spreadsheet)
7. **Compliance Obligations Matrix Template** (Spreadsheet)
8. **Model Card Template** (Markdown or Jupyter notebook)
9. **AI Development Process Documentation Template** (Flowchart + narrative)
10. **Governance Working Group Charter Template** (Word document)

*(Templates to be developed and placed in `/templates/` directory)*

---

### Common Pitfalls and How to Avoid Them

**Pitfall 1: Perfectionism Paralysis**
- **Problem**: Waiting to have "perfect" policies or processes before launching
- **Solution**: Start with "good enough" documentation and iterate. Maturity Level 2 is about having a foundation, not perfection.

**Pitfall 2: Governance Theater**
- **Problem**: Creating policies and structures that look good but don't change behavior
- **Solution**: Focus on integration and enforcement. Policies are worthless if no one follows them.

**Pitfall 3: Lack of Executive Sponsorship**
- **Problem**: Trying to drive AI maturity bottom-up without leadership backing
- **Solution**: Don't start implementation without securing an executive sponsor. Spend time building the business case first.

**Pitfall 4: Treating AI Governance as IT-Only**
- **Problem**: Technical teams drive governance without involving risk, legal, or business stakeholders
- **Solution**: AI governance is cross-functional by nature. Form the governance working group early and keep it engaged.

**Pitfall 5: Underestimating Time and Effort**
- **Problem**: Expecting Maturity Level 2 maturity in 3 months with 10% FTE
- **Solution**: Be realistic. This is a 12-month journey requiring 0.5-1.0 FTE. Set expectations accordingly.

**Pitfall 6: Skipping Assessment**
- **Problem**: Jumping into implementation without understanding current state
- **Solution**: Use the assessments in Section 5 to baseline. You may be further along than you think, or you may have blind spots.

**Pitfall 7: Neglecting Change Management**
- **Problem**: Focusing only on documentation and forgetting that people need to change behavior
- **Solution**: Invest in the change agent playbook. Communication, training, and stakeholder engagement are as important as policies.

**Pitfall 8: Confusing Maturity Level 2 with Maturity Level 3**
- **Problem**: Trying to implement enterprise-wide automation and advanced MLOps before establishing foundation
- **Solution**: Remember Maturity Level 2 is about documentation and emerging processes. Save automation and enterprise standards for Maturity Level 3.

---

### External Resources

**Standards and Frameworks**:
- NIST AI RMF 1.0: https://www.nist.gov/itl/ai-risk-management-framework
- ISO/IEC 42001:2023: https://www.iso.org/standard/81230.html (purchase required)
- Executive Order 14110: https://www.whitehouse.gov/briefing-room/presidential-actions/2023/10/30/executive-order-on-the-safe-secure-and-trustworthy-development-and-use-of-artificial-intelligence/

**AI Governance Resources**:
- Stanford HAI AI Index: https://aiindex.stanford.edu/
- Partnership on AI: https://partnershiponai.org/
- AI Ethics Guidelines Database: https://algorithmwatch.org/en/project/ai-ethics-guidelines-global-inventory/

**Responsible AI Tools**:
- Model Cards (Google): https://modelcards.withgoogle.com/
- AI Fairness 360 (IBM): https://aif360.mybluemix.net/
- Fairlearn (Microsoft): https://fairlearn.org/

**Training and Certifications**:
- Coursera: AI For Everyone (Andrew Ng)
- LinkedIn Learning: Responsible AI Courses
- IAPP AI Governance Professional Certification

---

## Conclusion: Your Journey from Maturity Level 1 to Maturity Level 2

You're embarking on a **12-month journey** to establish foundational AI governance and mature from ad-hoc AI usage to documented, visible, and managed AI capabilities.

**This is hard work**. It requires:
- Dedicated people and budget
- Cross-functional collaboration
- Leadership commitment
- Patience as new processes take hold
- Willingness to iterate and improve

**But it's worth it**. By achieving Maturity Level 2, you:
- **Reduce risk**: Visibility and governance prevent AI incidents
- **Enable scaling**: You can confidently expand AI use knowing you have oversight
- **Build trust**: Stakeholders (customers, partners, regulators) trust your AI practices
- **Lay foundation**: Maturity Level 2 is the springboard to Maturity Level 3 enterprise standards and automation

**You're not alone**. Most organizations are at Maturity Level 1 or early Maturity Level 2. The fact that you're investing in this work puts you ahead of the curve.

**Next Steps**:
1. Complete the assessments in Section 5 to confirm your Maturity Level 1 baseline
2. Secure executive sponsorship (if you haven't already)
3. Begin with Month 1 priority actions from each playbook
4. Track progress monthly using the change agent success metrics
5. Celebrate milestones and recognize contributors

By this time next year, you'll look back and see **dramatic progress**. Let's get started.

---

**Return to**: [Implementation Master](../IMPLEMENTATION-MASTER.md) | [Assessment Methodology](../assessments/ASSESSMENT-SCORING-METHODOLOGY.md)

**Next Guide**: [Maturity Level 2→3 Implementation Guide](maturity level-2-TO-3-GUIDE.md) (use this when you've solidified Maturity Level 2)
