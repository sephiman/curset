# Handoff — age-auxiliar-c2, round R1 (skeleton)

2026-11-06. Nothing committed. Requirements: `docs/age-auxiliar-course-requirements.md` v1.1 (a delta to the C1
requirements); method as C1's R1 (`docs/age-round-1-handoff.md`).

## What exists now

| Path | Content |
|---|---|
| `content/age-auxiliar-c2/course.yaml` | Slug `age-auxiliar-c2`, title «Auxiliar Administrativo del Estado (C2)», subtitle «Ingreso libre · convocatoria OEP 2026», `languages: [es]`, `status: draft`, `exercise_types: [quiz]` (with a comment: psicotécnico joins once platform delta section L exists), `lesson_noun: {es: tema}`, `lesson_practice: true`, `option_labels: letters`, `pdf_exercises: false`. No glyph or color (comment: identity round). Ends with an `# exams:` comment listing the R7.1 presets. |
| block `block-a` «Proceso de selección» | `m00` «El examen» → `m00-l01` «Cómo es el examen»; `ps` «Psicotécnicos» → `ps-l01` «Cómo son los psicotécnicos». Both lessons written in full; their modules and lessons carry real summaries. |
| block `block-b` «Programa» | `m01` «Organización pública» (bloque I, `m01-l01` … `m01-l16`) and `m02` «Actividad administrativa y ofimática» (bloque II, `m02-l01` … `m02-l12`). 28 lessons; titles are the tema paragraphs of `sources/programa.md`, verbatim; module and lesson summaries «Resumen pendiente.». |
| `es/lessons/m00-l01.md` | About 920 words (1,090 counting numbers and formulas): Anexo I rules (one exercise, two parts together, 90 minutes, 60 + 5 and 50 + 5, four options, −1/3 per error, blanks free, invalid marks), A − E/3, the 30 % floor (18 and 15), the CPS 2025 criteria (4.632/468 and 1.544/156), the 2025 cut-offs, 21,33 = 64/3 and 15,33 = 46/3 with the 22-right-2-wrong example, the CPS formula with two worked examples (part 1: 40 → 33,87; part 2: 23 → 26,45), the final mark, the C2 tie-breaks (part 2 first), norma común 11.1. |
| `es/lessons/ps-l01.md` | The 16 types of `docs/age-c2-psicotecnico-index.md` in four groups (tablas; cálculo y series; lenguaje; códigos, archivo y orden), a table of counts (2025 weights of 30 and totals over the six questionnaires), and per type one official question verbatim with its convocatoria, number, definitive key and the working. All 16 stems and options were checked against the questionnaire PDFs and all 16 keys against the ledger. The two analogía items have disputed keys; the lesson says so. |
| `es/lessons/m01-*.md`, `m02-*.md` | 28 stubs: title as `#`, `:::note{type=info}` «Tema sin redactar.», `## Normativa` from `normativa.yaml` (below). II.6–II.12 say «Este tema no se apoya en ninguna norma.». |
| `glossary.yaml` | `terms: []`. |
| `exercises/.gitkeep` | Empty folder; the loader needs no index. |
| Generated | `source-index.json` (`scripts/index_sources.py`), `excerpts.json` (empty: 0 questions), `citations.es.txt` (20 Normativa norms, 0 prose citations, 0 unknown norms), `glossary-links.es.txt` and `lesson-refs.es.txt` (both 0), `question-keys.tsv` (empty). |
| `sources/otros/` | 8 files added for tema I.6 (below); `fuentes.yaml` now 76 entries, every sha256 asserted. |

### Choices to check

- **Psicotécnicos module id `ps`.** Not `m01`: that would break «mNN = bloque NN», which C1 also follows. The badge reads «PS · Psicotécnicos». The id order of the course (m00, ps, m01, m02) is not sorted. The only test that pins sorted module ids is crypto-futures'. R6.4's «Psicotécnicos» practice entry can live in this module once section L exists.
- **`pdf_exercises: false`**, not in the round prompt, copied from C1 (the PDF prints theory only). The course has no exercises yet, so nothing changes today.
- **Block and module titles.** «Proceso de selección» and «Programa» as in C1; the module titles are the bloque names without the numeral.
- **Normativa line format.** A line with an article range reads `- <short>: <range>.` and the citation parser links it (20 lines). A norm without a range reads `- <short>.` and stays plain text, as in C1's R1 stubs (the parser only reads a line with «norm:»). A pending change reads «Cambio pendiente por el/la <norma>, en vigor el <fecha> (<preceptos>).». The phrase has no colon on purpose: «Reglamento del Congreso. Cambio pendiente: …» was parsed as a norm named «Reglamento del Congreso. Cambio pendiente». R2 adds the article list (`- <short>: arts. … Cambio pendiente: …`, C1's written form).
- **The intro lessons' Normativa** cite the convocatoria (BOE-A-2025-26262), not `normativa.yaml`, as in C1. The convocatoria line wraps before its colon, so it is not a linked norm (same as C1).
- **Generator.** `course.yaml`'s programme part and the 28 stubs come from a one-off script in the session scratchpad, not the repo. R2 edits the files by hand.

## Normativa state

### Aligned with C1's November audit

All 77 entries shared with C1 point at byte-identical files (sha256 checked per file; the other 4 are C2-only). For the shared norms, every currency field now matches C1's post-audit `normativa.yaml`:

- **Ley 4/2026 applied** (in force 23-10-2026): `cambios_aplicados` added, with C1's fields and precept lists, to LBRL (DF 3), Ley 16/1985 (DF 4), TREBEP (DF 11), LGSS (DF 12), RDL 1/2013 (artículo primero) and Ley 39/2006 (artículo segundo y DA 3). Their `version_vigente` notes now read «el fichero trae integrada la redacción … es el texto vigente». The DF numbers were checked in this course's copy of the Ley 4/2026. The Ley 4/2026 entry's note says its changes are in `cambios_aplicados`. The header documents the field.
- **RDL 31/2026 in force since 21-10-2026, convalidación pending.** RDL 4/2000, RDL 670/1987 and LGSS carry C1's notes, «sin convalidación del Congreso (art. 86.2 CE) en boe.es el 2026-11-05: si se deroga, estos preceptos vuelven a la redacción anterior», without C1's «se conserva el fichero anterior» (this course has no earlier file). Their `amended_2025_2026` lines and `cambios_pendientes` now carry C1's exact precepts and modifying provisions.
- **`version_vigente` of RDL 4/2000 and LGSS** was «sin comprobar». It now says what the files show. I checked this course's copies: the «Téngase en cuenta…» notice with «Redacción anterior» sits under RDL 4/2000 art. 19.1 and under LGSS arts. 144.4, 169.1.a), 171, 172, 173.1 and 309.1.
- **Not re-checked this round:** whether the Congreso has convalidated RDL 31/2026 since 2026-11-05 (the 30-working-day window ends about 04-12-2026).

### Pending changes (`cambios_pendientes`)

| Norm | Amending norm | In force | Precepts | Tema |
|---|---|---|---|---|
| Reglamento del Congreso | Reforma de 23-07-2026 | XVI legislatura (sesión constitutiva 23-12-2026) | art. 23 | I.3 |
| RDL 4/2000 | RDL 31/2026 | 01-12-2026 | art. 19.1 | I.14 |
| LGSS | RDL 31/2026 | 01-12-2026; 01-01-2027 | arts. 144.4, 169.1.a), 171, 172, 173.1; art. 309.1 | I.14 |
| RD 366/2007 | RD 707/2026 | 02-01-2027 | art. 13 | II.1 |

Each stub of those temas says so in its Normativa block.

### Sources for tema I.6

The files C1's I.6 lesson cites, minus the two pages that now answer 404 (`transparencia-planes-anteriores.html`, `transparencia-iv-plan.html`) and the copy of `transparencia-planes-accion.html` that the 2026-11-05 version replaced. Live check on 2026-11-06, the same text comparison as R0a (visible `<main>` text for HTML, sha256 for PDF):

| File | Result | Kept |
|---|---|---|
| `un-res-70-1-agenda-2030.pdf`, `oecd-recomendacion-gobierno-abierto-2017.pdf`, `transparencia-iv-plan.pdf`, `transparencia-v-plan.pdf` | live file has the same sha256 | C1's copy |
| `transparencia-planes-accion_2026-11-05.html` | same sha256 | C1's copy |
| `un-ods-objetivos.html` | same visible text | C1's copy |
| `transparencia-gobierno-abierto-que-es.html`, `transparencia-v-plan.html` | article text unchanged; the site menu changed (adds the five plans, drops «Subgrupo de Trabajo de la reforma de la Ley 19/2013») | fresh live copy, as R0a did for `ms-copilot-introduccion.html` |

## Normativa block: article ranges

Ranges appear only where the programme names a part of the norm. Each was checked against the título/capítulo headings of the course's own consolidated text:

| Tema | Norm | Range |
|---|---|---|
| I.1 | CE | arts. 1–9 (título preliminar) y 10–55 (título I) |
| I.2 | CE | arts. 56–65 (título II), 159–165 (título IX) y 166–169 (título X) |
| I.3 | CE | arts. 54 y 66–96 (título III) |
| I.4 | CE | arts. 117–127 (título VI) |
| I.5 | CE | arts. 97–107 (título IV) y 108–116 (título V) |
| I.8 | LRJSP | arts. 54–80 (título I) |
| I.9 | CE | arts. 137–158 (título VIII) |
| I.9 | LBRL | arts. 3, 11–30 (título II) y 31–41 (título III); art. 41 is the islands |
| I.10 | TUE | arts. 13–19 (título III) |
| I.10 | TFUE | arts. 223–281 (sexta parte, título I, capítulo 1: sections 1–5, Parliament to Court of Justice; section 6, the ECB, starts at 282) |
| I.11 | LPAC | arts. 53–126 (títulos IV y V) |
| I.11 | LJCA | arts. 18–30 (título II, las partes; título III capítulo I, actividad impugnable) |
| I.12 | RGPD | arts. 5–43 (capítulos II a IV) |
| I.12 | LOPDGDD | arts. 4–18 (títulos II y III) y 28–39 (título V) |
| I.13 | TREBEP | arts. 8–13 (título II), 55–62 (título IV, cap. I), 69–71 (título V, cap. I), 78–84 (título V, cap. III) y 85–92 (título VI) |
| I.14 | TREBEP | arts. 14–54 (título III) y 93–98 (título VII) |
| I.15 | LGP | arts. 32–41 (título II, capítulo III «Contenido, elaboración y estructura») |
| II.2 | RD 951/2005 | arts. 14–19 (capítulo IV, quejas y sugerencias) |
| II.3 | LPAC | arts. 16–17 (registros, archivo) |
| II.3 | Ley 16/1985 | arts. 48–66 (título VII) |

The other norm–tema pairs list the norm alone: they are supporting norms, or the programme names the subject as a whole.

### Programme sentences whose article mapping I could not pin down

- **I.15 «Fases del ciclo presupuestario».** No single unit holds it. Elaboración is LGP arts. 36–38, aprobación is CE art. 134, ejecución is LGP título II capítulo VI (art. 73, «Fases del procedimiento de la gestión»), control is título VI. CE is not tagged I.15 in `normativa.yaml`. I did not add the tag: R2 should decide when it writes the tema.
- **I.13 «Régimen jurídico».** The TREBEP has no unit by that name for funcionarios; the tema's sources are spread over TREBEP título I, Ley 30/1984 and the RD 364/1995 and 365/1995.
- **I.8 «Otros órganos administrativos».** Inside LRJSP título I it could mean the órganos colegiados (arts. 78–79) or the units below the directivos (art. 59). The range 54–80 covers both, but I could not tie the phrase to one.
- **I.6 «Gobierno Abierto … Agenda 2030».** It rests on the plans and the UN resolution in `sources/otros/`, not on a norm. Ley 19/2013 is tagged I.6 but the programme does not name a part of it.
- **II.1 «Acogida e información al ciudadano».** RD 208/1996 art. 4.a) (recepción y acogida) fits «acogida», but «información» spans arts. 1–4 and capítulo II. Left without a range.
- **II.2 «Los servicios de información administrativa. Información general y particular».** RD 208/1996 arts. 2–3 hold general and particular information; «servicios» is capítulo II (arts. 5–14). The roles of LPAC, RD 210/2024 and RD 776/2011, tagged II.2 in `normativa.yaml`, are not clear from the programme text.
- **II.4.** Administración electrónica, oficinas integradas, ventanilla única and PAG are spread over LRJSP, LPAC, RD 203/2021, Orden HAP/1949/2014, RD 127/2015, the 2005 Acuerdo and Ley 14/2013. No range.
- **I.11 «Las Leyes del Procedimiento Administrativo Común … y del Régimen Jurídico del Sector Público».** Names both laws whole; the LRJSP stays without a range.

## Pipeline

- **Load.** The course loads as a draft: 30 lessons, no figures. `pytest`'s «figure steps per course» prints `age-auxiliar-c2: no figures`.
- **Suites.** Registry, list-shape, cross-reference (0 references, 0 dangling), glossary links, citations and i18n all pass on the course.
- **PDF.** The draft-course PDF test passes for `age-auxiliar-c2`: no capture phase, `no figures` / `no exercise charts` logged, table-of-contents lesson entries equal the manifest's 30 titles in order, more pages than lessons. `pipeline_courses.py` and `courseContent.ts` already cover every course under `content/`, so nothing there changed.
- **One lesson fix the guard caught.** In `ps-l01` the options «a) 259.» … «d) 244.» read as stray numbered-list markers. They are printed without the final dot.
- **Identity tests narrowed** (`frontend/src/assets/identity/identity.test.ts`, `backend/tests/test_course_identity.py`). Both demanded a glyph and an accent from every course, drafts included. R2a.6 of the platform requirements asks only that a declared glyph exists, and the schema makes both optional. Now a published course must declare a glyph; any declared glyph must exist and be a clean SVG; the backend skips a draft that declares neither glyph nor color, so C2 is checked in full once its identity round adds them. C1 and crypto-futures are still checked as before.
- **README** («Courses, languages and reports», the identity paragraph, the figure-steps line) and `content/README.md` updated.

## Results

- **crypto-futures and C1:** no file under `content/crypto-futures/` or `content/age-administrativo-c1/` changed (git status).
- **Android bundle:** re-exported to a scratch folder, byte-identical to `dist/bundle/` (98 files + manifest).
- **Frontend (`npx vitest run`):** see «Suites» below. `tsc -b` clean.
- **Backend (`uv run pytest`):** see «Suites» below. `ruff check`, `ruff format` and `mypy` clean on the changed test file.

### Suites

Run on the final tree, after the blind check's fixes:

- **Backend (`uv run pytest`, Docker running):** 1,618 passed, 23 skipped (2 of them the C2 identity tests, skipped until its identity round), 0 failed, 0 errors. «Figure steps per course»: `age-administrativo-c1: no figures`, `age-auxiliar-c2: no figures`, `crypto-futures: 35 figures`, `fixture-oposiciones: no figures`.
- **Frontend (`npx vitest run`):** 715 passed, 81 skipped, 0 failed. `tsc -b` clean.

### Blind check of the two written lessons

One Opus verifier read `m00-l01` and `ps-l01` against `programa.md`, the psicotécnico index, the ledger and the questionnaire PDFs, and against `prose-voice.md`. It found no factual error. Every stem, option, question number, key and calculation matched. I applied its precision and voice points:

- «Si una norma cambia antes del examen» → «Si un cambio entra en vigor antes del examen» (norma común 11.1 is about the date in force).
- The no-calculator rule is now attributed to the OEP 2020 covers only (the 2025 questionnaire has no cover).
- «de la 31 a la 60» is now what the six questionnaires did, not an exam rule.
- The look-ahead closing line of the intro paragraph in `m00-l01` is dropped.
- Three «Cuatro …» openers and three triad-shaped lists in `ps-l01` are reworded.

It also noted that «colmena» counts as a group of animals only through its third DLE sense. Kept: it is the official key.

## Open, for R2 and later

- **Psicotécnico batch.** Open decision 1 of the requirements: the index proposes the 13 recurring types first.
- **Glyph and accent:** the identity round (R2.2).
- **Exam presets:** after the bank (R3) and section L (generated items in a part).
- **RDL 31/2026:** check convalidación or derogation before about 04-12-2026; if derogated, the three Seguridad Social entries revert.
- **I.15:** decide whether CE (art. 134) is tagged I.15.
- **Unchanged from R0a:** the source for «Grupos de envío y recepción»; the 26 Microsoft pages marked «live check pending (403 on 2026-11-05)»; the «Etiqueta actual» and Word-shortcut checks on a Spanish-locale Windows 11.
