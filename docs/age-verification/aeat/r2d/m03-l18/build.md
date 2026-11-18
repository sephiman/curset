# Build — `m03-l18` (III.18, IVA I), 2026-11-17, reworked

## Size

| | words |
|---|---|
| HEAD, excluding esquema rows | 6092 (wc -w 6276 with the HEAD esquema) |
| Built, excluding esquema rows | 9656 |
| Esquema rows, built | 22729 (HEAD: 184) |

Ratio to HEAD (excl. rows): 1.59. Ratio to the 1.6 target: 0.99. The first build was 21920 words (3.60 ×): category (c)
took about 365 sentences and the nested enumerations stayed as long bullet lists. The rework removed whole sentences
only (no sentence cut inside) and moved every nested enumeration into an esquema.

## Rework

- (c) articles keep the whole sentences that state their rule, conditions and exceptions. Nothing is left out for size.
  The 11 pool sentences left out of the added articles, each because it states no rule, condition or exception:
  - 8 bis: «la determinación del valor intrínseco … términos previstos en la legislación aduanera» (development: it
    points to customs law; the 150-euro condition is in the esquema).
  - 9.1.º c): «Los sectores diferenciados … los define el propio artículo 9.1.º c)» (pointer to III.19, no rule).
  - RIVA 6 (second sentence): «En cualquier caso, las exenciones … se aplicarán siempre que se cumplan los requisitos
    del apartado tres…» (repetition of the art. 20.Tres paragraph already kept).
  - Art. 22.Nueve: «En particular, se incluirán … la Comunidad Europea, … el Banco Central Europeo» and «Asimismo, se
    incluirán … pandemia de COVID-19» (development: examples of the rule already stated).
  - Art. 22.Trece: «Se entenderán incluidos … vuelos de conexión aérea» (development of the rule).
  - RIVA 11.2: «el adquirente … podrán utilizar el formulario disponible … sede electrónica» (procedure).
  - Art. 24.Dos: «El régimen fiscal de perfeccionamiento activo se autorizará …», «El régimen fiscal de importación
    temporal se autorizará …» and «el régimen de depósito distinto de los aduaneros será el definido en el apartado
    quinto del Anexo» (definitions of regimes the rule only names; development).
  - RIVA 22: «Dicha justificación podrá efectuarse, en particular, mediante … justificantes de declaración-liquidación»
    (procedure: evidence means).
  A sentence stays wherever its paragraph's citation sits only on it (RIVA 1, 9 bis.Cinco, RIVA 8.2, 13.2–13.3 RIVA,
  23.Dos, 73.Dos, 68.Cinco, 20.Tres), so no «Normativa» range changed. Everything else the first build held in prose
  for these articles is either kept or is an esquema row.
- Protected units keep their full text: 7.2.º, 7.5.º, 7.6.º, 8.Dos 3.º–7.º, 9.1.º a)–c), 12, 13.2.ª, 20.Uno.5.º, 18.º a),
  22.º A), 20.Dos, 21.2.º (embarcaciones deportivas), «Lo que más cae».
- Nested enumerations are esquemas, one row per item or sub-item (a multi-sentence item gives several rows with the same
  label), cell text as in the pool, citation of the lead-in repeated: art. 7 (52 rows), 8.Tres (10), 13 (10),
  20.Uno (146), 21 (22), RIVA 9.1 (57), 24.Uno (17), 68.Dos and 68.Tres (23), 69.Tres (20), 70.Uno (40). The prose keeps
  the verified lead-in sentence of each.

## Sentences added (165 prose sentences, 579 esquema rows; 85 HEAD sentences replaced by their pool form)

- (a) R2b removals: 0 (the map has none for this tema).
- (b) Review items: about 219 units (art. 20.Uno 1.º–28.º whole, 146 rows; 21.2.º A) viajeros, 7; RIVA 9.1.2.º B), 14;
  70.Uno.4.º and 6.º–9.º, 18; art. 7 items (7.1.º a)–c), 7.8.º B)–F), 10.º, 11.º), 29; art. 72, 5).
- (c) Articles HEAD did not treat or treated in part: about 142 prose sentences (rule, conditions, exceptions of
  5.Cuatro, 8 bis, 9 bis, 10, 20.Tres, 20.Uno.22.º A) and B), 20 bis, 21–25, 68.Cuatro–Seis, 71, 73, RIVA 1, 1 bis, 4,
  6–13, 22, 23) and about 300 esquema rows (enumerations of 3.Dos.1.º, 5.Cuatro, 6, 8.Tres, 8 bis, 9, 9 bis, 11.Dos,
  13.1.ª, 20.Tres, 20.Uno.22.º, 22, RIVA 10, 12, 13, 23, 68, 69, 70.Dos). Normativa: 12 lines, the pool's own.
- (d) «No confundir»: 3 blocks, 9 sentences.
- (e) HEAD sentences replaced by their pool form: 85 (the «entre otras» enumerations of arts. 6, 7, 11, 13.1.ª, 20.Uno, 21,
  22, 68, 69, 70, 3.Dos.1.º, the id `m03-l19`); some of them now sit as esquema rows. HEAD sentences kept as they were:
  140 (including 13.2.ª, 8.Dos and 12 lists).

## Esquemas

54 in all (43 of the first build plus 11 for the nested enumerations). Short lists (2–3 rows) stay esquemas. HEAD's
flat lists (arts. 1, 4.Dos, 5.Uno, 8.Dos, 12, 13.2.ª) stay HEAD bullets.

## Checks

- build_check: `m03-l18: HEAD 140 · added byte-identical 165 · esquema rows from items 579 · not in pool 0`.
- cites.py: 782 citations, 0 unresolved.
- split_paragraphs: 0 paragraphs split.
- index_sources (`--course aeat-agentes-hacienda`): ran to the end (exit 0), no validation error.

## «not in pool»

None.

## Notes

- «Normativa»: the pool's lines kept (every article they list is still cited); no new line. «Lo que más cae»: HEAD's ten lines.
- A row whose item is shorter than 15 characters keeps its marker in the cell (`21.º (Suprimida)`), so the check finds it.
- Open for the glossary step: `g-convenio` at l. 12–13 (Convenio Económico) is not touched here.
