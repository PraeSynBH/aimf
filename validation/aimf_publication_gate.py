#!/usr/bin/env python3
"""Publication gate for the AIMF documentation bundle (PRA-6702).

The bundle is HELD: Ben's 2026-10-21 decision is `publish_after_iso27001`, so
nothing may be pushed to a remote or uploaded until the ISO/IEC 27001 mapping is
at clause-level fidelity against a licensed copy of the 2022 text.

`validation/verify_release.sh` answers "is the shipped zip internally sound".
This script answers the different question the hold actually turns on: "is the
repository allowed to be published today, and is every publication claim true
for the version that would ship". It is deliberately narrow and cheap.

    python3 validation/aimf_publication_gate.py            # human table
    python3 validation/aimf_publication_gate.py --json f   # machine record

Exit 0 = gate clear (publication permitted, subject to Ben's fresh
confirmation). Exit 1 = gate held. Each check names the release-cut action that
flips it, so the release is a command, not a memory exercise.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BUNDLE = ROOT / "documents" / "AIMF-Full-Documentation"
REGISTER = BUNDLE / "AIMF-MAPPING-COMPLETENESS.md"
CHANGELOG = BUNDLE / "CHANGELOG.md"
ISO27001 = BUNDLE / "mappings" / "AIMF-ISO27001-MAPPING.md"
CATALOG = BUNDLE / "core" / "AIMF-CONTROL-CATALOG.csv"
ZIPS = ROOT / "documents"

PASS, FAIL, WARN, INFO = "PASS", "FAIL", "WARN", "INFO"
results: list[dict] = []


def record(check: str, status: str, detail: str) -> None:
    results.append({"check": check, "status": status, "detail": detail})


def run(*args: str) -> tuple[int, str]:
    p = subprocess.run(args, cwd=ROOT, capture_output=True, text=True)
    return p.returncode, (p.stdout + p.stderr).strip()


def first(pattern: str, text: str, group: int = 1) -> str | None:
    m = re.search(pattern, text, re.MULTILINE)
    return m.group(group) if m else None


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def ship_version() -> str | None:
    """The version the CHANGELOG says is current, i.e. what would ship."""
    return first(r"^\*\*Version\*\*:\s*([0-9][0-9.]*)\s*$", CHANGELOG.read_text())


def latest_tag() -> tuple[str, str] | None:
    code, out = run("git", "tag", "--list", "aimf-v*", "--sort=-v:refname")
    if code != 0 or not out:
        return None
    tag = out.splitlines()[0]
    return tag, tag.replace("aimf-v", "", 1)


# --- G1: the hold has no external exposure, and no publication path exists -----
def check_hold_intact() -> None:
    code, out = run("git", "remote", "-v")
    if code != 0:
        record("G1 hold_intact", FAIL, f"git remote failed: {out}")
        return
    remotes = [ln for ln in out.splitlines() if ln.strip()]
    if remotes:
        record(
            "G1 hold_intact",
            FAIL,
            "a git remote exists, so a publication path now exists and the hold "
            "can be violated by a single push: " + "; ".join(remotes),
        )
        return
    code, out = run("git", "log", "--oneline", "-1")
    record("G1 hold_intact", PASS, f"no git remote configured; nothing published (HEAD {out.split()[0] if out else '?'})")


# --- G2: CHANGELOG version, shipped zip and tag all name the same version ------
def check_version_coherence() -> None:
    ver = ship_version()
    if not ver:
        record("G2 version_coherence", FAIL, "CHANGELOG carries no Version field")
        return
    problems: list[str] = []

    tagged = latest_tag()
    if not tagged:
        problems.append("no aimf-v* tag found")
    elif tagged[1] != ver:
        problems.append(f"latest tag is {tagged[0]} but CHANGELOG says {ver}")

    shipped = ZIPS / f"AIMF-Full-Documentation-v{ver}.zip"
    rollup = ZIPS / "AIMF-Full-Documentation.zip"
    if not shipped.is_file():
        problems.append(f"no shipped zip documents/AIMF-Full-Documentation-v{ver}.zip")
    if not rollup.is_file():
        problems.append("no rollup documents/AIMF-Full-Documentation.zip")
    if shipped.is_file() and rollup.is_file():
        a, b = sha256(shipped), sha256(rollup)
        if a != b:
            problems.append(f"rollup zip is not the v{ver} zip (rollup {b[:12]} vs shipped {a[:12]})")

    if problems:
        record("G2 version_coherence", FAIL, "; ".join(problems))
    else:
        record("G2 version_coherence", PASS, f"tag aimf-v{ver} == CHANGELOG == shipped zip, rollup identical")


# --- G3: the register of record attests to the version that would ship ---------
def check_register_attestation() -> None:
    text = REGISTER.read_text()
    ver = ship_version()
    docver = first(r"^\*\*Version\*\*:\s*([0-9][0-9.]*)\s*$", text)
    attested = first(r"against repository state at commit\s*`([0-9a-f]+)`\s*\(v([0-9][0-9.]*)\)", text, 2)
    date = first(r"\*\*Status\*\*:\s*Verified\s+(\d{4}-\d{2}-\d{2})", text)

    if attested is None:
        record("G3 register_attestation", FAIL, "register states no verified repository state")
        return
    if attested != ver:
        record(
            "G3 register_attestation",
            FAIL,
            f"register (doc v{docver}) attests the repository at v{attested} verified "
            f"{date}, but the line ships {ver}: it is the register of publication "
            f"claims, so it must be re-verified and re-attested for {ver} at the "
            f"release cut (PRA-6356 R5.1)",
        )
        return
    record("G3 register_attestation", PASS, f"register re-attested for v{ver} ({date})")


# --- G4: the ISO 27001 mapping's claim is true, and it meets the gate condition -
def check_iso27001_claim() -> None:
    text = ISO27001.read_text()
    status = first(r"^\*\*Status\*\*:\s*(\w+)", text)
    coverage = re.search(r"(\d+) of (\d+) AIMF controls carry", text)
    no_analogue = first(r"(\d+) were reviewed", text)

    if status is None or coverage is None or no_analogue is None:
        record("G4 iso27001_claim", FAIL, "cannot parse Status / coverage figures from the mapping")
        return

    n_tagged, n_total = (int(g) for g in coverage.groups())
    n_none = int(no_analogue)

    # Catalogue truth, not the prose's own arithmetic.
    rows = list(__import__("csv").DictReader(CATALOG.open(newline="")))
    blank = [r["Control_ID"] for r in rows if not r["ISO27001_Controls"].strip()]
    cat_tagged = sum(1 for r in rows if r["ISO27001_Controls"].strip() not in ("", "—", "-"))
    cat_total = len(rows)

    problems: list[str] = []
    if n_tagged + n_none != n_total:
        problems.append(f"mapping arithmetic {n_tagged}+{n_none} != {n_total}")
    if (n_tagged, n_total) != (cat_tagged, cat_total):
        problems.append(f"mapping says {n_tagged}/{n_total}, catalogue holds {cat_tagged}/{cat_total}")
    if blank:
        problems.append(f"{len(blank)} catalogue rows carry a blank ISO27001_Controls cell")
    if status.lower().startswith("complete") and "licensed copy" in text:
        problems.append("status says Complete while the scope limitation still disclaims licensed-source depth")

    # The gate condition itself. Ben's decision `publish_after_iso27001` (2026-10-21)
    # holds publication until this mapping reaches clause-level fidelity, so a
    # mapping that is still Partial fails the gate even when every claim in it is
    # internally true. Passing this check on claim-integrity alone reported CLEAR
    # once, on 2026-10-22, against a Partial mapping - that is the bug this fixes.
    if not status.lower().startswith("complete"):
        problems.append(
            f"gate condition unmet: Ben's publish_after_iso27001 requires clause-level "
            f"fidelity, mapping status is {status}"
        )
    if problems:
        record("G4 iso27001_gate", FAIL, "; ".join(problems))
        return
    record(
        "G4 iso27001_gate",
        PASS,
        f"status {status}: {cat_tagged}/{cat_total} tagged, {cat_total - cat_tagged} no-analogue, "
        f"arithmetic and catalogue agree; claim does not exceed the text",
    )


# --- G5: generated tables still match the catalogue ----------------------------
def check_generator() -> None:
    code, out = run("python3", "scripts/aimf_mappings.py", "check")
    status = PASS if code == 0 else FAIL
    record("G5 mapping_check", status, out.splitlines()[-1] if out else f"exit {code}")


# --- G6: the licensed standard text cannot be committed by accident ------------
def check_licensed_text() -> None:
    code, tracked = run("git", "ls-files", "storage/")
    if code != 0:
        record("G6 licensed_text_hygiene", FAIL, f"git ls-files failed: {tracked}")
        return
    files = [f for f in tracked.splitlines() if f.strip()]
    leaked = [f for f in files if re.search(r"2700[12]", f)]
    if leaked:
        record(
            "G6 licensed_text_hygiene",
            FAIL,
            "licensed ISO/IEC 27001/27002 text is tracked by git: "
            + ", ".join(leaked)
            + " - untrack it before any publication path exists (the licence forbids redistribution)",
        )
        return
    if files:
        record(
            "G6 licensed_text_hygiene",
            WARN,
            f"{len(files)} storage/ file(s) are tracked by git ({', '.join(files)}); they are "
            "excluded from the bundle but a future push would publish them. Delivery instruction "
            "for the 27001 text: leave it untracked",
        )
        return
    record("G6 licensed_text_hygiene", PASS, "no licensed standard text tracked by git")


# --- G7: the shipped artifact carries no licensed standard documents -----------
def check_bundle_clean() -> None:
    ver = ship_version()
    shipped = ZIPS / f"AIMF-Full-Documentation-v{ver}.zip" if ver else None
    if not shipped or not shipped.is_file():
        record("G7 bundle_clean", FAIL, "no shipped zip to inspect")
        return
    with zipfile.ZipFile(shipped) as zf:
        names = zf.namelist()
    bad = [
        n
        for n in names
        if "storage/" in n
        or re.search(r"ISO_IEC_27001|ISO_IEC_27002|ISO_IEC_42001", n, re.IGNORECASE)
        or n.lower().endswith((".pdf", ".epub"))
    ]
    if bad:
        record("G7 bundle_clean", FAIL, "shipped zip contains licensed source material: " + ", ".join(bad[:5]))
        return
    record("G7 bundle_clean", PASS, f"{len(names)} entries, none from storage/ and no standard PDFs/EPUBs")


# --- G8: the source delivered for the mapping is the standard, not a proxy ------
def check_source_text() -> None:
    """A file called *27001* in storage/ is not the same thing as the standard.

    Ben delivers the licensed text by dropping it in storage/, so the gate has to
    assert what the file actually is before mapping work is dispatched against it.
    A derived control library carries Annex A cross-references in its prose but no
    Annex A control identifiers of its own and no clauses 4-10, so clause-level
    fidelity cannot be built from it.
    """
    storage = ROOT / "storage"
    candidates = sorted(p for p in storage.glob("*") if "27001" in p.name) if storage.is_dir() else []
    if not candidates:
        record("G8 source_text", INFO, "no ISO/IEC 27001 source delivered yet")
        return

    import csv as _csv

    verdicts: list[str] = []
    ok = False
    for path in candidates:
        if path.suffix.lower() not in (".csv", ".txt"):
            verdicts.append(f"{path.name}: binary/other format, not inspected")
            continue
        rows = list(_csv.DictReader(path.open(encoding="utf-8-sig", errors="replace")))
        codes = [next((v for v in r.values() if v), "") for r in rows]
        annex = sum(1 for c in codes if re.fullmatch(r"A\.\d+\.\d+", (c or "").strip()))
        clause = sum(1 for c in codes if re.match(r"^(?:[4-9]|10)(?:\.\d+)*$", (c or "").strip()))
        shape = re.sub(r"\d+", "#", (codes[0] or "").strip()) if codes else "?"
        if annex >= 50 or clause >= 4:
            ok = True
            verdicts.append(f"{path.name}: {len(rows)} rows, {annex} Annex A codes / {clause} clause ids")
        else:
            verdicts.append(
                f"{path.name}: {len(rows)} rows but 0 Annex A control codes and 0 clause 4-10 ids "
                f"(rows are coded like {shape!r}) - a derived control library, not the standard"
            )

    if ok:
        record("G8 source_text", PASS, "; ".join(verdicts))
    else:
        record(
            "G8 source_text",
            FAIL,
            "no delivered source is ISO/IEC 27001:2022 itself: " + "; ".join(verdicts),
        )


CHECKS = (
    check_hold_intact,
    check_version_coherence,
    check_register_attestation,
    check_iso27001_claim,
    check_generator,
    check_licensed_text,
    check_bundle_clean,
    check_source_text,
)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--json", metavar="PATH", help="write the machine-readable record here")
    args = ap.parse_args()

    for check in CHECKS:
        try:
            check()
        except Exception as exc:  # a broken check must not read as a green gate
            record(check.__name__, FAIL, f"check raised {type(exc).__name__}: {exc}")

    failures = [r for r in results if r["status"] == FAIL]
    warnings = [r for r in results if r["status"] == WARN]

    width = max(len(r["check"]) for r in results)
    for r in results:
        print(f"{r['check']:<{width}}  {r['status']:<4}  {r['detail']}")

    verdict = "HELD" if failures else "CLEAR"
    print()
    print(f"GATE: {verdict} - {len(results)} checks, {len(failures)} fail, {len(warnings)} warn")
    if failures:
        print("A CLEAR gate authorises the release cut only; Ben's fresh publication")
        print("confirmation is still required before anything leaves this machine.")

    if args.json:
        Path(args.json).write_text(
            json.dumps(
                {
                    "issue": "PRA-6702",
                    "shipping_version": ship_version(),
                    "gate": verdict,
                    "checks": results,
                    "head": run("git", "log", "--oneline", "-1")[1],
                },
                indent=2,
            )
            + "\n"
        )
        print(f"record: {args.json}")

    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
