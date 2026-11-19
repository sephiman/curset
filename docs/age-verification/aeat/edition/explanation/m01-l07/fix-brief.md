# Fix brief — `m01-l07`

## caso:### La regla de las plazas vacantes#1

Current: Óscar es nombrado interino en una plaza vacante el lunes 1 de marzo de 2027. Transcurridos tres años desde el nombramiento se produce el fin de la relación de interinidad; el lunes 4 de marzo de 2030 ya han transcurrido (art. 10.4 TREBEP). Si la convocatoria se publicó dentro de esos tres años y se resuelve conforme a los plazos del artículo 70, Óscar permanece hasta su resolución, sin compensación económica por el cese (art. 10.4 TREBEP).

Blind verifier: FAIL — Dates fine (01-03-2027 Monday; three years end 01-03-2030, so by Monday 04-03-2030 they have elapsed), but «Óscar permanece hasta su resolución» turns art. 10.4's «Excepcionalmente, el personal funcionario interino podrá permanecer [...] podrá permanecer hasta la resolución de la convocatoria» into an automatic effect; the article's modal is dropped.
Student reader: REWRITE — "El lunes 4 de marzo de 2030 ya han transcurrido" is confusing; state that the three years end on 1 March 2030 and give the two outcomes.

## caso:## Acceso de las personas con discapacidad#1

Current: Una comunidad autónoma convoca una oferta de empleo público con 300 plazas. Se reserva un cupo no inferior al siete por ciento de las vacantes para personas con discapacidad que superen los procesos selectivos y acrediten su discapacidad y la compatibilidad con las tareas: al menos 21 plazas (art. 59.1 TREBEP). Al menos el dos por ciento de las plazas ofertadas es para personas que acrediten discapacidad intelectual: al menos 6 plazas (art. 59.1 TREBEP).

Blind verifier: FAIL — Figures correct (7 % of 300 = 21; 2 % = 6), but the case omits the source the article names for who counts as a person with disability: «las definidas en el apartado 2 del artículo 4 del texto refundido [...] Real Decreto Legislativo 1/2013» (59.1).
Student reader: KEEP — 7% and 2% of 300 give 21 and 6 plazas, a clear calculation.

## caso:### Derechos#1

Current: Un sindicato convoca una huelga en un servicio de una Administración. Entre los derechos individuales de los empleados públicos figuran el de percibir las retribuciones y las indemnizaciones por razón del servicio y el de las vacaciones, descansos, permisos y licencias (art. 14 TREBEP). La huelga no figura entre ellos. Se ejerce colectivamente, con mantenimiento de los servicios esenciales (art. 15 TREBEP).

Blind verifier: FAIL — «Entre los derechos individuales [...] La huelga no figura entre ellos. Se ejerce colectivamente» leaves the wrong rule that the strike is not an individual right; art. 15 lists it among «derechos individuales que se ejercen de forma colectiva», with «la garantía del mantenimiento de los servicios esenciales de la comunidad».
Student reader: REWRITE — It is a rule restatement about the strike, with no facts; say who may strike and what must stay running.

## caso:### Toma de posesión y cese#1

Current: Elena cesa el viernes 12 de febrero de 2027 en su puesto, tras obtener otro por concurso. En ese período no hay festivos. Sin cambio de residencia, toma posesión en tres días hábiles a partir del día siguiente al del cese: hasta el miércoles 17 de febrero (art. 48 RD 364/1995; art. 30.2 LPAC). Con cambio de residencia dispondría de un mes, hasta el viernes 12 de marzo de 2027 (art. 48 RD 364/1995; art. 30.4 LPAC).

Blind verifier: FAIL — Dates correct (cese Friday 12-02-2027; three working days → Wednesday 17-02; one month → Friday 12-03-2027), but a condition of the same article that changes the result is missing: «El cómputo de los plazos posesorios se iniciará cuando finalicen los permisos o licencias que hayan sido concedidos» (48.3), and with change of residence a prórroga of up to twenty working days may be granted (48.2). The case should fix that Elena has no pending permisos/licencias (and no prórroga) for the end dates to hold.
Student reader: KEEP — The same cese gives two dates (17 Feb or 12 Mar) depending on change of residence.

## caso:### Excedencia voluntaria por interés particular#1

Current: Hugo ha prestado servicios efectivos en una Administración Pública durante los seis años inmediatamente anteriores y pide la excedencia voluntaria por interés particular. Esta exige un periodo mínimo de cinco años de servicios efectivos inmediatamente anteriores (art. 89.2 TREBEP). Su concesión queda subordinada a las necesidades del servicio debidamente motivadas (art. 89.2 TREBEP). En ella no devengará retribuciones ni se le computará el tiempo a efectos de ascensos, trienios y derechos de Seguridad Social (art. 89.2 TREBEP).

Blind verifier: FAIL — Drops a bar that changes the result: «No podrá declararse cuando al funcionario público se le instruya expediente disciplinario» (89.2); the case gives no fact on this. Also «Esta exige un periodo mínimo de cinco años» omits that leyes de Función Pública «podrán establecer una duración menor».
Student reader: KEEP — Six years against the five-year minimum, plus the loss of pay and seniority.

## caso:### Excedencia por cuidado de familiares#1

Current: Lucía, funcionaria, pide excedencia por el cuidado de su hija, nacida el lunes 14 de junio de 2027. La excedencia no es superior a tres años por cada hijo desde el nacimiento; el lunes 17 de junio de 2030 ya superaría ese límite (art. 89.4 TREBEP). El puesto se reserva al menos dos años (art. 89.4 TREBEP). El tiempo en esta situación computa a efectos de trienios, carrera y derechos de Seguridad Social (art. 89.4 TREBEP).

Blind verifier: PASS — 14-06-2027 is Monday; three years from birth end 14-06-2030 (Friday), so Monday 17-06-2030 exceeds it; reserve «al menos, durante dos años» and computation for trienios, carrera and Seguridad Social per 89.4.
Student reader: REWRITE — The limit date should be 14 June 2030, three years from birth; the 17 June date makes the reader doubt the count.

## caso:### Actividades públicas#1

Current: Teresa, del grupo A, funcionaria del Estado, tiene un segundo puesto público compatible. Su puesto principal se retribuye con 50.000 euros anuales y el cargo de Director General con 90.000. El total de ambos no puede superar esa cifra ni la del principal más un 30 por 100 para el grupo A: 65.000 euros (art. 7.1 Ley 53/1984). Un total de 70.000 euros exige acuerdo expreso del Gobierno por razones de especial interés para el servicio (art. 7.1 Ley 53/1984).

Blind verifier: FAIL — Not verifiable: the input has no text for art. 7 Ley 53/1984 («[encabezado del artículo 7 no localizado en la página 7]»). The case's limits (Director General remuneration, principal + 30 % for group A, «acuerdo expreso del Gobierno» for exceeding them) cannot be checked against cited text; extraction defect to fix and re-verify.
Student reader: REWRITE — "Esa cifra" is unclear and 140,000 is never compared with 65,000; the 70,000 total contradicts the stated salaries. Redo the figures.

## caso:### Actividades privadas#1

Current: Javier, funcionario, quiere ejercer una actividad mercantil fuera de las Administraciones Públicas desde el martes 1 de junio de 2027. Necesita el previo reconocimiento de compatibilidad, que se resuelve de forma motivada en el plazo de dos meses (art. 14 Ley 53/1984). El reconocimiento no puede modificar la jornada de trabajo y horario (art. 14 Ley 53/1984). Si Javier cambia de puesto en el sector público, queda automáticamente sin efecto (art. 14 Ley 53/1984).

Blind verifier: FAIL — Not verifiable: the input has no text for art. 14 Ley 53/1984 («[encabezado del artículo 14 no localizado en la página 9]»); the prior recognition, two-month motivated resolution, no change of jornada/horario and automatic lapse on change of post cannot be checked; extraction defect to fix and re-verify.
Student reader: KEEP — Prior recognition, the two-month term and the automatic loss of effect on changing post are all applied.

## caso:### Instrucción#1

Current: Se incoa el procedimiento disciplinario contra Sergio el lunes 8 de marzo de 2027. El Instructor formula el pliego de cargos en un plazo no superior a un mes desde la incoación, hasta el jueves 8 de abril de 2027 (art. 35.1 RD 33/1986; art. 30.4 LPAC). Por causas justificadas puede solicitar la ampliación del plazo (art. 35.1 RD 33/1986). El pliego comprende los hechos imputados, con la falta presuntamente cometida y las sanciones aplicables (art. 35.1 RD 33/1986).

Blind verifier: FAIL — Date correct (Monday 08-03-2027 → Thursday 08-04-2027), but «El pliego comprende los hechos imputados, con la falta presuntamente cometida y las sanciones aplicables» drops the article's «con expresión, en su caso, de la falta» and its named source «de acuerdo con lo previsto en el artículo 14 del presente Reglamento» (35.1 RD 33/1986).
Student reader: KEEP — The one-month pliego de cargos deadline (to 8 Apr) is clear and correct.

