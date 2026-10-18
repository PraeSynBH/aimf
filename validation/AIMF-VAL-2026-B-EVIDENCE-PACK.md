# AIMF Instrument Validation — Case Study B (B3 baseline, held out)

**Fixture id**: AIMF-VAL-2026-B
**Purpose**: a second, held-out evidence pack used to measure whether the AIMF anchors
(AIMF-ASSESSMENT-QUESTION-BANK, Anchor 0..4) make two assessors produce the same score on evidence
the anchors were **not** written against. Case A (`AIMF-VAL-2026-A`) is the fitting case: its
disagreements were remediated by editing the anchors, so agreement on A measures fit, not
reproducibility. This case was authored, frozen and hashed before any score existed, and no anchor
may be edited in response to it.
**Status**: validation fixture, not a customer engagement. The organisation is fictional; the
evidence is written to be dated and self-consistent so that a score can be decided from the pack
alone. Where the pack does not let an assessor decide, the control is deliberately left undecidable
or the artefact withheld, and `NA` is the correct verdict.
**Baseline**: B3 (high risk — aerospace and medical-device customers, safety-relevant visual
inspection). **Profile**: full framework (72 controls). **Assessment window**: 2026-Q3.
**System in scope**: Visual Inspection Classifier v2 (VIC-2) plus organisation-wide AI management
over the six registered AI systems.

**How an assessor uses this pack**: score each control from the artefacts listed under it, using
only the anchors for that control. If the pack does not let you decide, record `NA` (not assessable)
and say what is missing — do not default to 0.

**Organisation**: Northwind Precision Components (NPC), contract manufacturer of precision-machined
fittings and housings for medical-device and aerospace customers. 860 staff. Three plants:
Columbus, Ohio (HQ, plant 1, lines 1-2); Monterrey, Mexico (plant 2, line 3); Brno, Czech Republic
(plant 3, finishing). Quality system certified to ISO 9001:2015 and AS9100D; medical-device work
under ISO 13485. Artefact ids are `EV-nnn`; dates are ISO.

**Registered AI systems (6)**: `VIC-2` Visual Inspection Classifier (Monterrey line 3);
`SDE` Supplier Document Extractor (Columbus); `DFE` Demand & Flow Estimator (Columbus);
`PDM` Press Die Maintenance Predictor (Brno); `LDA` Line Data Anomaly Detector (Columbus lines 1-2);
`QAP` Quoting Assistant (pilot, sales engineering, Columbus).

---

## GOVERN — 19 controls

### GOV-1.1 — AI legal and regulatory policy
- **EV-014** "NPC Artificial Intelligence Policy v2.0" — approved by the AI Steering Committee 2026-02-11, effective 2026-03-01, applies to all three plants and all six registered AI systems.
- **EV-015** "Regulatory Mapping Annex" (annex to EV-014) — maps the EU AI Act (limited-risk obligations) and the EU Machinery Regulation to policy clauses. It does not map US state AI law, customer contractual AI clauses (two aerospace customers impose their own), or ISO/IEC 42001. No review date is recorded for the annex.
- **EV-016** Policy exception register — three open exceptions: VIC-2 (Monterrey), SDE (Columbus), QAP pilot. Two carry no approver and no expiry date.
- **EV-017** Legal memo 2026-01-28 from outside counsel covering the EU AI Act classification only; it states that US and customer-contract obligations were "out of scope of this instruction".

### GOV-1.2 — AI system inventory and risk classification
- **EV-020** "AI System Register" (governance platform) — 6 systems listed with owner, purpose, use case, vendor, plant and risk class (low/medium/high); last export 2026-09-30.
- **EV-021** Register field audit 2026-08-12 — 6 of 6 rows carry purpose, use case and risk class; 6 of 6 name a system owner.
- **EV-022** Deployment gate in the change-management system requires "AI classification approval" before a production release; 4 of 6 systems have a linked approval ticket. SDE and QAP have none.
- **EV-023** Email 2026-07-09 from Monterrey plant engineering noting VIC-2 was "running on line 3 since May pending the classification paperwork".

### GOV-1.3 — AI risk in the enterprise risk framework
- **EV-030** "Enterprise Risk Management Framework v5" (approved by the Board Audit & Risk Committee 2026-01-22) — carries an "AI and Algorithmic Risk" category with definitions, a 5x5 scoring scale and an escalation route.
- **EV-031** "AI Risk Appetite Statement" (approved 2026-01-22) — sets thresholds for three categories: model performance degradation, inspection escape (defective part reaching a customer), and vendor concentration. The statement names three categories.
- **EV-032** AI risk register export 2026-09-30 — five AI risk categories recorded: model performance degradation, inspection escape, vendor concentration, operator over-reliance, and training-data drift. All five entries carry a named owner and a dated escalation record; training-data drift was escalated to the Steering Committee 2026-05-19.
- **EV-033** Board Audit & Risk Committee minutes 2026-06-18 — AI risk is a standing agenda item; the minutes record one escalation (inspection escape threshold breach at Monterrey, 2026-05) and a request for "appetite coverage across all five categories".

### GOV-1.4 — Compliance monitoring of AI policy
- **EV-040** "AI Policy Compliance Monitoring Plan 2026" — quarterly checks against all 14 clauses of EV-014; owner: Compliance Manager (Columbus); method: evidence sampling per clause.
- **EV-041** Q1 2026 and Q2 2026 monitoring reports — both cover 14 of 14 clauses, with the clause list reproduced from EV-014 and one evidence sample per clause.
- **EV-042** Findings tracker — 9 findings raised in 2026 (4 in Q1, 5 in Q2); 6 closed with dated closure evidence and named owners; 3 open with named owners and target dates (2026-10-31, 2026-11-30, 2026-12-15).
- **EV-043** Compliance KPI set — one effectiveness KPI per policy clause (e.g. "share of registered systems with a current classification approval"), each with a target; reported in the quarterly compliance pack.
- **EV-044** Q2 2026 KPI report — 11 of 14 clauses at or above target, 3 below target with named corrective actions and owners.
- **EV-045** Deployment gate automation added 2026-06: the change-management system blocks a production release when the register shows no classification approval or an expired exception. Blocked 4 releases in Q2; the block list is retained.
- **EV-046** Internal Audit review of AI policy compliance (2026-07, report IA-2026-07) — independent of the Compliance function; raised 5 findings, all accepted, 3 closed by 2026-09-30. This is the first AI-specific internal audit; the audit plan schedules the next one for 2027.

### GOV-1.5 — Environmental impact of AI
- **EV-050** AI Policy v2.0 §7 requires that environmental impact "be considered where material to the system's use"; no method, threshold or owner is stated.
- **EV-051** No environmental assessment exists for VIC-2 or any of the six registered systems; the governance platform holds no environmental record for any system.
- **EV-052** Plant energy metering (Columbus and Monterrey) records line-level kWh monthly for the sustainability report; AI inference is not separated from line consumption in any month.
- **EV-053** Sustainability report 2025 discusses supplier emissions and water use; it contains no AI or compute reference.

### GOV-1.6 — Decommissioning process
- **EV-060** "AI System Retirement Procedure v3" (approved 2026-04-08) — covers data retention and deletion, model and artefact disposal, customer notification where a customer's part is affected, worker consultation, and a 45-day notice period.
- **EV-061** Retirement records exist for both systems retired since the procedure: "Vision Inspection v1" (retired 2026-05-30, deletion certificate attached, 2 customer notifications logged, 45-day notice evidenced) and "Supplier Scoring Model" (retired 2026-08-14, deletion certificate attached, 1 notification logged).
- **EV-062** Retirement register maintained by the AI Governance Lead; both records carry the named retiring owner and the plant manager's sign-off.
- **EV-063** Procedure reviewed annually; the 2026 review (2026-04-08) is the version in force, and the next review is scheduled 2027-04-08.

### GOV-1.7 — Third-party AI arrangements
- **EV-070** "Vendor AI Addendum" (legal-approved template, v4, 2026-03-02) — audit rights, model-change notification, data-use restrictions, sub-processor disclosure and exit assistance.
- **EV-071** Vendor register — 6 AI vendors; 4 carry a signed addendum (VIC-2 model vendor, SDE, PDM, LDA); DFE runs on an in-house model and has no vendor; QAP runs on a vendor API under a legacy MSA with no AI addendum.
- **EV-072** Vendor AI risk assessments — 4 of 6 vendors assessed (the same 4 with addenda), each refreshed at 12 months; the two most recent refreshes are 2026-06 and 2026-08.
- **EV-073** Vendor risk findings log — 3 findings in 2026 (sub-processor not disclosed, model-change notice arriving after release, data-retention term longer than contract), all closed with dated evidence.

### GOV-2.1 — AI risk roles and escalation
- **EV-080** AI RACI v3 (2026-03-15) — 12 AI risk activities, each with a named accountable role and a named responsible role; no blank cells.
- **EV-082** Role descriptions for the AI Governance Lead, Model Owner (per system), Plant Quality Manager and Data Steward include AI risk duties; HR records dated 2026-03.
- **EV-083** Escalation path published on the intranet and in the quality manual; a 2026-08 survey of 120 staff across the three plants found 84% could name the path and the first escalation step.
- **EV-084** The RACI names a Model Owner for all six systems in EV-020, including the QAP pilot.

### GOV-2.2 — Role-based AI risk training
- **EV-090** "AI Risk Curriculum v2" (2026-01) — three role-based modules: all-staff awareness (30 min), model-owner module (4 h), and assessor/inspector module for staff who act on model output (2 h).
- **EV-091** LMS completion at 2026-09-30 — all-staff module 91% (783 of 860); model-owner module 6 of 6; assessor module 34 of 38 inspectors at Monterrey.
- **EV-092** Competency is assessed, not only attendance: the model-owner and assessor modules end in a scenario-based assessment marked against a rubric (pass 80%), and the rubric and marked scripts are retained per person.
- **EV-093** Re-certification interval is 18 months, recorded in the LMS; the first cohort (enrolled 2026-01) reaches it in 2027-07, so no refresher cycle has yet completed.
- **EV-094** The 4 inspectors not yet assessed are recorded with a target date (2026-10-15) and their line supervisor as owner.

### GOV-2.3 — Executive oversight
- **EV-100** AI Steering Committee charter (approved 2026-01-15) — quarterly cadence, quorum of 4 of 7, decisions minuted, standing agenda including performance, incidents and register changes.
- **EV-101** Minutes for 2025-11, 2026-02, 2026-05, 2026-08 — four consecutive quarterly meetings held; attendance 5-7 of 7; quorum recorded at each.
- **EV-102** Decision log — 14 decisions in the period, 14 with a named action owner and 11 with a recorded completion date.
- **EV-103** The committee's remit covers the AI strategy: the 2026 strategy refresh (EV-220) was approved by the committee on 2026-02-12 and noted by the Board Audit & Risk Committee 2026-03-05.

### GOV-3.1 — Interdisciplinary expertise in AI teams
- **EV-110** "AI Project Team Composition Standard" (2026-01) — requires quality engineering, data science, maintenance/operations, EHS and (where a customer's part is affected) customer quality representation on every AI project.
- **EV-112** VIC-2 team record — quality engineering (2), data science (2), Monterrey maintenance (1), EHS (1), customer quality (1); all six attend the fortnightly design review, attendance log for 2026 shows 11 of 13 sessions at full attendance.
- **EV-113** Composition review completed for 3 of 6 systems in 2026 (VIC-2, PDM, LDA); no review recorded for SDE, DFE or QAP.
- **EV-114** No inclusion or participation metrics are collected per project; attendance logs are the only record.

### GOV-3.2 — Demographic representation monitoring
- **EV-120** HR workforce dashboard reports headcount, hiring and promotion by gender and age band for the whole company, quarterly; it does not break out AI, data or engineering roles.
- **EV-121** 2025 annual diversity report includes one paragraph on "technical and engineering roles" with no AI-specific or data-science breakdown, and no promotion analysis at role level.
- **EV-122** No action plan exists for representation in AI teams; no target is set; no review of AI hiring shortlists is recorded.

### GOV-4.1 — AI risk culture
- **EV-130** "Quality First, AI Included" awareness campaign 2026-Q2 — 6 shift-briefing sessions across the three plants, intranet series, and an andon-card redesign so that "model output suspected wrong" is a named stop reason.
- **EV-131** Engagement survey 2026 (response rate 71%) — two AI items: "I would raise a concern about an AI system" 74% favourable; "I know what the AI system on my line is allowed to do" 68% favourable.
- **EV-132** AI risk behaviours are named in the objectives of the 6 model owners and the 3 plant quality managers; they are not in the objectives of operators or supervisors.
- **EV-133** Both survey items were added in 2025 and now have two data points (2025, 2026): the "raise a concern" item moved 69% → 74%, the "allowed to do" item 66% → 68%. No culture metric beyond the survey is tracked.

### GOV-4.2 — Stakeholder feedback on AI systems
- **EV-140** Two intake channels: the operator andon/feedback form on the line terminals (Monterrey, Columbus) and the customer quality portal. 2026 to 2026-09-30: 187 operator items and 23 customer items tagged AI.
- **EV-141** Monthly AI feedback review, chaired by the AI Governance Lead; minutes retained for 9 of 9 months in 2026.
- **EV-142** Feedback-to-change log — 11 changes in 2026 attributed to feedback, each carrying the feedback item id, the change record id and the date the change was released; the log is maintained in the governance platform and links both directions.
- **EV-143** Response is sent to the person who raised the item for all 23 customer items and for 141 of the 187 operator items; the remainder were closed in the monthly review without a reply, which the minutes record as a backlog item.

### GOV-4.3 — Transparency communication
- **EV-150** Customer-facing "AI in our inspection process" statement published 2026-05 on the customer portal, covering VIC-2 only (purpose, what a human checks, how to raise a concern); it is not updated since 2026-05 and covers none of the other five systems.
- **EV-151** Internal quarterly AI bulletin (4 issues in 2026).
- **EV-152** No transparency report is published; no annual disclosure; no process for correcting a published statement and no owner for the statement after publication.
- **EV-153** The 2026-05 statement was drafted by Customer Quality and released without review by the AI Steering Committee; the committee minutes 2026-08 note "no visibility of external AI communications".

### GOV-5.1 — External governance participation
- **EV-160** Membership of one industry association AI working group (2026); attendance at 3 of 6 meetings; the representative is the AI Governance Lead.
- **EV-162** One response to the European Commission's consultation on AI in manufacturing (2026-04), filed through the association, not independently.
- **EV-163** No engagement plan and no register of external engagements; the association membership renews automatically and no follow-up on the consultation is recorded.

### GOV-5.2 — Research collaborations
- **EV-170** No academic partnership, research agreement, joint laboratory or funded research project exists; procurement and legal hold no such agreement for any plant.
- **EV-171** One data scientist at Columbus co-authored a conference paper with a university group in 2026 on a personal basis; there is no institutional agreement, no data-sharing record and no review of the data used.
- **EV-172** No knowledge-exchange programme, internship scheme or publication review process exists for AI work.

### GOV-6.1 — Governance resourcing
- **EV-180** FY2026 budget line "AI Governance and Quality Analytics" — $310k approved, covering 1.5 FTE (AI Governance Lead full-time, compliance analyst 0.5), the governance platform licence and external legal review.
- **EV-181** Actual spend to 2026-09-30: $228k; 1.5 of 1.5 FTE filled since 2026-02.
- **EV-182** Tooling in use: the governance platform (register, RACI, policy library, findings tracker) and the evaluation repository (EV-430); both are live and hold the records cited in this pack.

### GOV-6.2 — Capability-building plan
- **EV-190** "AI Governance Capability Plan 2026-2028" — funded in the FY2026 and FY2027 budgets; 6 milestones (policy refresh, training rollout, metric framework, evaluation repository, vendor programme, external assurance); owner: AI Governance Lead.
- **EV-191** Progress reviews 2026-03 and 2026-08 — 2 milestones complete (training rollout, evaluation repository), 3 on track, 1 slipped (external assurance, re-planned to 2027-Q1); both reviews minuted by the AI Steering Committee.
- **EV-192** A skills inventory is maintained in the HR system and refreshed at each annual review; the 2026 refresh (2026-04) covers the 6 model owners and 9 data/quality staff.

## MAP — 18 controls

### MAP-1.1 — Purpose, beneficial use and deployment setting
- **EV-200** VIC-2 System Definition v2.2 (2026-06-20) — purpose (defect classification of machined fittings on line 3), intended population (all line-3 part families), deployment setting (post-machining inspection station, night and day shifts), out-of-scope uses (no dimensional measurement, no scrap decision without inspector confirmation).
- **EV-201** Legal review record 2026-06-11 — covers product liability, EU Machinery Regulation obligations and the two customer AI clauses; signed by outside counsel and by the NPC General Counsel.
- **EV-202** System Definition exists for VIC-2, PDM and SDE; DFE and LDA carry a one-page description in the register only; QAP has a pilot brief with no deployment-setting section.

### MAP-1.2 — Interdisciplinary competency requirements
- **EV-210** "AI Competency Framework" (2026-02) — required competencies per role family (quality engineering, data science, maintenance, EHS, customer quality), each with a proficiency level.
- **EV-211** Project staffing checklist requires each competency to be named against a person; signed for 4 of 6 systems (VIC-2, PDM, LDA, SDE).
- **EV-212** Competency gaps are recorded on the checklist for 2 projects (PDM lacks an EHS representative; SDE lacks customer quality); no inclusion or diversity metric is produced per project.

### MAP-1.3 — AI strategy and mission review
- **EV-220** "Northwind Digital Quality Strategy 2026-2028" — approved by the AI Steering Committee 2026-02-12 and noted by the Board 2026-03-05; four themes, each tied to the company mission statement ("components our customers can trust in the body and in the air").
- **EV-221** The strategy is reviewed against the mission annually; the 2026 review was held 2026-02-12 and the 2027 review is scheduled in the committee calendar.
- **EV-222** Five strategic KPIs with owners and targets; the 2026-Q2 dashboard shows 3 of 5 on track, 1 behind (inspection automation coverage), 1 not yet instrumented (supplier AI maturity).

### MAP-1.4 — Business case and value tracking
- **EV-230** VIC-2 business case (2025-10) — capital and operating cost, value metrics (scrap rate, inspection labour hours, escape rate), expected 25% reduction in inspection hours, and the method for post-deployment validation.
- **EV-231** Post-deployment value report (2026-08) — measured 22% reduction in inspection hours against the 25% target, scrap rate down 1.4 points, escape rate unchanged; variance explained.
- **EV-232** Business cases exist for 4 of 6 systems (VIC-2, SDE, DFE, PDM); value tracking after deployment exists for 3 (VIC-2, SDE, DFE).

### MAP-1.5 — Risk tolerances
- **EV-240** AI Risk Appetite Statement (2026-01-22) — four tolerances, two quantified: inspection escape rate ≤ 0.02% of shipped lots, and model performance degradation trigger at a 3-point drop in defect-detection recall; the other two are qualitative (vendor concentration, operator over-reliance).
- **EV-241** Approval by the Board Audit & Risk Committee recorded in minutes 2026-01-22; the statement is referenced in the ERM framework (EV-030).
- **EV-242** Performance against both quantified tolerances is reported quarterly to the AI Steering Committee; 2026-Q1, Q2 and Q3 reports each show the measured value against the tolerance, and Q3 records one breach of the escape tolerance at Monterrey (2026-05) with the escalation.

### MAP-1.6 — Socio-technical requirements and traceability
- **EV-250** VIC-2 Requirements Specification v3 (2026-04) — 96 requirements, of which 18 are socio-technical (operator workload, explanation shown at the inspection station, override ergonomics, shift handover of model state).
- **EV-251** Traceability matrix links 90 of 96 requirements to a test case or a validation record; of the 18 socio-technical requirements, 6 have a linked test and 12 have none.
- **EV-252** Operator and inspector workshops (4 sessions, 2026-02 to 2026-04, Monterrey) recorded with attendance lists; input is attributed to a requirement id for 14 of the 18 socio-technical requirements.

### MAP-2.1 — Task taxonomy and method documentation
- **EV-260** "AI Task Taxonomy v1" (2026-01) — 7 task categories (classification, extraction, forecasting, ranking, generation, anomaly detection, recommendation), each with a definition and an example; used as a register field.
- **EV-261** Register field "task category" is populated for 6 of 6 systems.
- **EV-262** Method documentation exists for 5 of 6 systems (VIC-2, SDE, DFE, PDM, LDA); VIC-2's method note (v2, 2026-06) documents the model family, training data, labelling process, threshold setting and known failure modes. QAP has no method documentation.

### MAP-2.2 — Knowledge limits and human oversight
- **EV-270** "Known Limits and Human Oversight" note exists for all six systems (VIC-2 v2 2026-06; SDE, DFE, PDM, LDA 2026-03/04; QAP 2026-07 pilot note) — each lists out-of-scope inputs, confidence thresholds and the human decision that must follow model output.
- **EV-271** The VIC-2 oversight rule is enforced in configuration: any part below the confidence threshold routes to the inspector's re-inspection queue, and no part can be released from the line without an inspector confirmation in the MES (configuration export 2026-09-14).
- **EV-272** For SDE, PDM and LDA the oversight rule is documented but not enforced in configuration: the notes state what a human must check, and no system control prevents the downstream action (verified in the 2026-09 process walkthrough).

### MAP-2.3 — Scientific methodology and TEVV
- **EV-280** VIC-2 "Evaluation Methodology v2" (2026-05) — test design, sampling frame per part family, metrics, acceptance approach, and a "known limitations" section covering lighting variation, new part families and label noise from inspector disagreement.
- **EV-281** TEVV plan with 5 planned activities (offline evaluation, shadow run, staged rollout, drift re-validation, annual re-validation), each with a date and a named owner; the drift re-validation is scheduled 2026-12-01 with the data science lead as owner.
- **EV-282** Methodology reviewed by the Head of Quality Engineering and by an external metrology laboratory (review letter 2026-06-02); the laboratory's two comments were incorporated in v2.

### MAP-3.1 — Expected benefits and validation method
- **EV-290** Benefits analysis for VIC-2 (2025-10) — quantified baseline (inspection hours per 1,000 parts, scrap rate, escape rate) with the source data and a stated validation method (staged rollout comparison against two manual-inspection lines, same part families).
- **EV-291** Validation was executed 2026-06 to 2026-08 and reported 2026-08: 22% inspection-hour reduction against the 25% target, with the method and sample recorded.
- **EV-292** Benefits analyses exist for 4 of 6 systems; SDE's analysis has no validation method and LDA has none.

### MAP-3.2 — Costs including non-monetary
- **EV-300** VIC-2 total-cost model (2025-10, updated 2026-08) — licence, camera hardware, integration, training, maintenance; non-monetary costs are named and quantified where measurable: inspector rework hours per week, false-reject handling time, and an operator trust survey score.
- **EV-301** Non-monetary costs are linked to the risk appetite statement: rework hours feed the operator over-reliance assessment, and the trust score is reported with the value report.
- **EV-302** Cost tracking is updated quarterly by Finance; 2026-Q2 actuals and the variance against the business case are recorded.

### MAP-3.3 — Application scope and change control
- **EV-310** VIC-2 scope statement (2026-04) — part families (14), lines (line 3 only), plants (Monterrey), shifts (both), excluded populations (first-article inspection, customer-witnessed inspection).
- **EV-311** Change log with 5 scope changes in 2026, each approved under the recorded change process (change request, quality engineering review, AI Steering Committee approval where the change adds a part family); approvals are dated and named.
- **EV-312** Scope-drift check run per release (2026-04, 2026-06, 2026-08): inputs and uses compared with the recorded scope; one drift found in 2026-06 (a part family running without being added to scope) and re-scoped before release.

### MAP-3.4 — Operator proficiency
- **EV-320** "Inspector AI Proficiency Standard" (2026-03) — four proficiency levels, assessed by supervised case review against a rubric, with a certification step for acting on model output.
- **EV-321** All 38 line-3 inspectors assessed in 2026 (results in the LMS); 34 certified, 4 in supervised practice with a target date.
- **EV-322** Certification requires re-assessment every 24 months; the certification register records the date and the assessor for each inspector.

### MAP-3.5 — Human oversight effectiveness
- **EV-330** Oversight procedure (2026-05) documents who reviews what, override rights, escalation to the shift supervisor and the andon stop, and the records each step produces.
- **EV-331** Override log 2026 (to 2026-09-30): 1,240 overrides; a 60-case audit in 2026-08 rated 51 of 60 overrides appropriate against the procedure's criteria.
- **EV-332** Oversight effectiveness is assessed on a semi-annual cadence: the 2026-08 assessment is the first; 9 findings, 7 closed by 2026-09-30 with dated evidence, 2 open with owners and dates. The next assessment is scheduled 2027-02.

### MAP-4.1 — Third-party AI mapping
- **EV-340** Third-party AI dependency map (2026-07) — covers the VIC-2 model vendor, the camera and optics supplier, the cloud inference service and the MES integration; data flows, hosting location and contractual AI terms recorded per dependency.
- **EV-341** Legal review recorded for 4 of 6 AI vendors (the four with signed addenda); QAP's vendor and one sub-processor are not reviewed.
- **EV-342** The map is maintained by the AI Governance Lead and reviewed by the AI Steering Committee at each quarterly meeting; the 2026-08 review minutes record one update (new sub-processor added).

### MAP-4.2 — Controls over third-party components
- **EV-350** Control descriptions for third-party AI (2026-07) — 9 controls: model-change notification, sub-processor disclosure, data residency, output monitoring, exit assistance, audit right, security attestation, retention limit, and performance SLA.
- **EV-351** Implementation evidence exists for 7 of 9 controls (sub-processor disclosure and performance SLA are described but not evidenced for any vendor).
- **EV-352** Effectiveness testing is recorded for 2 of the 9 controls: a model-change notification test (2026-06) and a data-residency verification (2026-08), both with results and findings.

### MAP-5.1 — Impact assessment
- **EV-360** VIC-2 impact assessment (2026-05) — affected groups (inspectors, line operators, maintenance, customers receiving inspected parts, end users of medical devices), potential harms (escape of a defective part, over-reliance, deskilling, privacy of operator images), and mitigations per harm.
- **EV-361** Reviewed by the AI Steering Committee 2026-05-19; three mitigations adopted (inspector confirmation enforced in the MES, quarterly deskilling check, camera framing restricted to the part), one deferred with a recorded rationale.
- **EV-362** Impact assessment exists for VIC-2 and PDM; the AI Policy was amended in 2026-06 to require one for every high-risk system, so SDE, LDA and QAP are now overdue and the compliance tracker records them as open findings.

### MAP-5.2 — Stakeholder engagement
- **EV-370** Engagement plan for VIC-2 (2026-02) — inspector workshops (4), workers' council consultation (2), customer quality forum (1), supplier quality day (1).
- **EV-371** Records exist for 7 of 8 planned sessions: attendance lists, notes, and a changes log; the supplier quality day was replaced by written consultation, which is recorded.
- **EV-372** Changes attributed to engagement: 4 (inspection-station explanation display, override button placement, night-shift handover note, camera framing restriction), each with the session reference.
- **EV-373** The workers' council reviewed the impact assessment and its comments are minuted; two of its three comments were adopted.

## MEASURE — 22 controls

### MEA-1.1 — Risk metrics per system
- **EV-400** "AI Measurement Framework v2" (2026-04) — two to four metrics per risk category, an owner per metric, a stated reporting cadence and a target per metric.
- **EV-401** VIC-2 dashboard shows defect-detection recall, false-reject rate, escape rate, override rate, drift score and inference latency; refresh hourly from the MES.
- **EV-402** Framework maps all 18 risk categories in the register to at least one metric; 16 are instrumented directly and 2 use documented proxy metrics (operator over-reliance uses override-rate trend; vendor concentration uses dependency-share).
- **EV-403** Coverage report (share of risk categories with an instrumented metric) issued quarterly and reviewed by the AI Steering Committee; 2026-Q2 shows 18 of 18 covered, with the two proxies flagged.

### MEA-1.2 — Metric validity review
- **EV-410** Metric definitions document includes a "what this metric can and cannot show" note for 7 of 11 metrics.
- **EV-411** Two validation studies: the escape-rate metric was validated against customer returns and field complaints (2026-05, found to under-count by 1.3x because customer-detected escapes were not linked); the override-rate metric was compared against the 60-case audit (2026-08).
- **EV-412** Revision history exists for all 11 metrics; 2 metrics were revised as a result of validation, with the change and the reason recorded.
- **EV-413** Annual metric re-validation is scheduled for each metric in the framework; the 2026 cycle covered 9 of 11 metrics by 2026-09-30, with 2 scheduled for 2026-10.

### MEA-1.3 — Independent assessors
- **EV-420** Internal Audit charter covers "models and automated decisions affecting product conformity"; VIC-2 is in the 2026 audit plan.
- **EV-421** Internal Audit review of VIC-2 (2026-07, report IA-2026-07-AI) — independence statement signed by the audit lead; 5 findings.
- **EV-422** An external metrology laboratory was engaged for the 2026-06 methodology review and the 2026-08 drift verification; its independence from the build team is recorded in the engagement letter, and its two reports are in the pack record.

### MEA-2.1 — Reproducible test records
- **EV-430** Evaluation repository (Git) — test scripts, dataset version hashes, container image digests, metric code and run logs for every evaluation since 2025-11.
- **EV-431** Run manifest for the 2026-08 evaluation: dataset v4.1 hash, container digest, random seed, model version, metric code commit.
- **EV-432** Third-party re-run audit 2026-09: an external reviewer re-ran 11 of 11 evaluations from the repository alone (no help from the team) and reproduced the published metrics to within 0.1 percentage point; the audit report records the environment and the commands used.

### MEA-2.2 — Human-subject evaluations
- **EV-440** No human-subject evaluation has been run in the period. The inspector workshops (EV-252) and the trust survey (EV-300) are process design and staff experience measurement, not research on human subjects.
- **EV-441** NPC has no research ethics policy and no ethics review board; the quality system's human-subject provisions do not exist because the company does not conduct human-subject research.
- **EV-442** No consent records, no sampling rationale and no ethics approval exist for any AI-related activity in the period.

### MEA-2.3 — Pre-defined performance criteria
- **EV-450** VIC-2 acceptance criteria (2026-04, approved by the Plant Quality Board before testing) — defect-detection recall ≥ 97%, false-reject rate ≤ 2.5%, escape rate ≤ 0.02%, inference latency ≤ 400 ms, inspector-confirmation compliance 100%.
- **EV-451** Test report (2026-08) demonstrates 97.8% / 2.1% / 0.019% / 310 ms / 100% on a deployment-like replay of 48,000 line-3 images from production, with the sampling frame recorded.
- **EV-452** Two criteria (explanation usefulness rating, deskilling check) were added after the 2026-08 test and are recorded as applying from the 2026-12 re-validation; the pre-test criteria were met in full.
- **EV-453** A results-versus-criteria table is produced per release (2026-04, 2026-06, 2026-08), with the acceptance decision recorded against each criterion and signed by the Plant Quality Board.

### MEA-2.4 — Production monitoring
- **EV-460** Production monitoring covers input image quality, inference latency, output distribution, defect-class mix and drift score for all six systems; alerts route to the on-call quality engineer and to the line supervisor's terminal.
- **EV-461** 9 alerts in 2026, 8 acknowledged within SLA, 1 outside SLA (2026-05); 2 incidents (2026-05 lighting change at Monterrey, 2026-08 MES interface change) with incident records.
- **EV-462** Detection precision (0.88) and recall (0.83), alert-to-action time (median 3.5 h) and false-alert rate are measured monthly per system and reported to the AI Steering Committee at its quarterly meeting, with the monthly series retained.
- **EV-463** Thresholds were re-set from measured incident data twice in 2026 (2026-06 after the lighting incident, 2026-08 after the interface incident); the re-set cut alert-to-action time from 6.2 h to 3.5 h, and both changes are recorded with the incident reference.

### MEA-2.5 — Validity, reliability, generalisability
- **EV-470** Validity study (2026-06) — face and content validity by a panel of quality engineers and one customer quality representative; test-retest on 12,000 images (κ = 0.86); criterion validity against inspector-confirmed labels.
- **EV-471** Generalisability assessed across the three plants and 14 part families: performance holds on 11 part families and 2 plants; Brno finishing (3 part families, 900 images) is below threshold and excluded from the claim, with the exclusion recorded.
- **EV-472** Inter-rater reliability between inspectors on the labelling task was assessed (κ = 0.74) and reported as a limitation of the ground truth.

### MEA-2.6 — Safety evaluation and residual risk
- **EV-480** Safety evaluation (2026-05) for VIC-2 and PDM — fail-safe test on model timeout, camera failure, MES outage and malformed input; results documented with the fallback behaviour observed in each case.
- **EV-481** Residual safety risks documented for VIC-2 and PDM (3 items for VIC-2: escape during a camera failure, silent degradation, operator mis-keyed confirmation), each with an accepting role and a dated acceptance (Plant Quality Manager, 2026-05-28).
- **EV-482** No safety evaluation and no residual risk acceptance exists for SDE, DFE, LDA or QAP; the 2026-09 process walkthrough records the gap.
- **EV-483** Fail-safe tests are repeated at each annual re-validation; the next is 2026-12-01 and is on the TEVV plan.

### MEA-2.7 — Adversarial evaluation
- **EV-490** A red-team exercise on VIC-2 was commissioned 2026-06 and delivered 2026-07 by an external security firm.
- **EV-491** The report is held under a customer confidentiality agreement with an aerospace customer and is marked "restricted — not for distribution"; the contents, findings and resilience measures are not available to this assessment, and no summary or extract was produced.
- **EV-492** The exercise's existence, scope and delivery date are recorded in the AI Steering Committee minutes 2026-08; nothing about its results is recorded there.

### MEA-2.8 — Transparency and accountability risk
- **EV-500** Transparency and accountability risk assessment (2026-05) for VIC-2 — covers customer notification of AI-assisted inspection, worker understanding of the system's role, and the accountability chain for an escape (inspector, shift supervisor, plant quality manager, model owner).
- **EV-501** Customer notification text is approved by Customer Quality and appears in the customer portal statement (EV-150); the accountability chain is published in the quality manual.
- **EV-502** The assessment covers VIC-2 only; the other five systems have no transparency risk assessment and the policy requires one only for high-risk systems.

### MEA-2.9 — Explainability to decision-makers
- **EV-510** Explainability design note (2026-06) — the inspection station shows a defect-region overlay and the top-3 contributing image features in plain language; the inspector handbook carries interpretation guidance and the rule that the overlay is advisory.
- **EV-511** Interpretability study 2026-08 with 12 inspectors on 20 cases: 18 of 20 explanations rated actionable; the two failures were small-feature scratches.
- **EV-512** Guidance was updated after the 2026-08 model refresh (handbook v3, 2026-08-22), and the update records which model version it applies to.

### MEA-2.10 — Privacy
- **EV-520** Privacy impact assessment for SDE (2026-04) — supplier contact personal data in invoices and packing slips, minimisation, retention, data-subject rights, cross-border transfer to Monterrey; and a PIA for VIC-2 (2026-05) covering operator images and the camera framing restriction.
- **EV-521** Privacy-preserving measures assessed for SDE: pseudonymisation of supplier contacts in the extraction output (in place); field-level redaction considered and rejected with a recorded rationale.
- **EV-522** PIAs exist for 2 of 6 systems (SDE, VIC-2); privacy review is a gate in the deployment process since 2026-06 (the gate blocks release when no PIA is recorded), so the four remaining systems are blocked from their next release until a PIA is filed.

### MEA-2.11 — Bias and fairness
- **EV-530** Fairness evaluation (2026-06) for VIC-2 — 3 metrics (recall parity across part families, false-reject ratio across plants, calibration by part family) across 14 part families, 3 plants and 2 shifts.
- **EV-531** Two disparities flagged: Brno finishing part families (recall 91% vs 97.8% overall) and the night shift at Monterrey (false-reject ratio 1.4); mitigations assessed, one adopted (night-shift threshold recalibration, 2026-07), one deferred pending more data.
- **EV-532** Retest after mitigation (2026-09): night-shift false-reject ratio reduced to 1.1; Brno disparity unchanged and still open with an owner and a date.
- **EV-533** Results are reported per group for each release (2026-04, 2026-06, 2026-08) against pre-set thresholds; one threshold breach (Brno recall) is recorded and open.
- **EV-534** No demographic bias analysis is performed, because the system makes no decisions about individuals and the pack contains no individual-level data; the assessment records this as a scoping decision, not an omission.

### MEA-2.12 — Environmental impact
- **EV-540** No energy, compute or carbon figure is collected for AI training or inference; the cloud inference contract reports cost, not energy.
- **EV-541** No efficiency target exists for AI compute; the sustainability report does not mention AI.
- **EV-542** No assessment exists for any of the six systems; plant energy metering (EV-052) does not separate AI inference.

### MEA-2.13 — TEVV programme effectiveness
- **EV-550** TEVV effectiveness review (2026-09) — coverage analysis (78% of requirements tested, up from 61% in 2025), escaped defects found post-release (2), test-cycle time, and 3 process changes adopted (socio-technical test template, shadow-run requirement, drift re-validation trigger).
- **EV-551** Metric effectiveness was assessed for 4 of 11 metrics in the same review, using the validation studies in EV-411.
- **EV-552** The review covers the whole AI testing programme across the six systems, not one system; it is minuted by the Plant Quality Board and the AI Steering Committee.

### MEA-3.1 — Standing risk tracking
- **EV-560** "AI Risk Tracking Log" — named owner (AI Governance Lead), monthly review with the model owners, 31 entries in 2026 including 9 emergent risks.
- **EV-561** Review minutes exist for 9 of 9 months in 2026; each minute records the entries reviewed, the owner and the decision.
- **EV-562** Emergent-risk entries all carry owners; 24 of 31 entries have a closure record with dated evidence, 7 remain open with target dates.

### MEA-3.2 — Alternative measurement where conventional metrics fail
- **EV-570** "Assessment Methods for Hard-to-Measure AI Risks" note (2026-05) — 4 alternative methods (structured expert elicitation, scenario walkthrough, incident-proxy analysis, operator diary study), each with stated limits and a selection rule keyed to the risk category.
- **EV-571** Three methods used in the period: expert elicitation for deskilling risk (2026-06), scenario walkthrough for escape accountability (2026-07), operator diary study for over-reliance (2026-08); each has a record, a result and the limits recorded at the time.
- **EV-572** The selection rule is applied in the measurement framework (EV-400), which names the alternative method for each of the 2 proxy metrics.

### MEA-3.3 — End user and community feedback
- **EV-580** Operator andon/feedback form on line terminals and the customer quality portal (EV-140); 187 operator and 23 customer AI-tagged items in 2026.
- **EV-581** Every item receives a disposition within 10 working days, recorded in the governance platform; 164 of 210 items have a reply to the raiser (EV-143).
- **EV-582** Feedback is analysed monthly (EV-141) and the analysis is published in the internal AI bulletin; 11 changes are traced to feedback items in the feedback-to-change log (EV-142).

### MEA-4.1 — Measurement in deployment context
- **EV-590** All VIC-2 evaluations run on production line-3 images (48,000 images from the live inspection station in the 2026-08 evaluation), not on public benchmarks; the shadow run (2026-06) ran in parallel with inspectors on live production for 6 weeks.
- **EV-591** Domain expert input into test design and criteria is recorded: 4 inspector workshops and 2 quality-engineering sessions informed the criteria in EV-450, with the input attributed per criterion.
- **EV-592** Vendor benchmark results are used only for initial model selection in 2025 and are not part of the acceptance evidence; the 2026-04 acceptance record states that no benchmark result was used.

### MEA-4.2 — Expert review of measurement results
- **EV-600** Measurement results reviewed by the Plant Quality Board (2026-08-14) and by the external metrology laboratory (2026-08-27).
- **EV-601** Independence is recorded: the laboratory has no commercial relationship with the model vendor or the build team (engagement letter); the Plant Quality Board includes the VIC-2 product owner, which the review record notes as a partial conflict, mitigated by the laboratory review.
- **EV-602** Review comments are minuted; 3 led to re-analysis (two on the sampling frame, one on the escape-rate under-count in EV-411), and the re-analysis is in the record.

### MEA-4.3 — Performance change detection and root cause
- **EV-610** Drift monitoring with alert thresholds for all six systems; 3 performance declines detected in 2026 (2026-02 PDM, 2026-05 VIC-2, 2026-08 VIC-2).
- **EV-611** Root-cause analysis recorded for all 3: 2026-02 die-temperature sensor drift, 2026-05 lighting change at Monterrey, 2026-08 MES interface change altering image metadata; each has a corrective action, a fix date and a retest record.
- **EV-612** Detection latency (median 2 days from drift onset to alert) and change-to-action time (median 5 days) are measured and reported monthly to the AI Steering Committee against stated targets (3 days, 10 days).
- **EV-613** The change-detection process is applied to all six systems; the log records 3 declines and 5 model or input changes in 2026, and each change has a linked assessment.

## MANAGE — 13 controls

### MAN-1.1 — Go/no-go decision with criteria and approval
- **EV-620** "AI Deployment Decision Procedure v2" (2026-02) — 7 go/no-go criteria (classification approved, PIA filed, acceptance criteria met, oversight enforced, monitoring live, residual risk accepted, training complete), approver named (Plant Quality Board), decision record template.
- **EV-621** Decision records exist for 4 of 6 systems (VIC-2 2026-04-22, PDM, DFE, LDA); VIC-2's record shows 7 of 7 criteria met. SDE and QAP have no decision record.
- **EV-622** SDE has been in production since 2025-12 without a decision record; QAP is a pilot running since 2026-07 with a pilot brief but no decision record (email trail 2026-07-09).
- **EV-623** Decision metrics (4 approvals, 2 approvals with conditions, 0 rejections) are reviewed quarterly against the criteria by the Plant Quality Board, and the review minutes are retained.

### MAN-1.2 — Risk prioritisation driving resourcing
- **EV-630** "AI Risk Prioritisation Method" (2026-03) — impact × likelihood × customer-contract exposure × regulatory exposure, producing a ranked list refreshed quarterly.
- **EV-631** Ranked register produced 2026-04 and 2026-07; the top 5 risks are named with scores.
- **EV-632** FY2026 allocation decision: 4 of the top 5 risks received a named budget line or a named person with allocated hours, recorded in the FY2026 budget and the 2026-04 committee minutes; the fifth (training-data drift) has a plan and no allocation.

### MAN-1.3 — Response plans for top risks
- **EV-640** Response plans for the 5 top-ranked AI risks — options considered, chosen response, named owner and target date for each.
- **EV-641** 4 of 5 plans have a completion record with dated evidence; 1 (vendor concentration) is past its target date (2026-08-31) with a revised date recorded at the 2026-09 review.
- **EV-642** Plans are reviewed at every AI Steering Committee meeting (quarterly) and the review records the status of each plan.

### MAN-1.4 — Residual risk acceptance
- **EV-650** Residual risk register — entries for VIC-2 (signed by the Monterrey Plant Quality Manager 2026-05-28), PDM (Brno Plant Manager 2026-06-02), DFE and LDA (Columbus Plant Quality Manager, 2026-04 and 2026-07); each entry documents the residual risks and carries a signature and date.
- **EV-652** Downstream owner notification is recorded for VIC-2 (customer quality manager acknowledged 2026-06-03) and PDM (maintenance manager acknowledged 2026-06-05).
- **EV-653** 4 of 6 systems have a residual risk acceptance; SDE and QAP have none.

### MAN-2.1 — Non-AI alternative evaluation
- **EV-660** VIC-2 options analysis (2025-10) — rule-based image thresholds, additional human inspectors, outsourced inspection and no-change compared with the model on cost, throughput, false-reject rate and escape rate.
- **EV-661** The rationale for choosing the model is documented and approved by the business case sponsor (VP Operations) and the Plant Quality Board.
- **EV-662** Options analysis exists for 4 of 6 systems; the standard business case template was amended in 2026-06 to require an alternatives section, so SDE and LDA will carry one at their next business-case refresh.

### MAN-2.2 — Value sustainment and decay monitoring
- **EV-670** Maintenance plan for each of the six systems — named owner, quarterly review of value metrics, retraining and recalibration triggers, and a model-refresh schedule.
- **EV-671** Value metrics reviewed quarterly; the 2026-Q2 review flagged a utilisation decline on one Monterrey part family (down 18%), traced to a customer volume change, and the 2026-Q3 review recorded the decision to keep the system in service.
- **EV-672** All six systems carry a maintenance plan and a quarterly value review record; no system is without a review in 2026.

### MAN-2.3 — Emergent risk procedure
- **EV-680** "Emergent AI Risk and Recovery Procedure" (2026-03) — triage path, recovery steps, rollback, communication and a lessons-learned log; owner: AI Governance Lead.
- **EV-681** Applied twice in 2026 (2026-05 lighting incident, 2026-08 MES interface incident): recovery records with timeline, rollback step and the lessons-learned entry exist for both.
- **EV-682** Lessons-learned entries are reviewed at the next AI Steering Committee meeting and the review is minuted; both 2026 entries produced a procedure change (a lighting-change checklist and an interface-change pre-release test).

### MAN-2.4 — Deactivation mechanisms
- **EV-690** Deactivation mechanism documented for all six systems: VIC-2 and LDA use a line feature flag with the shift supervisor as the named operator and the Model Owner as the accountable role; SDE, DFE, PDM and QAP use a documented vendor or MES procedure with a named operator.
- **EV-691** Two game-day drills in 2026 (2026-03 and 2026-08) covering all six systems, with fallback to manual inspection confirmed at Monterrey and to manual document handling for SDE.
- **EV-692** Drill records show the measured time to deactivate per system (median 5 minutes, worst 18 minutes for PDM) against a stated 30-minute target, reported to the AI Steering Committee with the drill record.
- **EV-693** Drill findings are tracked to closure: 3 findings from the 2026-03 drill, all closed by 2026-08 with dated evidence.

### MAN-3.1 — Post-contract third-party monitoring
- **EV-700** Vendor monitoring schedule (quarterly) for the 3 critical AI vendors (VIC-2 model, camera/optics, cloud inference); performance and SLA reports collected each quarter.
- **EV-701** 2026-Q2 review raised 7 issues, 6 closed with dated evidence, 1 open with an owner and a date; the 2026-Q3 review raised 4, all open with dates.
- **EV-702** The 3 lower-spend AI vendors (SDE, PDM, QAP) are not on the monitoring schedule; no performance review exists for them since onboarding.

### MAN-3.2 — Model version and drift tracking
- **EV-710** Model inventory records vendor model version, release date, change notification and the internal approval for all six systems, including vendor-hosted models.
- **EV-711** 5 model or version changes in 2026; 4 triggered a re-evaluation before release (dates recorded), 1 (SDE extraction model, 2026-09) was applied without evaluation and is recorded as a finding in the compliance tracker.
- **EV-712** Version changes are captured from vendor notifications into the inventory within 5 working days; the inventory is reconciled against vendor release notes quarterly, and the 2026-Q2 reconciliation found one unrecorded minor version bump, now recorded.
- **EV-713** Drift and regression metrics per model are reviewed monthly with the model owners; the 2026-09 review flagged PDM with a 4-point accuracy drop and triggered a re-evaluation.

### MAN-4.1 — Post-deployment plans implemented
- **EV-720** For VIC-2: production monitoring live (EV-460), inspector appeal/override process operational (1,240 overrides logged, 41 appeals to the shift supervisor with dispositions), decommissioning procedure tested in the 2026-08 drill.
- **EV-721** Post-deployment review 2026-09 confirms all three operate for VIC-2, PDM, DFE and LDA; issues recorded (appeal disposition backlog of 12 cases).
- **EV-722** These plans are implemented for 4 of 6 systems; SDE has monitoring only, and QAP has neither monitoring nor an appeal route.

### MAN-4.2 — Improvements fed back from monitoring
- **EV-730** Improvement backlog linked to monitoring findings, feedback items and audit findings — 22 items raised in 2026, 16 released.
- **EV-731** Release notes for every 2026 release (5 releases) cite the finding, feedback item or audit reference that triggered the change.
- **EV-732** Measured effect per release (before/after delta on the target metric) is recorded for 11 of the 16 releases; throughput (22 raised, 16 released) is reported quarterly to the AI Steering Committee.

### MAN-4.3 — Incident communication
- **EV-740** AI incident register 2026 — 4 incidents (lighting 2026-05, MES interface 2026-08, camera failure 2026-03, escape 2026-05), each with severity, affected population, affected customers and communication actions.
- **EV-741** 3 incidents required customer notification; notification records exist for all 3 (2 within the 24-hour target, 1 at 31 hours, recorded as a breach), and the escape incident also triggered a customer quality report.
- **EV-742** A time-to-notify target (24 hours for a customer-affecting incident) is defined in the incident procedure, and notification performance is reported to the AI Steering Committee quarterly with the breach recorded.
