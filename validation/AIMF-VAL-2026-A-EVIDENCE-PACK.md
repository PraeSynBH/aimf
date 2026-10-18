# AIMF Instrument Validation — Case Study A (B2 baseline)

**Fixture id**: AIMF-VAL-2026-A
**Purpose**: a fixed, recorded evidence pack used to measure whether the AIMF anchors
(AIMF-ASSESSMENT-QUESTION-BANK, Anchor 0..4) make two assessors produce the same score.
**Status**: validation fixture, not a customer engagement. The organisation is fictional;
the evidence is written to be complete, dated and self-consistent so that a score can be
decided from the pack alone.
**Baseline**: B2 (moderate risk). **Profile**: full framework (72 controls) so the run covers
the whole catalog. **Assessment window**: 2026-Q3. **System in scope**: Claims Triage
Assistant (CTA) plus organisation-wide AI management.

**How an assessor uses this pack**: score each control from the artefacts listed under it,
using only the anchors for that control. If the pack does not let you decide, record
`NA` (not assessable) and say what is missing — do not default to 0.

**Organisation**: Calder Ridge Health Plan (CRHP), regional health insurer, 1,400 staff,
4 business units (Claims, Clinical Services, Member Services, Enterprise Technology).
Artefact ids are `EV-nnn`; dates are ISO.

---

## GOVERN — 19 controls

### GOV-1.1 — AI legal and regulatory policy
- **EV-014** "AI Governance Policy v3.1" — approved by the AI Risk Committee 2026-01-14, effective 2026-02-01, applies to all four business units.
- **EV-015** "Regulatory Mapping Appendix A" (annex to EV-014) — maps EU AI Act, Colorado SB24-205 and the NAIC Model Bulletin to policy clauses; review date recorded as 2027-01-14.
- **EV-016** "Policy exception register" — two open exceptions (Claims Triage Assistant, vendor screening pilot), neither carries a date or an approver.
- **EV-017** Legal memo 2025-11-03 confirming the mapping appendix was reviewed by external counsel.

### GOV-1.2 — AI system inventory and risk classification
- **EV-020** "AI System Register" (SharePoint list) — 14 systems listed with owner, purpose, use case, vendor and risk class (low/medium/high).
- **EV-021** Register field audit 2026-08-19 — 14 of 14 rows have purpose and use case; 11 have a risk class; 3 are blank.
- **EV-022** Deployment gate ticket template requiring "AI Risk Committee classification approval" attached before production release; 9 of 14 systems have a linked approval ticket.
- **EV-023** Email 2026-07-02 from Enterprise Technology noting two clinical pilots were running "ahead of registration".

### GOV-1.3 — AI risk in the enterprise risk framework
- **EV-030** "Enterprise Risk Framework v7" (approved 2026-03-04) — contains an "AI and Algorithmic Risk" category with definitions and a scoring scale.
- **EV-031** AI risk appetite statement (approved 2026-03-04) — threshold: "no high-risk AI system in production without an accepted residual risk record".
- **EV-032** Risk register export 2026-09-30 — 6 AI risks recorded; 4 have owners; 2 have no escalation history.
- **EV-033** Board Risk Committee minutes 2026-06-11 — AI risk is item 4 on the standing agenda; minutes record one escalation (claims model drift).

### GOV-1.4 — Compliance monitoring of AI policy
- **EV-040** "AI Compliance Monitoring Plan 2026" — quarterly checks against 12 policy clauses, owner: Compliance Officer.
- **EV-041** Q1 and Q2 2026 monitoring reports — Q1 covered 9 of 12 clauses; Q2 covered 12 of 12; findings listed.
- **EV-042** Findings tracker — 11 findings raised in 2026, 4 closed with evidence, 7 open; no target dates on 5 of the 7.
- **EV-043** Effectiveness KPI defined for each of the 12 policy clauses (e.g. "share of in-scope systems with a current classification"); reported quarterly against a per-clause target.
- **EV-044** 2026-Q2 KPI report: 9 of 12 clauses at target; 3 below target with named actions and owners.

### GOV-1.5 — Environmental impact of AI
- **EV-050** AI Governance Policy v3.1 §9 requires environmental impact to be "considered where material".
- **EV-051** No environmental assessment exists for CTA or any of the 14 registered systems.
- **EV-052** Sustainability report 2025 mentions AI compute in one paragraph without figures.

### GOV-1.6 — Decommissioning process
- **EV-060** "AI System Retirement Procedure v2" (approved 2026-05-20) — covers data retention, disposal, stakeholder notification and a 30-day notice period.
- **EV-061** Retirement record for "Member Chatbot v1" (retired 2026-04-30) — data disposal certificate attached, 3 stakeholder notifications logged.
- **EV-062** Procedure applied to 1 of 3 systems retired since approval; the other two were switched off by their product teams.

### GOV-1.7 — Third-party AI arrangements
- **EV-070** Vendor AI Addendum (template, legal-approved 2026-02-10) — audit rights, model-change notification, data-use restrictions.
- **EV-071** Vendor register — 9 AI vendors; 6 have a signed addendum, 3 are on legacy MSA terms.
- **EV-072** Vendor risk assessments — 5 of 9 completed; none reviewed since onboarding.
- **EV-073** Procurement note 2026-08: addendum negotiation is "best effort" for renewals under $50k.

### GOV-2.1 — AI risk roles and escalation
- **EV-080** AI RACI (v1.2, 2026-02-28) — names an owner for 11 AI risk activities across 6 roles.
- **EV-082** Role descriptions for Chief AI Officer, Model Owner and AI Risk Analyst include AI risk duties (HR records, 2026-03).
- **EV-083** Escalation path published on the intranet; 7 of 9 staff interviewed in the pilot (2026-08) could name it.
- **EV-084** Two activities in the RACI (vendor AI monitoring, incident communication) have no named owner.

### GOV-2.2 — Role-based AI risk training
- **EV-090** "AI Risk Essentials" LMS course — mandatory for 4 role families since 2026-01; 78% completion.
- **EV-091** Role-based module for model owners launched 2026-06; completion 41% (12 of 29).
- **EV-092** No competency assessment: completion is a click-through quiz with a 70% pass mark, no practical component.
- **EV-093** Refresher cycle set at 24 months in the LMS; no cohort has yet reached it.

### GOV-2.3 — Executive oversight
- **EV-100** AI Risk Committee charter (approved 2026-02-01) — quarterly cadence, quorum, decisions recorded.
- **EV-101** Minutes for 2026-03, 2026-06, 2026-09 — all three held; attendance 5-7 of 8 members.
- **EV-102** Committee decisions log — 9 decisions in 2026, 6 with a named action owner.
- **EV-103** AI strategy review is not on the committee's agenda; strategy sits with the Strategy Office.

### GOV-3.1 — Interdisciplinary expertise in AI teams
- **EV-110** "AI Team Composition Standard" (2026-01) — requires product, clinical, data science, legal and security representation per AI project.
- **EV-112** CTA team composition record — product, data science, clinical, security present; legal represented by an advisor who attended 2 of 9 design reviews.
- **EV-113** Composition review completed for 1 of 4 AI projects in 2026.
- **EV-114** No inclusion metrics are collected.

### GOV-3.2 — Demographic representation monitoring
- **EV-120** HR diversity dashboard covers all staff, not AI roles specifically.
- **EV-121** 2025 hiring review includes one paragraph on "technical roles" with no AI-specific breakdown.
- **EV-122** No action plan exists for AI representation; no promotion analysis by role.

### GOV-4.1 — AI risk culture
- **EV-130** "Responsible AI" awareness campaign 2026-Q2 — 4 town halls, intranet series.
- **EV-131** Engagement survey 2026 — one AI item ("I know how to raise an AI concern"): 62% favourable.
- **EV-132** AI risk behaviours are not in performance objectives or recognition criteria.
- **EV-133** No culture metric is tracked over time; the survey item was added in 2026 and has one data point.

### GOV-4.2 — Stakeholder feedback on AI systems
- **EV-140** Member feedback channel (web form + call centre) captures AI complaints as a tag; 214 items in 2026.
- **EV-141** Feedback review meeting monthly; decisions are recorded in a product backlog with no link back to the feedback item.
- **EV-142** Two changes (letter wording, appeal timing) are attributed to feedback in release notes but the linkage is narrative, not recorded.
- **EV-143** No response is sent to the person who raised the feedback.

### GOV-4.3 — Transparency communication
- **EV-150** Public "How we use AI" page published 2026-04, lists 5 of 14 systems, last updated 2026-04.
- **EV-151** Internal AI newsletter quarterly.
- **EV-152** No transparency report; no correction or notice process for published statements.
- **EV-153** Publication is owned by Communications with no review by the AI Risk Committee.

### GOV-5.1 — External governance participation
- **EV-160** Membership of one industry association AI working group (2026), attendance at 2 of 4 meetings.
- **EV-162** One response to a state insurance regulator consultation (2026-05), filed by the Compliance Officer.
- **EV-163** No documented engagement plan; no record of follow-up on the consultation.

### GOV-5.2 — Research collaborations
- **EV-170** No academic partnerships, no research agreements, no publications.
- **EV-171** One data scientist collaborates informally with a university lab on a personal basis; no agreement exists.

### GOV-6.1 — Governance resourcing
- **EV-180** FY2026 budget line "AI Governance" — $420k, approved, with 2.5 FTE and a governance platform licence.
- **EV-181** Actual spend Q1-Q3 2026: $290k; 2 of 2.5 FTE filled.
- **EV-182** The governance platform is deployed and holds the register, RACI and policy library.

### GOV-6.2 — Capability-building plan
- **EV-190** "AI Governance Capability Plan 2026-2027" — funded, 5 milestones, owner Chief AI Officer.
- **EV-191** Progress review 2026-07 — 2 of 5 milestones complete, 1 slipped; recorded in committee minutes.
- **EV-192** Skills inventory is a spreadsheet last updated 2025-12.

## MAP — 18 controls

### MAP-1.1 — Purpose, beneficial use and deployment setting
- **EV-200** CTA System Definition v2.1 (2026-03-18) — purpose, intended population, deployment setting (claims intake queue), out-of-scope uses.
- **EV-201** Legal review record (2026-03-05) — covers state insurance law and unfair-discrimination exposure; signed by counsel.
- **EV-202** Definition exists for CTA and one other system; the remaining 12 registered systems have a one-paragraph description only.

### MAP-1.2 — Interdisciplinary competency requirements
- **EV-210** "AI Competency Framework" (2026-02) — lists required competencies per role family (product, clinical, data science, legal, security).
- **EV-211** Project staffing checklist requires each competency to be named; signed off for 1 of 4 AI projects.
- **EV-212** No diversity or inclusion metric is produced per project.

### MAP-1.3 — AI strategy and mission review
- **EV-220** "CRHP AI Strategy 2026-2028" — approved by the board 2026-01-29, 4 strategic themes tied to the mission statement.
- **EV-221** Strategy reviewed against the mission annually; the 2027 review is scheduled, not yet held.
- **EV-222** Four strategic KPIs defined; Q2 dashboard shows 2 of 4 on track.

### MAP-1.4 — Business case and value tracking
- **EV-230** CTA business case (2025-11) — cost, expected 18% reduction in manual triage minutes, value metrics defined.
- **EV-231** Post-deployment value report (2026-08) — measured 11% reduction against the 18% target; variance explained.
- **EV-232** Business cases exist for 4 of 14 systems; value tracking exists for 2.

### MAP-1.5 — Risk tolerances
- **EV-240** AI risk appetite statement (2026-03-04) — 3 tolerances, one quantified ("false-negative rate on urgent claims ≤ 0.5%").
- **EV-241** Approval by the Board Risk Committee recorded in minutes 2026-03-04.
- **EV-242** Actual performance against the quantified tolerance is reported once (2026-08), not on a cadence.

### MAP-1.6 — Socio-technical requirements and traceability
- **EV-250** CTA Requirements Specification v3 (2026-04) — 148 requirements, including 22 socio-technical (operator workload, explainability to adjusters).
- **EV-251** Traceability matrix links 96 of 148 requirements to a test case; the 22 socio-technical requirements have no linked tests.
- **EV-252** Clinical and adjuster workshops (3, 2026-02/03) recorded; input attributed per requirement in 41 cases.

### MAP-2.1 — Task taxonomy and method documentation
- **EV-260** "AI Task Taxonomy v1" (2026-02) — 9 task categories (classification, extraction, ranking, generation...), used in the register.
- **EV-261** Register field "task category" is populated for 14 of 14 systems.
- **EV-262** Method documentation exists per system for 6 of 14; CTA's method note (2026-03) is 2 pages and current.

### MAP-2.2 — Knowledge limits and human oversight
- **EV-270** CTA "Known Limits and Escalation" note (2026-05) — lists out-of-scope claim types, confidence thresholds, and the rule that an adjuster must confirm every high-value decision.
- **EV-271** Oversight rule is enforced in configuration: claims above $25k route to manual review regardless of model output (config export 2026-09-12).
- **EV-272** Limits note exists only for CTA; other systems rely on vendor documentation.

### MAP-2.3 — Scientific methodology and TEVV
- **EV-280** CTA "Evaluation Methodology" (2026-04) — test design, metrics, sampling, and a "known limitations" section covering distribution shift and label noise.
- **EV-281** TEVV plan with 3 planned validation activities; one (drift re-validation) has no date or owner.
- **EV-282** Methodology reviewed by the Head of AI Quality; no independent peer review.

### MAP-3.1 — Expected benefits and validation method
- **EV-290** Benefits analysis for CTA — quantified baseline (triage minutes per claim), target, and a stated validation method (A/B on 2 queues).
- **EV-291** Validation was run 2026-07 and reported; result 11% vs 18% target.
- **EV-292** Benefits analysis exists for 3 of 14 systems; no validation method for the other 11.

### MAP-3.2 — Costs including non-monetary
- **EV-300** CTA total-cost model (2025-11) — licence, integration, staffing, and a qualitative line for "adjuster trust and rework".
- **EV-301** Non-monetary costs are named but not quantified; no link to the risk tolerance statement.
- **EV-302** Cost tracking updated quarterly; 2026-Q2 actuals recorded.

### MAP-3.3 — Application scope and change control
- **EV-310** CTA scope statement (2026-03) — claim types, queues, geographies, excluded populations.
- **EV-311** Change log with 7 scope changes, all 7 approved by the AI Risk Committee under the recorded change process.
- **EV-312** Scope-drift check run per release (2026-03, 2026-07, 2026-09): inputs and uses compared with the recorded scope; one drift found in 2026-07 and re-scoped.

### MAP-3.4 — Operator proficiency
- **EV-320** "Adjuster AI Proficiency Standard" (2026-06) — 4 proficiency levels, assessment by supervised case review.
- **EV-321** 34 of 61 adjusters assessed (2026-08); results recorded in the LMS.
- **EV-322** No certification requirement; no refresher cycle defined.

### MAP-3.5 — Human oversight effectiveness
- **EV-330** Oversight procedure (2026-05) documents who reviews what, override rights and escalation.
- **EV-331** Override log 2026: 412 overrides, 38% of sampled overrides rated "appropriate" on a 20-case audit.
- **EV-332** Oversight effectiveness assessed once (2026-08 audit), no cadence set, findings not yet actioned.

### MAP-4.1 — Third-party AI mapping
- **EV-340** Third-party AI dependency map (2026-07) — covers CTA's vendor model, OCR service and cloud inference; data flows and legal exposure noted.
- **EV-341** Legal review recorded for 3 of 9 AI vendors.
- **EV-342** Map is maintained by Enterprise Technology; not reviewed by the AI Risk Committee.

### MAP-4.2 — Controls over third-party components
- **EV-350** Control descriptions for third-party AI (2026-07) — 8 controls (model change notification, data residency, output monitoring, exit plan...).
- **EV-351** Implementation evidence exists for 3 of 8 controls; no effectiveness testing recorded.
- **EV-352** Vendor model-change notifications are received by email and not tracked.

### MAP-5.1 — Impact assessment
- **EV-360** CTA impact assessment (2026-03) — affected groups (members, adjusters, providers), potential harms, mitigations.
- **EV-361** Assessment reviewed by the AI Risk Committee; two mitigations adopted (appeal letter, manual review threshold).
- **EV-362** Impact assessment exists for 1 of 14 systems; no template mandated by policy.

### MAP-5.2 — Stakeholder engagement
- **EV-370** Engagement plan for CTA (2026-02) — member panel (2 sessions), provider forum (1), adjuster workshops (3).
- **EV-371** Records exist for 4 of 6 planned sessions: participant lists, notes, and a changes log.
- **EV-372** Changes attributed to engagement: 3 (letter clarity, appeal timing, threshold).
- **EV-373** Member panel recruitment was through the existing customer council, not a sample of affected members.

## MEASURE — 22 controls

### MEA-1.1 — Risk metrics per system
- **EV-400** "AI Measurement Framework v1" (2026-04) — 2-3 metrics per risk category, owner per metric, reporting cadence.
- **EV-401** CTA dashboard (Grafana) shows false-negative rate, override rate, latency and drift score; refresh daily.
- **EV-402** Framework maps all 24 risk categories to at least one metric; 22 are instrumented directly and 2 use documented proxy metrics.
- **EV-403** Coverage report (share of risk categories with an instrumented metric) issued quarterly; 2026-Q2 shows 100% coverage, reviewed by the AI Risk Committee.

### MEA-1.2 — Metric validity review
- **EV-410** Metric definitions document includes a "what this metric can and cannot show" note for 4 of 9 metrics.
- **EV-411** One validation study (2026-05) on the false-negative metric — compared against a 400-claim manual review sample; found the metric under-counts by 1.8x.
- **EV-412** Revision history exists for all 9 metrics; each has a documented false-positive and false-negative analysis.
- **EV-413** Annual metric re-validation is scheduled and was completed for 2026 in September.

### MEA-1.3 — Independent assessors
- **EV-420** Internal Audit charter requires independent review of "models materially affecting members"; CTA is listed as in scope for 2026.
- **EV-421** Internal Audit review of CTA (2026-07) — independence statement signed; 6 findings.
- **EV-422** External assessor has not been used; independence of the internal reviewer recorded per engagement.

### MEA-2.1 — Reproducible test records
- **EV-430** CTA evaluation repository (Git) — test scripts, dataset version hashes, metric code, run logs.
- **EV-431** Run manifest for the 2026-07 evaluation: dataset v3.2 hash, container image digest, seed.
- **EV-432** Reproducibility audit 2026-09: 9 of 12 evaluations could be re-run by a third party from the repository without help; 3 legacy runs lacked manifests, which the audit records as a defect.

### MEA-2.2 — Human-subject evaluations
- **EV-440** No human-subject evaluation has been run in the period; adjuster workshops were process design, not research.
- **EV-441** No IRB or ethics review process exists for AI research; the organisation has no research ethics policy.
- **EV-442** No consent records, no sampling rationale.

### MEA-2.3 — Pre-defined performance criteria
- **EV-450** CTA acceptance criteria (2026-03) — false-negative ≤ 0.5%, false-positive ≤ 8%, latency ≤ 900ms, defined before testing.
- **EV-451** Test report (2026-07) demonstrates 0.42% / 7.1% / 640ms on deployment-like replay of 12,000 claims.
- **EV-452** Criteria were met; two criteria (explainability rating, adjuster trust) were added after testing and apply from the next release.
- **EV-453** Results-versus-criteria table per release (2026-03, 2026-07, 2026-09) with the acceptance decision recorded against each criterion.

### MEA-2.4 — Production monitoring
- **EV-460** Production monitoring covers input schema, latency, output distribution and drift score for all 14 in-scope systems; alerts to on-call.
- **EV-461** 4 alerts in 2026, all acknowledged within SLA; 1 incident (2026-08) traced to an upstream data change.
- **EV-462** Detection precision (0.84) and recall (0.79), and alert-to-action time (median 5.5h), measured monthly and reviewed by the AI Operations Council.
- **EV-463** Predictive alerting added 2026-05 from the incident analysis; two thresholds were re-set from measured incident data, and the re-set cut alert-to-action time from 9h to 5.5h.

### MEA-2.5 — Validity, reliability, generalisability
- **EV-470** Validity study (2026-06) — face and content validity by clinical panel; test-retest on 2,000 claims (κ = 0.81).
- **EV-471** Generalisability assessed on one held-out region only; two regions have < 200 claims each and were excluded.
- **EV-472** Reliability across labelers not assessed.

### MEA-2.6 — Safety evaluation and residual risk
- **EV-480** Safety evaluation (2026-05) — fail-safe test on model timeout, malformed input, and downstream outage; results documented.
- **EV-481** Residual safety risks documented (3 items: misrouted urgent claim, silent degradation, vendor outage) with acceptance by the Model Owner.
- **EV-482** No periodic re-test; the evaluation was one-off.

### MEA-2.7 — Adversarial evaluation
- **EV-490** Red-team exercise commissioned 2026-06; report delivered under legal privilege.
- **EV-491** Report reference only: "CRHP-RT-2026-06, restricted". Contents not available to the assessment.
- **EV-492** Resilience measures are referenced in the report; no separate summary exists.

### MEA-2.8 — Transparency and accountability risk
- **EV-500** Transparency risk assessment (2026-04) covering member-facing notice, adverse-action explanation and appeal.
- **EV-501** Member notice text approved; adverse-action letters include the model's top-2 reasons.
- **EV-502** Assessment covers CTA only; no requirement for other systems.

### MEA-2.9 — Explainability to decision-makers
- **EV-510** Explainability design note (2026-04) — SHAP-based top-3 factors shown to adjusters; interpretation guidance in the adjuster handbook.
- **EV-511** 20-case interpretability study with 6 adjusters: 17 of 20 explanations rated "actionable".
- **EV-512** Guidance not updated since the 2026-07 model refresh.

### MEA-2.10 — Privacy
- **EV-520** Privacy impact assessment for CTA (2026-03) — data minimisation, retention, member rights, re-identification risk.
- **EV-521** Privacy-preserving techniques assessed: pseudonymisation in place; differential privacy considered and rejected with rationale.
- **EV-522** PIA exists for 2 of 14 systems; privacy review is not gated in the deployment process.

### MEA-2.11 — Bias and fairness
- **EV-530** Fairness evaluation (2026-07) — 4 metrics (demographic parity, equalised odds, calibration by group, error-rate ratio) across age, sex, and 3 regional groups.
- **EV-531** Two disparities flagged (age band 65+, rural region); mitigation options assessed, one adopted (threshold adjustment), one deferred.
- **EV-532** Retest after mitigation completed 2026-09; disparity reduced but not eliminated.
- **EV-533** Fairness results are reported by group for each release (2026-03, 2026-07, 2026-09) against pre-set thresholds; one threshold was breached in 2026-07 and remediated.
- **EV-534** No fairness evaluation for other in-scope systems.

### MEA-2.12 — Environmental impact
- **EV-540** No energy, compute or carbon figure is collected for inference or training; the vendor contract does not require one.
- **EV-541** No efficiency target; the sustainability report does not mention AI.
- **EV-542** No assessment exists for any of the 14 systems.

### MEA-2.13 — TEVV programme effectiveness
- **EV-550** TEVV review (2026-09) — coverage analysis (62% of requirements tested), defects found post-release (3), and two process changes adopted.
- **EV-551** Metric effectiveness assessed for 2 of 9 metrics.
- **EV-552** Review covers CTA's testing only, not the organisation's testing programme.

### MEA-3.1 — Standing risk tracking
- **EV-560** "AI Risk Tracking Log" — named owner (AI Risk Analyst), monthly review, 23 entries in 2026 including 5 emergent risks.
- **EV-561** Review minutes for 8 of 9 months; one month skipped with no note.
- **EV-562** Emergent-risk entries have owners; 7 of 23 have a closure record.

### MEA-3.2 — Alternative measurement where conventional metrics fail
- **EV-570** "Assessment Methods for Hard-to-Measure Risks" note (2026-05) — 3 alternative methods (structured expert elicitation, scenario walkthrough, incident-proxy) with stated limits.
- **EV-571** Two methods used once each (expert elicitation for trust, scenario walkthrough for fairness perception); records exist.
- **EV-572** Methods not applied to other hard-to-measure risks; no guidance on choosing between them.

### MEA-3.3 — End user and community feedback
- **EV-580** Member complaint channel tags AI-related complaints; 214 items in 2026.
- **EV-581** Appeal process documented and available to members; 31 appeals, 9 upheld.
- **EV-582** Feedback is analysed monthly by the product team; analysis is not published and not linked to system changes in a recorded way.

### MEA-4.1 — Measurement in deployment context
- **EV-590** All CTA evaluations run on replay of production claim data (12,000 claims from the live queue), not benchmarks.
- **EV-591** Clinical input into test design recorded (3 sessions); adjuster input into criteria recorded.
- **EV-592** Two vendor benchmark comparisons are also used for model selection; the benchmark results are not validated against CRHP data.

### MEA-4.2 — Expert review of measurement results
- **EV-600** Measurement results reviewed by the Clinical Advisory Panel (2026-07) and by Internal Audit (2026-07).
- **EV-601** Reviewer independence from the build team recorded for Internal Audit; the Clinical Advisory Panel includes one member who advises the CTA product team.
- **EV-602** Review comments are recorded in meeting minutes; two led to re-analysis.

### MEA-4.3 — Performance change detection and root cause
- **EV-610** Drift monitoring with alert thresholds; 2 performance declines detected in 2026 (2026-04, 2026-08).
- **EV-611** Root-cause analysis recorded for both; the 2026-08 decline traced to upstream coding changes, fix deployed and retested.
- **EV-612** Detection latency (median 2 days from drift onset) and change-to-action time (median 6 days) measured and reported monthly.
- **EV-613** The change-detection process is applied to all 14 systems; 6 have had at least one documented change event.

## MANAGE — 13 controls

### MAN-1.1 — Go/no-go decision with criteria and approval
- **EV-620** "AI Deployment Decision Procedure v2" (2026-02) — 6 go/no-go criteria, approver named (AI Risk Committee), decision record template.
- **EV-621** Decision records exist for all 14 registered systems; CTA's record (2026-03-26) shows 5 of 6 criteria met, 1 waived with rationale.
- **EV-623** Decision metrics (9 approvals, 3 approvals with conditions, 2 rejections) reviewed quarterly against the criteria by the AI Risk Committee.
- **EV-622** Two clinical pilots deployed without a decision record (email trail 2026-07).

### MAN-1.2 — Risk prioritisation driving resourcing
- **EV-630** "AI Risk Prioritisation Method" (2026-03) — impact × likelihood × regulatory exposure; produces a ranked list.
- **EV-631** Ranked register produced 2026-04 and 2026-07; 5 top risks.
- **EV-632** FY2026 allocation: 2 of the top 5 risks received named budget; the other 3 have plans but no funding decision recorded.

### MAN-1.3 — Response plans for top risks
- **EV-640** Response plans for 5 top-ranked AI risks — options considered, named owner, target date.
- **EV-641** 2 of 5 plans have a completion record; 3 are past their target date with no update.
- **EV-642** Plans reviewed at the AI Risk Committee quarterly; the 2026-09 review deferred 3 plans without a new date.

### MAN-1.4 — Residual risk acceptance
- **EV-650** Residual risk register — CTA's entry documents residual risks and is signed by the Chief Claims Officer (2026-03-30).
- **EV-652** Downstream owner notification recorded for CTA (adjuster operations manager acknowledged 2026-04-02).
- **EV-653** Acceptance exists for 4 of 14 systems; 3 systems in production have no residual risk record.

### MAN-2.1 — Non-AI alternative evaluation
- **EV-660** CTA options analysis (2025-10) — rule-based triage, outsourced human triage and no-change compared against the model on cost and error rate.
- **EV-661** Rationale for choosing the model documented; approved by the business case sponsor.
- **EV-662** Options analysis exists for 2 of 14 systems; the standard business case template has no alternatives section.

### MAN-2.2 — Value sustainment and decay monitoring
- **EV-670** CTA maintenance plan (2026-04) — owner, quarterly review of value metrics, retraining triggers.
- **EV-671** Value metrics reviewed 2026-07 and 2026-09; the 2026-09 review flagged utilisation decline in one queue.
- **EV-672** Maintenance plan exists for 1 of 14 systems; no other system has a value review.

### MAN-2.3 — Emergent risk procedure
- **EV-680** "Emergent AI Risk and Recovery Procedure" (2026-05) — triage path, recovery steps, lessons-learned log.
- **EV-681** Applied once (2026-08 upstream data incident): recovery record and lessons-learned entry exist.
- **EV-682** Lessons-learned log has 1 entry; no review cadence; procedure not exercised for 13 other systems.

### MAN-2.4 — Deactivation mechanisms
- **EV-690** CTA kill switch documented (feature flag) and tested 2026-06 in a game-day exercise; responsibility assigned to the Model Owner.
- **EV-691** Test record: system disabled within 4 minutes, fallback to manual triage confirmed.
- **EV-692** Deactivation mechanism documented and tested for all 14 systems in the 2026-06 game day (staggered); 3 depend on vendor procedures and were tested with the vendor present.
- **EV-693** Time-to-deactivate measured per system in the drill (median 6 minutes, worst 22 minutes) and reported against a 30-minute target.

### MAN-3.1 — Post-contract third-party monitoring
- **EV-700** Vendor monitoring schedule (quarterly) for 4 critical AI vendors; performance and SLA reports collected.
- **EV-701** 2026-Q2 review raised 6 issues, 4 closed; 2 open past their date.
- **EV-702** Vendor monitoring is not applied to 5 lower-spend AI vendors; no contract review records since onboarding.

### MAN-3.2 — Model version and drift tracking
- **EV-710** Model inventory records vendor model version, release date and change notification for CTA and the fraud model.
- **EV-711** 3 vendor model updates in 2026; 2 triggered a re-evaluation (2026-03, 2026-07), 1 was applied without evaluation (2026-09).
- **EV-712** Inventory covers all 14 systems, including vendor-hosted models; version changes are captured from vendor notifications.
- **EV-713** Drift and regression metrics per model reviewed monthly; the 2026-09 review flagged one model with a 3-point accuracy drop and triggered re-evaluation.

### MAN-4.1 — Post-deployment plans implemented
- **EV-720** CTA: production monitoring live, appeal process operational (31 appeals), decommissioning plan tested in the 2026-06 game day.
- **EV-721** Post-deployment review 2026-08 confirms all three operate; issues recorded (appeal backlog of 6 days).
- **EV-722** These plans are implemented for 1 of 14 systems; 4 systems have monitoring only.

### MAN-4.2 — Improvements fed back from monitoring
- **EV-730** Improvement backlog linked to monitoring findings; 14 items in 2026, 9 released.
- **EV-731** Release notes 2026-07 and 2026-09 reference the finding that triggered each change.
- **EV-732** Improvement throughput (14 raised, 9 released in 2026) and measured effect per release (A/B delta on the target metric) recorded for 7 of the 9 releases.

### MAN-4.3 — Incident communication
- **EV-740** AI incident register (2026) — 5 incidents, severity, affected population, communication actions.
- **EV-741** 3 incidents required member notification; notification records exist for 2, the third was internal-only by decision of the incident lead.
- **EV-742** No defined time-to-notify target; communication templates exist for data breach, not for AI incidents.

