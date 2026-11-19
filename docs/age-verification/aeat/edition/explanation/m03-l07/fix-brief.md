# Fix brief — `m03-l07`

## caso:### Iniciación#1

Current: El plazo para presentar la autoliquidación de Marta terminó el miércoles 30 de junio de 2027. Marta presenta el lunes 12 de julio de 2027 una autoliquidación extemporánea con resultado a devolver. El plazo para efectuar la devolución se cuenta desde esa presentación, el 12 de julio de 2027 (art. 125.2 LGT). Si la hubiera presentado en plazo, se contaría desde el 30 de junio de 2027 (art. 125.2 LGT).

Blind verifier: FAIL — Dates (Wed 30 Jun, Mon 12 Jul 2027) and both branches of art. 125.2 are right, but «El plazo para efectuar la devolución» does not name the source art. 125.2 gives for that plazo: «el plazo al que se refiere el artículo 31 de esta ley para devolver». Source omission only.
Student reader: KEEP — Late versus on-time filing and the day the refund clock starts are shown with dates.

## caso:### Tramitación y terminación#1

Current: El miércoles 6 de octubre de 2027 se notifica a Irene el inicio de un procedimiento de verificación de datos sobre su autoliquidación del IRPF, con 300 euros a devolver. Con ese inicio termina el procedimiento de devolución (art. 127 LGT). Si finalmente se practica una devolución de 120 euros, se mantiene la obligación de satisfacer el interés de demora sobre ella (art. 127 LGT).

Blind verifier: FAIL — Termination by the inicio of a verificación de datos is right (art. 127; Wed 6 Oct 2027 correct), but «se mantiene la obligación de satisfacer el interés de demora sobre ella» drops «de acuerdo con lo dispuesto en el artículo 31 de esta ley», the source and limit of that interest; the case reads as interest always owed on the 120 euros.
Student reader: KEEP — Shows the refund procedure ending when verification starts, with interest still owed on what is finally paid.

## caso:### Ejecución de las devoluciones#1

Current: El martes 8 de junio de 2027 se reconoce a Berta una devolución de 400 euros derivada de la normativa del tributo, sin garantías solicitadas, y se procede a ejecutarla (art. 131.1 RGAT). Berta cede ese derecho a Carlos mediante un contrato privado. La transmisión entre particulares no surte efectos ante la Administración (art. 131.5 RGAT), salvo la transmisión a sucesores (art. 131.4 RGAT).

Blind verifier: FAIL — Execution under RGAT 131.1 (no garantías) and Tue 8 Jun 2027 are right, but «La transmisión entre particulares no surte efectos ante la Administración (art. 131.5 RGAT)» omits the source the article names («conforme a lo dispuesto en el artículo 17.4 de la Ley 58/2003»), and «salvo la transmisión a sucesores (art. 131.4 RGAT)» omits that for sucesores «se atenderá a la normativa específica que determine los titulares del derecho y la cuantía».
Student reader: KEEP — A private assignment to Carlos having no effect against the Administration, except for successors, is clear.

## caso:### Tramitación#1

Current: Talleres Norte, S.L., presenta en plazo el jueves 16 de julio de 2026 una declaración cuyo plazo de presentación termina el lunes 20 de julio de 2026; la normativa del tributo no señala otro plazo para notificar la liquidación. Los seis meses se cuentan desde el día siguiente a la finalización del plazo de presentación, el 21 de julio de 2026 (art. 129.1 LGT), y concluyen el miércoles 20 de enero de 2027 (art. 30.4 LPAC).

Blind verifier: PASS — Declaración presented in time; normativa del tributo sets no other plazo; art. 129.1: six months from the day after the end of the presentation plazo (Mon 20 Jul 2026 → from 21 Jul), ending Wed 20 Jan 2027 under 30.4 LPAC. Weekdays correct.
Student reader: REWRITE — It counts from 21 July yet ends on 20 January with no explanation; say the six months run from the end of the filing period (art. 30.4 LPAC date-to-date).

## caso:### Efectos de la regularización#1

Current: Dictada el lunes 8 de noviembre de 2027 la resolución de una comprobación limitada, la Administración no puede efectuar una nueva regularización sobre el objeto comprobado, salvo que en una comprobación limitada o inspección posterior descubra hechos o circunstancias nuevos que resulten de actuaciones distintas (art. 140.1 LGT). Hugo prestó conformidad expresa a un elemento de la deuda: solo puede impugnarlo si prueba error de hecho (art. 140.2 LGT).

Blind verifier: PASS — Art. 140.1: no new regularisation of the objeto comprobado unless a later comprobación limitada or inspección discovers new facts from actuaciones distintas; 140.2: conformidad expresa → challengeable only proving error de hecho. Mon 8 Nov 2027 correct.
Student reader: REWRITE — It packs two rules and the second (Hugo's express conformity) has no facts; split them or give Hugo a concrete element and a challenge.

