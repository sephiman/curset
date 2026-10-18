# R2c esquemas, bloque I and the bloque V items — recheck (second, blind reviewer), 2026-10-18

Reviewer did not read `verify-*.md`, `fixes.md` or any scratchpad notes. Judged from `spec.md` (rule), the
`::esquema` section of `docs/platform-delta-handoff.md`, `docs/prose-voice.md`, the lesson and the norm texts in the
session scratchpad `txt/` (pdftotext; `art.py`). Each esquema checked whole: every row/node, title, header, order or
dependency, placement. Citation parsing checked read-only with `tradeschool.citations.grammar.parse_segment` and
against `C/citations.es.txt`. No lesson or content file was edited.

Placement: every esquema below follows the paragraphs it summarises and none replaces them.

## 1. m05-l06 — tabla «Del gasto al pago de la subvención»

| # | row (short) | citation | PASS/FAIL | passage / reason | replacement |
|---|---|---|---|---|---|
| 0 | title | — | PASS | Covers art. 34.1–5 LGS («Procedimiento de aprobación del gasto y pago»); not selective. | — |
| 1 | Aprobación del gasto | art. 34.1 LGS | PASS | «Con carácter previo a la convocatoria … o a la concesión directa … deberá efectuarse la aprobación del gasto en los términos previstos en la Ley General Presupuestaria» (the «restantes Administraciones» clause is left out, as in the prose; AGE lesson). | — |
| 2 | Compromiso del gasto | art. 34.2 LGS | PASS | «La resolución de concesión … conllevará el compromiso del gasto correspondiente». | — |
| 3 | Pago | art. 34.3 LGS | PASS | First paragraph of 34.3 verbatim; the «pérdida del derecho al cobro» paragraph is a consequence, not a condition, and the prose also leaves it out. | — |
| 4 | Pagos a cuenta | art. 34.4 LGS | PASS | «Cuando la naturaleza … lo justifique, podrán realizarse pagos a cuenta … abonándose por cuantía equivalente a la justificación presentada»; «La realización de pagos a cuenta … así como el régimen de garantías, deberán preverse expresamente». In the prose (ll. 109–116). | — |
| 5 | Pagos anticipados | art. 34.4 LGS | PASS | «entregas de fondos con carácter previo a la justificación»; the «En ningún caso…» sentence verbatim; garantías sentence as in row 4. | — |
| 6 | Ningún pago | art. 34.5 LGS | PASS | 34.5 verbatim; prose ll. 118–120. | — |

## 2. m01-l03

### tabla «Algunos quórum y mayorías de las Cortes Generales» (title, and whether it reads correctly)

| # | row (short) | citation | PASS/FAIL | passage / reason | replacement |
|---|---|---|---|---|---|
| 0 | title | — | PASS | «Algunos» marks the list as selective (e.g. art. 99, 113–114 CE are in m01-l05; art. 167–168 in m01-l01). The rows from the Reglamento del Congreso (arts. 37.1, 39.4) are rules of an organ of the Cortes, so «de las Cortes Generales» still reads correctly. Every row checked in passing against arts. 72.1, 72.2, 73.2, 74.2, 79.1, 79.2, 80, 81.2, 90.2, 155.1 CE and 37.1, 39.4 RC: verbatim or faithful shortening, all in the prose. Note only: «voto ponderado» (39.4 RC) is a voting criterion rather than a majority; the header «Quórum o mayoría» tolerates it. | — |

### plazos «Plazos de la tramitación en el Senado y de la sanción»

| # | row (short) | citation | PASS/FAIL | passage / reason | replacement |
|---|---|---|---|---|---|
| 0 | title | — | PASS | Names exactly what the four steps cover (arts. 90–91 CE). | — |
| 1 | Remisión al Senado | art. 90.1 CE | PASS | «su Presidente dará inmediata cuenta del mismo al Presidente del Senado, el cual lo someterá a la deliberación de éste». | — |
| 2 | Veto o enmiendas del Senado | art. 90.2–3 CE | PASS | «en el plazo de dos meses, a partir del día de la recepción del texto … mediante mensaje motivado, oponer su veto o introducir enmiendas … El veto deberá ser aprobado por mayoría absoluta»; 90.3 «veinte días naturales en los proyectos declarados urgentes por el Gobierno o por el Congreso». Parses as one segment, anchor art. 90 CE. | — |
| 3 | Pronunciamiento del Congreso | art. 90.2 CE | PASS | «no podrá ser sometido al Rey para sanción sin que el Congreso ratifique por mayoría absoluta, en caso de veto, el texto inicial, o por mayoría simple, una vez transcurridos dos meses … o se pronuncie sobre las enmiendas». Order 2 → 3 → 4 is the article's own («no podrá ser sometido al Rey para sanción sin que…»). | — |
| 4 | Sanción | art. 91 CE | PASS | Art. 91 verbatim. | — |

### arbol «Las Cortes Generales: las Cámaras y algunos de sus órganos»

| # | row (short) | citation | PASS/FAIL | passage / reason | replacement |
|---|---|---|---|---|---|
| 0 | title | — | PASS | «algunos de sus órganos» marks the selection (e.g. Comisión Mixta, Junta de Portavoces del Senado absent). | — |
| 1 | Cortes Generales | art. 66.1 CE | PASS | 66.1 verbatim. | — |
| 2 | Congreso de los Diputados | art. 68.1 CE | PASS | «se compone de un mínimo de 300 y un máximo de 400 Diputados». Child of Cortes: 66.1. | — |
| 3 | Congreso › Pleno | art. 75.1 CE | PASS | «Las Cámaras funcionarán en Pleno y por Comisiones». | — |
| 4 | Congreso › Comisiones | art. 75.1 CE | PASS | Same. | — |
| 5 | Congreso › Mesa | art. 30 RC | PASS | 30.1–30.2 RC verbatim shortening. | — |
| 6 | Congreso › Junta de Portavoces | art. 39.1 RC | PASS | 39.1 RC (2026 text) verbatim: «Las personas designadas para las portavocías … constituyen la Junta de Portavoces, que se reunirá bajo la presidencia del Presidente o Presidenta del Congreso». | — |
| 7 | Congreso › Diputación Permanente | art. 78.1 CE | PASS | «En cada Cámara habrá una Diputación Permanente compuesta por un mínimo de veintiún miembros…». | — |
| 8 | Congreso › Grupos Parlamentarios | art. 24.1 RC | PASS | 24.1 RC verbatim. | — |
| 9 | Grupos › Grupo Mixto | art. 25.1 RC | PASS | 25.1 RC verbatim («no quedarán integrados», sic in the BOE text). Dependency holds: the RC treats the Mixto as a Grupo Parlamentario (art. 26 «Grupo Parlamentario Mixto»; art. 27.1 «con excepción del Mixto»). | — |
| 10 | Senado | art. 69.1 CE | PASS | «El Senado es la Cámara de representación territorial». | — |
| 11 | Senado › Pleno | art. 75.1 CE | PASS | As row 3. | — |
| 12 | Senado › Comisiones | art. 53.2 RS | PASS | «En su primera reunión, las Comisiones procederán a elegir de entre sus miembros una Mesa, que estará formada, por un Presidente, dos Vicepresidentes y dos Secretarios»: faithful shortening, the prose's own (l. 275). | — |
| 13 | Comisiones › Comisión General de las CCAA | art. 55 RS | PASS | «La Mesa de la Comisión General de las Comunidades Autónomas estará integrada por un Presidente, dos Vicepresidentes y cuatro Secretarios». It sits in the RS chapter on Comisiones (Sección segunda) and the prose calls it «una excepción» to the rule of row 12, so the dependency is supported. | — |
| 14 | Senado › Mesa | art. 5.1 RS | PASS | «la Mesa, que estará formada por el Presidente, dos Vicepresidentes y cuatro Secretarios». | — |
| 15 | Senado › Diputación Permanente | art. 78.1 CE | PASS | As row 7. | — |
| 16 | Senado › Grupos parlamentarios | art. 27.1 RS | PASS | 27.1 RS verbatim. | — |

## 3. m01-l01 — tabla «Tres plazos ante el Tribunal Constitucional»

| # | row (short) | citation | PASS/FAIL | passage / reason | replacement |
|---|---|---|---|---|---|
| 0 | title | — | FAIL | Only row 2 is a plazo «ante» the Tribunal. Row 1 is the Tribunal's own plazo («el Tribunal, en su caso, deberá ratificarla o levantarla en un plazo no superior a cinco meses»); row 3 is the parties' plazo before the judge («el órgano judicial oirá a las partes y al Ministerio Fiscal para que en el plazo común e improrrogable de 10 días puedan alegar», art. 35.2 LOTC). The title invites «10 días ante el TC», a wrong exam answer. | «Tres plazos: la suspensión del artículo 161.2, el recurso y la cuestión de inconstitucionalidad» |
| 1 | Impugnación por el Gobierno (161.2) | art. 161.2 CE | PASS | 161.2 CE verbatim shortening («La impugnación producirá la suspensión … pero el Tribunal, en su caso, deberá ratificarla o levantarla en un plazo no superior a cinco meses»). | — |
| 2 | Recurso de inconstitucionalidad | art. 33.1 LOTC | PASS | «dentro del plazo de tres meses a partir de la publicación de la Ley, disposición o acto con fuerza de Ley impugnado»; the label keeps the 33.2 exception, which the prose states. | — |
| 3 | Cuestión: audiencia | art. 35.2 LOTC | PASS | «plazo común e improrrogable de 10 días». The label's «antes de plantearla» is the prose's shortening of «Antes de adoptar mediante auto su decisión definitiva» (prose l. 294). | — |

## 4. m01-l07 — plazos «Plazos de la resolución de acceso y de la reclamación ante el Consejo de Transparencia y Buen Gobierno»

| # | row (short) | citation | PASS/FAIL | passage / reason | replacement |
|---|---|---|---|---|---|
| 0 | title | — | PASS | Names the two procedures the three steps cover. | — |
| 1 | Resolución de la solicitud | arts. 20.1 y 20.4 Ley 19/2013 | PASS | 20.1 («deberá notificarse al solicitante y a los terceros afectados que así lo hayan solicitado en el plazo máximo de un mes … podrá ampliarse por otro mes … y previa notificación al solicitante») and 20.4 (desestimación). Anchor art. 20 only. | — |
| 2 | Reclamación ante el CTBG | arts. 23.2, 24.1 y 24.2 Ley 19/2013 | PASS | 24.1 «con carácter potestativo y previo a su impugnación en vía contencioso-administrativa»; 23.2 «contra las resoluciones dictadas por los órganos previstos en el artículo 2.1.f) sólo cabrá la interposición de recurso contencioso-administrativo»; 24.2 plazo verbatim («del acto impugnado» shortened to «del acto», as the prose). Citation: `parse_segment` returns units art 23 and art 24, no range, norm «Ley 19/2013»; `citations.es.txt` l. 747 records anchors `boe-a-2013-12887-art-23,boe-a-2013-12887-art-24`, opening page 16. It names arts. 23 and 24 only. The «artículo 2.1.f)» inside the label is not parsed as a citation (no art-2 anchor on that line). Order 1 → 2 holds: 24.2 counts from the notification or the silence of row 1. | — |
| 3 | Resolución de la reclamación | art. 24.4 Ley 19/2013 | PASS | «El plazo máximo para resolver y notificar la resolución será de tres meses, transcurrido el cual, la reclamación se entenderá desestimada». | — |

## 5. m01-l08 — arbol «El Delegado del Gobierno y los Subdelegados»

| # | row (short) | citation | PASS/FAIL | passage / reason | replacement |
|---|---|---|---|---|---|
| 0 | title | — | PASS | Names exactly the two nodes; the child label restricts to the pluriprovinciales, so the title does not claim the RD-created uniprovincial Subdelegaciones or the Directores Insulares. | — |
| 1 | Delegado del Gobierno | art. 72.3 LRJSP | PASS | «órganos directivos con rango de Subsecretario que dependen orgánicamente del Presidente del Gobierno y funcionalmente del Ministerio competente por razón de la materia». | — |
| 2 | › Subdelegado (pluriprovinciales) | art. 69.4 LRJSP | PASS | «En cada una de las provincias de las Comunidades Autónomas pluriprovinciales, existirá un Subdelegado del Gobierno, que estará bajo la inmediata dependencia del Delegado del Gobierno». Dependency is the article's. | — |

## 6. m01-l05 — arbol «El Gobierno y sus órganos de colaboración y apoyo»

| # | row (short) | citation | PASS/FAIL | passage / reason | replacement |
|---|---|---|---|---|---|
| 0 | title | — | PASS | Mirrors Ley 50/1997, título I: cap. I (Gobierno) and cap. II «De los órganos de colaboración y apoyo del Gobierno» (arts. 7–10); all four organs of cap. II are present, so the title's completeness is true. | — |
| 1 | Gobierno (root) | art. 1.2 Ley 50/1997 | PASS | 1.2 verbatim; prose l. 11. | — |
| 2 | › Presidente | art. 98.2 CE | PASS | 98.2 CE verbatim; prose l. 25. Member of the Gobierno per 1.2. | — |
| 3 | › Vicepresidentes | art. 3 Ley 50/1997 | PASS | 3.1–3.2 faithful shortening; prose l. 46. | — |
| 4 | › Ministros | art. 4.1 Ley 50/1997 | PASS | «como titulares de sus Departamentos, tienen competencia y responsabilidad en la esfera específica de su actuación»; prose l. 48. | — |
| 5 | › Ministros sin cartera | art. 4.2 Ley 50/1997 | PASS | «podrán existir Ministros sin cartera, a los que se les atribuirá la responsabilidad de determinadas funciones gubernamentales»; prose l. 50. They are Ministros, hence members (1.2). | — |
| 6 | › Consejo de Ministros | art. 5.1 Ley 50/1997 | PASS | «como órgano colegiado del Gobierno»; prose l. 56. Dependency supported by 1.3 (cited in prose l. 13). | — |
| 7 | › Comisiones Delegadas | art. 6.2 Ley 50/1997 | PASS | 6.2.b «Los miembros del Gobierno y, en su caso, Secretarios de Estado que la integran»; prose l. 82. Under the Gobierno per 1.3. | — |
| 8 | Secretarios de Estado (root) | art. 7.1 Ley 50/1997 | PASS | 7.1 verbatim; prose l. 90. A separate root, correctly not under the Gobierno. | — |
| 9 | Comisión General de SE y Subsecretarios (root) | art. 8.1–2 Ley 50/1997 | PASS | 8.1 first paragraph and 8.2 first sentence faithful; prose ll. 96–98. | — |
| 10 | Secretariado del Gobierno (root) | art. 9.1 Ley 50/1997 | PASS | «como órgano de apoyo del Consejo de Ministros, de las Comisiones Delegadas del Gobierno y de la Comisión General…»; prose l. 108. | — |
| 11 | Gabinetes (root) | art. 10.1 Ley 50/1997 | PASS | 10.1 first sentence verbatim; prose l. 117. | — |

Every citation in the tree (1.2, 98.2 CE, 3, 4.1, 4.2, 5.1, 6.2, 7.1, 8.1, 8.2, 9.1, 10.1) is cited in the prose.

## 7. m01-l04

### arbol «El Consejo General del Poder Judicial: composición, Pleno y Comisiones»

| # | row (short) | citation | PASS/FAIL | passage / reason | replacement |
|---|---|---|---|---|---|
| 0 | title | — | PASS | Composición (122.3 CE: Presidente + veinte miembros) is complete; the six Comisiones are the whole list of 595.2 LOPJ; «composición, Pleno y Comisiones» does not claim the Presidencia's functions or the Secretaría General. | — |
| 1 | CGPJ | art. 122.2 CE | PASS | «es el órgano de gobierno del mismo». | — |
| 2 | › Presidente | art. 122.3 CE | PASS | «por el Presidente del Tribunal Supremo, que lo presidirá». | — |
| 3 | › Veinte miembros | art. 122.3 CE | PASS | «veinte miembros nombrados por el Rey por un período de cinco años». | — |
| 4 | › Pleno | art. 595.1 LOPJ | PASS | «ejerce sus atribuciones en Pleno o a través de las Comisiones». | — |
| 5 | › Comisiones | art. 595.2 LOPJ | PASS | List of 595.2. | — |
| 6–11 | › the six Comisiones | art. 595.2 / 604.1 LOPJ | PASS | Names verbatim from 595.2; Disciplinaria's text is 604.1 faithful shortening («con la sola excepción de aquellos supuestos en que la sanción propuesta fuere de separación del servicio»), prose l. 179. | — |

### tabla «Mayorías en la elección de los Vocales y en algunos acuerdos del Consejo General del Poder Judicial»

| # | row (short) | citation | PASS/FAIL | passage / reason | replacement |
|---|---|---|---|---|---|
| 0 | title | — | PASS | «algunos acuerdos» marks the selection; both rules on the election of Vocales (122.3 CE, 567.2 LOPJ) are present. | — |
| 1 | Ocho juristas a propuesta de las Cámaras | art. 122.3 CE | PASS | «cuatro a propuesta del Congreso … y cuatro a propuesta del Senado, elegidos en ambos casos por mayoría de tres quintos de sus miembros, entre abogados y otros juristas…». | — |
| 2 | Diez Vocales por Cámara | art. 567.2 LOPJ | PASS | «Cada una de las Cámaras elegirá, por mayoría de tres quintos de sus miembros, a diez Vocales…». Note: the 40 % per sex rule of the same apartado is a requirement on the result, not on the majority; it stays in the prose (l. 98). | — |
| 3 | Cese de un Vocal | art. 582.1 LOPJ | PASS | «apreciadas por el Pleno … mediante mayoría de tres quintos». | — |
| 4 | Elección del Presidente | art. 586.3 LOPJ | PASS | «en votación nominal obtenga el apoyo de la mayoría de tres quintos de los miembros del Pleno». | — |
| 5 | Cese del Presidente | art. 588.1 LOPJ | PASS | 588.1.3.ª «apreciados por tres quintos de sus miembros». | — |
| 6 | Vicepresidente del TS | art. 589.2 LOPJ | PASS | «por mayoría de tres quintos del Pleno …, a propuesta del Presidente». | — |
| 7 | Dos Magistrados del TC | art. 599.1 LOPJ | PASS | 599.1.1.ª verbatim shortening, with the three-month plazo. | — |
| 8 | Acuerdos, regla general | art. 630.1 LOPJ | FAIL | Reads wider than the article. 630.1 has two exceptions: «salvo cuando esta Ley Orgánica disponga otra cosa **o cuando se trate del nombramiento de Presidentes de Sala y Magistrados del Tribunal Supremo, Presidente de la Audiencia Nacional y Presidentes de Sala de la Audiencia Nacional, Presidentes de los Tribunales Superiores de Justicia y Presidentes de Sala de los Tribunales Superiores de Justicia, y Presidentes de Audiencias Provinciales, en cuyo caso se requerirá una mayoría de tres quintos de los miembros presentes**» (plus the CNI Magistrate). The row keeps only the first. With no nombramientos row in the table, a nombramiento of a Magistrado del TS reads as mayoría absoluta. Restoring the prose's own exception (l. 184: «Presidentes de Sala y Magistrados del Tribunal Supremo») would make the AN, TSJ and Audiencia Provincial presidencies read as mayoría absoluta: that would need a clause the prose lacks. | Remove the row and list the gap in the ledger (prose l. 183–184 names only Presidentes de Sala and Magistrados del TS among the 630.1 nombramientos). |

## 8. m01-l09 — tabla «Tres materias en las dos listas de los artículos 148.1 y 149.1»

| # | row (short) | citation | PASS/FAIL | passage / reason | replacement |
|---|---|---|---|---|---|
| 0 | title | — | PASS | States the count; does not claim completeness. | — |
| 1 | Montes | arts. 148.1.8.ª y 149.1.23.ª CE | PASS | Both cells verbatim from the CE (and from the prose's own lists); the prose pairs the two (ll. 282–283). | — |
| 2 | Puertos | arts. 148.1.6.ª y 149.1.20.ª CE | PASS | 148.1.6.ª verbatim; «Puertos de interés general» a verbatim fragment of 149.1.20.ª; paired in the prose (ll. 283–284). | — |
| 3 | Sanidad | arts. 148.1.21.ª y 149.1.16.ª CE | PASS | Both verbatim; paired in the prose (ll. 284–285). The prose pairs a fourth materia (tráfico) with the Estado only, so it rightly stays out. | — |

## 9. m01-l10 — tabla «El municipio, la provincia y la isla en la Constitución»

| # | row (short) | citation | PASS/FAIL | passage / reason | replacement |
|---|---|---|---|---|---|
| 0 | title and header «Qué establece» | — | FAIL | Title + header read as what the Constitution establishes about each entity, but the rows leave out what art. 140 says about the election of Concejales and Alcaldes and the concejo abierto, and what 141.1 says on altering provincial limits by ley orgánica (both in the prose; the latter in «Lo que más cae»). A selective list reads as complete. | Header «Personalidad, gobierno y administración» (title unchanged). |
| 1 | Municipio | art. 140 CE | FAIL | Content verbatim, but the cell opens «Gozarán de personalidad jurídica plena» with no subject; after the singular label «Municipio» the plural verb reads wrong. The norm has «Estos gozarán». | «Los municipios gozarán de personalidad jurídica plena. Su gobierno y administración corresponde a sus respectivos Ayuntamientos, integrados por los Alcaldes y los Concejales» |
| 2 | Provincia | art. 141.1–2 CE | PASS | 141.1 first sentence and 141.2 verbatim; prose ll. 28–35. | — |
| 3 | Isla | art. 141.4 CE | PASS | 141.4 verbatim; the label carries «en los archipiélagos». | — |

## 10. m01-l11 — tabla «Algunas reglas de votación del Consejo Europeo, el Consejo, el Parlamento Europeo y la Comisión»

| # | row (short) | citation | PASS/FAIL | passage / reason | replacement |
|---|---|---|---|---|---|
| 0 | title | — | PASS | «Algunas» marks the selection. | — |
| 1 | Consejo Europeo | art. 15.4 TUE | PASS | 15.4 verbatim. | — |
| 2 | Consejo Europeo, procedimiento y reglamento | art. 235.3 TFUE | PASS | 235.3 verbatim. | — |
| 3 | Consejo | art. 16.3 TUE | PASS | 16.3 verbatim. | — |
| 4 | Consejo, mayoría cualificada desde 1-11-2014 | art. 16.4 TUE | FAIL | Verbatim to the whole of 16.4, but (a) its third sentence, «Las demás modalidades reguladoras del voto por mayoría cualificada se establecen en el apartado 2 del artículo 238 del TFUE», is not in the prose: the prose gives the 238.2 rule itself (l. 154–156) but never this cross-reference; (b) the row still reads wider than 16.4 + the prose on 238.2: 238.2 opens «No obstante lo dispuesto en el apartado 4 del artículo 16 TUE … cuando el Consejo no actúe a propuesta de la Comisión o del Alto Representante, la mayoría cualificada se definirá como un mínimo del 72 %…», a condition the prose carries and the label does not, so the 55 % rule reads as the only definition. | Label «Consejo, mayoría cualificada a partir del 1 de noviembre de 2014, salvo el caso del artículo 238.2»; cell = 16.4 first two paragraphs only (drop the cross-reference sentence); add a row «Consejo, cuando no actúa a propuesta de la Comisión o del Alto Representante \| La mayoría cualificada sube a un mínimo del 72 % de los miembros del Consejo que represente a Estados miembros que reúnan como mínimo el 65 % de la población de la Unión \| art. 238.2 TFUE» (the prose's words; 238.2 is cited in the prose). Ledger: 238.3 (not all members voting) is a further exception the prose lacks. |
| 5 | Consejo, mayoría simple | art. 238.1 TFUE | PASS | 238.1 verbatim. | — |
| 6 | Parlamento Europeo | art. 231 TFUE | PASS | 231 verbatim; the label carries «salvo disposición en contrario de los Tratados». | — |
| 7 | Comisión | art. 250 TFUE | PASS | 250 verbatim. | — |

## Totals

90 checks (titles, headers, rows and nodes): **85 PASS, 5 FAIL**.

| Esquema | Checks | FAIL |
|---|---|---|
| m05-l06 tabla | 7 | 0 |
| m01-l03 tabla (title) | 1 | 0 |
| m01-l03 plazos | 5 | 0 |
| m01-l03 arbol | 17 | 0 |
| m01-l01 tabla | 4 | 1 (title) |
| m01-l07 plazos | 4 | 0 |
| m01-l08 arbol | 3 | 0 |
| m01-l05 arbol | 12 | 0 |
| m01-l04 arbol | 12 | 0 |
| m01-l04 tabla | 9 | 1 (630.1 row) |
| m01-l09 tabla | 4 | 0 |
| m01-l10 tabla | 4 | 2 (header, municipio row) |
| m01-l11 tabla | 8 | 1 (16.4 row) |

The FAIL on m01-l04 row 8 cannot be fixed by rewording: a replacement would need a clause the prose lacks, so the row
goes and the gap goes to the ledger.
