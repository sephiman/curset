# Fix brief — `m03-l05`

## caso:### Acuerdos previos de valoración#1

Current: Lucas solicita el miércoles 3 de marzo de 2027, antes de realizar el hecho imponible, un acuerdo previo de valoración que la ley de su tributo prevé, y propone un valor de 90.000 euros (art. 91.1 LGT; art. 91.2 LGT). La normativa del tributo fija un plazo de contestación que vence el viernes 28 de mayo de 2027. La Administración no contesta en plazo y esa falta de contestación implica la aceptación de los valores propuestos (art. 91.4 LGT).

Blind verifier: FAIL — «solicita ... un acuerdo previo de valoración»: art. 91.2 says «La solicitud deberá presentarse por escrito»; the case cites 91.2 but drops the written-form requirement, on which the silence-acceptance result depends. Dates (Wed 3 Mar, Fri 28 May 2027) and the acceptance rule of 91.4 are otherwise right.
Student reader: KEEP — Makes the silence-means-acceptance effect concrete with a deadline date, which is the point the warning box contrasts.

## caso:### Efectos de la falta de resolución expresa#1

Current: Pablo recibe el martes 2 de marzo de 2027 la notificación del acuerdo de inicio de un procedimiento de oficio susceptible de producir efectos desfavorables; su normativa no regula la falta de resolución. El plazo de seis meses vence el jueves 2 de septiembre de 2027 sin resolución expresa (art. 104.1 LGT; art. 30.4 LPAC). Se produce la caducidad (art. 104.4 LGT), que se declara de oficio o a instancia de Pablo, con archivo de las actuaciones (art. 104.5 LGT).

Blind verifier: FAIL — «El plazo de seis meses vence ... (art. 104.1 LGT)»: the case only says the normativa «no regula la falta de resolución», not that it fixes no plazo máximo; under 104.1 the plazo is the one fixed by the procedure's normativa and six months applies only «Cuando las normas reguladoras de los procedimientos no fijen plazo máximo». The condition is missing, so the reader may take six months as the rule for every oficio procedure. Dates (Tue 2 Mar → Thu 2 Sep 2027) and the caducidad steps (104.4.b, 104.5) are right.
Student reader: KEEP — Walks an ex officio, unfavourable procedure to caducidad, the one outcome I could not guess from the long section.

