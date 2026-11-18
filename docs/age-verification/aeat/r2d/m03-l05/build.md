# Build — III.5 (`m03-l05`), R2d, 2026-11-17

Script: `…/scratchpad/b05/build.py` (pool walk: every sentence is a HEAD sentence or a pool sentence, byte-identical;
the only new text is three «Normativa» lines).

## Size

| | words |
|---|---|
| HEAD, excluding esquema rows | 8,994 (wc -w 9,583 with the HEAD rows, 589) |
| Built, excluding esquema rows | 20,970 (wc -w 24,497 with rows) |
| Esquema rows, built | 3,527 (HEAD: 589) |

Ratio to HEAD (excl. rows): 2.33. Ratio to the 1.6 target (14,390): 1.46. Above target: R2b removals (consultas
arts. 88–89 LGT with RGAT 65–68; prueba arts. 106–108 LGT) and about 60 articles HEAD did not treat (RGAT 30, 55–58,
87–101, 114–115 bis; LGT 93–94; Orden HAC/1398/2003) now give their rule, conditions and exceptions, and 18 legal
enumerations became esquemas.

## Sentences added (not in HEAD): 345 prose + 99 esquema rows (96 from pool items, 3 nested sub-items of the Orden)

- (a) R2b removals: 44 prose + 21 rows. Consultas arts. 88.1–88.8 and 89.1–89.4 LGT (88.3 entities as an esquema),
  RGAT 65, 66.1–66.2 (esquemas), 66.5–66.7, 67, 68; prueba arts. 106.1–106.4, 107.1–107.2, 108.1–108.5 LGT (14 units).
- (b) Review items confirmed (certificados and plazos): 41 prose + 16 rows. RGAT 71.1–71.3, 72.1 (esquema) and 72.1.b
  paragraphs, 73.1–73.4, 74.1 a)–i) (esquema) and 74.2–74.4, 75.1 second paragraph, 75.3; RGAT 102.2–102.7, 103.d)–e)
  last sentences, 104 h), i), a) last sentence, f) computation; LGT 104.3 actos presuntos.
- (c) Articles HEAD did not treat or treated in part: 211 prose + 59 rows (LGT 86.3–86.4, 87.3, 92.2, 93, 94, 95.3,
  95.5, 95.6, 95 bis.1–7 additions, 98.3, 99.5, 99.7, 99.8, 102.3; RGAT 30, 55–58, 63–64, 69, 77–81, 87–101, 114–115 bis;
  Orden HAC/1398/2003; RD 1363/2010 disp. adic. 3.ª.1–2).
- (d) «No confundir»: 3 blocks, 13 sentences (information/acuerdo/consulta effects of silence; plazos para contestar;
  vigencias), as in the pool.
- (e) HEAD sentences replaced by their pool form (not counted above): 86.4 LGT; the three certificate sentences
  (71.1, 72.1, 72.1.b; the first two now esquemas); 92.2 LGT clause; 95 bis.4 (fecha de referencia, alegaciones,
  publicación); 98.3 LGT; 99.7 comunicaciones; the 104 RGAT lead-in (now «entre otras»). Normativa: HEAD's LGT and RGAT
  lines, LOFCA, Concierto, CE and Ley 25/2003 lines replaced by the pool's «nombrado en …» form.
- Normativa: 17 pool lines copied; three lines rebuilt from what the built lesson cites (see «not in pool»).

## Enumerations as esquemas (18 + 1 nested)

art. 88.3 LGT (nine items); 66.1, 66.2, 69.2, 71.1, 72.1, 74.1, 55.1, 87.3, 88.2, 97.1, 98.1, 98.2, 98.3, 100.2 RGAT;
art. 93.1, 93.4 and 94.1 LGT; apartado segundo.2 Orden HAC/1398/2003 (nested a)–c), also kept whole in its bullet:
the row cells are verbatim sub-items). An item with a second sentence gives two rows with the same label. HEAD's
flat lists (85.2, 92.3, 79.1, 95.1, 95 bis.1, 99 LGT, 101.3–101.4, 102.2, 103 and 104 RGAT, 91.3 RGAT) stay HEAD bullets.
Bullet runs added without a lead-in sentence (63.x, 89, 93.3, 30.3, 57, 92–96 RGAT, 102 RGAT, 106–108 LGT) are
paragraphs of the same sentences, not lists.

## Pool sentences left out of added articles (each states no rule, condition or exception)

66.3 (domicilio, anexos), 66.4 (documentos normalizados), 69.3 (estimación de valoración), 69.4 (requerimiento de
documentos), 88.4 (domicilio), 88.5 (modelos), 88.6 (copia sellada), 88.7 recibí sentences, 93.2 RGAT (how the request is
made; contents of the answer), 94.4 RGAT (electronic access), 95.2 and 95.4 RGAT (delivery in diligencia; electronic
copies), 96.5 RGAT (elevation of the propuesta), 99.1 RGAT first two sentences (model-free format), 56 RGAT second
paragraph and State competent organs, 57.1 State authorisation organ, 57.2 data contents and mode, 58.2 record in the
expediente, RD 1363/2010 disp. adic. 3.ª.3. 28 sentences; the «Normativa» lines follow (units 66.3–66.4, 69.3–69.4, 88.4–88.6,
93.2, 94.4, 95.2, 95.4, 96.5 and RD art. 3.2.b removed).

## Kept deliberately

- HEAD's esquema «Plazo máximo de resolución y cómputo» (rows of art. 104.1 only; review item 4 «tables repeat the
  preceding text») stays: the pool dropped it, the build does not cut. For the coordinator: remove it or gather 104.1 with
  104.2 and 102.5/103/104 RGAT.
- Not done (outside this build): glossary links (g-silencio-administrativo, g-convenio, g-vecino, g-servicios-comunes:
  step 4 of the coordinator), course.yaml summary.

## Checks

- build_check: `m03-l05: HEAD 281 · added byte-identical 345 · esquema rows from items 99 · not in pool 3`.
- cites.py: 515 citations, 0 unresolved.
- split_paragraphs: 0 paragraphs split (no paragraph over 120 words).
- index_sources (`--course aeat-agentes-hacienda`): exit 0, validation passed (no error names m03-l05).

## «not in pool»

- l.910: «Normativa» RGAT line (rebuilt from the cites of the built lesson: pool line minus 66.3–66.4, 69.3–69.4, 88.4–88.6, 93.2, 94.4, 95.2, 95.4, 96.5).
- l.913: «Normativa» RD 1363/2010 line (disposición adicional tercera.1–2 only).
- l.925: «Normativa» Ley Orgánica 15/1999 line (art. 94.4 RGAT no longer cites it).

## Sentences that do not stand alone where they now sit

Dangling reference
- l.133 «Las solicitudes podrán presentarse … la identificación de las personas o entidades a que se refiere el apartado
  2.a) quede garantizada (art. 69.5 RGAT)»: points to the esquema row 69.2 a) above it, not to a sentence.
- l.106 «Si la solicitud no reúne los requisitos establecidos en los apartados 1 y 2 …» (66.6 RGAT) and l.90 «los datos
  incluidos en el apartado 1»: the apartados are the esquemas 66.1 and 66.2 (66.3–66.4 are not in the lesson).
- l.61 and l.63 (88.4, 88.6 LGT) «los requisitos establecidos en virtud del apartado 2»: 88.2 sits in l.43, two
  blocks above the 88.3 esquema.
- l.260 «a quienes no tuvieran acceso a los previstos en el artículo» (78.3 RGAT; the norm's own words, no number) and
  «El uso de estos medios» (78.3): the medios are those of the paragraph before.
- l.300–309 (Orden HAC/1398/2003): «el número 1 del apartado primero», «los números 1 y 2 del apartado segundo»,
  «el número 4 del apartado segundo» refer to the numbered paragraphs of the Orden, which the bullets do not number
  (only their citation shows it).
- l.481 «Lo dispuesto en el artículo no afecta …» (95 bis.6 LGT): «el artículo» is art. 95 bis, not named.
- l.772 and l.774: «en los términos establecidos en el «artículo 104.i)» RGAT» (RD 1363/2010) and «El texto consolidado
  del RGAT recoge este supuesto en la letra h) …»: «este supuesto» is the RD's designación de 30 días, two sentences
  above, in a different paragraph from the list h)/i).
- l.376 «en «este capítulo» del reglamento» (30.1 RGAT) and l.378 «en este capítulo»: chapter not named.
- l.676 «de la forma prevista en este apartado» (101.6 RGAT): the apartado is the two paragraphs before.
- l.497 «lo previsto en el artículo 97.1 RGAT» (87.3): 97.1 is only at l.588, further down.

Elided subject
- l.368 «Asimismo, participarán en la gestión o exacción de los tributos …» (94.1 LGT): the subject is the list of
  authorities in the esquema above it («Están obligados …» is in l.355).
- l.475 «La orden ministerial fija la fecha de publicación …» (95 bis.4): which orden is not said.
- l.290 «El incumplimiento … con el procedimiento y garantías previstos en el párrafo anterior» (79.3 RGAT): the
  «párrafo anterior» is the last sentence of l.288, then the pool puts the new paragraph.
- l.37 and l.39 (63.2–63.4 RGAT paragraphs converted from bullets): each starts a new subject («la información de carácter
  general», «las actuaciones de información tributaria») without the earlier sentence of art. 63 that frames it.

Item without lead-in
- HEAD lists that now carry added items and have no lead-in ending in «:»: 91 LGT (l.139–143), 95 bis.4 (l.468–473,
  after the 95 bis.3 paragraph), 99 LGT (l.542–550, after «… (art. 99.1 LGT).»).
- l.527–530 «El resto del artículo 88 RGAT dispone:» now holds only 88.3 and 88.7 (88.4–88.6 left out): the lead-in
  still reads as if the list were the whole rest of the article.
- l.103–110 «Sobre el resto de la tramitación el reglamento dispone:» likewise omits 66.3–66.4.
