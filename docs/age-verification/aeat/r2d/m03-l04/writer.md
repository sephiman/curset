# Writer notes — III.4 (m03-l04)
1. Work list: 1 done (RGAT 30–35 whole; 36 is «(Suprimido)»; 37–54 ter first apartado each, 39 quater marked RDL 29/2026, art. 49 BOE warning); 2 done (DA 5.ª LGT whole, RGAT 2.1–2.5, 3.3–3.12, 9, 10, 11 bis–16, Orden EHA/1274/2007 arts. 1–3, 11, 14); 3 done (19.3, 20.2, 21–28; 24–28 first apartado only); 4 done (RD 1619/2012 arts. 1–24, 8 bis; 15.4–6; with the RD 238/2026 deferral note); 5 done (RGAT 29.3–4, RIVA 61.1, 62.3–5, 63–66 apartado 1, 69, 70, 71.3, RIRPF 68.6–9, CCom 25, 28, 29, 31, LIVA 164.Uno–166, LIRPF 104, LIS 120); 6 done (l. 73 sentence replaced by whole 71.3); 7 done (RD 1676/2009 arts. 1–17); 8 done (40.2, 41.4, 46.4–5, 48.3, RGAT 110.2, 111.3–4 and 7, 112.2–3 and 6–7, 17.4, 59.1–5, 148–152); 9 done (66 bis.2 later párrafos and .3, 31.2, 32.1, 32.3, 33.1, 33.3, 29 bis) plus coordinator note RGRVA 72–79; 10 three «No confundir»; 11 done (both esquemas removed; long paragraphs of several cited sentences turned into lists automatically); 12 glossary not mine; 13 done.
2. Words 12,741 -> 57,559.
3. Not treated: RGAT arts. 4–8 (contenido del censo), 23 bis-type details of 24–28 beyond apartado 1, RIVA 62 bis–68 bis beyond 63–66.1, RIVA 71 beyond 71.3, RIRPF 68 already whole, 64.1 apartados 2+ of 63–66.
4. Enumerations completed: DA 5.ª.3 a)–k), art. 3.3 RGAT, 6.1 and 7 RD 1619/2012, 2.2 RD 1619/2012, 71.3 RIVA, 164.Uno LIVA, 3.1 RD 1676/2009.
5. «No confundir»: solidarios / subsidiarios (42.1–2, 43.1, 41.2, 41.5); 67.2 plazos; 46.7 LGT / 112.1 RGAT.
6. Deleted: the two esquemas, the «entre otros» sentence (named). Letter items «(Sin contenido)» dropped.
7. Facts with no pack question: several hundred.
8–9. Glossary none; course.yaml summary: add declaraciones informativas, censos, NIF, facturación, reembolso de garantías.
10. Intro names the added norms. Cambio pendiente: RDL 29/2026 (art. 39 quater RGAT), RD 238/2026 (arts. 8.1, 8 bis, 9, 10 RD 1619/2012; RD 238/2026 is not a normativa.yaml entry so it is mentioned in prose only). Cross-reference fixes owed: none.

## Fix pass (verifier notes)

- RD 1619/2012 collision: the sentences already say «(el real decreto, no el Reglamento que aprueba)» / «art. N del Real Decreto 1619/2012, no del Reglamento»; the Normativa line is now two lines, «RD 1619/2012 (real decreto)» (arts. 1, 2.2, 3) and «RD 1619/2012 (Reglamento de facturación)». Cited text left as is; cites.py resolves all 866 citations.
- Normativa: «nombrado en» lines for norms with an entry (Ley 7/2022, Ley 4/2020, Ley 49/2002, TRLIRNR, Ley 19/1991, LIRPF additional, LOFCA, Ley 25/2003, Concierto, Código Civil, LEC, Ley 40/2015, TREBEP, Ley 30/1992) and one final line for ~30 norms without an entry. LIVA already lists art. 164 whole.
- Not done: RGAT note in normativa.yaml (art. 49 vs 49 ter) is the coordinator's.


## Reduction pass (2026-11-17)

- Protected articles (kept whole, pack «Norma» lines and «Lo que más cae»): LGT 34, 35, 37, 38, 39, 43, 46, 48, 66, 66 bis, 67, 68, 69, DA 6.ª; RGAT 3, 11, 19, 20, 29, 59, 70, 73, 75, 111, 112, 113; Orden EHA/1274/2007 art. 14; RD 1619/2012 arts. 3, 4, 15; RIVA 40, 61, 62, 69 bis, 71; RIRPF 68; Código de Comercio 30; RD 1676/2009 art. 4.
- Method: script over the R2d-added blocks only (HEAD text untouched). Every other article added in R2d keeps at most its first four sentences (about 170 words), each cut paragraph ending with its own citation; lead-ins of lists, «El artículo N del X regula:» lines, headings, «No confundir» blocks, worked examples, «Lo que más cae» and «Normativa» untouched.
- Enumerations moved to esquemas (flat table, one row per item with its letter or ordinal, nested items flattened with their path, «Cita» = the lead-in's citation, item-level citations dropped from the cells): 60.
- Words (wc -w): 57,992 -> 52,404. Esquema markup (pipes and the repeated «Cita» column) counts as words, so the net cut is smaller than the prose removed.
- Per reduced article, words before -> after (cut by more than 10 words):
  - 1619/2012 5: 354 -> 207
  - 1619/2012 6: 728 -> 268
  - 1619/2012 7: 469 -> 240
  - 1619/2012 8: 287 -> 142
  - 1676/2009 10: 690 -> 251
  - 1676/2009 12: 223 -> 161
  - 1676/2009 5: 279 -> 133
  - 1676/2009 7: 469 -> 219
  - 1676/2009 8: 501 -> 169
  - 1676/2009 9: 445 -> 169
  - Comercio 28: 113 -> 70
  - EHA/1274/2007 11: 307 -> 220
  - EHA/1274/2007 2: 490 -> 215
  - LGT 31: 337 -> 161
  - LGT 36: 142 -> 118
  - LGT 40: 289 -> 199
  - LGT 41: 428 -> 208
  - LIRPF 104: 305 -> 152
  - LIS 120: 336 -> 174
  - LIVA 164: 623 -> 75
  - LIVA 165: 222 -> 105
  - LIVA 166: 113 -> 47
  - RGAT 10: 464 -> 285
  - RGAT 12: 332 -> 193
  - RGAT 149: 314 -> 180
  - RGAT 150: 120 -> 91
  - RGAT 151: 242 -> 178
  - RGAT 152: 345 -> 185
  - RGAT 17: 254 -> 190
  - RGAT 2: 248 -> 150
  - RGAT 21: 265 -> 165
  - RGAT 23: 334 -> 163
  - RGAT 26: 160 -> 123
  - RGAT 30: 495 -> 226
  - RGAT 31: 603 -> 218
  - RGAT 32: 83 -> 11
  - RGAT 33: 923 -> 231
  - RGAT 34: 455 -> 226
  - RGAT 35: 502 -> 225
  - RGAT 37: 251 -> 177
  - RGAT 38: 279 -> 267
  - RGAT 42 quater: 303 -> 203
  - RGAT 42 ter: 343 -> 238
  - RGAT 49: 160 -> 139
  - RGRVA 74: 140 -> 81
  - RGRVA 77: 178 -> 141
  - RGRVA 78: 175 -> 153
  - RIVA 69: 269 -> 187
- cites.py: 0 unresolved; index_sources.py --course aeat-agentes-hacienda: no validation error.

## Reduction pass — DISCARDED (2026-11-17)

Juanjo stopped the reduction pass and discarded its output. The lesson was restored to the verified expansion
(`r2d/expansion/m03-l04.md`) and is rebuilt from HEAD by the build pass (`r2d/spec-build.md`). The notes above about
the reduction describe no text now in the lesson.
