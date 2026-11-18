# m01-l04 — R2d verify, re-check 3 (blind, Opus)

39 pending rows, each read as it now stands in the lesson (every pending id matches the current sentence). Sources:
`BOE-A-1978-31229_ce_2026-05-20.pdf`, `BOE-A-1995-6358_estatuto-ceuta_1995-03-14.pdf`,
`BOE-A-1995-6359_estatuto-melilla_1995-03-14.pdf`, `BOE-A-1985-5392_lbrl_2026-10-03.pdf`,
`CELEX-02016M-20250315_tue_2025-03-15.pdf` (TUE and Protocolo n.º 3), `CELEX-02016E-20250315_tfue_2025-03-15.pdf`,
`normativa.yaml`.

| id | verdict | precept checked | note | replacement |
|---|---|---|---|---|
| `c067238f19` | PASS | art. 151.2.4.º CE | second sentence of 4.º, verbatim in substance | — |
| `c9427da686` | PASS | art. 151.2.4.º CE | third sentence of 4.º; the three 4.º rows together give the whole número | — |
| `35ddffc19d` | PASS | art. 151.3 CE | «párrafos 4.º y 5.º del apartado anterior» and «ley orgánica prevista en el apartado 1» correctly resolved to art. 151.2 / 151.1 | — |
| `c74f2884e6` | PASS | art. 156.2 CE | verbatim; «de acuerdo con las leyes y los Estatutos» kept | — |
| `26cccf8a91` | PASS | art. 157.1.a) CE | verbatim; list a)–e) under the lead-in is complete and in the article's order | — |
| `ecc6887d76` | PASS | art. 157.1.c) CE | verbatim | — |
| `b2f447e215` | PASS | art. 157.1.d) CE | verbatim | — |
| `2dd8be8a4a` | PASS | art. 157.3 CE | «precedente apartado 1» resolved to art. 157.1; all three objects kept | — |
| `4e412c0962` | PASS | art. 21.2 LO 1/1995 y LO 2/1995 | both Estatutos identical; «en los términos que establezca la legislación general del Estado» kept on the potestad reglamentaria | — |
| `adc04ecb9c` | PASS | art. 22.2 LO 1/1995 y LO 2/1995 | both Estatutos identical; reglamentaria limited to «organización de los correspondientes servicios» kept | — |
| `76007d1fb0` | PASS | art. 4.2 LBRL | the CA-law and mancomunidades clauses follow in the next sentence under the same citation | — |
| `b4a6d9a0b2` | PASS | art. 4.3 LBRL | first sentence of 4.3, purpose clause kept | — |
| `897c76c687` | PASS | art. 4.3 LBRL | «siempre que sean precisas para el cumplimiento de su finalidad» and «en ambos casos» kept | — |
| `27982ce3e6` | PASS | art. 121.1 LBRL | closing paragraph of 121.1 verbatim | — |
| `a3ef6327c3` | PASS | art. 20.2 LBRL | «número anterior» rendered «apartado 1» with art. 20 in the citation | — |
| `8f238e65e8` | PASS | art. 21.3 LBRL | the «No obstante» exception to the non-delegable list, subject named; apartado 1 of art. 21 by the citation | — |
| `1e961096d2` | PASS | art. 23.2 LBRL | both letters a) and b) | — |
| `a7fdcb76c9` | PASS | art. 25.3 LBRL | four principles complete | — |
| `b4089636a4` | PASS | art. 26.2 LBRL (nota BOE) | matches the consolidated text's note: incisos declared unconstitutional and void, redacción of Ley 27/2013, STC 111/2016 de 9 de junio | — |
| `8d9624f541` | PASS | art. 26.2 LBRL | governed by the closing citation of the paragraph | — |
| `2f9436cc0b` | PASS | art. 26.2 LBRL | condition «financiados por tasas» and the assumption by the Diputación kept | — |
| `6d3b91dc99` | PASS | art. 28 LBRL | four kinds of medidas complete and in order; governed by the paragraph's art. 28 citation | — |
| `2c191ce50e` | PASS | art. 29.2 LBRL | «municipios del apartado b)» spelled out from art. 29.1.b); three requirements kept | — |
| `9fb99a6e0f` | FAIL | art. 29.3 LBRL | the article says «a lo establecido en esta Ley», i.e. the LBRL; «la ley» leaves the norm unnamed | Los municipios en Concejo Abierto ajustan su funcionamiento a los usos, costumbres y tradiciones locales y, en su defecto, a lo establecido en la LBRL y en las leyes de las Comunidades Autónomas sobre régimen local (art. 29.3 LBRL). |
| `eac6ff36a5` | PASS | art. 34.2 LBRL | the full list of non-delegable atribuciones, «a), i) y j)» right | — |
| `02b60f317a` | PASS | art. 36.2 LBRL | lead-in; rows a)–d) complete and in order | — |
| `fbe4f73e9e` | PASS | art. 15.2 TUE | composition complete; governed by the paragraph's art. 15.2 citation | — |
| `1a62c58a6c` | PASS | art. 16.2 TUE | «del Estado miembro al que represente» rendered «de su Estado» without loss | — |
| `aa30b6df32` | PASS | art. 16.6 TUE | — | — |
| `8c66afc81d` | PASS | art. 16.8 TUE | governed by the next sentence's art. 16.8 citation | — |
| `1639878dfe` | PASS | art. 14.2 TUE | governed by the next sentence's art. 14.2 citation | — |
| `0ebec2ecac` | PASS | art. 17.7 TUE | structure sentence; the three párrafos of 17.7 are the three steps | — |
| `7bc25802e4` | PASS | art. 19.2 TUE | first párrafo of 19.2 | — |
| `7ebdda2321` | FAIL | art. 50 ter Estatuto TJUE (Protocolo n.º 3) | the article lists the materias as a)–f) and attributes the «peticiones de decisión prejudicial planteadas sobre la base del artículo 267 TFUE»; the esquema numbers them 1–6 (relabel the Elemento cells a)–f)); the TJ's retained competence follows correctly at l. 1404 | El Tribunal General es competente para conocer de las peticiones de decisión prejudicial planteadas sobre la base del artículo 267 del TFUE que estén comprendidas exclusivamente en una o varias de las siguientes materias específicas (art. 50 ter Estatuto del Tribunal de Justicia de la Unión Europea, Protocolo n.º 3): |
| `27390301fc` | PASS | art. 263 TFUE, párrafo cuarto | both kinds of acts and «que no incluyan medidas de ejecución» kept | — |
| `ef872b6315` | PASS | Normativa — CE | both ways: every CE article cited in the lesson falls in 2, 81, 137–158, DA 1.ª and 3.ª, DT 4.ª and 5.ª; 18.1 named at l. 369 (art. 11.3 Estatutos), 105 at l. 733 (art. 18.1.e LBRL); arts. 27, 144.b and 149.1.29.ª named inside copied text fall within the listed range | — |
| `da2d484030` | PASS | Normativa — LOREG | art. 197 named at l. 420 (art. 19.2 Estatutos); the LOREG named without precept at l. 685 (art. 13.4 LBRL); LOREG is in `normativa.yaml` | — |
| `6d2288d18e` | PASS | Normativa — TRLRHL | arts. 123 and 124.1 named at l. 685 (art. 13.4 LBRL); «Ley Reguladora de las Haciendas Locales» at ll. 785, 831, 839, 1011, 1019, 1039 (arts. 21.1.f, 22.2.e and m, 33.2.c and k, 34.1.f LBRL) | — |
| `af69b4e754` | FAIL | Normativa — norms outside `normativa.yaml` | missing norms the prose names: Estatuto de Autonomía de Baleares (l. 1107, art. 40 LBRL; l. 1115, art. 41.3 LBRL), Ley de Presupuestos Generales del Estado (l. 685, art. 13.4 LBRL), Reglamento de la Asamblea of Ceuta and Melilla (ll. 360 and 369, arts. 9.1, 11.1 and 11.3 LO 1/1995 and LO 2/1995), Reglamentos de Procedimiento del Tribunal de Justicia and del Tribunal General (ll. 1361 and 1367, arts. 253 and 254 TFUE), régimen aplicable a los otros agentes (l. 1469, art. 270 TFUE); none is in `normativa.yaml` | Ley 12/1989 (Función Estadística Pública), Ley Orgánica 2/2012, Ley 39/1988 (art. 158.5), Ley 51/2002 (disposición adicional décima), Ley 22/2005 (disposición adicional segunda), Ley de Presupuestos Generales del Estado, Ley 27/2013, Sentencia del Tribunal Constitucional 111/2016, Estatuto de Autonomía del País Vasco y Estatuto de Autonomía de Baleares: nombrados en los arts. 13.4, 16.3, 24 bis.3, 21.1.f), 26.2, 34.1.f), 39, 40 y 41.3 LBRL; Reglamento de la Asamblea de Ceuta y Reglamento de la Asamblea de Melilla: nombrados en los arts. 9.1, 11.1 y 11.3 LO 1/1995 y LO 2/1995; Decisión 2009/908/UE y Decisión (UE) 2016/1316, Decisión de 8 de abril de 1965, Protocolo sobre las disposiciones transitorias (art. 238.2 TFUE), Reglamento de Procedimiento del Tribunal de Justicia y Reglamento de Procedimiento del Tribunal General (arts. 253 y 254 TFUE), Estatuto de los funcionarios de la Unión y régimen aplicable a los otros agentes (art. 270 TFUE) y Estatutos del Banco Europeo de Inversiones y del SEBC y del BCE (art. 271 TFUE); no figuran en `normativa.yaml`. |

PASS 36 · FAIL 3
