# Build — III.7 (`m03-l07`), 2026-11-17 (second build; the first, stopped part-way, was discarded)

- Words: HEAD 7,624 (wc) = 6,870 excluding table/esquema rows + 754 in rows (HEAD's own tables). Built excluding rows 12,809 (wc, `:::esquema` directive lines counted as in HEAD); words inside esquema rows 4,607 (pipes not counted). Ratio excluding rows 1.86 × HEAD (6,870); against the 1.6 × target (10,992) 1.17 × over. The target is passed: every article of the ranges keeps its rule, conditions and exceptions, every legal enumeration is an esquema, and nothing was left out for size. HEAD's lettered lists moved into rows (their words leave the prose count), so the real growth of prose is larger than the ratio shows.
- Method: pool paragraph order, HEAD base, only two pool sentences omitted (below). Lettered lists after a citation lead-in became esquemas (`| Elemento | Contenido | Cita |`, one row per sentence of each item, cite = the lead-in's cite); pool bullets with no lead-in became plain paragraphs; no sentence was reworded.
- Sentences added (new to HEAD, prose / rows):
  - (a) 0: no R2b removal in this tema.
  - (b) review item 1 and item 9 (TPC step by step, one esquema of all steps): 44 sentences + 17 rows in «Tasación pericial contradictoria» (arts. 135.1 párr. 2–4, 135.3 LGT; 161.1–5, 162.2–5 RGAT). Review item 2 (control de presentación, beneficios rogados, ejecución de devoluciones): 6 + 10, 12, 2 sentences (arts. 153.2–5, 136.1–3, 137.1–4, 131.2, 132 RGAT).
  - (c) every other article of the ranges, rule/conditions/exceptions sentences: art. 116 RGAT (1); 125.1 second paragraph; 126.2–5, 127.1–3, 128.2 RGAT (15 + rows); 129 RGAT (6 + 14 rows); 130.1 second part, 130.2 RGAT (4); 129.3 LGT third paragraph, 133.1–2 RGAT, 134 RGAT (12 + 12); 57.3, 134.2, 134.4–5 LGT, 157.2, 158.1–3, 159.2–4, 160.1, 160.3, 160.4 RGAT (24 + rows); 164.2, 164.3, 164.5 RGAT; 144–147 RGAT (32 + 27 rows); 154 RGAT (7 + 9 rows). Total new prose sentences 196, new rows 166 (rows include HEAD's own lettered lists now in esquemas).
  - (d) three «No confundir» blocks (TPC 20 % vs 120.000 €/10 %; plazos de alegaciones 10 vs 15 días; verificación vs comprobación limitada): 10 sentences.
  - (e) HEAD sentences replaced by their pool form: l.34 (id `m03-l06` removed → «se tratan en el tema III.6»); l.81 (art. 125.1 RGAT cited on the first sentence); l.109 and l.111 (126.2, 126.3 and 127.4 sentences split per norm, art. 126.2 second half); l.241 (art. 134.4 LGT in full); l.243 (arts. 160.2–160.4 split); l.251 (135.2/135.4 split); l.365 (arts. 136.1–136.4 split); the one-paragraph TPC esquema l.253–258 (repeating l.251) is replaced by the whole-TPC esquema; the caducidad esquema gains the «otras obligaciones formales» row; Normativa lines (LGT and the added «nombrado en» lines as in the pool).
- Enumerations as esquemas (one row per item or sentence): arts. 117.1, 118, 123.1, 130, 131, 133.1, 57.1, 126.4, 127.1, 129.4 (a–f, row per sentence), 159.1, 160.3, 162.1, 136.2, 139.1, 139.2, 144.4, 145.4, 146.1, 147.1, 153.1, 153.6, 154.3, 154.5, 163, 164.2 and the existing HEAD esquemas. Left as lists: art. 127 LGT (three items the pool gives unlettered; no letter is invented) and the arts. 125.2/126.2 LGT plazo cases (a synthesis of two articles, not a list of the norm); art. 147.2–8 RGAT and 158.1–3 RGAT (separate rules, not a list); arts. 162.2–4 RGAT (c, d, e carry their own cites).
- Esquema header: `| Elemento | Contenido | Cita |` (the one lettered-list header that passed blind in another pool; `Letra | Supuesto` did not).
- Pool sentences left out (2), none states a rule, condition or exception of the lesson's range:
  - l.116 «Las solicitudes de rectificación de autoliquidaciones se dirigen al órgano competente de acuerdo con la normativa de organización específica (art. 126.1 RGAT).»: organisational detail (map row «out: organisational detail»).
  - l.375 «El órgano competente para designar un perito tercero es el que se determina en la normativa de organización específica.»: organisational detail.
- build_check: `HEAD 186 · added byte-identical 233 · esquema rows from items 128 · not in pool 1`.
- «Not in pool»: the new RGAT «Normativa» line (`RGAT (RD 1065/2007): arts. 4.2, 9–11, 12.2, 21.3, 24.3, 29.3, 74, 88.2, 116, 122–125, 126.2–5, 127–128, …`), rebuilt from what the lesson cites: art. 126.1 removed (omitted sentence), the rest as the pool line. The other Normativa lines are the pool's, unchanged.
- cites.py: 417 citations, 0 unresolved. `index_sources.py --course aeat-agentes-hacienda`: exit 0, no validation error naming `m03-l07`.
- Readability: `split_paragraphs.py` run (0 paragraphs split).
- Pool gaps (articles of the ranges without a pool sentence): none. Every article of the map has pool sentences, including art. 116 RGAT, 57.3, 134.2, 134.5 LGT, 158.1–3, 161, 162.2–5, 164.2–3, 164.5, 126.4–5, 127.1–3, 128.2, 129, 130.2, 131.2, 132, 133.1, 134, 144–147, 153.2–5, 154 RGAT.
- Glossary sense (review 6, audit item 14: `g-convenio` at the former l.136, `g-interesado` at l.111): not touched (the glossary and `glossary-links.es.txt` are out of scope for this build); the sentence is the same as in HEAD (art. 131.3 RGAT).

## Sentences that do not stand on their own where they now sit

Each is byte-identical to the pool and refers to something placed earlier in the pool's order; the cure is a lead-in or a move, which a builder may not write.

- «En esos casos, el plazo máximo de resolución es el del procedimiento que se esté tramitando (art. 159.3 RGAT).»: «esos casos» are the procedures of art. 159.1 (esquema), separated by the 159.2 paragraph.
- «Antes de abrirlo, la Administración puede acordar…» (art. 155.2 RGAT, HEAD text): «abrirlo» refers to the plazo of the previous sentence.
- «Lo dispuesto en la letra b) del apartado 3…» (art. 134.3.c RGAT) and «Lo dispuesto en los apartados 2 y 3 del artículo 134…» (art. 134.4 RGAT): refer to apartados whose numbers are not visible in the paragraphs.
- «Si el obligado obtuvo previamente el levante de la mercancía conforme a las letras b) y c) del apartado 3…» (art. 134.5 RGAT).
- «En este caso, la liquidación que se dicte toma el valor comprobado…» (art. 161.2 RGAT, third bullet) and «Para ello, el órgano competente remite…» (art. 161.1 RGAT): depend on the previous bullet.
- «En este procedimiento la Administración tributaria puede proceder al examen…» (art. 160.1 RGAT): «este procedimiento» is the comprobación de valores, now after the paragraphs of arts. 134.4–5 LGT.
- «En el supuesto de la letra a)/b)/c), …» (arts. 153.2–4 RGAT): letters of the art. 153.1 esquema.
- «En los supuestos a), b) y c), la baja cautelar se convierte en definitiva…» (art. 144.4 RGAT): letters of the esquema.
- «A estos efectos, cuando se trata de tributos sin periodo impositivo…» (art. 137.3 RGAT) and «Dicho órgano puede declarar…» (art. 137.2 RGAT).
- «c)/d)/e) La liquidación que se dicte…» (arts. 162.2–4 RGAT): letters of the art. 162.1 esquema.
- «A los efectos de lo dispuesto en este apartado se aplica…» (art. 164.2 RGAT, third sentence of its paragraph).
- «En ese caso se notifica esta circunstancia al perito tercero…» (art. 161.5 RGAT, third bullet).
- «Cuando se han realizado las actuaciones del apartado 2 y los datos o valores…» (art. 129.3 LGT, HEAD text).
