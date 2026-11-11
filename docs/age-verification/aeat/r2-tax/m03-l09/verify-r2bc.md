# Blind check of the R2b/R2c edits — m03-l09, 2026-11-11

Verifier spec `docs/age-verification/aeat/r2b/verify/spec.md`. Three esquemas, all tabla, each right after the paragraphs
it summarises: «Otros plazos de pago en período voluntario» (art. 62.1, 62.3, 62.4 LGT; the art. 62.2 plazos are a prose
table just above), «Cobertura de la garantía y límite exento en el aplazamiento y fraccionamiento» and «Plazos del
aplazamiento y fraccionamiento».

| id | verdict | reason | replacement |
|---|---|---|---|
| `fab391fa14` | PASS | Header; columns fit the rows. | |
| `ed9f73f95d` | PASS | Art. 62.1 LGT verbatim; in the prose. | |
| `2199bd7683` | PASS | Art. 62.3 LGT, both paragraphs: «entre el día uno de septiembre y el 20 de noviembre o, si éste no fuera hábil, hasta el inmediato hábil siguiente», and the Administración «podrá modificar el plazo… siempre que dicho plazo no sea inferior a dos meses». Condition in the label; in the prose. | |
| `2cbb34af42` | PASS | Art. 62.4 LGT verbatim; in the prose. | |
| `4a2e1a9c14` | PASS | Header; columns fit the rows. | |
| `efdc37390b` | PASS | Art. 2 Orden HFP/311/2023, first two paragraphs, faithful (50.000 euros, both periods, the trabas proviso, the accumulation rule and its «salvo que estén debidamente garantizadas»). In the prose with that citation. Note for the coordinator: art. 2 applies to «las deudas a que se refiere el artículo anterior», and art. 1 excludes the deudas aduaneras of the CAU and those of disposición adicional undécima of Ley 16/2022; neither prose nor row says so, but that scope is another article, not the passage cited. | |
| `17453c2aa7` | PASS | Art. 48.2 RGR, first paragraph, verbatim; in the prose. | |
| `f6e133f270` | PASS | Art. 48.2 RGR, second paragraph: «…incluyendo el recargo del periodo ejecutivo correspondiente, los intereses de demora que genere el aplazamiento, más un 5 por ciento de la suma de ambas partidas». Quotation as in the prose. | |
| `65efa8ba0f` | PASS | Header; columns fit the rows. | |
| `148e01cf42` | PASS | Art. 46.6 RGR, first paragraph: 10 días «contados a partir del siguiente al de la notificación del requerimiento… con indicación de que, de no atender el requerimiento en el plazo señalado, se tendrá por no presentada la solicitud y se archivará sin más trámite». Faithful; in the prose. Note: the same apartado excludes subsanación when the missing document is the autoliquidación («procederá la inadmisión conforme a lo previsto en el artículo 47»); the prose states that inadmission under art. 47.1.a RGR, so the lesson is not wider than the norm. | |
| `cd6631f927` | PASS | Art. 48.5 RGR verbatim; in the prose. | |
| `d4afd97c80` | PASS | Art. 48.6 RGR: «La garantía deberá formalizarse en el plazo de dos meses contados a partir del día siguiente al de la notificación del acuerdo de concesión cuya eficacia quedará condicionada a dicha formalización.» Quotation as in the prose. | |
| `099abfd5d9` | PASS | Art. 52.1 RGR, quotation verbatim; in the prose. | |
| `4c96dab47f` | PASS | Art. 52.6 RGR: six months; «se podrá entender desestimada la solicitud a los efectos de interponer el recurso correspondiente o esperar la resolución expresa». In the prose. | |
| title m03-l09 «Otros plazos de pago en período voluntario» | PASS | «Otros» relative to the art. 62.2 LGT prose table right above; the rows are the remaining período voluntario plazos of art. 62.1, 62.3 and 62.4 LGT. | |
| title m03-l09 «Cobertura de la garantía y límite exento en el aplazamiento y fraccionamiento» | PASS | Accurate for the three rows. | |
| title m03-l09 «Plazos del aplazamiento y fraccionamiento» | FAIL | Selective: the plazos for filing the solicitud (art. 46.1 RGR, in the prose table of «Solicitud») and the consequences of not formalising the garantía in two months (art. 48.7 RGR) are left out. The title reads the five rows as all the plazos of the procedure. | Algunos plazos del aplazamiento y fraccionamiento |
