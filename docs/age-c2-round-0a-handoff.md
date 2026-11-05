# Handoff — age-auxiliar-c2, round R0a (sources, programme, legislation, exam style, ofimática, psicotécnicos, ledger)

2026-11-05. Nothing committed. Nothing written under `es/`, `glossary/` or `exercises/`; no `course.yaml`. Requirements: `docs/age-auxiliar-course-requirements.md` v1.1 (a delta to the C1 requirements).

**Juanjo's decisions of 2026-11-05 are applied** (source URLs, Microsoft pages, ledger rows, «programa anterior», exam rules); each section below says what was decided. The working data of the round is in `docs/age-verification/c2/r0a/`.

## What this round produced

| File | Content | Counts |
|---|---|---|
| `content/age-auxiliar-c2/sources/programa.md` | Anexo I of BOE-A-2025-26262 verbatim: exam rules (points 1–2.3.3), norma común 11.1, programme (point 3); then the three CPS notes of the 2025 convocatoria (criterios, puntuaciones mínimas, fórmula de transformación). | 2 bloques, 28 temas (I: 16, II: 12). 83 copied paragraphs checked by script against the BOE and CPS text: all verbatim. |
| `content/age-auxiliar-c2/sources/normativa.yaml` + `sources/normativa/` | Every norm the 28 temas rest on, in C1's format plus an `origen` field. | 81 entries: 75 BOE, 5 EU, 1 not located. 86 files: 79 copied from C1 (same name, same sha256), 7 downloaded fresh. 4 entries with cambio-pendiente. 21 of 28 temas tied to a norm; II.6–II.12 rest on none. |
| `docs/age-c2-exam-style.md` | Style guide for the knowledge questions: bloque I, bloque II II.1–II.4 and ofimática II.5–II.12 described separately, C1's 12 sections (section 11 points to the psicotécnico index instead of supuestos), reviewer checklist of 21 items, statistics per exam, questions per tema per exam (OEP 2020 columns marked «programa anterior» and left out of the totals). | 6 distinct questionnaires, 525 knowledge questions. |
| `docs/age-c2-ofimatica-index.md` | Every II.5–II.12 question by application, family, feature, form, version, exam and number; recurring and one-convocatoria families; programme phrases asked and never asked; retired, relabelled and version-specific features; the saved Microsoft pages. | 268 questions: Windows 53, Excel 39, Internet 39, Word 36, Access 35, Outlook 31, hardware/software 26, seguridad 6, Copilot 2, otros 1, PowerPoint and Teams 0. 68 pages in `sources/otros/`. |
| `docs/age-c2-psicotecnico-index.md` | Every psicotécnico question by type, with counts per exam and type, weights in the 30 scored questions, parameters per type, a difficulty note, one verbatim example per type with its key, and the first generator batch. | 195 questions, 16 types; 13 recurring types (3+ exams) form the first batch. |
| `docs/age-c2-official-exams-ledger.md` | Per questionnaire (8, modelo B included): number, tema or psicotécnico type, status, definitive key, «Nota de clave», note. A distinct list of excluded and noted questions. The transcription of the image table. | 960 rows (720 distinct): vigente 681, vigente-con-nota 17, anulada 10, norma modificada 3, función retirada 6, dudosa 3, fuera de temario 0 (distinct). |
| `content/age-auxiliar-c2/sources/examenes-oficiales/renders/` | Page 7 of the 2024 modelos A and B rendered at 150 dpi (the «Cuadro Laboratorios» image table). | 2 PNG. |
| `content/age-auxiliar-c2/sources/otros/` + `fuentes.yaml` | Saved Microsoft pages covering the ofimática features, listed in `fuentes.yaml` in C1's format plus `origen` and `comprobacion` (see below). | 68 files. |
| `docs/age-verification/c2/r0a/` | The working data: parsed questionnaires and answer sheets, per-question classification by the four classifiers, the coordinator's overrides, the scripts that generate the ledger and the indexes, the psicotécnico recomputation, the INAP sha256 match and the Microsoft live check. Its `README.md` says how to rerun them. | 66 files. |

The INAP and Microsoft downloads used only for hashing and text comparison stay out of the repo (189 MB of third-party pages).

## Source files

All 20 PDFs are readable and complete. The 8 questionnaires each have 60 + 5 and 50 + 5 questions; every answer sheet has 120 keys and pairs with its questionnaire (checked by hand on several questions per sheet, and modelo A against B by stem and keyed text: all 240 pairs agree). The BOE convocatoria is byte-identical to C1's.

Points to know:

- **`conv2020_*` naming.** The covers say «CUESTIONARIO 19 / AUX–LI» and the footers «2019 AUX-LI»; the answer sheets say «Oferta de Empleo Público de 2020». Same pattern as C1; names kept.
- **Image table.** 2024 modelos A and B, part 1, 55–60: «Cuadro Laboratorios» is an embedded image (the same image in both modelos). Transcribed; the transcription reproduces the six official keys; render kept in `renders/`; ledger rows marked.
- **Misprints.** 2022, part 2, reserve 5 printed «5    En Excel 2019…» without the dot. 2024 extr., part 2, 39 printed «39.¿Cuál…» without a space. 2024 extr., part 2, 1, option d is truncated in the original («…se tramiten los procedimientos en cu»).
- **Extraordinarios.** None for 2025 or 2022: the INAP page publishes none (Juanjo, 2026-11-05).
- **No questionnaire prints the exam date.** 2025 from the file names; the others carry only the PDF creation date (ledger).
- **The transformation note** is the generic CPS note for all bodies; its text equals C1's file of the same name (different bytes, dated 29-09-2026).

### Source URLs

Matched by downloading every PDF linked from the INAP pages to a temp folder on 2026-11-05 and comparing sha256 with the file in `sources/`.

Pages fetched (all answered HTTP 200 to an automated request):
- `https://sede.inap.gob.es/es/procedimientos-y-servicios/seleccion/procesos-selectivos-de-cuerpos-y-escalas-generales/cuerpo-general-auxiliar-de-la-administracion-del-estado-ingreso-libre-convocatoria-2025`
- `…/cuerpo-general-auxiliar-de-la-administracion-del-estado/cuerpo-general-auxiliar-de-la-administracion-del-estado-ingreso-libre-oferta-de-empleo-publico-2023-y-2024`
- `…/cuerpo-general-auxiliar-de-la-administracion-del-estado/cuerpo-general-auxiliar-de-la-administracion-del-estado-ingreso-libre-oferta-de-empleo-publico-2021-y-2022`
- `…/cuerpo-general-auxiliar-de-la-administracion-del-estado/cuerpo-general-auxiliar-de-la-administracion-del-estado-ingreso-libre-oferta-de-empleo-publico-2020`
  (the last three under `https://sede.inap.gob.es/es/procedimientos-y-servicios/seleccion/procesos-selectivos-de-cuerpos-y-escalas-generales/`)
- `https://www.inap.es/es/seleccion/procesos-selectivos-de-cuerposescalas-generales/cuerpo-general-auxiliar-de-la-administracion-del-estado` (archive of earlier exams; its 52 documents end at OEP 2018).

83 PDF links on the sede pages and 52 on the inap.es page were downloaded and hashed.

| File | Download date | sha256 | URL |
|---|---|---|---|
| `convocatorias/2025-12-22_BOE-A-2025-26262_convocatoria.pdf` | 2026-11-05 | `c3063f0665554d67fcb9f45a8a4f59dba9bb883e197ad3c3269539927c35bb47` | https://boe.es/boe/dias/2025/12/22/pdfs/BOE-A-2025-26262.pdf |
| `examenes-oficiales/2026-05-19_conv2025_criterios-correccion.pdf` | 2026-11-05 | `56bbb610148e858e73cc41d11351055f5a29381ca3d11cd0f58cfca361a2471b` | https://sede.inap.gob.es/sites/sede/files/public/2026-05/AUX%20LI%202025.pdf |
| `examenes-oficiales/2026-05-23_conv2025_modeloA_cuestionario.pdf` | 2026-11-05 | `3c0c4d9ccb6c1895a03c1f33f8e231832e822b8a9e29ea7e5124225dba46388d` | https://sede.inap.gob.es/sites/sede/files/public/2026-05/Cuestionario%20AUX-L%20MODELO%20A.pdf |
| `examenes-oficiales/2026-05-23_conv2025_modeloA_plantilla-definitiva.pdf` | 2026-11-05 | `006d4ea365e9c58bd5a06aa41ef1218a2f3827d427b06d1de907d29e81f56680` | https://sede.inap.gob.es/sites/sede/files/public/2026-10/PLANTILLA%20RESPUESTAS%20DEFINITIVA%20AUX-L-ModeloA.pdf |
| `examenes-oficiales/2026-05-23_conv2025_modeloB_cuestionario.pdf` | 2026-11-05 | `3c062e66c687c244a4da1b7beb36a55abd7baf5e0cfb967daf32c4b84e625a31` | https://sede.inap.gob.es/sites/sede/files/public/2026-05/Cuestionario%20AUX-L%20MODELO%20B.pdf |
| `examenes-oficiales/2026-05-23_conv2025_modeloB_plantilla-definitiva.pdf` | 2026-11-05 | `5a3708ee878a9fab29493377e657e795054c3c2faff036cce6614682d6f9719b` | https://sede.inap.gob.es/sites/sede/files/public/2026-10/PLANTILLA%20RESPUESTAS%20DEFINITIVA%20AUX-L-ModeloB.pdf |
| `examenes-oficiales/2026_conv2025_formula-transformacion.pdf` | 2026-11-05 | `fe42454378689cfee9410263caa87721e23ee27c3bfe07a88542c1de287da133` | https://sede.inap.gob.es/sites/sede/files/public/2026-10/Nota%20informativa%20F%C3%B3rmula%20Transformada%20aux.pdf |
| `examenes-oficiales/2026_conv2025_puntuaciones-minimas.pdf` | 2026-11-05 | `1bf14c50664b945ae353a874814e1d56474ed381341e4f29064e167d16b09da0` | https://sede.inap.gob.es/sites/sede/files/public/2026-10/PUNTUACIONES%20MINIMAS%20EJER%20UNICO%20AUX%20L.pdf |
| `examenes-oficiales/conv2020_cuestionario.pdf` | not recorded; in the repo since 2026-11-05 (commit 10af421) | `761e5b5998f8fdece2c977efdc4536ebed6f407d581a168752ff3733d06bad6d` | sede page OEP 2020; the page no longer links it |
| `examenes-oficiales/conv2020_plantilla-definitiva.pdf` | not recorded; in the repo since 2026-11-05 (commit 10af421) | `84e83760808cef0db380c514f567f520d6d73c70b775e89326e9c169422af53b` | sede page OEP 2020; the page no longer links it |
| `examenes-oficiales/conv2020_extraordinario_cuestionario.pdf` | not recorded; in the repo since 2026-11-05 (commit 10af421) | `5382d142d4c6c95b59e1c8ad2453849d7464249663d9ad2e5d914aeefe2f05dd` | sede page OEP 2020; the page no longer links it |
| `examenes-oficiales/conv2020_extraordinario_plantilla-definitiva.pdf` | not recorded; in the repo since 2026-11-05 (commit 10af421) | `ba4efb0f6bd73bc221534af18264dd15da1ad54097d0b00e64d2621df02b3d8c` | sede page OEP 2020; the page no longer links it |
| `examenes-oficiales/conv2022_cuestionario.pdf` | not recorded; in the repo since 2026-11-05 (commit 10af421) | `10c1a41c613a3ff7793484d8d5a1f4feb9889058a23aea20670f27174fcb2b68` | sede page OEP 2021 y 2022; the page no longer links it |
| `examenes-oficiales/conv2022_plantilla-definitiva.pdf` | not recorded; in the repo since 2026-11-05 (commit 10af421) | `4d5e59e59b310abe59d947487a78038c9d95c4b61982651368d6aaddc53e0c3a` | sede page OEP 2021 y 2022; the page no longer links it |
| `examenes-oficiales/conv2024_modeloA_cuestionario.pdf` | not recorded; in the repo since 2026-11-05 (commit 10af421) | `d962838cdf84cb6e5f201fe7c7069c65c384e50c2a3900ff2ca9ab15335dde31` | sede page OEP 2023 y 2024; the page no longer links it |
| `examenes-oficiales/conv2024_modeloA_plantilla-definitiva.pdf` | not recorded; in the repo since 2026-11-05 (commit 10af421) | `8abdaa035c62c471f6391e4bc6bf691fff3408d1b8c0a3869993d64bbf1a843e` | sede page OEP 2023 y 2024; the page no longer links it |
| `examenes-oficiales/conv2024_modeloB_cuestionario.pdf` | not recorded; in the repo since 2026-11-05 (commit 10af421) | `c37eac3938c3cd72d73c7a36924ad37da189636ce63a7e89ba13fb591e776d85` | sede page OEP 2023 y 2024; the page no longer links it |
| `examenes-oficiales/conv2024_modeloB_plantilla-definitiva.pdf` | not recorded; in the repo since 2026-11-05 (commit 10af421) | `e7a72fdfbd6d2f952fb15cbed2648f82099693de8250b825e0c42e47229bae1e` | sede page OEP 2023 y 2024; the page no longer links it |
| `examenes-oficiales/conv2024_extraordinario_cuestionario.pdf` | not recorded; in the repo since 2026-11-05 (commit 10af421) | `73f97967048ccd2be86deb92e49a81fbc1f436be06e7826521903d4d6c346f01` | sede page OEP 2023 y 2024; the page no longer links it |
| `examenes-oficiales/conv2024_extraordinario_plantilla-definitiva.pdf` | not recorded; in the repo since 2026-11-05 (commit 10af421) | `23356f9ef2e9ef7f4f64a4db1b69a94591adb1057bcf487b794a797ee4d43c06` | sede page OEP 2023 y 2024; the page no longer links it |

**The 12 files of 2024, 2022 and OEP 2020 match no live link** (decision, Juanjo 2026-11-05: record the page, the date and the sha256; no guessed URL). Each row names the INAP sede page of its convocatoria (full URLs in the list above: OEP 2023 y 2024, OEP 2021 y 2022, OEP 2020). Those pages now link only BOE resolutions, and the inap.es archive stops at OEP 2018. The site did not refuse access; the documents are no longer linked. The download date was not recorded when the files were added; the earliest date on record is the commit that added them.

## Normativa

- **Copied from C1:** 79 files (75 entries), same name and sha256; the build asserts it per file.
- **Downloaded fresh (7 files):**
  - Three norms boe.es consolidated after C1's snapshot (C1: up to 2026-10-03; boe.es now 2026-10-21), all by **Real Decreto-ley 31/2026, de 20 de octubre** (BOE-A-2026-21872, mejora de la acción protectora de la Seguridad Social): LGSS (RDL 8/2015), RDL 4/2000 (TR Seguridad Social de los Funcionarios Civiles) and RDL 670/1987 (TR Clases Pasivas). The RDL itself is also saved.
  - Three norms the C2 exams cite and C1 lacks: RD 210/2024 (estructura del MTDFP; 2025 part 2 reserve 4), Orden TDF/379/2024 (directivos públicos profesionales; 2024 part 1, 29), Orden PCM/1382/2021 (REG-AGE; 2024 part 2, 9).
- **C1 is now out of date for those three norms**, and its `cambios_pendientes` for Ley 4/2026 (effective 23-10-2026) have passed. Not touched (C1 is read-only for this round); a C1 currency audit should pick them up.
- **Cambio-pendiente (4 entries):** Reglamento del Congreso art. 23 (XVI legislatura); RD 366/2007 art. 13 (RD 707/2026, from 02-01-2027); LGSS arts. 144.4, 169.1.a), 171, 172 and 173.1 (from 01-12-2026) and art. 309 (from 01-01-2027); RDL 4/2000 art. 19.1 (from 01-12-2026, per the boe.es analysis). For the RDL 31/2026 entries I did not check whether the consolidated PDF already shows the future wording; `version_vigente.note` says so.
- **RDL 31/2026 needs convalidación** by the Congreso (art. 86.2 CE) within 30 working days of 21-10-2026. If it is derogated, the three Seguridad Social entries revert.

### Norms not verified or not located

- **RDL 14/2025** (retribuciones): as in C1, not in the consolidated collection; `unverified: true`.
- **Resolución de la SEFP de 7 de mayo de 2024** (adecuación de puestos a la DT 6.ª del RDL 6/2023; 2024 part 1, 30): not found on boe.es; an entry with `unverified: true` and no file. The key (C2: niveles 14–18) matches the RDL 6/2023 DT 6.ª, which the classifier quoted.
- **Resolución de 7 de mayo de 2014** (lists of interim staff; 2024 part 1, 18) and **the order regulating the Consejo de Desarrollo Sostenible** (2024 extr. part 1 reserve 1): cited by the exams, not in `sources/`, not added. Both questions are `dudosa` for that reason.
- **EU norms** (TUE, TFUE, Estatuto del TJUE, Reglamento interno del Consejo, RGPD): taken from C1 as they are, not re-verified this round.
- **Not added, on purpose:** repealed norms the exams cite (LO 15/1999 and RD 1720/2007 in OEP 2020 extr. part 1, 18; Ley 51/2003 named in a 2024 stem). «Real Decreto 203/2023» (2022 part 2, 9) is an erratum for RD 203/2021.
- **No norm for some programme items:** Agenda 2030 and Gobierno Abierto (I.6) rest on non-normative documents. C1 keeps them in `sources/otros/`; this course does not have them yet. The V Plan de Gobierno Abierto decided a ledger row (below).

## Microsoft pages (deliverable 4)

The literal test, «the live page still matches the stored sha256», cannot pass for any page. 0 of 182 C1 `ms-*` pages match byte for byte, because the HTML changes on every deploy: build hashes, tracking pixels, the `updated_at` meta. I compared the visible article text instead (`<main>` or `<article>`, scripts and tags removed). Of the 69 pages the classifiers relied on:

- **41 pages:** text identical, so copied from C1 (same sha256 as C1's file).
- **1 page** (`ms-copilot-introduccion.html`): text changed slightly; the fresh live copy is kept.
- **26 pages** (all on support.microsoft.com): the server answered HTTP 403 to the automated request. **Decision (Juanjo, 2026-11-05):** C1's copies of 2026-10-17 are accepted. They are copied with C1's sha256 (asserted per file) and marked `comprobacion: "live check pending (403 on 2026-11-05)"` in `sources/otros/fuentes.yaml`; the monthly currency audit retries them. I did not retry with browser-like headers: the session's permission check classified that as bot-check circumvention.
- **1 page dropped** (`ms-outlook-grupos-envio-recepcion.html`): the URL now serves another page (text similarity 0.13 with C1's copy). One question loses its saved source: OEP 2020 extr. part 2, 15 (Grupos de envío y recepción, classic Outlook only). It is `vigente` and «programa anterior»; a source must be found before a lesson or question relies on that feature.

`sources/otros/` now holds 68 pages, all listed in `fuentes.yaml`. The per-page table is in section 7 of the ofimática index.

`ms-word-atajos.html` lists US-keyboard shortcuts. It is not a source for Spanish shortcuts: a classifier relied on it once, and I reversed that row (2022 part 2, 35; see below).

## Ledger: decisions

Status rules as C1's. Decided by Juanjo on 2026-11-05:

- **2025 part 2, 6 → `norma modificada`, stands.** Ley 4/2026 (in force 23-10-2026) replaced the RDL 1/2013 art. 2.j) definition of «inclusión social» that the stem copies; it is now «Inclusión: proceso o estado irrenunciable…». The only 2025 question excluded.
- **2022 part 1, 12 → `norma modificada`, stands.** The V Plan de Gobierno Abierto 2025-2029 abolishes the axes («se suprimen los ejes, que quedan integrados en los compromisos», C1's `transparencia-v-plan.pdf`), as in C1's conv2022 P1 29.
- **2022 part 2, 35: the classifier's dispute is rejected, stands.** `ms-word-atajos.html` gives US shortcuts, so the row stays `vigente` with an «atajo sin confirmar en la interfaz española» note.
- **2024 extr. part 2, 29 and 30 → `vigente-con-nota` «Clave oficial discutida».** 29 d «Firma, Etiqueta y Mensaje» (only sender and recipient are required; c is nearest); 30 a «Tabla de envío» (the feature is «Grupo de contactos», d). The sheet does print d and a, and 31–33 are right, so it is not a shifted column. The note says the sheet may belong to another model of the extraordinario.
- **OEP 2020 sets are «programa anterior»**, as in C1 (R3.4). Their questions keep their classification against the 2025 programme and go into the practice set by status, but never into tema counts. The ledger headings, the per-tema tables of the style guide and the ofimática index show the 2020 columns marked «programa anterior», with totals over 2022–2025. The style guide's summary of tema weights was recomputed on those four exams.

Unchanged from the first handoff, for the record:

- **2024 extr. part 2, 2:** the key c («Se utilizarán siglas o abreviaturas») contradicts RD 366/2007 art. 13.1. Disputed; the correct option is d (art. 13.2), and that holds after RD 707/2026.
- **Other disputed keys.** Part 2: 2024 part 2, 18 (Vínculo móvil and iPhone photos); 2024 extr. part 2, 9 (PAG described as covering all administrations and the EU). Psicotécnicos: 2022 part 1, 39 (operators evaluated left to right); 2022 part 1 reserve 5 (rounds against days); 2020 part 1, 55 and 2020 extr. part 1, 39 (two analogies with more than one pair breaking the relation).
- **`dudosa` (3):** 2024 part 1, 18 and 2024 extr. part 1 reserve 1 (norms absent, above); 2022 part 2, 13 (the «latest Android version» has expired).
- **`función retirada` (6):** WordPad, Asistente de concentración, «Presentar en línea», Reconocimiento de voz de Windows, the Explorer ribbon's «Mover a», Visor 3D. Same calls as C1 where the questions overlap.
- **Keys not checkable from `sources/`** (16; the list is in the ledger notes and `key_check`). Among them 2024 extr. part 2, 11 (Word 3D models): it is vigente by reasoning, but d may also be right if the 3D-model pane offers a background fill.
- **Tema assignment.** 58 of 525 knowledge questions have a second plausible tema, in brackets in the ledger. The common overlaps are II.7/II.6 (Explorador against Windows, 9), II.12/II.5 (5), II.4/I.11 (administración electrónica against LPAC, 5) and II.5/II.6 (3). The per-tema tables use the first tema only.
- **Classification fields** (stem form, option type, distractor, psicotécnico difficulty) are one reader's judgement per question; the guide uses them for proportions only.
- **Psicotécnicos.** The computed answers match 192 of 193 non-annulled keys. Two official options truncate instead of rounding (2020 part 1, 41 and reserve 2); still the only close option, so kept `vigente`. Unwritten conventions the tribunal applies (operators left to right; the Ñ counted in letter series; «Proyector y Megafonía» counts as projector) are in the index: the generators must decide whether to copy or avoid them.

Distinct counts after the decisions (unchanged): vigente 681, vigente-con-nota 17, anulada 10, norma modificada 3, función retirada 6, dudosa 3, fuera de temario 0.

## Exam rules (confirmed by Juanjo, 2026-11-05)

From Anexo I and the CPS notes (`sources/programa.md`):

- **Software versions:** «Windows 11 y Microsoft 365 versión de escritorio» (Anexo I 2.2). It does not say Windows 10, and names no Microsoft 365 release or channel.
- **Time:** «noventa minutos» for the whole exercise, both parts together. No split per part.
- **Counts:** part 1, «un máximo de 60 preguntas» (30 bloque I + 30 psicotécnicas) + 5 reserve; part 2, «un máximo de 50 preguntas» + 5 reserve. Four options, one correct.
- **Penalty:** a wrong answer costs one third; blank costs nothing. Raw score A − E/3 per part (CPS criterios 2).
- **Minimums:**
  - Each part is graded 0–50 and needs 25 (Anexo I 2.3.1). Raw minimums may not be below 30 % of the maximum (2.3.2).
  - CPS criterios: part 1 apto at ≥ 50 % of 60, lowered if fewer than 4.632 (sistema general) / 468 (norma común 13) reach it, never below 30 %. Part 2: the best up to 1.544 / 156, never below 30 % of 50.
  - **Cut-offs fixed for 2025:** part 1 M = 29,00 (sistema general), 21,33 (cupo NC 13); part 2 M = 21,33 (general), 15,33 (NC 13). N = 60 and 50; E = 50 each. **R5 stores the sistema general cut-offs as exact fractions: part 1 M = 29, part 2 M = 64/3** (21,33 is 64/3 printed to two decimals; with the one-third penalty every raw score is a multiple of 1/3).
- **Transformation:** t(d) = E/2 × d/M below the cut-off; E/2 × (1 + (d − M)/(N − M)) at or above it (CPS note of 29-09-2026).
- **Order between parts:** part 2 is graded only if part 1 reaches the CPS minimum (2.3.1.a). Ties are broken by the part 2 mark first (2.3.3), the reverse of C1; irrelevant for the platform, which ranks no one.
- **Inconsistency in the BOE text:** 2.1 and 2.2 refer to «el programa recogido en el punto 5 del presente anexo»; the programme is point 3. Copied as printed and noted in `programa.md`.

## Open for the next round (R1)

- Decide the first psicotécnico batch: the index proposes the 13 recurring types, which also answers open decision 1 of the requirements.
- Add to `sources/otros/` what C1 has for I.6 (Agenda 2030, Gobierno Abierto, V Plan) before the theory round, with the same live check.
- Find a source for «Grupos de envío y recepción» (OEP 2020 extr. part 2, 15) if a lesson or question needs it; the page C1 used now serves another page.
- The monthly currency audit retries the 26 pages marked «live check pending (403 on 2026-11-05)».
- Confirm on a Spanish-locale Windows 11 / Microsoft 365 the «Etiqueta actual» notes marked «sin confirmar» and the Word shortcut of 2022 part 2, 35.
- R6.1 of the requirements lists psicotécnico types that no Auxiliar questionnaire of 2020–2025 asks: counting symbols, finding differences, error detection in copied data, spatial and logical reasoning. They have no official style to copy (psicotécnico index, section 2).
- C1 is out of date for LGSS, RDL 4/2000 and TRLCPE (RDL 31/2026) and its Ley 4/2026 `cambios_pendientes` have passed; a C1 currency audit should pick them up.
