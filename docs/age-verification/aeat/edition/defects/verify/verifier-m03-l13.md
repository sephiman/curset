| Sentence | Verdict | Reason |
|---|---|---|
| S1 | PASS | Art. 191.4 párr. 1: "La infracción será muy grave cuando se hubieran utilizado medios fraudulentos." Stated condition is sufficient on its own; the second muy grave case (retenciones >50 %) is an additional case, not a missing condition. |
| S2 | FAIL | Restates only the first paragraph of art. 193.2 and omits its carve-out: "La infracción no será leve, cualquiera que sea la cuantía", when (a) false or falsified invoices, receipts or documents were used, or (b) incorrect bookkeeping exceeds 10 % of the base. Medios fraudulentos also make it muy grave in every case (193.3 last paragraph). As written, the sentence is false in those cases. |
| S3 | FAIL | Matches the first paragraph of art. 193.3 but omits the override in the same apartado: "La utilización de medios fraudulentos determinará que la infracción sea calificada en todo caso como muy grave." With a base above 3,000 euros, ocultación and medios fraudulentos, the infraction is muy grave, not grave. |
| S4 | PASS | Art. 193.4: "La infracción será muy grave cuando se hubieran utilizado medios fraudulentos." It is the only muy grave case in art. 193, so the sentence is true and complete. |

## Sentence ids of the passed sentences (S1 only; S2 and S3 failed and were replaced by the pool text)

| id | verdict |
|---|---|
| `aac8b3b344` | PASS |


# Fixes round 1, step 1 (blind check, opus)

# Fixes round 1, step 1: blind check report

Verifier: opus. Sources: the lessons as they now stand, `git show HEAD:` for the previous state, and `pdftotext -layout`
extractions of BOE-A-2015-11719 (TREBEP, 2026-10-03), BOE-A-2006-21990 (Ley 39/2006, 2026-11-11) and
BOE-A-2006-20764 (LIRPF, 2026-11-11). The extractions are in the session scratchpad `v1/`.

| place | verdict | reason |
|---|---|---|
| A. `m01-l07` «Término: suspensión provisional» | PASS | The definition matches art. 90.4 TREBEP ("con ocasión de la tramitación de un procedimiento judicial o expediente disciplinario") and art. 98.3 TREBEP (6 months as a medida cautelar in the expediente disciplinario, "salvo en caso de paralización del procedimiento imputable al interesado"). The section uses the term in exactly that sense: art. 98.3 duration and pay of the suspenso provisional, and the Clara case. |
| A. `m01-l01` (lesson as a whole) | PASS | The line has been removed from «Cuestión de inconstitucionalidad», where "suspensión provisional" meant the suspension of the judicial proceedings (art. 35.3 LOTC). The four «Término» lines left each match their section: personas con discapacidad / art. 49 CE row and paragraph; moción de censura / art. 114 CE dimisión; CGPJ / its 2 proposed TC members (art. 159.1 CE); Defensor del Pueblo / standing under art. 162.1.a CE. |
| B. `m01-l06` esquema art. 5.1 Ley 39/2006 | PASS | Rows labelled i) and ii), as in the norm. Row i) is verbatim. Row ii) is verbatim except that it drops the redundant closing clause ", por el que se aprueba el Reglamento…", which the row already names. No letter or number appears that the norm does not have at that place (the old «b)» label is gone). |
| C. `m03-l13` intro, last sentence | PASS | The «Lo que más cae» block has exactly ten bullets, and each is explained in the body (arts. 194.1, 180.3, 212.3.a, 179.2.a/e, 191.2, 187.1, 188.1.a/188.3, 189.1, 211.2/211.4, 208.1 LGT all appear before the block). The rest of the intro matches the lesson's sections and their order, including the worked example at «Ejemplo: graduación y reducciones de una sanción». |
| D. `m03-l14` «Recursos en vía económico-administrativa» / «Procedimiento abreviado» | PASS | Each table now appears once: «Plazos de interposición…» after the recursos section and «Plazos máximos para resolver…» in «Procedimiento abreviado». All 14 data rows and both header rows of the two removed tables («Algunos plazos…») are present word for word in the tables kept (checked mechanically, 16/16). The kept interposición table also has the extra row «Recurso contra la ejecución». No table row in the lesson is repeated. |
| E. `m03-l15` paragraph «En los períodos impositivos 2023, 2024, 2025 y 2026» | PASS | Sentence 1 quotes the DA 55.ª LIRPF word for word: the periods 2023–2026, the 1,1 por ciento "previsto en el artículo 85", the "revisados, modificados o determinados mediante un procedimiento de valoración colectiva de carácter general" condition, and "a partir de 1 de enero de 2012". Sentence 2 («esta regla sustituye a la de los diez períodos impositivos anteriores») does not mislead. In 2023–2026 the ten-period window of art. 85.1 (redacción vigente hasta el 31-12-2026) starts in 2013–2016, so every case it covers is also covered by "a partir de 1 de enero de 2012". Applying only the DA rule therefore gives the same result as applying both. Note: "sustituye" is the course's reading. The DA does not use the word, but it states no false idea. |

No FAIL, so no corrected text is proposed.

Optional note on E, not a FAIL: the second sentence does not say what the DA adds. In 2023, for example, a revision that took effect in 2012 is outside the ten periods but inside the DA. If the author wants that stated, a norm-grounded wording is: «En esos períodos el 1,1 por ciento se aplica, por tanto, también a los valores catastrales que entraron en vigor a partir de 1 de enero de 2012 aunque hayan transcurrido más de diez períodos impositivos.»


| id | verdict | note |
|---|---|---|
| `686174b630` | PASS | fixes round 1 step 1 |
| `aac8b3b344` | PASS | fixes round 1 step 1 |

Sentences checked word for word in the blind passes of round fixes-1 (reports 1-3 above for the 5 lessons of steps 2-3; step-1 report for earlier rows):

| id | verdict | note |
|---|---|---|
| `f6d0d1c485` | PASS | checked wording unchanged since the pass |
