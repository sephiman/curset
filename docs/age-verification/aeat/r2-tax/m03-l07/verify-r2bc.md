# Blind check of the R2b/R2c edits — m03-l07, 2026-11-11

Verifier spec `docs/age-verification/aeat/r2b/verify/spec.md`. Four esquemas, all tabla, each right after the paragraphs
it summarises: devolución and rectificación (after «Terminación» of the rectificación), tasación pericial contradictoria
(after art. 135.2–4 LGT), plazos of the procedures iniciado mediante declaración, verificación de datos and comprobación
limitada (after the comprobación limitada «Tramitación»), and effects of the lapse of the plazo (after «Control de la
presentación de declaraciones», the last procedure it covers).

| id | verdict | reason | replacement |
|---|---|---|---|
| `171614df81` | PASS | Header; columns fit the rows. | |
| `4f2dcc1f87` | PASS | Art. 31.2 LGT, first sentence, verbatim; in the prose. | |
| `b7044e495f` | PASS | Art. 120.3 LGT, second paragraph: six months «sin que se hubiera ordenado el pago por causa imputable a la Administración tributaria», interest «sin necesidad de que el obligado lo solicite», and the start of the six months. Faithful; in the prose. | |
| `7a947797e3` | FAIL | Art. 127.4 RGAT: «…para que en un plazo de 15 días… alegue lo que convenga a su derecho, salvo que la rectificación que se acuerde coincida con la solicitada por el interesado, en cuyo caso se notificará sin más trámite la liquidación que se practique.» The row drops the exception, which the prose carries with the same citation («Si la rectificación que se acuerda coincide con la solicitada, se notifica sin más trámite la liquidación que se practique»). | \| Rectificación de autoliquidaciones: alegaciones \| finalizadas las actuaciones, se notifica al interesado la propuesta de resolución para que alegue en el plazo de 15 días, contados desde el día siguiente al de la notificación de la propuesta; si la rectificación que se acuerda coincide con la solicitada, se notifica sin más trámite la liquidación que se practique \| art. 127.4 RGAT \| |
| `0fe1c9d853` | PASS | Art. 128.4 RGAT: «El plazo máximo para notificar la resolución de este procedimiento será de seis meses. Transcurrido dicho plazo sin haberse realizado la notificación expresa…, la solicitud podrá entenderse desestimada.» In the prose. | |
| `2a6aa0af8c` | PASS | Header; the first column states the magnitude the two rows compare, in the words of art. 135.2 LGT. | |
| `0aed5066fd` | PASS | Art. 135.2 LGT: «considerada en valores absolutos, es igual o inferior a 120.000 euros y al 10 por ciento de dicha tasación, esta última servirá de base para la liquidación». Both thresholds kept; in the prose. | |
| `9b9c3e33de` | PASS | Art. 135.2 LGT: «Si la diferencia es superior, deberá designarse un perito tercero». In the prose. | |
| `936316d9df` | PASS | Header; columns fit the rows. | |
| `e904bd60ce` | PASS | Art. 129.1 LGT, all three paragraphs (six months and both starting points, extemporáneas, other plazos in each tributo's normativa). In the prose. | |
| `0c471d4fd1` | PASS | Art. 133.1 RGAT: «se le otorgará un plazo de 10 días, contados a partir del día siguiente al de la notificación del requerimiento, para su aportación, salvo que la normativa específica establezca otro plazo». In the prose. | |
| `2451920e87` | PASS | Art. 155.3 RGAT: propuesta de resolución o de liquidación, «en un plazo de 10 días, contados a partir del día siguiente al de la notificación de la propuesta». In the prose. | |
| `e168f20749` | PASS | Art. 164.4 RGAT: 10 días, and «Se podrá prescindir del trámite de alegaciones cuando la resolución contenga manifestación expresa de que no procede regularizar la situación tributaria». Exception kept; in the prose. | |
| `468257949f` | PASS | Header; columns fit the rows. | |
| `f5da8a6a01` | PASS | Art. 128.4 RGAT, as `0fe1c9d853`. | |
| `951c1d3a16` | PASS | Art. 130.b) LGT verbatim («del artículo 129.1» for «del apartado 1 del artículo anterior»); in the prose. | |
| `6ac613a257` | PASS | Art. 133.1.d) LGT verbatim; in the prose. | |
| `92f0b5d71b` | PASS | Art. 139.1.b) LGT verbatim; in the prose. | |
| `2c61e471d0` | PASS | Art. 153.6.d) RGAT verbatim; in the prose. | |
| title m03-l07 «Plazos de la devolución y de la rectificación de autoliquidaciones» | PASS | The devolución interest plazo (art. 31.2 LGT) and the rectificación plazos (arts. 120.3 LGT, 127.4 and 128.4 RGAT) the section states. | |
| title m03-l07 «La diferencia de valoraciones en la tasación pericial contradictoria» | PASS | Both cases of art. 135.2 LGT. | |
| title m03-l07 «Plazos de los procedimientos iniciados mediante declaración, de verificación de datos y de comprobación limitada» | FAIL | The four rows are trámite plazos only; the same procedures have the maximum duration of art. 104 LGT the lesson states for their caducidad (arts. 133.1.d) and 139.1.b) LGT), and other plazos of their articles. The title reads the four as all the plazos of the three procedures. | Algunos plazos de los procedimientos iniciados mediante declaración, de verificación de datos y de comprobación limitada |
| title m03-l07 «Efecto del vencimiento del plazo sin notificación expresa» | FAIL | Five procedures; the lesson states the same effect for two more it leaves out (devolución, «Por caducidad, en los términos del artículo 104.3 de la LGT», art. 127 LGT; tasación pericial contradictoria, art. 162.1.e) RGAT). The title reads as the rule for every procedure of the lesson. | Efecto del vencimiento del plazo sin notificación expresa en algunos procedimientos de gestión |
