# AI Management Framework (AIMF) by PraeSyn
## Standards Mapping Completeness Register

**© 2026 PraeSyn, LLC. All rights reserved.**
Licensed under CC BY-NC-ND 4.0

**Version**: 1.0.12
**Document Type**: Verification Register
**Status**: Verified 2026-10-17 against repository state at commit `e46481d` (v1.0.1)
**Supersedes**: the standards-mapping completeness claims previously carried by
README.md, QA-VERIFICATION-REPORT.md and QUALITY-ASSURANCE-CHECKLIST.md

---

## Why this document exists

The v1.0 baseline stated, in several places, that specific standards mappings were
complete. A review on 2026-10-17 found that some of those statements were not supported
by the content of the files they pointed at. In an asset that is sold on standards
alignment, an unsupported completeness claim is a credibility defect, so this register
records, for every mapping artifact, (a) what the file actually contains and (b) the
command used to check it.

Every claim in this register is reproducible with the commands in
[Evidence commands](#evidence-commands). Where a mapping is incomplete, it is marked
incomplete. No status here exceeds the file content.

**Revision note (v1.0.1).** The first issue of this register verified the v1.0 baseline
(`78d9089`), at which point four dedicated mapping documents were still research
skeletons. Release v1.0.1 (`f76f757`) completed those four documents and normalised the
control catalog. This revision re-verifies every row against the v1.0.1 tree and is the
register of record. The status of each file below is taken from its own content and
matches that file's `**Status**` header.

**Revision note (v1.0.12).** The v1.0.1 issue of this register was the register of record
for ten releases without being re-attested: it described the tree at `e46481d` while the line
shipped 1.0.11. This revision re-runs every evidence command below against the v1.0.12 tree and
re-attests the register to the version that ships. The substantive change since v1.0.1 is one
attribution decision: D2 (Data Governance & Management) now carries **4 primary + 3 secondary**
controls instead of 2, restored as an **authorised framework change** on 2026-10-21 (Ben; decision
record `aimf-publication-decisions-20261021` on PRA-6356 §R1 row 3), not as a correction of a data
defect. Every standards-mapping claim in this register — NIST 72/72, ISO 42001 19 clauses, ISO 27001
54 tagged + 18 reviewed-no-analogue, EO 14179 23 controls — is unchanged by that edit and is
re-evidenced here. Nothing in this register treats the D2 attribution as derived from a count: it is
a framework decision and the dimension mapping says so in its own words.

---

## Correction of the headline figure

The v1.0 documentation claimed **"59"** NIST AI RMF subcategories.

The authoritative count in **NIST AI 100-1 (AI RMF 1.0)** is **72 subcategories**
across 19 categories:

| Function | Categories | Subcategories |
|----------|-----------:|--------------:|
| GOVERN   | 6          | 19            |
| MAP      | 5          | 18            |
| MEASURE  | 4          | 22            |
| MANAGE   | 4          | 13            |
| **Total**| **19**     | **72**        |

Both the total ("59") and the earlier per-function split published in
`mappings/MANAGE-FUNCTION-MATURITY-MAPPING.md` (GOVERN 18 / MAP 14 / MEASURE 17 /
MANAGE 10) were wrong. The framework's coverage is now **72/72** in the catalog, in the
four function maturity mappings and in the dedicated NIST mapping, and the figure
carried in the documentation has been corrected to match.

---

## Mapping completeness

Status is taken from each file's real content, not from its header. "Evidence" refers to
the numbered commands in [Evidence commands](#evidence-commands); each command was run on
2026-10-17 against commit `e46481d` and its output is quoted.

| File | Standard | Status taken from content | Evidence |
|------|----------|---------------------------|----------|
| `core/AIMF-CONTROL-CATALOG.csv` | NIST AI RMF 1.0 | **Complete** — `NIST_RMF_Subcategory` populated for all 72 controls; GOVERN 19 / MAP 18 / MEASURE 22 / MANAGE 13 = 72 distinct subcategory IDs | E1, E2 |
| `core/AIMF-CONTROL-CATALOG.csv` | ISO/IEC 42001:2023 | **Complete** — `ISO42001_Clauses` non-empty for 72/72 controls; 19 distinct clause references | E4 |
| `core/AIMF-CONTROL-CATALOG.csv` | ISO/IEC 27001:2022 | **Partial** — 54/72 controls carry a 2022 Annex A reference; 18 reviewed as having no ISMS analogue (`—`); 0 retired 2013-edition IDs remain | E5 |
| `mappings/AIMF-NIST-RMF-MAPPING.md` | NIST AI RMF 1.0 | **Complete detailed mapping** — 72 subcategory IDs, each attributed to an AIMF control; 72 AIMF control IDs; 0 "Required Research" markers | E6, E7, E8 |
| `mappings/AIMF-ISO42001-MAPPING.md` | ISO/IEC 42001:2023 | **Complete detailed mapping** — all 19 catalog-attributed clause references mapped; 72 AIMF control IDs; 0 "Required Research" markers | E4, E6, E8 |
| `mappings/AIMF-ISO27001-MAPPING.md` | ISO/IEC 27001:2022 | **Partial** — mapped at public Annex A control-theme level; 72 AIMF control IDs; 54 controls carry a 2022 Annex A reference and 18 are recorded as no-analogue findings. Deep Annex A fidelity is **not** claimed | E5, E6, E8 |
| `mappings/AIMF-EXECUTIVE-ORDER-14179-MAPPING.md` | EO 14179 | **Complete detailed mapping** — every provision and each of the three follow-on federal actions mapped; 23 AIMF control IDs; 0 "Required Research" markers | E6, E8 |
| `mappings/AIMF-EXECUTIVE-ORDER-14110-MAPPING.md` | EO 14110 | **Complete detailed mapping** — but note the order was **rescinded 2025-01-20** by EO 14179; retained for historical traceability only | header |
| `mappings/AIMF-DIMENSION-MAPPING.md` | Internal (4 dimensions) | **Complete** — dimension attribution regenerated from the catalog for all 72 controls; D2 carries 4 primary + 3 secondary under the 2026-10-21 authorised framework change (Ben), recorded as a framework decision rather than a derived count; 72 AIMF control IDs | E6, E8 |
| `mappings/GOVERN-FUNCTION-MATURITY-MAPPING.md` | NIST GOVERN + ISO 42001 | **Complete detailed mapping** — all 19 GOVERN subcategory IDs present | E8 |
| `mappings/MAP-FUNCTION-MATURITY-MAPPING.md` | NIST MAP + ISO 42001 | **Complete detailed mapping** — all 18 MAP subcategory IDs present | E8 |
| `mappings/MEASURE-FUNCTION-MATURITY-MAPPING.md` | NIST MEASURE + ISO 42001 | **Complete detailed mapping** — all 22 MEASURE subcategory IDs present | E8 |
| `mappings/MANAGE-FUNCTION-MATURITY-MAPPING.md` | NIST MANAGE + ISO 42001 | **Complete detailed mapping** — all 13 MANAGE subcategory IDs present | E8 |

### What this means for the NIST claim

NIST AI RMF 1.0 subcategory coverage **is** complete (72/72), and it is now evidenced in
**three** independent places that agree exactly:

1. `core/AIMF-CONTROL-CATALOG.csv` — every control carries its NIST subcategory ID, and
   the union of those IDs is the complete NIST set (GOVERN 19, MAP 18, MEASURE 22,
   MANAGE 13).
2. The four `*-FUNCTION-MATURITY-MAPPING.md` files — 19 + 18 + 22 + 13 = 72.
3. `mappings/AIMF-NIST-RMF-MAPPING.md` — 72 subcategory IDs, each attributed to an AIMF
   control.

At the v1.0 baseline only (1) and (2) held, and the published README pointed at the one
file that did **not** hold the mapping. As of v1.0.1 all three hold, and the claims name
the files that actually carry the mapping.

### Remaining partial / disclosed items

Only one mapping is short of complete, and it is disclosed rather than asserted:

- **ISO/IEC 27001:2022** — `mappings/AIMF-ISO27001-MAPPING.md` is mapped at the level of
  the public Annex A control themes. 18 of the 72 controls were reviewed and recorded as
  having no ISMS analogue. Clause-level depth beyond the public theme titles is not
  claimed, pending a licensed copy of the 2022 edition.

---

## Evidence commands

Run from `documents/AIMF-Full-Documentation/`. Outputs below are verbatim from
the v1.0.12 re-verification on 2026-10-21; the figures they print are unchanged from
the 2026-10-17 run at commit `e46481d` except where a row says otherwise.

**E1 — distinct NIST subcategories covered in the catalog, total and per function**
```
$ grep -oE '(GOVERN|MAP|MEASURE|MANAGE) ?[0-9]+\.[0-9]+' core/AIMF-CONTROL-CATALOG.csv | sort -u | wc -l
72
$ for fn in GOVERN MAP MEASURE MANAGE; do
    printf "%s: " "$fn"
    grep -oE "$fn ?[0-9]+\.[0-9]+" core/AIMF-CONTROL-CATALOG.csv | sort -u | wc -l
  done
GOVERN: 19
MAP: 18
MEASURE: 22
MANAGE: 13
```

**E2 — catalog row count**
```
$ python3 -c "import csv;print(len(list(csv.DictReader(open('core/AIMF-CONTROL-CATALOG.csv')))))"
72
```

**E3 — the catalog is machine-validated against the mapping documents**
```
$ python3 scripts/aimf_mappings.py check
OK: mapping documents, catalog and generated tables are consistent
```

**E4 — controls carrying an ISO 42001 clause reference, and distinct clause count**
```
$ python3 -c "import csv;r=list(csv.DictReader(open('core/AIMF-CONTROL-CATALOG.csv')));print(sum(1 for x in r if x['ISO42001_Clauses'].strip()))"
72
$ python3 - <<'PY'
import csv,re
r=list(csv.DictReader(open('core/AIMF-CONTROL-CATALOG.csv')))
cl=set()
for x in r:
    cl |= set(re.findall(r'\d+(?:\.\d+)+', x['ISO42001_Clauses']))
print(len(cl))
PY
19
```

**E5 — ISO 27001 attribution: how many carry a 2022 Annex A id, and 2013-vintage check**
```
$ python3 -c "import csv;r=list(csv.DictReader(open('core/AIMF-CONTROL-CATALOG.csv')));print(sum(1 for x in r if x['ISO27001_Controls'].strip()))"
72
$ python3 - <<'PY'
import csv,re
r=list(csv.DictReader(open('core/AIMF-CONTROL-CATALOG.csv')))
real=sum(1 for x in r if re.search(r'A\.\d+\.\d+', x['ISO27001_Controls']))
print("carry A.x.y reference:", real, " no-analogue:", len(r)-real)
PY
carry A.x.y reference: 54  no-analogue: 18
$ grep -oE 'A\.(9|18)\.[0-9]+' core/AIMF-CONTROL-CATALOG.csv | sort -u | wc -l
0
```

**E6 — AIMF control IDs inside each dedicated mapping document**
```
$ for f in mappings/AIMF-NIST-RMF-MAPPING.md mappings/AIMF-ISO42001-MAPPING.md \
           mappings/AIMF-ISO27001-MAPPING.md mappings/AIMF-EXECUTIVE-ORDER-14179-MAPPING.md \
           mappings/AIMF-DIMENSION-MAPPING.md; do
    echo -n "$f: "; grep -oE '\b(GOV|MAP|MEA|MAN)-[0-9]+\.[0-9]+' "$f" | sort -u | wc -l; done
mappings/AIMF-NIST-RMF-MAPPING.md: 72
mappings/AIMF-ISO42001-MAPPING.md: 72
mappings/AIMF-ISO27001-MAPPING.md: 72
mappings/AIMF-EXECUTIVE-ORDER-14179-MAPPING.md: 23
mappings/AIMF-DIMENSION-MAPPING.md: 72
```

**E7 — the three claimed sources of NIST coverage agree exactly**
```
$ python3 - <<'PY'
import re,glob,csv
def s(t): return {f"{a} {b}" for a,b in re.findall(r'\b(GOVERN|MAP|MEASURE|MANAGE)\s*(\d+\.\d+)', t)}
cat=set()
for r in csv.DictReader(open('core/AIMF-CONTROL-CATALOG.csv')):
    cat |= s(r['NIST_RMF_Subcategory'])
fn=set()
for f in glob.glob('mappings/*-FUNCTION-MATURITY-MAPPING.md'):
    fn |= s(open(f).read())
nist=s(open('mappings/AIMF-NIST-RMF-MAPPING.md').read())
print("catalog:",len(cat)," union(function mappings):",len(fn)," dedicated NIST doc:",len(nist))
print("catalog==function-union:",cat==fn," catalog==nist-doc:",cat==nist)
print("missing from function union:",sorted(cat-fn)," extra:",sorted(fn-cat))
PY
catalog: 72  union(function mappings): 72  dedicated NIST doc: 72
catalog==function-union: True  catalog==nist-doc: True
missing from function union: []  extra: []
```

**E8 — "Required Research" markers and `**Status**` header per mapping file**
```
$ for f in mappings/*.md; do
    printf "%-55s research=%s  %s\n" "$f" "$(grep -c 'Required Research' "$f")" \
      "$(grep -m1 -E '^\*\*Status\*\*' "$f")"; done
mappings/AIMF-DIMENSION-MAPPING.md                       research=0  **Status**: Complete - dimension attribution for all 72 controls regenerated from the catalog, with D2's composition set by an authorised framework change (Ben, 2026-10-21) recorded below
mappings/AIMF-EXECUTIVE-ORDER-14110-MAPPING.md           research=0  **Status**: Complete detailed mapping
mappings/AIMF-EXECUTIVE-ORDER-14179-MAPPING.md           research=0  **Status**: Complete - every EO 14179 provision and each of its three follow-on federal actions is mapped to the AIMF controls that support readiness
mappings/AIMF-ISO27001-MAPPING.md                        research=0  **Status**: Partial - mapped at public Annex A control-theme level; 54 of 72 AIMF controls carry an ISO/IEC 27001:2022 Annex A reference and 18 were reviewed as having no ISMS analogue
mappings/AIMF-ISO42001-MAPPING.md                        research=0  **Status**: Complete - all 19 clause references the AIMF catalog attributes to ISO/IEC 42001:2023 are mapped
mappings/AIMF-NIST-RMF-MAPPING.md                        research=0  **Status**: Complete - all 72 subcategories of NIST AI RMF 1.0 carry an AIMF control attribution
mappings/GOVERN-FUNCTION-MATURITY-MAPPING.md             research=0  **Status**: Complete detailed mapping - all 19 NIST AI RMF GOVERN subcategories mapped
mappings/MANAGE-FUNCTION-MATURITY-MAPPING.md             research=0  **Status**: Complete detailed mapping
mappings/MAP-FUNCTION-MATURITY-MAPPING.md                research=0  **Status**: Complete detailed mapping
mappings/MEASURE-FUNCTION-MATURITY-MAPPING.md            research=0  **Status**: Complete detailed mapping
```

---

## Open items passed to follow-up

Defects found during verification that are outside the scope of the
standards-completeness correction are tracked separately rather than silently folded in:

- **Control count.** The catalog contains **72** controls. Every current-count statement in
  README.md, core/, implementation/ and the QA report now reads 72 (GOVERN 19, MAP 18,
  MEASURE 22, MANAGE 13) as of v1.0.2; the only remaining `73` figures are the dated
  January-2026 change-control plan records (`change-control/20260129143000-*.md`), which
  are kept as the historical record of what was planned before the change was completed.
- **ISO 27001 depth.** `mappings/AIMF-ISO27001-MAPPING.md` is mapped at the public
  Annex A control-theme level only; control-level depth is not claimed pending a licensed
  copy of ISO/IEC 27001:2022.

Items closed by v1.0.1 (previously listed here): the four dedicated standard mappings
(`AIMF-NIST-RMF-MAPPING.md`, `AIMF-ISO42001-MAPPING.md`, `AIMF-ISO27001-MAPPING.md`,
`AIMF-EXECUTIVE-ORDER-14179-MAPPING.md`) are no longer research skeletons, and the
catalog's ISO 27001 numbering is normalised to the 2022 edition with no 2013-vintage IDs
remaining.
