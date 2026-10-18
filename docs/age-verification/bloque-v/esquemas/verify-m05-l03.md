# Verification — esquemas of m05-l03 (2026-10-18)

I am a blind reviewer: I wrote neither these esquemas nor the lesson. Scope: the three `:::esquema` blocks that
`git diff C/es/lessons/m05-l03.md` shows as added. The prose is unchanged. Rules: `spec.md` (this folder) and the
`::esquema` section of `docs/platform-delta-handoff.md`. Source: the scratchpad
`txt/BOE-A-2003-21614_lgp_2022-12-24.txt` (LGP consolidated 2022-12-24, `pdftotext -layout`). I read arts. 73, 74, 75,
140, 142, 148, 154, 155, 157, 162 and 164 with `art.py lgp`. I took no norm wording from memory. Line numbers are those
of the current lesson file.

## tabla «Fases del gasto del Estado hasta la ordenación del pago» (l. 150–157)

| # | row (short) | citation | PASS/FAIL | passage / reason | replacement |
|---|---|---|---|---|---|
| 1 | Aprobación del gasto: definition; Ministros… salvo Consejo de Ministros; Secretarios de Estado y Subsecretario below the limits | arts. 73.2 y 74.1 LGP | PASS | 73.2: «La aprobación es el acto mediante el cual se autoriza la realización de un gasto determinado por una cuantía cierta o aproximada, reservando a tal fin la totalidad o parte de un crédito presupuestario. La aprobación inicia el procedimiento de ejecución del gasto, sin que implique relaciones con terceros ajenos a la Hacienda Pública estatal o a la Seguridad Social.» The row is a verbatim shortening. Dropping «o a la Seguridad Social» fits the title's «del Estado». 74.1: «Corresponde a los Ministros y a los titulares de los demás órganos del Estado con dotaciones diferenciadas … aprobar y comprometer los gastos …, salvo los casos reservados por la Ley a la competencia del Consejo de Ministros … Asimismo, corresponderá a los Ministros, fijar los límites por debajo de los cuales las citadas competencias corresponderán, en su ámbito respectivo, a los Secretarios de Estado y Subsecretario del departamento.» The row keeps the salvo, and the limits clause is faithful. In prose at l. 49–52 and l. 24–29. | — |
| 2 | Compromiso de gasto: definition; «Los mismos órganos que aprueban el gasto» | arts. 73.3 y 74.1 LGP | PASS | 73.3: «…por un importe determinado o determinable. El compromiso es un acto con relevancia jurídica para con terceros, vinculando a la Hacienda Pública estatal o a la Seguridad Social a la realización del gasto a que se refiera en la cuantía y condiciones establecidas.» The row is a faithful shortening, the same as the prose at l. 56–59. Organ: 74.1 gives «aprobar y comprometer» one subject and one salvo, so «los mismos órganos» is exact, including the Consejo de Ministros cases. The cell is a cross-reference, not a verbatim fragment. Writing the organ out as in row 1 would be stricter, but it is not needed. In prose at l. 24–29. | — |
| 3 | Reconocimiento de la obligación: definition plus documentary proof; «Los mismos órganos que aprueban el gasto» | arts. 73.4 y 74.1 LGP | FAIL | (a) 73.4 párr. 2: «…previa acreditación documental ante el órgano competente de la realización de la prestación o el derecho del acreedor de conformidad con los acuerdos que en su día aprobaron y comprometieron el gasto.» The row drops the condition «de conformidad con los acuerdos…», which the prose keeps at l. 66–67 («conforme a los acuerdos que aprobaron y comprometieron el gasto»). (b) 74.1: «aprobar y comprometer los gastos …, salvo los casos reservados por la Ley a la competencia del Consejo de Ministros, así como reconocer las obligaciones económicas correspondientes». The salvo governs aprobar and comprometer only, and «reconocer» comes after it. Row 1 names the Consejo de Ministros as the organ that approves in the reserved cases. So «los mismos órganos que aprueban el gasto» also reads as «the Consejo de Ministros recognises the obligation in those cases», which 74.1 does not say. The row reads wider than the article. The prose (l. 24–29) states everything the replacement needs. | `\| Reconocimiento de la obligación \| El acto mediante el que se declara la existencia de un crédito exigible contra la Hacienda Pública estatal, derivado de un gasto aprobado y comprometido, y que comporta la propuesta de pago correspondiente; exige la acreditación documental previa ante el órgano competente de la realización de la prestación o el derecho del acreedor, conforme a los acuerdos que aprobaron y comprometieron el gasto \| Los Ministros y los titulares de los demás órganos del Estado con dotaciones diferenciadas; por debajo de los límites que fijen los Ministros, los Secretarios de Estado y Subsecretario del departamento \| arts. 73.4 y 74.1 LGP \|` |
| 4 | Ordenación del pago: «Qué es» = órdenes de pago a favor del acreedor / Orden del Ministro…; organ = Director General del Tesoro y Política Financiera | arts. 75.1 y 75.3 LGP | FAIL | 75.1: «Bajo la superior autoridad del Ministro de Economía, competen al Director General del Tesoro y Política Financiera las funciones de Ordenador General de pagos del Estado.» The organ cell is verbatim and correct. The «Qué es» cell fails. (a) The column header makes 75.3 read as a definition, but 75.3 regulates in whose favour the órdenes de pago are issued. The prose (l. 135–136) says explicitly that «La LGP no define la ordenación del pago». (b) 75.3: «…a favor de Habilitaciones, Cajas pagadoras o Depositarías de fondos, así como entidades colaboradoras de conformidad con la Ley 38/2003 … General de Subvenciones y otros agentes mediadores en el pago, que actuarán como intermediarias para su posterior entrega a los acreedores.» The row cuts the list to «Habilitaciones, Cajas pagadoras u otros agentes mediadores». It drops Depositarías de fondos and the entidades colaboradoras, and the shortened list still reads as the article's own list. It also drops the intermediary clause. The prose (l. 136–140) keeps all of these. | `\| Ordenación del pago \| La LGP no la define; la enumera como cuarta fase, entre el reconocimiento de la obligación y el pago material. Las órdenes de pago se expiden a favor del acreedor que figura en la propuesta de pago; por Orden del Ministro de Economía se pueden regular los supuestos en que se expiden a favor de Habilitaciones, Cajas pagadoras o Depositarías de fondos, entidades colaboradoras de la Ley General de Subvenciones y otros agentes mediadores en el pago, que actúan como intermediarios para su posterior entrega a los acreedores \| El Director General del Tesoro y Política Financiera, Ordenador General de pagos del Estado, bajo la superior autoridad del Ministro de Economía \| arts. 73.1.d), 75.1 y 75.3 LGP \|` (all of it is in the prose at l. 128–140, with these citations) |

## arbol «Control de la gestión económico-financiera del sector público estatal» (l. 226–233)

| # | node (short) | citation | PASS/FAIL | passage / reason | replacement |
|---|---|---|---|---|---|
| 1 | Control externo — Tribunal de Cuentas | art. 140 LGP | PASS | 140.1: «…corresponde al Tribunal de Cuentas el control externo del sector público estatal, en los términos establecidos en la Constitución, en su ley orgánica y en las demás leyes que regulen su competencia.» A verbatim shortening that keeps «en los términos…». In prose at l. 188–189. The citation matches the prose's «art. 140 LGP». | — |
| 2 | Control interno — IGAE, plena autonomía, three means | arts. 140 y 142.2 LGP | PASS | 140.2: «La IGAE ejercerá en los términos previstos en esta ley el control interno de la gestión económica y financiera del sector público estatal, con plena autonomía respecto de las autoridades y demás entidades cuya gestión controle.» 142.2: «El control se realizará mediante el ejercicio de la función interventora, el control financiero permanente y la auditoría pública». A faithful shortening. «En los términos previstos en esta ley», which the prose keeps at l. 190, is a reference to the LGP itself and not a limiting condition, so leaving it out does not widen the node. In prose at l. 189–193. | — |
| 3 | Función interventora — controla, antes de que sean aprobados… | art. 148 LGP | PASS | 148 párr. 1: «…controlar, antes de que sean aprobados, los actos del sector público estatal que den lugar al reconocimiento de derechos o a la realización de gastos, así como los ingresos y pagos que de ellos se deriven, y la inversión o aplicación en general de sus fondos públicos, con el fin de asegurar…». A verbatim shortening that drops the purpose clause. In prose at l. 205–208. See Notes on párr. 2. | — |
| 4 | Control financiero permanente — verifica de forma continua… | art. 157 LGP | PASS | 157: «…la verificación de una forma continua realizada a través de la correspondiente intervención delegada, de la situación y el funcionamiento de las entidades del sector público estatal en el aspecto económico-financiero, para comprobar…». A faithful shortening that keeps «a través de la intervención delegada». It is closer to the norm than the prose, which says «funcionamiento económico-financiero». Same fact, in prose at l. 195–196. | — |
| 5 | Auditoría pública — verificación posterior y sistemática | art. 162 LGP | PASS | 162: «la verificación, realizada con posterioridad y efectuada de forma sistemática, de la actividad económico-financiera del sector público estatal». A faithful shortening, the same as the prose at l. 196–197. | — |
| 6 | Modalidades — regularidad contable, cumplimiento, operativa (child of Auditoría pública) | art. 164.1 LGP | PASS | 164.1: «La auditoría pública adoptará las siguientes modalidades: a) La auditoría de regularidad contable … b) La auditoría de cumplimiento … c) La auditoría operativa». The list is complete. The citation names the apartado without a letter. In prose at l. 197–198. | — |

Nesting: the two roots are the two controls of art. 140 (1 and 2). The three children of «Control interno» are the three
means of art. 142.2, in its order. «Modalidades» sits under «Auditoría pública» as in art. 164.1. All PASS.

## pasos «Reparo y discrepancia» (l. 258–263)

| # | step (short) | citation | PASS/FAIL | passage / reason | replacement |
|---|---|---|---|---|---|
| 1 | Reparo — por escrito, con cita de preceptos; suspende la tramitación… — la Intervención | art. 154.1 LGP | PASS | 154.1: «Si la Intervención … se manifiesta en desacuerdo con el contenido de los actos examinados o con el procedimiento seguido para su adopción, deberá formular sus reparos por escrito, con cita de los preceptos legales en los que sustente su criterio. La formulación del reparo suspenderá la tramitación del expediente hasta que sea solventado, bien por la subsanación de las deficiencias observadas o bien, en el caso de no aceptación del reparo, por la resolución del procedimiento previsto en el artículo siguiente.» A faithful shortening, word for word the prose at l. 237–239. | — |
| 2 | Discrepancia, si el gestor no acepta — motivada, por escrito, ante la IGAE, por conducto de la Subsecretaría / presidentes o directores | art. 155 LGP | PASS | 155 párr. 1: «Cuando el órgano gestor no acepte el reparo formulado, planteará a la IGAE por conducto de la Subsecretaría del departamento, en caso de ministerios y a través de los presidentes o directores de los organismos o entidades en los demás casos, discrepancia motivada por escrito, con cita de los preceptos legales en los que sustente su criterio.» A faithful shortening, the same as the prose at l. 246–247. It drops «con cita de los preceptos legales», which narrows the step and does not widen it. The prose omits it too (see Notes). | — |
| 3 | Resolución, si el reparo es de una intervención delegada — IGAE, obligatoria; Defensa / Seguridad Social first, vinculante; then IGAE | art. 155 LGP | PASS | 155.a): «…corresponderá a la IGAE conocer la discrepancia, siendo su resolución obligatoria para aquélla. No obstante lo anterior, cuando el reparo haya sido formulado por una intervención Delegada en … Ministerio de Defensa, o en las entidades gestoras y servicios comunes de la Seguridad Social, corresponderá conocer … a la Intervención General de la Defensa y a la Intervención General de la Seguridad Social, respectivamente, haciendo constar su criterio que será vinculante para aquélla. Cuando … éstas hayan confirmado el de una intervención delegada, subsistiendo la discrepancia, corresponderá a la IGAE resolver…». The step keeps the «No obstante» exception and the «si subsiste» condition. In prose at l. 248–251. The citation leaves out the letter, as the spec asks for list-type rows. | — |
| 4 | Resolución definitiva, si el reparo es de la IGAE o esta confirmó el de otra Intervención, y la discrepancia subsiste — Consejo de Ministros | art. 155 LGP | PASS | 155.b): «Cuando el reparo haya sido formulado por la IGAE o este centro directivo haya confirmado el de otra Intervención General o delegada, subsistiendo la discrepancia, corresponderá al Consejo de Ministros adoptar resolución definitiva.» A faithful shortening, the same as the prose at l. 251–253. | — |

## Order

- tabla: makes no claim of order. Its four rows are the first four letters of art. 73.1, in the norm's order. The title
  «hasta la ordenación del pago» marks pago material as left out, so the table does not read as complete. PASS.
- arbol: makes no claim of order. Nesting PASS (see above).
- pasos: 1 → 2 is supported. Art. 154.1 says the reparo suspends «hasta que sea solventado … en el caso de no
  aceptación del reparo, por la resolución del procedimiento previsto en el artículo siguiente», and art. 155 starts
  «Cuando el órgano gestor no acepte el reparo». 2 → 3 is supported by «Planteada la discrepancia se procederá de la
  siguiente forma: a)…». 3 → 4 is supported for the delegada path: 155.b) covers the case where the IGAE «haya
  confirmado el de otra Intervención General o delegada, subsistiendo la discrepancia», which is the outcome of step 3.
  When the reparo is the IGAE's own, the path is 1 → 2 → 4 and step 3 does not apply. Each conditional step carries its
  «si…» in the label, so the stepper does not claim that step 3 always comes before step 4. No false order. PASS.

## Placement

- tabla (l. 150): follows every paragraph it summarises: the órganos at l. 24–29, the phases at l. 47–67, and the
  ordenación del pago at l. 126–148. It sits at the end of the ordenación section, before «Realización del pago». PASS.
- arbol (l. 226): follows the paragraphs it summarises: «Clases» at l. 188–198 and the definition of the función
  interventora at l. 205–208. PASS. It sits inside «Especial referencia al control de legalidad / La función
  interventora», after the fiscalización paragraphs (l. 209–224) that it does not summarise. Moving it to l. 199 would
  put it ahead of l. 205–208 and break the rule, so the current spot is the right one.
- pasos (l. 258): follows «Reparos» (l. 237–242) and «Discrepancias y omisión» (l. 246–256). PASS.

## Notes

- None of the three esquemas repeats a list or table that already exists in the prose. The prose table at l. 83–92
  covers documentos contables, not phases or organs. The art. 150.2 list at l. 212–216 is not reproduced.
- tabla row 2: the «Los mismos órganos que aprueban el gasto» cross-reference is accurate for comprometer, as explained
  in the row. Row 3 fails because the same words are wrong for reconocer.
- arbol node 3: art. 148 párr. 2 («No obstante, la fiscalización previa e intervención de los derechos e ingresos del
  Tesoro Público se podrá sustituir reglamentariamente por las comprobaciones … del control financiero permanente y la
  auditoría pública, salvo en los actos de ordenación del pago y pago material correspondientes a devoluciones de
  ingresos indebidos») is absent from both the node and the prose at l. 205–208. It is a power to substitute by
  regulation, not a limit on what párr. 1 defines, so I did not fail the node. The writer may list it as a possible
  prose gap.
- pasos step 2 and the prose at l. 246 both leave out «con cita de los preceptos legales en los que sustente su
  criterio» (art. 155 párr. 1). This narrows the step and does not widen it, so it is not a FAIL. It could be added to
  both together.
- pasos step 4 reads «Resolución definitiva … — resolución definitiva — el Consejo de Ministros». The label and the
  fact field are the same words. This is cosmetic, not a FAIL.
- The tabla cites the Ministro de Economía as art. 75 says. The prose (l. 128) adds the current department
  (RD 1009/2023). The row does not need that note, because the 75.1 wording is quoted as the norm's.

## Counts

14 rows: 12 PASS, 2 FAIL (tabla row 3, tabla row 4). Order: PASS. Placement: PASS.
