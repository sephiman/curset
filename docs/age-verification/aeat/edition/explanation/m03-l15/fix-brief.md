# Fix brief — `m03-l15`

## overview (draft.md, the OVERVIEW block) — FAIL

«El período impositivo es el año natural y el impuesto se devenga el 31 de diciembre (art. 12.1 y 12.2 LIRPF)» omite la salvedad del propio 12.2 («sin perjuicio de lo establecido en el artículo siguiente»): con fallecimiento en día distinto del 31 de diciembre el período es inferior y el devengo se produce en esa fecha (art. 13). El resto (arts. 1, 6.1, 8.1, 17.1, 21.1, 27.1, 85.1, 33.1) es correcto, aunque «según su residencia habitual» resume el 8.1 de forma laxa.

## caso:### Rendimiento neto y reducciones#1

Current: Raúl, desempleado inscrito, acepta en 2026 un puesto que exige trasladar su residencia habitual a otro municipio. Sus otros gastos, 2.000 euros, aumentan en 2.000 euros adicionales en 2026 y en 2027: 4.000 euros (art. 19.2.f LIRPF). Carmen, trabajadora activa con discapacidad, suma 3.500 euros a los 2.000: 5.500 euros anuales (art. 19.2.f LIRPF).

Blind verifier: FAIL — «Carmen, trabajadora activa con discapacidad, suma 3.500 euros a los 2.000: 5.500 euros anuales»: el 19.2.f distingue y eleva el incremento a 7.750 euros si acredita ayuda de terceras personas, movilidad reducida o grado igual o superior al 65 %; el caso no fija esa condición y deja la regla de que toda discapacidad da 3.500. Además, para Raúl no se dice que el cambio de residencia se produzca en 2026, que es lo que fija los dos períodos del incremento.
Student reader: REWRITE — "aumentan en 2.000 adicionales en 2026 y en 2027: 4.000" is ambiguous (4.000 each year? in total?); state the year-by-year figures.

## caso:### Concepto y métodos de determinación#1

Current: El rendimiento de la actividad de Sara se determina por estimación directa, que se aplica como método general y tiene modalidad normal y simplificada (art. 16.2.a LIRPF). Pedro renunció a la estimación objetiva y a él se le aplica la estimación indirecta: se tienen en cuenta preferentemente los signos, índices o módulos de la objetiva (art. 16.3 LIRPF).

Blind verifier: FAIL — «Pedro renunció a la estimación objetiva y a él se le aplica la estimación indirecta» presenta la indirecta como consecuencia de la renuncia; el 16.3 dice que la indirecta «se aplicará de conformidad con lo dispuesto en la» LGT, y solo cuando se aplica por esa vía se toman preferentemente los módulos de la objetiva si el contribuyente renunció a ella. Falta la condición que la activa.
Student reader: REWRITE — It suggests renouncing the objective method leads to indirecta, which confuses; say what triggers indirecta and that renunciation leads to directa.

## caso:## Imputación de rentas inmobiliarias#1

Current: En 2026 Beatriz es titular de un derecho de aprovechamiento por turno de 10 días al año. No procede la imputación, porque su duración no excede de dos semanas por año (art. 85.3 LIRPF). Carlos es titular de otro de 21 días al año sobre un inmueble de valor catastral 70.000 euros: la imputación se hace al titular del derecho real, prorrateando el valor catastral según la duración anual del aprovechamiento (art. 85.3 LIRPF).

Blind verifier: PASS — 10 días no exceden de dos semanas: sin imputación; 21 días: imputación al titular del derecho real prorrateando el valor catastral (85.3).
Student reader: REWRITE — Carlos's imputation is described but never computed; add the proration figure from the 70.000 cadastral value.

