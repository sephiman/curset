# Fix brief — `m03-l08`

## overview (draft.md, the OVERVIEW block) — FAIL

«su extensión por periodos de 60 días naturales (art. 150.4 LGT)»: 150.4 allows one or several periods that together cannot exceed 60 días naturales for the whole procedure, not periods of 60 days each. «que la inspección debe ratificar en 15 días (art. 146.3 LGT)»: 146.3 gives the ratification to the «órgano competente para liquidar», not to the inspección in general (the funcionarios who adopt the measure, RGAT 181.1). Minor: «las funciones y las facultades de la inspección (art. 141 LGT)»: 141 lists only the funciones; the facultades and the entrada en fincas are in art. 142.

## caso:### Actas#1

Current: En un acta de 2026 el obligado Sergio acepta unos hechos. Las actas son documentos públicos y hacen prueba de los hechos que motiven su formalización, salvo que se acredite lo contrario (art. 144 LGT). Los hechos aceptados por Sergio en el acta se presumen ciertos y solo pueden rectificarse mediante prueba de haber incurrido en error de hecho (art. 144 LGT).

Blind verifier: PASS — 144.1 and 144.2 LGT are quoted closely, with «salvo que se acredite lo contrario» and the error de hecho rule.
Student reader: REWRITE — Sergio 'accepts some facts' with no facts named; give one accepted and one contested fact so the 'error de hecho' versus 'prueba en contrario' difference shows.

## caso:### Personación en las empresas, oficinas y locales#1

Current: La inspección se persona sin previa comunicación en el almacén de Telas Ortega, S.L., y las actuaciones se entienden con el obligado o con el encargado o responsable de los locales (art. 151.2 LGT). Después requiere la comparecencia en las oficinas, sin que el requerimiento se haga en presencia del obligado: debe habilitar un plazo mínimo de 10 días, contados desde el día siguiente al de la notificación (art. 180.3 RGAT).

Blind verifier: FAIL — «Después requiere la comparecencia en las oficinas»: 180.3 RGAT sets the 10-day minimum only for «requerimientos de comparecencia en las oficinas de la Administración tributaria» not made in the obligado's presence. Right after the visit to Telas Ortega's almacén, «las oficinas» reads as the company's own offices. The reader would apply the 10-day minimum to any comparecencia. 151.2 part is correct.
Student reader: KEEP — Visit without notice, then a summons to the offices with the 10-day minimum when the obliged person is not present.

## caso:### Horario#1

Current: La inspección quiere actuar en los locales de Soto, S.L. fuera de su jornada laboral de oficina. Puede hacerlo con el consentimiento del obligado o, sin él, cuando se considera necesario para que no desaparezcan, se destruyan o alteren elementos de prueba (art. 182.2 RGAT). En ambos supuestos obtiene la previa autorización del órgano competente, que en la Agencia Estatal de Administración Tributaria es el delegado o el director de departamento del que dependa el órgano actuante (art. 182.2 RGAT).

Blind verifier: FAIL — «En ambos supuestos obtiene la previa autorización del órgano competente»: in 182.2.b «en ambos supuestos» refers to the two cases inside letter b (risk to pruebas / especial celeridad), both without consent. With the obligado's consent (182.2.a) no authorization is required. The case also gives letter b as the risk to pruebas only, dropping «o las circunstancias del caso requieran ... especial celeridad».
Student reader: KEEP — The two routes (consent, or risk to evidence) both needing prior authorisation are laid out clearly.

## caso:### Solicitud de una inspección de carácter general#1

Current: Isabel, objeto de actuaciones parciales, solicita el martes 15 de septiembre de 2026 que tengan carácter general, y la solicitud no interrumpe las actuaciones en curso (art. 149.1 LGT). La Administración debe ampliar el alcance o iniciar la inspección general en el plazo de seis meses desde la solicitud (art. 149.3 LGT), es decir, hasta el lunes 15 de marzo de 2027 (art. 30.4 LPAC).

Blind verifier: FAIL — The case leaves out the 149.2 condition: the solicitud must be made within 15 days from notification of the start of the partial actuaciones. Without that fact the duty «La Administración debe ampliar ... en el plazo de seis meses» does not follow. The date is right: Tuesday 15-09-2026 + 6 months = Monday 15-03-2027 (30.4 LPAC).
Student reader: KEEP — Dated six-month deadline and the point that the request does not stop current actions.

## caso:### Actas con acuerdo#1

Current: El lunes 5 de octubre de 2026 Pilar suscribe un acta con acuerdo: hacen falta autorización del órgano competente para liquidar y un depósito, aval o seguro de caución (art. 155.3 LGT). Si en 10 días hábiles desde el día siguiente no se notifica acuerdo que rectifique errores materiales, se entiende producida y notificada la liquidación según la propuesta (art. 155.5 LGT; art. 186.7 RGAT). Con el 12 de octubre festivo (art. 30.2 LPAC), es el martes 20 de octubre.

Blind verifier: FAIL — The 10 días hábiles from Tuesday 06-10-2026, skipping 12-10, do end on Tuesday 20-10-2026 (186.7 RGAT). But «se entiende producida y notificada la liquidación ... es el martes 20 de octubre» makes 20 October read as the notification date. 186.7 says that, if no rectification is notified within the plazo, the liquidación «se entenderá dictada y notificada el día siguiente», i.e. 21-10-2026. 155.3 requisitos are correct.
Student reader: KEEP — The business-day count skipping the 12 October holiday is a real calculation I can copy.

