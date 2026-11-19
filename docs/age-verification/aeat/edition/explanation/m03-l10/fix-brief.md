# Fix brief — `m03-l10`

## caso:### Compensación a instancia del obligado tributario#1

Current: Ainhoa presenta el 12 de marzo de 2026 una solicitud de compensación de una deuda en período voluntario con un crédito reconocido que ya cumple los requisitos. La solicitud impide el inicio del período ejecutivo de la deuda concurrente con el crédito ofrecido, pero no el devengo del interés de demora que pueda proceder hasta la fecha de reconocimiento del crédito (art. 72.2 LGT). La deuda se extingue en el momento de la presentación de la solicitud (art. 72.3 LGT).

Blind verifier: PASS — 72.2 effects are correct. The requisitos are already met, so extinction happens on presentación (72.3).
Student reader: REWRITE — The interest-keeps-running point is subtle and no figures or dates show it; add the debt, the credit date and the interest period.

## caso:### Cuenta corriente tributaria#1

Current: Rosa está acogida al sistema de cuenta corriente tributaria. Presenta fuera de plazo una autoliquidación del Impuesto sobre el Valor Añadido en 2026: los créditos y deudas que se deriven de ella no pueden anotarse (art. 139.4 RGAT). La duración del sistema es, con carácter general, indefinida, y se aplica mientras Rosa no renuncie expresamente a su aplicación o proceda la revocación por la Administración (art. 143.1 RGAT).

Blind verifier: PASS — Autoliquidaciones filed late cannot be anotadas (139.4.a RGAT). The duration is indefinite unless there is renuncia or revocación (143.1).
Student reader: REWRITE — Two unrelated rules are joined (late return not annotated; indefinite duration) and the second has no facts; keep one or give Rosa a renunciation scenario.

## caso:## Extinción de deudas de las entidades de derecho público mediante deducciones sobre transferencias#1

Current: El Ayuntamiento de Villaflor tiene con el Estado una deuda vencida, líquida y exigible, impagada tras el período voluntario y sin crédito compensable de oficio. Se inicia el procedimiento de deducción mediante acuerdo notificado el lunes 9 de noviembre de 2026 (art. 60.2 RGR). Dispone de 15 días desde el día siguiente para alegar, sin festivos hasta el lunes 30 de noviembre (art. 60.2 RGR; art. 30.2 LPAC). El inicio suspende el cobro de la deuda (art. 74.2 LGT).

Blind verifier: FAIL — The debtor is an Ayuntamiento, an entidad local. Art. 74.1 párr. 2 LGT says that for entidades locales the régimen applies «en los supuestos y conforme al procedimiento establecido en la legislación específica». The case applies RGR 60.2 as the procedure and never names that source. Date check is correct: Monday 09-11-2026, 15 días hábiles from 10-11 end on Monday 30-11-2026. The suspension is correct (74.2).
Student reader: KEEP — Dated 15-day allegations window and the suspension of collection on start are clear.

