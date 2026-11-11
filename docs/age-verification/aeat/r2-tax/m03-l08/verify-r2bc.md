# Blind check of the R2b/R2c edits — m03-l08, 2026-11-11

Verifier spec `docs/age-verification/aeat/r2b/verify/spec.md`. Three esquemas, all tabla, each right after the paragraphs
it summarises: plazo of the actuaciones inspectoras and its extensions (art. 150 LGT), plazos of the actas (arts. 155–157
LGT, 186–187 RGAT), plazos of the medidas cautelares (art. 146.3 LGT, 181.5 RGAT).

| id | verdict | reason | replacement |
|---|---|---|---|
| `0330d6d632` | PASS | Header; columns fit the rows. | |
| `4231139ba5` | PASS | Art. 150.1.a) LGT: «18 meses, con carácter general». In the prose. | |
| `89f83a2b04` | PASS | Art. 150.1.b) LGT verbatim, the three circumstances kept. In the prose. | |
| `6d5bd4557e` | FAIL | Art. 150.4 LGT: the periods «no podrán exceder en su conjunto de 60 días naturales para todo el procedimiento y supondrán una extensión del plazo máximo», but «El órgano actuante podrá denegar la solicitud si no se encuentra suficientemente justificada o si se aprecia que puede perjudicar el desarrollo de las actuaciones». The row makes the requested periods and the extension follow from the request alone; the prose carries the denial with the same citation. | \| Extensión: periodos solicitados por el obligado tributario antes de la apertura del trámite de audiencia, en los que la inspección no puede efectuar actuaciones con él y queda suspendido el plazo para atender los requerimientos; el órgano actuante puede denegar la solicitud si no está suficientemente justificada o si aprecia que puede perjudicar las actuaciones \| «no podrán exceder en su conjunto de 60 días naturales para todo el procedimiento» y suponen una extensión del plazo máximo de duración \| art. 150.4 LGT \| |
| `a18259c0dc` | PASS | Art. 150.5 LGT, first paragraph: three months if the aportación comes «una vez transcurrido al menos nueve meses desde su inicio», six months after the acta when it leads to actuaciones complementarias. Both conditions kept; in the prose. | |
| `651a4230a7` | PASS | Art. 150.5 LGT, second paragraph: «se extenderá por un periodo de seis meses cuando tras dejar constancia de la apreciación de las circunstancias determinantes de la aplicación del método de estimación indirecta, se aporten datos, documentos o pruebas relacionados con dichas circunstancias». In the prose. | |
| `e2893efacf` | PASS | Header; columns fit the rows. | |
| `bc7097453e` | PASS | Art. 155.5 LGT, first paragraph, faithful; in the prose. | |
| `31f0a1e928` | PASS | Art. 186.7 RGAT: «un plazo de 10 días hábiles, contados a partir del día siguiente al de la fecha del acta, para notificar… una liquidación que rectifique los errores materiales». «Ese plazo» points to the row above, as the prose does («El RGAT precisa que ese plazo es de 10 días hábiles»). | |
| `3e217a1d34` | PASS | Art. 156.3 LGT verbatim with the four contents a)–d). In the prose. | |
| `dd204e4793` | PASS | Art. 187.3.b) RGAT: «se concederá un plazo de 15 días, contados a partir del día siguiente al de la notificación de la apertura de dicho plazo, para que formule alegaciones». In the prose. | |
| `3420f95af8` | PASS | Art. 157.3 LGT verbatim; in the prose. | |
| `65efa8ba0f` | PASS | Header; columns fit the rows. | |
| `f64fc1b1d8` | PASS | Art. 146.3 LGT: «Las medidas adoptadas deberán ser ratificadas por el órgano competente para liquidar en el plazo de 15 días desde su adopción». Quotation as in the prose. | |
| `421156bd89` | PASS | Art. 181.5 RGAT, quotation as in the prose. | |
| `5dae4e9854` | PASS | Art. 181.5 RGAT: the órgano competente para liquidar «deberá ratificar, modificar o levantar la medida» by acuerdo motivado in 15 days from adoption, communicated to the obligado. In the prose. | |
| title m03-l08 «Plazo de las actuaciones inspectoras y sus extensiones» | PASS | Both plazos of art. 150.1 and every extension of art. 150.4–5 LGT. | |
| title m03-l08 «Plazos de las actas con acuerdo, de conformidad y de disconformidad» | PASS | Accurate for the rows; one or more plazo per kind of acta. | |
| title m03-l08 «Plazos de las medidas cautelares» | PASS | The three plazos of arts. 146.3 LGT and 181.5 RGAT. | |
