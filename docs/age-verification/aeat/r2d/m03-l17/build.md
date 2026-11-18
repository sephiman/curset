# Build — `m03-l17` (R2d, 2026-11-17)

- Words: HEAD 9476 (8562 excl. esquema rows, 914 in rows) → built 23314 (16893 excl. rows, 6421 in rows). Ratio excl. rows:
  1.78 × HEAD wc (9476) and 1.97 × HEAD excl. rows (8562); the 1.6 target (15162) is passed by about 1730 words (1.11 × target).
  The pool is 2.4 × HEAD, so the lesson is the pool minus the sentences listed under «Left out».
- Sentences added (≈ 367 units over HEAD, 171 of them esquema rows): (a) none (the map records no R2b removal in this tema);
  (b) art. 30 bis LIS whole (16 prose units, 11 rows), art. 15 whole as esquema a)–n) (23 rows), the 2027 line (arts. 29.1 and DT 44.ª.3),
  9.1 f)–h), 29.4, 25.1 no disposición a)–c), 25.2 a)–g), 26.4 c) 1.º–4.º, 23.3 c)–d), 23.5 whole; (c) every other article of the ranges
  (arts. 5.1–2, 8.1, 11.8–13, 12, 13, 14, 15 bis, 16, 17.2–11, 18, 19, 21, 22, 23.2/23.4, 25.3, 31.4, 32.2, 33.4–6, 41, 101, 105, 111, 118–123,
  DA 15.ª.2, RIS 1, 3–7, 13–20, 57, 58); (d) the three «No confundir» blocks (límites de compensación y de reserva de capitalización;
  Ceuta y Melilla IS/IRPF; plazos 10 / 4 años); (e) HEAD sentences replaced by pool versions: 9.1 lead-in, 11.3.1.º («No obstante…»),
  23.3 lead-in, 23.5 (inline sentence → list), 25.2 lead-in, 26.4 c), 29.4 lead-in, 33.3 lead-in, the pago fraccionado remission (without
  `m03-l06`), «Lo que más cae» item 8 (colegios profesionales), Normativa lines of norms still named. The two «Fuera del enunciado literal»
  notes (arts. 17 and 20) are gone; the one on «Pago fraccionado» stays (pool wording).
- HEAD summaries replaced by the article's own rule sentences: «Las letras f) y g) añaden determinados organismos…» (9.1 f)–h) rows)
  and «Los apartados 8 a 10, 12 y 13 del artículo 11 regulan…» (11.8–11.13, one sentence of rule each).
- Enumerations as esquemas (new): 5.2, 12.1, 12.1.a table (coeficientes), 12.3, 13.1 (a–d and 1.º–3.º), 13.2, 15, 16.6, 17.4, 18.2, 18.3 (two),
  18.4, 21.11, 23.5, 25.1 (no disposición), 25.2, 30 bis.1, 30 bis.2, 33.4, 41, 111.2, 119.1. Multi-sentence items: one row per sentence,
  same marker (first row carries the item's first sentence without the marker). HEAD lists stay lists and gained items (9.1 a)–h), 23.3 a)–d),
  26.4 c) 1.º–4.º nested). Kept as the pool's nested list, not an esquema: 29.4 a)–e) (its lead-in «Tributan al tipo del 1 por ciento
  (art. 29.4 LIS):» is a bullet fused with its sub-items in the splitter, so it is not a sentence of its own and cannot sit as a lead-in).
  In-sentence enumerations kept whole in prose: 14.3 a)–e), 13.2 b) 1.ª–2.ª, 15 i) 1.º–2.º, 15 k) 1.º–2.º, 29.4 d) 1.ª–3.ª.
- Esquema header row: `| Elemento | Contenido | Cita |` (HEAD's own); the coefficient table keeps the pool's four-column header.
- Left out (pool sentences that do not state a rule, condition or exception: procedure): art. 4.2 RIS (turnos, formula); arts. 7.6, 7.7, 7.10
  RIS (plazo de resolución, silencio, extensión a otros elementos); arts. 1.6–1.7 and 2 RIS (plazo del procedimiento, órgano competente);
  art. 18.9 LIS (acuerdos previos de valoración); arts. 23.6–23.7 LIS (acuerdos previos). Normativa edited to match: 18.9–10 → 18.10,
  23.1–7 → 23.1–5, RIS 1.1, 1.3, 3.2–3, 4.1, 5.1, 6.1, 7.1, 13–20, 21–44, 57.1, 57.3, 58.
- Not taken from the pool because they are not in HEAD and have no place: art. 8.3 LIS is in HEAD's domicilio fiscal paragraph; arts. 102–104 and
  35–39 LIS, art. 100.10 stay out per the map.
- build_check: `m03-l17: HEAD 261 · added byte-identical 228 · esquema rows from items 137 · not in pool 2`
- «not in pool» (the two new Normativa lines, edited from the pool's): LIS line (18.10, 23.1–5 instead of 18.9–10, 23.1–7) and RIS line
  (1.1, 1.3, 3.2–3, 4.1, 5.1, 6.1, 7.1, 13–20, 21–44, 57.1, 57.3 y 58).
- cites.py: 524 citations, 0 unresolved. index_sources: no validation error.
- Glossary: not touched in this round of the build (review items 8–9, `g-convenio` at l. 9 and `g-servicios-comunes` at l. 70, remain for the
  glossary pass).

## Sentences that do not stand on their own where they now sit

All depend on a list or esquema that is the thing they refer to; each is whole and cited, but a reader meets the antecedent only by looking up.
- 12.3 closing: «Las cantidades aplicadas a la libertad de amortización minoran…» (after the 12.3 esquema).
- 17.5 three sentences «En los supuestos de las letras a), b), c) y d) del artículo 17.4…», «En los supuestos de las letras e) y f)…» (after the 17.4 esquema).
- 13.2: «En el supuesto de la letra b), son deducibles siempre que…» (letters of the 13.2 esquema).
- 18.2: «La mención a los administradores incluye…» and «Cuando la vinculación se define…» (after the 18.2 esquema, no lead-in of their own).
- 21.3: «El requisito de la letra a) del apartado 1 debe cumplirse el día…» (letters of the 21.1 esquema).
- 23.4: «Esta reducción se tiene en cuenta…» (reduction of 23.1, after the 23.3 list).
- 25.2: «Esas partidas tampoco se tienen en cuenta…» (the partidas of the esquema above).
- 30 bis.1 rows «El porcentaje es el 10 por ciento…», «Tratándose de entidades… el porcentaje es…» (the percentage of the 15 % rule, which sits in the sentence before the lead-in).
- 30 bis.3: «Las cantidades no deducidas por aplicación de las reglas anteriores…» (30 bis.1–2 esquemas above).
- 33.4: «El porcentaje de la letra c) solo es aplicable…» (letters of the 33.4 esquema); 33.6 «El importe máximo de rentas con derecho a bonificación…».
- 41: «Cuando esos conceptos superen el importe de la cuota líquida…» (a)–c) esquema above).
- Second and later sentences of multi-sentence items shown as separate rows (marker repeated): 5.2 d), 12.1 a)–d), 12.3 b), e), 15 a), b), e), 17.4 a),
  18.3 b), 21.1 a), b), 33.4 b), 111.2 a), 30 bis.2 a), b) — each repeats the marker of its item, which is how the splitter reads them.
- 30 bis.1 «Esa cuota tiene el carácter de cuota líquida mínima» (needs the preceding sentence).
