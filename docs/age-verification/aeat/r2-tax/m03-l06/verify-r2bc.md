# Blind check of the R2b/R2c edits — m03-l06, 2026-11-11

Verifier spec `docs/age-verification/aeat/r2b/verify/spec.md`. Two esquemas, both tabla: «Plazos de declaración e
ingreso de retenciones y pagos fraccionados» (after art. 40.1–2 LIS paragraphs) and «Modalidades del pago fraccionado del
Impuesto sobre Sociedades» (after the art. 40.3–5 LIS paragraph).

| id | verdict | reason | replacement |
|---|---|---|---|
| `fd401c00ee` | PASS | Header; columns fit the rows. | |
| `02fb5270af` | PASS | Art. 108.1 RIRPF, first paragraph: «en los primeros veinte días naturales de los meses de abril, julio, octubre y enero… por el trimestre natural inmediato anterior». «Con carácter general» in the label keeps the exceptions of the next paragraphs open; in the prose. | |
| `0f097a1353` | PASS | Art. 108.1 RIRPF, second paragraph: «en los veinte primeros días naturales de cada mes… por el mes inmediato anterior, cuando se trate de retenedores u obligados en los que concurran las circunstancias a que se refieren los números 1.º y 2.º del apartado 3 del artículo 71» RIVA. Faithful; in the prose. | |
| `4243d92246` | PASS | Art. 111.1.a) RIRPF verbatim; in the prose. | |
| `8302e9d037` | PASS | Art. 111.1.b) RIRPF verbatim; in the prose. | |
| `db3cb3deb1` | PASS | Art. 40.1 LIS: «En los primeros 20 días naturales de los meses de abril, octubre y diciembre…»; the exclusion of the entities of art. 29.4–5 LIS is in the label. In the prose. | |
| `6b9bb0658e` | PASS | Header; columns fit the rows. | |
| `e226ce5ea7` | FAIL | Art. 40.2 LIS gives the base (first paragraph, kept verbatim) and the 18 por ciento, but the same apartado adds: «Cuando el último período impositivo concluido sea de duración inferior al año se tomará también en cuenta la parte proporcional de la cuota de períodos impositivos anteriores, hasta completar un período de 12 meses.» The row's base reads as the whole rule; the prose (art. 40.2 LIS paragraph) has the same gap. Drop until the prose has it (gap: m03-l06, art. 40.2 párrafo segundo LIS). | drop |
| `d9532db64c` | FAIL | Art. 40.3 LIS, first paragraph (base of the 3, 9 u 11 primeros meses «de cada año natural»), the 6 millones obligation and the cinco séptimos percentage are kept. But the same apartado gives a different base when the period does not match the calendar year: «Los contribuyentes cuyo período impositivo no coincida con el año natural realizarán el pago fraccionado sobre la parte de la base imponible correspondiente a los días transcurridos desde el inicio del período impositivo hasta el día anterior al inicio de cada uno de los períodos de ingreso…». The row's base reads as the rule for every contribuyente in this modalidad; the prose mentions non-calendar periods only for exercising the option. Drop until the prose has the base rule (gap: m03-l06, art. 40.3 párrafo segundo LIS). | drop |
| title m03-l06 «Plazos de declaración e ingreso de retenciones y pagos fraccionados» | FAIL | The rows are only the IRPF retenciones and the IRPF and IS pagos fraccionados, and art. 108.1 RIRPF has a further monthly case the table leaves out (Administraciones públicas whose budget exceeds 6 millones de euros, párrafo tercero). The title reads the list as every such plazo. | Algunos plazos de declaración e ingreso de retenciones y pagos fraccionados |
| title m03-l06 «Modalidades del pago fraccionado del Impuesto sobre Sociedades» | PASS | The two modalidades of art. 40.2 and 40.3 LIS; complete. | |
