# Handoff — age-administrativo-c1, round R0a (sources, programme, legislation, exam style)

2026-10-16; decisions applied 2026-10-17. Nothing committed. Nothing written under `es/`, `glossary/` or `exercises/`; no `course.yaml`.

## What this round produced

| File | Content | Counts |
|---|---|---|
| `content/age-administrativo-c1/sources/programa.md` | Anexo III of BOE-A-2025-26262 verbatim: exam rules (points 1–2.3.3), programme (point 3), plus norma común 11.1 (applicable legislation). | 6 bloques, 45 temas (11/4/7/9/6/8). All 74 paragraphs checked by script against the BOE text. |
| `content/age-administrativo-c1/sources/normativa.yaml` | Every norm the 45 temas rest on: short name, BOE title, BOE-A id, consolidated-text URL, consolidation date, temas, 2025–2026 amendments, notes. | 76 entries: 72 BOE, 4 EU (CELEX). 75 verified, 1 unverified. 33 with amendments published in 2025–2026. 38 of 45 temas tied to a norm; VI.2–VI.8 rest on none. |
| `docs/age-exam-style.md` | Style guide from the official questionnaires (2025 primary, 2024/2022/2020 secondary), reviewer checklist of 17 items, statistics per exam, questions per tema per exam. | 8 distinct questionnaires, 1,000 questions. |
| `docs/age-ofimatica-index.md` | Every bloque VI question indexed by application, feature family, feature, form, exam and number. Recurring and one-off families, programme features never asked, retired or changed features. | 242 questions: Windows 60, otros 35, Access 34, Outlook 31, Word 30, Excel 28, correo e Internet 24, PowerPoint 0, Teams/OneDrive/SharePoint 0. 55 families recur across at least two convocatorias. 11 questions on retired features. |
| `docs/age-official-exams-ledger.md` | Per questionnaire (10, modelo B included): number, tema (2025 programme), status, key as printed, «Nota de clave» (disputed key or «c Modificada» caveat), note. | 1,250 rows: vigente 1,140, vigente-con-nota 47, anulada 40, función retirada 12, norma modificada 9, dudosa 2, fuera de temario 0. Modelo B rows duplicate modelo A's. |

The working data behind these files (parsed questionnaires, per-question classification, scripts) is in the session scratchpad, not in the repo.

## Source files: all usable

All 25 PDFs are readable and complete. Every questionnaire has 70 + 5 + 2 × (20 + 5) questions, and every answer sheet matches its questionnaire: Q1 checked by hand everywhere, modelo A against B by stem and keyed text. Points to know:

- **Naming of `conv2019_*`.** These four files are the OEP 2020 exams (answer sheets: «Oferta de Empleo Público de 2020»; cover: «CUESTIONARIO 19 / ADVO–LI»), sat in 2022. They are called conv2020 in every doc of this round, as decided. The files keep their names until you rename them.
- **No questionnaire prints the exam date.** The 2025 dates come from the file names and R3.4. For the others the ledger gives only the PDF creation date.
- **2026-05-23 modelo B: misprint.** Part 1 has two questions numbered «66» and none «65». Numbered by position; the answer sheet says so itself («65. ANULADA (en el cuestionario aparece como pregunta 66)»). Recorded once in the ledger.
- **conv2022: «c Modificada».** The answer sheet prints «c Modificada» for part 1 question 7 and supuesto II questions 8 and 9. They stay as printed, «c (Modificada)», with a note that the graded text may differ from the printed questionnaire (decision of 2026-10-17).
- **conv2022 extraordinario: truncated options in the PDF itself.** Some options stop mid-word in the original («…del funcionamiento normal o anormal de los ser», reserve question 4, option a; checked against a render of page 7). Affected: part 1 question 55, reserve 4, supuesto I 14 and 18, supuesto II 6, 11 and 16. Recorded as printed.
- **Exam-sheet boilerplate in two PDFs.** In the conv2020 questionnaires the line «NO OLVIDE MARCAR EL SUPUESTO ELEGIDO EN LA HOJA DE EXAMEN» runs into option d of reserve question 5. It was removed from the parsed text; the PDFs are untouched.
- **Missing documents, not needed this round.** The 2024 and 2022 convocatorias are absent, so «Cambios entre convocatorias» was left out of `programa.md`, as decided.
- **Inconsistency in the BOE text.** Anexo III point 2.1 says the programme is «recogido en el punto 6 del presente anexo»; it is point 3. Copied as printed and noted at the top of `programa.md`.

## Norms not verified, or verified with a caveat

- **RDL 14/2025** (BOE-A-2025-24445, retribuciones): exists and its title was checked in the original text, but it is not in the consolidated collection (`act.php` and the API return 404). `unverified: true`.
- **EU norms** (TUE, TFUE, RGPD, Reglamento interno del Consejo): CELEX ids and in-force status checked in the EU Publications Office SPARQL endpoint, because EUR-Lex blocked automated access. Consolidation date read only for TUE/TFUE (2016-06-07); null for the RGPD and the Council's rules.
- **Dates.** `consolidated_as_of` is the «Última actualización publicada el» line on act.php, re-read for all 72 BOE entries. Six never-amended norms show no such line; the field carries their publication date, and the YAML header says so.
- **Points the manifest flags but did not resolve:**
  - boe.es gives Ley 1/2025's change to LCSP art. 202 and ET art. 15 an effect date before the law's publication.
  - Two norms each add a DA 57 to the LCSP (Ley 9/2025 and RDL 7/2026).
  - Some amendments of Ley 31/2022 (PGE 2023, prorrogados) have no entry-into-force date.
- **Already published, in force after today.** These change norms the bank will cite. The next exam will almost certainly fall after these dates.
  - Ley 4/2026, from 23-10-2026: TREBEP art. 49.e, Ley 38/2003 art. 2.4, LBRL, RDL 1/2013, Ley 39/2006 and others.
  - RD 813/2026, from 28-10-2026: art. 6 of RD 725/1989 and of RD 640/1987.
  - RD 707/2026, from 02-01-2027: art. 13 of RD 366/2007.
- **The R3.5 list was corrected and completed** from the programme and the exams. About 45 norms were added, for example RD 208/1996, RD 951/2005, RD 1708/2011, RD 366/2007, Ley 53/1984, LGSS, ET, Ley 38/2003, RD 887/2006, RD 725/1989, RD 640/1987, the Orden of 1-2-1996 on documentos contables and LO 1/2025. Left out on purpose: norms the exams name only as wrong options (RD 1494/2007, Ley 8/2021, RD 4/2010 and others) and repealed ones (Ley 6/1997).
- **The 2026 constitutional reform** (art. 69.3, BOE-A-2026-10881, in force 20-05-2026) and the 2024 one (art. 49, BOE-A-2024-3099) were confirmed on the BOE API.

## Decisions taken (2026-10-17) and how the ledger applies them

1. **Ministry names in supuesto keys.** These questions stay in the set with the official key and a «Denominación actual» note. There are ten: the nine supuesto questions plus conv2020 P1 8. Status `vigente-con-nota`. conv2020 extr. P1 31 stays `norma modificada`: it is a part-1 question whose answer itself changed.
2. **VUE and Cl@ve in 2022.** Kept under tema II.3. The ofimática index now says the 2022 exams placed them in the ofimática positions (2022 ord. 41, 2022 extr. 44 and 66).
3. **Gobierno Abierto.** Confirmed: conv2022 P1 29 `norma modificada`; conv2024 P1 8 and conv2024 extr. reserve 1 `vigente`.
4. **«Programa anterior».** Now R3.4 of the requirements (v1.3). The ledger says so for the conv2020 set.
5. **Changed labels.** The questions stay with an «Etiqueta actual» note giving the Windows 11 label; 11 questions are `vigente-con-nota`. Only `función retirada` is dropped (12 rows, 11 distinct questions).
6. **Disputed official keys.** The keys stay, with «Clave oficial discutida: …» in the new «Nota de clave» column and status `vigente-con-nota`. That covers 24 distinct questions (26 rows with modelo B). Three of them were `dudosa` before: conv2025 extr. reserve 2, conv2024 extr. P1 65 and conv2022 extr. S2 17. Four also carry a «Denominación actual» note.
7. **«c Modificada».** As printed, with the caveat note; `vigente-con-nota`.

Tribunal errata that do not affect the key are listed as «Errata: …» in the «Nota» column and do not change the status. Examples: a person renamed in the options, a law given the wrong title in a stem.

## Open after the decisions

- **Two questions are still `dudosa`.**
  - conv2022 extr. P1 22: Spain's seat on the OGP steering committee ended on 30-9-2026, and its renewal is not confirmed.
  - conv2020 extr. P1 17: the key is right today, but RD 707/2026 rewrites RD 366/2007 art. 13 from 02-01-2027. Under R3.5 (v1.3), the version in force on the 2027 exam applies, which would make this `norma modificada` with the tag `cambio-pendiente`. I left the status for your call.
- **R3.5 (v1.3) is not applied in this round's files.** `normativa.yaml` records only the version in force on 2026-10-16. It does not yet record the forthcoming versions with their dates: Ley 4/2026 from 23-10-2026, RD 813/2026 from 28-10-2026, RD 707/2026 from 02-01-2027. Nor was the ledger re-checked against them. Known contacts are conv2025 ord. P1 21 (Ley 38/2003 art. 2.4, gains a letter from 23-10-2026; the key holds by the per-exam pass's reading) and the TREBEP art. 49.e change. To do before or in R1.
- **R3.4 (v1.3) and the style guide.** The questions-per-tema table in `docs/age-exam-style.md` still has the two 2020 columns, marked «programa anterior». Under v1.3 they should not be there. Not changed, as instructed.
- **Statuses in the ofimática index.** `docs/age-ofimatica-index.md` was generated before these decisions. Its «Status» column still shows `dudosa` for conv2025 extr. reserve 2 and conv2024 extr. P1 65, and `vigente` for the label-changed questions. The ledger is the authoritative source for status.
- **Labels not confirmed.** Several «Etiqueta actual» notes say «Sin confirmar en la interfaz española». They come from the per-exam pass and need a check against a Spanish-locale Windows 11 before the practice set shows them.
- **Notes still to check.** The «Clave oficial discutida» reasons are the per-exam pass's reading. Each should be checked against the norm text before the set is published. conv2025 ord. S1 16 most of all: the 15 días naturales may come from the convocatoria bases.

**Tema assignment.** 217 of 1,000 questions have a second plausible tema, shown in brackets in the ledger. The common overlaps are:
- III.3 / III.2;
- IV.5 / IV.4;
- V.3 / V.5;
- III.4 / V.6;
- I.5 / I.8.

The questions-per-tema table in the style guide uses the first tema only.

**Classification fields.** Option type and distractor construction are one reader's judgement per question; the style guide uses them for proportions only.

## Not done in this round, by design

- The «Exámenes oficiales» practice set is not built; the ledger is its input.
- Nothing under `es/`, `glossary/` or `exercises/`, and no `course.yaml` (round R1).
