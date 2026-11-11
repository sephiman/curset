# aeat-agentes-hacienda, round R0a: working data

2026-11-11. Handoff: `docs/aeat-round-0a-handoff.md`. Scripts run from the repo with `python3 -I <script>`.

| Folder / file | Content |
|---|---|
| `sources-manifest.tsv` | Every file in `sources/examenes-oficiales/`: download date, sha256, AEAT URL. Written by `scripts/place_sources.py` (copies from a download folder under the C1 naming scheme). |
| `parsed/` | The 13 first-exercise questionnaires parsed to JSON (`scripts/parse_exams.py`), and `master.json`: the 680 distinct questions (tipo A + the 2022 extraordinario) with key, tipo B number and the Tribunal's decision (`scripts/build_master.py`). |
| `keys/` | The definitive answer sheets as JSON (2022X: the provisional sheet, made definitive unchanged). |
| `classification/` | `brief_common.md` (the classifiers' brief), `class_set1.json` (2025, 2024, 2023, 2022X) and `class_set2.json` (2022, 2021, 2020) from two Opus classifiers, `overrides.json` (coordinator). |
| `checks/` | `pairing.json` (tipo A ↔ B), `provisional-vs-definitive.txt`, `resoluciones-anulaciones.txt`, `norms_cited.txt`, `textstats.json`, `style_stats.json`, `style_by_part.txt`, `repeated.txt`, `second-exercise-outline.txt`, `norm_build_report.json`, `norm_currency.json`. |
| `scripts/` | Parsers and generators. `gen_ledger.py` writes `docs/aeat-official-exams-ledger.md` (header in `ledger_header.md`). `verify_programa.py` checks `programa.md` against the BOE and criteria PDFs. `norm/` builds `sources/normativa.yaml`. The style guide was written by hand on top of the stats. |

Not kept: the raw downloads (scratchpad), the provisional answer sheets other than 2022X, and the admitted/approved lists.
