# AI Management Framework (AIMF) by PraeSyn
## Assessment Guide

**© 2026 PraeSyn, LLC. All rights reserved.**
Licensed under CC BY-NC-ND 4.0

**Version**: 1.0.5
**Publication Date**: January 29, 2026
**Document Type**: Assessment Methodology
**Status**: Pre-Publication (Working Draft)

---

## Overview

This guide provides the methodology for conducting AI Management Framework (AIMF) assessments. It covers the assessment process, scoring methodology, and interpretation of results.

---

## Assessment Objectives

The AIMF assessment enables organizations to:

1. **Determine Risk Baseline**: Assess AI system risk characteristics to select appropriate baseline (B1/B2/B3)
2. **Select Profile**: Choose or customize a profile based on baseline, industry, and organizational context
3. **Assess Maturity**: Evaluate implementation quality for each control using the ML1-5 scale
4. **Calculate Scores**: Generate profile, baseline-relative, and framework-relative scores
5. **Identify Gaps**: Compare current maturity to target maturity levels
6. **Prioritize Actions**: Focus improvement efforts on highest-impact gaps
7. **Track Progress**: Measure maturity improvement over time
8. **Demonstrate Compliance**: Provide objective evidence of AI governance capability

---

## Assessment Framework

### Maturity Scoring Scale

Each control is assessed using the **5-level CMMI-based maturity scale** with a **0-4 point scoring system**:

| Score | Maturity Level | Definition | Characteristics |
|-------|----------------|------------|-----------------|
| **0** | **ML1 - Initial** | Ad-hoc, individual-dependent; no documentation | No written procedures; depends on heroic individuals; knowledge in heads not docs |
| **1** | **ML2 - Developing** | Documented but inconsistent | Policies exist; implementation varies; some compliance, some non-compliance |
| **2** | **ML3 - Defined** | Standardized, organization-wide | Fully documented; consistently applied (>90%); trained workforce; audited |
| **3** | **ML4 - Managed** | Quantitatively measured and controlled | All ML3 + metrics tracked; performance data reviewed; data-driven decisions |
| **4** | **ML5 - Optimizing** | Continuous improvement and innovation | All ML4 + systematic innovation; industry leadership; external recognition |

**Key Principle**: ML1 scores as 0 to incentivize moving beyond ad-hoc processes. The assessment uses a **0-4 point scale** where ML3 (Defined) = 2 points represents the standard "implemented" level.

### Scale Retirement and Conversion (0-3 → 0-4)

The 0-3 assessment scale is **retired**. It was removed in [1.0.0] by
`change-control/20260129143000-CHANGE-PLAN-TIER-TO-BASELINE.md` and the migration was
completed in this release: as of v1.0.4 **no shipped document defines or asserts a scoring
scale other than 0-4 / ML1-ML5**. The only remaining `0-3` occurrences in the bundle are
historical records — the `OLD` column of the `change-control/` change logs, the
`CHANGELOG` entries for releases before 1.0.0, and the conversion table below. If a
document you are reading still presents `0-3` as a live scale, it is out of date and should
be reported.

The 0-3 lens had four buckets for a five-level model, which is why it could never express
ML4 or ML5:

| Old 0-3 score | Old level name | 0-4 score | Maturity level |
|---------------|----------------|-----------|----------------|
| 0 | Not Present | 0 | ML1 - Initial |
| 1 | Ad-Hoc | 0 | ML1 - Initial |
| 2 | Developing | 1 | ML2 - Developing |
| 3 | Established | 2 | ML3 - Defined |
| *(unreachable)* | — | 3 | ML4 - Managed |
| *(unreachable)* | — | 4 | ML5 - Optimizing |

Read the table left to right when re-reading old audit notes; read it right to left when
converting a current score back into an old 0-3 workbook. Two cautions:

- **Old `0` and old `1` both convert to 0 (ML1).** The old lens distinguished "capability
  absent" from "capability informal"; the 0-4 lens folds both into ML1 because the
  discriminating question at ML1→ML2 is *documentation*, not intent.
- **Do not up-convert an old `3` to ML4.** Old `3 Established` is ML3 *Defined* (score 2).
  ML4 (score 3) requires evidence the old lens never asked for — tracked quantitative
  metrics, reviewed and used in decisions. A control previously scored 3 must be
  re-assessed, not promoted.

### Maturity Assessment Decision Tree

```
Does the control capability exist at all?
   |
   ├→ NO or undocumented → ML1 (Score: 0)
   |
   └→ YES, documented → Is it consistently applied organization-wide (>90%)?
          |
          ├→ NO → ML2 (Score: 1) [Documented but inconsistent]
          |
          └→ YES → Are there quantitative metrics measuring effectiveness?
                 |
                 ├→ NO → ML3 (Score: 2) [Standardized]
                 |
                 └→ YES → Is there systematic continuous improvement?
                        |
                        ├→ NO → ML4 (Score: 3) [Measured]
                        |
                        └→ YES → ML5 (Score: 4) [Optimizing]
```

### Special Scoring Considerations

| Situation | Scoring Guidance |
|-----------|------------------|
| Partial implementation | If documented but <90% adoption → ML2 (Score: 1) |
| Recent adoption (<6 months) | ML2 (Score: 1) until proven sustainable |
| Policy exists but not implemented | ML2 (Score: 1) — policy = documented, implementation = inconsistent |
| Best team vs. organization norm | Score based on organization-wide norm, not best case |
| Metrics exist but not used | ML3 (Score: 2) — measurement alone doesn't equal ML4; must be used for decisions |
| One-time innovation | ML4 (Score: 3) — ML5 requires **continuous** improvement pattern |

**See**: [AIMF-MATURITY-LEVELS.md](AIMF-MATURITY-LEVELS.md) for detailed maturity level definitions and evidence criteria.

---

## Four-Audience Assessment Model

The AIMF uses a four-audience assessment approach to ensure comprehensive coverage:

### Audience Profiles

| Audience | Focus Area | Primary Dimension | Representative Roles |
|----------|------------|-------------------|---------------------|
| **Leadership** | Governance, sponsorship, resources | D1: AI Governance | CIO, CAIO, Risk Officer, Business Unit Leaders |
| **Technical** | Systems, processes, tools | D3: Technical Operations | ML Engineers, Data Scientists, MLOps, Architecture |
| **Governance** | Policies, controls, compliance | D2: Data Governance | Legal, Compliance, Privacy, Security Officers |
| **Change Agent** | Culture, collaboration, stakeholders | D4: Organizational Culture | HR, Change Management, Training, Communications |

### Why Four Audiences?

1. **Cross-functional visibility**: Each audience sees different aspects of maturity
2. **Comprehensive coverage**: Ensures all dimensions are assessed
3. **Targeted action planning**: Enables audience-specific improvement plans
4. **Validation**: Cross-validates responses across perspectives

---

## Assessment Process

### Phase 0: Baseline Selection

**Objectives**:
- Characterize AI system risk profile
- Determine appropriate baseline (B1/B2/B3)
- Identify controls in scope

**Activities**:

1. **Complete Risk Characterization Questionnaire**
   - Assess AI system across 6 risk dimensions:
     - Autonomy Level (1-5)
     - Decision Reversibility (1-5)
     - Impact Scale (1-5)
     - Consequence Severity (1-5)
     - Data Sensitivity (1-5)
     - Regulatory Environment (1-5)
   - Calculate total risk score (6-30 range)

2. **Apply Baseline Assignment Rules**
   - **B3 (High Risk)** if: Any dimension = 5, Consequence ≥ 4, Regulatory ≥ 4, or Total ≥ 21
   - **B2 (Moderate Risk)** if: Any dimension ≥ 4, Two+ dimensions ≥ 3, or Total ≥ 13
   - **B1 (Low Risk)** if: All dimensions ≤ 3, Majority ≤ 2, and Total ≤ 12

3. **Document Baseline Assignment**
   - Record risk scores for each dimension
   - Document baseline assignment rationale
   - Identify controls in scope (B1: 23, B2: 61, B3: 72 controls)

**See**: [Baseline Selection Questionnaire](../../change-control/20260129143000-BASELINE-SELECTION-QUESTIONNAIRE.md) for detailed methodology.

---

### Phase 1: Pre-Assessment Preparation

**Objectives**:
- Identify assessment scope
- Select participants
- Gather preliminary evidence

**Activities**:

1. **Define Scope**
   - AI system(s) or portfolio being assessed
   - Baseline determined from Phase 0 (B1/B2/B3)
   - Profile selected or customized (framework profile or organization-specific)
   - All dimensions or focused assessment (by function or dimension)

2. **Select Participants**
   - One or more representatives per audience
   - Ensure organization-wide visibility (not just department)
   - Select for candor over optimism

3. **Set Expectations**
   - Confidentiality of individual responses
   - Honesty valued over inflated scores
   - No penalties for current state
   - Timeframe: 30-45 minutes per audience

4. **Gather Evidence** (Recommended)
   - AI project documentation
   - Policy and procedure documents
   - Organizational charts showing AI roles
   - Tools and platform inventories
   - Recent audit or compliance reports

### Phase 2: Conduct Assessment

**Format Options**:

| Format | Description | When to Use |
|--------|-------------|-------------|
| Self-Assessment | Each stakeholder completes independently | Distributed teams; initial quick assessment |
| Facilitated Interview | Assessor walks through questions | Detailed assessment; evidence gathering |
| Workshop | Group assessment with discussion | Alignment building; consensus required |

**Best Practices**:

- **Use evidence**: Score based on what exists today, not plans
- **Be specific**: Note examples and evidence for each score
- **Flag uncertainty**: Mark questions where uncertain for follow-up
- **Capture notes**: Document "why" behind each score
- **Avoid inflation**: If you can't show evidence in 10 minutes, score is likely too high

### Phase 3: Maturity Assessment

**Step 1: Individual Control Scoring**
- Assess each control in the profile using ML1-5 scale
- Use evidence-based evaluation (see maturity level definitions)
- Score: ML1=0, ML2=1, ML3=2, ML4=3, ML5=4
- If multiple assessors: Average scores and round to nearest integer

**Step 2: Profile Score Calculation**

Profile score measures achievement against the profile's target maturity:

```
Profile Target Score = Σ (Target Maturity for each control in profile)
Profile Actual Score = Σ (Assessed Maturity for each control in profile)
Profile Achievement = (Actual / Target) × 100%

Example: Healthcare profile with 48 controls, target ML3 (=2 points each)
- Profile Target: 48 controls × 2 points = 96 points
- Actual Assessment: Sum of all control scores = 104 points
- Profile Achievement: 104/96 = 108% ✅ Exceeding target
```

**Step 3: Baseline-Relative Score**

Baseline-relative score shows coverage of the full risk baseline:

```
Baseline Max Score = (Controls in Baseline) × 4 points
Baseline Achievement = (Profile Actual Score / Baseline Max) × 100%

Example: B2 baseline (61 controls), profile uses 48 of them
- Baseline Max: 61 × 4 = 244 points
- Profile Actual: 104 points
- Baseline Coverage: 104/244 = 43%
```

**Step 4: Framework-Relative Score**

Framework-relative score enables universal benchmarking:

```
Framework Max Score = 72 controls × 4 points = 288 points
Framework Achievement = (Profile Actual Score / 288) × 100%

Example:
- Profile Actual: 104 points
- Framework Achievement: 104/288 = 36%
```

**Step 5: Function and Dimension Breakdown**

Calculate scores by function and dimension for gap analysis:

```
Function Score = (Sum of Control Scores in Function) / (Max for those controls) × 100%

Example: GOVERN function with 14 controls in profile, target ML3 (2 points each)
- Scores: 2,3,2,2,1,3,2,2,0,2,3,2,2,3
- Actual Sum: 29 points
- Target: 14 × 2 = 28 points
- Function Achievement: 29/28 = 104% ✅

MEASURE function with 15 controls in profile
- Actual Sum: 18 points
- Target: 15 × 2 = 30 points
- Function Achievement: 18/30 = 60% ⚠️ Gap
```

### Phase 4: Hierarchical Profile Scoring (If Applicable)

For organizations with nested profiles (parent-child relationships):

**Attribution Types**:
- **Direct**: Control assessed at this profile level (no delegation)
- **Single**: One child profile fully owns the control (100% attribution)
- **Distributed**: Multiple children share responsibility (equal or weighted)

**Composite Score Calculation**:
```
Parent Control Score = Σ (Child Score × Attribution Weight)

Example: Distributed with equal attribution (3 business units)
- Child A: ML3 (2 points), 33% → 0.66
- Child B: ML4 (3 points), 33% → 0.99
- Child C: ML2 (1 point), 34% → 0.34
- Parent Score: 1.99 ≈ ML3
```

**Parent Profile Score**:
```
Sum all parent control scores (direct + delegated)
Calculate against parent's target maturity
```

**See**: [AIMF-PROFILES-GUIDE.md](AIMF-PROFILES-GUIDE.md#profile-attribution) for detailed attribution specification.

---

### Phase 5: Results Analysis and Gap Identification

**Gap Analysis Questions**:
- Is the profile target being met? (Profile Achievement ≥ 100%?)
- Which functions are below target?
- Which dimensions are lagging?
- Are gaps clustered (e.g., all MEASURE controls)?
- What are the lowest-scoring individual controls (ML1 = 0)?
- Which controls are one level below target (quick wins)?

**Maturity Distribution Analysis**:

| Maturity Distribution | Interpretation |
|----------------------|----------------|
| Mostly ML1-2 (0-1 points) | Early implementation; foundational work needed |
| Mixed ML2-3 (1-2 points) | Standardization in progress; nearing target |
| Mostly ML3 (2 points) | Meeting target; ready for measured management |
| Mixed ML3-4 (2-3 points) | Exceeding baseline; strong capability |
| Some ML4-5 (3-4 points) | Industry-leading in select areas; optimization culture |

**Score Interpretation**:

| Profile Achievement | Interpretation | Recommended Focus |
|---------------------|----------------|-------------------|
| < 60% | Critical gaps | Prioritize ML1→ML2 (documentation and ownership) |
| 60-79% | Below expectations | Focus ML2→ML3 (consistency and standardization) |
| 80-99% | Approaching target | Close gaps to reach ML3 baseline |
| 100-119% | Meeting target | Maintain; selective advancement to ML4 |
| ≥ 120% | Exceeding expectations | Mature organization; ML4-5 optimization |

---

## Assessment Questions

### Coverage of this question bank

**This bank covers 72/72 controls: one question and one evidence expectation for every
`Control_ID` in `core/AIMF-CONTROL-CATALOG.csv`** (GOVERN 19, MAP 18, MEASURE 22,
MANAGE 13). Every catalog control appears in exactly one audience table below, and
`python3 scripts/aimf_mappings.py check` fails if the bank and the catalog disagree on the
control set — a control with no question, a control appearing twice, or an ID that is not
in the catalog.

Questions are routed to the audience that has to produce the evidence. The default follows
the catalog's `Dimension` (`D1` → Leadership, `D2` → Governance, `D3` → Technical, `D4` →
Change Agent). Four controls whose primary evidence is a compliance record sit with
Governance rather than their dimension's audience: `GOV-1.4` (compliance monitoring) and
`MEA-1.3` (independent evaluation), plus `MAP-1.5` (risk tolerance) and `MAN-4.3` (incident
reporting), which have been in the Governance table since v1.0.4. The Governance table is
therefore short — the catalog attributes only two controls to `D2` (`MAP-1.6`,
`MEA-2.10`) — and an assessor may ask any question of any audience provided the same
evidence is scored.

**How to score a question.** Ask it, then score 0-4 against what the interviewee can put on
the table in the session: nothing documented → ML1 (0); a document exists → ML2 (1);
documented and applied organization-wide → ML3 (2); applied and measured → ML4 (3);
measured and systematically improved → ML5 (4). The evidence column names the artefacts
that carry a score above ML1. Record the question asked, the artefact produced and the
score, so that a second assessor can reproduce the number.

### Assessment Questions by Audience

Each row is one control: the question the assessor asks, and the evidence the answer must
be supported by. A row is scored once per assessment on the 0-4 scale described above.

#### Leadership Assessment (24 controls)

| Control | Question | Evidence to Look For |
|---------|----------|---------------------|
| GOV-1.1 | Has the organization established documented policies recognizing AI legal and regulatory requirements? | Policy documents; regulatory mapping |
| GOV-1.2 | Is every AI system in scope documented with its purpose, use case and risk classification, and is that classification approved before use? | AI system registry; classification record; approval sign-off; review dates |
| GOV-1.3 | Are AI risks managed inside the enterprise risk framework, with AI-specific appetite statements and risk thresholds? | Enterprise risk register entries; AI risk appetite statement; escalation records; board risk report |
| GOV-1.5 | Do AI policies require environmental impact to be considered, and is it assessed for the systems where it is material? | Policy clause; environmental assessment for named systems; energy or carbon figures |
| GOV-1.6 | Is there a documented decommissioning process covering data retention, disposal and stakeholder notification? | Decommissioning procedure; a completed retirement record; disposal evidence; notification log |
| GOV-1.7 | Do third-party AI arrangements carry documented risk assessment, contractual AI provisions and ongoing monitoring obligations? | Vendor risk assessments; contract clauses; vendor inventory; monitoring reports |
| GOV-2.1 | Are AI risk responsibilities assigned by role, with escalation paths that staff can name? | RACI matrix; role descriptions; escalation path; a named owner per system |
| GOV-2.3 | Is there senior leadership engagement and oversight of AI risk management? | Committee charter; meeting minutes; reporting cadence |
| GOV-6.1 | Are adequate resources (budget, personnel, tools) allocated for AI governance? | Budget documentation; headcount; tool inventory |
| GOV-6.2 | Is there a funded plan to build AI governance capability, and is progress against it reviewed? | Capability roadmap; training and tooling budget lines; review minutes; skills inventory |
| MAN-1.1 | Is there a documented go/no-go decision with stated criteria and a recorded approval before an AI system is deployed? | Decision record per system; criteria; approver sign-off; one conditioned or rejected case |
| MAN-1.2 | Are AI risks prioritized against defined criteria, and does that priority drive resourcing? | Prioritization method; risk-ranked register; allocation decisions traceable to the top risks |
| MAN-1.3 | Are response plans documented for the highest-priority AI risks, each with a named owner and date? | Risk treatment plans; owner assignments; due dates; completion evidence |
| MAN-1.4 | Is residual AI risk documented and accepted by a named accountable person before deployment? | Residual risk register; acceptance signature; communication to downstream owners |
| MAN-2.1 | Is a non-AI or simpler alternative evaluated and the choice justified in writing? | Options analysis; cost-benefit comparison; documented rationale; approver |
| MAN-3.1 | Are third-party AI components and services monitored after contracting, with findings acted on? | Monitoring schedule; vendor performance reports; issues raised and closed; contract review records |
| MAP-1.1 | Is each AI system's intended purpose, beneficial use and deployment setting documented, including a legal review? | Purpose statement; deployment context; legal and regulatory review record |
| MAP-1.3 | Is the organization's AI strategy documented and reviewed against its mission at a defined cadence? | AI strategy document; review minutes; strategic KPIs; board or committee papers |
| MAP-1.4 | Is the business case for each AI system documented with value metrics and tracked outcomes? | Business case; value or ROI metrics; post-deployment value report |
| MAP-3.1 | Are expected benefits documented before investment, with a method for validating them afterwards? | Benefits analysis; quantified baseline; validation plan; measured results |
| MAP-3.2 | Are costs documented, including non-monetary costs such as trust and operational burden? | Cost analysis; total-cost model; non-monetary assessment; link to the risk tolerance statement |
| MAP-4.1 | Is third-party AI mapped for technical and legal risk before use, with the assessment recorded? | Third-party risk assessment; legal review; dependency or data-flow map |
| MAP-4.2 | Are internal controls over third-party AI components documented, implemented and tested? | Control descriptions; implementation evidence; effectiveness test results |
| MAP-5.1 | Is an impact assessment completed for affected individuals and groups, with findings feeding the decision? | Impact assessment; stakeholder input; mitigation decisions; impact report |

#### Technical Assessment (30 controls)

| Control | Question | Evidence to Look For |
|---------|----------|---------------------|
| MAN-2.2 | Are there mechanisms that sustain the system's value in use, and monitoring that would catch value decay? | Maintenance plan; usage and value monitoring; periodic review of continued need |
| MAN-2.3 | Are procedures defined for risks that were not anticipated, including recovery and lessons learned? | Emergent-risk procedure; incident playbook; recovery records; lessons-learned log |
| MAN-2.4 | Are there mechanisms to disengage or deactivate AI systems? | Deactivation procedures; testing records |
| MAN-3.2 | Are pre-trained or third-party models tracked for version changes and performance drift? | Model inventory with versions; change notifications; re-evaluation records |
| MAN-4.1 | Are post-deployment monitoring, appeal and decommissioning plans implemented, not only written? | Live monitoring configuration; appeal process records; tested decommissioning plan |
| MAN-4.2 | Are measurable improvements from monitoring fed back into system updates? | Improvement backlog; release notes tying changes to findings; stakeholder input |
| MAP-2.1 | Is each system's task and method formally categorized, with the method documented? | Task taxonomy; method documentation; classification record |
| MAP-2.2 | Are the system's knowledge limits and required human oversight documented and enforced? | Boundary documentation; out-of-scope behaviour; oversight requirement; guardrail configuration |
| MAP-2.3 | Is the scientific methodology documented, including the TEVV approach and its known limitations? | Methodology document; TEVV plan; validity discussion; independent or peer review |
| MAP-3.3 | Is the application scope specified, and are scope changes controlled and approved? | Scope statement; change log; scope-drift monitoring; approval for each change |
| MAP-3.5 | Are human oversight processes designed, documented and shown to work in practice? | Oversight procedure; role assignments; override records; effectiveness assessment |
| MEA-1.1 | Is there a defined set of risk metrics per AI system, and are they wired into a measurement process? | Measurement framework; metric definitions; instrumentation or dashboard configuration |
| MEA-1.2 | Are the chosen metrics themselves reviewed for whether they measure what they claim? | Metric validation studies; revision history; false-positive and false-negative analysis |
| MEA-2.1 | Are test sets, metrics and tools recorded so that a third party could reproduce the evaluation? | Test documentation; dataset versions; tool configuration; version-controlled test scripts |
| MEA-2.2 | Do human-subject evaluations use ethics review, informed consent and representative sampling? | Ethics or IRB approval; consent records; sampling rationale; participant protections |
| MEA-2.3 | Are performance and assurance criteria defined before testing and demonstrated under deployment-like conditions? | Acceptance criteria; results under deployment conditions; sign-off against the criteria |
| MEA-2.4 | Is AI system functionality monitored in production? | Monitoring dashboards; alert configurations; runbooks |
| MEA-2.5 | Is validity and reliability demonstrated, including generalizability beyond the test set? | Validation report; out-of-distribution tests; reliability statistics; drift evidence |
| MEA-2.6 | Are safety risks evaluated with residual risks documented? | Safety assessment reports; residual risk register |
| MEA-2.7 | Is the system evaluated against adversarial attack, with resilience measures documented and retested? | Threat model; adversarial or red-team results; resilience measures; retest dates |
| MEA-2.8 | Are transparency and accountability risks assessed, and is the documentation adequate for those affected? | Transparency assessment; accountability mapping; published documentation |
| MEA-2.9 | Can the model's outputs be explained to the people who must act on them, at the level of detail they need? | Model documentation; explanation method; interpretation guidance; user-facing explanations |
| MEA-2.11 | Is bias tested across the affected populations with multiple metrics, and are mitigations recorded? | Fairness results by group; metric definitions; mitigation records; retest cadence |
| MEA-2.12 | Is the environmental impact of training and running the system measured and documented? | Energy or compute estimates; carbon figures; sustainability assessment; efficiency targets |
| MEA-2.13 | Is the effectiveness of the testing programme itself evaluated? | TEVV review; coverage analysis; defects found after test; process changes made |
| MEA-3.1 | Is there a standing process that tracks known and emergent AI risks over time, with a named owner? | Risk tracking log; review cadence; named owner; entries for emergent risks |
| MEA-3.2 | Where a setting resists conventional measurement, are alternative methods used and their limits documented? | Method rationale; documented limitations; results from multiple methods; expert judgment record |
| MEA-4.1 | Is measurement tied to the actual deployment context rather than to benchmark data alone? | Context analysis; tests on deployment data; domain expert input |
| MEA-4.2 | Are measurement results reviewed by domain experts who are independent of the build team? | Review records; reviewer independence; disagreements and their resolution |
| MEA-4.3 | Are performance changes detected and investigated, with root cause and action recorded? | Trend reports; drift alerts; root cause analyses; corrective actions |

#### Governance Assessment (6 controls)

| Control | Question | Evidence to Look For |
|---------|----------|---------------------|
| GOV-1.4 | Is compliance with AI policy monitored on a schedule, and are findings tracked to closure? | Compliance monitoring plan; KPI definitions; audit findings; closure evidence |
| MAP-1.5 | Are organizational risk tolerances for AI formally defined? | Risk appetite statements; approval records |
| MAP-1.6 | Are socio-technical requirements elicited with stakeholder input and traced into testing? | Requirements specification; traceability matrix; stakeholder input records |
| MEA-1.3 | Are internal experts and independent assessors involved in evaluation, with independence documented? | Assessment scope; assessor independence statement; assessment reports; external review |
| MEA-2.10 | Are privacy risks examined and documented for AI systems? | Privacy impact assessments; privacy review records |
| MAN-4.3 | Are AI incidents communicated to relevant stakeholders? | Incident records; communication logs |

#### Change Agent Assessment (12 controls)

| Control | Question | Evidence to Look For |
|---------|----------|---------------------|
| GOV-2.2 | Is AI risk training role-based and refreshed, with completion and competence recorded? | Training curriculum by role; completion records; competency assessment; refresh cycle |
| GOV-3.1 | Do AI teams include the required interdisciplinary expertise, and is team composition reviewed? | Team composition records; expertise requirements; inclusion metrics |
| GOV-3.2 | Is demographic representation in AI teams monitored, with documented action on findings? | Representation data; hiring and promotion analysis; action plans; progress reviews |
| GOV-4.1 | Is a culture of AI risk awareness fostered? | Training records; awareness campaigns; culture surveys |
| GOV-4.2 | Is stakeholder feedback on AI systems collected systematically and shown to change decisions? | Feedback intake; decision log linking feedback to changes; response records |
| GOV-4.3 | Is there a proactive AI transparency communication programme, with published reports? | Transparency report; communication plan; published disclosures; correction notices |
| GOV-5.1 | Does the organization take part in external AI governance forums, standards bodies or regulator dialogue? | Membership records; consultation responses; regulator correspondence; attendance |
| GOV-5.2 | Are research collaborations with academic institutions formalized and documented? | Partnership agreements; publication record; knowledge-exchange activities |
| MAP-1.2 | Are interdisciplinary teams with diverse competencies involved? | Team composition records; diversity metrics |
| MAP-3.4 | Are operator proficiency requirements defined, assessed and certified where needed? | Proficiency requirements; assessment records; certification; training linkage |
| MAP-5.2 | Are affected stakeholders engaged to understand impacts, with the engagement recorded? | Engagement plan; participant lists; findings; changes made |
| MEA-3.3 | Are end user and community feedback processes established? | Feedback channels; response records; feedback analysis |

---

## Results Interpretation

### Example Assessment Report

```
═══════════════════════════════════════════════════════════════
AI MANAGEMENT FRAMEWORK (AIMF) ASSESSMENT REPORT
═══════════════════════════════════════════════════════════════

Organization: Regional Healthcare Provider
Assessment Date: 2026-01-29
AI System: Diagnostic Imaging Support AI
Baseline: B2 (Moderate Risk - 61 controls applicable)
Profile: Healthcare Profile (48 controls selected)
Target Maturity: ML3 (Defined) per control

───────────────────────────────────────────────────────────────
PROFILE ACHIEVEMENT
───────────────────────────────────────────────────────────────

Profile Score:        104 / 96 points  = 108% ✅ EXCEEDING TARGET
Profile Maximum:      104 / 192 points = 54%  (room for ML4-5 growth)
Baseline-Relative:    104 / 244 points = 43%  (43% of B2 baseline max)
Framework-Relative:   104 / 288 points = 36%  (36% of full framework max)

Status: MEETING PROFILE OBLIGATIONS with room for advancement

───────────────────────────────────────────────────────────────
FUNCTION BREAKDOWN
───────────────────────────────────────────────────────────────

┌──────────┬──────────┬────────┬────────┬─────────────────────┐
│ Function │ Actual   │ Target │ %      │ Status              │
├──────────┼──────────┼────────┼────────┼─────────────────────┤
│ GOVERN   │ 29/14    │ 28     │ 104%   │ ✅ Exceeding        │
│ MAP      │ 28/14    │ 28     │ 100%   │ ✅ Meeting target   │
│ MEASURE  │ 30/15    │ 30     │ 100%   │ ✅ Meeting target   │
│ MANAGE   │ 17/5     │ 10     │ 170%   │ ✅ Significantly    │
│          │          │        │        │    exceeding        │
└──────────┴──────────┴────────┴────────┴─────────────────────┘

All functions meeting or exceeding target maturity.

───────────────────────────────────────────────────────────────
DIMENSION BREAKDOWN
───────────────────────────────────────────────────────────────

┌────────────────────────┬────────┬────────┬─────────────────┐
│ Dimension              │ Actual │ Target │ Achievement     │
├────────────────────────┼────────┼────────┼─────────────────┤
│ D1: Governance & Risk  │ 58     │ 50     │ 116% ✅         │
│ D2: Data Governance    │ 24     │ 20     │ 120% ✅         │
│ D3: Technical Ops      │ 18     │ 20     │  90% ⚠️ Gap     │
│ D4: Culture & Change   │ 4      │ 6      │  67% ⚠️ Gap     │
└────────────────────────┴────────┴────────┴─────────────────┘

Gaps identified in D3 (Technical Ops) and D4 (Culture).

───────────────────────────────────────────────────────────────
MATURITY DISTRIBUTION
───────────────────────────────────────────────────────────────

ML5 (Optimizing):     8 controls  (17%) - Industry leading
ML4 (Managed):        12 controls (25%) - Data-driven
ML3 (Defined):        20 controls (42%) - Standardized ✅ Target
ML2 (Developing):     6 controls  (13%) - Documented but inconsistent
ML1 (Initial):        2 controls  ( 4%) - Ad-hoc

Primary Gaps (ML1-2):
1. MEA-2.4 Production Monitoring [D3] - ML1 (0) → Need ML3 (2)
2. GOV-4.1 Risk Culture Development [D4] - ML2 (1) → Need ML3 (2)
3. MEA-3.1 Continuous Risk Tracking [D3] - ML2 (1) → Need ML3 (2)
4. MAP-1.2 Team Diversity [D4] - ML2 (1) → Need ML3 (2)
5. MEA-2.11 Fairness Assessment [D3] - ML2 (1) → Need ML3 (2)

───────────────────────────────────────────────────────────────
RECOMMENDATIONS
───────────────────────────────────────────────────────────────

Priority 1: Close D3 Technical Operations gaps
- Implement production monitoring (MEA-2.4): ML1 → ML3
- Establish continuous risk tracking (MEA-3.1): ML2 → ML3
- Formalize fairness testing (MEA-2.11): ML2 → ML3

Priority 2: Advance D4 Culture initiatives
- Systematize risk culture program (GOV-4.1): ML2 → ML3
- Formalize team diversity requirements (MAP-1.2): ML2 → ML3

Overall: Strong foundation with targeted gaps in technical
operations and culture. Closing 8 controls from ML1-2 to ML3
would achieve 118% profile score.

Next Assessment: 6 months (after technical operations improvements)
```

---

## Common Assessment Pitfalls

### Pitfalls and Mitigations

| Pitfall | Description | Mitigation |
|---------|-------------|------------|
| **Aspiration Inflation** | Scoring based on plans, not reality | Ask "Can you show me evidence this exists today?" |
| **Best Case Bias** | Scoring based on best team, not norm | Score reflects consistent, organization-wide capability |
| **All-or-Nothing** | Only scoring 0, 2, or 4 | Use full scale (0-4); most organizations have many 1s and 2s |
| **Documentation ≠ Implementation** | Assuming documented = done | ML2 (1 point) is documented; ML3 (2 points) requires consistent application |
| **Compliance ≠ Measurement** | Tracking completion, not performance | Tracking "it was done" is ML3; measuring "how well" is ML4 |
| **Evidence Gaps** | High scores without proof | If no evidence in 10 minutes, score is inflated |
| **Single Perspective** | One stakeholder assesses | Include all four audience assessments for validation |

---

## Assessment Frequency

| Organizational Maturity | Recommended Frequency |
|------------------------|----------------------|
| **ML1-2** (Initial to Developing) | Every 3-6 months (rapid improvement expected) |
| **ML3** (Defined) | Every 6-12 months (building consistency) |
| **ML4** (Managed) | Annually (metrics provide continuous visibility) |
| **ML5** (Optimizing) | Annually (innovation tracking) |

| Trigger Event | Action |
|---------------|--------|
| **Initial baseline** | Before beginning improvement work |
| **Baseline change** | When AI system risk changes (scope expansion, autonomy increase, new regulations) |
| **Profile update** | When controls added/removed from profile |
| **Major incidents** | After significant AI-related incidents or audit findings |
| **Regulatory changes** | When new AI regulations apply |
| **Technology changes** | After significant platform or architecture changes |

---

## Action Planning

### Using Assessment Results

1. **Validate Baseline Assignment**
   - Confirm AI system risk profile is current
   - Review if baseline escalation is needed (system changes, scope expansion)
   - Document any baseline adjustments

2. **Review Profile Adequacy**
   - Verify profile covers all applicable regulatory requirements
   - Confirm control selection appropriate for organizational context
   - Adjust profile if gaps identified

3. **Prioritize Maturity Improvements**
   - **First Priority**: Close ML1 (0-point) gaps → ML2 (document and assign)
   - **Second Priority**: Advance ML2 (1-point) → ML3 (standardize and enforce)
   - **Third Priority**: Selectively advance ML3 → ML4 (measure and manage)
   - Consider control dependencies (e.g., can't have ML4 monitoring without ML3 governance)

4. **Develop Implementation Roadmap**
   - Use [Maturity Level Progression Guides](maturity-level-guides/) for detailed roadmaps
   - ML1→ML2: 1-3 months per control (documentation effort)
   - ML2→ML3: 6-12 months per control (standardization and adoption)
   - ML3→ML4: 12-18 months per control (measurement infrastructure)
   - ML4→ML5: 18-36 months per control (innovation culture)

5. **Set Measurable Targets**
   - Define target profile achievement percentage (e.g., 100% within 12 months)
   - Specify per-control maturity targets (can adjust from default ML3)
   - Establish interim milestones (e.g., 80% achievement in 6 months)
   - Schedule reassessment to track progress

---

## Assessment Documentation Template

### Assessment Record

```
═══════════════════════════════════════════════════════════════
AIMF ASSESSMENT RECORD
═══════════════════════════════════════════════════════════════

Organization: ___________________________________________________
Assessment Date: ________________________________________________
Assessment Lead: ________________________________________________
Assessment Type: [ ] Self [ ] Facilitated [ ] Workshop

Participants:
- Leadership: ___________________________________________________
- Technical: ____________________________________________________
- Governance: ___________________________________________________
- Change Agent: _________________________________________________

───────────────────────────────────────────────────────────────
SCOPE DEFINITION
───────────────────────────────────────────────────────────────

AI System(s): ___________________________________________________
Risk Baseline: [ ] B1 (Low - 23 controls)
               [ ] B2 (Moderate - 61 controls)
               [ ] B3 (High - 72 controls)
Profile: ________________________________________________________
Controls in Profile: ______ controls
Dimensions Assessed: [ ] All [ ] Selected: _____________________

───────────────────────────────────────────────────────────────
RESULTS SUMMARY
───────────────────────────────────────────────────────────────

Profile Achievement:     _____ / _____ points = _____%
Baseline-Relative:       _____ / _____ points = _____%
Framework-Relative:      _____ / _____ points = _____%

Function Scores:
- GOVERN:   _____ / _____ = _____%
- MAP:      _____ / _____ = _____%
- MEASURE:  _____ / _____ = _____%
- MANAGE:   _____ / _____ = _____%

Dimension Scores:
- D1 (Governance & Risk):  _____%
- D2 (Data Governance):    _____%
- D3 (Technical Ops):      _____%
- D4 (Culture & Change):   _____%

Maturity Distribution:
- ML5 (Optimizing):  ___ controls (___%)
- ML4 (Managed):     ___ controls (___%)
- ML3 (Defined):     ___ controls (___%) ← Target
- ML2 (Developing):  ___ controls (___%)
- ML1 (Initial):     ___ controls (___%)

───────────────────────────────────────────────────────────────
GAP ANALYSIS
───────────────────────────────────────────────────────────────

Top 5 Priority Controls (Lowest Maturity):
1. ____________________________________________ - ML___ (Gap: ___)
2. ____________________________________________ - ML___ (Gap: ___)
3. ____________________________________________ - ML___ (Gap: ___)
4. ____________________________________________ - ML___ (Gap: ___)
5. ____________________________________________ - ML___ (Gap: ___)

Key Gaps:
__________________________________________________________________
__________________________________________________________________

Priority Actions:
__________________________________________________________________
__________________________________________________________________

Next Assessment Date: ___________________________________________
```

---

## References

- CMMI Institute Assessment Methodology
- ISO 19011:2018 Guidelines for auditing management systems
- NIST Cybersecurity Framework Assessment Guidance

---

**Related Documents**: [Framework Overview](../core/AIMF-FRAMEWORK-OVERVIEW.md) | [Risk Baselines](AIMF-RISK-BASELINES.md) | [Maturity Levels](AIMF-MATURITY-LEVELS.md) | [Profiles Guide](AIMF-PROFILES-GUIDE.md) | [Control Catalog](../core/AIMF-CONTROL-CATALOG.csv)
