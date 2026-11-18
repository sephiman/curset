# Build — III.3 (`m03-l03`), R2d, 2026-11-17

The pool (`expansion/m03-l03.md`) is HEAD's lesson with every verified addition and correction in the norm's order; the build is the pool whole, with the two new legal lists turned into esquemas (script `scratchpad/b03/build.py`, which writes the pool lines byte-identical). `split_paragraphs.py`: 0 paragraphs split.

## Size
- Words (`wc -w`): HEAD 5,714 = 4,785 excluding esquema rows + 929 in rows. Built 6,599 = 6,197 excluding rows + 402 in rows.
- Ratio excluding rows: 1.30 × HEAD (4,785); 0.81 of the 1.6 target (7,656). Under target.

## Sentences added (not in HEAD): 44 prose + 7 esquema rows
- (a) R2b removals: none (the map lists none).
- (b) Confirmed review items: none needing new sentences. Item 7 (the two non-norm sentences, l. 76 first and l. 92 last) and item 4 (the two repeating esquemas, l. 129–134 and l. 157–168) are handled by leaving them out: neither is in the pool. Item 2: HEAD carries no g-convenio mark.
- (c) Articles HEAD did not treat or treated in part (about 36 prose sentences): art. 1.1 second clause cut at HEAD is now in (e); 1.2 (three), 2.1 second sentence, 6, 9.1–9.2, 10.2 split, 12.3 (three), 17.4, DA 1.ª.1–2 (six), 26.4 second sentence, 26.5 (two), 27.2 last párrafo, 27.3, 51 (two), 52, 53.1–53.3 (lead-ins; items as rows), 56.2.
- (d) «No confundir»: 3 blocks, 6 sentences (art. 27.2 vs 28.2–4; art. 20.2 vs 22; art. 50.1 vs 54).
- (e) HEAD sentences replaced by the pool form: art. 1.1 first sentence (with «en virtud y con el alcance … 149.1.1.ª, 8.ª, 14.ª y 18.ª de la Constitución»); art. 10.2 first sentence (now with the «y se aplican a los tributos sin período impositivo…» clause). HEAD's «Normativa» replaced by the pool's (adds CE, arts. 1.2, 6, 9, 10.2, 12.3, 17.4, 26.4–5, 27.3, 51–53, 56.2, 88.5, 158, 29 bis, DA 1.ª; keeps the other lines).
- HEAD sentences not in the built lesson: l. 76 first sentence, l. 92 last sentence (not text of the norm), the esquemas «Interés de demora y interés legal del dinero para 2026» (repeated the paragraph) and «Algunas reglas del artículo 27 LGT…» (repeated the prose, title incomplete).

## Enumerations as esquemas
art. 53.1 LGT a)–d) (4 rows) and art. 53.2 LGT a)–c) (3 rows), header `| Elemento | Contenido | Cita |`, row cite = the lead-in's. Already whole at HEAD and kept as lists: arts. 7.1, 8, 15.1, 26.2, 27.2, 50.2, 56.1, 58.2 LGT (the 50.2, 56.1 and 58.2 ones also under the HEAD esquema «De la base imponible a la cuota diferencial», kept). Art. 1.1 (four constitutional titles) and art. 26.4 («entre otros supuestos», three cases) are enumerated inside one verified sentence each and stay there. «Entre otros/otras» kept as the law's own: arts. 24.2 and 26.2.

## Pool gaps
None: every article of the ranges has pool sentences (arts. 5, 28, 29, 29 bis, 57 are outside the epígrafes).

## Pool sentences left out
None: every pool sentence states a rule, condition or exception or is a verified lead-in.

## Sentences that do not stand on their own where they now sit
- Art. 12.3, third bullet «Se publican en el boletín oficial que corresponda» (subject is the disposiciones of the two previous bullets).
- DA 1.ª.2 bullets «Pueden tener carácter tributario o no tributario», «En particular, se consideran…» and «En concreto, tienen tal consideración…» (depend on the preceding bullet).
- Art. 1.2 bullets «Se entiende por asistencia mutua…» and «La asistencia mutua puede comprender…» (follow the first bullet).
- Art. 27.2 last párrafo «Lo dispuesto en el apartado 2 no impide…» (the apartado is the previous paragraphs of the same article).
- Art. 51 «A estos efectos, la Administración tributaria utiliza…» (follows the previous sentence).

## build_check line
`m03-l03: HEAD 177 · added byte-identical 44 · esquema rows from items 7 · not in pool 0`

cites.py: 163 citations, 0 unresolved. `index_sources.py --course aeat-agentes-hacienda`: result in the final report (run last).
