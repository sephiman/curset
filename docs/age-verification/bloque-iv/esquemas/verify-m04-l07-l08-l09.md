# Verification — esquemas of m04-l07, m04-l08, m04-l09 (2026-10-18)

The reviewer did not write these esquemas or the lessons. Each row was checked against the cited article, as the spec
(`spec.md`) asks: verbatim or faithful verbatim shortening that keeps every number, plazo, organ, condition and
exception; no wider reading; right citation; fact already in the prose; no order the text does not support; placement
after the paragraphs summarised. Scope: the lines that `git diff` shows as added in the three lessons (only
`:::esquema` blocks; the prose is unchanged). Sources: the scratchpad `txt/*.clean` texts (`pdftotext -layout` of the
consolidated BOE PDFs in `C/sources/normativa/`): RDL 4/2000 (`trlssfce`, 2024-12-21), RD 375/2003 (2024-12-21), ET
(2026-10-03), IV Convenio único AGE (2025-04-11), Resolución de 14-04-2026 (jornada y horarios AGE, 2026-04-15), LGSS
(2026-10-03). Article bodies read with `art.py` (the last heading match); apartado 2.4 of the Resolución read with
`grep -n`. No source was taken from memory.

## m04-l07

| # | esquema / row (short) | citation | PASS/FAIL | passage / reason | replacement |
|---|---|---|---|---|---|
| 1 | tabla «Alta, conservación y baja como mutualista» / Alta obligatoria | art. 7.1 RDL 4/2000 | PASS | Verbatim: «Los funcionarios de carrera de la Administración Civil del Estado se incorporarán obligatoriamente, como mutualistas, a la Mutualidad General de Funcionarios Civiles del Estado, en el momento de la toma de posesión de su cargo, cuando adquieran la condición de funcionario, o sean rehabilitados en dicha condición, o reingresen al servicio activo». In prose (l. 54–56). | — |
| 2 | tabla / Conservación de la condición | art. 7.1 RDL 4/2000 | PASS | «y conservarán la condición de mutualista, con los mismos derechos y obligaciones que en la situación de servicio activo, cuando pasen a alguna de las siguientes situaciones: a) Servicios especiales, salvo lo dispuesto en el párrafo c) del apartado 1 y en el apartado 3 del artículo 8. b) … f) Suspensión provisional o firme de funciones». All six situations, with the a) salvedad, are kept. In prose (l. 58–61). | — |
| 3 | tabla / Baja como mutualista obligatorio, entre otros | art. 8.1.a)–b) RDL 4/2000 | PASS | Verbatim of 8.1.a) (with its «salvo que ejerciten la opción … apartado 3 del artículo 7») and 8.1.b). «entre otros supuestos» in the label covers c) and d). In prose (l. 63–65). A citation ending in a letter is only barred in list-type esquemas; this is a `tabla`. | — |
| 4 | tabla / Mutualista voluntario | art. 8.2 RDL 4/2000 | PASS | Verbatim: «Podrán mantener facultativamente la situación de alta como mutualistas voluntarios, con igualdad de derechos, los funcionarios a que se refieren los párrafos a), b) y c) del apartado 1 de este artículo, siempre que abonen exclusivamente a su cargo las cuotas correspondientes al funcionario y al Estado». In prose (l. 65–68). | — |
| 5 | tabla / Plazo de la opción | art. 10.3 RD 375/2003 | FAIL | Number, plazo, dies a quo and the effect of not opting are verbatim. The organ is dropped: «El derecho de opción deberá ser ejercitado por el propio interesado, ante la Mutualidad General, en el plazo de un mes…». The prose keeps it («La opción se ejerce ante la MUFACE en el plazo de un mes», l. 68). Restore the organ in the norm's words. («por el propio interesado» is not in the prose, so it stays out.) | `\| Plazo de la opción \| Ante la Mutualidad General, en el plazo de un mes, a partir de la fecha de recepción de la notificación, o de la fecha de efectos si ésta fuera posterior, del acuerdo o declaración de excedencia voluntaria, de la pérdida de la condición de funcionario, o del ejercicio del derecho de transferencia; en caso de no ejercitarlo, baja con la misma fecha de efectos de los actos administrativos correspondientes \| art. 10.3 RD 375/2003 \|` |
| 6 | tabla «Retribuciones y subsidio…» / Tres primeros meses | art. 21.1 RDL 4/2000 | PASS | Final paragraph of 21.1, verbatim: «Durante los tres primeros meses la persona mutualista tendrá derecho al percibo de la totalidad de las retribuciones previstas en las Leyes y Reglamentos aplicables según su respectiva Carrera, Cuerpo y Escala, a cargo de los órganos de personal correspondientes». In prose (l. 131–132), cited there as «art. 21.1 RDL 4/2000, párrafo final». | — |
| 7 | tabla / Desde el cuarto mes | art. 21.1.b) RDL 4/2000 | PASS | Verbatim: «Desde el cuarto mes percibirá las retribuciones básicas, la prestación por hijo a cargo, en su caso, y un subsidio por incapacidad temporal a cargo de la Mutualidad General de Funcionarios Civiles del Estado». In prose (l. 132–133). | — |
| 8 | tabla / Nacimiento del derecho al subsidio | art. 95.1–2 RD 375/2003 | PASS | 95.2: «El derecho al subsidio por incapacidad temporal nace a partir del día en que finalice el plazo de tres meses desde el inicio de la situación de incapacidad temporal». 95.1: «tengan acreditado un período de cotización de seis meses, salvo que tengan cubierta esta contingencia por otro régimen de Seguridad Social, organismo o institución, por la misma relación de servicios. En la situación especial de incapacidad temporal para las personas funcionarias donantes de órganos o tejidos para su trasplante, no se exigirá periodo previo de cotización». Faithful shortening; the salvedad and the donor exception are kept. In prose (l. 134–137). | — |
| 9 | tabla / Cuantía del subsidio | art. 21.1.b) RDL 4/2000 | PASS | «cuya cuantía, fija e invariable mientras dure la incapacidad, será la mayor de las dos cantidades siguientes: 1.ª El 80 por ciento de las retribuciones básicas (sueldo, trienios y grado, en su caso), incrementadas en la sexta parte de una paga extraordinaria, correspondientes al tercer mes de licencia. 2.ª El 75 por ciento de las retribuciones complementarias devengadas en el tercer mes de licencia». Verbatim. In prose (l. 139–142). | — |
| 10 | tabla / IT por donación de órganos o tejidos | art. 21.1.c) RDL 4/2000 | PASS | «el subsidio … tendrá una cuantía igual al 100 por ciento de las retribuciones complementarias devengadas desde el tercer mes de licencia». «desde» kept. In prose (l. 142–144). | — |
| 11 | tabla / Riesgo durante el embarazo o la lactancia natural | art. 22.4 RDL 4/2000 | PASS | «los derechos económicos en toda la duración de la licencia serán los establecidos en el artículo 21 precedente con la particularidad de que la prestación económica equivalente al subsidio por incapacidad temporal consistirá en un subsidio a cargo de la Mutualidad General de Funcionarios Civiles del Estado en cuantía igual al 100 por ciento de las retribuciones complementarias devengadas en el tercer mes de licencia». Faithful shortening. In prose (l. 151–153). | — |

Placement: the first esquema follows «Afiliación, alta y baja» (l. 54–71); the second follows «Incapacidad temporal» and
«Riesgo durante el embarazo» (l. 131–153). Both PASS.

## m04-l08

| # | esquema / row (short) | citation | PASS/FAIL | passage / reason | replacement |
|---|---|---|---|---|---|
| 1 | tabla «La jornada en el ET, el Convenio único y la Resolución…» / ET | art. 34.1 ET | PASS | Verbatim, second paragraph of 34.1: «La duración máxima de la jornada ordinaria de trabajo será de cuarenta horas semanales de trabajo efectivo de promedio en cómputo anual». In prose (l. 128–129). | — |
| 2 | tabla / Convenio único | art. 64.1 Convenio único | PASS | Verbatim: «La duración máxima de la jornada general de trabajo será de treinta y siete horas y media semanales de trabajo efectivo de promedio en cómputo anual, equivalente a mil seiscientas cuarenta y dos horas anuales». In prose (l. 129–131). «general» keeps it apart from the 64.3 jornada of up to forty hours, which the prose gives at l. 145–146. | — |
| 3 | tabla / Resolución de 14-04-2026, calendarios laborales | apartado 2.4.a) Resolución de 14-04-2026 | PASS | «2.4 El calendario laboral habrá de respetar, en todo caso: a) La duración de la jornada general, establecida en 35 horas semanales, sin que pueda menoscabarse el cómputo anual…». The label carries the context (what the calendario must respect). In prose (l. 134–135). The table puts the three rules side by side and does not say which applies, as the spec requires. | — |
| 4 | tabla «Horas extraordinarias…» / Convenio único, qué son | art. 72.1 Convenio único | PASS | Verbatim: «las que excedan de 37,5 horas semanales o, en su caso, las que excedan de la jornada contemplada en el artículo 64.3 del presente Convenio». In prose (l. 145–146). | — |
| 5 | tabla / Convenio único, compensación | art. 72.2 Convenio único | PASS | «se compensarán preferentemente con tiempo de descanso acumulable a razón de dos horas por cada una realizada, salvo en los casos de horas nocturnas o en días festivos cuya compensación será de dos horas y media. Si así se pacta se retribuirán en metálico conforme a lo establecido en el artículo 59 del Convenio. En el caso de compensación por períodos de descanso, en todos los supuestos, ésta deberá producirse en el plazo de los cuatro meses siguientes a la realización de las horas extraordinarias, de conformidad con lo dispuesto en el artículo 35 [ET]». «El descanso deberá producirse» is the prose's own shortening («El descanso compensatorio se produce»); the closing cross-reference to art. 35 ET is left out (see Notes). Every number, plazo and exception kept. In prose (l. 148–152). | — |
| 6 | tabla / Convenio único, límite | art. 72.3 Convenio único | PASS | «En ningún caso las mismas podrán exceder de sesenta horas anuales, salvo las razones justificadas previstas en el artículo 35.3 del texto refundido de la Ley del Estatuto de los Trabajadores». In prose (l. 153–154). | — |
| 7 | tabla / ET, compensación | art. 35.1 ET | PASS | Verbatim of the second sentence; the third shortened: «En ausencia de pacto al respecto, se entenderá que las horas extraordinarias realizadas deberán ser compensadas mediante descanso dentro de los cuatro meses siguientes a su realización». Nothing lost. In prose (l. 156–158). | — |

Placement: the jornada esquema follows the jornada paragraph (l. 128–135) and precedes the horas extraordinarias
paragraphs; the horas extraordinarias esquema follows them (l. 145–158). Both PASS.

## m04-l09

| # | esquema / row (short) | citation | PASS/FAIL | passage / reason | replacement |
|---|---|---|---|---|---|
| 1 | tabla «Duración de la incapacidad temporal» / enfermedad común o profesional y accidente | art. 169.1.a) LGSS | PASS | Verbatim: «Las debidas a enfermedad común o profesional y a accidente, sea o no de trabajo, mientras el trabajador reciba asistencia sanitaria de la Seguridad Social y esté impedido para el trabajo, con una duración máxima de trescientos sesenta y cinco días, prorrogables por otros ciento ochenta días cuando se presuma que durante ellos puede el trabajador ser dado de alta médica por curación». In prose (l. 57–60). | — |
| 2 | tabla / períodos de observación | art. 169.1.b) LGSS | PASS | Verbatim: «Los períodos de observación por enfermedad profesional en los que se prescriba la baja en el trabajo durante los mismos, con una duración máxima de ciento ochenta días, prorrogables por otros ciento ochenta días cuando se estime necesario para el estudio y diagnóstico de la enfermedad». In prose (l. 61–63). | — |
| 3 | tabla / Extinción del derecho al subsidio, entre otras causas | art. 174.1 LGSS | PASS | Verbatim: «El derecho al subsidio se extinguirá por el transcurso del plazo máximo de quinientos cuarenta y cinco días naturales desde la baja médica». «entre otras causas» in the label. In prose (l. 82–84). | — |
| 4 | tabla «Períodos mínimos de cotización» / IT enfermedad común | art. 172 LGSS | PASS | 172.a): «En caso de enfermedad común, ciento ochenta días dentro de los cinco años inmediatamente anteriores al hecho causante». The label's exception is the prose's faithful shortening of the rest of 172.a) (no periods for párrafos segundo y cuarto of 169.1.a), the 178.1 periods for párrafo tercero): «Las situaciones especiales del art. 169.1.a) tienen reglas propias» (l. 65–67). | — |
| 5 | tabla / IT accidente y enfermedad profesional | art. 172 LGSS | PASS | 172.b), verbatim: «En caso de accidente, sea o no de trabajo, y de enfermedad profesional, no se exigirá ningún período previo de cotización». In prose (l. 66). | — |
| 6 | tabla / Nacimiento, menos de veintiún años | art. 178.1 LGSS | PASS | 178.1.a): «Si la persona trabajadora tiene menos de veintiún años de edad en la fecha del nacimiento, o en la fecha de la decisión administrativa […] no se exigirá período mínimo de cotización». In prose (l. 101–102). The reference date for the age is left out in the row and in the prose (see Notes). | — |
| 7 | tabla / Nacimiento, veintiún a veintiséis | art. 178.1 LGSS | PASS | 178.1.b): «noventa días cotizados dentro de los siete años inmediatamente anteriores al momento de inicio del descanso. Se considerará cumplido el mencionado requisito si, alternativamente, acredita ciento ochenta días cotizados a lo largo de su vida laboral, con anterioridad a esta última fecha». Faithful; «con anterioridad a esta última fecha» left out, as in the prose (see Notes). In prose (l. 102–103). | — |
| 8 | tabla / Nacimiento, veintiséis cumplidos | art. 178.1 LGSS | PASS | 178.1.c): «ciento ochenta días cotizados dentro de los siete años inmediatamente anteriores al momento de inicio del descanso. […] alternativamente, acredita trescientos sesenta días cotizados a lo largo de su vida laboral». Same as row 7. In prose (l. 103–104). | — |
| 9 | tabla / Jubilación, modalidad contributiva | art. 205.1 LGSS | PASS | 205.1.b): «Tener cubierto un período mínimo de cotización de quince años, de los cuales al menos dos deberán estar comprendidos dentro de los quince años inmediatamente anteriores al momento de causar el derecho. A efectos del cómputo de los años cotizados no se tendrá en cuenta la parte proporcional correspondiente a las pagas extraordinarias. En los supuestos en que se acceda a la pensión de jubilación desde una situación de alta o asimilada a la de alta, sin obligación de cotizar, el período de dos años […] deberá estar comprendido dentro de los quince años inmediatamente anteriores a la fecha en que cesó la obligación de cotizar». Faithful shortening; all numbers and the special case kept. In prose (l. 146–150). | — |
| 10 | tabla / Jubilación parcial con contrato de relevo | art. 215.2.a) LGSS | FAIL | Numbers and exclusions are verbatim: «acreditar un periodo de cotización de treinta y tres años, sin que, a tales efectos, se tengan en cuenta las bonificaciones o anticipaciones de la edad de jubilación […] ni la parte proporcional correspondiente por pagas extraordinarias» and «En el supuesto de personas con discapacidad en grado igual o superior al 33 por ciento, el período de cotización de 33 años […] se reducirá al de veinticinco años». The label drops two conditions of 215.2's opening words, which set who the rule covers: «siempre que con carácter simultáneo se celebre un contrato de relevo […], los trabajadores a tiempo completo que no hayan alcanzado la edad ordinaria de jubilación podrán acceder». «Jubilación parcial con contrato de relevo» reads wider (any worker, any relevo). The prose keeps both: «Con contrato de relevo simultáneo, el trabajador a tiempo completo» (l. 153). | `\| Jubilación parcial de los trabajadores a tiempo completo, con contrato de relevo simultáneo \| Treinta y tres años, sin que se tengan en cuenta las bonificaciones o anticipaciones de la edad de jubilación ni la parte proporcional correspondiente por pagas extraordinarias; veinticinco años con discapacidad en grado igual o superior al 33 por ciento \| art. 215.2.a) LGSS \|` |
| 11 | tabla «Cuantía de las prestaciones económicas» / Incapacidad temporal | art. 171 LGSS | PASS | «consistirá en un subsidio equivalente a un tanto por ciento sobre la base reguladora, que se fijará y se hará efectivo en los términos establecidos en esta ley y en sus normas de desarrollo». The row uses the prose's shortening (l. 67–68). The «No obstante» exception sits in the next row. | — |
| 12 | tabla / IT por donación | art. 171 LGSS | PASS | Verbatim: «la prestación consistirá en un subsidio equivalente al cien por ciento de la base reguladora establecida para la prestación de incapacidad temporal derivada de contingencias comunes». In prose (l. 68–70). | — |
| 13 | tabla / Nacimiento y cuidado de menor | art. 179.1 LGSS | PASS | Verbatim: «consistirá en un subsidio equivalente al 100 por ciento de la base reguladora correspondiente». In prose (l. 104–105). | — |
| 14 | tabla / Riesgo durante el embarazo y la lactancia | arts. 187.3 y 189 LGSS | PASS | 187.3: «un subsidio equivalente al 100 por cien de la base reguladora correspondiente. A tales efectos, la base reguladora será equivalente a la que esté establecida para la prestación de incapacidad temporal derivada de contingencias profesionales»; 189 extends the embarazo terms to lactancia. Faithful. In prose (l. 111–112). | — |
| 15 | tabla / Cuidado de menores con cáncer | art. 192.1 LGSS | PASS | Verbatim: «un subsidio equivalente al 100 por ciento de la base reguladora establecida para la prestación de incapacidad temporal derivada de contingencias profesionales, y en proporción a la reducción que experimente la jornada de trabajo». In prose (l. 125–126). | — |
| 16 | tabla / Desempleo | art. 270.2 LGSS | PASS | «aplicando a la base reguladora los siguientes porcentajes: el 70 por ciento durante los ciento ochenta primeros días y el 60 por ciento a partir del día ciento ochenta y uno». In prose (l. 194–196). | — |

Placement: «Duración» follows 169.1 and 174.1 (l. 55–84); «Períodos mínimos» follows 172, 178.1, 205.1 and 215.2.a)
(l. 65–156); «Cuantía» follows 171, 179.1, 187.3/189, 192.1 and 270.2 (l. 67–196). All PASS. No `plazos` or `pasos`
esquema, so there is no order to check; no table claims a sequence.

## Notes

- m04-l07 row 5: the norm says the option is exercised «por el propio interesado». The prose does not say this, so
  the replacement leaves it out. Adding it would need a prose change first.
- m04-l07 row 9: art. 21.3 RDL 4/2000 caps the total («En ningún caso la suma resultante … podrá exceder del importe
  de las percepciones que el funcionario tuviera en el tercer mes de licencia»). This is a separate apartado, and the
  prose does not state it either. The row does not misstate 21.1.b). Not a FAIL.
- m04-l07 rows 3–4: the RDL lets the voluntary option cover párrafo c) (transferencia), which the baja row does not
  list («entre otros»). The prose names it (l. 66). Art. 10.5 RD 375/2003 removes the option for excedencia voluntaria
  caused by moving to another cuerpo of the AGE. Neither the cited article nor the prose has this, so the row is not
  wider than art. 8.2 RDL 4/2000.
- m04-l07 row 6 cites «art. 21.1 RDL 4/2000»; the prose cites «art. 21.1 RDL 4/2000, párrafo final». If the loader
  matches citations exactly, check that the shorter form passes.
- m04-l08 row 5 leaves out the cross-reference «de conformidad con lo dispuesto en el artículo 35» ET, which the prose
  keeps. Optional verbatim form: `… a la realización de las horas extraordinarias, de conformidad con lo dispuesto en el artículo 35 del ET`.
- m04-l08 horas extraordinarias table: there is an ET «compensación» row but no ET «límite» row (art. 35.2 ET: eighty
  a year). The prose does not state the ET limit, so the esquema correctly leaves it out.
- m04-l09 «Duración»: rows 1–2 repeat the art. 169.1 a)/b) list that the prose already gives as a list (l. 55–63).
  The spec's choice rule says such a list is not repeated as an esquema. The rows are correct; the choice is for the
  caller (the esquema could keep only what joins the 545-day extinction to the list, or be dropped).
- m04-l09 rows 6–8: art. 178.1 fixes the age at the date of the birth or decisión; for birth, 178.2 uses the age at
  the start of the descanso. The rows and the prose leave the reference date out, and they leave out «con
  anterioridad a esta última fecha» for the vida laboral alternative. Neither changes a number. Optional verbatim
  tail for rows 7–8: `… a lo largo de su vida laboral, con anterioridad a esta última fecha`.
- m04-l09 row 16: art. 270.3 sets maximum and minimum amounts (175/200/225 % and 107/80 % of the IPREM). This is a
  separate apartado, not in the prose. Not a FAIL.

## Counts

| Lesson | Rows | PASS | FAIL |
|---|---|---|---|
| m04-l07 | 11 | 10 | 1 (row 5) |
| m04-l08 | 7 | 7 | 0 |
| m04-l09 | 16 | 15 | 1 (row 10) |
| Total | 34 | 32 | 2 |
