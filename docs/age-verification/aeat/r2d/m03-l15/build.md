# Build — III.15 (`m03-l15`), R2d, 2026-11-17

Words (`wc -w`): HEAD 8,514 (esquema rows 578; 7,936 without) → built 30,687 (esquema rows 12,955; 17,732 without, of which
plain tables 434). Ratio excluding esquema rows: 2.23 to HEAD without rows; 1.40 of the 1.6 target (12,698). Above the
target: the range holds ~100 articles (HEAD treated about a third in full); every article states its rule, conditions and
exceptions, every legal enumeration (nested ones too) is an esquema, and nothing is left out for size. Most of the added
words are esquema rows (items that were bullets or in-sentence lists now sit in rows, and the pool's complete lists:
art. 7 (27 letters), 14.2 (13), 17.2, 37.1 (14), 3.1.d) of the Orden, the 23.2 tramos).

Method: the pool (`expansion/m03-l15.md`) is HEAD's lesson with every verified addition and correction in the norm's
order; the build is the pool whole (every pool sentence states a rule, a condition or an exception of its article, so
none was left out), with legal lists turned into esquemas and two headings added to place material (the dietas section
now follows art. 17.3; «Exención por transmisión de vivienda a entes públicos» before DA 65.ª). «Lo que más cae» is HEAD's
ten lines (the pool's are identical). A script (`scratchpad/b15/build.py`) wrote the file from the pool lines so bytes stay
identical.

## Sentences added (not in HEAD): 218 prose + 265 esquema rows (253 from items, 12 for the new tramo/rule rows split by sub-item)

- (a) R2b removals: none (the map lists none for this tema).
- (b) Review items: dietas (art. 9 RIRPF, 11 prose + 7 table rows), elementos afectos (art. 29 LIRPF, arts. 22–23 RIRPF, 12 prose + 12 rows), art. 38 LIRPF with arts. 41, 41 bis, 42 RIRPF (7 prose; DA 65.ª goes under (c)), reducciones por alquiler with DT 38.ª and the three wordings (19 prose + 22 rows incl. the all-tramos esquema), 15 + 18 more rows counted under (c) for the lists they complete.
- (c) Every other article not or partly treated at HEAD (157 prose + 224 rows): arts. 7 (all letters), 9.2, 14.2–14.3, 17.1.e–f, 17.2, 18.2–18.4, 24 (both wordings), 25.1–25.6, 26.2, 28.3–28.4, 30.2, 31.1.2.ª–4.ª, 31.2, 32.2, 33.2–33.5, 34.2, 35–37, 40, 41 LIRPF; DA 65.ª; DT 3.ª, 32.ª; arts. 1, 2.2, 4, 6.2, 10, 11.2, 12, 13–15, 17–21, 22–29, 30–39, 40–42, 43–48 bis RIRPF; Orden HAC/1425/2025 art. 3.1.c–d and Orden HAC/1161/2026 DA 4.ª.1.ª.
- (d) Estimación objetiva paragraph (three bullets: DT 32.ª for 2016–2024 only, RDL 9/2024, 16/2025 and 2/2026 derogated, limits in force on 14-11-2026: 150.000 / 75.000 / 250.000 / 150.000 €) and the three «No confundir» blocks (EDS/EO exclusion; the 30 % of arts. 18.2 and 32.1; art. 33.5 e) and f)–g)): 3 + 9 sentences. The 250.000 / 125.000 figures appear only as the pool states them (DT 32.ª, derogated extensions).
- (e) HEAD sentences replaced by their pool form: 46 (the «entre otros» lead-ins of arts. 7, 17.1, 17.2, 23.1.a), 25.4, 30.2, 31.1.3.ª, 33.2–33.5, 42.3; art. 7.f), 7.j), 7.ñ) and its last paragraph; art. 14.2.a) and d); art. 18.1–2; art. 23.2 «convalidación pendiente» wording; art. 24; 85.1 «convalidación pendiente»; DA 55.ª; the «Cambio pendiente … sin convalidar» Normativa lines; art. 25 bullets «1.»–«4.» (now «Apartado 1:» …)).
- Normativa: the LIRPF, RIRPF, Orden and RDL lines are the pool's (rebuilt from what the built lesson cites); new lines versus HEAD: RIRPF, Orden HFP/792/2023, versiones del art. 23 LIRPF, RDL 9/2024, 16/2025, 2/2026, RDL 29/2026 (convalidado) and the final «no figuran en `normativa.yaml`» line.

## Enumerations as esquemas (253 rows from items)

art. 7 LIRPF a)–z); 14.2 a)–m) (h) A)–B), k) 1.º–3.º as sub-rows); 17.1 a)–f); 17.2 a)–k) (a) 1.ª–7.ª); 42.3 a)–f); 43.1.1.º a)–g)
(d) 1.º–4.º); 12.1 RIRPF a)–g); 13 RIRPF a)–h); 15 RIRPF a)–c); 21 RIRPF a)–c); 23.2 LIRPF 31-12-2025 a)–d) and the tramos of
the wording in force (a).1.º ×5, a).2.º, a).3.º ×5, b) ×5, c), d); 25.1 a)–e); 25.3 a).2.º (six age percentages), a).3.º (four
durations), a).4.º–6.º, b); 29.1 a)–c); 22.2 RIRPF 1.º–2.º; 22.4 RIRPF a)–e); 30.2 1.ª–4.ª and 5.ª a)–c); 31.1.3.ª a)–d);
Orden 3.1.d) (six employee thresholds and vehicles); 32.2.1.º a)–b) (tramos); 32.2.2.º a)–g); 25 RIRPF a)–d); 33.2, 33.3, 33.4,
33.5 a)–g); 37.1 a)–n). Lists HEAD already had whole stay as bullets (6.2, 8.1, 9.1, 10.1, 14.1, 16.2, 19.2, 20, 23.1.a), 26.1,
42.2, 2.1 RIRPF, 25.4 inline). Where the enumeration sits inside a single pool sentence (25.1, 25.3, 22.2, 22.4, 15 and 21
RIRPF, the 23.2 tramos), that sentence stays in the prose (nested layout where it was a list) and the esquema repeats its
items as verbatim sub-items: a lead-in alone would not be a verified sentence. The dietas, estimación objetiva and 85.1
tables stay plain tables as in the pool (their Cita cells name units the prose does not cite, so an esquema would break the
cross-reference rule). In esquema rows a trailing own citation of an item (e.g. «(art. 30.2.1.ª LIRPF)») is not repeated in
the cell; the Cita column carries the lead-in's unit.

## Checks

- build_check: `m03-l15: HEAD 211 · added byte-identical 224 · esquema rows from items 253 · not in pool 6`.
- cites.py: 608 citations, 0 unresolved.
- split_paragraphs: 0 paragraphs split.
- index_sources (`--course aeat-agentes-hacienda`): exit 0, no validation error naming `m03-l15`.

## Pool sentences left out

None: every pool sentence is in the built lesson (as prose or as an esquema row/sub-row; a few rows cut a sentence at its
own sub-items). No pool sentence states only development or procedure beyond what is a condition of the article.
Gaps against the map (no pool sentence, so none added; no prose of my own): arts. 3, 5, 6.1 and 7 RIRPF (premios literarios,
misiones internacionales, trabajos en el extranjero, imputación de atrasos; the LIRPF letters 7.l), 7.o), 7.p) and 14.2.b)
carry the rule) and arts. 1–2 of the Orden HAC/1425/2025 (actividades incluidas).

## Not in pool (6, all pending sentences of the pool awaiting a verifier; the pool's `pending.md` lists them)

They are the pool's corrected forms after the recheck-2 FAILs (`m03-l15/verify-recheck-2.md`), not new text:
- l.79: 7.ñ) last paragraph (new text with the DA 26.ª clause).
- l.486: art. 23.2 «Los requisitos deben cumplirse …» (80 % prórroga, FAIL fixed).
- l.493 (art. 24 from 01-01-2027, «Desde el 01-01-2027, el rendimiento neto total …»; FAIL fixed).
- l.501: art. 25.1 «Quedan incluidos dentro de esta categoría …» (letter e) condition restored).
- l.826: art. 85.1 from 01-01-2027 «El valor catastral de cada inmueble …» (FAIL fixed).
- the pool's LIRPF «Normativa» RDL line (`Redacción del Real Decreto-ley 29/2026 … en vigor desde el 08-10-2026`).

## Sentences that do not stand on their own where they now sit (built-lesson line numbers)

Mostly references to a list that is now an esquema directly above, or to the previous sentence:
- Art. 7 block: l. 73 («la letra e)»), 77 («La letra f)»), 78 («la letra n)»), 79 («la letra ñ)»), 83 («esos principios», «estos requisitos»).
- Residencia: l. 107–109 (the 9.1 presumption and 9.1.a) notes follow the esquema-less list but refer to «esos criterios» and «las estancias»), 121 («esta regla», «Tampoco»).
- l. 155 and l. 190 (14.1.b)/14.3: «esa imputación», «esas rentas»).
- Art. 17: l. 209 inside the 17.1.f) rows («Esta imputación fiscal …»), l. 213 («con esos límites», «por tanto»), l. 240 (17.3: «las letras c) y d)» now point to esquema rows).
- Dietas: l. 255 («Las asignaciones para manutención y estancia …»), l. 258 («El régimen es aplicable también …»), l. 259 («Las cuantías son revisables») refer to the table above.
- Especie: l. 304 («de la letra b)»), l. 308 («esas reglas»).
- Rendimiento neto: l. 330 («La cuantía de la letra f)»), 336 («Los gastos de la letra f)»), 337 («El límite de la letra d)»), 339–340 (art. 11.1 RIRPF and the discapacidad example refer to the 2.000 € increase), 345–350 (art. 18.2 sub-rules: «la regla siguiente», «ese límite», «tales rendimientos», «los indicados»), 368 («esos rendimientos»), 378 («a estos efectos»).
- Capital inmobiliario: l. 414 («este», the soil value of the amortización), 437 and 439–441 («Redacción vigente a …» are labels), 452, 484–488 (art. 23.2 rules «las reducciones que dependen de la edad», «los requisitos», «la de mayor cuantía», «Las reducciones solo se aplican …»), 493–494 (art. 24 2027: «el porcentaje medio efectivo»).
- Capital mobiliario RIRPF: l. 555, 556.
- Actividades: l. 645 («ese conjunto», after the 30.2 esquema), 656 («esas entidades»), 682 («las magnitudes del apartado b)»), 684–685 («esa reducción de 2026»), 690–691 («esos límites», «por tanto»), 701 and 716 (3.1.d: «esas magnitudes», «esas magnitudes»), 719 and 722 (art. 33–34 RIRPF: «La renuncia», «También son causas»), 757 («La reducción del número 1.º»), 772–778 (32.2.3.º/4.º and 32.3 bullets: «Esta reducción», «el saldo resultante», «Se inicia una actividad», «El rendimiento neto sobre el que», «No se aplica»).
- Imputación de rentas inmobiliarias: l. 815–816 (85.1 bullets: «el inmueble», «no se estima renta»), 826 («El valor catastral de cada inmueble …» after the scale table), 830 («Estas rentas»).
- Ganancias: l. 861 («Esos supuestos»), 904 («las letras f) y g)»), 906 («ese año»), 946 («las letras a), b) y c)», «las letras d), e) y h)»).
