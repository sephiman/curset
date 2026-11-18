# Build — III.6 (`m03-l06`), R2d, 2026-11-17 (second build; the first was stopped and discarded)

- Words (`wc -w`): HEAD 5,484 = 4,405 excluding table/esquema rows + 1,079 in rows. Built 22,121 = 12,635 excluding rows + 9,486 in rows (HEAD's own tables and the pool's tables included; the new esquema rows are about 8,400 of them). Ratio excluding rows: 2.87 × HEAD (4,405); against the 1.6 × target (7,048) it is 1.79 × over. The target is passed: the pool is the whole expansion (22.8k words) and every article of the ranges stays at its rule, conditions and exceptions, every legal enumeration is an esquema.
- Method: HEAD text written first; the build keeps every HEAD sentence except those the pool holds in corrected form, and adds pool sentences byte-identical. Esquema rows are built from the pool's list items (one row per item, per sentence when an item has several, per sub-item for the nested 1.º/2.º and a)–d) ones).
- Sentences added (new to HEAD, approximate): (a) 0 (no R2b removal in this tema); (b) review items 1–5: art. 71 RIVA and art. 164.Uno.6.º LIVA (about 22 prose sentences + 5 rows), the resumen anual 108.2–108.5 RIRPF (5 + 14 rows), art. 75.3 h)–k) with the final párr. and 75.4 (4 + 14 rows), art. 101.1 escala (table, 6 rows) and retribuciones variables, the 60 % reduction per apartado of art. 101 (7), art. 110 RIRPF (about 10 + 24 rows); (c) the other articles: arts. 117–121 RGAT (about 33), 120.3 párr. 3 and 122.2 párr. 2 LGT, arts. 99.2–99.11 and 100 LIRPF (about 40), 74, 76 (+ 1.º–4.º and 76.2 esquemas), 77–82, 88, 89 RIRPF, 90–107 RIRPF (about 20), 109.5, 111.2–3, 128 LIS, 60–68 RIS, 23 and 31 TRLIRNR (about 60 prose sentences + about 110 rows); (d) two «No confundir» blocks (autoliquidación complementaria vs rectificativa, art. 122.2 vs 120.3–4 LGT; plazo de retenciones 108.1 RIRPF vs pago fraccionado IS 40.1 LIS) — 4 sentences; (e) pool versions of the intro bullets (LIS now with the RIS), of the lead-in «Los demás porcentajes son» (the HEAD sentence said «sin la reducción del 60 por ciento prevista para Ceuta y Melilla»), of the 75.3 lead-in (no «entre otras», RDL 29/2026 marked only on h), i), k) and the final párr.), of art. 109.2–4 as a list, and the final «Normativa» lines the pool holds.
- Enumerations as esquemas (new): art. 71.3 RIVA 1.º–5.º; 100.2 LIRPF a)–c); 75.3 RIRPF a)–k) (HEAD's a)–g) list replaced by its esquema rows); 76.1 RIRPF 1.º–4.º; 76.2 a)–i) (nested 1.º–5.º under b), d), g)); 80.1 1.º–5.º; 82 1.ª–5.ª; 89.A) a)–d); 95.1 RIRPF 7 % cases a)–d) (with a «Regla» row for the fused lead-in); 108.2 a)–j); 110.1 a)–c); 110.3 a)–d) (nested 1.º–3.º and the four tramos of c)); 128.4 and 128.6 LIS; 60.1, 61 (a–z) and 62.1 RIS; 31.1 and 31.4 TRLIRNR. Items of art. 61 RIS with trailing ordinals ((1.º), (2.º) in i), q), t), y)) stay one row each: the ordinals close sub-conditions inside one sentence, not sub-items. Header row `| Elemento | Contenido | Cita |`. HEAD lists that were already whole stay lists (99.1, 75.1, 75.2, 76.1 a)–d), 111.1, 101.11); the pool's bullet lists without letters (71.1, 71.4, 71.7, 99.5, 99.8–99.11, the 60 % apartados, 40.3–40.5, DA 14.ª) stay bullets.
- build_check: `m03-l06: HEAD 134 · added byte-identical 226 · esquema rows from items 156 · not in pool 2`.
- cites.py: 448 citations, 0 unresolved. `index_sources.py --course aeat-agentes-hacienda`: see the final report. `split_paragraphs.py`: 7 paragraphs split.
- «Not in pool» (new «Normativa» lines, rebuilt from what the lesson cites): `RIRPF (RD 439/2007): arts. 74.1–3, … 78.1, 78.3, … 90, 93, 94, 95.1, …` (78.2, 91 and 92 no longer cited) and `RIVA (RD 1624/1992): arts. 30, 62.6, 71.1, 71.3–5 y 71.7.` (71.2 left out). The `Orden EHA/586/2011` line is HEAD's own (`art. 1.1`).

## Pool sentences left out (each states no rule, condition or exception, or lies outside the ranges)

- Intro bullets and body sentences on the orders EHA/3127/2009 (modelo 190), EHA/672/2007 (130/131), EHA/3786/2008 (303), EHA/3111/2009 (390), HFP/227/2017 (202/222), HAC/529/2026 (200), HAC/277/2026 (100), the art. 3 plazos of Orden EHA/586/2011 (a)–c) and domiciliación) and the «Modelos de declaración y plazo de presentación» table: outside the articles of the map's ranges (the map keeps only art. 1.1 of Orden EHA/586/2011 «at this depth»; modelos 100 and 200 are III.16 / III.17).
- Art. 71.2 RIVA (where the declaraciones-liquidaciones are presented): procedure.
- Art. 99.8.2.º second item (the Administración issues a documento acreditativo): procedure.
- Art. 100.3 párr. 2 (emisor deposits the amount at the judicial authority's disposal): procedure.
- Art. 78.2 RIRPF (remission to arts. 94 and 98): states no rule.
- Art. 90 RIRPF second sentence (arts. 91–94 «regulan el concepto…»): remission, states no rule.
- Art. 108.1 RIRPF sentence on direct payment when the pagador is the Administración del Estado: procedure.
- Art. 128.2 LIS sentence on the Ministro approving the modelos: procedure.

## Pool gaps (articles of the ranges with no rule sentence in the pool)

- Arts. 83–87 RIRPF (base, mínimo, cuota, tipo, regularización): only named by the five steps of art. 82.
- Arts. 91–94 RIRPF: only the remission sentence above.
- Art. 89.B) RIRPF (procedimiento especial por cambio de residencia): named in the art. 89 lead-in only.
- Art. 108.6 RIRPF; art. 62.2 RIS; arts. 62.4–62.8 and 63 RIS (one summary sentence, kept) and the rest of arts. 64–65 RIS (64.2 ff., 65.2 ff.).

## Sentences that do not stand on their own where they now sit

- «Para la aplicación de este tipo de retención, los contribuyentes deben comunicar al pagador…» and «Estos porcentajes se reducen en un 60 por ciento…» (art. 95.1): the first bullet after the 7 % esquema; «este tipo» and «estos porcentajes» point at the paragraph before the esquema.
- Rows of 75.3 e) and b) («Las entidades de crédito… están obligadas a retener respecto de los rendimientos obtenidos por los titulares de esas cuentas», «Queda sujeta a retención la parte del precio que equivalga al cupón corrido…»): depend on the row above; likewise «En el tercer supuesto, el arrendador debe acreditar…» (75.3 g)).
- 75.3 final paragraph («Para la aplicación de las exclusiones de retención relativas a los activos integrados en una Cuenta de Ahorro e Inversión Financia Europa a que se refieren las letras h), i) y k)…»): the letters are in the esquema above.
- «Estas deducciones no resultan de aplicación cuando…» (110.3 d)) and the second c) row («Cuando el importe de la minoración sea superior…»): depend on the rows above.
- «Los porcentajes del apartado 1 se reducen en un 60 por ciento…» (110.2) and «De la cantidad resultante se pueden deducir…» (110.3): «apartado 1» and «la cantidad resultante» point at the esquema of 110.1.
- «En estos supuestos, el pago fraccionado es a cuenta de la liquidación…», «Además, la cantidad a ingresar no puede ser inferior…», «Para los contribuyentes a los que se aplica el tipo de gravamen del párrafo primero del apartado 6…», «Del resultado positivo se excluyen…», «Este mínimo no se aplica…», «Los porcentajes de los apartados 2 y 3 podrán ser modificados…» (40.3, 40.4 and DA 14.ª.1): each depends on the bullet before it.
- «Solo se pueden presentar antes de que la Administración tributaria… haya acordado la devolución…» (120.2 RGAT) and the 121.2 sentence: «se pueden presentar» refers to the two definitions above.
- «Lo anterior no es de aplicación cuando correspondan los tipos fijos…» (81.3), «Se entiende por hijos y otros descendientes…» and «Los importes del cuadro se incrementan…» (81.2): refer to the 81.1 table.
- «Las mismas reglas de declaración mensual se aplican a los retenedores…» (108.1): «las mismas reglas» is the previous paragraph's second sentence.
- «Además, el artículo 99 LIRPF establece estas reglas:» and the 99.5 «Además (art. 99.5 LIRPF):» lead-ins: «además» depends on the paragraph before.
- «Lo dispuesto en los apartados 2 y 3 del artículo 100 LIRPF resulta aplicable…» (100.5) and «Estas obligaciones se entienden cumplidas…» (100.4): refer to apartados not repeated.
- «Reglamentariamente pueden modificarse los porcentajes de retención… previstos en el apartado 6» (128.6): after the esquema.
- The 128.1 and 62.1 bullets «Asimismo, están obligadas…» / «También están obligados…»: depend on the first bullet.
