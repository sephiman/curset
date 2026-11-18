# R2d — structural and Normativa fixes owed after verifier passes (for a fixer writer)

Each item: lesson, report, row id; the note column of that row says what to do. Sentence replacements were already
applied by `r2dprov.py apply`; these are what it cannot apply.

- m03-l08 `verify.md`: `9a79a83068`, `3e7f1bcbb4` (a)–c) items must nest under their lead-ins, arts. 186.7 and 187.2
  RGAT), `edbb54e798` (art. 188.4 RGAT lead-in «y se procede de la siguiente forma» and a)–b) nested), `96890861ee`
  (LGT Normativa line: add 179.3 and 188.2–4), `e86bae2619` (add Normativa lines for TRLCI RDLeg 1/2004 and Ley
  21/2001 art. 46.3, named in art. 166 RGAT).
- m03-l10 `verify.md`: if `9c9e36fae9` applied, add art. 161.2 to the LGT Normativa line.
- m03-l06 `verify.md`: note of `16e7b81041` — «nombrado en» lines for the ~15 norms the prose names (Ley 35/2003, RD
  1082/2012, TRLIS RDLeg 4/2004, Directivas 2003/41/CE, 2003/48/CE, 2009/65/CE, Ley 6/2023, RD 813/2023, Reglamento (UE)
  648/2012, Ley 41/1999, Ley 24/1988, RD 878/2015, Ley 19/1994, Ley 11/2009, Ley 22/2014, Código de Comercio).
- m03-l07 `verify.md`: note of `a8172d409f` — add Normativa lines: RGR (RD 939/2005) nombrado en art. 132.2 RGAT; Ley
  10/2010 art. 4.2 nombrado en art. 147.8 RGAT.

## Status

- 2026-11-14 second pass: m03-l02 and m03-l04 recheck notes (RD 238/2026 line, nesting under arts. 32.b) and 34.1.f) RGAT), m01-l06 and m01-l07 «nombrado en» lines — done

- m03-l08 items — done
- m03-l10 item — done
- m03-l06 item — done
- m03-l07 item — done
- m03-l02 items — done
- m03-l04 items — done
- m03-l08 art. 187.3 nesting — done
- m03-l02 (done) `verify.md`: Normativa rows 527–540 notes (undécimo bis/ter/quater listed — done by coordinator via the line
  already present; check primero.1 and decimosexto.2 removed if uncited; segundo.8; art. 93.1.a) LGT; «nombrado en»
  lines for the norms named inside copied text, per the note); rows 345–348 (closing paragraph of apartado tercero.2
  Resolución DCGC out of item k)); rows 98 and 195 (ordinal references rendered as nested sub-items: rejoin into the
  item's sentence). The arbol esquema was rebuilt by the coordinator (new root «Organización central de la Agencia»).
- m03-l04 (done; normativa.yaml RGAT note left to the coordinator) `verify.md`: Normativa notes (seven lines: «nombrado en» entries for ~40 norms; LIVA 164 whole); RD 1619/2012
  collision: the real decreto's own arts. 1–3 vs the Reglamento's articles share «art. N RD 1619/2012» — cite the
  Reglamento's articles as now and the real decreto's own articles in words («artículo 2.2 del Real Decreto 1619/2012,
  que aprueba el Reglamento») or as its disposiciones; RGAT note in normativa.yaml (art. 49 vs 49 ter) is for the
  coordinator.
- m01-l01 `verify.md`: Normativa CE line notes (arts. 87, 95; reform of art. 49 CE own line). (done)
- m01-l02 `verify.md`: Normativa CE line notes (arts. 18, 168; lines for RD 2917/1981, LOTC, Reglamento (UE) 2017/1939).
- m03-l15 (done) `verify.md`: Normativa notes — LIRPF cambio-pendiente for arts. 24 and 85.1 from 01-01-2027; an RDL 29/2026
  line; RDL 9/2024 / RDL 16/2025 / RDL 2/2026 articles if `d484bf3c04` was applied (notes of `2dbeff0149`,
  `40b9795dc7`); «nombrado en» / «no figuran» lines for ~20 named norms.
- m03-l01 `verify.md`: Normativa notes — Ley 38/2022 article list fixed; «nombrado en» / «no figuran» lines (Ley
  24/2001, LO 18/2001, LO 2/2012, Ley 30/1995, Ley 54/1997, Ley 34/1998, TRLSC, Directiva 2014/65/UE, Ley 4/2014 de
  Canarias, Código Civil, TFUE).
- (done) m03-l02 `verify-recheck-1.md`: Normativa notes of `7d68fd8924`, `ddcb430bf7`, `d05230607c`, `223793e146` (apply the
  replacement lines if not applied; they are full lines).
- (done) m03-l04 `verify-recheck-1.md`: Normativa notes of `e371ea02da`, `bf76c4bb5b` (+ new RD 238/2026 line), `43f2559ac6`,
  `42ebfd27ef`, `2c3405dc0a`, `052cc50e1d`; and the two paragraphs that split their lists (l. ~770 belongs to art.
  32.b) RGAT, l. ~842 to art. 34.1.f) RGAT: nest them).
- (done) m01-l06, m01-l07: «Normativa» lacks the norms named only inside quoted articles (the writer's notes list them): add
  «nombrado en» lines or the final «no figuran» line.
- m02-l01..05, m01-l03 `verify.md`: «Normativa» notes (named norms per lesson, LJCA art. 44 in m02-l02); m02-l03 art.
  24.1 LPAC: letters a)–e) invented — give the cases as the article's running text or as unlettered items.

- m03-l01 Normativa notes — done (R2d fixer)
- m01-l02 Normativa notes — done (R2d fixer)
- m01-l03 Normativa merged-range line — done; art. 69.3 «hoy» note — not done by coordinator's decision
- m02-l01..05, m01-l03 Normativa notes and m02-l03 art. 24.1 letters — done (R2d fixer)
- m01-l05 `verify.md`: Normativa notes (`8dfee16e15` LRJSP art. 155; `47314556d5` RD 203/2021 anexo; `81fe62cc9d`
  named norms: in normativa.yaml CE, Ley 30/1992, LBRL, LGP, LOFCA, TRLRHL, Ley 8/1989; not in it RD 3/2010, RD
  128/2018, Reg. (UE) 2018/1724, RD 1164/2002, Ley 16/1985, RD 1083/2009, Reg. (UE) 651/2014, RD 4/2010, Ley 37/2007,
  Ley 6/1997, LO 2/2012, Directiva 2002/58/CE); `24bce5c342` citation placement in art. 17.1 LPAC.
- m01-l06 `verify.md`: stray fragment « de igualdad de las empresas» (l. ~144, row `2a81e5974b`, drop the fragment
  only); closing paragraphs of art. 20 (l. ~108) and art. 46.2 (l. ~165) out of their list items (46.2 needs its
  citation); list items to add: art. 3.1.ñ) and art. 40.ñ) Ley 15/2022, art. 2.m) RDL 1/2013; chapter lead-ins that
  skip art. 34 (LO 3/2007 tít. II cap. II; Ley 15/2022 tít. II cap. II); l. 842 capítulo VII not VI; Normativa notes
  (Ley 50/1981 line; ET, CE, RGPD, LO 3/2018 lines; final «no figuran» line for RDLeg 2/2000, LECrim, Ley 1/1996, Ley
  35/1995, Ley 15/2015, Convención ONU discapacidad, Ley 12/2009, RD 1325/2003, Ley 14/1986, Ley 19/2007).
- m03-l07 `verify-recheck-2.md` `45082c76b3`: move the art. 134.5 first-paragraph bullet (l. ~242) after 134.3.c and
  134.4.
- m03-l15 `verify-recheck-1.md` `ace5654237`: art. 25.1 letters a)–e) inline « - a) …» → a real list; `ea9e9cb4a0`
  Normativa named norms (RD 63/2006, LO 1/2004, Ley 19/2021, Ley 29/1987 art. 20.6; LAU line: DT 2.ª.11 regla 7.ª, not
  art. 10).
- m03-l18 `cc46fdeb3a`: Normativa line «LIVA, versiones del art. 20: art. 20.» (or «versiones del art. 20 LIVA»).
- m03-l19 `c6620a7e63`: art. 24.2.b RIVA items 2.º–4.º out of the 1.º item; the concurso paragraph cited as art.
  24.2.b) (structural; the verifier's replacement was NOT applied).
- m03-l20 `8310be0d5c`: incisos ii)–iv) out of the i) item, each its own sub-item under a) (structural; replacement
  NOT applied); Normativa: Convenio relativo a un régimen común de tránsito, Convenio de París 1963, TIR, ATA.
- m01-l01 `a90a6479dc`: Normativa line for the laws named in the disposición derogatoria (Ley 1/1977, Leyes
  Fundamentales, laws of 25-10-1839 and 21-07-1876 — none in normativa.yaml).
- m01-l04 `0759d60916`, `03b33be1f7`, `0ddd956dc5`: Normativa named norms (LOREG art. 197; CE art. 18.1; Ley 39/2015,
  Ley 12/1989, LO 2/2012, Ley 4/2026, Ley 39/1988 art. 158.5, Ley 27/2013 with STC 111/2016, Estatuto del País Vasco).

- m01-l05, m01-l06, m03-l07, m03-l15, m03-l18, m03-l19, m03-l20, m01-l01, m01-l04 last block — done (R2d fixer 2); m01-l06 l. ~842 chapter lead-in left as is (already «capítulos VI y VII»)
- m01-l07 `verify.md` (first pass, 903/26; replacements applied): structural — `e77736de15` art. 77 TREBEP item out of
  the RDL 6/2023 list; `cce4a84cf7` «A tal objeto» rejoined to art. 16.2; `528052560a` art. 7.2 RDL 4/2000 joined to
  its context so «igualmente» has a referent; `33bceea4d9` «ese capítulo» → capítulo II; Normativa notes `a45b8b31d9`
  (TREBEP DF 3.ª), `241f49996e` (Ley 30/1984 art. 1.1), `b9bbf44442` (RDL 4/2000 preámbulo, DA 1.ª.2, DA 3.ª.2–3),
  `a09d851745` (LGSS: remove art. 128; RDL 31/2026 cambio-pendiente note), `9584b2d6a5` (1994 LGSS on the «no figuran»
  line); Ley 29/1975 line add «preámbulo»; art. 41.1.d) TREBEP scale given twice: keep one.
- m01-l03: art. 2.2.n) Ley 50/1997 out of place (after the art. 13.1 paragraph): move it to close the art. 2.2 list.

- m01-l07 first-pass structural and Normativa notes; m01-l03 art. 2.2.n) placement — done (R2d fixer 3)
| m03-l12 | 2ca9170fc6 (art. 80.4 RGR) | FAIL in verify-recheck-2, replacement applied 2026-11-17; re-check 3 by a different verifier owed (batched with the next Opus run) |
| m03-l15 | 6 pool sentences with no verdict (pool fixes after recheck-2 FAILs; listed in m03-l15/pending.md) | Opus check owed |
| all | build_check.py hole closed 2026-11-17: a row passed as «verbatim sub-item» when its citation cell (≥15 chars) was a substring of any pool sentence; now only the item's own (longest) cell counts. Rerun: III.13/9/11/12/14/05 unchanged; III.18 +1 row (l.208, art. 8 bis b), owed to Opus after recheck-5), III.16 +9 rows, III.17 +3 rows (both now in recheck-5) |
| m03-l12 | 2ca9170fc6 → bc4c209eb1 (art. 80.4 RGR) | PASS in recheck-3: closed; III.12 fully through |
| m03-l14 | 201328d6a0 (DA undécima.8 LGT), 04df458a2d (art. 61.2 RGRVA) | FAIL in recheck-4, replacements applied; re-check by a different verifier owed |
| m03-l15 | 14f819d916 (art. 24 LIRPF from 2027) | FAIL in recheck-3; apply after the III.15 reader-fixer finishes (it is editing the lesson), then re-check |
| m03-l05 | b4e52df06f (95 bis.4 LGT), 92356fb7cb (98.2 RGAT), 0a84fcfa16 (98.3 RGAT), e3ac4f2596 (104 RGAT) | FAIL in recheck-2 (the last three: the law's own «entre otros» removed under spec-fix rule, now corrected); replacements applied; re-check by a different verifier owed |
| m03-l20 | 19 pool sentences with no verdict (m03-l20/pending.md: 86.6 CAU; RD 135–142 items) | Opus check owed, batched after the III.20 reader-fixer |
| m03-l05 | 4 re-checked (recheck-3) | PASS: closed; III.5 fully through |
| m03-l18 | 44fbceaae6 (art. 8 bis b) row) | PASS in recheck-6: closed; III.18 fully through |
| m03-l14 | ba841be330 (61.2 RGRVA) PASS; eb605858b2 (DA undécima.8 LGT) FAIL in recheck-5 (failed re-check 1 of 2: «sus apartados» ambiguous) | replacement applied; re-check by a third verifier owed; a second failure drops the sentence |
| m03-l15 | 14f819d916 (art. 24 LIRPF 2027) replacement applied after the reader-fixer; 68 reworded + 6 pool rows | Opus recheck-4 owed (with the art. 24 re-check by a different verifier) |
| m03-l16 | 1492a086f7 (51.6), 7ceaafea58 (66.2), 727eb964a7 (68.2.c) LIRPF | FAIL in recheck-5, replacements applied; re-check owed |
| m03-l17 | 8b18884c93 (14.5 LIS), 4f4b96f210 (23.2 LIS) | FAIL in recheck-5, replacements applied; re-check owed |
| all | taxprov apply on a «No confundir» quoted line nested a «» and repeated the citation (III.20 l.169), fixed by hand; check quoted-line applies by eye |
| m03-l15 | recheck-4: PASS 59 · FAIL 15 (rewordings that lost conditions; 85.1 version marks; 85.2 uncited) | replacements applied; 3 structural notes (85.1 marks, 3.1.d) table row split, 23.2 2025 table b) row) to a fixer; re-check owed |
| m03-l07 | 521b61216c → art. 134.4 RGAT replacement | re-check owed |
| m03-l20 | 18.1 CAU line (repaired by hand), norms-not-in-normativa line | re-check 2 owed; a FAIL drops |
| all | build_check.py: rows built from a HEAD item now match (HEAD provenance), 2026-11-18 |
| m03-l03 | c884cba09b (15.2 LGT) FAIL recheck-2, applied; Normativa: Concierto/Convenio «nombrado en el art. 1.1 LGT» lines added by coordinator | re-check owed (3 rows) |
| m03-l01 | 8f118a90e6 (54.1 Ley 22/2009) FAIL recheck-3, applied | re-check owed |
| m03-l08 | 429bec47a0 (150.1 LGT), 9a79a83068 (186.7 RGAT), 1de1bc54f6 (row 186.7 RGAT) FAIL recheck-3, applied | re-check owed |
| m03-l07 | recheck-5 PASS | closed; III.7 fully through |
| m03-l20 | recheck-7 PASS 2 | closed; III.20 fully through |
| m03-l15 | recheck-5 FAIL 4: b94edc5ee5 (9.A.3 RIRPF, failed re-check 1 of 2), b31dbbad11/58ad9b0e43 (23.2 2025 wording placement), 379ef5b3ba (3.1.d) Orden) | applied; re-check owed |
| m03-l06 | recheck-3 FAIL 3: b8b51f98c9 (40.3 LIS), d9957c9392 (DA 14.ª.1.a) LIS), 0809d30049 (60.3 RIS) | applied; re-check owed |
| m03-l03, m03-l01, m03-l08 | re-checks PASS (recheck-3, -4, -4) | closed; fully through |
| m03-l19 | recheck-4 FAIL 3: 234daefb7c (119.Dos lead-in), bd6ea41b5e («Lo que más cae» 95.Tres line), 7e46bc49dc (LIVA Normativa) | applied; art. 119 material given its own heading (LIVA art. 119 heading) and 119.Uno moved under it by coordinator; re-check owed |
| m02-l04 | 89.1 a)–e) rows kept without PASS (complete enumeration); art. 74 nulidad clause pool version not PASS | Opus owed |
| m03-l06 | recheck-4 PASS 3 | closed; III.6 fully through |
| m03-l15 | 4c1babe348, 62b4d97f52, 3f09f4863c PASS; cd3b36e7d8 FAIL (second failed re-check) | dropped (r2d/dropped.md); III.15 fully through once the record is redone |
| m03-l02 | recheck-3 PASS 24 · FAIL 1 (776d5142e6, undécimo.1 Resolución 13-01-2021) | applied; re-check owed |
| m02-l01 | recheck-3 PASS 8 | closed; II.1 fully through |
| m02-l02 | recheck-3 FAIL 3 (107.3, 109.2, 110 LPAC) applied; CE «nombrada en el art. 47.2 LPAC» Normativa line added (ruling: a different norm named in copied text gets its own line) | re-check owed (4 rows) |
| m03-l19 | recheck-5 PASS 3; 119.Siete first paragraph moved after 119.Seis by coordinator (bytes unchanged) | closed; III.19 fully through |
| m03-l02 | recheck-4 PASS (current id ea967fff28 recorded by coordinator: pending.md was stale — always re-plan after apply) | closed; III.2 fully through |
| m02-l03 | recheck-2 FAIL 4 (10.3, 12.2, 23, 32.2 LPAC) applied | re-check owed |
| m02-l05 | recheck-2 FAIL 5 (125.2, 126.3 LPAC; 8.2, 8.6, 25.1 LJCA) applied | re-check owed |
| m02-l02 | recheck-4 PASS 4 (incl. CE «nombrada en» line) | closed; II.2 fully through |
| m02-l03 | recheck-3 PASS 3 | closed; II.3 fully through |
| m03-l04 | recheck-4 PASS 114 · FAIL 19 applied; 7 esquemas out of order, art. 37 bis.1 RGAT missing, 42 ter.1 labels, 74.2 RGRVA row, 164 LIVA 6.º paragraphs → structural fixer | re-check owed after the fixer |
| m02-l05 | recheck-3 PASS 4 | closed; II.5 fully through |
| m02-l04 | recheck-3 FAIL 5 applied (56.2, 62.4, 85.3, 96.6.g), 103.1 row); ENI «nombrado en el art. 70.3 LPAC» Normativa line added by coordinator | re-check owed |
| m01-l02 | recheck-4 PASS 56 · FAIL 3 (54, 570.2 LOPJ; DF única LO 3/1981) applied | re-check owed |
| m02-l04 | recheck-4 PASS 5 (incl. ENI line) | closed; II.4 fully through |
| m01-l01 | recheck-3 PASS 29 · FAIL 4 (33.2.b, 41.1, 50.1 lead-in, 56.2 — now cites arts. 52.2 y 56.2 LOTC) applied; art. 50.2 LOTC not covered → pool gap | re-check owed |
| m01-l03 | art. 101.2 CE sentence removed by the fixer as a repeat of 21.2 Ley 50/1997; restored by coordinator (HEAD bytes): a CE article of the range keeps its own rule | — |
| m03-l04 | recheck-5 PASS 18 · FAIL 1 (b43fe3b4a9, 37–54 ter lead-in: failed re-check 1 of 2) applied; art. 49 ter BOE note moved after 49 bis and art. 34.2 b) second-paragraph row labelled b) by coordinator | re-check owed |
| m01-l02 | recheck-5 PASS 3 | closed; I.2 fully through (gap fill still owed) |
| m01-l04 | recheck-3 PASS 36 · FAIL 3 (29.3 LBRL, 50 ter lead-in, «no figuran» line) applied; art. 50 ter table relabelled a)–f) by coordinator | re-check owed |
| m03-l04 | recheck-6 PASS 2 | closed; III.4 fully through (gap fill for art. 37 bis.1 still owed) |
| m01-l04 | recheck-4 PASS 8 · FAIL 1 (85cbf753f3, «no figuran» line: failed re-check 1 of 2 — Carta de Derechos Fundamentales UE, Reglamentos de la Asamblea at 9.2/12.1) applied | re-check owed |
| m01-l01 | recheck-4 PASS 4 | closed; I.1 fully through (gap fill still owed) |
| m01-l03 | recheck-3 PASS 35 · FAIL 4 + Normativa (21.3, 64.3, 75.b LRJSP; RD 1009/2023; Normativa) applied; the 64.3 sentence absorbed by the replacement removed by coordinator; 2 shared C1 gaps listed in c1-c2-list.md | re-check owed |
| all | build_check.py: C1/C2 lesson text now counts as verified (inherited provenance), 2026-11-18 — common-part builders had treated ~2,000 inherited pool sentences as unusable |
| m01-l05 | recheck-2 PASS 40 · FAIL 1 (11.1.i) RD 203/2021) applied | re-check owed |
| m01-l06 | recheck-2 PASS 12 · FAIL 3 (9 and 61.2 LO 1/2004; CP Normativa) applied | re-check owed |
| m02-l02 | recheck-5 PASS 3 | closed (gap fill) |
| m02-l05 | recheck-4 PASS 8 | closed (gap fill) |
| m02-l01 | recheck-4 FAIL 1 (4.3 TUE order): paragraph 1 moved above paragraph 2 by coordinator, bytes unchanged | re-check of the order owed |
| m03-l20 | recheck-8 FAIL 1 (72.6 RD scope) applied | re-check owed |
| m02-l03 | recheck-4 FAIL 1 (26.2 RD 203/2021) applied | re-check owed |
| m03-l20, m02-l03, m02-l01 | re-checks PASS; m02-l01 art. 4.3 TUE third paragraph moved after the second by coordinator (bytes unchanged, verified sentence) | closed |
| m03-l15 | gap-fill recheck-7 PASS 33 · FAIL 3 (1.1, 2.2 Orden HAC/1425/2025; Orden Normativa) applied; RIVA art. 37 «nombrado en» line added by coordinator | re-check owed |
| m03-l16 | gap-fill recheck-7 PASS 27 · FAIL 3 (49.3 ×2, 61.2 RIRPF → 61.1 quoted) applied; RIRPF line 61.1–6 by coordinator | re-check owed |
| m03-l19 | gap-fill recheck-6 PASS 22 | closed |
| m03-l06 | gap-fill recheck-5 PASS 136 · FAIL 10 applied | re-check owed |
| m03-l04 | gap-fill recheck-7 PASS 140 · FAIL 5 applied; LGT art. 1.2 «nombrado en» line added; art. 3.1 a), d) RD 1619/2012 paraphrases (HEAD text) → fixer | re-check owed |
| m01-l04 | recheck-5: 8.1, 8.2 PASS; «no figuran» line FAIL (second re-check) → replacement applied, third check (coordinator-notes); LOPJ «nombrada en» line added | re-check owed |
| m01-l01 | gap-fill recheck-5 PASS 130 · FAIL 3 (9.1 LOTC dropped as repeat; 8.2 LOTC; LOPJ/LEC/LJCA line) applied | re-check owed (2) |
| m03-l15, m03-l16, m03-l06 | gap-fill re-checks PASS (recheck-8, -8, -6) | closed (III.15: IAE lists still owed) |
| m01-l03 | gap-fill recheck-4 PASS 152 · FAIL 39 (16 content applied; 23 order → fixer); Normativa lines owed (LOTC, Ley 19/2013, LBRL, LO 2/2012) | fixer running; re-check owed |
| m01-l05 | recheck-3 PASS 2 | closed; I.5 fully through |
| m03-l04 | recheck-8 PASS 5 · FAIL 1 (RIVA line) applied + OCDE Acuerdo added to «no figuran» line | closed under the Normativa ruling (coordinator-notes) |
| m01-l04 | recheck-6 PASS 1 · FAIL 1 («no figuran» line) applied + TUE arts. 7, 40, título V cap. 2 «nombrados en» line added | closed under the Normativa ruling |
| m01-l06 | gap-fill recheck-3 PASS 192 · FAIL 13 applied (3 Normativa lines closed under the Normativa ruling) | re-check owed for the 10 content rows |
| m01-l02 | gap-fill part 2 (recheck-7) PASS 309 · FAIL 22 applied; Normativa additions owed: CE 150, 155 (named in RS 56); Estatuto del Personal de las Cortes Generales (RS 27.6); Reglamento de la Conferencia de Presidentes (RS 56 ter.3) | re-check owed after parts 1–4 |
| m01-l02 | gap-fill part 1 (recheck-6) PASS 308 · FAIL 23 applied; Normativa additions owed: CE 102, 116, 143, 144, 146, 150, 151, 159, 166, 167, DT 1.ª and 6.ª (named in RC); Ley de Procedimiento Administrativo (RC 92.2); LO 2/1982 (RC 199.2); Ley of art. 76.2 CE (LO 5/1984) | re-check owed after parts 1–4 |
| m01-l06 | recheck-4 PASS 12 · FAIL 1 (fe15ff30f4, capítulo I título II range: failed re-check 1 of 2) applied | re-check owed |
| m01-l02 | gap-fill part 3 (recheck-8) PASS 286 · FAIL 45 applied; moves owed (LO 3/1981 15 and 17.3 order; RS 160.2 f) closing paragraph below the table, like RS 92.3 g)); Normativa additions owed: LOTC also named in art. 29 LO 3/1981, LECrim also in art. 20.4 LO 3/1981, CE 55, 103, 143, 144, 146, 150, 155, 159, 167, DT 1.ª | after part 4: one structural fixer, then re-check |
| m03-l15, m03-l04 | recheck-9 PASS 96 and PASS 4 (IAE lists; art. 3.1 a), d) RD 1619/2012) | closed; III.15 and III.4 gap fill complete |
| m01-l02 | gap-fill part 4 (recheck-9) PASS 265 · FAIL 63 applied; all four parts: 1,168 PASS · 153 FAIL; structural fixer running (moves, duplicate 582.1, Normativa additions, art. 93.6 LOPJ) | then one re-check of the ~153 replacements and the new rows |
| m01-l01, m01-l06 | re-checks PASS (recheck-6, -5) | closed; I.1 and I.6 fully through |
| m03-l19 | DA 3.ª Ley 10/2014 saved (sha256 333bd…617c) and stated in the c´) bullet; Normativa line | Opus check owed (the sentence is a cut of DA 3.ª.1 — check it is the norm's words) |
| glossary | g-silencio-administrativo FAIL in recheck-2 (24.1 LPAC «dictase y notificase»; failed re-check 1 of 2), replacement applied | re-check owed |
| summaries | recheck-2 PASS 25 · FAIL 8 (m00-l01, m01-l02, m01-l07, m02-l04, m03-l04, m03-l10, m03-l11, m03-l20), replacements applied to course.yaml | re-check owed (with I.2 and I.7 once their lessons are final) |
| m01-l03 | recheck-6 PASS 10 | closed except the art. 9 notes (9.2.c)/9.4 order, 9.1 Organismos públicos clause, 9.4 «indicarán expresamente») → fixer, then re-check |
| m03-l19 | recheck-8 PASS | closed; III.19 fully through |
| summaries | recheck-3: 6 PASS; m00-l01 and m03-l04 FAIL (failed re-check 1 of 2), replacements applied | re-check owed |
| m01-l02 | recheck-10 PASS 155 · FAIL 11 applied (8 content = failed re-check 1 of 2; 3 Normativa closed under the Normativa ruling + 4 «nombrado en» lines added: Código Civil, LEC, TFUE, TRLPI) | last re-check owed |
| m01-l03 | art. 9 LRJSP block reordered, 9.1 and 9.4 clauses restored (9.4 tense set to the norm's «se considerarán» by coordinator) | re-check owed |
| m01-l07 | Opus part 1 (recheck-1) PASS 172 · FAIL 65 applied | part 2 running; then one re-check |
| m01-l07 | Opus part 2 (recheck-2) PASS 181 · FAIL 56 applied; total I.7 PASS 353 · FAIL 121 of 474; structural fixer running (22 order moves, Normativa) | then one re-check |
| m01-l02 | recheck-11: 6 PASS; 87.7 and 96.2–3 LOPJ dropped (second failed re-check, dropped.md); 88.4 reordered by replacement; Normativa lines closed under the ruling; art. 15.1 LO 3/1981 short repeat removed; LOTC line + art. 5.2 LOPJ | closed |
| m01-l03 | recheck-7: 9.4 PASS; 9.1 FAIL (first) applied | last re-check owed |
| summaries | m00-l01, m03-l04 recheck-4 FAIL (second failed re-check), replacements applied | closed by ruling: a summary cannot be dropped; final text = recheck-4 replacement (for Juanjo) |
| m01-l07 | structural fixer done (moves, Normativa lines) | final re-check owed: rechecks 1–2 replacements + art. 18 RD 365/1995 repeat, c91b1f4f87 lead-in, art. 17 «la», LBRL 92.1 |
| glossary | g-silencio-administrativo rewritten from art. 24.4 and 24.2 LPAC (recheck-4 replacement) → recheck-5 PASS; g-diligencia origin m03-l08 and link_except ×13; g-recusacion and g-oposicion link_except extended; g-mutualista and the complementos PASS | closed |
| m01-l03 | recheck-8 PASS | closed; I.3 fully through |
| m01-l07 | recheck-3 PASS 106 · FAIL 28 applied (11 extra rows by id; 3 repeated art. 18.4–5 sentences dropped with the full art. 18 replacement); Normativa lines closed under the ruling; art. 64.3 a)–d) RD 364/1995 organs absent → pool gap for the handoff | last re-check owed for the content rows (+ line-1326 suspension paragraph placement, line-2380 «(Derogado)», art. 45.2 TRLCPE) |
| m01-l07 | recheck-6 PASS 4; record written | closed; I.7 fully through |
| m03-l01, m03-l02 | gap fill verified (recheck-5..8); records written | closed |
