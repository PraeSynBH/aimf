#!/usr/bin/env bash
# P8 release gate: verify the SHIPPED zip, not the working tree.
#
#   clean committed tree -> build both zips -> unpack one -> run the counts and
#   `check` from inside the zip -> then tag.
#
# Usage: bash validation/verify_release.sh documents/AIMF-Full-Documentation-v1.0.6.zip
set -euo pipefail

zip_path="${1:?usage: verify_release.sh <zip>}"
zip_path="$(cd "$(dirname "$zip_path")" && pwd)/$(basename "$zip_path")"
work="$(mktemp -d "${TMPDIR:-/tmp}/aimf-zipcheck.XXXXXX")"
trap 'rm -rf "$work"' EXIT

echo "== zip"
ls -l "$zip_path" | awk '{print $5" bytes  "$9}'
shasum -a 256 "$zip_path" | awk '{print "sha256 "$1}'
unzip -l "$zip_path" | tail -1

unzip -q "$zip_path" -d "$work"
root="$work/AIMF-Full-Documentation"
[ -d "$root" ] || { echo "FAIL: zip root AIMF-Full-Documentation/ missing"; exit 1; }
cd "$root"

echo
echo "== validator (from inside the unpacked zip)"
python3 scripts/aimf_mappings.py check
python3 scripts/aimf_question_bank.py check

echo
echo "== report"
python3 scripts/aimf_mappings.py report

echo
echo "== anchors"
printf 'guide anchor mentions: '; grep -cniE 'anchor' implementation/AIMF-ASSESSMENT-GUIDE.md || true
printf 'bank anchor rows (72 expected): '; grep -cE '^\| (GOV|MAP|MEA|MAN)-[0-9]+\.[0-9]+ \|' implementation/AIMF-ASSESSMENT-QUESTION-BANK.md
printf 'bank anchor cells (360 expected): '; python3 - <<'PY'
import csv
rows = list(csv.DictReader(open('implementation/AIMF-ASSESSMENT-QUESTION-BANK.csv')))
cells = [r[f'anchor_{i}'].strip() for r in rows for i in range(5)]
print(f"{len(cells)} cells, {sum(1 for c in cells if c)} non-empty, {len(set(cells))} distinct")
PY

echo
echo "== scoring protocol"
for needle in "### Scoring Protocol" "#### P3. Not assessable" "#### P4. Blind double scoring" "#### P5. Adjudication" "insufficient evidence"; do
  n=$(grep -cF "$needle" implementation/AIMF-ASSESSMENT-GUIDE.md || true)
  printf '%-34s %s\n' "$needle" "$n"
done

echo
echo "== validation record"
python3 - <<'PY'
import re, sys

record = open('implementation/AIMF-INSTRUMENT-VALIDATION.md').read()
guide = open('implementation/AIMF-ASSESSMENT-GUIDE.md').read()

pat = re.compile(r'(\d{1,2})/72 controls agreed \(([\d.]+)%\)|(\d{1,2}) of 72 controls \(([\d.]+)%\)')
def first(text):
    m = pat.search(text)
    if not m:
        return None
    n = m.group(1) or m.group(3)
    pct = m.group(2) or m.group(4)
    return int(n), float(pct)

r, g = first(record), first(guide)
print(f"validation record headline: {r}")
print(f"guide P7 measured line:     {g}")
if r is None:
    sys.exit("FAIL: validation record states no measured result")
if g is None:
    sys.exit("FAIL: the Assessment Guide has no P7 measured result")
if r != g:
    sys.exit(f"FAIL: record says {r}, guide says {g} - the artifact contradicts itself")

# P6: below 90% the guide must carry the not-validated sentence; at or above 90% it must
# carry the validated one. Both directions are gated so the sentence cannot be dropped
# without a measured number that earns it.
if r[1] >= 90.0:
    if 'not validated' in guide:
        sys.exit("FAIL: guide is at or above the P6 threshold but still says not validated")
    if 'validated for reproducibility' not in guide:
        sys.exit("FAIL: guide clears the threshold without stating that it is validated")
    state = "validated for reproducibility"
else:
    if 'not validated' not in guide:
        sys.exit("FAIL: guide is below the P6 threshold without the not-validated sentence")
    state = "not validated"
print(f"OK: both documents state {r[0]}/72 ({r[1]}%) and the guide says {state}")
PY
printf 'anchor set sha (in zip): '
python3 - <<'PY'
import hashlib
print(hashlib.sha256(open('implementation/AIMF-ASSESSMENT-QUESTION-BANK.csv','rb').read()).hexdigest())
PY

echo
echo "OK: in-zip verification complete"
