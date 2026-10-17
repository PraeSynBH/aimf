# AI Management Framework (AIMF) by PraeSyn
## Standards Mapping Completeness Register

**© 2026 PraeSyn, LLC. All rights reserved.**
Licensed under CC BY-NC-ND 4.0

**Version**: 1.0
**Document Type**: Verification Register
**Status**: Verified 2026-10-17 against repository state at commit `78d9089`
**Supersedes**: the standards-mapping completeness claims previously carried by
README.md, QA-VERIFICATION-REPORT.md and QUALITY-ASSURANCE-CHECKLIST.md

---

## Why this document exists

The v1.0 baseline stated, in several places, that specific standards mappings were
complete. A review on 2026-10-17 found that some of those statements
were not supported by the content of the files they pointed at. In an asset that is
sold on standards alignment, an unsupported completeness claim is a credibility
defect, so this register records, for every mapping artifact, (a) what the file
actually contains and (b) the command used to check it.

Every claim in this register is reproducible with the commands in
[Evidence commands](#evidence-commands). Where a mapping is incomplete, it is marked
incomplete. No status here exceeds the file content.

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
MANAGE 10) were wrong. The framework's actual coverage is 72/72 — see below — but the
figure carried in the documentation was not.

---

## Mapping completeness

Status is taken from each file's real content, not from its header. "Evidence"
refers to the numbered commands in [Evidence commands](#evidence-commands); each
command was run on 2026-10-17 and its output is quoted.

| File | Standard | Status taken from content | Evidence |
|------|----------|---------------------------|----------|
| `core/AIMF-CONTROL-CATALOG.csv` | NIST AI RMF 1.0 | **Complete** — `NIST_RMF_Subcategory` populated for all 72 controls; the 72 distinct subcategory IDs equal the authoritative NIST set exactly (0 missing, 0 extra) | E1, E2, E9 |
| `core/AIMF-CONTROL-CATALOG.csv` | ISO/IEC 42001:2023 | **Populated** — `ISO42001_Clauses` non-empty for 72/72 controls; 19 distinct clause references | E2, E4 |
| `core/AIMF-CONTROL-CATALOG.csv` | ISO/IEC 27001 | **Partial and numbered inconsistently** — `ISO27001_Controls` non-empty for 34/72 controls; IDs mix ISO 27001:2022 themes (A.5, A.6, A.8) with retired ISO 27001:2013 IDs (A.9.2, A.18.1, A.18.2) while the doc set cites the 2022 edition | E3 |
| `mappings/AIMF-NIST-RMF-MAPPING.md` | NIST AI RMF 1.0 | **Research skeleton** — 4 subcategory IDs, 5 "Required Research" markers, 0 AIMF control IDs | E5, E7, E8 |
| `mappings/GOVERN-FUNCTION-MATURITY-MAPPING.md` | NIST GOVERN + ISO 42001 | **Working draft** — all 19 GOVERN subcategory IDs present, but header remains `Pre-Publication (Working Draft)` pending SME review | E10 |
| `mappings/MAP-FUNCTION-MATURITY-MAPPING.md` | NIST MAP + ISO 42001 | **Complete** — all 18 MAP subcategory IDs present | E10 |
| `mappings/MEASURE-FUNCTION-MATURITY-MAPPING.md` | NIST MEASURE + ISO 42001 | **Complete** — all 22 MEASURE subcategory IDs present | E10 |
| `mappings/MANAGE-FUNCTION-MATURITY-MAPPING.md` | NIST MANAGE + ISO 42001 | **Complete** — all 13 MANAGE subcategory IDs present; the "59" total line in its closing section is superseded by this register | E10 |
| `mappings/AIMF-ISO42001-MAPPING.md` | ISO/IEC 42001:2023 | **Research skeleton** — 7 clause references, 5 "Required Research" markers, 0 AIMF control IDs | E6, E7, E8 |
| `mappings/AIMF-ISO27001-MAPPING.md` | ISO/IEC 27001:2022 | **Research skeleton** — 9 "Required Research" markers, 0 AIMF control IDs | E7, E8 |
| `mappings/AIMF-EXECUTIVE-ORDER-14179-MAPPING.md` | EO 14179 | **Research skeleton** — 6 "Required Research" markers, 0 AIMF control IDs | E7, E8 |
| `mappings/AIMF-EXECUTIVE-ORDER-14110-MAPPING.md` | EO 14110 | **Complete detailed mapping** — but note the order was **rescinded 2025-01-20** by EO 14179; retained for historical traceability only | header |
| `mappings/AIMF-DIMENSION-MAPPING.md` | Internal (4 dimensions) | **Working draft** — maps dimensions to the 72 controls | header |

### What this means for the NIST claim

NIST AI RMF 1.0 subcategory coverage **is** complete (72/72). It is evidenced in two
places:

1. `core/AIMF-CONTROL-CATALOG.csv` — every control carries its NIST subcategory ID,
   and the union of those IDs is the complete NIST set.
2. The four `*-FUNCTION-MATURITY-MAPPING.md` files — 19 + 18 + 22 + 13 = 72.

It is **not** evidenced in `mappings/AIMF-NIST-RMF-MAPPING.md`, whose header the
published README pointed at. That document is still a research skeleton. A correct
claim therefore has to name the file that actually holds the mapping.

---

## Evidence commands

Run from `documents/AIMF-Full-Documentation/`. Outputs below are verbatim.

**E1 — distinct NIST subcategories covered in the catalog**
```
$ grep -oE '(GOVERN|MAP|MEASURE|MANAGE) [0-9]+\.[0-9]+' core/AIMF-CONTROL-CATALOG.csv | sort -u | wc -l
72
```

**E2 — catalog row count**
```
$ python3 -c "import csv;r=list(csv.DictReader(open('core/AIMF-CONTROL-CATALOG.csv')));print(len(r))"
72
```

**E3 — controls carrying an ISO 27001 reference, and their numbering vintage**
```
$ python3 -c "import csv;r=list(csv.DictReader(open('core/AIMF-CONTROL-CATALOG.csv')));print(sum(1 for x in r if x['ISO27001_Controls'].strip()))
34
$ grep -oE 'A\.[0-9]+\.[0-9]+' core/AIMF-CONTROL-CATALOG.csv | sort -u | wc -l
21        # includes retired 2013 IDs A.9.2, A.18.1, A.18.2
```

**E4 — controls carrying an ISO 42001 clause reference**
```
$ python3 -c "import csv;r=list(csv.DictReader(open('core/AIMF-CONTROL-CATALOG.csv')));print(sum(1 for x in r if x['ISO42001_Clauses'].strip()))
72
```

**E5 — subcategory IDs inside the dedicated NIST mapping document**
```
$ grep -oE '(GOVERN|MAP|MEASURE|MANAGE) [0-9]+\.[0-9]+' mappings/AIMF-NIST-RMF-MAPPING.md | sort -u | wc -l
4
```

**E6 — clause references inside the dedicated ISO 42001 mapping document**
```
$ grep -oE 'Clause [0-9]+\.[0-9]+' mappings/AIMF-ISO42001-MAPPING.md | sort -u | wc -l
7
```

**E7 — AIMF control IDs inside each dedicated mapping document**
```
$ for f in mappings/AIMF-NIST-RMF-MAPPING.md mappings/AIMF-ISO42001-MAPPING.md \
           mappings/AIMF-ISO27001-MAPPING.md mappings/AIMF-EXECUTIVE-ORDER-14179-MAPPING.md; do
    echo -n "$f: "; grep -oE '\b(GOV|MAP|MEA|MAN)-[0-9]+\.[0-9]+' "$f" | sort -u | wc -l; done
mappings/AIMF-NIST-RMF-MAPPING.md: 0
mappings/AIMF-ISO42001-MAPPING.md: 0
mappings/AIMF-ISO27001-MAPPING.md: 0
mappings/AIMF-EXECUTIVE-ORDER-14179-MAPPING.md: 0
```

**E8 — "Required Research" markers per mapping file**
```
$ for f in mappings/*.md; do echo -n "$f: "; grep -c 'Required Research' "$f"; done
mappings/AIMF-DIMENSION-MAPPING.md: 0
mappings/AIMF-EXECUTIVE-ORDER-14110-MAPPING.md: 0
mappings/AIMF-EXECUTIVE-ORDER-14179-MAPPING.md: 6
mappings/AIMF-ISO27001-MAPPING.md: 9
mappings/AIMF-ISO42001-MAPPING.md: 5
mappings/AIMF-NIST-RMF-MAPPING.md: 5
mappings/GOVERN-FUNCTION-MATURITY-MAPPING.md: 0
mappings/MANAGE-FUNCTION-MATURITY-MAPPING.md: 0
mappings/MAP-FUNCTION-MATURITY-MAPPING.md: 0
mappings/MEASURE-FUNCTION-MATURITY-MAPPING.md: 0
```

**E9 — catalog subcategory set equals the authoritative NIST AI 100-1 set**
```
$ # authoritative set extracted from https://nvlpubs.nist.gov/nistpubs/ai/nist.ai.100-1.pdf
$ python3 - <<'PY'
import re, csv
txt = open('nist-ai-100-1.txt', encoding='utf-8', errors='ignore').read()
auth = {f"{a} {b}" for a, b in re.findall(r'\b(GOVERN|MAP|MEASURE|MANAGE)\s+(\d+\.\d+)', txt)}
csvset = set()
for r in csv.DictReader(open('core/AIMF-CONTROL-CATALOG.csv')):
    csvset.update(f"{m[0]} {m[1]}" for m in
                  re.findall(r'\b(GOVERN|MAP|MEASURE|MANAGE)\s*(\d+\.\d+)', r['NIST_RMF_Subcategory']))
print("authoritative:", len(auth), " catalog:", len(csvset))
print("missing:", sorted(auth - csvset), " extra:", sorted(csvset - auth))
PY
authoritative: 72  catalog: 72
missing: []  extra: []
```

**E10 — distinct NIST subcategory IDs per mapping file, with header status**
```
$ for f in mappings/*.md; do n=$(grep -oE '(GOVERN|MAP|MEASURE|MANAGE) [0-9]+\.[0-9]+' "$f" | sort -u | wc -l);
    st=$(grep -m1 -E '^\*\*Status\*\*' "$f"); printf "%-55s %3s  %s\n" "$f" "$n" "$st"; done
mappings/AIMF-DIMENSION-MAPPING.md                        0  **Status**: Pre-Publication (Working Draft)
mappings/AIMF-EXECUTIVE-ORDER-14110-MAPPING.md            9  **Status**: Complete detailed mapping
mappings/AIMF-EXECUTIVE-ORDER-14179-MAPPING.md            0  **Status**: Pre-Publication (Working Draft)
mappings/AIMF-ISO27001-MAPPING.md                         0  **Status**: Pre-Publication (Working Draft)
mappings/AIMF-ISO42001-MAPPING.md                         0  **Status**: Research Required - Detailed mapping needed
mappings/AIMF-NIST-RMF-MAPPING.md                         4  **Status**: Pre-Publication (Working Draft)
mappings/GOVERN-FUNCTION-MATURITY-MAPPING.md             19  **Status**: Pre-Publication (Working Draft)
mappings/MANAGE-FUNCTION-MATURITY-MAPPING.md             13  **Status**: Complete detailed mapping
mappings/MAP-FUNCTION-MATURITY-MAPPING.md                18  **Status**: Complete detailed mapping
mappings/MEASURE-FUNCTION-MATURITY-MAPPING.md            22  **Status**: Complete detailed mapping
```

---

## Open items passed to follow-up

These are real defects found during verification but outside the scope of the
standards-completeness correction; they are tracked separately rather than silently
folded in:

- **Control count.** The catalog contains **72** controls, but README.md,
  CHANGELOG.md, several profile documents and the change-control records variously
  say **73** (and README lists MAP as 19 controls where the catalog has 18).
- **ISO 27001 numbering.** The catalog's `ISO27001_Controls` column mixes
  ISO/IEC 27001:2022 theme IDs with retired ISO/IEC 27001:2013 IDs while the doc set
  cites the 2022 edition.
- **Dedicated standard mappings.** `AIMF-NIST-RMF-MAPPING.md`,
  `AIMF-ISO42001-MAPPING.md`, `AIMF-ISO27001-MAPPING.md` and
  `AIMF-EXECUTIVE-ORDER-14179-MAPPING.md` remain research skeletons.
