# Fix brief — `m03-l06`

## overview (draft.md, the OVERVIEW block) — FAIL

«Sus clases son las autoliquidaciones (art. 120.1 LGT) y las comunicaciones de datos (art. 121 LGT), con sus variantes complementarias y sustitutivas (art. 122.1 LGT)»: no cited article sets out «clases», and the list leaves out the plain declaraciones that art. 122.1 names beside them («autoliquidaciones complementarias, o declaraciones o comunicaciones complementarias o sustitutivas»), so a partial list reads as complete; it also attaches «sustitutivas» to autoliquidaciones, while art. 122.1 allows only complementarias for autoliquidaciones and sustitutivas only for declaraciones and comunicaciones. The other legal statements (119.1, 23.1 autonomy, 99.1 three forms, 40.1, 128.1, 164.Uno.6.º, Orden 1.1, 99.2/RIRPF 75.3, 101.8 19 %, 119.3) match the cited text.

## caso:## Las autoliquidaciones#1

Current: El plazo para presentar la autoliquidación de Rosa concluyó el martes 30 de junio de 2026. El martes 15 de septiembre de 2026 presenta la solicitud de rectificación, que origina una devolución derivada de la normativa del tributo. Los seis meses, contados desde esa presentación, terminan el lunes 15 de marzo de 2027 (art. 120.3 LGT; art. 30.4 LPAC). Sin pago ordenado por causa imputable a la Administración, abona el interés de demora sin que lo pida (art. 120.3 LGT).

Blind verifier: FAIL — Dates and the six-month count are right: plazo ended Tue 30 Jun 2026, so the six months run from the solicitud (Tue 15 Sep 2026) and end Mon 15 Mar 2027 (art. 120.3; 30.4 LPAC). But «abona el interés de demora sin que lo pida» drops the source art. 120.3 names: «el interés de demora del artículo 26 de esta Ley sobre el importe de la devolución que proceda»; the case also does not say the interest is on the importe of the devolución.
Student reader: REWRITE — The last sentence ("abona el interés de demora sin que lo pida") reads as if Rosa pays; say the Administración pays Rosa, and that the six months passed with no payment ordered.

## caso:### El pago fraccionado del Impuesto sobre Sociedades#1

Current: Una sociedad con período impositivo igual al año natural efectúa su pago fraccionado de octubre de 2026 entre el jueves 1 y el martes 20 de octubre (art. 40.1 LIS). Su último período con plazo de declaración vencido tiene una cuota íntegra de 100.000 euros, con 10.000 euros de deducciones y bonificaciones y 5.000 euros de retenciones e ingresos a cuenta. La base es de 85.000 euros y el 18 por ciento da 15.300 euros (art. 40.2 LIS).

Blind verifier: FAIL — Arithmetic (100.000 − 10.000 − 5.000 = 85.000; 18 % = 15.300) and the 1–20 Oct 2026 window (Thu–Tue) are right, but the case applies the art. 40.2 modality without the condition of art. 40.3 that changes the result: the company must not have opted for the base-imponible modality and its importe neto de la cifra de negocios must not have exceeded 6 millones in the 12 months before the período began («estarán obligados a aplicar la modalidad a que se refiere este apartado»). The reader may take 18 % of the cuota as the rule for every company.
Student reader: KEEP — The step-by-step base (quota minus deductions minus withholdings) times 18 percent gives a method I can repeat.

