# Build — III.12 (`m03-l12`), R2d, 2026-11-17

Words (`wc -w`): HEAD 10,048 (esquema rows 785; 9,263 without) → built 21,766 (esquema rows 5,503; 16,263 without).
Ratio excluding rows: 1.76 to HEAD without rows (2.17 to HEAD's 10,048); 1.10 of the 1.6 target (14,821). Above the
target: the range holds some 75 articles (LGT 162, 169–172, 174–177; RGR 10, 75–116, 124–127; LEC 605–607); each one
states its rule, conditions and exceptions, and every legal enumeration is an esquema.

## Sentences added (not in HEAD): 262 prose + 125 esquema rows

- (a) R2b removals: none inside the range (R2b removed no section of m03-l12); the art. 167.3 LGT pointer is item (b)/(d).
- (b) Review item 1 (broken pointer to III.11): the pointer sentence now reads «están en el tema III.11» (no id) and the
  art. 167.3 / 170.3 motivos stand in the «No confundir» block. Review item 3 (glossary) is a coordinator edit.
- (c) Articles not or partly treated, about 215 prose sentences and the rows: arts. 10.2, 76.1–3, 77, 79.1, 79.3–6, 80.2–4, 80.6,
  81, 82.1–3, 83.3, 84.2–3, 86–88 bis.2, 89–93, 94.4, 95.1–2, 96.2, 97.2–5, 97.7–8, 98, 99, 100.3–5, 101.2–4, 102, 103,
  103 bis.2–4, 103 ter, 104.1–3, 104 bis.1–4, 105.2–3, 106.2–3, 107.2–10, 109–112, 113–116, 124.1–4, 124 bis, 125, 126,
  127.1–6 RGR; LGT 170.5, 170.6, 171.1, 174.5; LEC 607.3–6. 
  Left out (each because it is development, procedure or repetition, not the rule, a condition or an exception; none for size):
  76.1 «Lo anterior se efectúa…» (cross-reference to arts. 142/146 LGT); 77.2 proposal and authorisation of the
  subrogación (procedure); 79.3 notice of the retention plazo (procedure); 80.2 «forma, medio y lugar convenidos»
  (convenio detail, repeated in 81 and 82.1); 80.3 custody of the títulos with the póliza (development); 81 and 82.1
  «forma, medio y lugar convenidos» (repetition); 86.1 return and filing of the copies (procedure); 88.1 files attached
  to the expediente and 88.3 communication of reiterated dilaciones (procedure); 93.2 prior traba noted by the gestoras
  (procedure); 95.2 «el nombramiento fija la clase y cuantía de las operaciones» (development); 97.2 fichero de
  expertos (optional development); 97.5 content of the creditors' answer, two sentences (procedure); 101.4 media of
  difusión (development); 103.2 forms of alta and the warning to the new user (procedure); 104.2 publication of the
  puja (procedure); 111.1 correction of defects (procedure); 109.2 notification of the adjudicación (procedure);
  114.1 payment of the honorarios (procedure); 115.4 content of the justificante (procedure); 126.3 content of the
  request (procedure). The rest of the pool's sentences for these articles are in.
- (d) «No confundir» blocks: art. 167.3 / 170.3 LGT (new); arts. 175.1 / 176 LGT (new); arts. 101.2 / 104.2 RGR (the
  pool's block, HEAD sentences).
- (e) HEAD sentences replaced by their pool form: l. 3 (RGR article ranges), l. 7, 119 and 339 (ids removed), l. 98
  (art. 76.1), l. 123 (art. 170.5 completed), l. 145 (art. 79.3 places), l. 167 (art. 83.1 whole), l. 241 (art. 97.7
  whole), l. 265 (art. 101.4 whole), l. 271–272 (art. 103 bis.1), l. 284 (art. 104 bis.3), l. 306 (art. 105.2.a),
  l. 329 (art. 107.3), l. 385 (arts. 127.2 and 127.4), l. 398 («Lo que más cae» line on art. 85) and the three
  Normativa lines.

## Enumerations as esquemas (25, 125 rows from items; header «Elemento | Contenido | Cita»)

art. 169.1 a)–d); 169.2 a)–i); 605 LEC 1.º–4.º; 606 LEC 1.º–5.º; 170.3 a)–d); 79.3 a)–b); 83.1 a)–g); 84.3 a)–d);
85 a)–f); 90.3 a)–e); 94.3 a)–e); 97.6 and 97.7 a)–b) with 1.º–2.º sub-items; 101.4 a)–g); 103 bis.1 a)–b); 104 bis.3
a)–f); 105.2 a)–e); 106.1; 107.1; 107.4; 113.2 a)–f); 114.3 a)–c); 116.3 a)–c); 174.4 a)–c); 175.1 a)–b). Items with
two sentences give two rows with the same label. Already in the pool as tables and copied whole: the 607.2 scale,
the tercería plazos, the subasta plazos (with five added rows from items), the 127.1 and 127.4 plazos.

## Checks

- build_check: `m03-l12: HEAD 220 · added byte-identical 262 · esquema rows from items 125 · not in pool 1`.
- cites.py: 565 citations, 0 unresolved. index_sources: see the final report.
- split_paragraphs: 29 paragraphs split.
- «Lo que más cae»: HEAD's ten lines; the art. 85 line is the pool's (e).
- Not in pool (1): the RGR «Normativa» line, which is the pool's with three ranges narrowed to what the built lesson cites
  (`88.1–3` → `88.1–2`; `115.1–6` → `115.1–3, 115.5–6`; `126.1–4` → `126.1–2, 126.4`).
