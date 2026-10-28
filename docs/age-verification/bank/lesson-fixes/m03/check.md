# Lesson fixes, m03 (bloque III): blind check, 2026-10-23 (session 5)

Checked from `git diff HEAD -- content/age-administrativo-c1/es/lessons/m03-l0{3..7}.md` and from the norms, read with
`pdftotext -layout` from `sources/normativa/` (LPAC `…_2024-11-06`, LRJSP `…_2024-08-02`, LJCA `…_2025-01-03`, LOPJ
`…_2025-02-17`, Código Civil `…_2025-01-03`, LCSP `…_2026-04-09`, LO 1/2004 `…_2022-09-07`, RD 829/2023 `…_2023-12-29`,
RD 1009/2023 `…_2026-07-29`, LO 1/2025 `…_2025-06-04`). None has `cambios_pendientes`. LO 1/2025 art. 21 amends LJCA
arts. 11.1.a), 19.1, 45.2, 74.8 and 78 only, and art. 1 does not touch art. 185 LOPJ, so arts. 6 and 128 LJCA and 185
LOPJ are read as in the files. Every citation below was run through `CourseCitations.build(...)._anchor(lesson,
citation, 'es')` from `backend/`; all 19 resolve. Line numbers are those of the lesson files now.

Checks: F faithful, C cited, P placed and scoped, V voice.

| # | Item | Lesson, lines | F | C | P | V | Verdict | Reason |
|---|---|---|---|---|---|---|---|---|
| 1 | Art. 13 LRJSP, suplencia | m03-l03, 52–56 | ✓ | ✓ | ✓ | ✓ | PASS | 13.1 «podrán ser suplidos temporalmente en los supuestos de vacante, ausencia o enfermedad, así como en los casos en que haya sido declarada su abstención o recusación. Si no se designa suplente, … por quien designe el órgano administrativo inmediato superior»; 13.2 «para su validez no será necesaria su publicación». Each half cited to its apartado; sits after delegación in «Competencia». |
| 2 | Art. 30.2–3 LRJSP, start of prescription | m03-l03, 105–108 | ✓ | ✓ | ✓ | ✓ | PASS | 30.2 «desde el día en que la infracción se hubiera cometido … continuadas o permanentes … desde que finalizó la conducta infractora»; 30.3 «desde el día siguiente a aquel en que sea ejecutable la resolución … o haya transcurrido el plazo para recurrirla». Interruption rules and the 30.3 párr. 3 alzada-presunta start are left out; they are separate rules the item did not ask, and the general rule stated is not contradicted by them. |
| 3 | Art. 93.2 LRJSP, «(hoy: …)» | m03-l03, 148–150 | ✓ | ✓ | ✓ | ✓ | PASS | Norm's words kept («a propuesta conjunta del Ministerio de Hacienda y Administraciones Públicas»); first mention in the lesson; the «hoy» name matches the I.8 precedent for the same old name in the same law (m01-l08 l. 23–26) and art. 22.2 RD 829/2023 («administración pública, función pública, y gobernanza pública»). |
| 4 | Art. 95.3 párr. 2 LPAC | m03-l03, 298–301 | ✓ | ✓ | ✓ | ✓ | PASS | «podrán incorporarse a éste los actos y trámites cuyo contenido se hubiera mantenido igual … En todo caso, en el nuevo procedimiento deberán cumplimentarse los trámites de alegaciones, proposición de prueba y audiencia al interesado.» Joined after the 95.3 párr. 1 sentence. |
| 5 | Art. 96.5 LPAC | m03-l03, 303–305 | ✓ | ✓ | ✓ | ✓ | PASS | «se podrá adoptar la tramitación simplificada … cuando el órgano competente para iniciar … considere que … existen elementos de juicio suficientes para calificar la infracción como leve, sin que quepa la oposición expresa por parte del interesado prevista en el apartado 2.» Dropping «prevista en el apartado 2» narrows nothing. Placed before the 96.6 sentence. |
| 6 | Art. 106.3 LPAC, inadmisión | m03-l03, 333–337 | ✓ | ✓ | ✓ | ✓ | PASS | All three grounds kept: not based on an art. 47.1 cause, «carezcan manifiestamente de fundamento», «se hubieran desestimado en cuanto al fondo otras solicitudes sustancialmente iguales»; «motivadamente» and «sin necesidad de recabar Dictamen» kept. Between 106.1 and 106.5. |
| 7 | Art. 6 LJCA now anchored | m03-l03, 438–441 | ✓ | ✓ | ✓ | ✓ | PASS | The five organs of art. 6 a)–e), none missing. `art. 6 LJCA` → `boe-a-1998-16718-art-6`. Placed at the head of the section, right before the DA 1.ª LO 1/2025 paragraph that reads those references; art. 6 not amended by LO 1/2025. |
| 8 | Art. 128.2 LJCA, August | m03-l03, 452–454 | ✓ | ✓ | ✓ | ✓ | PASS | «Durante el mes de agosto no correrá el plazo para interponer el recurso contencioso-administrativo ni ningún otro plazo de los previstos en esta Ley salvo para el procedimiento para la protección de los derechos fundamentales en el que el mes de agosto tendrá carácter de hábil.» After the 46.1 plazos. |
| 9 | Month counting in the contencioso | m03-l03, 456–458 | ✓ | ✓ | ✓ | ✓ | PASS | Art. 185.1 LOPJ «Los plazos procesales se computarán con arreglo a lo dispuesto en el Código Civil»; art. 5.1 CC «se computarán de fecha a fecha. Cuando en el mes del vencimiento no hubiera día equivalente al inicial del cómputo, se entenderá que el plazo expira el último del mes». Citing both is right: art. 5.1 alone does not reach the contencioso. |
| 10 | Normativa | m03-l03, 499–504 | ✓ | — | ✓ | ✓ | PASS | Adds LRJSP 13.1–13.2 and 30.1–30.3, CC 5.1, LOPJ 185.1 and LJCA 128.2: each matches a citation added in the body; nothing else changed. |
| 11 | Art. 29.7 párr. 3 LCSP | m03-l04, 103–106 | ✓ | ✓ | ✓ | ✓ | PASS | All four conditions kept: requisitos del art. 118, «su duración no exceda de 30 meses», exceso «justificado exclusivamente por la duración del período de garantía … y los trabajos relacionados con la liquidación». Joined right after the 29.8 one-year rule it qualifies. |
| 12 | Art. 89.1 LPAC, archivo without propuesta | m03-l05, 95–104 | ✓ | ✓ | ✓ | ✓ | PASS | Lead-in and letters a)–e) match the norm word for word («se ponga de manifiesto que concurre» → «se ponga de manifiesto», same meaning). A list, as the lesson already does for 29.3 LRJSP; placed after 85 in «El procedimiento sancionador». |
| 13 | Art. 25.1.b) LPAC, caducidad | m03-l05, 106–109 | ✓ | ✓ | ✓ | ✓ | PASS | «En los procedimientos en que la Administración ejercite potestades sancionadoras o, en general, de intervención, susceptibles de producir efectos desfavorables o de gravamen, se producirá la caducidad. En estos casos, la resolución que declare la caducidad ordenará el archivo de las actuaciones, con los efectos previstos en el artículo 95.» Overlaps m03-l03 l. 230–231 but carries the archivo clause and sits in the sancionador procedure the item filed it to. |
| 14 | Normativa | m03-l05, 186 | ✓ | — | ✓ | ✓ | PASS | Adds LPAC 25.1 and 89.1, matching the body. |
| 15 | Art. 68.1 LPAC, subsanación | m03-l06, 161–164; Normativa 238 | ✓ | ✓ | ✓ | ✓ | PASS | «Si la solicitud de iniciación no reúne los requisitos que señala el artículo 66, y, en su caso, los que señala el artículo 67 … diez días … se le tendrá por desistido de su petición, previa resolución … en los términos previstos en el artículo 21.» Placed after the 67.2 contents it applies to. Note: the sentence is word for word the one in m03-l03 l. 245–247; acceptable because the item asked for it in m03-l06's procedure. |
| 16 | Observatorio, citation of art. 20 RD 829/2023 | m03-l07, 96–103 | ✓ | ✓ | ✗ | ✗ | FAIL | The fix is right in removing art. 20 from the «hoy» (art. 30.1 LO 1/2004 «adscrito al Ministerio de Trabajo y Asuntos Sociales»; no norm in sources states the present adscripción). But it then adds two new sentences on the Ministerio de Igualdad's general competences and órgano superior (art. 20.1–20.2 RD 829/2023), which are not about the Observatorio and go beyond a correction. The I.8 precedent keeps the «hoy» uncited and lists the RD article in Normativa only (m01-l08: «hoy: Ministerio para la Transformación Digital…», Normativa «arts. 1 y 22», no body citation of art. 22); the Normativa line «art. 20 (Ministerio de Igualdad)» already does that here. «Su órgano superior» also reads as the RD's, its grammatical antecedent. |

**Fix for #16 (one line):** in m03-l07 delete the two sentences from «El Real Decreto 829/2023, de 20 de noviembre, por el
que se reestructuran…» to «…contra las Mujeres (art. 20.2 RD 829/2023).», so the paragraph ends «…en materia de violencia
de género (art. 30.1 LO 1/2004).»; leave the Normativa line «RD 829/2023 (departamentos ministeriales): art. 20
(Ministerio de Igualdad).» as it is.

## Items not done

| Item | Reason given | Verdict | Check |
|---|---|---|---|
| m03-l04, art. 98 RGLCAP | RGLCAP not in sources | True | No RD 1098/2001 file in `sources/normativa/`, no entry in `sources/normativa.yaml`, no mention in `sources/otros/`. |
| m03-l05, arts. 47.1, 48, 49, 51, 123 LRJSP | Already in m03-l03; art. 48 answers no question | True | m03-l03 l. 113–144 states 47.1 (definition, protocolos), 49.h) (four years, unanimous prórroga up to four more), 51.1–2 (extinción and the a)–e) causes), 53.1 and 123.1–2.a)–b). The filed questions are answered there: conv2025_A·S2·13 (key c, 49.h), ·14 (key b, «acuerdo unilateral» is not a 51.2 cause), conv2024_A·S2·7 (key d, convenio, 47.1), ·8 (key d, 49.h), conv2025_X·S2 reserva 5 (key d, 123.2.a). A search of every official questionnaire in sources finds no question on art. 48 (perfeccionamiento, REOICO, requisitos). |

## Counts

- Items checked: 16. PASS 15, FAIL 1 (#16, m03-l07 Observatorio: scope and voice).
- Not-done items: 2, both reasons true.
- `uv run pytest tests/test_esquema.py tests/test_citations.py -q -k "not frozen"`: 66 passed, 4 errors; the 4 errors
  are Testcontainers tests that could not reach Docker from this session (`ConnectionError` fetching the server API
  version), not content failures.
