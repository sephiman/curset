# Handoff — age-administrativo-c1, round R1 (skeleton)

2026-10-16. Nothing committed. Requirements: `docs/age-administrativo-course-requirements.md` v1.3.

## What exists now

| Path | Content |
|---|---|
| `content/age-administrativo-c1/course.yaml` | Slug `age-administrativo-c1`, title «Administrativo del Estado (C1)», subtitle «Ingreso libre · convocatoria OEP 2026», `languages: [es]`, `status: draft`, `exercise_types: [quiz]`. Two blocks: `block-a` «Proceso de selección» (module `m00` «El examen», lesson `m00-l01` «Cómo es el examen») and `block-b` «Programa» (modules `m01`–`m06`, one per bloque I–VI, titled with the official bloque names; 45 lessons `mNN-lMM` = bloque NN, tema MM). |
| `content/age-administrativo-c1/es/lessons/m00-l01.md` | The intro lesson, written in full (about 910 words, 1,000 counting numbers). Anexo III rules, the CPS 2025 criteria, the 2025 cut-offs, the transformation formula with a worked example, tie-breaks, norma común 11.1. |
| `content/age-administrativo-c1/es/lessons/m01-l01.md` … `m06-l08.md` | 45 stubs: the tema title verbatim as `#`, a `:::note{type=info}` «Tema sin redactar.» marker, and `## Normativa` pre-filled from `normativa.yaml`. |
| `content/age-administrativo-c1/glossary.yaml` | `terms: []`. |
| `content/age-administrativo-c1/exercises/.gitkeep` | Empty folder. The loader needs no index file. |
| `content/age-administrativo-c1/glossary-links.es.txt`, `lesson-refs.es.txt` | Generated goldens. Both are empty: 0 marks and 0 references. |
| `content/age-administrativo-c1/sources/normativa/` | 79 files, 46 MB. 71 BOE consolidated PDFs, the PGE 2023 as HTML, the RDL 14/2025 original, 3 EU texts, and the 4 amending norms. No `DOWNLOAD.md`, because every download worked. |

### Choices to check

- **Titles.** Lesson titles are the full tema paragraph, as in `programa.md`. The BOE gives no shorter title. Module titles are the bloque names without the roman numeral. The PDF and the course tree show them as `M01 · Organización del Estado y de la Administración pública`, so `M0N` is bloque N.
- **Block names.** The course model needs a level above modules. «Proceso de selección» (Anexo III point 2) and «Programa» (point 3) are the BOE's own headings.
- **Summaries.** All 51 summaries (6 modules + 45 lessons) are the placeholder «Resumen pendiente.». The intro is the exception. Its module and lesson carry a real summary of three sentences at most, because the lesson is written.
- **Normativa block.** It lists every norm whose `temas` in `normativa.yaml` names the tema, using the yaml's `short` name. Article ranges appear only where the programme names a part of the norm: 29 norm–tema pairs (CE, LRJSP, LBRL, TUE, TFUE, LPAC, RGPD, LJCA, Código Civil, TREBEP). Each range was checked against the título/capítulo structure of the downloaded consolidated text. One was corrected: RGPD «capítulos II a IV» became «arts. 5–39 y 51–59», because chapter IV runs to art. 43. A norm with `cambio-pendiente` carries «Cambio pendiente: <norm>, en vigor el <date> (<precepts>).»; the precepts are omitted when there are more than three. They sit in parentheses because a line ending «art. 23.» reads as a numbered-list marker to the list-shape guard. VI.2–VI.8 say «Este tema no se apoya en ninguna norma.».
- **The intro lesson's Normativa block** cites the convocatoria (BOE-A-2025-26262), not `normativa.yaml`. The CPS notes are cited in the prose, not listed as norms.
- **glyph / color.** The repo documents no placeholder value, and the schema (`extra="forbid"`) rejects both keys. `course.yaml` carries a comment saying the identity round adds them.
- **exams.** No exam-presets schema exists (`docs/exam-presets-handoff.md` is absent, and `ManifestCourse` has no `exams` field). `course.yaml` ends with an `# exams:` comment listing the R7.1 presets.
- **Generator.** `course.yaml` and the stubs were written by a one-off script from `programa.md` and `normativa.yaml`. The script lives in the session scratchpad, not the repo. R2 edits the files by hand.

## Normativa block: norms listed without an article range

The «29» above counts norm–tema pairs, not temas. The 45 stubs list 127 norm–tema pairs; 29 carry an article range and 98 give the norm alone. By tema:

- **Every norm has a range (4):** I.2, I.9, I.10, III.2.
- **No norm (7):** VI.2–VI.8. These say «Este tema no se apoya en ninguna norma.».
- **At least one norm without a range (34):** in the table. R2 replaces each of these with the articles the written lesson cites (R4.4).

Most gaps are by design: the programme does not name a part of the norm. Five are not: a range exists, but I did not check it against the text, so I left it out (II.4, III.1, IV.9, V.1, V.2).

| Tema | With a range | Norm alone | Why no range |
|---|---|---|---|
| I.1 | CE: arts. 10–55 (título I), 159–165 (título IX) y 166–169 (título X) | LO 2/1979 (LOTC); LO 3/1981 (Defensor del Pueblo) | supporting norms, cited for specific points the programme does not name |
| I.3 | CE: arts. 66–96 (título III) | Reglamento del Congreso; Reglamento del Senado | the Reglamentos are the source of «funcionamiento», which the programme does not tie to a part |
| I.4 | CE: arts. 117–127 (título VI) | LOPJ (LO 6/1985); Ley 38/1988 (Demarcación y Planta); LO 1/2025 (eficiencia de la Justicia) | supporting norms, cited for specific points the programme does not name |
| I.5 | CE: arts. 97–107 (título IV) y 108–116 (título V) | Ley 50/1997 (Gobierno) | «Las funciones del Gobierno» spans the whole Ley 50/1997 |
| I.6 | — | Ley 19/2013 (transparencia) | the Gobierno Abierto and the Agenda 2030 rest on plans and a UN resolution, not on this law |
| I.7 | — | Ley 19/2013 (transparencia); RD 615/2024 (Estatuto del CTBG) | the tema is the whole Ley 19/2013; the CTBG Estatuto is a supporting norm |
| I.8 | Ley 40/2015 (LRJSP): arts. 54–80 (título I) | Ley 2/2014 (Acción y Servicio Exterior); Ley 3/2015 (alto cargo); RD 829/2023 (departamentos ministeriales); RD 1009/2023 (estructura orgánica básica) | supporting norms, cited for specific points the programme does not name |
| I.11 | TUE: arts. 13–19 (título III); TFUE: arts. 223–281 | Reglamento interno del Consejo | cited for specific points (seat, sessions) |
| II.1 | — | RD 208/1996 (información administrativa); RD 951/2005 (calidad;  quejas y sugerencias); RD 366/2007 (accesibilidad ante la AGE); LO 4/2001 (derecho de petición); RDL 1/2013 (TR derechos personas con discapacidad); Ley 39/2015 (LPAC) | the subject is spread over scattered articles, not one título or capítulo |
| II.2 | Ley 39/2015 (LPAC): arts. 16–17 | RD 1708/2011 (Sistema Español de Archivos); Ley 16/1985 (Patrimonio Histórico); RD 203/2021 (Reglamento de actuación por medios electrónicos) | supporting norms, cited for specific points the programme does not name |
| II.3 | — | Ley 40/2015 (LRJSP); Ley 39/2015 (LPAC); RD 203/2021 (Reglamento de actuación por medios electrónicos); Orden HAP/1949/2014 (PAG); RD 127/2015 (ventanilla única empresarial); RD 1112/2018 (accesibilidad web) | the subject is spread over scattered articles, not one título or capítulo |
| II.4 | RGPD (Reglamento (UE) 2016/679): arts. 5–39 y 51–59 | LOPDGDD (LO 3/2018) | LOPDGDD: a range exists but I did not check it against the text, so I left it out |
| III.1 | CE: arts. 9.3, 81–86 y 97; Ley 39/2015 (LPAC): arts. 127–133 (título VI); Código Civil: arts. 1–7 | Ley 50/1997 (Gobierno) | Ley 50/1997 (título on the potestad reglamentaria): a range exists but I did not check it against the text, so I left it out |
| III.3 | Ley 39/2015 (LPAC): arts. 1–2 y 53–126 (títulos IV y V); LJCA (Ley 29/1998): arts. 18–30 | LO 1/2025 (eficiencia de la Justicia); Ley 40/2015 (LRJSP) | supporting norms, cited for specific points the programme does not name |
| III.4 | — | LCSP (Ley 9/2017) | the tema walks the whole life of a contract across the LCSP |
| III.5 | — | Ley 40/2015 (LRJSP); LCSP (Ley 9/2017); Ley 60/2003 (Arbitraje); Ley 38/2003 (General de Subvenciones) | the subject is spread over scattered articles, not one título or capítulo |
| III.6 | Ley 40/2015 (LRJSP): arts. 32–37 | Ley 39/2015 (LPAC); LO 3/1980 (Consejo de Estado) | the LPAC rules for responsabilidad patrimonial are scattered special rules |
| III.7 | — | RDL 1/2013 (TR derechos personas con discapacidad); LO 3/2007 (igualdad); LO 1/2004 (violencia de género); Ley 4/2023 (trans y LGTBI); Ley 15/2022 (igualdad de trato); Ley 39/2006 (dependencia) | the programme names the norm or its subject as a whole, not a part of it |
| IV.1 | TREBEP (RDL 5/2015): arts. 1–13 (títulos I y II) | Ley 30/1984 (reforma de la Función Pública); RD 1405/1986 (Registro Central de Personal) | supporting norms, cited for specific points the programme does not name |
| IV.2 | CE: arts. 23.2 y 103.3; TREBEP (RDL 5/2015): arts. 55–62 y 70 | RDL 1/2013 (TR derechos personas con discapacidad); RD 364/1995 (Reglamento General de Ingreso y Provisión); RD 2271/2004 (empleo público y discapacidad); RDL 6/2023 (medidas urgentes;  función pública) | supporting norms, cited for specific points the programme does not name |
| IV.3 | TREBEP (RDL 5/2015): arts. 9–10 y 55–62 | RD 364/1995 (Reglamento General de Ingreso y Provisión) | supporting norms, cited for specific points the programme does not name |
| IV.4 | TREBEP (RDL 5/2015): arts. 62–68 y 85–92 | Ley 30/1984 (reforma de la Función Pública); RD 365/1995 (situaciones administrativas) | supporting norms, cited for specific points the programme does not name |
| IV.5 | TREBEP (RDL 5/2015): arts. 14–20, 52–54 y 78–84 | Ley 30/1984 (reforma de la Función Pública); RD 364/1995 (Reglamento General de Ingreso y Provisión); RDL 6/2023 (medidas urgentes;  función pública) | supporting norms, cited for specific points the programme does not name |
| IV.6 | TREBEP (RDL 5/2015): arts. 93–98 (título VII) | Ley 53/1984 (incompatibilidades); RD 598/1985 (incompatibilidades, desarrollo); RD 33/1986 (Reglamento de Régimen Disciplinario) | the incompatibility and disciplinary rules are covered whole |
| IV.7 | — | Ley 40/2015 (LRJSP); RDL 4/2000 (TR Seguridad Social Funcionarios Civiles); RD 375/2003 (Reglamento General del Mutualismo Administrativo); RDL 670/1987 (TR Clases Pasivas); LGSS (RDL 8/2015) | the programme names the norm or its subject as a whole, not a part of it |
| IV.8 | TREBEP (RDL 5/2015): arts. 7 y 11 | Ley 53/1984 (incompatibilidades); ET (RDL 2/2015); IV Convenio único AGE | the programme names the norm or its subject as a whole, not a part of it |
| IV.9 | — | LGSS (RDL 8/2015) | LGSS «acción protectora»: a range exists but I did not check it against the text, so I left it out |
| V.1 | CE: arts. 134–135 | LGP (Ley 47/2003); LO 2/2012 (Estabilidad Presupuestaria) | LGP and LO 2/2012 principles: a range exists but I did not check it against the text, so I left it out |
| V.2 | — | LGP (Ley 47/2003); Ley 31/2022 (PGE 2023, prorrogados) | LGP modifications of credits: a range exists but I did not check it against the text, so I left it out |
| V.3 | — | LGP (Ley 47/2003); LO 2/1982 (Tribunal de Cuentas); Ley 7/1988 (Funcionamiento del Tribunal de Cuentas); RD 2188/1995 (control interno IGAE); Orden de 1 de febrero de 1996 (documentos contables); Orden PRE/1576/2002 (pago de obligaciones) | the subject is spread over scattered articles, not one título or capítulo |
| V.4 | TREBEP (RDL 5/2015): arts. 21–30 | Ley 30/1984 (reforma de la Función Pública); IV Convenio único AGE; Ley 31/2022 (PGE 2023, prorrogados); RD 462/2002 (indemnizaciones por razón del servicio); Orden de 30 de julio de 1992 (confección de nóminas); RDL 14/2025 (retribuciones sector público) | the subject is spread over scattered articles, not one título or capítulo |
| V.5 | — | LGP (Ley 47/2003); Orden de 1 de febrero de 1996 (documentos contables); Orden PRE/1576/2002 (pago de obligaciones); RD 725/1989 (anticipos de caja fija); RD 640/1987 (pagos a justificar) | the subject is spread over scattered articles, not one título or capítulo |
| V.6 | — | LCSP (Ley 9/2017); Ley 38/2003 (General de Subvenciones); Orden de 1 de febrero de 1996 (documentos contables); RD 887/2006 (Reglamento de Subvenciones) | the programme names the norm or its subject as a whole, not a part of it |
| VI.1 | — | ENS (RD 311/2022) | the ENS is cited only for concepts |


## Pipeline changes

- `backend/tests/pipeline_courses.py` and `frontend/src/test/courseContent.ts` (`GOLDEN_COURSES`) now cover every course under `content/`, drafts included, plus the published fixtures. Before this round they covered published courses only, so a draft course was loaded but never checked. `fixture-borrador` stays out, because it is a fixture for «a draft is served to nobody».
- New test in `frontend/src/lib/pdf/render.test.ts`, «the draft course %s». It prints each draft course end to end with pdfmake and checks four things:
  - capture is never called;
  - the export logs `<slug>: no figures` and `<slug>: no exercise charts`;
  - the lesson entries of the table of contents equal the manifest's 46 titles, in order;
  - the PDF has more pages than lessons.
- README «Courses, languages and reports» and `content/README.md` (the `sources/` folder) are updated.

Results: see «Suites» at the end.

## Normativa (R3.5)

`normativa.yaml` keeps its 76 entries and existing fields. Each entry gains four fields, documented in the header:
- `file`: the downloaded text;
- `tags`;
- `version_vigente`: `consolidated_as_of` plus an optional note;
- `cambios_pendientes`: norma, boe_id, precepto_modificador, publicada, en_vigor, articulos, and file (the amending norm's own text).

The header states the citation rule: where a norm has `cambio-pendiente`, lessons and questions cite the later version.

**12 norms carry `cambio-pendiente`:**

| Norm | Amending norm | In force | Precepts of this norm |
|---|---|---|---|
| LBRL | Ley 4/2026 (BOE-A-2026-20528), DF 3 | 23-10-2026 | art. 25.2.q) (new), 69.1 |
| Ley 16/1985 | Ley 4/2026, DF 4 | 23-10-2026 | DA 12 (new) |
| Ley 38/2003 | Ley 4/2026, DF 7 | 23-10-2026 | art. 2.4.j) (new). Asked in 2025 (conv2025 ord. P1 21) |
| ET | Ley 4/2026, DF 10 | 23-10-2026 | art. 37.6 |
| TREBEP | Ley 4/2026, DF 11 | 23-10-2026 | art. 49.e), new paragraphs 5.º and 6.º |
| LGSS | Ley 4/2026, DF 12 | 23-10-2026 | art. 190.5 (new), 363.1.d) (new paragraph) |
| RDL 1/2013 | Ley 4/2026, art. 1 | 23-10-2026 | about 45 precepts, listed in the yaml |
| Ley 39/2006 | Ley 4/2026, art. 2 and DA 3 | 23-10-2026 | about 50 precepts. The DA 3 change («actividades básicas de la vida diaria» → «actividades de la vida diaria») touches the definition of dependencia that the exams ask about |
| RD 725/1989 | RD 813/2026 (BOE-A-2026-20915), art. 2 | 28-10-2026 | art. 6.3 (new) |
| RD 640/1987 | RD 813/2026, art. 1 | 28-10-2026 | art. 6 |
| RD 366/2007 | RD 707/2026 (BOE-A-2026-18509), DF 1 | 02-01-2027 | art. 13 |
| Reglamento del Congreso | Reforma de 23-07-2026 (BOE-A-2026-16353) | XVI legislatura. RD 806/2026 dissolved the Cortes; elections on 29-11-2026, constitutive session on 23-12-2026 | art. 23 (Grupo Parlamentario) |

**Why these are tagged.** The exam date is unknown and will fall in 2027. Every one of these changes takes effect before 2027 or at its very start. The Reglamento del Congreso change was the only one not already known. Its date became concrete with the dissolution of the Cortes.

**Checked and not tagged:**
- RDL 30/2026: «dictado en relación con» LO 2/2012; it is not an amendment.
- RDL 25/2026: already in force.
- RDL 21/2026: repealed.
- The 16-10 erratum to RD 707/2026: preamble only.
- The staggered LGSS effects from RDL 2/2023: transitional rules inside the text, not pending amendments.

**Method.** The BOE API `analisis` was read for all 72 BOE norms, and the BOE sumarios of 1–16 October 2026 were scanned.

**Ley 4/2026 also amends norms outside the list** (LPH, LCS, LISOS, LIRPF, LEC and others). None of them is in the programme.

### Files and versions

- **Two versions in one file — only in two files.** *(Corrected in R2, 2026-10-16, after checking every cambio-pendiente file.)* Where boe.es has already merged the future change, the PDF prints the new wording. Two files, RD 366/2007 and the Reglamento del Congreso, also print «Téngase en cuenta que esta actualización … entra en vigor …» followed by «Redacción anterior», which is the text in force today. The ten files amended by Ley 4/2026 (LBRL, Ley 16/1985, Ley 38/2003, ET, TREBEP, LGSS, RDL 1/2013, Ley 39/2006) or RD 813/2026 (RD 725/1989, RD 640/1987) carry the new wording only: no notice of its entry into force and no «Redacción anterior». For those, the text in force today is not in the downloaded file. The `version_vigente` notes in `normativa.yaml` now say so. No separate file of the version in force today was downloaded.
- **Filename dates.** The date in each name is the «Última modificación» printed in the PDF. It equals `consolidated_as_of` in all 71 cases.
- **Ley 31/2022 (PGE 2023)** is `act.php` HTML (2.8 MB), because its PDF is 135 MB. Its annex tables are linked images and are not in the file.
- **EU texts.** These come from the DOUE copies on boe.es/doue, because EUR-Lex and the cellar block automated access. None is consolidated:
  - TUE and TFUE: one file, the 2016 consolidated versions (C 202);
  - RGPD: the original (L 119), without later corrigenda;
  - Council Rules of Procedure: the original (L 325, 2009), without the yearly annex III updates.
  The names use `CELEX-<id>` instead of a BOE id.
- **Largest file:** the Orden of 1-2-1996 (documentos contables), 8 MB. All 46 MB go into the repo as asked. Consider Git LFS before committing.

## Ofimática index against the ledger (step 2)

The «Status» column of `docs/age-ofimatica-index.md` was rebuilt from `docs/age-official-exams-ledger.md`. All 242 index rows have a ledger row. Modelo A and B agree in every case.

**17 rows disagreed. In every case the index was stale and the ledger right:**

| Exam | Nº | Feature | Index → ledger |
|---|---|---|---|
| 2025 ord. (A/B) | 45 | Notificaciones | vigente → vigente-con-nota |
| 2025 extr. | 53 | Coautoría en Word para la Web | vigente → vigente-con-nota |
| 2025 extr. | 55 | Plantilla .dotm | vigente → vigente-con-nota |
| 2025 extr. | P1R 2 | Gráficos modernos | dudosa → vigente-con-nota |
| 2024 extr. | 52 | Unidad de recuperación | vigente → vigente-con-nota |
| 2024 extr. | 55 | Explorador: Ordenar por | vigente → vigente-con-nota |
| 2024 extr. | 56 | Menú contextual: Enviar a | vigente → vigente-con-nota |
| 2024 extr. | 57 | Buscar en Windows: ubicaciones | vigente → vigente-con-nota |
| 2024 extr. | 58 | Historial de archivos | vigente → vigente-con-nota |
| 2024 extr. | 65 | Búsqueda instantánea | dudosa → vigente-con-nota |
| 2024 extr. | 70 | Menú Inicio: anclados | vigente → vigente-con-nota |
| 2022 ord. | 54 | SIERROR | vigente → vigente-con-nota |
| 2022 extr. | 45 | Escritorios virtuales | vigente → vigente-con-nota |
| 2022 extr. | 62 | Compactar y reparar | vigente → vigente-con-nota |
| 2020 ord. | 44 | Sistema > Acerca de | vigente → vigente-con-nota |
| 2020 ord. | 46 | Explorador: diseño Detalles | vigente → vigente-con-nota |
| 2020 ord. | 49 | Explorador: Acceso rápido | vigente → vigente-con-nota |

**Why they changed:**
- 11 are «Etiqueta actual» label changes (R0a decision 5).
- 6 are disputed keys (R0a decision 6): 2025 extr. 53, 55 and P1R 2; 2024 extr. 65; 2022 ord. 54; 2022 extr. 62.

**Other changes in the index:**
- **Header sentence.** In «Changed, key still holds», «(status `vigente`, with a note)» now reads «(status `vigente`, or `vigente-con-nota` where the ledger gives the current label or disputes the key)».
- **Counts.** No count in the index depends on status. The «Retired» table (11 questions, `función retirada`) was already consistent and is unchanged.

## Ledger against the 12 cambio-pendiente norms

All 10 questionnaires were split into questions. They were searched by norm name and by the subject of each affected precept. The rows of I.3, I.10, II.1, III.7 and IV.9 were also read one by one. Each hit was read against the new wording in the amending norm.

**Questions that rest on an affected precept:**

| Question | Precept | Verdict |
|---|---|---|
| conv2025 A and B, P1 21 (V.6) | Ley 38/2003 art. 2.4, new letter j), from 23-10-2026 | Key c) holds. Letter j) adds ayudas económicas de emergencia o urgencia social. No option states it, and letter g) (beneficios fiscales) is unchanged. «Revisado R1» note added. |
| conv2020 extr. P1 17 (II.1) | RD 366/2007 art. 13, from 02-01-2027 | Exclusion confirmed. The keyed «versiones simplificadas» is gone from the new art. 13. Status is now `norma modificada: RD 366/2007 art. 13 (cambio-pendiente, desde 02-01-2027)`. |
| conv2024 extr. P1 reserva 2 (III.7) | RDL 1/2013 art. 2, from 23-10-2026 | Key b) holds. Letter i) is unchanged. Distractors a) and c) are the old wordings of h) and j), and they stay wrong. «Revisado R1» note added. |
| conv2025 A S1 17 / B S2 17 (IV.5) | TREBEP art. 49, from 23-10-2026 | Key c) holds. Only letter e) changes; the fifteen-day preaviso of letter c) does not. «Revisado R1» note added. |

**Not affected:**
- About 25 caja fija and «a justificar» questions. None asks how funds are disbursed (art. 6).
- The other RD 366/2007 questions: conv2020 P1 10; conv2020 extr. P1 20 and S2 9; conv2024 extr. S1 5; conv2022 P1 3.
- LBRL questions on arts. 11, 19, 20, 32 and 121.
- LGSS questions on arts. 42, 44, 46 and 215.
- Two archive questions that rest on RD 1708/2011, not on the new DA 12 of Ley 16/1985.

No question asks about Reglamento del Congreso art. 23, ET art. 37.6, TREBEP art. 49.e) or any Ley 39/2006 precept.

**Counts.** No key changes for a new reason, so the summary table does not move:

| vigente | vigente-con-nota | anulada | norma modificada | función retirada | dudosa | fuera de temario |
|---|---|---|---|---|---|---|
| 1,140 | 47 | 40 | 10 | 12 | 1 | 0 |

A per-section script recount matches the table. The ledger header now gives the date format «(cambio-pendiente, desde DD-MM-YYYY)» and explains the «Revisado R1» note. A line under the summary records this review.

**Limit.** The search runs on keywords. A question that tests a changed rule without naming the norm or its subject could be missed. The row-by-row reading of the most affected temas found none.

## Open, for R2 and later

- **Write against the later version.** R2 lessons on these temas must cite it:
  - I.3: Reglamento del Congreso art. 23;
  - I.10: LBRL;
  - II.1: RD 366/2007 and RDL 1/2013;
  - II.2: Ley 16/1985;
  - III.5 and V.6: Ley 38/2003;
  - III.7: RDL 1/2013 and Ley 39/2006;
  - IV.1–IV.6, IV.8 and V.4: TREBEP;
  - IV.7 and IV.9: LGSS;
  - IV.8: ET;
  - V.5: RD 725/1989 and RD 640/1987.
- **The intro lesson follows the 2025 convocatoria.** R0b updates it when the OEP 2026 convocatoria is published, and with it the cut-off table and the CPS criteria.
- **Unchanged from R0a:**
  - RDL 14/2025 is still `unverified` (no consolidated text);
  - the RGPD and the Council's rules have no consolidation date;
  - the «Etiqueta actual» labels still need a check against a Spanish-locale Windows 11.
- **Step 7 of the round prompt was cut off** after «and anything in the». The follow-up session settled it as the Normativa mapping gaps, now in their own section above.

## Suites

- **Backend (`uv run pytest`):** 1,374 passed, 20 skipped. The «figure steps per course» section reads:
  - `age-administrativo-c1: no figures`
  - `crypto-futures: 34 figures`
  - `fixture-oposiciones: no figures`

  Run again on the final tree in the follow-up session: 1,374 passed, 20 skipped, same three lines.
- **Frontend (`npx vitest run`):** 563 passed, 49 skipped. `tsc -b` is clean.
- **Lint:** `ruff check`, `ruff format` and `mypy` are clean on `pipeline_courses.py`.
- **crypto-futures goldens:** byte-identical (no diff under `content/crypto-futures/`).
- **Android bundle:** re-exported with the same fingerprint `9c95cf4a…` (98 files), and `--verify-only` is OK.
