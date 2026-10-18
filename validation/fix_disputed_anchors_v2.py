#!/usr/bin/env python3
"""Instrument change P8, second pass (A3b): rewrite the anchors on the controls
that still split after v1.0.7.

Run 4 (AIMF-VAL-2026-A, v1.0.7 anchors) agreed on 51/72 controls (70.8%). The 21
controls that split are listed below. The diagnosis is unchanged from run 4: a
level boundary that is written as an adjective ("documented", "systematic",
"assessed") can be resolved either way on the same evidence pack, and a level
boundary written as a count cannot.

The rule applied to every edited row, identically:

  anchor 1 = the artefact exists but fails at least one COUNTABLE test: a stated
             population (register, deployment list, metric register, study
             register) not fully covered, a dated record missing for one member
             of that population, or a required element absent from the artefact.
  anchor 2 = the same artefact passes every countable test: 100% of the stated
             population, dated and current, with the named elements present.

Anchor 3 is edited only where the split was 2<->3 and the level-3 clause itself
was the ambiguous one (MEA-2.4, MEA-4.3, MEA-1.1); anchor 3/4 keep the ladder
prefixes the validator enforces. MEA-2.2 and GOV-3.2 required an anchor-0 edit
because the split was NA-vs-0 / 0-vs-1: those anchors now say when the absence is
established and when the verdict is NA.

Two failure patterns from the card are fixed where they occur:
  * bundled measurement + governance decision (GOV-1.3): anchor 2 now names the
    artefact that settles category coverage (the appetite statement) and the
    artefact that settles escalation (the dated register entry).
  * one artefact evidencing either clause (MEA-2.8): anchor 2 names two artefacts
    and requires both, so the control cannot be satisfied by the assessment alone.

Nothing outside the anchors listed here changed.
"""
import csv
import pathlib

BANK = pathlib.Path(__file__).resolve().parents[1] / "documents" / "AIMF-Full-Documentation" / "implementation" / "AIMF-ASSESSMENT-QUESTION-BANK.csv"

EDITS = {
    # ---- 1<->2 splits -------------------------------------------------------
    "GOV-1.3": {
        "anchor_1": "The AI risk appetite statement is approved and dated, but the number of risk categories carrying a threshold in that statement is smaller than the number of AI risk categories in the dated AI risk register export, or at least one register entry has no dated escalation record. Count the categories in the statement against the register export and check each entry for an escalation date: any mismatch or gap is level 1.",
        "anchor_2": "The approved, in-date AI risk appetite statement sets a threshold for every AI risk category in the dated AI risk register export - the category counts are equal and each category is named in the statement - every register entry carries a named owner and a dated escalation record, and the statement sits inside the approved enterprise risk framework.",
    },
    "GOV-2.3": {
        "anchor_1": "A charter, standing agenda and minutes exist, but at least one AI risk decision in the dated decisions log has no named action owner or no due date, or a meeting the charter cadence required in the last 12 months has no minutes. Count decisions against decisions carrying an owner, and required meetings against minutes: any gap is level 1.",
        "anchor_2": "The chartered executive committee has held every meeting its stated cadence required in the last 12 months, each with minutes recording attendance and decisions, and every decision in the dated decisions log carries a named action owner, a due date and a recorded disposition.",
    },
    "MAN-1.1": {
        "anchor_1": "A go/no-go procedure with documented criteria exists, but at least one deployment in the dated deployment list - pilots included - has no decision record, or a record lacks the named approver's sign-off. Count deployments in the deployment list against decision records carrying the approver's name and a date: any gap is level 1.",
        "anchor_2": "Every deployment in the dated deployment list, production and pilot alike, has a decision record that applies the documented criteria, carries the named approver's sign-off and date, and records any written waiver with its rationale.",
    },
    "MAN-3.2": {
        "anchor_1": "A model inventory exists, but at least one vendor model update in the dated change log has no dated re-evaluation record. Count version changes in the change log against re-evaluation records: any update relied on without an assessment of that model's performance is level 1.",
        "anchor_2": "The inventory covers every system in the dated scope register, and every vendor model update recorded in the change log for the last 12 months has a dated re-evaluation of that model's performance before the update is relied on.",
    },
    "MAN-4.2": {
        "anchor_1": "An improvement backlog linked to monitoring findings exists, but at least one release in the dated release log does not cite the finding that triggered it, or a release has no recorded measured effect. Count releases in the log against cited findings and against measured effects: any gap is level 1.",
        "anchor_2": "Every release in the dated release log cites the monitoring or user finding that triggered it, the backlog records which findings are open and closed, and each release carries a measured effect on its stated target metric with the measurement date.",
    },
    "MAP-1.3": {
        "anchor_1": "A dated, approved AI strategy tied to the mission exists, but the review register shows no review held in the last 12 months - a review that is merely scheduled does not count - or the review held did not test each strategic theme against the mission statement. Count reviews held in the last 12 months: zero is level 1.",
        "anchor_2": "The approved AI strategy is dated, ties each strategic theme to the mission statement, and has at least one minuted review in the last 12 months recording the date, the attendees and the mission test applied to each theme.",
    },
    "MAP-3.5": {
        "anchor_1": "An oversight procedure and an override log exist, but the procedure does not cite the AI policy clause it implements, or the effectiveness assessment on record has findings with no named owner or no due date, or oversight is not shown to cover every system in the scope register.",
        "anchor_2": "A procedure dated within the last 12 months covers every system in the scope register, cites the AI policy clause it implements, names the reviewer and the override rights per system, and every finding in the effectiveness assessment carries a named owner and a due date.",
    },
    "MEA-2.6": {
        "anchor_1": "A safety evaluation with fail-safe testing and a residual-risk entry exists, but the number of systems covered by safety evaluations is smaller than the number of systems in the dated scope register, or a residual-risk entry has no named acceptance. Count evaluated systems against the scope register: any shortfall is level 1.",
        "anchor_2": "Every system in the dated scope register has a safety evaluation that includes fail-safe testing, and each residual safety risk carries a named acceptance with the accepting role and the date.",
    },
    "MEA-2.8": {
        "anchor_1": "A transparency and accountability risk assessment exists, but one of the two required artefacts is missing or incomplete: the assessment does not name the affected population and the decision points, or there is no dated adequacy test recording what those people understood. Either gap is level 1.",
        "anchor_2": "Two artefacts exist and both are required: a dated transparency and accountability risk assessment naming the affected population and the decision points, and a separate dated adequacy test of the documentation carried out with that population, with the findings recorded.",
    },
    "MEA-2.11": {
        "anchor_1": "Bias testing with more than one metric and a grouped analysis exists, but it covers fewer systems than the dated scope register lists, or a flagged disparity has no recorded mitigation. Count systems with a fairness evaluation against systems in the scope register: any shortfall is level 1.",
        "anchor_2": "Every system in the dated scope register has a fairness evaluation covering the groups it affects, using more than one metric with thresholds set before the test, and every flagged disparity carries a recorded mitigation with a retest date.",
    },
    "MEA-3.1": {
        "anchor_1": "A risk tracking log with a named owner and a stated cadence exists, but a review month in the period has no minutes, or a system in the scope register has no dated entry. Count review months against minutes and systems against log entries: any gap is level 1.",
        "anchor_2": "The log names its owner and stated cadence, every review month in the period has dated minutes, every system in the dated scope register has at least one dated entry, and every emergent risk carries a named owner and a closure date.",
    },
    "MEA-3.3": {
        "anchor_1": "A complaint channel with a recorded volume and a documented appeal process exist, but appeal outcomes are not recorded, or no dated record links analysis of that feedback to a named change or decision. Either gap is level 1.",
        "anchor_2": "Three dated artefacts exist: a channel recording AI-related problems with a volume for the period, a documented appeal process with recorded outcomes, and a record showing that analysis of that feedback produced a named change or decision, with the date.",
    },
    # ---- 2<->3 / 3<->4 splits ----------------------------------------------
    "GOV-1.4": {
        "anchor_1": "A monitoring plan exists, but at least one period's report covers fewer clauses than the dated AI policy contains, or a finding in the tracker has no named owner or no target date. Count clauses monitored in each period against clauses in the policy, and findings against owner and date: any gap is level 1.",
        "anchor_2": "Every clause in the dated AI policy is monitored in each period's report, and every finding in the tracker carries a named owner, a target date and, once closed, dated closure evidence.",
    },
    "MEA-1.2": {
        "anchor_1": "A metric definitions document exists, but fewer than all metrics in the dated metric register carry a recorded validation of what the metric can and cannot show, or no metric has a dated revision made from validation evidence. Count metrics in the register against validated entries: any gap is level 1.",
        "anchor_2": "Every metric in the dated metric register carries a recorded validation - the claim it measures, its documented limits, and the study or manual-sample comparison that tested it - and at least one metric was revised from that evidence, with the revision dated in the revision history.",
    },
    "MEA-2.1": {
        "anchor_1": "Evaluation artefacts sit in version control, but at least one evaluation in the dated evaluation register lacks the manifest needed to rerun it (dataset version, environment, seed), so a third party could not reproduce it without help. Count evaluations in the register against complete manifests: any gap is level 1.",
        "anchor_2": "Every evaluation in the dated evaluation register has a manifest in version control naming the dataset version, the environment, the seed and the metric code, such that a third party can rerun it without asking the team.",
    },
    "MEA-2.4": {
        "anchor_3": "Level 2 evidence plus a dated report stating, per monitored system, detection precision, recall and alert-to-action time, reviewed by a named body at a stated cadence.",
        "anchor_4": "Level 3 evidence plus a dated change to alert thresholds or detection logic made from measured incident data, with the before-and-after alert-to-action time recorded and the change traceable to the report that motivated it.",
    },
    "MEA-4.3": {
        "anchor_1": "Drift monitoring detects changes, but at least one detected performance change in the period has no recorded root-cause analysis, or the analysis has no recorded corrective action. Count detected changes in the change log against root-cause and corrective-action records: any gap is level 1.",
        "anchor_2": "Every performance change detected in the period has a dated root-cause analysis and a recorded corrective action, and the change log ties each detected change to its analysis and its fix.",
        "anchor_3": "Level 2 evidence plus detection latency and change-to-action time recorded per change event against a stated target, reported to a named reviewing body on a stated cadence.",
    },
    "MEA-1.1": {
        "anchor_1": "Metrics exist for some risk categories only, or metrics are selected without a recorded definition and owner per metric. Count risk categories in the dated risk register against categories carrying a defined metric: any gap is level 1.",
        "anchor_2": "The dated measurement framework assigns at least one metric to every risk category in the risk register, each metric has a recorded definition, a named owner and a stated reporting cadence, and the metrics are wired to a live instrument (dashboard or pipeline) rather than described.",
        "anchor_3": "Level 2 evidence plus a dated coverage report stating the share of risk categories with an instrumented metric, reviewed by a named body.",
    },
    # ---- NA-vs-numeric splits ----------------------------------------------
    "MEA-2.2": {
        "anchor_0": "A study register exists and lists at least one human-subject evaluation run in the period, and none of those studies has ethics review or recorded consent. If the register shows no human-subject evaluation in the period, the control is not applicable: score NA, never 0.",
        "anchor_1": "At least one study in the period is registered, but a study lacks formal ethics review, recorded consent, a documented sampling rationale or a participant-protection record. Count the studies in the register against studies carrying all four: any study missing one is level 1.",
        "anchor_2": "Every study in the dated study register has a dated ethics approval, a signed consent record, a documented sampling rationale and participant-protection measures, with no gaps across the register.",
    },
    "GOV-3.2": {
        "anchor_0": "No representation data of any kind is collected for AI roles and no AI-specific hiring or team record exists, with the pack stating that absence.",
        "anchor_1": "Representation data is collected but not for AI roles specifically - an all-staff or 'technical roles' view only - or it is collected without a dated action plan. Either gap is level 1.",
        "anchor_2": "Representation in AI roles is monitored across every in-scope hiring and team record for a stated period, bias in AI hiring is assessed, and each finding carries a dated action plan with a named owner.",
    },
    # ---- 0<->1 split --------------------------------------------------------
    "GOV-5.2": {
        "anchor_0": "No research collaboration of any kind exists - no agreement, no publication, no individual engagement - and the pack states that absence.",
        "anchor_1": "Engagement is individual and undocumented - a researcher's personal contact with a university lab - with no agreement, no knowledge-exchange programme and no publication. Any one of those three missing keeps the level at 1.",
        "anchor_2": "Signed research partnership agreements with dated terms exist, at least one knowledge-exchange activity has occurred in the period, and publication support is documented.",
    },
}


def main() -> int:
    with BANK.open(newline="", encoding="utf-8") as fh:
        reader = csv.DictReader(fh)
        fields = reader.fieldnames
        rows = list(reader)

    seen = set()
    for row in rows:
        cid = row["control"]
        edits = EDITS.get(cid)
        if not edits:
            continue
        for field, value in edits.items():
            if field not in fields:
                raise SystemExit(f"unknown field {field} for {cid}")
            row[field] = value
        seen.add(cid)

    missing = set(EDITS) - seen
    if missing:
        raise SystemExit(f"controls not found in bank: {sorted(missing)}")

    with BANK.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=fields, quoting=csv.QUOTE_ALL, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)

    print(f"edited {len(seen)} controls; bank now {len(rows)} rows")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
