# AIMF Change Plan: Tier-to-Baseline Conceptual Revision

**Change Control ID**: CP-2026-001
**Change Type**: Major Conceptual Revision
**Framework Version**: 1.0 (No version increment - pre-publication refinement)
**Date Created**: 2026-01-29
**Status**: Planning
**Estimated Effort**: 26-38 hours (4-6 working days)

---

## Executive Summary

### Change Rationale

The current AIMF framework conflates two orthogonal concepts under "Tiers":
- **Organizational maturity** (where the organization is in its journey)
- **System risk level** (characteristics of the AI systems being deployed)

This creates conceptual confusion and operational ambiguity, particularly when:
- A mature organization deploys low-risk AI (should they use T3 rigor for everything?)
- A startup deploys high-risk AI (are they forced into T1 despite needing T3 controls?)

### Solution

Separate the concepts into three distinct dimensions:

| Dimension | Purpose | Values |
|-----------|---------|--------|
| **Baseline (B1/B2/B3)** | Risk-based control scoping | Which controls apply based on AI system risk |
| **Maturity Level (ML1-5)** | Implementation quality assessment | How well controls are implemented (CMMI scale) |
| **Profile** | Context-specific refinement | Fine-tuning from baseline for industry/org/system |

### Impact

- **Conceptual**: Clearer separation between scope and quality
- **Operational**: Better assessment and scoring model
- **Framework**: More flexible, supports hierarchical profiles and composite scoring
- **Documentation**: Extensive terminology changes across all documents

---

## Change Overview

### Core Terminology Changes

| Old Term | New Term | Rationale |
|----------|----------|-----------|
| Tier 1 (T1) Initial | Baseline 1 (B1) Low Risk | Reflects risk-based scoping, not org stage |
| Tier 2 (T2) Mature | Baseline 2 (B2) Moderate Risk | Reflects risk level of AI systems |
| Tier 3 (T3) High-Risk | Baseline 3 (B3) High Risk | Already correct - kept risk focus |
| T1/T2/T3 Requirements | Implementation Examples (ML1-2, ML3, ML4-5) | Shows what different maturity looks like |
| Tier progression | Maturity level progression | Separate organizational growth from scope |
| 0-3 Assessment Scale | 1-5 Maturity Scale (or 0-4) | CMMI alignment, better granularity |

### New Concepts Introduced

1. **Risk Characterization Questions**: Determines B1/B2/B3 selection based on AI system characteristics
2. **Baseline Selection Methodology**: Process for determining which baseline applies
3. **Profile Attribution Rules**: How hierarchical profiles aggregate scores (single/distributed/weighted)
4. **Per-Control Target Maturity**: Profiles can set custom maturity targets per control (default: ML3)
5. **Composite Scoring Architecture**: Framework-relative, baseline-relative, and profile scores

---

## Implementation Phases

### Phase 1: Definition Documents (PRIORITY 1)

**Objective**: Establish new conceptual foundation

**Documents**:
1. AIMF-FRAMEWORK-OVERVIEW.md
2. AIMF-IMPLEMENTATION-TIERS.md → AIMF-RISK-BASELINES.md (rewrite)
3. New: AIMF-MATURITY-LEVELS.md (detailed ML1-5 definitions)

**Status**: Not Started
**Estimated Effort**: 8-12 hours
**Dependencies**: None (foundational)

---

### Phase 2: Data Structures (PRIORITY 1)

**Objective**: Update control catalog to reflect new model

**Documents**:
1. AIMF-CONTROL-CATALOG.csv (column restructure)
2. AIMF-CONTROL-CATALOG.md (if separate documentation exists)

**Status**: Not Started
**Estimated Effort**: 3-4 hours
**Dependencies**: Phase 1 (need baseline definitions)

---

### Phase 3: Assessment & Scoring (PRIORITY 1)

**Objective**: Implement new assessment and scoring methodology

**Documents**:
1. AIMF-ASSESSMENT-GUIDE.md (major revision)
2. AIMF-PROFILES-GUIDE.md (attribution rules, scoring architecture)

**Status**: Not Started
**Estimated Effort**: 7-10 hours
**Dependencies**: Phase 1 & 2 (need definitions and data structure)

---

### Phase 4: Profile Documents (PRIORITY 2)

**Objective**: Update existing profiles to use new terminology

**Documents**:
1. profile-foundational.md
2. profile-balanced.md
3. profile-high-assurance.md
4. profile-financial-services.md
5. profile-healthcare.md
6. profile-government.md
7. profile-implementation-template.md
8. Example implementation profiles (2 files)

**Status**: Not Started
**Estimated Effort**: 3-4 hours
**Dependencies**: Phase 1 & 3 (need baseline and profile concepts)

---

### Phase 5: Maturity Guides (PRIORITY 2)

**Objective**: Rename and clarify maturity progression guides

**Documents**:
1. tier-transition-guides/ → maturity-level-guides/ (directory rename)
2. TIER-1-TO-2-GUIDE.md → MATURITY-LEVEL-1-TO-2-GUIDE.md
3. TIER-2-TO-3-GUIDE.md → MATURITY-LEVEL-2-TO-3-GUIDE.md
4. TIER-3-TO-4-GUIDE.md → MATURITY-LEVEL-3-TO-4-GUIDE.md
5. TIER-4-TO-5-GUIDE.md → MATURITY-LEVEL-4-TO-5-GUIDE.md
6. TIER-5-OPTIMIZATION-GUIDE.md → MATURITY-LEVEL-5-OPTIMIZATION-GUIDE.md

**Status**: Not Started
**Estimated Effort**: 2-3 hours
**Dependencies**: Phase 1 (need maturity level definitions)

---

### Phase 6: Function Documents (PRIORITY 3)

**Objective**: Update terminology in function-specific documents

**Documents**:
1. AIMF-FUNCTION-GOVERN.md
2. AIMF-FUNCTION-MAP.md
3. AIMF-FUNCTION-MEASURE.md
4. AIMF-FUNCTION-MANAGE.md

**Status**: Not Started
**Estimated Effort**: 2-3 hours
**Dependencies**: Phase 1 & 2

---

### Phase 7: Mapping Documents (PRIORITY 3)

**Objective**: Update terminology in standards mapping documents

**Documents**:
1. AIMF-DIMENSION-MAPPING.md
2. AIMF-ISO42001-MAPPING.md
3. AIMF-NIST-RMF-MAPPING.md
4. AIMF-ISO27001-MAPPING.md
5. AIMF-EXECUTIVE-ORDER-14110-MAPPING.md
6. AIMF-EXECUTIVE-ORDER-14179-MAPPING.md
7. GOVERN-FUNCTION-MATURITY-MAPPING.md
8. MAP-FUNCTION-MATURITY-MAPPING.md
9. MEASURE-FUNCTION-MATURITY-MAPPING.md
10. MANAGE-FUNCTION-MATURITY-MAPPING.md

**Status**: Not Started
**Estimated Effort**: 2-3 hours
**Dependencies**: Phase 1 & 2

---

### Phase 8: Supplemental Documents (PRIORITY 3)

**Objective**: Update terminology in supporting documents

**Documents**:
1. AIMF-GLOSSARY.md (add new terms, update definitions)
2. AIMF-FAQ.md (update Q&A for new model)
3. AIMF-REFERENCES.md (ensure consistency)
4. AIMF-FUTURE-PROFILES.md (update terminology)

**Status**: Not Started
**Estimated Effort**: 2-3 hours
**Dependencies**: Phase 1

---

### Phase 9: Diagrams & Assets (PRIORITY 3)

**Objective**: Update visual assets to reflect new model

**Documents**:
1. framework-architecture-diagram.md (update tier → baseline)
2. maturity-progression-diagram.md (validate correctness)
3. tier-comparison-infographic.md → baseline-comparison-infographic.md (rename & update)
4. profile-selection-flowchart.md (update with baseline selection)
5. standards-integration-diagram.md (validate)

**Status**: Not Started
**Estimated Effort**: 2-3 hours
**Dependencies**: Phase 1

---

### Phase 10: Root Documents (PRIORITY 3)

**Objective**: Update repository-level documents

**Documents**:
1. README.md (update framework description)
2. CHANGELOG.md (document changes)
3. QUALITY-ASSURANCE-CHECKLIST.md (validate against new model)
4. QA-VERIFICATION-REPORT.md (may need regeneration)
5. AIMF-V1.0-REVIEW-PLAN.md (update if needed)

**Status**: Not Started
**Estimated Effort**: 1-2 hours
**Dependencies**: All previous phases

---

## Detailed Change Specifications

### Critical Decisions Required

Before implementation, these decisions must be finalized:

| Decision | Options | Recommendation | Rationale |
|----------|---------|----------------|-----------|
| **Maturity Scoring Floor** | ML1=0 vs ML1=1 | ML1=0 (0-4 scale) | Incentivizes moving beyond ad-hoc |
| **Control Weighting** | Equal vs Weighted | Equal (v1.0) | Simpler, defensible; add weighting in v2.0 |
| **Baseline Control Counts** | Define exact counts | B1: 30-35, B2: 45-50, B3: 73 | Needs validation with risk questions |
| **Profile Attribution Default** | Implicit vs Explicit | Explicit specification required | Prevents ambiguity |
| **Default Target Maturity** | ML2, ML3, or custom | ML3 (Defined) | Industry standard "implemented" |

**Decision Status**: Pending - requires stakeholder approval

---

## Document-Specific Change Details

### 1. AIMF-FRAMEWORK-OVERVIEW.md

**File**: `core/AIMF-FRAMEWORK-OVERVIEW.md`
**Change Type**: Major Revision
**Lines Affected**: Multiple sections throughout

**Specific Changes**:

1. **Section: "Three Implementation Tiers" (lines 66-74)**
   - **OLD**: Describes T1/T2/T3 as organizational maturity stages
   - **NEW**: "Three Risk Baselines" describing control scope based on AI system risk
   - Update table to show B1/B2/B3 with risk-based characteristics

2. **Section: "Five Maturity Levels" (lines 56-64)**
   - **ADD**: Explicit statement that maturity measures implementation quality
   - **CLARIFY**: Maturity is orthogonal to baseline selection
   - **UPDATE**: Reference to 0-4 or 1-5 scoring scale (pending decision)

3. **NEW Section: "Framework Scoring Architecture"**
   - Add after maturity levels section
   - Explain profile targeting (actual vs target score)
   - Explain composite scoring for hierarchical profiles
   - Explain framework-relative vs baseline-relative scores

4. **Section: "Framework Application" (lines 107-132)**
   - Update "For Assessment" to reference baseline selection
   - Update "For Implementation" to reference maturity progression
   - Clarify baseline determines scope, maturity determines gaps

5. **Global Changes**:
   - Find/replace "tier" → "baseline" (with context awareness)
   - Find/replace "T1" → "B1", "T2" → "B2", "T3" → "B3"
   - Update all references to implementation rigor

**Validation**: Cross-reference with all other core documents

---

### 2. AIMF-IMPLEMENTATION-TIERS.md → AIMF-RISK-BASELINES.md

**File**: `implementation/AIMF-IMPLEMENTATION-TIERS.md`
**Change Type**: Complete Rewrite
**New Filename**: `implementation/AIMF-RISK-BASELINES.md`

**Specific Changes**:

1. **NEW Section: "Risk Characterization Methodology"**
   - Replace entire "Tier Selection Criteria" section
   - Add risk assessment questions (6-10 questions)
   - Add scoring logic (low/moderate/high) → B1/B2/B3
   - Decision tree for baseline selection

2. **Reframe All Baseline Definitions**:
   - **B1 Low Risk**: 30-35 foundational controls
   - **B2 Moderate Risk**: 45-50 comprehensive controls
   - **B3 High Risk**: All 73 controls
   - Remove all "organizational journey" language
   - Focus on AI system characteristics, not org maturity

3. **Remove "Tier Progression" Section**:
   - This concept moves to maturity level guides
   - Organizations don't "progress" between baselines
   - Different AI systems may require different baselines

4. **NEW Section: "Baseline Assignment Examples"**:
   - Medical diagnosis AI → B3 (high risk, patient safety)
   - Internal chatbot → B1 (low risk, limited impact)
   - Credit decisioning → B2-B3 (regulatory, fairness concerns)
   - Content recommendation → B1-B2 (impact dependent)

5. **Update "Evidence Requirements" Sections**:
   - Reframe as "Controls in Scope" per baseline
   - Reference maturity assessment for implementation quality
   - Remove "tier compliance" language

**Validation**: Test risk assessment questions with example scenarios

---

### 3. AIMF-CONTROL-CATALOG.csv

**File**: `core/AIMF-CONTROL-CATALOG.csv`
**Change Type**: Column Structure Update

**Column Changes**:

1. **Rename Columns**:
   ```
   T1_Requirements → Implementation_Basic
   T2_Requirements → Implementation_Defined
   T3_Requirements → Implementation_Advanced
   ```

2. **Add New Columns** (insert after Profile_Tags):
   ```
   Baseline_Applicability (values: B1, B2, B3, or B1|B2, B2|B3, B1|B2|B3)
   Default_Target_Maturity (default: 3, can be 2-5)
   ```

3. **Update Column Descriptions**:
   - Implementation_Basic: "Example of ML1-2 implementation (ad-hoc to developing)"
   - Implementation_Defined: "Example of ML3 implementation (defined, standardized)"
   - Implementation_Advanced: "Example of ML4-5 implementation (managed to optimizing)"

4. **Content Updates**:
   - Review each control's Implementation_* descriptions
   - Ensure they reflect maturity characteristics, not tier/risk level
   - Assign Baseline_Applicability based on control criticality:
     - Foundational governance → B1|B2|B3
     - Advanced measurement → B2|B3
     - High-assurance validation → B3 only

5. **Validation Rules**:
   - Every control must have Baseline_Applicability
   - Default_Target_Maturity must be 2-5
   - Implementation_* descriptions must be distinct and progressive

**Estimated Rows Affected**: All 73 control rows

---

### 4. AIMF-ASSESSMENT-GUIDE.md

**File**: `implementation/AIMF-ASSESSMENT-GUIDE.md`
**Change Type**: Major Revision

**Specific Changes**:

1. **Section: "Scoring Scale" (lines 34-54)**
   - **REPLACE**: 0-3 scale with 1-5 maturity scale
   - **NEW TABLE**:
     ```
     | Score | Maturity Level | Definition |
     |-------|----------------|------------|
     | 0 or 1 | Initial | Ad-hoc, individual-dependent |
     | 2 | Developing | Documented but inconsistent |
     | 3 | Defined | Standardized, organization-wide |
     | 4 | Managed | Quantitatively measured |
     | 5 | Optimizing | Continuous improvement |
     ```
   - Decision: Use 0-4 scale (ML1=0) or 1-5 scale (ML1=1)

2. **Section: "Assessment Process" - NEW Pre-Phase**
   - **ADD**: "Phase 0: Baseline Selection"
   - Risk characterization questions
   - Baseline determination (B1/B2/B3)
   - Controls in scope identification

3. **Section: "Score Calculation" (lines 142-172)**
   - **REMOVE**: "Overall Tier Determination" (lines 162-172)
   - **ADD**: New sections:
     - "Profile Score Calculation" (actual/target percentage)
     - "Baseline-Relative Score" (coverage of full baseline)
     - "Framework-Relative Score" (universal benchmark)
   - **ADD**: Scoring formulas with examples

4. **NEW Section: "Hierarchical Profile Scoring"**
   - Insert after score calculation
   - Explain attribution (single/distributed/weighted)
   - Provide examples of composite scoring
   - Roll-up logic for nested profiles

5. **Section: "Results Interpretation" (lines 229-282)**
   - Update score interpretation matrix
   - Remove tier classification language
   - Add profile achievement bands:
     - < 80%: Below target
     - 80-99%: Approaching target
     - 100%: Meeting target
     - > 100%: Exceeding expectations (ML4-5 implementations)

6. **Section: "Assessment Questions" (lines 191-226)**
   - Validate questions still work with 1-5 scale
   - Update examples to reference maturity levels
   - Add note about baseline-specific question subsets

**Validation**: Test scoring formulas with example data

---

### 5. AIMF-PROFILES-GUIDE.md

**File**: `implementation/AIMF-PROFILES-GUIDE.md`
**Change Type**: Moderate Revision + Major New Content

**Specific Changes**:

1. **Section: "Relationship to Tiers and Maturity" (lines 87-148)**
   - **REPLACE**: "Tier" with "Baseline" throughout
   - **UPDATE**: Three Dimensions table to show Baseline/Maturity/Profile
   - **CLARIFY**: Baseline determines scope, maturity measures quality

2. **NEW Section: "Profile Attribution in Hierarchical Structures"**
   - Insert after "Profile Types" section
   - **Content**:
     - Single child implementation (100% attribution)
     - Distributed implementation (equal or weighted)
     - Explicit specification requirements
     - Examples with calculations
   - **YAML Example**: Profile definition with attribution rules

3. **NEW Section: "Per-Control Target Maturity"**
   - Insert in "What is a Profile?" section
   - Explain default target (ML3)
   - Show how profiles can override per control
   - Example: Critical control target = ML4, lower priority = ML2

4. **Section: "Available Framework Profiles" (lines 150-223)**
   - Update all "Tier Alignment" → "Baseline Applicability"
   - Update descriptions to reference baselines not tiers
   - Add "Default Target Maturity: 3" to each profile spec

5. **Section: "Profile Selection Methodology" (lines 300-457)**
   - Update Step 2 to reference baseline risk assessment
   - Update decision logic to use baseline terminology
   - Update regulatory requirements table with baseline mappings

6. **Section: "Creating Implementation Profiles" (lines 458-502)**
   - Add attribution specification to template requirements
   - Add per-control target maturity specification
   - Add parent/child profile relationship documentation

**Validation**: Ensure examples align with new scoring model

---

### 6-10. Tier Transition Guides → Maturity Level Guides

**Files**: All files in `implementation/tier-transition-guides/`
**Change Type**: Rename + Terminology Updates

**Changes Apply to All 5 Files**:

1. **Directory Rename**:
   ```
   implementation/tier-transition-guides/ → implementation/maturity-level-guides/
   ```

2. **File Renames**:
   ```
   TIER-1-TO-2-GUIDE.md → MATURITY-LEVEL-1-TO-2-GUIDE.md
   TIER-2-TO-3-GUIDE.md → MATURITY-LEVEL-2-TO-3-GUIDE.md
   TIER-3-TO-4-GUIDE.md → MATURITY-LEVEL-3-TO-4-GUIDE.md
   TIER-4-TO-5-GUIDE.md → MATURITY-LEVEL-4-TO-5-GUIDE.md
   TIER-5-OPTIMIZATION-GUIDE.md → MATURITY-LEVEL-5-OPTIMIZATION-GUIDE.md
   ```

3. **Global Find/Replace in Each File**:
   - "Tier 1" → "Maturity Level 1"
   - "Tier 2" → "Maturity Level 2"
   - "Tier 3" → "Maturity Level 3"
   - "Tier 4" → "Maturity Level 4"
   - "Tier 5" → "Maturity Level 5"
   - "T1" → "ML1" (where referring to maturity, not baseline)
   - "T2" → "ML2" (where referring to maturity)
   - "T3" → "ML3" (where referring to maturity)

4. **Header Updates**:
   ```
   OLD: "Target Audience: Organizations at Tier 2 (Developing)"
   NEW: "Target Audience: Organizations at Maturity Level 2 (Developing)"
   ```

5. **Content Validation**:
   - These guides are conceptually CORRECT
   - They describe maturity progression (how to improve implementation)
   - Only terminology needs updating, not content

**Note**: These files should NOT reference baselines—they're about improving implementation quality across whatever controls are in scope.

---

### 11-16. Framework Profile Documents

**Files**:
- `profiles/framework-profiles/profile-foundational.md`
- `profiles/framework-profiles/profile-balanced.md`
- `profiles/framework-profiles/profile-high-assurance.md`
- `profiles/framework-profiles/profile-financial-services.md`
- `profiles/framework-profiles/profile-healthcare.md`
- `profiles/framework-profiles/profile-government.md`

**Change Type**: Terminology Updates

**Changes Apply to All 6 Files**:

1. **Global Find/Replace**:
   - "Tier Alignment: Primarily T1 requirements" → "Baseline Applicability: B1 (Low Risk)"
   - "Tier Alignment: Primarily T2 requirements" → "Baseline Applicability: B2 (Moderate Risk)"
   - "Tier Alignment: Primarily T3 requirements" → "Baseline Applicability: B3 (High Risk)"
   - "Tier Alignment: T2-T3 requirements" → "Baseline Applicability: B2-B3 (Moderate to High Risk)"

2. **Add to Each Profile Header**:
   ```markdown
   **Default Target Maturity**: 3 (Defined - standardized, organization-wide)
   ```

3. **Update Profile Descriptions**:
   - Replace tier-based language with baseline-based language
   - Focus on risk characteristics of AI systems, not org stage
   - Clarify that profiles select controls from baseline(s)

4. **Specific Profile Adjustments**:
   - **Foundational**: "Based on B1 baseline controls"
   - **Balanced**: "Based on B1 and B2 baseline controls"
   - **High-Assurance**: "Includes all B1, B2, and B3 controls"
   - **Industry Profiles**: "Selects controls from B2 and B3 based on regulatory requirements"

---

## Quality Assurance Plan

### Pre-Implementation Validation

- [ ] All critical decisions finalized (scoring floor, weighting, etc.)
- [ ] Risk characterization questions validated with examples
- [ ] Baseline control counts determined (B1: X, B2: Y, B3: 73)
- [ ] Scoring formulas tested with sample data
- [ ] Attribution logic validated with hierarchical profile examples

### During Implementation

- [ ] Phase completion checklists
- [ ] Cross-document consistency checks after each phase
- [ ] Example scenario validation (e.g., "medical AI" should → B3, ML3 target)
- [ ] Terminology consistency (no "tier" references remain where "baseline" intended)

### Post-Implementation Validation

- [ ] All document links functional
- [ ] Glossary updated with all new terms
- [ ] FAQ updated with common questions about new model
- [ ] README accurately reflects framework structure
- [ ] All diagrams reflect current model
- [ ] Control catalog validates (no empty cells, consistent formatting)
- [ ] Example profiles work with new scoring model
- [ ] Maturity level guides reference correct terminology

### Validation Checklist Template

```markdown
## Document: [FILENAME]
- [ ] All "tier" references updated to "baseline" (where appropriate)
- [ ] All T1/T2/T3 references updated to B1/B2/B3 (where appropriate)
- [ ] Maturity level terminology consistent (ML1-5)
- [ ] No conceptual contradictions with core definitions
- [ ] Examples and scenarios align with new model
- [ ] Internal links functional
- [ ] External references accurate
- [ ] Version/date information current
```

---

## Risk Management

### Known Risks

| Risk | Impact | Mitigation |
|------|--------|------------|
| **Terminology inconsistency** | High - framework unusable if inconsistent | Automated find/replace + manual review + QA checklist |
| **Conceptual contradiction** | High - framework illogical if definitions conflict | Phase-based approach, definition docs first |
| **Broken cross-references** | Medium - navigation problems | Link validation after each phase |
| **Example misalignment** | Medium - confusion if examples don't match model | Validate all examples against new scoring formulas |
| **Lost "tier" references that should remain** | Low - some historical tier references may be valid | Context-aware replacement, not global find/replace |

### Contingency Plans

- **If timeline extends beyond 6 days**: Pause after Phase 3, validate critical documents before continuing
- **If conceptual issues discovered**: Reconvene for decision-making before proceeding
- **If cross-document conflicts**: Create conflict log, resolve before QA phase

---

## Rollout Plan (Post-Implementation)

### Communication Strategy

1. **Internal Stakeholders** (if applicable):
   - Summary of changes
   - Rationale for revision
   - Impact on existing work (assessments, implementations)

2. **Framework Users** (if published):
   - Change announcement
   - Migration guide from old to new terminology
   - Updated documentation and training materials

3. **Certification/Assessment Programs** (if exist):
   - Updated assessment tools
   - Assessor training on new model
   - Retroactive scoring adjustments (if needed)

### Version Management

**Current Status**: Pre-publication, Version 1.0 (not yet released)

**Versioning Decision**: No version increment
- Rationale: This is a pre-publication refinement
- Framework considered "1.0 working draft" until formal publication
- Changes are conceptual clarification, not feature additions

**Documentation**:
- Record changes in CHANGELOG.md
- Note as "1.0 Conceptual Revision (Pre-Publication)"
- Date: 2026-01-29

---

## Success Criteria

### Definition of Done

- [ ] All Phase 1-10 documents updated
- [ ] All QA validation checklists completed
- [ ] Zero cross-document terminology conflicts
- [ ] All examples validate against new scoring model
- [ ] Risk characterization questions tested with 5+ scenarios
- [ ] Glossary includes all new terms with clear definitions
- [ ] CHANGELOG.md documents all changes
- [ ] README.md reflects updated framework structure

### Acceptance Criteria

**Framework Integrity**:
- Conceptual model is logically consistent
- No contradictions between documents
- Terminology is consistent across all 40+ documents

**Operational Viability**:
- Risk characterization produces clear baseline assignments
- Scoring model calculates correctly for test cases
- Hierarchical profile attribution logic works for examples
- Assessment guide provides clear, actionable methodology

**Documentation Quality**:
- All definitions are clear and unambiguous
- Examples illuminate concepts rather than confuse
- Cross-references are accurate and helpful
- Diagrams reflect current model

---

## Change Log

| Date | Phase | Status | Notes |
|------|-------|--------|-------|
| 2026-01-29 | Planning | Created | Initial change plan document created |
| | | | Awaiting decision on critical questions |
| | | | Awaiting approval to begin Phase 1 |

---

## Appendix A: Critical Terms Glossary

### New Terms (Post-Change)

**Baseline (B1/B2/B3)**: Risk-based control scoping mechanism that determines which controls apply based on AI system characteristics (autonomy, impact, reversibility, scale, data sensitivity).

**Maturity Level (ML1-5)**: CMMI-based assessment scale measuring implementation quality for each control:
- ML1: Initial (ad-hoc, individual-dependent)
- ML2: Developing (documented but inconsistent)
- ML3: Defined (standardized, organization-wide)
- ML4: Managed (quantitatively measured and controlled)
- ML5: Optimizing (continuous improvement, innovation)

**Profile Attribution**: Specification of how hierarchical profiles aggregate control assessments (single child, distributed equal, distributed weighted).

**Profile Target Maturity**: Per-control maturity level that a profile specifies as the expected implementation level (default: ML3).

**Framework-Relative Score**: Organization's score as a percentage of the complete framework maximum (all 73 controls at ML5).

**Baseline-Relative Score**: Organization's score as a percentage of their applicable baseline maximum.

**Profile Score**: Organization's actual maturity score as a percentage of their profile's target score.

### Deprecated Terms (To Be Removed)

**Tier (T1/T2/T3) in organizational context**: Previously used to describe organizational maturity stages. Replaced by maturity levels (ML1-5) for implementation quality and baselines (B1/B2/B3) for risk-based scoping.

**Tier Requirements**: Previously used to describe implementation expectations at each tier. Replaced by "Implementation Examples" showing what different maturity levels look like.

**Tier Progression**: Previously described organizational journey through T1→T2→T3. Replaced by "Maturity Level Progression" (ML1→ML2→ML3→ML4→ML5).

---

## Appendix B: File Change Checklist

### Phase 1: Definition Documents
- [ ] core/AIMF-FRAMEWORK-OVERVIEW.md
- [ ] implementation/AIMF-IMPLEMENTATION-TIERS.md (rewrite)
- [ ] implementation/AIMF-RISK-BASELINES.md (new file)
- [ ] implementation/AIMF-MATURITY-LEVELS.md (new file - optional)

### Phase 2: Data Structures
- [ ] core/AIMF-CONTROL-CATALOG.csv
- [ ] core/AIMF-CONTROL-CATALOG.md (if exists)

### Phase 3: Assessment & Scoring
- [ ] implementation/AIMF-ASSESSMENT-GUIDE.md
- [ ] implementation/AIMF-PROFILES-GUIDE.md

### Phase 4: Profile Documents
- [ ] profiles/framework-profiles/profile-foundational.md
- [ ] profiles/framework-profiles/profile-balanced.md
- [ ] profiles/framework-profiles/profile-high-assurance.md
- [ ] profiles/framework-profiles/profile-financial-services.md
- [ ] profiles/framework-profiles/profile-healthcare.md
- [ ] profiles/framework-profiles/profile-government.md
- [ ] profiles/implementation-profiles/profile-implementation-template.md
- [ ] profiles/implementation-profiles/examples/example-mid-market-tech.md
- [ ] profiles/implementation-profiles/examples/example-healthcare-provider.md

### Phase 5: Maturity Guides
- [ ] Rename directory: implementation/tier-transition-guides/ → implementation/maturity-level-guides/
- [ ] TIER-1-TO-2-GUIDE.md → MATURITY-LEVEL-1-TO-2-GUIDE.md
- [ ] TIER-2-TO-3-GUIDE.md → MATURITY-LEVEL-2-TO-3-GUIDE.md
- [ ] TIER-3-TO-4-GUIDE.md → MATURITY-LEVEL-3-TO-4-GUIDE.md
- [ ] TIER-4-TO-5-GUIDE.md → MATURITY-LEVEL-4-TO-5-GUIDE.md
- [ ] TIER-5-OPTIMIZATION-GUIDE.md → MATURITY-LEVEL-5-OPTIMIZATION-GUIDE.md

### Phase 6: Function Documents
- [ ] functions/AIMF-FUNCTION-GOVERN.md
- [ ] functions/AIMF-FUNCTION-MAP.md
- [ ] functions/AIMF-FUNCTION-MEASURE.md
- [ ] functions/AIMF-FUNCTION-MANAGE.md

### Phase 7: Mapping Documents
- [ ] mappings/AIMF-DIMENSION-MAPPING.md
- [ ] mappings/AIMF-ISO42001-MAPPING.md
- [ ] mappings/AIMF-NIST-RMF-MAPPING.md
- [ ] mappings/AIMF-ISO27001-MAPPING.md
- [ ] mappings/AIMF-EXECUTIVE-ORDER-14110-MAPPING.md
- [ ] mappings/AIMF-EXECUTIVE-ORDER-14179-MAPPING.md
- [ ] mappings/GOVERN-FUNCTION-MATURITY-MAPPING.md
- [ ] mappings/MAP-FUNCTION-MATURITY-MAPPING.md
- [ ] mappings/MEASURE-FUNCTION-MATURITY-MAPPING.md
- [ ] mappings/MANAGE-FUNCTION-MATURITY-MAPPING.md

### Phase 8: Supplemental Documents
- [ ] supplemental/AIMF-GLOSSARY.md
- [ ] supplemental/AIMF-FAQ.md
- [ ] supplemental/AIMF-REFERENCES.md
- [ ] supplemental/AIMF-FUTURE-PROFILES.md

### Phase 9: Diagrams & Assets
- [ ] assets/diagrams/framework-architecture-diagram.md
- [ ] assets/diagrams/maturity-progression-diagram.md
- [ ] assets/diagrams/tier-comparison-infographic.md → baseline-comparison-infographic.md
- [ ] assets/diagrams/profile-selection-flowchart.md
- [ ] assets/diagrams/standards-integration-diagram.md

### Phase 10: Root Documents
- [ ] README.md
- [ ] CHANGELOG.md
- [ ] QUALITY-ASSURANCE-CHECKLIST.md
- [ ] QA-VERIFICATION-REPORT.md
- [ ] AIMF-V1.0-REVIEW-PLAN.md

**Total Files**: 53 files to update/rename/create

---

## Appendix C: Decision Log

| Decision ID | Question | Options | Decision | Date | Rationale |
|-------------|----------|---------|----------|------|-----------|
| D001 | Maturity scoring floor | ML1=0 vs ML1=1 | PENDING | - | Need to incentivize vs. acknowledge existence |
| D002 | Control weighting | Equal vs Weighted | Equal (v1.0) | 2026-01-29 | Simpler for initial version |
| D003 | B1 control count | 25-40 controls | 30-35 | PENDING | Need risk question validation |
| D004 | B2 control count | 40-55 controls | 45-50 | PENDING | Need risk question validation |
| D005 | Default target maturity | ML2, ML3, ML4 | ML3 | 2026-01-29 | Industry standard "implemented" |
| D006 | Profile attribution default | Implicit vs Explicit | Explicit required | 2026-01-29 | Prevents ambiguity |

---

**End of Change Plan**

**Next Actions**:
1. Review and approve change plan
2. Make critical decisions (D001, D003, D004)
3. Approve Phase 1 commencement
4. Begin AIMF-FRAMEWORK-OVERVIEW.md revision
