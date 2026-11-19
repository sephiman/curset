# Fix brief — `m02-l02`

## caso:### Inderogabilidad singular#1

Current: El lunes 5 de octubre de 2026 se aprueba un reglamento que exige un requisito para una ayuda. El lunes 9 de noviembre un órgano de rango superior al que lo dictó resuelve un caso sin exigir ese requisito. Las resoluciones de carácter particular no podrán vulnerar una disposición de carácter general, aunque procedan de un órgano de igual o superior jerarquía (art. 37.1 LPAC), y son nulas si vulneran una disposición reglamentaria (art. 37.2 LPAC).

Blind verifier: PASS — Art. 37.1 (igual o superior jerarquía) and 37.2 (nulas si vulneran disposición reglamentaria) support the steps; Monday 5 Oct and Monday 9 Nov 2026 correct.
Student reader: REWRITE — The facts are clear but the case never states the outcome (the resolution is null, art. 37.2); say it.

## caso:### Ejecutividad#1

Current: El martes 3 de noviembre de 2026 se notifica a Ismael una resolución sancionadora contra la que cabe recurso potestativo de reposición. Los actos serán inmediatamente ejecutivos, salvo en los supuestos del artículo 98.1 (art. 98.1 LPAC). Entre ellos, una resolución de un procedimiento sancionador contra la que quepa algún recurso en vía administrativa, incluido el potestativo de reposición (art. 98.1.b) LPAC).

Blind verifier: PASS — Art. 98.1 general rule and exception 98.1.b (sanción recurrible en vía administrativa, incluido el potestativo de reposición). Tuesday 3 Nov 2026 correct.
Student reader: REWRITE — It never says the conclusion (the sanction is not immediately executable while reposición is possible); add that sentence.

## caso:### Condiciones generales#1

Current: Rosa recibe la misma notificación en papel el jueves 12 de noviembre de 2026 y accede a ella por medios electrónicos el lunes 9. Cada notificación es válida si permite tener constancia de la recepción o acceso y de sus fechas y horas (art. 41.1 LPAC). Con distintos cauces, se toma la fecha de la producida en primer lugar (art. 41.7 LPAC): el lunes 9 de noviembre.

Blind verifier: FAIL — «Cada notificación es válida si permite tener constancia de la recepción o acceso y de sus fechas y horas (art. 41.1 LPAC)» presents a partial list as sufficient: art. 41.1 also requires constancia «de su envío o puesta a disposición ..., del contenido íntegro, y de la identidad fidedigna del remitente y destinatario». The art. 41.7 step (first date, Monday 9 Nov) and weekdays (Thursday 12, Monday 9) are correct.
Student reader: KEEP — The two channels with different dates show clearly that the first one counts.

## caso:### Notificación electrónica#1

Current: El jueves 5 de noviembre de 2026 se pone a disposición de Marta una notificación electrónica obligatoria y Marta no accede a su contenido. Se entiende practicada cuando se produce el acceso (art. 43.2 LPAC). Sin acceso, se entiende rechazada al transcurrir diez días naturales desde la puesta a disposición (art. 43.2 LPAC), contados desde el día siguiente (art. 30.3 LPAC): el domingo 15 de noviembre.

Blind verifier: FAIL — Arithmetic is right (Thursday 5 Nov + 10 natural days counted from the next day = Sunday 15 Nov), but the case invokes art. 30 for the counting and silently ends on an inhábil day while the same article says «Cuando el último día del plazo sea inhábil, se entenderá prorrogado al primer día hábil siguiente» (art. 30.5). The cited text alone leaves the reader unable to tell whether the rechazo falls on Sunday 15 or Monday 16; pick dates that end on a hábil day or address 30.5.
Student reader: KEEP — It walks through the ten natural days counted from the next day, ending on Sunday 15 November.

## caso:### Nulidad de pleno derecho#1

Current: El martes 3 de noviembre de 2026 un órgano dicta un acto en una materia para la que es manifiestamente incompetente. Los actos dictados por órgano manifiestamente incompetente por razón de la materia o del territorio son nulos de pleno derecho (art. 47.1.b) LPAC). Un reglamento que regula una materia reservada a la Ley también es nulo (art. 47.2 LPAC).

Blind verifier: PASS — Art. 47.1.b (órgano manifiestamente incompetente por materia o territorio) and 47.2 (disposiciones que regulen materias reservadas a la Ley, nulas de pleno derecho). Tuesday 3 Nov correct.
Student reader: REWRITE — The facts only cover the incompetent organ; the last sentence about a reglamento has no facts and should go or get its own facts.

