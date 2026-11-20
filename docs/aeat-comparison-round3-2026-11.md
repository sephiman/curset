# Comparison, round 3 — the 12 temas rated «worse» on understanding, re-measured

2026-11-20 · follows `docs/aeat-comparison-2026-11.md` (round 1 of the comparison, 2026-11-19) and the fixes rounds 1–2 (`docs/age-verification/aeat/fixes-1/`, `fixes-2/`). Read-only for `content/`. Not committed.
R4.13: no text of the benchmark syllabus appears here; topics and article numbers only. Working notes, specs, tools and reader tables: `docs/_work/age-verification/aeat/comparison-3/` (the blind pairs contain benchmark text and stay in the session scratchpad, outside the repo).

The 12 temas: I.3, I.4, II.4, III.1, III.5, III.6, III.7, III.9, III.11, III.14, III.15, III.19.

## 0. Finish criteria — stated plainly

| # | Criterion | Result | Met |
|---|---|---|---|
| 1 | 452 questions answerable | **447 / 452** (the 12 temas re-measured: 175, same total as before; 20 temas not re-measured, with the 2 round-1 fixes confirmed). Five unanswered: III.1 OEP 2023 Q92, III.8 OEP 2022 Q56, III.13 OEP 2024 Q74 (partly), III.14 OEP 2022 Q70 (partly), III.19 OEP 2025 Q60 (partly) | **No** |
| 2 | Zero errors | **9 confirmed errors** (opus, against the norm) in 5 of the 12 temas: I.3 ×2, I.4 ×2, III.6 ×2, III.19 ×2, III.15 ×1. The 5 errors of round 1 are fixed. The other 20 temas were not re-scanned with the deeper method used here | **No** |
| 3 | Understanding better or equal in ≥ 28 of 32 temas | **32 / 32** with the controlling reader (opus: 11 better, 1 equal among the 12; the other 20 as rated in round 1 and not re-measured). With sonnet as the reader: 30 / 32 (III.5 and III.15 worse) | **Yes** |
| 4 | Reading size ≤ 1.3 × the other text | **1.52 ×** (prose + in-place esquemas, 351,898 words, against 231,544 = prose + tables of the other). Prose alone 1.21 ×. 21 of 32 temas are over 1.3 × | **No** |

## 1. How it was measured (and what differs from round 1)

- **Pairs.** Per tema, the five topics round 1 used (matched to today's lessons by topic, because the lessons were restructured) and five more chosen at random: a seeded shuffle of the course's sections, taking the first five that have a counterpart in the other text and do not overlap an old pair. Each side is given whole: the course section with its «Preguntas», «Caso», «No confundir» and in-place table (annex tables appended only where the section points to them), the other text's whole treatment of the same topic. No side was cut (two course sections of 3,935 and 3,166 words were replaced by their level-4 sub-sections, both sides on the same topic). Unlabelled, A/B random, key kept apart.
- **II.4 has 8 pairs and III.6 has 8**: the lessons have too few sections that the other text also treats (II.4 also overlaps: its «Prueba» pair is inside the «Instrucción» pair on the course side).
- **Readers.** Sonnet read all 116 pairs. A blind opus re-check of 12 pairs (10 %) disagreed on 3 (25 %), above the one-in-ten tolerance round 1 used. Following that rule, opus read all 116 pairs and is the controlling reader; sonnet's figures are shown beside it. Sonnet and opus differ on 24 of 116 pairs (21 %); opus gives the course more wins (83 against 78).
- **A first reading round was discarded.** Its line ranges for the other text were misaligned (form-feed characters shifted the numbering); readers judged wrong passages on one side. The ranges were re-derived and checked by the first and last line of every passage, and every reader ran again. Only the second round is reported.
- **Before** is round 1's count per tema on its five sections (sonnet, sections cut at 700 words, so not like for like), with the individual pairs from `fixes-1/understanding-report.md`. The round-1 pair files are gone.
- **Coverage and accuracy.** Course side only (the other text did not change; its round-1 figures stand). Sonnet analysts, who were not given round-1 results and not the other text: each official question answered by the lesson alone; accuracy = every line that did not exist in the version round 1 read (diff against `1e8e21f`) plus 12 or more rule-bearing sentences per lesson, against the norm snapshots. 12 doubtful points were adjudicated by opus.
- **Sizes** by script, same rules as round 1, with the annex counted apart.

## 2. Per tema

### 2.1 Understanding

Course–other–equal wins. «Now» uses the whole pair set; «same sections» are the five round-1 topics; «new» the added ones.

| Tema | Before (same sections, round 1) | Now, same sections: opus · sonnet | New sections: opus · sonnet | All pairs: opus · sonnet | Verdict (opus) |
|---|---|---|---|---|---|
| I.3 | 2–3–0 | 5–0–0 · 4–1–0 | 4–1–0 · 4–1–0 | 9–1–0 · 8–2–0 | better |
| I.4 | 2–3–0 | 4–1–0 · 5–0–0 | 3–2–0 · 4–0–1 | 7–3–0 · 9–0–1 | better |
| II.4 | 1–4–0 | 2–3–0 · 3–2–0 | 2–1–0 · 3–0–0 | 4–4–0 · 6–2–0 | **equal** |
| III.1 | 1–4–0 | 4–1–0 · 2–3–0 | 3–2–0 · 3–2–0 | 7–3–0 · 5–5–0 | better (sonnet: equal) |
| III.5 | 2–3–0 | 3–2–0 · 2–3–0 | 4–1–0 · 1–3–1 | 7–3–0 · 3–6–1 | better (sonnet: worse) |
| III.6 | 1–3–1 | 5–0–0 · 4–0–1 | 1–2–0 · 2–1–0 | 6–2–0 · 6–1–1 | better |
| III.7 | 0–5–0 | 5–0–0 · 5–0–0 | 2–3–0 · 2–3–0 | 7–3–0 · 7–3–0 | better |
| III.9 | 2–3–0 | 3–2–0 · 5–0–0 | 3–2–0 · 3–2–0 | 6–4–0 · 8–2–0 | better |
| III.11 | 2–3–0 | 4–1–0 · 4–1–0 | 3–2–0 · 4–1–0 | 7–3–0 · 8–2–0 | better |
| III.14 | 1–4–0 | 3–2–0 · 2–3–0 | 3–2–0 · 4–1–0 | 6–4–0 · 6–4–0 | better |
| III.15 | 1–4–0 | 5–0–0 · 1–4–0 | 2–3–0 · 2–3–0 | 7–3–0 · 3–7–0 | better (sonnet: worse) |
| III.19 | 0–5–0 | 5–0–0 · 4–1–0 | 5–0–0 · 5–0–0 | 10–0–0 · 9–1–0 | better |
| **Total** | 15–44–1 (60 pairs) | 48–12–0 · 41–18–1 | 35–21–0 · 37–17–2 | **83–33–0** · 78–35–3 | 11 better, 1 equal |

Verdict rule: better if the course wins more pairs than the other text, equal if the same, worse if fewer, over all pairs of the tema. On the five round-1 sections alone, opus puts the course ahead in 11 of the 12 temas and behind only in II.4 (2–3). On the new sections it is ahead in 9 and behind in 3 (III.6 1–2, III.7 2–3, III.15 2–3): the new sections are weaker for the course than the old ones, which were the ones round 1 had already shown as weak spots and the fixes rounds worked on.

### 2.2 Coverage and accuracy

Coverage: official questions answered by the text alone (course now · course round 1 · other, unchanged). Errors: confirmed against the norm (course now · other, round 1).

| Tema | Questions | Course now | Course round 1 | Other | Coverage | Errors course · other | Accuracy |
|---|---|---|---|---|---|---|---|
| I.3 | 13 | 13 | 13 | 11 | better | 2 · 4 | better |
| I.4 | 13 | 13 | 13 | 11 | better | 2 · 4 | better |
| II.4 | 15 | 15 | 15 | 14 | better | 0 · 0 | equal |
| III.1 | 9 | 8 | 8 | 7 | better | 0 · 6 | better |
| III.5 | 21 | 21 | 21 | 17 | better | 0 · 2 | better |
| III.6 | 8 | 8 | 8 | 2 | better | **2 · 0** | **worse** |
| III.7 | 15 | 15 | 15 | 10 | better | 0 · 6 | better |
| III.9 | 15 | 15 | 14 | 13 | better | 0 · 0 | equal |
| III.11 | 11 | 11 | 10 | 6 | better | 0 · 4 | better |
| III.14 | 18 | 17 | 18 | 16 | better | 0 · 9 | better |
| III.15 | 22 | 22 | 22 | 16 | better | 1 · 9 | better |
| III.19 | 18 | 17 | 18 | 12 | better | 2 · 9 | better |
| **Total** | 178 | **175** | 175 | 135 | 12 better | **9 · 53** | 9 better, 2 equal, 1 worse |

- Misses among the 12: III.1 OEP 2023 Q92 (partly; the lesson says «real» without equating it to «objetiva»; unchanged since round 1), III.14 OEP 2022 Q70 (partly: the conditions of art. 212.3 LGT), III.19 OEP 2025 Q60 (partly: the lesson never names the rappel). III.9 and III.11 now answer their round-1 misses (OEP 2022 extraordinario Q67; OEP 2024 Q32). The two new partials in III.14 and III.19 had been answered in round 1; the analysts of this round were not told the old verdicts, so this is a stricter reading or a real regression and cannot be told apart here.
- Outside the 12: II.5 OEP 2024 Q67 now answered (re-read this round); III.13 OEP 2024 Q74 is only partly answered (ranges by grade, no link with the requerimiento case); III.8 OEP 2022 Q56 stays open.
- **The 9 confirmed errors** (opus; all in lines that mostly predate this round, so round 1's spot checks had not reached them):
  - I.3 `m01-l03.md:145` (art. 8.2 Ley 50/1997: the sentence on the interruption of attendance is dropped, so the substitute rule reads as applying to the absence); `:423` (art. 22.3 LRJSP: «sus acuerdos» reads as applying to every collegiate body; the norm limits it to working groups and committees).
  - I.4 `m01-l04.md:592` (art. 21.3 LBRL: the ban on delegating the powers of letter j) is stated without the exception for the Junta de Gobierno Local); `:554` (art. 121.1 LBRL: Title X applied automatically to letters c) and d); it needs the decision of the Asamblea Legislativa).
  - III.6 `m03-l06.md:413` (art. 101.1 LIRPF: arrears at 15 % without the rates of 101.2 and 101.3 that override it); `:243` (art. 81.1–3 RIRPF: «nothing is withheld below the thresholds» without the exclusions of 81.3 and the increases of 81.2).
  - III.19 `m03-l19.md:272` (art. 89.Cinco LIVA: corrective return always required; the exception for art. 80 base changes and error fundado de derecho is missing); `:454` and about `:762` (art. 99.Cuatro LIVA: input VAT counts as borne on receipt of the invoice; the norm moves it later when the tax becomes chargeable later).
  - III.15 annex, table «Reducciones del art. 23.2 LIRPF por tramo» (about lines 834–838; art. 23.2.a).1.º LIRPF, RDL 29/2026 wording): the five tiers (100 to 70 %) lack the condition (new contract, landlord not a large holder, initial rent lowered by more than 5 %) and read as contradicting the other tiers.
  - Ruled omissions, not errors: III.1 `m03-l01.md:62` (art. 5 TRLIRNR gives only letter a)), III.6 `:340` (DA 14.ª LIS floor of 25 %). Ruled no issue: III.6 `:412` (art. 101.3 LIRPF).
- The other text's error counts are round 1's figures; its text did not change.

### 2.3 Size as a reader meets it

Words. «Reading» = prose + in-place esquemas; the annex is shown apart; ratio against the other text's prose + tables.

| Tema | Course prose | In-place esquemas | Annex | Other prose | Other tables | Reading ratio | Prose-only ratio |
|---|---|---|---|---|---|---|---|
| I.3 | 8,758 | 2,659 | 2,559 | 8,120 | 318 | 1.35 | 1.08 |
| I.4 | 12,221 | 2,898 | 3,746 | 10,870 | 60 | 1.38 | 1.12 |
| II.4 | 4,027 | 1,653 | 0 | 4,400 | 520 | 1.15 | 0.92 |
| III.1 | 4,694 | 3,125 | 190 | 5,040 | 0 | 1.55 | 0.93 |
| III.5 | 12,674 | 2,305 | 0 | 9,280 | 590 | 1.52 | 1.37 |
| III.6 | 6,515 | 1,879 | 2,673 | 2,650 | 40 | 3.12 | 2.46 |
| III.7 | 9,343 | 3,028 | 863 | 6,630 | 0 | 1.87 | 1.41 |
| III.9 | 7,793 | 3,008 | 0 | 8,850 | 500 | 1.16 | 0.88 |
| III.11 | 6,461 | 1,382 | 0 | 5,150 | 0 | 1.52 | 1.25 |
| III.14 | 10,394 | 2,505 | 0 | 8,960 | 1,370 | 1.25 | 1.16 |
| III.15 | 11,021 | 3,306 | 8,910 | 11,100 | 575 | 1.23 | 0.99 |
| III.19 | 10,189 | 5,003 | 5,849 | 5,730 | 0 | 2.65 | 1.78 |
| **12 temas** | 104,090 | 32,751 | 24,790 | 86,780 | 3,973 | **1.51** | 1.20 |

## 3. Where the other text still wins (33 of 116 pairs, controlling reader)

Kind of the deciding device (primary one) and whether verified sentences already exist in `reserve/` or `pool/` (ids in `notes/other-wins-A.md` and `-B.md`).

| Tema | Pairs won by the other text | Kind | Content in reserve / pool |
|---|---|---|---|
| I.3 | Delegados del Gobierno | completeness (appointment, powers, command of security forces only in the annex) | yes |
| I.4 | Financiación de las Comunidades; Organización institucional de las CCAA; Provincia | completeness ×2 (art. 156.2 CE; art. 152.2–3 CE); grouping (aims of the province as a list) | yes ×2; restructure only |
| II.4 | Instrucción; Prueba; Expediente; Medios de ejecución forzosa | ordered steps and completeness (arts. 80.3–4); completeness (arts. 77.4–77.7, 78); contrast (art. 70.3–70.4); plain explanation first | yes ×4 (the last one by restructure) |
| III.1 | Gases fluorados; Principios del art. 31 CE; IRPF | grouping; plain explanation first with example; ordered steps | **no ×3** (nothing in reserve or pool beyond sentences already used) |
| III.5 | Liquidaciones: concepto y clases; Fases: iniciación; Personas legitimadas para recibir notificaciones | contrast (provisional/definitive/firm); completeness (arts. 87.5, 88.2–3 RGAT); contrast (arts. 111.1–2 LGT) | no; yes; no |
| III.6 | Pago fraccionado del IS; Declaración e ingreso de las retenciones | contrast of the two modalities (layout of existing sentences); completeness (art. 108.2 RIRPF, art. 71.3 RIVA) | restructure only; partly |
| III.7 | Tramitación por declaración; Lista de procedimientos; Devoluciones (ingresos indebidos) | completeness (arts. 129.3 LGT, 133.2 RGAT); completeness (art. 123.2 LGT); contrast (art. 32 LGT) | yes; partly; **no** |
| III.9 | Imputación y consignación; Medios de pago en efectivo; Tramitación y resolución; Solicitud | contrast by layout; grouping and completeness (arts. 36, 38.3 RGR); completeness (arts. 51–52 RGR); completeness (art. 46 RGR) | restructure only; yes; yes; partly |
| III.11 | Suspensión; Medidas cautelares; Ejecución de garantías | emphasis (arts. 165.1, 165.4–5 LGT); completeness (art. 81.7–81.9 LGT); emphasis (art. 74.7 RGR, art. 168 LGT) | no; yes; partly |
| III.14 | Revocación; Tribunales y competencias; Reposición: iniciación; Normas comunes: motivación | ordered steps and contrast (arts. 219 LGT, 10–12 RGRVA); completeness (art. 35.1 RGRVA); completeness (arts. 223.3 LGT, 2.1 RGRVA); completeness (art. 215.2 LGT) | yes ×3; partly |
| III.15 | Imputación temporal; Rendimientos íntegros del trabajo; Ganancias excluidas | plain explanation first (art. 14 LIRPF); plain explanation first (art. 17.3 LIRPF); completeness (art. 38.2 LIRPF, art. 41 bis RIRPF) | partly ×3 |

By kind: completeness 15, contrast of neighbouring rules 6, plain explanation first 4, grouping 3, ordered steps 3, emphasis on what is examined 2. By availability: in reserve/pool 14, partly 8, none 7, restructure only (the content is in the lesson, the layout is the point) 4. The seven without any sentence are III.1 ×3, III.5 ×2 (liquidaciones, notifications), III.7 (art. 32 LGT) and III.11 (art. 165.1 warning).

## 4. Course totals, updated (32 temas)

| Measure | Round 1 | Now | Other |
|---|---|---|---|
| Temas better or equal on understanding | 20 / 32 (19 better, 1 equal) | **32 / 32** (opus; 30 / 32 with sonnet). The 20 outside the 12 are as rated in round 1, not re-measured; their lessons were edited in rounds 1–2 | |
| Official questions answered by the text alone (452) | 446 | **447** (the 12 temas re-measured: 175 of 178; 20 temas carried from round 1 with II.5 Q67 re-read) | 326 |
| Confirmed errors | 5 (course) | **9** known in the 12 temas re-measured; round 1's 5 are fixed (I.1, I.6, III.13 re-checked; III.14, III.15 by the analysts); the 20 others not re-scanned | 145 |
| Reading size, prose + in-place esquemas | 1.16 × prose; 1.71 × with all esquemas | **1.52 ×** (351,898 against 231,544); prose alone 1.21 ×; with the annex 1.77 × | 1.00 |
| Words (32 lessons) | prose 257,536 · esquemas 138,145 | prose 269,300 · in-place esquemas 82,598 · annex 58,044 | prose 222,936 · tables 8,608 |

## 5. Caveats

- **Readers disagree.** Sonnet and opus differ on 21 % of the pairs, and the 12-pair re-check differed on 25 %. Opus was chosen as controlling by the round-1 rule; with sonnet instead, III.5 and III.15 are «worse» and III.1 «equal». Criterion 3 holds either way (30 of 32 at worst).
- **Before and now are not like for like**: round 1 cut sections at 700 words and used sonnet; now sections are whole and opus decides. Whole sections remove the artefact round 1 named, but they also give the course's longer, structured sections more room.
- Format cues (markdown directives against PDF text, inline citations) can still show the source; the directives were converted to plain markdown and the other text's page headers stripped, nothing more.
- The sample is five old plus up to five new sections per tema; a tema's verdict moves by two pairs. II.4 («equal») and III.9 (6–4) sit at that edge.
- The other 20 temas were not re-measured for understanding, coverage or accuracy; criterion 3 counts them as round 1 rated them. Criterion 2 therefore cannot be called met even for them: the deeper accuracy check found 9 errors in 12 temas where round 1's spot checks had found 0 there.
- Coverage verdicts and the accuracy scan were made by sonnet (opus only on the 12 doubtful points); no 10 % opus re-check of coverage was run this round.
- Annex tables are counted apart and shown to readers only where the section points to them (this lengthens some course sides, e.g. III.19, III.15, III.6).

## 6. Decisions logged

- Old topics were matched to today's sections by topic (the lessons changed since round 1). Fewer than five new pairs for II.4 and III.6 (no more qualifying sections).
- Whole sections, no one-sided cut; level-4 headings added to the tooling to avoid cutting.
- First reading round discarded (misaligned ranges); ranges re-derived and checked by first/last line; readers rerun.
- Opus made the controlling reader after the 10 % re-check exceeded one in ten.
- Verdict rule: majority of pair wins over all pairs; equal on a tie.
- Coverage/accuracy measured on the course side only; the other text's round-1 figures reused (text unchanged).
- Official questions II.5 Q67 and III.13 Q74 were re-read (round 1 had changed those lessons).
- Nothing in `content/` was changed; nothing committed.
