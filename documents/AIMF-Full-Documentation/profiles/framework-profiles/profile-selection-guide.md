# AIMF Profile Selection Guide

Use this guide whenever you need to pick the framework profile that will become the starting point for an implementation profile. It distills the step-by-step logic shown in `implementation/AIMF-PROFILES-GUIDE.md` so governance, legal, and technical stakeholders can align quickly.

## Step-by-step decision flow

1. **Industry/Sector** – If you operate in healthcare, financial services, or the public sector, start with the matching industry profile (healthcare, financial services, government). These profiles already encode the key regulatory controls, so treat them as the default unless the risk characterization pulls you to a different tier.
2. **Risk-based baseline** – Run the [Risk Characterization Questionnaire](../change-control/20260129143000-BASELINE-SELECTION-QUESTIONNAIRE.md) to score autonomy, reversibility, impact scale, consequences, data sensitivity, and regulatory pressure (1‑5 each). Assign:
   - **B3** when the total ≥ 21 or any dimension is 5 or both consequences/regulatory ≥ 4
   - **B2** when the total ≥ 13, any dimension ≥ 4, or two+ dimensions ≥ 3
   - **B1** when the total ≤ 12 and all dimensions ≤ 3
   Use the baseline result to pick a profile: Foundational for B1, Balanced or an industry profile for B2, and High-Assurance (or B3-enhanced industry variant) for B3.
3. **Regulatory overlay** – Cross-check applicable laws (HIPAA, GLBA, FCRA, Executive Orders, state AI statutes) against the chosen profile’s control set. Add any missing controls or increase target maturity for specific compliance drivers.
4. **Organizational readiness** – Assess existing AI governance maturity. Organizations without formal programs should phase from Foundational→Balanced. Ones with mature governance may start at Balanced or High-Assurance if they have the supporting processes.
5. **Resource availability** – Match the profile to budget, personnel, and timeline: Foundational (low effort, 3‑6 months, part-time team), Balanced (moderate, 6‑12 months, dedicated team), High-Assurance (high effort, 12‑24 months, full team + external support). Industry profiles usually mirror Balanced/High-Assurance effort.
6. **Customization decision** – Decide whether to add or remove controls on top of the selected profile:
   - **Add** when unique risks, regulations, or stakeholder expectations demand extra rigor.
   - **Remove** when scope exclusions are justified and documented with risk acceptance.
   - **Adjust target maturity** (ML2 → ML3 → ML4) as needed for critical controls or phased rollouts.
   Record every customization with rationale, especially when deviating from control applicability or maturity assumptions.
7. **Validation & approval** – Before creating an implementation profile, check that:
   - All regulatory drivers are covered
   - Risk-based selections are justified
   - Resources and timelines are realistic
   - Legal/compliance, risk, and governance stakeholders have signed off
   - Executive sponsor has given final approval

## After selection

- Document the context, rationale, and customizations in an implementation profile using `../profiles/implementation-profiles/profile-implementation-template.md`.
- Link the profile to the risk baseline and maturity objectives so assessors can track success metrics.
- Revisit the selection when new systems are deployed, regulations change, incidents occur, or maturity advances.

## Quick references

- Framework profiles: foundational, balanced, high-assurance, healthcare, financial services, government (see the companion documents in this directory).
- Baseline questionnaire: `../change-control/20260129143000-BASELINE-SELECTION-QUESTIONNAIRE.md`
- Implementation template: `../profiles/implementation-profiles/profile-implementation-template.md`
- Full profiles guide: `implementation/AIMF-PROFILES-GUIDE.md`
