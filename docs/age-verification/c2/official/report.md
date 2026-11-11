# Official-exam sets, build report (R5, 2026-11-11)

Built by `backend/scripts/build_c2_official_exams.py` from the questionnaire PDFs and `docs/age-c2-official-exams-ledger.md`
(tables in `scripts/c2_official_exam_tables.py`, recomputation in `scripts/verify_c2_official_tables.py`). Tests:
`backend/tests/test_age_c2_official_exams.py`. Counts: `summary.json`.

| Exam | Included | With note | Excluded (ledger ids) | Table questions |
|---|---|---|---|---|
| conv2025_A | 118 | 0 | P2-6 norma modificada, P2-13 anulada | 12 |
| conv2025_B | 118 | 0 | P2-4 norma modificada, P2-12 anulada | 12 |
| conv2024_A | 118 | 2 | P1-18 dudosa, P1-23 anulada | 12 |
| conv2024_B | 118 | 2 | P1-15 dudosa, P1-24 anulada | 12 |
| conv2024_X | 117 | 7 | R1-1 dudosa, P2-39 función retirada, P2-48 anulada | 12 |
| conv2022 | 115 | 3 | P1-12 norma modificada, P2-13 dudosa, P2-42, P2-43, R2-3 anuladas | 12 |
| conv2020 | 116 | 3 | P1-12, P1-53 anuladas, P2-17, P2-19 función retirada | 12 |
| conv2020_X | 114 | 2 | P1-18 norma modificada, P1-54, P2-28 anuladas, P2-3, P2-8, P2-31 función retirada | 12 |

934 included (915 vigente + 19 vigente-con-nota), 26 excluded: the ledger's Summary row by row.

**Shape.** One quiz exercise per questionnaire (`ofi-<slug>`), `shuffle: false`, variants `q001…` over the included
questions in questionnaire order (P1, R1, P2, R2), original option order, tags `[<ledger code>, <section>-<n>]`
(how a test maps a variant to its ledger row). A table question carries `table:` on every question that uses it.

**Notes.** `vigente-con-nota` → `explanation` = «Nota de clave» + «Nota», cleaned. Dropped: the «Modelo B: P1 4.» /
«= modelo A P1 55.» cross-references; the «Tabla … transcrita de la imagen» mark; on conv2024_X P2-29 and P2-30 three
sentences about the answer sheet's column (coordinator bookkeeping). A `vigente` question has no explanation even when
its Nota column holds a review remark (115 rows). A final period is added where a ledger part has none.

**Tables.** Préstamos and Desplazamientos (2025; the «Dieta / Combustible» side block is two extra columns, no question
uses them), Biblioteca (2024, two-level header flattened), Laboratorios (2024, the ledger's checked transcription),
Academia and Archivos (2024 X), Ponencias and Flores (2022; Flores merges three tables sharing the «Flor» column),
and the tables of 2020 and 2020 X. For tables with no printed instruction sentence the title is the caption plus the
printed sentences, asserted present in the PDF text.

**Recomputation.** All 96 table questions recomputed from the transcribed tables: 96 of 96 equal the official key.
Two rest on reading, not arithmetic: conv2024_X P1-56 (that «Hamlet» is English is not in the table) and the Archivos
statement questions («primer estante negro» in P1-58 c = estante 1, color 3).

**Images.** None besides the Laboratorios table (one image per conv2024 modelo, page 7); no question needs a figure.

**Layout notes.** conv2024_X P2-39 prints «39.¿Cuál…» without a space; conv2022 R2-5 prints «5    En Excel 2019…»
without a period; both kept as printed. conv2020 and conv2020_X print two options per line in 51 questions each.

## Blind verification (two Opus verifiers, PDFs only, ledger and builder unread)

All 934 variants checked: stems, options, keys against the definitive sheets (modelo B against its own), tables cell by
cell, and every absent number confirmed as an excluded question visible in the PDF. **0 discrepancies in wording,
options or keys.** One structural finding, fixed: in the 2025 Desplazamientos table the separate «Dieta / Euros» block
and the «Combustible: 0,2 €/Km» line had been merged into two extra columns on specific project rows, which read as
belonging to those projects. The table now has the printed six columns and the side block is in the title
(`side_note`); no question used it; builder rerun, tests 108 passed. The 2022 «3y6» was checked on the render:
printed «3 y 6».
