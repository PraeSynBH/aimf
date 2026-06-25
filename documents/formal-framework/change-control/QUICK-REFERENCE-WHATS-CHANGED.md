# AIMF Framework Revision - Quick Reference

**Date**: 2026-01-29
**Change ID**: CP-2026-001
**Status**: ✅ COMPLETE

---

## What Changed (Quick Summary)

### Old Model → New Model

| Aspect | OLD | NEW |
|--------|-----|-----|
| **Control Scoping** | Tiers (T1/T2/T3) = Organizational stages | **Baselines (B1/B2/B3)** = Risk-based scoping |
| **Quality Measurement** | Implicit maturity | **Maturity Levels (ML1-5)** = Explicit 0-4 scale |
| **Assessment Scale** | 0-3 points | **0-4 points** (ML1=0, ML5=4) |
| **Total Controls** | 59 or 73 (inconsistent) | **72 controls** |
| **Scoring** | Single score | **Four score types** (profile, profile-max, baseline-relative, framework-relative) |

---

## Baselines (Risk-Based Control Scoping)

| Baseline | Controls | % | When to Use |
|----------|----------|---|-------------|
| **B1** (Low Risk) | 23 | 32% | Internal tools, low-impact, easily reversible |
| **B2** (Moderate Risk) | 61 | 85% | Customer-facing, business-critical, regulated |
| **B3** (High Risk) | 72 | 100% | Autonomous, life-safety, civil rights impact |

**Selection**: Use 6-question risk assessment (see Baseline Selection Questionnaire)

---

## Maturity Levels (Implementation Quality)

| Level | Name | Score | Definition |
|-------|------|-------|------------|
| **ML1** | Initial | 0 | Ad-hoc, undocumented |
| **ML2** | Developing | 1 | Documented but inconsistent |
| **ML3** | Defined | 2 | Standardized, organization-wide ← *Target* |
| **ML4** | Managed | 3 | Quantitatively measured |
| **ML5** | Optimizing | 4 | Continuous improvement |

**Assessment**: Evaluate each control ML1-5 based on evidence

---

## Scoring Model

```
Profile Target = Σ (Target Maturity per control)
Profile Actual = Σ (Assessed Maturity per control)
Profile Score = (Actual / Target) × 100%

Example:
48 controls × ML3 target (2 points each) = 96 target points
Actual assessment sums to 104 points
Profile Score = 104/96 = 108% ✅ Exceeding target
```

---

## Key Documents

| Document | Purpose |
|----------|---------|
| **AIMF-RISK-BASELINES.md** | How to select B1/B2/B3 (NEW) |
| **AIMF-MATURITY-LEVELS.md** | ML1-5 definitions and evidence (NEW) |
| **AIMF-ASSESSMENT-GUIDE.md** | How to assess and score (UPDATED) |
| **AIMF-PROFILES-GUIDE.md** | How to select/create profiles (UPDATED) |
| **AIMF-CONTROL-CATALOG.csv** | All controls with baselines (UPDATED) |

---

## Terminology Changes

| OLD | NEW |
|-----|-----|
| Tier 1 (T1) Initial | Baseline 1 (B1) Low Risk |
| Tier 2 (T2) Mature | Baseline 2 (B2) Moderate Risk |
| Tier 3 (T3) High-Risk | Baseline 3 (B3) High Risk |
| T1/T2/T3 Requirements | Implementation Basic/Defined/Advanced |
| Tier progression | Maturity level progression |
| tier-transition-guides/ | maturity-level-guides/ |
| IMPLEMENTATION-TIERS.md | RISK-BASELINES.md |

---

## Where to Find Things

**Risk Assessment**:
→ change-control/20260129143000-BASELINE-SELECTION-QUESTIONNAIRE.md

**Baseline Selection**:
→ implementation/AIMF-RISK-BASELINES.md

**Maturity Definitions**:
→ implementation/AIMF-MATURITY-LEVELS.md

**How to Assess**:
→ implementation/AIMF-ASSESSMENT-GUIDE.md

**How to Score**:
→ implementation/AIMF-ASSESSMENT-GUIDE.md (Phase 3: Score Calculation)

**Hierarchical Profiles**:
→ implementation/AIMF-PROFILES-GUIDE.md (Profile Attribution section)

**Maturity Progression**:
→ implementation/maturity-level-guides/ (5 guides)

**All Changes**:
→ CHANGELOG.md (comprehensive entry)

---

## Quick Start (Using Revised Framework)

### Step 1: Assess Risk
Use Baseline Selection Questionnaire → Determine B1, B2, or B3

### Step 2: Select Profile
Choose framework profile or create custom (see Profiles Guide)

### Step 3: Assess Maturity
Rate each control ML1-5 (0-4 points) using evidence criteria

### Step 4: Calculate Scores
- Profile Score = Actual/Target
- Identify gaps (ML1-2 controls)
- Prioritize improvements

### Step 5: Implement
Use Maturity Level Guides for progression roadmaps
- ML1→ML2: Document and assign (1-3 months)
- ML2→ML3: Standardize and enforce (6-12 months)
- ML3→ML4: Measure and manage (12-18 months)

---

**For Full Details**: See 20260129143000-COMPLETION-REPORT.md
