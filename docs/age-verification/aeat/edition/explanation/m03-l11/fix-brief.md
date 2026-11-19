# Fix brief — `m03-l11`

## caso:### Medidas cautelares#1

Current: Hay indicios racionales de que el cobro de una deuda de Ramiro se vería frustrado o gravemente dificultado. El martes 2 de febrero de 2027 se le notifica una prohibición de enajenar bienes (art. 81.1 y 81.4.c LGT). Sus efectos cesan en el plazo de seis meses desde su adopción, el lunes 2 de agosto de 2027 (art. 81.7 LGT; art. 30.4 LPAC), salvo que se amplíe mediante acuerdo motivado, sin exceder de seis meses (art. 81.7.d LGT).

Blind verifier: FAIL — «Sus efectos cesan en el plazo de seis meses desde su adopción ... salvo que se amplíe mediante acuerdo motivado» gives ampliación as the only exception. 81.7 lists five (a–e): conversion into embargos, the circumstances disappearing, substitution by another garantía, ampliación, and adoption in the art. 253 procedure (24 months). The case also counts the 6 months from the notification date («se le notifica» on 02-02-2027), but 81.7 counts from adoption, which the case never dates. The arithmetic is right: 02-02-2027 + 6 months = Monday 02-08-2027.
Student reader: KEEP — Dated six-month life of the prohibition to dispose with the extension rule; the last clause is a little compressed but readable.

## caso:### Iniciación del período ejecutivo#1

Current: El plazo para ingresar una liquidación de Sara vence el viernes 20 de noviembre de 2026. El período ejecutivo de las deudas liquidadas por la Administración se inicia el día siguiente al vencimiento (art. 161.1.a LGT): el sábado 21 de noviembre. Sara presentó el martes 10 de noviembre una solicitud de aplazamiento en período voluntario, y esa solicitud impide el inicio del período ejecutivo durante la tramitación (art. 161.2 LGT).

Blind verifier: PASS — Vencimiento on Friday 20-11-2026 → período ejecutivo would start on Saturday 21-11 (161.1.a). The aplazamiento filed in voluntary period on Tuesday 10-11 prevents that during tramitación (161.2). Minor: the case does not state that no earlier request was denied (161.2 párr. 2).
Student reader: REWRITE — It says enforcement starts on 21 November and then that the request prevents it; say that 21 November would be the start and that the request stops it.

