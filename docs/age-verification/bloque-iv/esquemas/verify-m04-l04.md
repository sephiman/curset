# Verification — esquemas of m04-l04 (2026-10-18)

The reviewer did not write these esquemas or the lesson. Each row of the three `tabla` esquemas added to
`C/es/lessons/m04-l04.md` (the `git diff` shows only added lines; the prose is unchanged) was checked against the cited
article, as the spec (`spec.md`) asks: verbatim or faithful verbatim shortening, no wider reading, right citation,
fact already in the prose, no order claimed, placement after the paragraphs summarised. Sources: the scratchpad
`txt/*.clean` texts (`pdftotext -layout` of the consolidated BOE PDFs in `C/sources/normativa/`): TREBEP
(2026-10-03), RD 365/1995 (2006-03-04), Ley 30/1984 (2015-10-31), LGSS (2026-10-03). Article bodies read with `art.py`
(the last heading match). Ley 30/1984 arts. veintinueve and treinta y tres, and LGSS disposición transitoria séptima,
read with `grep -n` and `sed` on the `.clean` file. No source was taken from memory.

## Tabla «Jubilación forzosa y prolongación en el servicio activo»

| # | esquema / row (short) | citation | PASS/FAIL | passage / reason | replacement |
|---|---|---|---|---|---|
| 1 | TREBEP — de oficio a los 65; prolongación hasta 70; resolución motivada; excluidos | art. 67.3 TREBEP | PASS | Verbatim: «La jubilación forzosa se declarará de oficio al cumplir el funcionario los sesenta y cinco años de edad. No obstante, en los términos de las leyes de Función Pública […] como máximo hasta que se cumpla setenta años de edad. La Administración Pública competente deberá de resolver de forma motivada […]». The last sentence drops «De lo dispuesto en los dos párrafos anteriores» before «quedarán excluidos». The exclusion still applies to the whole row, which holds only those two paragraphs, so it is not widened. In prose (l. 74–77). | — |
| 2 | TREBEP, funcionario del Régimen General — edad de la pensión contributiva sin coeficiente reductor | art. 67.4 TREBEP | PASS | «la edad de la jubilación forzosa del personal funcionario incluido en el Régimen General de la Seguridad Social será, en todo caso, la que prevean las normas reguladoras de dicho régimen para el acceso a la pensión de jubilación en su modalidad contributiva sin coeficiente reductor por razón de la edad». The label carries the subject. Leaving out «Con independencia de la edad legal […] apartado 3» does not widen the row. In prose (l. 77–78). | — |
| 3 | LGSS, desde 2027 — 67, o 65 con 38 años y 6 meses | art. 205.1.a) y disposición transitoria séptima LGSS | PASS | Art. 205.1.a): «Haber cumplido sesenta y siete años de edad, o sesenta y cinco años cuando se acrediten treinta y ocho años y seis meses de cotización». DT 7ª, table: «A partir del año 2027 — 38 años y 6 meses o más: 65 años; menos de 38 años y 6 meses: 67 años». The row follows the prose's shortening (l. 78–80), and the label «desde 2027» carries the DT 7ª condition. | — |
| 4 | Ley 30/1984 — no se declara mientras prolongue hasta 70; exceptuados | art. 33 Ley 30/1984 | PASS | «tal declaración no se producirá hasta el momento en que los funcionarios cesen en la situación de servicio activo, en aquellos supuestos en que voluntariamente prolonguen su permanencia en la misma hasta, como máximo, los setenta años de edad. […] De lo dispuesto en el párrafo anterior quedan exceptuados los funcionarios de aquellos cuerpos y escalas que tengan normas específicas de jubilación». «La declaración de jubilación forzosa» resolves «tal declaración» (the art.'s first paragraph). The procedural sentence («Las Administraciones Públicas dictarán las normas de procedimiento») is left out, as it is in the prose. In prose (l. 82–84). | — |

## Tabla «Efectos de las situaciones administrativas»

| # | esquema / row (short) | citation | PASS/FAIL | passage / reason | replacement |
|---|---|---|---|---|---|
| 5 | Servicios especiales — retribuciones del puesto, trienios; cómputo; salvo transferencia UE | art. 87.2 TREBEP | PASS | Verbatim of the whole apartado, «Quienes se encuentren en situación de servicios especiales» moved into the label. The exception for the right of transfer is kept. In prose (l. 160–163). | — |
| 6 | Servicios especiales, en el RD 365/1995 — cómputo | art. 8.2 RD 365/1995 | PASS | Verbatim: «se les computará el tiempo que permanezcan en tal situación, a efectos de ascensos, consolidación de grado personal, trienios y derechos pasivos, así como a efectos del cómputo del período mínimo de servicios efectivos para solicitar el pase a la situación de excedencia voluntaria por interés particular». In prose (l. 163–165). | — |
| 7 | Excedencia voluntaria por interés particular — sin retribuciones ni cómputo | art. 89.2 TREBEP | PASS | Verbatim, last paragraph of 89.2. In prose (l. 187–188). | — |
| 8 | Excedencia voluntaria por agrupación familiar — sin retribuciones ni cómputo | art. 89.3 TREBEP | PASS | Verbatim, second paragraph of 89.3. In prose (l. 202–203). | — |
| 9 | Excedencia por cuidado de familiares — cómputo; reserva dos años, luego localidad | art. 89.4 TREBEP | PASS | Verbatim: «El tiempo de permanencia en esta situación será computable a efectos de trienios, carrera y derechos en el régimen de Seguridad Social que sea de aplicación. El puesto de trabajo desempeñado se reservará, al menos, durante dos años. Transcurrido este periodo, dicha reserva lo será a un puesto en la misma localidad y de igual retribución». In prose (l. 218–219). | — |
| 10 | Cuidado de hijos, en el RD 365/1995 — reserva y cómputo | art. 14.2 RD 365/1995 | PASS | «tendrán derecho a la reserva del puesto de trabajo y a su cómputo a efectos de trienios, consolidación de grado personal, derechos pasivos y solicitud de excedencia voluntaria por interés particular, de acuerdo con lo dispuesto en la Ley que regula esta figura». The trailing cross-reference is left out, which does not change the scope. In prose (l. 221–223). | — |
| 11 | Violencia de género o sexual — seis meses de reserva, prórroga a 18, dos meses de retribuciones | art. 89.5 TREBEP | PASS | 89.5, paragraphs 2–4, verbatim except for dropped clauses: «que desempeñarán», «a los señalados anteriormente», «a fin de garantizar la efectividad del derecho de protección de la víctima» and «de esta excedencia la funcionaria tendrá». Every number (seis, tres, dieciocho, dos), the condition «Cuando las actuaciones judiciales lo exigieran» and «con idénticos efectos» are kept. The prose (l. 230–233) makes the same cuts. | — |
| 12 | Excedencia voluntaria incentivada — impide el sector público; mensualidad por año, máx. doce | arts. 18.4 y 18.5 RD 365/1995 | PASS | 18.4: «impedirá desempeñar puestos de trabajo en el sector público, bajo ningún tipo de relación funcionarial o contractual, sea ésta de naturaleza laboral o administrativa». 18.5 is verbatim from «una mensualidad» to «doce mensualidades». Leaving out «sea ésta de naturaleza laboral o administrativa» only restates «ningún tipo», so it does not narrow the bar. In prose (l. 254–258). | — |
| 13 | Excedencias voluntarias, salvo esa mensualidad — sin reserva, sin retribuciones, sin cómputo | art. 19 RD 365/1995 | PASS | «Las distintas modalidades de excedencia voluntaria no producen, en ningún caso, reserva de puesto de trabajo y los funcionarios que se encuentren en las mismas no devengarán retribuciones, salvo lo previsto en el apartado 5 del artículo anterior. No será computable el tiempo permanecido en esta situación a efectos de promoción, trienios y derechos pasivos». The «salvo» is carried by the label in the prose's own words («salvo esa mensualidad», l. 260). See Notes. | (optional, verbatim) `\| Excedencias voluntarias \| No producen, en ningún caso, reserva de puesto de trabajo y los funcionarios que se encuentren en las mismas no devengarán retribuciones, salvo lo previsto en el apartado 5 del artículo anterior. No será computable el tiempo permanecido en esta situación a efectos de promoción, trienios y derechos pasivos \| art. 19 RD 365/1995 \|` |
| 14 | Expectativa de destino, salvo en las retribuciones — equiparada al servicio activo | art. 12.5 RD 365/1995 | PASS | Second paragraph of 12.5, verbatim: «A los restantes efectos, incluido el régimen de incompatibilidades, esta situación se equipara a la de servicio activo». «Restantes» refers to the retribuciones in the first paragraph, and the label says so, as the prose does (l. 250–251). The amounts of those retribuciones are in neither the prose nor the row. | — |
| 15 | Excedencia forzosa — retribuciones básicas, prestaciones por hijo; cómputo pasivos y trienios | art. 13.6 RD 365/1995 | PASS | Verbatim. In prose (l. 251–252). | — |
| 16 | Suspensión de funciones — privado de funciones y derechos; pierde el puesto si excede de seis meses | art. 90.1 TREBEP | PASS | Verbatim, with «declarado en la situación de suspensión» moved into the label. In prose (l. 265–266). | — |

## Tabla «Duración de las situaciones»

| # | esquema / row (short) | citation | PASS/FAIL | passage / reason | replacement |
|---|---|---|---|---|---|
| 17 | Interés particular, Ley 30/1984 — no menos de dos años continuados | art. 29.3.c) Ley 30/1984 | PASS | «en ella no se podrá permanecer menos de dos años continuados» (art. veintinueve.3.c), second paragraph). Verbatim. In prose (l. 190–191). The article's derogation and the BOE note keeping it in force are stated in the prose (l. 115–118). | — |
| 18 | Interés particular, RD 365/1995 — dos años a los años servidos, máx. quince | art. 16.3 RD 365/1995 | PASS | Verbatim. In prose (l. 191–192). | — |
| 19 | Agrupación familiar — mínimo dos, máximo quince | art. 17 RD 365/1995 | PASS | 17.1: «con una duración mínima de dos años y máxima de quince». In prose (l. 204). | — |
| 20 | Cuidado de familiares — tres años por hijo / por familiar, con condiciones | art. 89.4 TREBEP | PASS | First and second paragraphs of 89.4, verbatim from «no superior a tres años» on. Each condition is kept: «cada», guarda or acogimiento permanente, start date, segundo grado, «no pueda valerse por sí mismo», «no desempeñe actividad retribuida». In prose (l. 209–213). | — |
| 21 | Violencia de género o sexual — sin plazo de permanencia | art. 89.5 TREBEP | PASS | «sin que sea exigible plazo de permanencia en la misma». Verbatim. In prose (l. 229). | — |
| 22 | Prestación de servicios en el sector público — mientras dure la relación | art. 15.3 RD 365/1995 | PASS | «podrán permanecer en esta situación en tanto se mantenga la relación de servicios que dio origen a la misma». Verbatim. In prose (l. 244–245). | — |
| 23 | Expectativa de destino — máximo un año, luego excedencia forzosa | art. 12.2 RD 365/1995 | PASS | Verbatim: «un período máximo de un año, transcurrido el cual pasarán a la situación de excedencia forzosa». In prose (l. 249). | — |
| 24 | Excedencia voluntaria incentivada — cinco años | art. 18.4 RD 365/1995 | PASS | «tendrá una duración de cinco años». In prose (l. 254). | — |
| 25 | Suspensión firme por sanción disciplinaria — no más de seis años | art. 90.2 TREBEP | PASS | «La suspensión firme por sanción disciplinaria no podrá exceder de seis años». The label carries the subject, which keeps out the suspensión firme by criminal sentence. In prose (l. 267–268). | — |
| 26 | Suspensión provisional en expediente disciplinario — seis meses, salvo paralización | art. 21.3 RD 365/1995 | PASS | «no pudiendo exceder esta suspensión de seis meses, salvo en caso de paralización del procedimiento imputable al interesado». The «salvo» is kept, and the label carries the expediente condition. In prose (l. 271–272). | — |

## Placement

- «Jubilación forzosa y prolongación en el servicio activo» follows the three Jubilación paragraphs it lays out
  (l. 74–86, arts. 67.3, 67.4, LGSS, art. 33 Ley 30/1984), and comes before «Rehabilitación». OK.
- «Efectos de las situaciones administrativas» and «Duración de las situaciones» come at the end of «Suspensión de
  funciones», before «Reingreso al servicio activo». They gather facts from every section from «Servicios especiales:
  efectos y reingreso» (l. 158) to «Suspensión de funciones» (l. 263), all above them. Each row follows the
  paragraph it summarises. OK.
- Order: all three are `tabla`, and no label claims a sequence. The row order follows the lesson's section order, not
  any chronology. OK.

## Notes

- #13 and #14: the exception sits in the label («salvo esa mensualidad de la incentivada», «salvo en las
  retribuciones») and not in the fact field, in the prose's words. That is allowed: a label may carry the condition.
  In #13, «esa» refers back to row #12, which sits right above it. If the row were ever moved or shown alone, the
  reference would dangle. The optional verbatim replacement given for #13 avoids that.
- #3: art. 205.1.a) also says «sin que se tenga en cuenta la parte proporcional correspondiente a las pagas
  extraordinarias» for the 38 years and 6 months. That is a counting rule, also left out of the prose, and it does
  not change who the age applies to. This lesson was reviewed on 2026-10-18, and the label «desde 2027» is accurate
  only from 1 January 2027. For 2026, DT 7ª gives «38 años y 3 meses o más — 65 años; menos — 66 años y 10 meses»,
  which neither the prose nor the row states. That is not a row defect.
- #3: the LGSS row gives the pension age. It reads as the forced-retirement age only through row #2 (art. 67.4), as
  the prose's colon does. The rows are adjacent and the table title frames them, so this is not failed.
- #19: art. 17 RD 365/1995 defines its agrupación familiar more narrowly than art. 89.3 TREBEP («otro municipio»;
  «Administración pública, Organismo autónomo o Entidad Gestora de la Seguridad Social, así como en Organos
  Constitucionales o del Poder Judicial»). The row gives only the duration, cited to the RD, and the prose does the
  same.
- #11 and #21: the label «Excedencia por violencia de género o de violencia sexual» leaves out «Las funcionarias
  víctimas». Art. 89.6 extends the same conditions to victims of terrorism. Neither point widens the effects or the
  duration stated.
- Voice: the headers and labels («Norma», «Regla», «Situación», «Efectos», «Duración», «Artículo») are plain
  Peninsular Spanish, and none of them is an invented term.
- Citation forms «arts. 18.4 y 18.5 RD 365/1995» (#12) and «art. 205.1.a) y disposición transitoria séptima LGSS»
  (#3) are pairs. The prose cites them separately (18.4, 18.5) or in exactly this form (LGSS). This is a table, not a
  list, so the rule against a citation ending in a letter does not arise, and none of them ends in a letter anyway.

## Counts

26 rows checked: 26 PASS, 0 FAIL. One optional verbatim replacement offered (#13). Placement OK for all three
esquemas.
