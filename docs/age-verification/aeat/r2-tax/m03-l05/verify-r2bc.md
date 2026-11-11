# Blind check of the R2b/R2c edits — m03-l05, 2026-11-11

Verifier spec `docs/age-verification/aeat/r2b/verify/spec.md`. Four esquemas, each right after the paragraphs it
summarises: «Plazos de la información previa, los acuerdos de valoración y los certificados» (tabla), «Plazo máximo de
resolución y cómputo» (tabla), «Efectos del vencimiento del plazo sin resolución expresa» (tabla), «La notificación por
comparecencia» (plazos); and three «Normativa» lines changed by removals.

| id | verdict | reason | replacement |
|---|---|---|---|
| `0330d6d632` | PASS | Header; columns fit the rows. | |
| `72c513cb27` | PASS | Art. 90.2 LGT: «Esta información tendrá efectos vinculantes durante un plazo de tres meses, contados desde la notificación al interesado, siempre que la solicitud se haya formulado con carácter previo a la finalización del plazo para presentar la correspondiente autoliquidación o declaración y se hayan proporcionado datos verdaderos y suficientes…». Both conditions kept; in the prose. | |
| `4693b95aa4` | PASS | Art. 69.6 RGAT: «El plazo para contestar estas solicitudes de información será de tres meses.» In the prose. | |
| `317a004432` | PASS | Art. 91.5 LGT: «Dicho acuerdo tendrá un plazo máximo de vigencia de tres años excepto que la normativa que lo establezca prevea otro distinto.» «Máximo» keeps the earlier end when the legislation or circumstances change; in the prose. | |
| `eec2ccd103` | PASS | Art. 73.1 RGAT: «en el plazo de 20 días, salvo que en la normativa reguladora del certificado se haya fijado un plazo distinto». In the prose. | |
| `c45b925c67` | PASS | Art. 73.4 RGAT: «en el plazo de 10 días, contados a partir del día siguiente al de su recepción». In the prose. | |
| `a12e688828` | PASS | Art. 73.4 RGAT: «procederá a la emisión de uno nuevo en el plazo de 10 días»; condition in the label. In the prose. | |
| `a11c7df8ba` | PASS | Art. 75.2 RGAT: 12 meses (obligaciones periódicas, while circumstances do not change) or tres meses (no periódicas), «salvo que la normativa específica» says otherwise (in the label). In the prose. | |
| `4a2e1a9c14` | PASS | Header; columns fit the rows. | |
| `9f805d69a2` | PASS | Art. 104.1 LGT, first sentence, verbatim with both exceptions; in the prose. | |
| `2c9ff49900` | PASS | Art. 104.1 LGT: «Cuando las normas reguladoras de los procedimientos no fijen plazo máximo, éste será de seis meses.» In the prose. | |
| `b84029b6eb` | PASS | Art. 104.1.a) LGT verbatim; in the prose. | |
| `ff36ab3ed6` | PASS | Art. 104.1.b) LGT verbatim; in the prose. | |
| `7e4fd90858` | PASS | Art. 104.1 LGT: «Queda excluido de lo dispuesto en este apartado el procedimiento de apremio, cuyas actuaciones podrán extenderse hasta el plazo de prescripción del derecho de cobro.» In the prose. | |
| `468257949f` | PASS | Header; columns fit the rows. | |
| `9ef600ad5e` | PASS | Art. 104.3 LGT, second paragraph, verbatim with the two desestimatorio exceptions; the label keeps «en defecto de» the normativa reguladora. In the prose. | |
| `cef68e853b` | PASS | Art. 104.4.a) LGT verbatim; label keeps «en ausencia de regulación expresa». In the prose. | |
| `e62ec3979b` | PASS | Art. 104.4.b) LGT verbatim; label keeps the condition. In the prose. | |
| `bc2a799b71` | PASS | Art. 112.1 LGT, first paragraph: two attempts, the domicile rule for procedures a solicitud, «Será suficiente un solo intento cuando el destinatario conste como desconocido». First step: the norm's «En este supuesto se citará…» supports the order. In the prose. | |
| `fb30913420` | PASS | Art. 112.1 LGT: anuncios «por una sola vez para cada interesado, en el "Boletín Oficial del Estado"… los lunes, miércoles y viernes de cada semana». In the prose. | |
| `4927f21cf0` | PASS | Art. 112.2 LGT: «en el plazo de 15 días naturales, contados desde el siguiente al de la publicación del anuncio en el "Boletín Oficial del Estado"». Follows the publication, as the norm says. In the prose. | |
| `04f82ae620` | PASS | Art. 112.2 LGT: «Transcurrido dicho plazo sin comparecer, la notificación se entenderá producida a todos los efectos legales el día siguiente al del vencimiento del plazo señalado.» Last step, as the norm orders. In the prose. | |
| `92604de768` | PASS | Starts with the `short` «LGT (Ley 58/2003)». Prose citations: 85.1–2, 86.1–2, 86.4, 87.1–2, 90.1–3, 91.1–6, 92.1–4, 95.1–5, 95 bis.1–2, 95 bis.4–5, 95 bis.7, 97, 98.1–4, 99.1–4, 99.6–9, 100.1–2, 101.1–4, 102.1–4, 103.1–3, 104.1–5, 105.1–2, 109, 110.1–2, 111.1–2, 112.1–3; precepts named in the text: 27.1, 35.4, 57.1 («apartado 1 del artículo 57»), 128, 155, 250.2. The line matches; the removed 88–89 and 106–108 are no longer cited. | |
| `019d9116bf` | PASS | Starts with the `short` «RGAT (RD 1065/2007)». Prose citations: 62, 63.1–3, 64.1, 69.1, 69.6, 70.1–5, 71.1, 72.1, 73.1–2, 73.4, 75.1–2, 77.1, 77.4, 78.1, 79.1–4, 91.1–6, 102.1, 102.5, 103, 104; named in the text: 36, 59. The line matches; the removed art. 65 is no longer cited. | |
| `e40837a502` | PASS | Starts with the `short` «Ley 25/2003 (modificación del Convenio Económico con Navarra)»; art. 51 is named inside the art. 103.f) RGAT list in the prose. | |
| title m03-l05 «Plazos de la información previa, los acuerdos de valoración y los certificados» | PASS | Every row is a plazo of one of the three institutions, all from the section's prose. | |
| title m03-l05 «Plazo máximo de resolución y cómputo» | PASS | Accurate for the rows of art. 104.1 LGT. | |
| title m03-l05 «Efectos del vencimiento del plazo sin resolución expresa» | PASS | Accurate for art. 104.3–4 LGT; the rows are the default rules, each label keeping «en defecto de» / «en ausencia de regulación expresa». | |
| title m03-l05 «La notificación por comparecencia» | PASS | Heading of art. 112 LGT; the four steps follow the article's order. | |
