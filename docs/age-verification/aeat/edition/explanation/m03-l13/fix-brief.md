# Fix brief — `m03-l13`

## caso:### Principio de responsabilidad#1

Current: Marta presentó el lunes 20 de abril de 2026 una autoliquidación con una cuota menor y la subsanó voluntariamente el lunes 8 de junio de 2026. El lunes 15 de junio de 2026 se le notificó un requerimiento para el cumplimiento de la obligación tributaria. La regularización voluntaria es la efectuada antes de esa notificación (art. 2 RGRST), así que Marta no incurre en responsabilidad (art. 179.3 LGT).

Blind verifier: FAIL — «así que Marta no incurre en responsabilidad (art. 179.3 LGT)» drops what limits the rule. 179.3 excludes only responsibility «por las infracciones tributarias cometidas con ocasión de la presentación de aquéllas». Its second paragraph adds that this is «sin perjuicio de lo previsto en el artículo 27» and of infracciones from the late or incorrect new filing. A subsanación on 08-06-2026 of an autoliquidación filed on 20-04-2026 is the textbook art. 27 recargo case, and the reader is left thinking it has no consequence. The dates (Mondays 20-04, 08-06, 15-06-2026) and the RGRST art. 2 timing are correct.
Student reader: KEEP — Voluntary correction before the 15 June notification is dated and clear, so I can test any new date against the notification.

## caso:### Principio de no concurrencia#1

Current: Óscar recibe en 2026 una sanción de 5.000 euros y un interés de demora de 600 euros. La omisión que debe aplicarse como criterio de graduación de la sanción no puede sancionarse además como infracción independiente (art. 180.1 LGT). La sanción resulta compatible con la exigencia del interés de demora de 600 euros (art. 180.3 LGT).

Blind verifier: PASS — Rules match 180.1 and 180.3. Minor: «La omisión que debe aplicarse como criterio de graduación» has no matching fact in the case, and 180.1's second alternative (circumstance deciding the calificación) is not mentioned. Nothing stated is wrong.
Student reader: REWRITE — The second sentence is abstract with no facts about Óscar; say which omission was used as a graduation criterion, and use the 5,000 and 600 euros only for the interest point.

## caso:### Extinción de la responsabilidad derivada de las infracciones#1

Current: Hugo cometió una infracción tributaria el jueves 10 de marzo de 2022. El plazo de prescripción para imponer sanciones es de cuatro años desde que se cometió (art. 189.2 LGT) y se cumpliría el 10 de marzo de 2026. El lunes 2 de febrero de 2026 la Administración realiza, con conocimiento formal de Hugo, una acción conducente a la imposición de la sanción, y eso interrumpe la prescripción (art. 189.3.a LGT).

Blind verifier: PASS — Thursday 10-03-2022 + 4 years = 10-03-2026 (189.2). The action on Monday 02-02-2026, with conocimiento formal, interrupts it (189.3.a).
Student reader: REWRITE — The interruption is stated but not its effect (the four years start again), so I cannot tell the new expiry date.

## caso:### Dejar de ingresar la deuda que debiera resultar de una autoliquidación#1

Current: Pedro dejó de ingresar 2.800 euros en una autoliquidación de 2026, sin facturas falsas ni retenciones impagadas. La base de la sanción es 2.800 euros, inferior a 3.000, y la infracción es leve con multa proporcional del 50 por ciento: 1.400 euros (art. 191.2 LGT). Esa multa no prevé graduación (art. 191.2 LGT). Si lo no ingresado fueran cantidades retenidas, no sería leve cualquiera que fuera la base (art. 191.2.c LGT).

Blind verifier: FAIL — The facts rule out two of the three «no será leve» cases, «sin facturas falsas ni retenciones impagadas». They leave out 191.2.b, llevanza incorrecta de libros above 10 % of the base. So the leve conclusion does not rest on the stated facts, and the reader gets a two-item list as if complete. 2.800 ≤ 3.000 → 50 % = 1.400 is right.
Student reader: KEEP — 2,800 euros under the 3,000 limit gives leve and 1,400 euros, with the retained-amounts exception.

## caso:### Solicitar indebidamente devoluciones, beneficios o incentivos fiscales#1

Current: Carmen solicitó en 2026 una devolución de 6.000 euros omitiendo datos relevantes y no la obtuvo. La infracción es grave, la base es 6.000 euros y la multa proporcional del 15 por ciento da 900 euros (art. 194.1 LGT). Si la hubiera obtenido, no se aplicaría este apartado (art. 194.1 LGT). Por un beneficio fiscal pedido con datos falsos, sin sanción por los artículos 191, 192 o 195 LGT, la multa fija es de 300 euros (art. 194.2 LGT).

Blind verifier: FAIL — «sin sanción por los artículos 191, 192 o 195 LGT, la multa fija es de 300 euros»: 194.2 also requires no sanción under «el primer apartado de este artículo» (194.1). One of the four sources the article names is missing. 6.000 × 15 % = 900 (grave) and the «no obtenida» condition are correct.
Student reader: KEEP — 15 percent of 6,000 versus the fixed 300 euros separates the two paragraphs.

