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
if [ -f implementation/AIMF-INSTRUMENT-VALIDATION.md ]; then
  grep -m1 -E '^\*\*Current result' implementation/AIMF-INSTRUMENT-VALIDATION.md || echo "MISSING headline result"
else
  echo "MISSING record"
fi
printf 'P7 measured line: '
grep -m1 -E '^\*\*Agreement: [0-9]+ of 72 controls' implementation/AIMF-ASSESSMENT-GUIDE.md || echo "MISSING"
printf 'anchor set sha (in zip): '
python3 - <<'PY'
import hashlib
print(hashlib.sha256(open('implementation/AIMF-ASSESSMENT-QUESTION-BANK.csv','rb').read()).hexdigest())
PY

echo
echo "OK: in-zip verification complete"
