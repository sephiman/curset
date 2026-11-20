# Final comparison — Agentes de la Hacienda Pública (C1) course vs the benchmark syllabus

2026-11-19 · requirement R4.10 («Comparison»), R4.13 · working notes: `docs/age-verification/aeat/comparison/` (notes, adjudication, tools, log).
Not committed. No text of the benchmark appears here: topics and article numbers only.

**What was compared.** The course `aeat-agentes-hacienda` (32 lessons, state after edition step 2) against the benchmark syllabus kept in `notcommit/`
(a commercial syllabus, publisher's copyright line 2024), tema by tema, the same way for both texts. «Course» and «Other» below.

## 1. Headline numbers

| Measure | Course | Other |
|---|---|---|
| Words, prose (32 temas) | 257,536 | 222,936 |
| Words, esquema / table rows | 138,145 | 8,608 |
| Words, glossary · source lists | 4,370 · 3,690 | 0 · 0 |
| Exam coverage: vigente official questions (OEP 2022–2025) answered by the text alone | 446 / 452 (98.7%) | 326 / 452 (72.1%) |
| Errors against the norm (confirmed by opus) | 5 (none a false rule; see §4) | 145 |
| Topics inside the epígrafes the text lacks | 343 (of which 40 asked by some official question; 259 already in reserve/pool, 84 to write) | 299 |
| Reader preference (160 blind pairs, 5 per tema) | 90 (56%) | 67 (42%); 3 equal |

Reading it:
- **Coverage and accuracy favour the Course clearly** (446 against 326 of 452 questions; 5 against 145 confirmed errors). The Other is a 2024 edition and cannot reflect the 2025–2026 changes.
- **Size.** The Course's prose is 1.16× the Other's; counting esquemas it is 1.71×.
- **Missing topics are the Course's open flank**: 343 concepts inside the epígrafes that the Other treats; 259 of them have verified sentences in reserve/pool, 84 would have to be written; 40 were asked by an official question at some time.
- **Understanding is closer than the rest** (90 to 67). Where the Other won, readers named completeness in 52 of 67 pairs (22 on that alone); the rest is a handful of teaching devices (§6). The pair texts were cut at 700 words, which favours the more compact side (§7).

## 2. Method, decisions, what could not be read

Rules: R4.13 (no benchmark text in any committed file), R4.10, R4.7. Models: sonnet for the 32 analysts and 4 blind readers; opus for every adjudication against a norm (6 runs) and for the blind re-check of 10 % of the coverage verdicts.

**Decisions taken** (also in `log.md`):
- Mapping: the benchmark's «Bloque I / II / III – Tema n» files are programme temas I.n, II.n, III.n (titles checked). Its annexes attach to their tema.
- Not read: `EXTRA TREBEP.docx`, `Apuntes Organizacion AEAT NO IMPRIMIR.docx` and `Plazos en Derecho Tributario.xlsx` are 0-byte files. Image-only annexes (BI T1 Anexo, BI T3 Anexo 2, BI T4 Anexo 2, BIII T3 Anexo, BIII T9 Anexo 2) were rasterised and read visually (no OCR language data on this machine). Some tables inside tema PDFs are images too (III.4 three tables, III.6 sections 4.1, 4.2 and 5.2, III.14 §4.7 diagram): not counted, so the Other's words and its coverage in those places are lower bounds.
- `BOE TREBEP.pdf` and `BOE 39_2015.pdf` are legal texts, not syllabus: not counted. `Casos practicos *.pdf` (five files) are second-exercise practice and outside this first-exercise comparison.
- «Vigente» question = ledger estado `vigente` or `vigente-con-nota`, OEP 2022–2025 plus the 2022 extraordinario, 452 questions; the tema is the ledger's first tema. OEP 2020–2021 texts are not in the package: «asked by an official question» for those two convocatorias rests on the ledger's keys and the analysts' notes.
- A question counts as answered only on a clear Y (fact stated and correct, judged against the official key and the norm; discussed keys judged on the norm).
- Words: prose excludes headings, esquema blocks, `Término` lines, lead source bullets and `## Normativa`. The Other was counted by a script corrected by hand per tema (±5 %).
- The Other is a 2024 edition: a fact that changed later is not «correct».
- 10 % re-check: 91 verdicts sampled by part (15 / 13 / 63, seed in the log) and re-read by opus without the sonnet verdict: 3 disagreements (all on the Other, two N→P, one P→Y). No part exceeds one in ten, so measure 2 stays on sonnet.
- Adjudication downgraded several analyst «confirmed» items to omissions, rejected Course errors the analysts had flagged (III.7 art. 125.2 LGT, III.16 full stop, III.20 UK in the CAU list, III.2 ministry name) and left some disputes NORM_NOT_AVAILABLE (case law, orders not in `sources/normativa/`) or UNRESOLVED (III.8 D4, III.9 integridad rule); those are not counted as errors for either text.


## 3.1 Part I — Organización del Estado y funcionamiento de la AGE

Words: Course prose / esquema · Other prose / tables. Coverage: answered / vigente questions. Accuracy: confirmed errors, Course · Other. Topics: Other-only (asked by an official question; in reserve/pool) · Course-only. Understanding: pairs won Course–Other–equal. Verdict: coverage / accuracy / understanding for the Course against the Other.

| Tema | Words | Coverage C · O | Accuracy | Currency (C / O) | Topics | Underst. | Verdict |
|---|---|---|---|---|---|---|---|
| I.1 `m01-l01` | 6,455 / 2,022 · 8,150 / 60 | 9/9 · 8/9 | 1 · 2 | CE art. 49 (2024) in; LOTC to 2024-08-02; no (hoy:) markers; 2026… / 2024 edition; knows 2024 art. 49 reform in annex footnote;… | 7 (0; 5) · 9 | 5–0–0 | better / better / better |
| I.2 `m01-l02` | 8,986 / 5,672 · 8,350 / 0 | 9/9 · 5/9 | 0 · 7 | Carries the 2026 reform of art. 69.3 CE with its postponed effect,… / 2024 edition: no 2026 change; misses Formentera and the… | 14 (2; 13) · 7 | 4–1–0 | better / better / better |
| I.3 `m01-l03` | 8,196 / 4,678 · 8,120 / 318 | 13/13 · 11/13 | 0 · 4 | Ley 50/1997 snapshot 2025-01-03 already holds LO 1/2025 (arts. 5, 26,… / 2024 edition. Counts '3 vicepresidentas y 22 ministerios'… | 11 (1; 6) · 12 | 2–3–0 | better / better / worse |
| I.4 `m01-l04` | 10,778 / 6,644 · 10,870 / 60 | 13/13 · 11/13 | 0 · 4 | Reflects LBRL consolidated 2026-10-03 incl. Ley 4/2026 (art. 25.2.q),… / 2024 edition: municipal competence list ends at letter m)… | 9 (0; 5) · 12 | 2–3–0 | better / better / worse |
| I.5 `m01-l05` | 10,708 / 7,919 · 5,800 / 0 | 10/10 · 5/10 | 0 · 5 | Consolidated snapshots to 2025-12 (LOPDGDD), 2025-04 (RD 203/2021);… / 2024 edition: uses ministry names since renamed (Política… | 8 (2; 2) · 5 | 5–0–0 | better / better / better |
| I.6 `m01-l06` | 6,649 / 8,776 · 6,856 / 0 | 9/9 · 5/9 | 1 · 8 | Reflects Ley 4/2026 (in force 2026-10-23) on Ley 39/2006 and RDL… / 2024 edition. Predates Ley 4/2026 and RDL 36/2026. Pre-… | 15 (1; 14) · 7 | 4–1–0 | better / better / better |
| I.7 `m01-l07` | 20,345 / 8,707 · 12,300 / 30 | 10/10 · 6/10 | 0 · 5 | Reflects RDL 6/2023 libro segundo (carrera horizontal in tramos,… / 2024 edition: current on interinos (three years, Ley… | 8 (0; 7) · 11 | 5–0–0 | better / better / better |
| **Total** | 72,117 / 44,418 · 60,446 / 468 | 73/73 · 51/73 | 2 · 35 | | 72 (6; 52) · 63 | 27–8–0 | |


## 3.2 Part II — Derecho Administrativo General

Words: Course prose / esquema · Other prose / tables. Coverage: answered / vigente questions. Accuracy: confirmed errors, Course · Other. Topics: Other-only (asked by an official question; in reserve/pool) · Course-only. Understanding: pairs won Course–Other–equal. Verdict: coverage / accuracy / understanding for the Course against the Other.

| Tema | Words | Coverage C · O | Accuracy | Currency (C / O) | Topics | Underst. | Verdict |
|---|---|---|---|---|---|---|---|
| II.1 `m02-l01` | 3,404 / 642 · 6,700 / 70 | 9/9 · 7/9 | 0 · 5 | Consolidated sources: CE 2026-05-20, Ley 50/1997 2025-01-03, TFUE and… / 2024 edition. Uses ministry names of before December 2023… | 12 (1; 5) · 9 | 4–1–0 | better / better / better |
| II.2 `m02-l02` | 4,178 / 1,257 · 6,000 / 1,075 | 14/14 · 13/14 | 0 · 4 | LPAC consolidated 2024-11-06 with no 2025-2026 change; LO 3/1980 art… / 2024 edition; no covered article changed since; nothing… | 12 (0; 10) · 8 | 3–2–0 | better / better / better |
| II.3 `m02-l03` | 4,471 / 1,809 · 4,540 / 0 | 14/14 · 9/14 | 0 · 1 | Reflects the 2023 ministry renaming (hoy), arts. 32.4-32.5 technical… / 2024 edition; nothing outdated in what it covers; lacks… | 10 (1; 9) · 11 | 4–1–0 | better / better / better |
| II.4 `m02-l04` | 3,380 / 1,653 · 4,400 / 520 | 15/15 · 14/15 | 0 · 0 | Current: LPAC has no 2025-2026 amendment (consolidated 2024-11-06);… / 2024 edition; nothing out of date found for arts. 54-104;… | 19 (5; 19) · 11 | 1–4–0 | better / equal / worse |
| II.5 `m02-l05` | 2,841 / 1,107 · 6,750 / 190 | 11/12 · 10/12 | 0 · 1 | Reflects LO 1/2025 (Secciones of Tribunales de Instancia, DA 1ª);… / 2024 edition: no Tribunales de Instancia (LO 1/2025, phased… | 11 (0; 9) · 8 | 3–2–0 | better / better / better |
| **Total** | 18,274 / 6,468 · 28,390 / 1,855 | 63/64 · 53/64 | 0 · 11 | | 64 (7; 52) · 47 | 15–10–0 | |


## 3.3 Part III — Organización de la Hacienda Pública y Derecho Tributario

Words: Course prose / esquema · Other prose / tables. Coverage: answered / vigente questions. Accuracy: confirmed errors, Course · Other. Topics: Other-only (asked by an official question; in reserve/pool) · Course-only. Understanding: pairs won Course–Other–equal. Verdict: coverage / accuracy / understanding for the Course against the Other.

| Tema | Words | Coverage C · O | Accuracy | Currency (C / O) | Topics | Underst. | Verdict |
|---|---|---|---|---|---|---|---|
| III.1 `m03-l01` | 4,199 / 3,290 · 5,040 / 0 | 8/9 · 7/9 | 0 · 6 | Reflects Ley 7/2024 (Impuesto Complementario, margen de intereses),… / 2024 edition. Has the Impuesto Complementario and margen de… | 19 (5; 6) · 12 | 1–4–0 | better / better / worse |
| III.2 `m03-l02` | 4,172 / 4,624 · 2,680 / 890 | 9/9 · 5/9 | 0 · 4 | Norm snapshots: Orden 1994 (2024-02-07), Orden PRE/3581/2007… / 2024 edition. Reflects the 2021 Resolution structure (ADIs,… | 6 (1; 4) · 8 | 4–1–0 | better / better / better |
| III.3 `m03-l03` | 5,949 / 936 · 6,300 / 190 | 13/13 · 9/13 | 0 · 7 | LGT unchanged since 2024-12-21; 2026 interest figures (4,0625 % /… / 2024 edition; LGT content still valid; no interest figure… | 9 (3; 4) · 9 | 3–2–0 | better / better / better |
| III.4 `m03-l04` | 14,427 / 1,333 · 12,335 / 18 | 32/32 · 17/32 | 0 · 6 | RGAT consolidated 2026-10-07, LGT 2024-12-21 (no change since), RD… / 2024 edition, copyright 2024. Predates RD 238/2026, the… | 13 (2; 11) · 10 | 3–2–0 | better / better / better |
| III.5 `m03-l05` | 11,764 / 2,166 · 9,280 / 590 | 21/21 · 17/21 | 0 · 2 | LGT snapshot 2024-12-21 (no change in arts. 85-112); RGAT snapshot… / 2024 edition; still matches the norm on every point tested;… | 16 (0; 14) · 7 | 2–3–0 | better / better / worse |
| III.6 `m03-l06` | 6,088 / 4,552 · 2,650 / 40 | 8/8 · 2/8 | 0 · 0 | Reflects the consolidated norms up to 2026-11: RDL 29/2026 wording of… / 2024 edition. Nothing after 2024: no CAIE exceptions of… | 4 (1; 1) · 11 | 1–3–1 | better / equal / worse |
| III.7 `m03-l07` | 8,802 / 3,553 · 6,630 / 0 | 15/15 · 10/15 | 0 · 6 | LGT snapshot 2024-12-21 (no amendment in 2025-2026), RGAT 2026-10-07… / 2024 edition. No norm of this tema changed afterwards, so… | 5 (1; 2) · 9 | 0–5–0 | better / better / worse |
| III.8 `m03-l08` | 10,676 / 1,582 · 11,570 / 419 | 21/22 · 17/22 | 0 · 2 | LGT snapshot 2024-12-21 (no 2025-26 change) and RGAT 2026-10-07;… / 2024 edition: already has the Impuesto Complementario term,… | 16 (0; 15) · 9 | 2–2–1 | better / better / equal |
| III.9 `m03-l09` | 7,503 / 2,890 · 8,850 / 500 | 14/15 · 13/15 | 0 · 0 | 2026 figures: orden limit 50.000 € (in force 15-04-2023), interés… / 2024 edition; 50.000 € limit and annulled 46.8 RGR noted;… | 12 (3; 11) · 6 | 2–3–0 | better / equal / worse |
| III.10 `m03-l10` | 4,346 / 3,091 · 3,950 / 0 | 10/10 · 7/10 | 0 · 4 | Articles in scope unchanged in LGT (2024-12-21), RGR (2024-01-31),… / 2024 edition; rules still current; only the RGGI name is… | 4 (0; 1) · 7 | 3–2–0 | better / better / better |
| III.11 `m03-l11` | 6,073 / 1,382 · 5,150 / 0 | 10/11 · 6/11 | 0 · 4 | LGT 2024-12-21 and RGR 2024-01-31 snapshots, no later changes; art.… / 2024 edition; norm text unchanged since; keeps Ley 22/2003… | 10 (2; 8) · 7 | 2–3–0 | better / better / worse |
| III.12 `m03-l12` | 10,649 / 3,730 · 7,900 / 230 | 24/24 · 18/24 | 0 · 5 | Reflects RGR 2024-01-31 (RD 117/2024 depósito 10 %/5 %), LGT 174.2… / 2024 edition; flags the RD 117/2024 depósito; outdated on… | 15 (1; 15) · 13 | 4–1–0 | better / better / better |
| III.13 `m03-l13` | 11,333 / 3,990 · 7,450 / 963 | 19/20 · 18/20 | 1 · 7 | Built on LGT consolidated 2024-12-21 and RGRST consolidated… / 2024 edition, aligned with the LGT text of 2024. No… | 15 (1; 13) · 10 | 5–0–0 | better / better / better |
| III.14 `m03-l14` | 9,518 / 2,991 · 8,960 / 1,370 | 18/18 · 16/18 | 1 · 9 | Built on LGT consolidated 2024-12-21 and RGRVA consolidated… / 2024 edition. No 2025-2026 change in the norms of the tema,… | 20 (1; 20) · 13 | 1–4–0 | better / better / worse |
| III.15 `m03-l15` | 10,273 / 11,906 · 11,100 / 575 | 22/22 · 16/22 | 1 · 9 | RDL 29/2026 (arts. 7.ñ, 23.2, 85.1 from 2027, DA 55, DA 65), Orden… / 2024 edition with a few later notes (DA 60, convenio… | 12 (3; 9) · 8 | 1–4–0 | better / better / worse |
| III.16 `m03-l16` | 8,546 / 1,512 · 6,450 / 140 | 14/14 · 11/14 | 0 · 2 | Consolidated LIRPF 2026-11-11. Reflects RDL 29/2026 (convalidated… / 2024 edition, but already carries the 2026 deduction por… | 9 (2; 6) · 9 | 3–1–1 | better / better / better |
| III.17 `m03-l17` | 10,935 / 3,076 · 4,300 / 0 | 8/8 · 3/8 | 0 · 5 | Reflects DA 15 from 2024, DT 44 2026-2028, RDL 22/2026 on art. 33… / 2024 edition: DA 15 limits and 15 % minimum tax present;… | 6 (0; 6) · 8 | 3–2–0 | better / better / better |
| III.18 `m03-l18` | 6,749 / 16,400 · 5,800 / 0 | 15/15 · 13/15 | 0 · 6 | Consolidated LIVA snapshot of 2026-10-07. Gives the art. 20.Uno.23.º… / 2024 edition. Its art. 20.Uno.23.º e´) is the text valid… | 2 (0; 0) · 10 | 4–1–0 | better / better / better |
| III.19 `m03-l19` | 8,667 / 10,035 · 5,730 / 0 | 18/18 · 12/18 | 0 · 9 | LIVA consolidated 2026-10-07. The 2025-26 changes (RDL 9/2024,… / 2024 edition; the articles it covers read the same today,… | 7 (0; 7) · 13 | 0–5–0 | better / better / worse |
| III.20 `m03-l20` | 6,476 / 4,220 · 1,975 / 360 | 11/11 · 5/11 | 0 · 6 | CAU snapshot 2022-12-12 (incl. Reg. 2022/2399); Reglamento Delegado… / 2024 edition: no ventanilla única rule, no Windsor items;… | 7 (1; 2) · 10 | 4–1–0 | better / better / better |
| **Total** | 167,145 / 87,259 · 134,100 / 6,285 | 310/315 · 222/315 | 3 · 99 | | 207 (27; 155) · 189 | 48–49–3 | |


## 4. The course's fix list, in priority order

### 4.1 Errors (file and line)

Five items remain after the opus adjudication; only no. 5 is a gap in a legal rule, the others are editorial. Everything else the analysts flagged was ruled an omission or no error.

1. `content/aeat-agentes-hacienda/es/lessons/m01-l01.md:593` — I.1: Glossary «suspensión provisional» (suspension of functions, arts. 90.4 and 98.3 TREBEP) placed where the text means suspension of judicial proceedings (art. 35.3 LOTC) (arts. 90.4, 98.3 TREBEP; art. 35.3 LOTC).
2. `content/aeat-agentes-hacienda/es/lessons/m01-l06.md:601` — I.6: Esquema row label «b)» in front of exemption ii) (protección temporal); should be «ii)» (art. 5.1 Ley 39/2006 (exemption ii)).
3. `content/aeat-agentes-hacienda/es/lessons/m03-l13.md:3` — III.13: Intro says the «Lo que más cae» block has six points; the block at lines 668-677 has ten (editorial, no legal error) (n/a (lesson intro)).
4. `content/aeat-agentes-hacienda/es/lessons/m03-l14.md:497-507 and 533-543` — III.14: Tables «Algunos plazos de interposición…» and «Algunos plazos máximos para resolver…» duplicate the tables at 484-495 and 521-531; no legal error (n/a (editorial)).
5. `content/aeat-agentes-hacienda/es/lessons/m03-l15.md:781` — III.15: States the ten-period window for the 1,1 % imputation as the rule in force until 31-12-2026 without the DA 55.ª override (values in force from 1-1-2012) that governs 2023-2026; only the example at line 813 applies it (85.1 LIRPF; DA 55.ª LIRPF).

(1 is a glossary line under the wrong section; 2 a mislabelled esquema row; 3 the intro of «Lo que más cae» says six points and there are ten; 4 two tables printed twice; 5 the ten-period rule for the 1,1 % imputation stated without the DA 55 override for 2023–2026, the same gap the Other has.)

### 4.2 Omissions the norm backs the Other on (not errors; cheap to close)

| Tema | Topic | Article | Where in the Course |
|---|---|---|---|
| I.4 | Appointment of the Council Secretary General | art. 240.2 TFUE | — |
| I.7 | Prestación por hijo a cargo con discapacidad: grados 33/65/75 % | art. 119 RD 375/2003 (remits to the… | — |
| III.4 | Sanctions of dissolved entities against successors | art. 40.5 LGT | — |
| III.4 | Effects of NIF revocation on bank accounts | DA 6.ª.4 LGT | m03-l04.md:80-84 |
| III.4 | Duty to show telematic presenter as representative | art. 46.4 LGT | — |
| III.6 | Pago fraccionado mínimo del IS: exclusiones | DA 14.ª.1 LIS | — |
| III.7 | Autoliquidación rectificativa como vía general y excepción por norma de rango superior | 120.3-4 LGT | — |
| III.8 | Place of actions for taxpayers with disability or reduced mobility | arts. 151 LGT, 174 RGAT | — |
| III.10 | Identity debtor-creditor example (State debt vs CCAA credit) | 55, 57 RGR | — |
| III.12 | Accounts with an autorizado | 171.2 LGT | — |
| III.15 | Reinvestment period, main home | art. 41.3 RIRPF | — |
| III.15 | 30 % reduction, five-year bar and dismissal | art. 18.2 LIRPF | m03-l15.md:325 |
| III.16 | Hijos en acogimiento o tutela en la tributación conjunta | art. 82.1 LIRPF | — |

Questions the Course answers only partly (6 of 452): II.5 OEP 2024 Q67 (art. 114.1.e LPAC relation clause and the absence of reposición), III.1 OEP 2023 Q92 (neither text says «real = objetiva»), III.8 OEP 2022 Q56 (neither text; the fact belongs to tema 11 per the ledger), III.9 OEP 2022 extraordinario Q67 (the quincena of art. 28 RGR), III.11 OEP 2024 Q32 (recargo and art. 62.2), III.13 OEP 2024 Q74 (both texts allow it only by elimination).

### 4.3 Currency gaps in the Course

- III.17: DA 20 LIS (pagos fraccionados 2026, Ceuta and Melilla) not mentioned. III.15: DA 60 and DA 63 LIRPF absent. III.5: art. 104 RGAT list stops at g); the consolidated text has h) and i).
- «(hoy: …)» markers missing where a quoted norm keeps an old ministry name: III.2 (Ley 31/1990), III.3 (art. 12.3 LGT), III.8.
- III.4: no mention of RD 238/2026 (mandatory electronic invoice, applicable 2027–2028). III.8: no mention of the pending constitutional question on art. 150.7 LGT (cuestión 1254/2025).
- III.20: the 3 EUR distance-sales duty (Reg. 2026/1022) is outside the programme sentence; nothing to do.

### 4.4 Missing topics an official question asked

Topics the Other treats and the Course lacks inside the epígrafe, asked by an official first-exercise question (any convocatoria). «In reserve» = verified sentences exist in `docs/age-verification/aeat/reserve/` or `pool/` (restorable without writing); «to write» = none.

| Tema | Topic | Article | Asked by | Status |
|---|---|---|---|---|
| I.2 | Función financiera de las Cortes | arts. 31, 133, 135, 136 CE | 2021-35 (art. 134) | in reserve (reserve/m01-l02.md#d208c8a00a (art. 134 amendments)) |
| I.2 | Nombramiento del Fiscal General del Estado | art. 124.4 CE | 2020-9 | in reserve (reserve/m01-l02.md#1fc3cd0d6a) |
| I.3 | Presidente's functions i), l), m), n): recurso de inconstitucionalidad, conflictos de atribuciones… | art. 2.2 Ley 50/1997 | OEP 2020 Q10 (as distractors); OEP 2023 Q22 (option A… | in reserve (reserve/m01-l03.md#08b99a66a8, #a82d0800c7, #9c737c1ae0, #13aa24e272) |
| I.5 | Registro electrónico de apoderamientos | art. 6 LPAC | OEP 2020 Q25 (tema II.3) | in reserve (reserve/m01-l05.md#9ba136dc10 (RD 203/2021 angle only)) |
| I.5 | Identification and signature systems, mandatory signature cases | arts. 9-11 LPAC | OEP 2022 Q24 (tema II.3) | **to write** |
| I.6 | Dependency system as public network | art. 6 Ley 39/2006 | OEP 2020 Q6; OEP 2021 Q14 | in reserve (docs/age-verification/aeat/reserve/m01-l06.md#e279572a64) |
| II.1 | Tratados internacionales: forma de celebración y autorización de las Cortes | arts. 93-96 CE | OEP 2022 extraordinario Q20 asked art. 1.5 CC, which the… | in reserve (reserve/m02-l01.md 20a36e7388, faeccfe0d4, 4f43ee877e; pool also…) |
| II.3 | Suspension versus interruption of the term (annex) | 22; 25.2 | OEP 2024 Q80 (25.2, Course has it) | **to write** |
| II.4 | Acumulación (definition) | 57.1 | OEP 2020 Q23 | in reserve (reserve/m02-l04.md#1cbb105bab) |
| II.4 | Medidas provisionales: urgencia, principios, alzamiento, extinción | 56.1, 56.2, 56.5-56.6 | OEP 2021 Q32; OEP 2023 Q52 option D | in reserve (reserve/m02-l04.md#44aa538472, d29c094f06, cb90702e11) |
| II.4 | Concentración de trámites; orden de despacho | 71.2, 72 | OEP 2024 Q76 options A, C | in reserve (reserve/m02-l04.md#6ee088e11e, 744a0ec296) |
| II.4 | Actos de instrucción con intervención del interesado | 75.2-75.3 | OEP 2021 Q28 | in reserve (reserve/m02-l04.md#8ce93df169, 084e9a3244) |
| II.4 | Alegar defectos de tramitación | 76.2 | OEP 2021 Q29 | in reserve (reserve/m02-l04.md#4f8332e4e0) |
| III.1 | IRNR: contribuyentes, hecho imponible, formas de sujeción | arts. 12, 13, 15 TRLIRNR | OEP 2024 Q29 (ledger: fuera de temario, programa 2024 tema… | in reserve (reserve m03-l01.md: 9e44e267e3, fd70e23cff (ámbito, interpretación);…) |
| III.1 | DST: rate 3 % and the three services | arts. 4 and 10 Ley 4/2020 | OEP 2021 Q34 (ledger: fuera de temario) | in reserve (reserve m03-l01.md 17311c627f (three services, art. 4.5); rate: none) |
| III.1 | ITF: 0,2 % rate and 1.000 millones threshold | arts. 2 and 7 Ley 5/2020 | OEP 2022 Q32 (ledger: fuera de temario) | in reserve (reserve m03-l01.md 9b6d1ff0ad and e8f929f384) |
| III.1 | Medioambientales (Ley 15/2012; Ley 7/2022) as a block with Canarias/Ceuta/Melilla scope | Ley 15/2012; Ley 7/2022 | OEP 2024 Q71 and OEP 2022 extraordinario Q100 (fuera de… | **to write** |
| III.1 | Hacienda local: IBI hecho imponible, IAE categories, exacción obligatoria vs potestativa | arts. 59-61, 78 TRLRHL | OEP 2023 Q92 (nature only) | in reserve (pool m03-l01.md (art. 61 mention); the lesson already has arts.…) |
| III.2 | Dependence of the Oficinas Nacionales (ONIF and others) on the Inspección head | not in local norms | OEP 2021 Q38 (ledger, tema III.2) | **to write** |
| III.3 | Executive-period surcharges: incompatibility and compatibility with interés de demora; 62.2/62.5… | 28.1, 28.5, 62.2, 62.5 | 2020 Q61, 2022 Q35, 2022X Q68, 2023 Q38 (other temas) | **to write** |
| III.3 | Medios and procedure of estimación indirecta | 53.2, 53.3, 158 | 2022 Q53 (other tema) | in reserve (reserve/m03-l03.md#c3c343a1fe, 6d9cfe3207, 38650d0411) |
| III.3 | Doctrinal classifications (impuestos, bases, exenciones, tipos) | doctrine | 2024 Q1 (other tema) | **to write** |
| III.4 | NIF revocation: credit institutions stop debits and credits | DA 6.ª.4 LGT | OEP 2020 Q47; OEP 2021 Q51 | in reserve (reserve/m03-l04.md#4a26b10b42) |
| III.4 | IVA registers: anotación deadlines, special-regime books (bienes usados, agencias de viajes,… | arts. 62-69 RIVA | OEP 2021 Q52 (SII); OEP 2022 Q44 (Course already answers) | in reserve (reserve/m03-l04.md#5b003f4826, c205b16284, e1f14448bc, 384e1d9e90) |
| III.6 | Recargos por declaración extemporánea (cross-reference) | art. 27 LGT | not checked; OEP 2025 Q18/Q61 and 2023 Q95 carry III.6 as… | **to write** |
| III.7 | Autoliquidación rectificativa as general route and the higher-norm exception | 120.3-4 LGT | OEP 2024 Q52 (120.4 text only) | **to write** |
| III.9 | Competencia en aplazamientos | 45.2-3 RGR | ledger 2021 competence rows (not text-checked) | in reserve (reserve/m03-l09.md:133-134) |
| III.9 | Apremio si el plazo de subsanación acaba tras el voluntario | 46.6 RGR | OEP 2024 Q55 scenario (answer by 47.3) | **to write** |
| III.9 | Compensación, orden de fracciones, modificación sin efecto suspensivo | 52 RGR | OEP 2022 Q58 (distractor D) | in reserve (reserve/m03-l09.md:197-201) |
| III.11 | tercería de dominio / mejor derecho | 165.3-5 LGT | OEP 2021 Q82 | in reserve (reserve line 131 (assigned to III.12)) |
| III.11 | conservación de actuaciones, anulación de recargos | 166.2 LGT | OEP 2020 Q79 | in reserve (reserve/m03-l11.md#af40538018) |
| III.12 | traslado del órgano inspector al de recaudación (delito) | 124 bis RGR | OEP 2020 Q90 (norma modificada) | in reserve (reserve#e37a47fc7b, 9a0dbf158a, c048f92e68, a996e267b4, 3ddaada44f,…) |
| III.13 | Recurso: acumulación, reducción por conformidad intacta, actas con acuerdo, intereses de demora,… | 212.1, 212.2, 212.3.b | OEP 2022 extraordinario Q86 (stem 212.3; distractor D on… | in reserve (reserve/m03-l13.md#6bfd9cd13e, #39b685a960, #6e73624854, #b8de740359,…) |
| III.14 | Cuantía of the reclamación: rules by type of act | 35.1 RGRVA | OEP 2020 Q88 (cites art. 35; threshold is art. 36, which… | in reserve (reserve/m03-l14.md#71c3fb5154, #901aba853d (table, 9 rows)) |
| III.15 | General dieta amounts | art. 9.A RIRPF | OEP 2022 ext Q94 (concept only) | in reserve (reserve/m03-l15.md#9317df3f17, #4c1babe348) |
| III.15 | In-kind exempt details (meal, transport, shares) | art. 42.3 LIRPF; arts. 45-46 RIRPF | OEP 2024 Q70 (42.2 only) | in reserve (reserve/m03-l15.md#fe2da1e155, #ce138cbeae) |
| III.15 | Courses and literary works: employment or business | art. 17.2.c-d, 17.3 LIRPF | OEP 2022 ext Q94 (option d) | in reserve (reserve/m03-l15.md#b50e38fb26) |
| III.16 | Pagos a cuenta: sujetos obligados, rentas no sujetas, retención y escala | arts. 99-101 LIRPF | OEP 2025 and 2024 questions filed under III.6 [III.16]… | in reserve (reserve/m03-l16.md#fd058e7512 (says it belongs to III.6)) |
| III.16 | Pensionistas y perceptores de desempleo pueden minorar la cuota diferencial con las deducciones… | art. 81 bis.1 último párrafo | OEP 2024 Q57 (as distractor B) | in reserve (reserve/m03-l16.md#7377bad23b) |
| III.20 | Full list of additions to transaction value (Course keeps only 71.1.e) | art. 71 CAU | OEP 2024 Q85 | in reserve (reserve/m03-l20.md#f2633fa835 and 13 rows) |

### 4.5 Missing topics inside an epígrafe (never asked)

Same test; each line marked «in reserve» or «to write».


**I.1** — I.1

- constitution dates and characteristics, parte dogmática/orgánica (preámbulo / dispositions) — **to write**
- constitutional reforms 1992 and 2011 (arts. 13.2, 135) — in reserve
- text of arts. 16, 17.1/17.3, 18.1/18.4, 19, 20.3-4, 24.1, 25, 26, 28.1, 29.1, 31, 33-35, 37.1 (arts. 16-37) — in reserve
- oath of the King, Prince and Regents (art. 61 CE) — in reserve
- liability of Magistrados (art. 26 LOTC) — in reserve
- control previo de tratados (art. 95 CE; art. 78 LOTC) — **to write**
- recurso previo contra Estatutos: content (art. 79 LOTC) — in reserve

**I.2** — I.2

- Estados de alarma, excepción y sitio (art. 116 CE) — in reserve
- Moción de censura (arts. 113-114 CE) — **to write**
- Defensor: queja en un año (art. 15.1 LO 3/1981) — in reserve
- Defensor: ámbito de competencias (arts. 12-14 LO 3/1981) — in reserve
- Diputación Permanente continues after dissolution (art. 78.3 CE) — in reserve
- Sufragio de españoles en el exterior (art. 68.5 CE) — in reserve
- Comisión de investigación: resultado al Ministerio Fiscal (art. 76.1 CE) — in reserve
- Poderes de los Presidentes de las Cámaras; sesiones conjuntas (art. 72.2-3 CE) — in reserve
- Comisión Permanente y Disciplinaria del CGPJ (arts. 601-604 LOPJ) — in reserve
- Competencias de la Sala de lo Civil y de lo Militar del Supremo (arts. 56, 61 LOPJ) — in reserve
- Presidencia de Sección en Tribunales de Instancia (art. 84.3 LOPJ) — in reserve
- Publicidad y oralidad; art. 127 CE; jurado (arts. 120.1-2, 127 CE) — in reserve

**I.3** — I.3

- Incompatibilities of Government members (art. 14 Ley 50/1997; art. 98.4 CE) — in reserve
- Government functions by constitutional act: referéndum art. 92, control previo of treaties art. 95, estados art. 116, exclusive… (arts. 92, 95, 116, 134, 161.2, 162 CE) — **to write**
- Principios de intervención (proporcionalidad, evaluación) and powers of verification (art. 4 LRJSP) — in reserve
- Concept of órgano and requirements for creating one (art. 5 LRJSP) — in reserve
- Residual competence of the Ministerio de Hacienda in organisation, personnel, procedure, inspection (art. 54.2 LRJSP) — in reserve
- Comisión interministerial de coordinación de la Administración periférica; Comisiones de asistencia al Delegado y al Subdelegado (arts. 78, 79 LRJSP) — in reserve
- Control de eficacia, supervisión continua and plan de actuación of the sector público institucional (art. 85 LRJSP) — **to write**
- Territorial entes: Administración local (provincias, municipios, isla), Comunidades Autónomas, administración corporativa (art. 137 CE; art. 2 LRJSP) — **to write**
- Current list of Comisiones Delegadas (art. 6 Ley 50/1997 (list set by Real Decreto)) — **to write**
- Creation of sociedades mercantiles by Consejo de Ministros agreement and functional tutelage (arts. 111 bis, 115 LRJSP (to confirm)) — **to write**

**I.4** — I.4

- Haciendas locales (art. 142 CE) — in reserve
- Organisation of municipios de gran población (arts. 122-127 LBRL) — **to write**
- Consejo Europeo functions, voting, presidency term (art. 15.1, 15.4, 15.5 TUE) — **to write**
- Secretary General of the Council (art. 240.2 TFUE) — in reserve
- Temporary committee of inquiry; European Ombudsman (arts. 226, 228 TFUE) — in reserve
- Internal bodies of the Parliament (Mesa, groups) (Reglamento PE; art. 14.4 TUE) — **to write**
- Court of Justice: staff disputes, arbitration clause, non-contractual liability, standing of individuals/ECB/CoA/CoR (arts. 263, 268, 270, 272 TFUE) — in reserve
- Court of Justice formations and specialised courts (arts. 251, 257 TFUE) — in reserve
- Advisory opinion on draft international agreements (art. 218.11 TFUE) — **to write**

**I.5** — I.5

- Cl@ve system (art. 9 LPAC (identification)) — **to write**
- Órganos colegiados a distancia (art. 17 LRJSP) — **to write**
- Validity of electronic documents, authentic copies (arts. 26-27 LPAC) — in reserve
- Electronic expediente (art. 70 LPAC) — **to write**
- Electronic notifications, ten-day rejection (arts. 41-43 LPAC) — **to write**
- Rights of persons before the Administrations (art. 13 LPAC) — **to write**

**I.6** — I.6

- Pregnancy as direct discrimination (art. 8 LO 3/2007) — in reserve
- Burden of proof (art. 13 LO 3/2007) — in reserve
- Judicial protection and legitimation (art. 12.1-2 LO 3/2007) — in reserve
- Equality in access to employment, training, promotion (art. 5 LO 3/2007) — in reserve
- Civil consequences, nullity, patrimonial liability, standing (arts. 25-29 Ley 15/2022) — in reserve
- LO 1/2004 title I and title II rights (arts. 4-19, 28 LO 1/2004) — in reserve
- Penal norms of LO 1/2004 (arts. 148, 171-172 CP) — in reserve
- Juzgados de Violencia sobre la Mujer and Fiscal (LO 1/2004 title V; LOPJ) — in reserve
- Scope of disability measures; participation in public life (arts. 5-7, 63 RDL 1/2013) — in reserve
- Dependency principles (art. 3 Ley 39/2006) — in reserve
- Valuation bodies and baremo (art. 27 Ley 39/2006) — in reserve
- Linked economic benefit and incompatibilities (arts. 17, 25 Ley 39/2006) — in reserve
- Comité Consultivo (art. 40 Ley 39/2006) — in reserve
- CE arts. 14, 32 and EU directives behind LO 3/2007 (CE) — **to write**

**I.7** — I.7

- Personal directivo: concept and principles (art. 13 TREBEP) — in reserve
- Movilidad por cambio de adscripción de puestos (art. 61 RD 364/1995) — in reserve
- Misiones de cooperación internacional (comisión de servicios hasta seis meses) (art. 65 RD 364/1995) — in reserve
- Atribución temporal de funciones (art. 66 RD 364/1995) — in reserve
- MUFACE servicios sociales: hijo con discapacidad, subsidio de jubilación, becas de estudios (arts. 111, 119 RD 375/2003) — in reserve
- MUFACE asistencia social: subsidio por defunción, ayuda de sepelio, ayudas asistenciales, ayuda de vivienda (arts. 133-134 RD 375/2003) — **to write**
- MUFACE indemnización por lesiones permanentes no invalidantes (RDL 4/2000 / RD 375/2003 (incapacidad…) — in reserve
- Clases Pasivas: retroactividad máxima de tres meses, imprescriptibilidad, silencio negativo, incompatibilidad de más de tres… (arts. 6.2, 7, 25.1 TRLCPE) — in reserve

**II.1** — II.1

- Reforma constitucional (procedimiento, límites) (arts. 166-169 CE) — **to write**
- Control de constitucionalidad: recurso de inconstitucionalidad y legitimados (arts. 161-165 CE) — **to write**
- Iniciativa legislativa y tramitación (veto, 2 meses/20 días, sanción 15 días) (arts. 87-91 CE) — in reserve
- Reserva de ley y ausencia de reserva de reglamento (art. 53.1, 81 CE) — **to write**
- Leyes de transferencia o delegación a las CCAA (art. 150.2 CE) — in reserve
- Leyes de las CCAA y principio de competencia (arts. 148-152 CE) — **to write**
- Clasificación doctrinal de reglamentos (ejecutivos, independientes, autónomos; jurídicos y administrativos) (art. 97 CE) — **to write**
- Reglamentos ilegales y medios de reacción (recurso directo e indirecto, inaplicación, revisión de oficio) (art. 47.2 LPAC; arts. 25, 26, 46, 71 LJCA) — **to write**
- Contenido de la Memoria del Análisis de Impacto Normativo, informes, Secretaría General Técnica, Comisión General de Secretarios… (art. 26.3-26.9 Ley 50/1997) — in reserve
- Principios del Derecho de la UE (autonomía, primacía, eficacia directa, responsabilidad) (case law; Declaración 17) — in reserve
- Fuentes directas e indirectas; costumbre (tipos); concepto de ley en sentido material (art. 1 CC) — **to write**

**II.2** — II.2

- Oral acts record; merging acts (36.2, 36.3) — in reserve
- Requerimiento previo (39.5 LPAC; 44 LJCA) — in reserve
- Notification enough for the deadline; data protection (40.4, 40.5) — in reserve
- Voluntary/mandatory electronic notification, avisos device, request medium, INE padrón (41.1, 41.3, 41.4) — in reserve
- Paper notification in sede; option for electronic; second failure to art 44 (42.1-42.3) — in reserve
- Duty to notify met by availability (43.3) — in reserve
- Optional prior notices; complementary media; indication (44, 46) — in reserve
- Publication details (45.1-45.4) — in reserve
- Indemnity on annulment (106.4) — in reserve
- Acts that end the administrative route (list) (114, 52 LBRL) — **to write**
- Suspension on appeal (117) — **to write**
- Delegación, avocación, encomienda, delegación de firma, suplencia (8-13 LRJSP) — in reserve

**II.3** — II.3

- Additional steps only by law / regulatory specialities (1.2) — in reserve
- New interesados in the procedure (8) — in reserve
- Registros particulares and the AGE registry (6.1, 6.4) — in reserve
- Publish and inform of times and silence effects; staff responsibility; means to meet deadlines (21.4-21.6) — in reserve
- Resolution in desistimiento, caducidad, prescripción (21.1) — in reserve
- Extension of the maximum time: proposal, no appeal (23) — in reserve
- Obligatoriedad de términos y plazos (29) — in reserve
- Maximum extension for consulates and procedures abroad (32.2) — in reserve
- Punto de Acceso General for information and copies (53.1.a) — in reserve

**II.4** — II.4

- Actuaciones previas (55) — in reserve
- Propia iniciativa; petición razonada defined (59, 61.1) — in reserve
- Denunciante exemption/reduction (62.4) — in reserve
- Solicitud: código de identificación, pluralidad, recibo, modelos masivos (66.2-66.5, 67) — in reserve
- Mejora voluntaria de la solicitud (68.3) — in reserve
- Prueba: rechazo y práctica (77.3-77.6, 78) — in reserve
- Informe no emitido en plazo (80.3-80.4) — in reserve
- Audiencia: renuncia al trámite; información pública (82.3, 83.1) — in reserve
- Imposibilidad material de continuar (84.2) — in reserve
- Terminación convencional: contenido mínimo (86.2) — in reserve
- Resolución: congruencia, deber de resolver (88.2-88.4) — in reserve
- Desistimiento de la Administración; límites de la caducidad (93, 95.2, 95.4) — in reserve
- Tramitación simplificada: desestimación presunta; responsabilidad patrimonial (96.3, 96.4) — in reserve
- Ejecución: notificar la resolución; pago por medios electrónicos (97.2, 98.2) — in reserve

**II.5** — II.5

- Content of the appeal writing; defect not alleged by its author (115.1, 115.3 LPAC) — in reserve
- Remaining procedural acts; replacement of appeals; appeals founded on a general disposition (112.1-3 LPAC) — in reserve
- Hearing, resolution, plurality of appeals (118-120 LPAC) — in reserve
- Alzada: report and file, selection tribunals, firmness (121.2, 122.1 LPAC) — in reserve
- Revisión: other rights, ruling on the merits, contencioso after silence (125.3, 126.2-3 LPAC) — in reserve
- Other bodies within the order (1.3 LJCA) — in reserve
- Jurisdiction improrrogable; organic competence (5, 8-14 LJCA) — in reserve
- Pretensiones, acumulación (31-35 LJCA) — in reserve
- Amount of the appeal (40-42 LJCA) — in reserve
- Capacity, legitimation, defendant, representation (18-24 LJCA) — **to write**
- Start of the proceedings (45 LJCA) — **to write**

**III.1** — III.1

- Principle exposition: generalidad, capacidad económica, igualdad, progresividad, no confiscatoriedad, one each (art. 31.1 CE; art. 3 LGT) — **to write**
- Redistribution principle (arts. 131.1 and 138 CE) — **to write**
- Elements of the tributary system (fines fiscales/extrafiscales, institutional elements) (none (doctrine)) — **to write**
- IRPF elements: hecho imponible, contribuyentes, paraíso fiscal rule, base, cuotas (arts. 6, 8, 10, 15, 50, 62, 67, 79 LIRPF) — **to write**
- IS elements: ámbito, hecho imponible, contribuyentes, base, cuotas (arts. 2, 4, 7, 10, 29-30 LIS) — **to write**
- IP: hecho imponible, sujeto pasivo, base (arts. 3, 5, 9 Ley 19/1991) — **to write**
- ISD: hecho imponible, contribuyentes, base, cuotas (arts. 3, 5, 9, 21, 22 Ley 29/1987) — **to write**
- IVA types, deducción, repercusión (arts. 90-91 (types), 92 ss., 88 LIVA) — **to write**
- ITPAJD hecho imponible and operaciones societarias exemption (art. 7, 45.I.B.11 TRLITPAJD) — **to write**
- Gases fluorados: hecho imponible and contribuyentes (arts. 5.Seis and Siete Ley 16/2013) — **to write**
- Depósitos en entidades de crédito: tipo (art. 19.Ocho Ley 16/2012) — **to write**
- Entes supramunicipales: áreas metropolitanas, comarcas, mancomunidades (arts. 150-156 TRLRHL) — in reserve
- Foral financing: cupo (aportación to the State) (Ley 12/2002 (Concierto) arts. 48-57) — **to write**
- Regímenes especiales by territory: IGIC, Arbitrio, IPSI, IIEE in Canarias/Ceuta/Melilla (Ley 20/1991; Ley 8/1991; art. 3 Ley 38/1992) — in reserve

**III.2** — III.2

- Comité Permanente de Dirección (composition, role) (apartado primero.4 Orden de 2-6-1994) — in reserve
- Comité de Coordinación de la Dirección Territorial (apartado primero.5 Orden de 2-6-1994) — in reserve
- Gabinete del Director General and Intervención Delegada (apartados duodécimo y decimocuarto Orden de…) — in reserve
- Application of LGT and procedure law to gestión, inspección and recaudación; LRJSP DA 17 (art. 103.Dos.1 Ley 31/1990; DA 17 Ley 40/2015) — in reserve
- List of the four ADIs (Anexo III Resolución 13-01-2021) — **to write**

**III.3** — III.3

- Obligaciones formales content (17.3, 29.2) — **to write**
- Estimación directa and objetiva definitions (51, 52) — in reserve
- Potestad reglamentaria reglada and impugnable (6) — in reserve
- Tasa vs precio público cost rules (Ley 8/1989 19.2, 25) — **to write**
- Decreto-ley, decreto legislativo, circulares, costumbre (CE 86, 82) — **to write**
- Cuota íntegra methods (56.2) — in reserve

**III.4** — III.4

- Censal alta and modificación: who files, content, plazo of one month, December exceptions (DA 5.ª LGT; arts. 9, 10 RGAT) — in reserve
- Registros within the censo: ROI, devolución mensual (REDEME), territorial de impuestos especiales (art. 3.3, 3.4, 3.6 RGAT) — in reserve
- NIF assignment: provisional vs definitive, 10 days, requirements (arts. 23-24 RGAT) — in reserve
- Use of the NIF in relations with tax consequence (arts. 26-27 RGAT) — in reserve
- Books of the Impuesto sobre Sociedades and mercantile books (art. 120 LIS; Código de Comercio) — **to write**
- Invoice content, means of issue, issue deadline, recapitulativas, duplicados (arts. 6, 7, 8, 11, 13, 14 RD 1619/2012) — in reserve
- Catalogue of declaraciones informativas (models, thresholds, deadlines) (arts. 30-37 RGAT and orders) — in reserve
- Sanctions of dissolved entities against successors; payment from the herencia yacente (arts. 40.5, 39.3 LGT) — in reserve
- Telematic presenter acts as representative (art. 46.4 LGT) — in reserve
- Exception for inspection and responsabilidad procedures after a change of domicilio (art. 59.3 RGAT) — in reserve
- Residence test of art. 9 LIRPF and domicilio of non-residents (art. 11 TRLIRNR) (art. 9 LIRPF; art. 11 TRLIRNR) — **to write**

**III.5** — III.5

- Texto íntegro de consultas o resoluciones a petición (87.2 LGT) — in reserve
- Acceso gratuito por internet a las publicaciones (86.4 LGT) — in reserve
- Archivo de consultas sin requisitos no subsanadas (10 días) (88 LGT) — in reserve
- Contenido de la comunicación de inicio y efecto de declaraciones e ingresos posteriores (87 RGAT; 27 LGT) — in reserve
- Contenido de la solicitud y subsanación en 10 días (88-89 RGAT) — in reserve
- Modelos normalizados y presentación telemática obligatoria (98.3-4 LGT) — in reserve
- Certificación de lo presentado y acceso a expedientes concluidos (un mes) (99.3, 99.5 LGT; 94 RGAT) — in reserve
- Lugar y horario de las actuaciones (90 RGAT) — in reserve
- Trámite de audiencia y alegaciones, prescindir de la audiencia (96 RGAT; 99.8 LGT) — in reserve
- Supuestos de liquidación provisional en inspección (parcial, conflicto, valor, delito) (190 RGAT; 101.4 LGT) — **to write**
- Dilaciones h) días de cortesía e i) libros registro IVA (104.h-i RGAT) — in reserve
- Notificación colectiva por edictos y supuestos sin notificación expresa (102.3-4 LGT) — in reserve
- Aviso de llegada y exposición de anuncios en oficina o consulado (112.1 LGT; 114 RGAT) — in reserve
- Segundo intento: tres días, franja horaria, mayor de 14 años; defectos de la notificación (42.2, 40 LPAC) — **to write**
- Pruebas de otros Estados en asistencia mutua (106.2 LGT) — in reserve
- Publicidad del listado limitada a tributos estatales (95 bis.3 LGT) — in reserve

**III.6** — III.6

- Formas y obligatoriedad de presentación electrónica de autoliquidaciones (Clave, certificado, NIF más número de referencia,… (Orden HAP/2194/2013) — **to write**
- Cuadros de autoliquidaciones periódicas y no periódicas (image-only in the extraction) (n/a) — **to write**
- Obligaciones del retenedor: certificado, comunicación al perceptor, resumen anual modelo 190 (arts. 105-108 RIRPF) — in reserve

**III.7** — III.7

- Devolución de ingresos indebidos: concept and interest from the date of the ingreso (32.1-2 LGT) — **to write**
- Effects of the start communication (prescripción interrupted, ingresos as ingresos a cuenta) and of caducidad (no interruption,… (68.1, 104.5 LGT; 87 RGAT) — **to write**
- Interest on rectification resulting in an amount to pay (130.2 RGAT) — in reserve
- Valor comprobado vinculante para otros obligados (134.4 LGT) — in reserve

**III.8** — III.8

- Central and territorial organs of the inspection (ONIF, ONFI, large-taxpayers office, regional dependencies) (Resolución 24-03-1992 Uno; Orden 1994) — in reserve
- Effects of the start: declarations after start are not spontaneous, payments are on account, no interest on them (art. 87.5 RGAT; arts. 27, 68.1, 189.3 LGT) — in reserve
- Modifying the extension or the scope of the actions once started; scope versus extension (art. 178.1, 178.5 RGAT) — in reserve
- Inadmission of the request for a general inspection: motivated, no appeal (art. 179.2 RGAT) — in reserve
- End of the suspension of the term (art. 150.3 LGT (last paragraphs)) — in reserve
- 27-month term extended to all linked persons (art. 150.1 LGT) — in reserve
- Periods without actions: automatic grant and automatic denial under 7 days (art. 184.2 RGAT) — in reserve
- Default interest on the new liquidation after retroactive annulment (art. 150.7 LGT) — in reserve
- Partial conformity (two related actas) and mixed acuerdo/conformidad/disconformidad actas (arts. 187.2, 186.8 RGAT) — in reserve
- Extra contents of actas (officials, start date and term, allegations, provisional or definitive) (art. 176.1 RGAT) — in reserve
- Diligencias for other procedures (98.3); how diligencias are processed (99); mandatory reports (100.2) (arts. 98.3, 99, 100.2 RGAT) — in reserve
- Interest on refunds from an inspection (art. 191.4 RGAT) — in reserve
- Free entry in ports, stations, airports and markets (art. 173.4 RGAT) — in reserve
- Provisional liquidations under 190.2 and 190.4 RGAT (101.4.b LGT) (arts. 190.2, 190.4 RGAT) — in reserve
- Sanction reductions 65 % and 30 % in actas (belongs to another tema's lesson) (art. 188.1 LGT) — in reserve
- Evidential value of diligencias (art. 107 LGT) — **to write**

**III.9** — III.9

- Plazos de pago en ejecutivo (62.5 LGT) — in reserve
- Preferencia de la Administración sobre entidades dependientes (63.4 LGT) — in reserve
- Datos de la solicitud (46.2 RGR) — in reserve
- Documentos para garantía no aval (46.4 RGR) — in reserve
- Inadmisión por inspección suspendida (47.1.b RGR) — in reserve
- Sin garantía si solicita una Administración (48.1 RGR) — in reserve
- Tramitación, calendario provisional, alegaciones (50.2, 51 RGR) — in reserve
- Fallo del cargo en cuenta no imputable al obligado (38.3 RGR) — in reserve
- Ejecución de garantías tras 62.5 (54.1.c RGR; 168 LGT) — in reserve

**III.10** — III.10

- List of forms of extinction; Código Civil 1.156 (59 LGT) — **to write**
- Reiterated requests do not stop período ejecutivo (161.2 LGT; 56.5 RGR) — in reserve
- Same debtor and creditor requirement (71 LGT; 55 RGR) — **to write**
- Four-year prescription and interruption in baja provisional (66-67 LGT) — **to write**

**III.11** — III.11

- medidas cautelares art. 253: 24 months, 18-month cap (81.7.e LGT) — in reserve
- embargo preventivo sin establecimiento / espectáculos (81.8 LGT) — in reserve
- medidas cautelares en asistencia mutua (81.2 LGT) — in reserve
- retención de devolución notificada con el acuerdo (81.4.a LGT) — in reserve
- garantías generales del derecho común (CC 1911; LGT 39-40) — **to write**
- créditos de otros Estados sin privilegios (80 bis LGT) — in reserve
- continuar apremio con garantía manifiestamente insuficiente (74.7 RGR) — in reserve
- órganos competentes (providencia, medidas cautelares) (AEAT organisation) — **to write**

**III.12** — III.12

- embargo of a pro indiviso share limited to the quota (76.3 RGR) — in reserve
- embargo in premises of third persons (entrega, precinto, auxilio) (76.1 RGR) — in reserve
- formación de lotes (99 RGR) — in reserve
- agrupación de subastas (102 RGR) — in reserve
- capacidad para licitar and excluded persons (103.1 RGR) — in reserve
- depositario: retribución and acts beyond custody (95-96 RGR) — in reserve
- interventor or administrador for business rentas (89.2 RGR) — in reserve
- Registro de Bienes Muebles for the establecimiento (90 RGR) — in reserve
- adjudicación directa: plazo de un mes and precio mínimo (107.3, 107.5 RGR) — in reserve
- patrimonio histórico: no enajenación (109.1 RGR) — in reserve
- bienes sin adjudicar: new enajenación before prescription (104 bis, 109 RGR) — in reserve
- insolvencia parcial and declaración de fallido (124.4 RGR) — in reserve
- herencia sin herederos conocidos (127.3 RGR) — in reserve
- certificado de deudas to the deliberating heir (127.1 RGR) — in reserve

**III.13** — III.13

- Legalidad, tipicidad and proporcionalidad explained (the Course only names them) (178) — **to write**
- Retroactividad favorable of the sanction regime (10.2 (cited in 178)) — **to write**
- Criterio de una consulta ajena and 206 bis exclusion of diligencia (179.2.d) — in reserve
- Compatibility of 198 with 199 and 203 (180.2) — in reserve
- Suspensión de doce meses y sanción accesoria del 202.3 (186.3, 186.4) — in reserve
- Devolución obtenida más falta de ingreso (cuantía no ingresada and 100 % perjuicio) and falta de ingreso leve cuando se… (191.5, 191.6) — in reserve
- Incumplir requisitos de facturación (1 %) (201.2.a) — in reserve
- Conflicto en la aplicación de la norma: supuestos, criterio administrativo, incompatibilidades, reducciones (206 bis.1, 2, 5, 6) — in reserve
- Medidas cautelares en el procedimiento sancionador (210.3) — in reserve
- Renuncia a la tramitación separada: plazos and forma (208.1-2, RGRST 26) — in reserve
- Un procedimiento sancionador por propuesta de liquidación (RGRST 22.4) — in reserve
- Base de la sanción: cantidades sancionables y no sancionables (RGRST 8) — in reserve
- Actions leading to regularización interrupt prescription of the derived sanction (189.3.a) — in reserve
- Recaudación de sanciones and sanciones ingresadas indebidamente (190.3, 190.4) — in reserve

**III.14** — III.14

- Acts that must also be motivated (list) (215.2 LGT) — in reserve
- Nulidad: tramitación (audiencia 15 días, propuesta, dictamen request) (4 to 6 RGRVA) — in reserve
- Lesividad: initiation, audiencia, report of legal advisers (7 to 9 RGRVA) — in reserve
- Revocación: who starts, who processes, who resolves (director general / director de departamento), audiencia 15 días (10 to 12 RGRVA) — in reserve
- Rectificación de errores: tramitación, alegaciones 15 días; error de hecho versus de derecho (220 LGT; 13 RGRVA) — in reserve
- Devolución de ingresos indebidos: plazo de seis meses and silencio, alegaciones 10 días, competent organ (19 and 18 RGRVA) — in reserve
- Reposición: content of the escrito and guarantee attached (23 RGRVA) — in reserve
- Reposición: suspension request before the organ that issued the act; no guarantee means no effect; consequences of denial (25 RGRVA) — in reserve
- Interest stops when the deadline passes with suspension (reposición, reclamación, abreviado) (225.4, 240, 247.3 LGT) — in reserve
- Competence of CCAA economic-administrative organs; criterio resolutions of salas desconcentradas (229.3 and 229.4 LGT) — in reserve
- Acumulación: the agreement is a non-appealable trámite act (230.3 LGT) — in reserve
- Suspension in the reclamación: submission, cautelar suspension, período ejecutivo (233.9, 233.3 LGT; 40 RGRVA) — in reserve
- Iniciación: órgano may annul the act before sending the file; copia sellada (235.3 LGT) — in reserve
- Tramitación: electronic filing failures, evidence by acta notarial (236 LGT) — in reserve
- Terminación: archivo; execution of resolutions within one month and no interest after; retroacción; confirmed suspended act (238, 239.3 LGT; 66 to 71 RGRVA) — in reserve
- Recurso de anulación: archivo agreement, effect on alzada plazo, later appeal covers both (241 bis.2, 241 bis.5, 241 bis.6 LGT) — in reserve
- Recurso contra la ejecución: procedure, no prior reposición, inadmisibilidad (241 ter.5, 241 ter.7, 241 ter.8 LGT) — in reserve
- Composition of the Sala Especial para la Unificación de Doctrina (243.2 LGT) — in reserve
- Abreviado: content of the escrito (246 LGT) — in reserve

**III.15** — III.15

- 30 % reduction details (dismissal period, 700.000-1.000.000 band, capital benefits) (art. 18.2-3 LIRPF) — in reserve
- Rendimiento neto with family tenant (art. 24 LIRPF) — in reserve
- Requirements of the 2.000 reduction and the 1.620 reduction (art. 32.2.2.º-3.º LIRPF) — in reserve
- Simplified modality: 5 % difícil justificación, amortization table (art. 30.2.4.ª LIRPF; art. 30 RIRPF) — in reserve
- Reinvestment of main home (two years, vivienda habitual) and start-up shares (art. 38 LIRPF; arts. 41, 41 bis RIRPF) — in reserve
- Pending income on change of residence (art. 14.3 LIRPF) — in reserve
- Artistic income reduction (DA 60 LIRPF) — **to write**
- Church abuse-victim payments exemption (DA 63 LIRPF) — **to write**
- Other RCM go to the general base (art. 25.4, 46 LIRPF) — **to write**

**III.16** — III.16

- Obligaciones formales del retenedor (art. 105 LIRPF) — **to write**
- Deducciones por obras de eficiencia energética y vehículos eléctricos (DA 50.ª and 58.ª LIRPF) — in reserve
- Incremento de 150 euros en el mes de los 30 días cotizados (maternidad) (art. 81.1 LIRPF) — in reserve
- Reducción de 1.000 euros por aportaciones a favor del cónyuge (art. 51.7 LIRPF) — in reserve
- Fallecimiento del descendiente o ascendiente y convivencia la mitad del período (mínimos) (art. 61.4 and 61.5 LIRPF) — in reserve
- Custodia compartida: quién opta por la conjunta (criterio TEAC) (art. 83 LIRPF (doctrina)) — **to write**
- Esquema de liquidación del impuesto (flujo de cuotas) (arts. 62-79) — **to write**

**III.17** — III.17

- plantilla tranches 26.5 % / 30 % (25.1) — in reserve
- 50 % joint cap on arts. 31-32 deductions (DA 15.2) — in reserve
- minimum tax 10 % / 18 %, exclusions (30 bis.1) — in reserve
- negative rents on group transfers; quitas y esperas (11.9, 11.10, 11.13) — in reserve
- foreign tax as expense; grouping by country (31) — in reserve
- payment with Patrimonio Histórico goods; loss of incentive (125.2, 125.3) — in reserve

**III.18** — III.18

- Characteristics of the IVA (real, objetivo, instantáneo, neutral, harmonised by the EU) (art. 1 LIVA (not in the article text as such)) — **to write**
- Exenciones limitadas (art. 20) against plenas (arts. 21-25), tied to the right to deduct (art. 94 LIVA) — **to write**

**III.19** — III.19

- Devengo with digital-platform sales (75.Tres (8 bis)) — in reserve
- BI in commission sales/purchases and services for third parties (79.Seis-Ocho) — in reserve
- Re-increase of the base when the concurso ends (80.Tres 2.º párrafo) — in reserve
- Rectification: include the difference in the period's return (89.Cinco 2.º párrafo) — in reserve
- Goods and services tied to investment goods (95.Cuatro) — in reserve
- Regularisation: late start, switch from exclusive use, later quotas, business-transfer subrogation, loss of the good (107.Uno 2.º, Dos, Cuatro, Cinco, Seis) — in reserve
- Electronic refund claims by EU-established businesses (117 bis) — in reserve

**III.20** — III.20

- Customs union, objectives of customs authorities (art. 28 TFUE; art. 3 CAU) — **to write**
- Definitions: autoridades aduaneras, titular de las mercancías, titular del régimen (art. 5.1, 5.34, 5.35 CAU) — **to write**
- Customs status of goods (arts. 153-157 CAU) — **to write**
- Surveillance of Union goods declared for export (art. 158.3 CAU) — in reserve
- Normal vs simplified declaration (art. 166 CAU) — **to write**
- Duty types: ad valorem, antidumping, compensatory (art. 5.18 CAU context) — **to write**

## 5. Questions each text misses (OEP 2022–2025)

| Tema | Course misses | Other misses |
|---|---|---|
| I.1 | — | OEP 2023 Q13 |
| I.2 | — | OEP 2025 Q9, OEP 2024 Q81, OEP 2022 Q2, OEP 2022 extraordinario Q6 |
| I.3 | — | OEP 2023 Q35, OEP 2023 Q84 |
| I.4 | — | OEP 2025 Q46, OEP 2025 Q79 |
| I.5 | — | OEP 2024 Q37, OEP 2022 Q11, OEP 2022 Q21, OEP 2022 extraordinario Q13, OEP 2022 extraordinario Q14 |
| I.6 | — | OEP 2023 Q33, OEP 2022 Q12, OEP 2022 Q13, OEP 2022 Q14 |
| I.7 | — | OEP 2024 Q68, OEP 2023 Q39, OEP 2022 extraordinario Q17, OEP 2022 extraordinario Q19 |
| II.1 | — | OEP 2024 Q91, OEP 2022 extraordinario Q20 |
| II.2 | — | OEP 2024 Q69 |
| II.3 | — | OEP 2025 Q61, OEP 2025 Q67, OEP 2024 Q3, OEP 2024 Q10, OEP 2022 Q24 |
| II.4 | — | OEP 2022 Q25 |
| II.5 | OEP 2024 Q67 | OEP 2024 Q28, OEP 2024 Q67 |
| III.1 | OEP 2023 Q92 | OEP 2023 Q87, OEP 2023 Q92 |
| III.2 | — | OEP 2025 Q40, OEP 2024 Q15, OEP 2024 Q27, OEP 2023 Q48 |
| III.3 | — | OEP 2023 Q47, OEP 2023 Q95, OEP 2022 extraordinario Q32, OEP 2022 extraordinario Q33 |
| III.4 | — | OEP 2025 Q2, OEP 2025 Q30, OEP 2025 Q63, OEP 2024 Q8, OEP 2024 Q39, OEP 2024 Q43, OEP 2024 Q59, OEP 2023 Q11, OEP 2023 Q40, OEP 2023 Q46, OEP 2023 Q96, OEP 2022 Q44, OEP 2022X Q43, OEP 2022X Q45, OEP 2022X Q79 |
| III.5 | — | OEP 2025 Q62, OEP 2024 Q24, OEP 2023 Q88, OEP 2023 Q99 |
| III.6 | — | OEP 2025 Q15, OEP 2025 Q65, OEP 2024 Q5, OEP 2024 Q78, OEP 2023 Q64, OEP 2023 Q91 |
| III.7 | — | OEP 2025 Q43, OEP 2024 Q52, OEP 2023 Q67, OEP 2022 Q48, OEP 2022 Q49 |
| III.8 | OEP 2022 Q56 | OEP 2025 Q39, OEP 2023 Q26, OEP 2022 Q53, OEP 2022 Q56, OEP 2022 extraordinario Q58 |
| III.9 | OEP 2022 extraordinario Q67 | OEP 2022 Q60, OEP 2022 extraordinario Q67 |
| III.10 | — | OEP 2025 Q3, OEP 2024 Q31, OEP 2023 Q72 |
| III.11 | OEP 2024 Q32 | OEP 2024 Q32, OEP 2023 Q38, OEP 2022 Q35, OEP 2022 extraordinario Q68, OEP 2022 extraordinario Q69 |
| III.12 | — | OEP 2024 Q26, OEP 2023 Q97, OEP 2022 Q66, OEP 2022 Q68, OEP 2022 extraordinario Q73, OEP 2022 extraordinario Q81 |
| III.13 | OEP 2024 Q74 | OEP 2024 Q74, OEP 2022 Q46 |
| III.14 | — | OEP 2025 Q52, OEP 2022 Q76 |
| III.15 | — | OEP 2025 Q7, OEP 2025 Q31, OEP 2023 Q45, OEP 2022 Q79, OEP 2022 Q83, OEP 2022 extraordinario Q87 |
| III.16 | — | OEP 2024 Q75, OEP 2022 Q86, OEP 2022 extraordinario Q59 |
| III.17 | — | OEP 2025 Q18, OEP 2025 Q75, OEP 2024 Q86, OEP 2024 Q94, OEP 2022 Q45 |
| III.18 | — | OEP 2025 Q8, OEP 2024 Q93 |
| III.19 | — | OEP 2025 Q5, OEP 2025 Q24, OEP 2025 Q60, OEP 2023 Q29, OEP 2023 Q80, OEP 2022 Q96 |
| III.20 | — | OEP 2025 Q33, OEP 2025 Q64, OEP 2025 Q76, OEP 2023 Q73, OEP 2022 Q100, OEP 2022 extraordinario Q98 |

## 6. Teaching devices the readers preferred in the Other

The blind readers chose the Other in 67 of 160 pairs (the Course in 90, tie in 3). The device kinds that decided those 67 pairs (a pair can carry up to three):

| Device kind | Pairs |
|---|---|
| completeness / missing condition or figure | 52 |
| plain-language explanation before the rule | 14 |
| contrast of neighbouring rules | 12 |
| emphasis of what is examined | 11 |
| ordered steps / phases | 10 |
| headline overview / grouping by theme | 7 |
| worked example | 5 |
| brevity / density | 3 |
| table / esquema / structured outline | 3 |

- «Completeness» alone decided 22 pairs; in 18 the reader noted that the other side was cut off, skeletal or thin. Those are mostly the Course's long sections cut at 700 words (§7), not a device.
- Devices the Other used that the readers valued, with the sections where they helped:
  - **Contrast of two neighbouring rules, with the difference spelled out** — tasa and precio público (III.3), natural and legal-person successors (III.4), definitive and firm (III.5), complementaria / rectification request / rectificativa (III.6), comprobación limitada against caducidad (III.7), lesividad against nullity (III.14), IRPF and IS residence (III.17), guarantee against suspension and the two tercerías (III.11). The Course has «No confundir» blocks, but not for these pairs.
  - **Plain-language explanation before a technical rule** — devengo against due date with an IRPF example (III.3), imputed income with a short example (III.15), requisitos of a rectificación (III.7), notification effects (III.11).
  - **Ordered steps or phases with the figures inline** — rectification of autoliquidaciones (III.7), the revision procedures (III.14), the tiers of the reductions for rental income (III.15), embargo of securities (III.12).
  - **Grouping by theme, with a one-line headline per group** — VAT exemptions by health, social, teaching (III.18), competence by tribunal with the 150,000 / 1,800,000 thresholds (III.14).
  - **Emphasis on what is examined** — what a plain list of limits and thresholds says in one block (III.16 limits, III.19 devengo special cases).
- Kind of section where the Other won (sections classified by keywords in their titles, so approximate): sections of amounts, limits and computations 15 of 27 pairs (56 %); lists of cases, organs and competences 11 of 27 (41 %); sections of other concept and definition kinds 33 of 78 (42 %); procedures with deadlines 8 of 28 (29 %). The Course holds its ground best on procedures and is weakest, relative to the Other, on sections of figures and conditions.


## 7. Caveats

- The blind pairs were cut at 700 words per side. Several Course sections are longer than the Other's, so the cut hit the Course first: readers noted cut-off text in many pairs and preferred the side with the full rule. The preference figure understates the Course on those sections and cannot be corrected without rerunning with whole sections.
- Format cues (markdown directives against PDF text, inline citations) may have revealed the source to the readers; some analysts left the Course's «(art. … LPAC)» citations in the Course side.
- Measure 2 for the Other is a lower bound where its tables or diagrams are images; measure 1 likewise.
- «Asked by an official question» for OEP 2020 and 2021 rests on the ledger's keys and the analysts' notes; those two questionnaires' texts were not in the package.
- The «asked» flag of a missing topic is the analyst's reading of the ledger and exam texts; a few rows record a question that touched the topic only through a distractor or in another tema (read the «Asked by» cell). Treat the count of 40 as an upper bound.
- The sample of five sections per tema is small: a tema's reader preference moves by two pairs at the edge of noise.
- Norms not in `sources/normativa/` (Orden HAP/2194/2013, Orden HAC/1398/2003, TJUE case law, MUFACE amounts) left some disputes unresolved; those are not counted as errors of either text.

## 8. Verdict per tema

| Tema | Coverage | Accuracy | Understanding |
|---|---|---|---|
| I.1 I.1 | better | better | better |
| I.2 I.2 | better | better | better |
| I.3 I.3 | better | better | worse |
| I.4 I.4 | better | better | worse |
| I.5 I.5 | better | better | better |
| I.6 I.6 | better | better | better |
| I.7 I.7 | better | better | better |
| II.1 II.1 | better | better | better |
| II.2 II.2 | better | better | better |
| II.3 II.3 | better | better | better |
| II.4 II.4 | better | equal | worse |
| II.5 II.5 | better | better | better |
| III.1 III.1 | better | better | worse |
| III.2 III.2 | better | better | better |
| III.3 III.3 | better | better | better |
| III.4 III.4 | better | better | better |
| III.5 III.5 | better | better | worse |
| III.6 III.6 | better | equal | worse |
| III.7 III.7 | better | better | worse |
| III.8 III.8 | better | better | equal |
| III.9 III.9 | better | equal | worse |
| III.10 III.10 | better | better | better |
| III.11 III.11 | better | better | worse |
| III.12 III.12 | better | better | better |
| III.13 III.13 | better | better | better |
| III.14 III.14 | better | better | worse |
| III.15 III.15 | better | better | worse |
| III.16 III.16 | better | better | better |
| III.17 III.17 | better | better | better |
| III.18 III.18 | better | better | better |
| III.19 III.19 | better | better | worse |
| III.20 III.20 | better | better | better |

Count over 32 temas — coverage: better 32, equal 0, worse 0; accuracy: better 29, equal 3, worse 0; understanding: better 19, equal 1, worse 12.

«Better / equal / worse» are the Course's against the Other's: coverage by questions answered, accuracy by confirmed errors (fewer is better), understanding by blind-pair wins.

## 9. Pointers

Per-tema notes with every verdict, dispute and topic: `docs/age-verification/aeat/comparison/notes/<code>.md|json`; adjudications: `adjudication/<code>.md|json`; decisions and resume points: `log.md`; tools: `tools/` (`count_course_words.py`, `count_other_words.py`, `decode_readers.py`, `aggregate.py`, `gen_report.py`). Blind pairs, reader tables and keys are in the session scratchpad (they contain benchmark text and stay out of the repo).
