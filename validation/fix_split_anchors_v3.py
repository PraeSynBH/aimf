#!/usr/bin/env python3
"""Instrument change P8, third pass (A3b): close the nine splits that survived v1.0.8.

Run 5 (the 21-control rewrite, bank sha 872d4b7a...) measured 63/72 (87.5%) — three
controls short of the 90% threshold in P6. The nine remaining disagreements are not
random; each has a named cause in the anchors themselves:

  clause blending   MEA-2.1, MEA-1.2, MAN-4.2
      anchor 2 required a level-3 measure ("could a third party rerun it", "measured
      effect per release", "revision history") so one reader scored 1 where the other
      scored 2. The level-2 clause is now the manifest/record itself and the anchor
      says which measure belongs to level 3.

  unreachable-rung  MEA-2.4, MEA-4.3
      one reader scored level 4 (resp. 3) from a top-rung artefact while the rung
      below was unevidenced, which the ladder forbids. The level-3/4 anchors now
      state in words that the higher rung is unreachable without the lower one.

  population stated MAP-2.2, MEA-2.6
      anchor 2 said "every system" in one control and not in the other; the countable
      population (dated scope register) is now named in both anchors of both controls.

  assertion vs minute  MAP-1.3
      "reviewed annually" was read as satisfying an anchor that requires a minuted
      review. Anchor 1 now says an asserted cadence without minutes is level 1.

  absence boundary  GOV-5.2
      level 0 said "no collaboration of any kind" while the pack contains informal
      individual contact, which is exactly what level 1 describes. Level 0 now
      excludes informal contact explicitly.

No protocol text (P1-P6) is touched. Only these nine rows change.
"""
import csv
import pathlib

BANK = pathlib.Path(__file__).resolve().parents[1] / "documents" / "AIMF-Full-Documentation" / "implementation" / "AIMF-ASSESSMENT-QUESTION-BANK.csv"

EDITS = {
    # ---- clause blending ----------------------------------------------------
    "MEA-2.1": {
        "anchor_2": "Every evaluation in the dated evaluation register has a manifest in version control naming the dataset version, the environment, the seed and the metric code. Whether a third party could rerun it without help is measured at level 3 and is not required here.",
    },
    "MEA-1.2": {
        "anchor_1": "A metric definitions document exists, but fewer than all metrics in the dated metric register carry a recorded validation of what the metric can and cannot show. Count metrics in the register against entries carrying a validation record: any gap is level 1.",
        "anchor_2": "Every metric in the dated metric register carries a validation record stating the claim it measures and its documented limits - the study or manual-sample comparison that tested it. The false-positive and false-negative analysis and the revision history are level-3 artefacts and are not required here.",
    },
    "MAN-4.2": {
        "anchor_1": "An improvement backlog linked to monitoring findings exists, but at least one release in the dated release log does not cite the finding that triggered it, or a backlog item that changed a release has no recorded disposition. Count releases in the log that cite a finding against all releases in the log: any gap is level 1.",
        "anchor_2": "Every release in the dated release log cites the monitoring or user finding that triggered it, and the backlog records, for each finding, whether it is open or closed. The measured effect of each release is a level-3 requirement and is not part of this level.",
    },
    # ---- unreachable rung ---------------------------------------------------
    "MEA-2.4": {
        "anchor_2": "Production monitoring tracks component behaviour and detects anomalies for every system in the dated scope register.",
        "anchor_3": "Level 2 evidence plus a dated report stating, per monitored system, detection precision, recall and alert-to-action time, reviewed by a named body at a stated cadence. A dashboard or an alert configuration alone is not this level.",
        "anchor_4": "Level 3 evidence plus a dated change to alert thresholds or detection logic made from measured incident data, with the before-and-after alert-to-action time recorded and the change traceable to the report that motivated it. This level is unreachable unless the level-3 dated report and its named review exist.",
    },
    "MEA-4.3": {
        "anchor_2": "Every performance change recorded in the dated change log has a dated root-cause analysis and a recorded corrective action, and the log ties each detected change to its analysis and its fix.",
        "anchor_3": "Level 2 evidence plus detection latency and change-to-action time recorded per change event against a stated target, reported to a named reviewing body on a stated cadence. A measured median with no stated target and no named reviewing body is not this level.",
        "anchor_4": "Level 3 evidence plus predictive performance modelling that pre-empted a decline, used in release decisions. This level is unreachable unless the level-3 stated target and named reviewing body exist.",
    },
    # ---- population stated --------------------------------------------------
    "MAP-2.2": {
        "anchor_1": "Limits and oversight are documented for some systems only - the count of systems carrying a limits note is smaller than the count in the dated scope register - or the oversight rule is not shown enforced in configuration for at least one system in scope. Any gap is level 1.",
        "anchor_2": "For every system in the dated scope register: knowledge limits, out-of-scope behaviour and the human oversight requirement are documented, and the oversight rule is shown enforced in a dated configuration export covering that system.",
    },
    "MEA-2.6": {
        "anchor_1": "A safety evaluation with fail-safe testing exists, but the number of systems carrying a safety evaluation is smaller than the number of systems in the dated scope register, or a residual-risk entry has no named acceptance. Count evaluated systems against the scope register, and residual-risk entries against entries carrying an accepting role and a date: any shortfall is level 1.",
        "anchor_2": "The count of systems carrying a safety evaluation that includes fail-safe testing equals the count of systems in the dated scope register, and every residual safety risk carries a named acceptance with the accepting role and the date.",
    },
    # ---- assertion vs minute ------------------------------------------------
    "MAP-1.3": {
        "anchor_1": "A dated, approved AI strategy tied to the mission exists, but the review register shows no minuted review in the last 12 months - a strategy that asserts an annual review cadence without minutes is level 1, not level 2 - or the review held did not test each strategic theme against the mission statement. Count minuted reviews held in the last 12 months: zero is level 1.",
        "anchor_2": "The approved AI strategy is dated, ties each strategic theme to the mission statement, and at least one minuted review held in the last 12 months records the date, the attendees and the mission test applied to each theme. An asserted cadence without minutes does not satisfy this level.",
    },
    # ---- absence boundary ---------------------------------------------------
    "GOV-5.2": {
        "anchor_0": "No academic contact of any kind exists: no signed agreement, no publication, and no named researcher with a dated record of external university correspondence in the pack, and the pack states that absence. Informal individual contact is not level 0 - it is level 1.",
    },
}


def main() -> int:
    with BANK.open(newline="", encoding="utf-8") as fh:
        reader = csv.DictReader(fh)
        fields = reader.fieldnames
        rows = list(reader)

    by_id = {r["control"]: r for r in rows}
    seen = set()
    for cid, edits in EDITS.items():
        row = by_id.get(cid)
        if row is None:
            raise SystemExit(f"control not found in bank: {cid}")
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
