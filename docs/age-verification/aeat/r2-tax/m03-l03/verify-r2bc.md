# Blind check of the R2b/R2c edits — m03-l03, 2026-11-11

Verifier spec `docs/age-verification/aeat/r2b/verify/spec.md`. One scope note and three esquemas: «Interés de demora y
interés legal del dinero para 2026», «Recargos por declaración extemporánea sin requerimiento previo» and «De la base
imponible a la cuota diferencial» (all tabla, each right after the paragraphs it summarises).

| id | verdict | reason | replacement |
|---|---|---|---|
| `f5198c1e99` | PASS | Note heads «Vigencia, sujeción, interpretación y calificación» (arts. 10–16 LGT). Tema III.3 literal names «Fuentes», which in the LGT is sección 1.ª «Fuentes normativas» (arts. 7–9); the ámbito temporal, interpretación and calificación are other secciones and not named. 2022X-33 exists (art. 10.1 LGT, key A «entrarán en vigor a los veinte días naturales…»), `vigente`; answered by the section's art. 10.1 LGT sentence. | |
| `dd284bf2d7` | PASS | Header; columns fit both rows. | |
| `901ae99d42` | FAIL | Disposición adicional cuadragésima segunda.Dos Ley 31/2022: «Durante el mismo periodo [hasta el 31 de diciembre del año 2023], el interés de demora… será el 4,0625 por ciento.» The figure is right, but the cited precept on its own fixes it only for 2023; the prose carries it for 2026 as «disposición adicional cuadragésima segunda.Dos Ley 31/2022, prorrogada para 2026». An annual figure must keep the norm as the prose has it, and the row drops «prorrogada para 2026». | \| Interés de demora \| 4,0625 por ciento \| disposición adicional cuadragésima segunda.Dos Ley 31/2022, prorrogada para 2026 \| |
| `642059ad06` | FAIL | Disposición adicional cuadragésima segunda.Uno Ley 31/2022: interés legal «en el 3,25 por ciento hasta el 31 de diciembre del año 2023». Same defect as `901ae99d42`: the prose has «disposición adicional cuadragésima segunda.Uno Ley 31/2022, prorrogada para 2026»; the row drops the prórroga. | \| Interés legal del dinero \| 3,25 por ciento \| disposición adicional cuadragésima segunda.Uno Ley 31/2022, prorrogada para 2026 \| |
| `ee80d4dfed` | PASS | Header; columns fit the rows. | |
| `56de3bb17e` | FAIL | Art. 27.2 LGT, first two paragraphs, verbatim. But the row says every «Presentación sin requerimiento previo» bears the recargo, and art. 27.2 has an exception: «no se exigirán los recargos de este apartado si el obligado tributario regulariza, mediante la presentación de una declaración o autoliquidación correspondiente a otros períodos del mismo concepto impositivo, unos hechos o circunstancias idénticos a los regularizados por la Administración, y concurren las siguientes circunstancias: a)… d)». Art. 27.4 adds a condition for the whole article: the autoliquidaciones extemporáneas «deberán identificar expresamente el período impositivo de liquidación al que se refieren y deberán contener únicamente los datos relativos a dicho período». The prose has neither, so the row reads wider than the article and cannot carry the exception: drop until the prose has it (gap: m03-l03, art. 27.2 párrafos quinto y sexto and art. 27.4 LGT). | drop |
| `837f0f90ed` | FAIL | Art. 27.2 LGT, third paragraph, verbatim. Same gap as `56de3bb17e`: the 15 por ciento recargo is subject to the same exception of art. 27.2 (regularización de otros períodos, circunstancias a)–d)) and to art. 27.4, both missing from the prose. Drop until the prose has it. | drop |
| `df19f3c753` | PASS | Art. 27.5 LGT, both paragraphs, faithful shortening: 25 por ciento, the three ingreso conditions (art. 62.2 plazo; deuda at presentation or art. 62.2 plazo; aplazamiento o fraccionamiento con aval o certificado de seguro de caución solicitado in time) and the clawback «sin más requisito que la notificación al interesado» all kept; in the prose with art. 27.5 LGT. | |
| `ba91a4afa8` | PASS | Header; columns fit the rows. | |
| `f2088aea7f` | PASS | Art. 50.1 LGT verbatim; in the prose. | |
| `100c71f3ae` | PASS | Art. 54 LGT verbatim; in the prose. | |
| `5464f21677` | PASS | Art. 55.1 LGT verbatim; in the prose. | |
| `4138f91714` | PASS | Art. 56.1 LGT: «La cuota íntegra se determinará: a) Aplicando el tipo de gravamen a la base liquidable. b) Según cantidad fija señalada al efecto.» Both ways kept; in the prose. | |
| `0f148d054b` | PASS | Art. 56.5 LGT verbatim; in the prose. | |
| `995cf1507c` | PASS | Art. 56.6 LGT verbatim; in the prose. | |
| title m03-l03 «Interés de demora y interés legal del dinero para 2026» | PASS | Both figures the prose gives for 2026; year in the title. | |
| title m03-l03 «Recargos por declaración extemporánea sin requerimiento previo» | PASS | The heading of art. 27 LGT; accurate for the rows (the defect is in the rows, see `56de3bb17e`). | |
| title m03-l03 «De la base imponible a la cuota diferencial» | PASS | The rows run from art. 50.1 to art. 56.6 LGT, each defined on the previous one (base liquidable on base imponible, tipo on base liquidable, cuota íntegra on tipo and base, cuota líquida on cuota íntegra, cuota diferencial on cuota líquida), so the «de… a…» order is the norm's. | |
