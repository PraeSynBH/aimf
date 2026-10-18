#!/usr/bin/env python3
"""Instrument change P8: make the level 1 <-> 2 boundary decisive.

The 2026-10-18 validation run (AIMF-VAL-2026-A, four independent sessions) put
41 of 49 non-unanimous controls on the 1<->2 edge. The diagnosis was not "the
assessors read differently", it was that anchor 1 and anchor 2 were written with
qualitative hedges ("applied unevenly", "partial", "comprehensive") that an
assessor can resolve either way for the same pack. Adding protocol definitions
(run 2) did not move the number, which is why this change edits the anchors.

The rule applied to every edited row, identically:

  anchor 1 = the artefact exists but fails at least one COUNTABLE test:
             a stated population not fully covered by the scope register, an
             unapproved/undated/overdue artefact, or a missing named element.
  anchor 2 = the same artefact passes every countable test: 100% of the
             population in the dated scope register, approved and current, no
             open exceptions.

Nothing outside anchor 1/2 changed. Controls not listed are untouched.
"""
import csv
import pathlib

BANK = pathlib.Path(__file__).resolve().parents[1] / "documents" / "AIMF-Full-Documentation" / "implementation" / "AIMF-ASSESSMENT-QUESTION-BANK.csv"

EDITS = {
    # control: (anchor_1, anchor_2)
    "GOV-1.1": (
        "A policy exists, but it misses at least one applicable regime, or is unapproved or past its review date, or applies to some business units in the scope register. Any one of the three makes the level partial.",
        "An approved, in-date AI compliance policy maps every applicable AI law, regulation and standard, covers every system in the dated scope register with no open exceptions, and is reviewed on a stated cycle.",
    ),
    "GOV-1.3": (
        "AI risk is named in the enterprise framework, but there is no approved AI-specific appetite statement or thresholds, or the thresholds cover only some categories in the AI risk register.",
        "Approved AI appetite statements and thresholds cover every risk category in the AI risk register, sit inside the enterprise risk framework, and named staff can describe the escalation path.",
    ),
    "GOV-2.3": (
        "An executive sponsor is named, but there is no chartered committee or standing agenda, or the committee meets without recorded AI risk decisions.",
        "A chartered executive committee receives AI risk reporting on a stated cadence, minutes show the decisions recorded, and coverage is the full in-scope portfolio.",
    ),
    "GOV-3.2": (
        "A non-discrimination policy exists, but representation data is not collected for AI roles, or is collected without a documented dated action plan.",
        "Representation in AI roles is monitored across every in-scope hiring and team record, hiring bias is assessed, and each finding carries a documented action plan with progress reviewed on cadence.",
    ),
    "MAN-4.3": (
        "An incident route exists, but the register is undated or covers some in-scope systems only, or incidents are recorded without stakeholder communication.",
        "An AI incident programme is in force: every in-scope system is in the register, each entry is dated with owner and status, and stakeholder communication and recovery documentation are defined.",
    ),
    "MAP-1.6": (
        "Technical requirements are gathered, but socio-technical requirements, recorded stakeholder input, or traceability into testing are missing for at least one in-scope system.",
        "Every in-scope system has requirements that include socio-technical implications and recorded stakeholder input, and each requirement carries a traceability link to test evidence.",
    ),
    "MAP-3.1": (
        "Benefits are listed in a proposal, but at least one in-scope system has no quantified baseline, or no stated method for validating the benefit afterwards.",
        "Every in-scope system has a documented benefits analysis with a quantified baseline and a stated validation method, approved before the investment decision.",
    ),
    "MAP-3.2": (
        "Direct costs are recorded, but non-monetary costs are excluded, or the analysis is not documented for every in-scope system.",
        "A total-cost analysis including non-monetary costs and an explicit link to the risk tolerance statement is documented for every system in the scope register.",
    ),
    "MAP-3.4": (
        "Proficiency expectations are stated for some operator roles, but they are neither assessed nor certified, or they do not cover every AI operator role in the register.",
        "Every operator role in the register has formal proficiency requirements, an assessment process with recorded results, and certification requirements.",
    ),
    "MEA-2.2": (
        "Ethical consideration is informal, or the sampling rationale and participant protections are undocumented for at least one study in the period.",
        "Every study in the period has formal ethics review, recorded informed consent, a documented sampling rationale and participant protections.",
    ),
    "MEA-2.6": (
        "A safety assessment exists for some in-scope systems, without fail-safe testing or a documented residual-risk entry.",
        "Every system in the scope register has a safety evaluation with fail-safe testing and a documented residual-risk entry.",
    ),
    "MEA-3.1": (
        "Ongoing risk monitoring exists, but the log has no named owner, or no dated emergent-risk entry for at least one in-scope system.",
        "Risk tracking covers every system in the scope register, with a named owner, a stated review cadence and dated entries for emergent risks.",
    ),
}


def main():
    with BANK.open(newline="", encoding="utf-8") as fh:
        reader = csv.DictReader(fh)
        fields = reader.fieldnames
        rows = list(reader)

    seen = set()
    for row in rows:
        cid = row["control"]
        if cid in EDITS:
            a1, a2 = EDITS[cid]
            row["anchor_1"] = a1
            row["anchor_2"] = a2
            seen.add(cid)

    missing = set(EDITS) - seen
    if missing:
        raise SystemExit(f"controls not found in bank: {sorted(missing)}")

    with BANK.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=fields, quoting=csv.QUOTE_ALL, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)

    print(f"edited {len(seen)} controls; bank now {len(rows)} rows")


if __name__ == "__main__":
    main()
