# Build — III.4 (`m03-l04`), R2d, 2026-11-17

Base HEAD plus whole pool sentences, byte-identical (`tools/build_check.py`). Assembled in scratch by script (pool order; picks by sentence index), written to the lesson once every esquema was complete.

## Size
- Words (`wc -w`, esquema rows excluded): HEAD 11,827 → built 37,345. Ratio 3.16 × HEAD; 1.97 × the 1.6 target (target 18,923). Over target on purpose: every article of the range keeps its rule/conditions/exceptions sentences and every enumeration is an esquema.
- Esquema-row words (table lines, headers included): HEAD 914 → built 16,691 (58 esquemas: 2 HEAD prescripción esquemas kept, 56 new; the 2 HEAD baja/domicilio esquemas that repeat a paragraph are removed, review item 7).

## Sentences added by category (build_check: 614 byte-identical + 371 esquema rows from items; HEAD base 379)
- (a) R2b removals: none (map: none inside this tema).
- (b) Review item 1, declaraciones informativas (RGAT 30–54 ter): 112 sentences + 102 rows (arts. 31–35 in full; 37–54 ter first apartado of each with its lists as esquemas; art. 36 «Suprimido»). Review item 2, censos (DA 5.ª LGT, RGAT 2–16): 65 sentences + 79 rows. (Orden modelos 036/037: left out, see below.)
- (c) Article sentences: 343 sentences + 182 rows (art. 29 bis, 66 bis.2–3, 40.2, 41.4, 46.4–5, 110.2, 111.3–4, 112.2–7, 17.4, 59.1–5, 148–152 RGAT, 31–33 LGT, NIF arts. 19.3–28 RGAT, libros RGAT 29.3–4, RIVA, RIRPF 68.6–9, Código de Comercio, LIVA 164–166, LIRPF 104, LIS 120, Reglamento de facturación 5–24, RD 1007/2023 arts. 1–4, RD 1676/2009 arts. 1–17, RGRVA 72–79 by the coordinator note on 2020-71).
- (d) «No confundir»: 3 blocks (responsables solidarios/subsidiarios; 46.7 LGT / 112.1 RGAT; 67.2 LGT), 7 new sentences plus the HEAD sentences they repeat as the pool writes them.
- (e) Pool versions replacing HEAD: the opening paragraphs (RGAT, RD 1007/2023, RIVA/LIVA/RIRPF/LIRPF/LIS, RD 1676/2009, RGRVA: 5 sentences); the HEAD «entre otros» sentence of art. 71.3 RIVA replaced by the whole list as an esquema (2 sentences + 8 rows). HEAD esquema rows l. 43–49 and 296–301 removed.

## Enumerations as esquemas (56 new)
DA 5.ª.3 LGT; RGAT 3.3, 9.3, 10.2, 10.4, 22.1, 22.4, 32, 33.2, 33.3, 34.1, 34.2, 38.1, 38 bis, 38 ter, 39.1, 42.1, 42 ter (two), 44.1, 46.1, 49.1, 51.1, 53, 54, 59.2, 111.3, 111.4, 112.2; RD 1619/2012 5.2, 6.1 (with nested 1.º–5.º and 1.º–3.º), 6.2, 6.5, 7.1, 7.2, 7.4, 10.1, 14.2, 19.1; RD 1007/2023 1.2, 3.1, 4; RD 1676/2009 3.1, 4.1, 6.3, 9.1, 15.1, 15.2; RGRVA 73, 74.1, 76.2; RIVA 62.5, 66.1, 71.3; LIVA 164, 166.Uno. Rows: text cell byte-identical to the pool item, citation cell = the lead-in's citation (cited in prose). Arts. 37–54 ter (other than their lists) stay prose, one sentence per article, not an esquema (the pool sentences are long).

## build_check line
`m03-l04: HEAD 379 · added byte-identical 614 · esquema rows from items 371 · not in pool 6`

## «not in pool» (6)
Rebuilt «Normativa» lines (new text): RD 1619/2012 (Reglamento; 17–24 plus «art. 16.1 nombrado en el art. 3.3»), Código de Comercio (29.1 only; 29.2 left out), RGRVA (72–76 y 78–79), TRLIRNR (Orden clause removed), Ley 30/1992 (art. 36.1 clause removed), final «no figuran en `normativa.yaml`» line (five norms the lesson no longer names removed: RD 296/2004, Ley 3/2015, Ley 11/2007, LO 15/1999, Reglamento de censos; locations of Orden and 10.6.b) removed). Orden EHA/1274/2007 and RD 1619/2012 (real decreto) lines dropped.

## Pool gaps (article of the range with no pool sentence; no prose written)
- Arts. 4–8 RGAT (contenido de los censos): none in the pool.
- Reglamento de facturación: art. 1; art. 2.2 a)–f), 2.3 a)–b), 2.4; art. 3.2 a)–b); art. 16 (pool has only the «regula» heading sentence; the lesson names it in art. 3.3 and 19.1).
- RIVA arts. 62 bis, 67, 68, 68 bis (and 61.3); LIVA art. 164.Uno.8.º; Código de Comercio art. 30.2.
- Orden EHA/1274/2007 (modelo 036): pool has it, but it is not among the map's article rows and every RGAT 9–13 sentence is already in; left out (decision for the coordinator).

## Pool sentences left out and why (283)
- Every «El artículo N … regula: …» / «dispone lo siguiente» heading sentence and the apartado markers («Uno.», «Dos.», «Declaración de alta.», …): they state no rule.
- Orden EHA/1274/2007 (pool sentences on arts. 1, 2, 3, 11, 14) and RD 1619/2012 real decreto arts. 1–3: outside the map's rows.
- Development, procedure or repetition (no rule, condition or exception): 3.7 second paragraph lead; 12.3 (copia de escrituras); 16.2; 21–28 solicitud mechanics (23.3 forma de la solicitud, 23.4 trámite); RGAT 29.3 simplified diario; 70 bis rectification of bienes de inversión; Código de Comercio 29.2 («pesetas», superseded text); RGAT 30.3–30.4 requerimiento mechanics; 38.1 contenido y vía electrónica; 38 bis/ter, 39, 42 ter later paragraphs (datos de detalle); 46 later paragraphs; RD 1619/2012 8.5–8.6 (controles de gestión), 7.5 publicidad, 22.3 (comunicación fuera de España); RD 1676/2009 4.6–4.8 (suplencia, asesores), 5.3–5.4, 6.2, 6.4, 8.3–8.6, 9.3–9.5, 10.1, 10.4–10.8 (except those kept), 12.2–12.6, 13, 14, 15.3, 16.2–16.3; RGRVA 75.2, 77.1–77.4, 78.2–78.3; RGAT 149.2–3, 149.5, 152.2 notification mechanics; LGT 48.3 first sentence (duplicates of the HEAD paraphrase).
- The full list by sentence was generated in scratch and lost when the scratchpad was cleared; it can be regenerated: pool sentences not in the lesson and not heading sentences.

## Sentences that do not stand on their own where they now sit
- «En este último figurarán la totalidad de personas físicas o jurídicas y entidades a q…» (l.60)
- «Este registro formará parte del Censo de Empresarios, Profesionales y Retenedores (ar…» (l.125)
- «Este registro formará parte del Censo de Empresarios, Profesionales y Retenedores (ar…» (l.129)
- «Esta declaración deberá presentarse, según los casos, con anterioridad al inicio de l…» (l.186)
- «Esta declaración, en particular, servirá para (art. 10.2 RGAT):…» (l.192)
- «Esta declaración no será necesaria cuando la modificación de uno de los datos que fig…» (l.227)
- «De igual forma, en relación con los sujetos pasivos que resulten exentos del Impuesto…» (l.266)
- «A tal efecto, podrá realizar las altas, bajas y modificaciones correspondientes de ac…» (l.272)
- «El anterior número de identificación fiscal surtirá efectos hasta la fecha de comunic…» (l.303)
- «Dicho número se asignará cuando se solicite por el interesado la inclusión en el Regi…» (l.354)
- «Dichas autorizaciones serán revocables en cualquier momento (art. 62.5 RIVA).…» (l.419)
- «La misma obligación incumbirá a quienes, sin tener la condición de empresarios o prof…» (l.423)
- «Esta numeración podrá realizarse mediante series separadas siempre que existan razone…» (l.425)
- «Esta rectificación deberá efectuarse mediante una anotación o grupo de anotaciones qu…» (l.449)
- «Lo anterior resultará de aplicación para las personas y entidades a que se refiere el…» (l.451)
- «Lo previsto en los apartados anteriores será igualmente aplicable a quienes, sin ser …» (l.520)
- «Esta obligación se podrá cumplir por un tercero, que actuará en nombre y por cuenta d…» (l.524)
- «En estos casos, la información requerida deberá aportarse por los obligados tributari…» (l.579)
- «A estos efectos, se considerarán actividades empresariales o profesionales todas las …» (l.587)
- «A estos efectos, se atenderá al importe de las primas o contraprestaciones percibidas…» (l.624)
- «Como excepción a lo dispuesto en el segundo párrafo de este apartado, los sujetos pas…» (l.628)
- «A estos efectos, las operaciones se entenderán producidas en el período en el que, de…» (l.721)
- «A estos efectos, el importe total de las operaciones realizadas con la misma persona …» (l.725)
- «Estarán obligados a suministrar información a la Administración tributaria mediante l…» (l.801)
- «Dicha obligación también se extiende a quienes hayan sido titulares, representantes, …» (l.814)
- «A estos efectos, se entenderá por titular real quien tenga dicha consideración de acu…» (l.816)
- «Dicha obligación también se extiende a quienes hayan sido titulares, autorizados, o b…» (l.846)
- «A estos efectos, se entenderá por titular real quien tenga dicha consideración de acu…» (l.848)
- «Lo dispuesto en este artículo resultará de aplicación a los siguientes rendimientos (…» (l.852)
- «Hasta entonces rige la redacción anterior de esos preceptos.…» (l.1129)
- «Estas facturas deberán ser expedidas como máximo el último día del mes natural en el …» (l.1183)
- «Esta obligación incumbe asimismo a los empresarios o profesionales acogidos a los reg…» (l.1233)
- «A estos efectos, se entenderá por conservación por medios electrónicos la conservació…» (l.1243)
- «A estos efectos, el interés de demora se devengará desde la finalización de dicho pla…» (l.1325)
- «Lo dispuesto en el presente artículo no será de aplicación respecto de las garantías …» (l.1337)
- «Transcurrido el plazo a que se refiere el apartado anterior sin que los servicios res…» (l.1554)
- «Este plazo se contará desde la fecha en que la queja haya tenido entrada en el regist…» (l.1562)
- «A estos efectos se remitirán a dicho órgano los antecedentes que sean necesarios.…» (l.1855)
- «Lo anterior no impedirá que la Administración tributaria pueda iniciar en cualquier o…» (l.1857)
- «Lo dispuesto en el apartado 2.b) anterior no será de aplicación en las actuaciones y …» (l.1859)
- «Esta competencia se mantendrá aun cuando las actuaciones hayan de proseguirse frente …» (l.1859)
- «En este último caso, el cambio de domicilio tendrá efectos a partir del día siguiente…» (l.1887)

All are whole pool sentences whose subject («esa», «dicha», «en este caso», «lo dispuesto…») points to the sentence before it in the pool; where the pool neighbour was dropped, the reader meets the pronoun without its referent (examples: art. 3.7 RGAT «Lo dispuesto en el párrafo anterior…» second paragraph kept without the paragraph before; RD 1676/2009 10.3/10.7; RGAT 33.3 and 59.3).

## Checks
`build_check` (above); `cites.py m03-l04`: 1,061 citations, 0 unresolved; `split_paragraphs.py`: 0 paragraphs split; `index_sources.py --course aeat-agentes-hacienda`: see the final message.
