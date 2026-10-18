# AI Management Framework (AIMF) by PraeSyn
## Assessment Guide

**© 2026 PraeSyn, LLC. All rights reserved.**
Licensed under CC BY-NC-ND 4.0

**Version**: 1.0
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

**This is a partial bank: 12 of the 72 controls have a mapped question here** (GOV-1.1,
GOV-2.3, GOV-4.1, GOV-6.1, MAP-1.2, MAP-1.5, MEA-2.4, MEA-2.6, MEA-2.10, MEA-3.3, MAN-2.4,
MAN-4.3). It is published as worked examples of the format — control ID, question, and the
evidence an assessor should look for — not as a complete instrument. For the other 60
controls, the assessor derives the question from the control's statement and evidence
criteria in `core/AIMF-CONTROL-CATALOG.csv` and its objective in
`core/AIMF-CONTROL-CATALOG.md`, and records the question used in the assessment workbook so
two assessors can reproduce the score. A complete 72-control bank is tracked as its own
work item against this release; until it ships, do not quote this section as full coverage.

### Sample Assessment Questions by Audience

#### Leadership Assessment (Sample)

| Control | Question | Evidence to Look For |
|---------|----------|---------------------|
| GOV-1.1 | Has the organization established documented policies recognizing AI legal and regulatory requirements? | Policy documents; regulatory mapping |
| GOV-2.3 | Is there senior leadership engagement and oversight of AI risk management? | Committee charter; meeting minutes; reporting cadence |
| GOV-6.1 | Are adequate resources (budget, personnel, tools) allocated for AI governance? | Budget documentation; headcount; tool inventory |

#### Technical Assessment (Sample)

| Control | Question | Evidence to Look For |
|---------|----------|---------------------|
| MEA-2.4 | Is AI system functionality monitored in production? | Monitoring dashboards; alert configurations; runbooks |
| MEA-2.6 | Are safety risks evaluated with residual risks documented? | Safety assessment reports; residual risk register |
| MAN-2.4 | Are there mechanisms to disengage or deactivate AI systems? | Deactivation procedures; testing records |

#### Governance Assessment (Sample)

| Control | Question | Evidence to Look For |
|---------|----------|---------------------|
| MAP-1.5 | Are organizational risk tolerances for AI formally defined? | Risk appetite statements; approval records |
| MEA-2.10 | Are privacy risks examined and documented for AI systems? | Privacy impact assessments; privacy review records |
| MAN-4.3 | Are AI incidents communicated to relevant stakeholders? | Incident records; communication logs |

#### Change Agent Assessment (Sample)

| Control | Question | Evidence to Look For |
|---------|----------|---------------------|
| GOV-4.1 | Is a culture of AI risk awareness fostered? | Training records; awareness campaigns; culture surveys |
| MAP-1.2 | Are interdisciplinary teams with diverse competencies involved? | Team composition records; diversity metrics |
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
