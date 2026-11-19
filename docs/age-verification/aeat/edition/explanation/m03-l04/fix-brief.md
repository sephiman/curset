# Fix brief — `m03-l04`

## caso:### Declaraciones censales#1

Current: Ramón, empresario, fallece el martes 3 de noviembre de 2026. Sus herederos presentan la declaración de baja en el Censo de Empresarios, Profesionales y Retenedores en el plazo de seis meses desde el fallecimiento, hasta el lunes 3 de mayo de 2027 (art. 11.4 RGAT; art. 30.4 LPAC). En ese mismo plazo comunican la modificación de la titularidad de los derechos y obligaciones vigentes con terceros (art. 11.4 RGAT).

Blind verifier: FAIL — Dates are correct: Tue 3 Nov 2026 + 6 months = Mon 3 May 2027 under art. 30.4 LPAC. But «comunican la modificación de la titularidad de los derechos y obligaciones vigentes con terceros» drops art. 11.4's limiter «con trascendencia tributaria», which widens the duty to all rights and obligations.
Student reader: KEEP — The six-month deadline from death is computed to a date.

## caso:### Número de identificación fiscal#1

Current: Elena, española residente en Lisboa y sin documento nacional de identidad, y Mateo, español de 13 años residente en Madrid, deben obtener un número de identificación fiscal propio (art. 19.2 RGAT). Lo solicitan a la Administración tributaria: nueve caracteres, con la letra inicial L para Elena y la K para Mateo (art. 19.2 RGAT).

Blind verifier: FAIL — «deben obtener un número de identificación fiscal propio (art. 19.2 RGAT)» drops the condition that triggers the duty: Spaniards «que realicen o participen en operaciones de naturaleza o con trascendencia tributaria». The case also omits the article's alternative of applying for the DNI voluntarily. The letters L and K are correct.
Student reader: REWRITE — The letters L and K appear without saying why each person gets that letter, so I cannot reuse it; state the rule for each.

## caso:### Libros registro#1

Current: Daniel, fisioterapeuta, determina su rendimiento en estimación directa simplificada. Lleva los libros registro de ingresos, de gastos, de bienes de inversión y de provisiones de fondos y suplidos (art. 68.5 RIRPF). Alba, empresaria cuya actividad no tiene carácter mercantil, limita sus obligaciones contables a los libros de ventas e ingresos, de compras y gastos y de bienes de inversión (art. 68.3 RIRPF).

Blind verifier: FAIL — Daniel is correct (art. 68.5, any modality of estimación directa). For Alba, art. 68.3 is an exception to apartado 2 (modalidad normal de estimación directa); 68.4 extends it to the simplified modality. The case never states that Alba is in estimación directa, and in estimación objetiva (68.6/68.7) the books differ, so a condition that changes the result is missing.
Student reader: KEEP — Two taxpayers, two sets of books; the contrast is easy to follow.

## caso:## Obligaciones y deberes de la Administración tributaria#1

Current: Iker realiza un ingreso indebido el martes 10 de febrero de 2026. La Administración ordena el pago de su devolución el lunes 20 de julio de 2026. Con la devolución abona el interés de demora del artículo 26 sin necesidad de que Iker lo solicite (art. 32.2 LGT). Lo devenga desde el 10 de febrero hasta el 20 de julio (art. 32.2 LGT).

Blind verifier: FAIL — The dates are correct (Tue 10 Feb, Mon 20 Jul 2026). But «Lo devenga desde el 10 de febrero hasta el 20 de julio» omits art. 32.2's second paragraph: «no se computarán las dilaciones en el procedimiento por causa no imputable a la Administración». That condition can shorten the period, and the case does not rule it out.
Student reader: KEEP — Interest runs from payment date to refund order date, with the dates given.

## caso:### Obligados en las obligaciones entre particulares#1

Current: Un comerciante, sujeto pasivo, vende a Luis, destinatario de la operación gravada, y repercute una cuota de 210 euros. Luis es el obligado a soportar la repercusión (art. 38.2 LGT). No está obligado al pago frente a la Administración tributaria, pero debe satisfacer al sujeto pasivo los 210 euros de cuota repercutida (art. 38.2 LGT).

Blind verifier: FAIL — «Luis, destinatario de la operación gravada ... Luis es el obligado a soportar la repercusión» drops art. 38.2's «salvo que la ley disponga otra cosa». Under the article, being the destinatario makes someone the repercutido only by default. The second sentence is correct.
Student reader: KEEP — Shows who pays whom in repercusión.

## caso:### Sucesores#1

Current: Marcos fallece el martes 3 de noviembre de 2026 con una deuda tributaria pendiente de 5.000 euros y una sanción de 600 euros. Las obligaciones tributarias pendientes se transmiten a sus herederos (art. 39.1 LGT). En ningún caso se transmiten las sanciones (art. 39.1 LGT). Los 5.000 euros pasan a sus herederos.

Blind verifier: FAIL — «Las obligaciones tributarias pendientes se transmiten a sus herederos ... Los 5.000 euros pasan a sus herederos» drops art. 39.1's «sin perjuicio de lo que establece la legislación civil en cuanto a la adquisición de la herencia», a condition that changes the result (e.g. if the heirs do not accept). The non-transmission of the sanción is correct, and 3 Nov 2026 is a Tuesday.
Student reader: KEEP — The debt passes to the heirs and the sanción does not; amounts make it clear.

## caso:### Responsables#1

Current: Una ley configura a Nora como responsable de la deuda de una sociedad y no dice si lo es solidaria o subsidiariamente. Salvo precepto legal expreso en contrario, la responsabilidad es siempre subsidiaria (art. 41.2 LGT). Derivarle la deuda requiere la previa declaración de fallido del deudor principal y de los responsables solidarios (art. 41.5 LGT).

Blind verifier: FAIL — Art. 41.2 is applied correctly. But «Derivarle la deuda requiere la previa declaración de fallido» gives only the subsidiary-specific requirement. Art. 41.5 also requires, «salvo que una norma con rango de ley disponga otra cosa», an administrative act that, previa audiencia, declares the responsibility and fixes its scope. The reader is left thinking fallido is enough.
Student reader: KEEP — Default subsidiary liability and the fallido requirement are applied well.

## caso:## La capacidad de obrar en el orden tributario#1

Current: Noa, menor de edad, ejerce una actividad que el ordenamiento jurídico le permite sin asistencia de la persona que ejerza la patria potestad, tutela, curatela o defensa judicial. Tiene capacidad de obrar en las relaciones tributarias derivadas de esa actividad (art. 44 LGT). Si además estuviera incapacitada y la incapacitación afectara al ejercicio y defensa de esos derechos e intereses, se exceptuaría (art. 44 LGT).

Blind verifier: PASS — Art. 44: the permitted-activity condition and the exception for menores incapacitados are both kept.
Student reader: REWRITE — The last sentence ("si estuviera incapacitada... se exceptuaría") is a hypothetical that is hard to parse; say plainly what is excepted.

## caso:### Representación legal#1

Current: El administrador único de una sociedad cesó el 28 de febrero de 2027 y Elena ocupa el cargo desde el 1 de marzo. El miércoles 10 de marzo de 2027 se produce una actuación tributaria. Por la sociedad actúa Elena, que ostenta la titularidad del órgano en el momento en que se produce la actuación (art. 45.2 LGT). Por una comunidad de bienes actúa quien la represente, si su representación resulta acreditada en forma fehaciente (art. 45.3 LGT).

Blind verifier: PASS — Art. 45.2: titular of the organ at the time of the actuación (Wed 10 Mar 2027, checked). Art. 45.3 is stated with its «acreditada en forma fehaciente» condition.
Student reader: REWRITE — The comunidad de bienes sentence is a second unrelated situation tacked on the end; split it or drop it.

## caso:## Domicilio fiscal#1

Current: La base imponible general del IRPF de Sergio en 2026 es de 50.000 euros y 30.000 proceden de rendimientos netos de actividades económicas. Es más de la mitad: desarrolla principalmente actividades económicas (art. 113 RGAT). La Administración puede considerar su domicilio fiscal el lugar donde esté centralizada la gestión administrativa y la dirección de esas actividades, no su residencia habitual (art. 48.2.a) LGT).

Blind verifier: FAIL — «Es más de la mitad: desarrolla principalmente actividades económicas (art. 113 RGAT)» turns art. 113's «se podrá considerar» into a certainty. It also omits that the test uses the IRPF base «del año anterior» (2026 data serve the following year) and the three-year alternative. The art. 48.2.a) sentence correctly keeps «puede».
Student reader: KEEP — The more-than-half test with numbers decides the domicilio.

## caso:## Plazos de prescripción#1

Current: Ana generó bases negativas en 2021. El plazo para presentar su declaración terminó el jueves 30 de junio de 2022. El derecho de la Administración a iniciar su comprobación prescribe a los diez años a contar desde el día siguiente, el 1 de julio de 2022 (art. 66 bis.2 LGT). El martes 15 de septiembre de 2026 no ha prescrito. El derecho a liquidar la deuda, en cambio, prescribe a los cuatro años (art. 66 LGT).

Blind verifier: FAIL — The dates are correct (Thu 30 Jun 2022; ten years from 1 Jul 2022; Tue 15 Sep 2026 is not prescribed). But the case contrasts the 10-year right with «El derecho a liquidar la deuda, en cambio, prescribe a los cuatro años» without art. 66 bis.2's limiting condition: the comprobación and any correction «sólo podrá realizarse en el curso de procedimientos de comprobación relativos a obligaciones tributarias y periodos cuyo derecho a liquidar no se encuentre prescrito». That leaves the reader with too wide a rule.
Student reader: KEEP — Ten-year versus four-year periods with a start date.

## caso:### Cómputo#1

Current: El plazo de pago en período voluntario del deudor principal terminó el lunes 20 de abril de 2026. El plazo para exigir el pago a un responsable solidario empieza el martes 21 de abril de 2026 (art. 67.2 LGT). La última actuación recaudatoria al deudor principal se le notificó el lunes 4 de mayo de 2026: ese día empieza el plazo para un responsable subsidiario (art. 67.2 LGT).

Blind verifier: FAIL — The dates are correct (Mon 20 Apr → Tue 21 Apr; Mon 4 May 2026). But the solidario step omits art. 67.2's «No obstante» (if the facts giving rise to the responsibility occur later, the plazo starts then). The subsidiario step says «La última actuación recaudatoria al deudor principal», whereas 67.2 counts the last one «practicada al deudor principal o a cualquiera de los responsables solidarios». Both conditions change the start date.
Student reader: KEEP — Distinguishes the start for solidario and subsidiario with dates.

## caso:### Interrupción#1

Current: Pedro y Marta están obligados al pago de la deuda A. El lunes 4 de mayo de 2026 la Administración realiza, con conocimiento formal de Pedro, una acción dirigida de forma efectiva a su recaudación (art. 68.2 LGT). La interrupción se extiende a Marta (art. 68.8 LGT). Pedro tiene además una deuda B liquidada: la interrupción solo afecta a la deuda a la que se refiera (art. 68.8 LGT).

Blind verifier: FAIL — Art. 68.2.a) applies on Mon 4 May 2026, and the deuda B point is correct. But «La interrupción se extiende a Marta (art. 68.8 LGT)» drops the article's own exception: «si la obligación es mancomunada y solo se reclama a uno de los obligados tributarios la parte que le corresponde, el plazo no se interrumpe para los demás». The case does not say the obligation is solidaria.
Student reader: REWRITE — The debt B sentence is unexplained (what act, what outcome); say which debts are or are not interrupted.

