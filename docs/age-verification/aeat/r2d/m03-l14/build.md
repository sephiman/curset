# Build — III.14 (`m03-l14`), R2d, 2026-11-17

Words (`wc -w`): HEAD 8,571 (of which esquema rows 960; 7,611 without) → built 28,261 (esquema rows 5,614; 22,647
without). Ratio excluding rows: 2.98 to HEAD without rows; 1.86 of the 1.6 target (12,178). Above the target: the range
holds 125 articles (65 not treated at HEAD); every article states its rule, conditions and exceptions, and every new
legal enumeration is an esquema (rows excluded from the count). Nothing is left out for size.

## Sentences added (not in HEAD): 341 prose + 147 esquema rows (98 built from list items, 49 from the pool's four tables)

- (a) R2b removals: none (the map lists none for this tema).
- (b) Review items 1 and 2: art. 241 ter.1–8 LGT (8 sentences, with its row in the interposición esquema) and ejecución de resoluciones (arts. 239.3 paragraphs 2–4, 239.7, 225.3 LGT; arts. 66–71 RGRVA): 35 prose sentences.
- (c) Articles not or partly treated (arts. 2–20, 21–27, 38–65 RGRVA; arts. 223–225, 228–247 LGT; disp. adic. 11.ª, 13.ª, 21.ª; TEA organisation arts. 28–37 RGRVA): 281 prose sentences.
- (d) «No confundir» blocks: plazos para resolver; recurso de anulación / contra la ejecución; revocación / rectificación de errores (3 blocks, 10 sentences with the labels).
- (e) HEAD sentences replaced by their pool form: the art. 229.1 lead-in without «entre otros supuestos» and its four items, art. 35.1.e, art. 230.1 lead-in and 230.3, art. 233.3, art. 239.4, recurso de anulación, art. 242.3, art. 244.4, art. 246.2, «Lo que más cae» art. 221.1 line: 19 sentences.
- Normativa: the LGT and RGRVA lines rebuilt from what the lesson cites (2 new lines).

## Enumerations as esquemas (98 rows from items)

art. 215.2 a)–f); art. 2.1 RGRVA a)–f); art. 14.1 RGRVA a)–c); art. 14.2 RGRVA a)–c); art. 14.2.c RGRVA 1.º–4.º; art. 15.1
RGRVA a)–f); art. 16 RGRVA a)–c); art. 17.2 RGRVA a)–c); art. 25.1 RGRVA a)–b); disp. adic. 11.ª.1 a)–b), .2 a)–c), .4 a)–e) LGT;
art. 229.4 a)–c) LGT; art. 35.1 RGRVA a)–g); disp. adic. 13.ª.1 a)–b) LGT; art. 230.1 a)–d) LGT; art. 39.2 RGRVA a)–d); art. 40.2
RGRVA a)–d); art. 45 RGRVA a)–b); art. 52.3 RGRVA a)–c); art. 239.4 a)–f) LGT; art. 239.6 1.ª–3.ª LGT; art. 243.2 LGT (six items);
art. 246.1 a)–b) LGT. Items with a second sentence become two rows with the same marker. The pool's four esquemas (TEAR/TEAL and
salas desconcentradas, plazos de interposición, plazos de resolución, plazos de procedimientos especiales) are copied whole,
including the 241 ter row. Already-listed HEAD enumerations (arts. 216, 217.1, 227, 229.1 a)–d), …) stay as bullets, now with the
pool's corrected items for 229.1.

## Checks

- build_check: `m03-l14: HEAD 244 · added byte-identical 394 · esquema rows from items 98 · not in pool 2` — the two are the new
  «Normativa» LGT and RGRVA lines.
- cites.py: 646 citations, 0 unresolved.
- split_paragraphs: 0 paragraphs split.
- index_sources: see the builder's final report.

## Pool sentences left out (each: development, procedure or repetition, not rule/condition/exception)

- art. 5.2 RGRVA (copia cotejada and informe requested), 5.4 (propuesta de resolución): procedure.
- art. 8.2 RGRVA, art. 11.2 RGRVA: the órgano remits a copia cotejada of the expediente within 10 days: procedure.
- art. 17.3 RGRVA (notification of the initiation/propuesta), art. 18.1 RGRVA (checks the órgano makes): procedure.
- arts. 29.3–29.6, 29.10 and 30.4–30.6, 30.8, 30.10, 30.13 RGRVA: substitution of presidents and vocales, the president's
  agreement on salas, proposal of resolutions, ponentes, delegation: internal functioning of the tribunals (development).
- art. 34.3 RGRVA (one acta per meeting): development of art. 34.1–2, which is kept.
- art. 233.15 LGT, art. 236.3 LGT second sentence, art. 234.6 LGT: remission to the reglamento.
- art. 44.4 RGRVA (content of the resolution granting the suspension), art. 47.1 RGRVA (informe of the órgano de recaudación): procedure.
- art. 50.3 RGRVA (two sentences: domicilio and paper notification): notification mechanics, development of arts. 50.1–2, which are kept.
- The two opening sentences of the pool (HEAD sentences) are kept as in HEAD.

## Not in pool

- l.1005: the «Normativa» LGT line (rebuilt from the built lesson's citations).
- l.1006: the «Normativa» RGRVA line (same).
