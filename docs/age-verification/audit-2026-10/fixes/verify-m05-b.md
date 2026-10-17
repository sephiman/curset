# R2b fixes, bloque V — blind verification, m05-l04 and m05-l06

Verifier: blind verifier B, 2026-10-17, per «Verifier (blind)» in `spec.md` (this folder). Share: every change to
`m05-l04` and `m05-l06` in `fix-m05.md` (m05-l02 and m05-l03 are verified in another report). Nothing edited but this
file; nothing committed.

Method. Lessons read as they stand (`git diff` against HEAD for the exact changes, then the whole section around each
change). Every cited article opened in the source file itself with `pdftotext -layout`: Ley 33/1987 art. 33
(`BOE-A-1987-28404_…`), Resolución de 20-01-2014 anexo IV art. 23 concepto 233 (`BOE-A-2014-879_…`, anexo IV starts
at the «ANEXO IV» heading; the concepto 233 text is under «Artículo 23. Indemnizaciones por razón del servicio»), RD
462/2002 art. 1.1.d) (`BOE-A-2002-10337_…`), LCSP arts. 118.3 and 243.1 párr. 2 (`BOE-A-2017-12902_…`), LGS art. 44.3
and título III heading (`BOE-A-2003-20977_…`), RLGS art. 56 (`BOE-A-2006-13371_…`). Ley 4/2026 (`BOE-A-2026-20528_…`)
checked: its only change to the LGS is DF 7, a new art. 2.4.j); it does not touch the LCSP, Ley 33/1987 or the RLGS, so
the LGS file's integrated future text does not affect art. 44.3. Every question named by the writer opened in the
questionnaire and its key read on the plantilla definitiva; tema and estado read in `docs/age-official-exams-ledger.md`.

## Results

| # | Lesson | Change | PASS/FAIL | Reason | Replacement (for FAIL) |
|---|---|---|---|---|---|
| 1 | m05-l04 | Coverage: art. 33.a)–c) Ley 33/1987 inserted after the art. 33 opening sentence, before 33.d) | PASS | Every element is in art. 33 as written: six months before junio or diciembre, the 182 (183 in bisiestos) or 183 days divisor, licencia sin retribución with the same reduction (33.b), change of puesto to another Administración without change of situación (33.c). Citations point to the right letters. Row conv2024_X sup. II reserva 2 (key c, «1 y 15 de diciembre» vs d «1 de julio y 15 de diciembre»): the missing fact the coverage report names, the six-month window before junio or diciembre, is now stated. The 33.d) sentence is word-for-word unchanged (only rewrapped). | |
| 2 | m05-l04 | Coverage: concepto 233 sentence + «Esas asistencias son las del artículo 1.1.d) RD 462/2002.»; introduction gains the Resolución de 20-01-2014 title | FAIL | First sentence PASS: concepto 233 text in anexo IV, art. 23 of the Resolución de 20-01-2014 is faithfully shortened («entre otros gastos» covers the omitted evaluaciones items), and it answers conv2022 sup. I reserva 2 (funcionaria teaching a curso de formación y perfeccionamiento, key b «233»). Title in the introduction matches the BOE title. The second sentence fails check (1): neither the Resolución (which does not mention RD 462/2002) nor art. 1.1.d) RD 462/2002 (which says nothing about concepto 233) states that the two lists are the same; the sentence asserts a link no article makes, the same kind of link the writer refused to write in m05-l03 change 2. The exam row does not need it. | Delete the sentence, so the paragraph ends: «… por participación en tribunales y por colaboración en centros de formación y perfeccionamiento del personal (anexo IV, art. 23, concepto 233, Resolución de 20-01-2014).» (rewrap the last line). Normativa unchanged: art. 1.1 RD 462/2002 stays cited in «Indemnizaciones por razón del servicio». |
| 3 | m05-l04 | «Lo que más cae» unchanged (9 lines) | PASS | Each new fact is asked by one question (conv2024_X sup. II reserva 2; conv2022 sup. I reserva 2); no rule requires a line. | |
| 4 | m05-l04 | Normativa: new line «Resolución de 20-01-2014 … anexo IV, artículo 23 (concepto 233).»; Ley 33/1987 line kept | PASS | Every newly cited article is on its line; «arts. 33 …» already covers 33.a)–d). Nothing became uncited. | |
| 5 | m05-l06 | Restore art. 118.3 LCSP under «El expediente de gasto», with pointer to m03-l04 | PASS | Text matches art. 118.3 («aprobación del gasto y la incorporación al mismo de la factura correspondiente, que deberá reunir los requisitos que las normas de desarrollo de esta Ley establezcan»). Questions exist and ask it: conv2020_X sup. I 1 (art. 118 LCSP, key a includes «aprobación del gasto y la incorporación de la correspondiente factura»), conv2020_X sup. II 13 (key a: aprobación de gasto, informe de necesidad, factura), conv2025_X sup. I 2 and 3 (options c: «compromiso de gasto» + documento O / proyecto, the distractor against 118.3). m03-l04 does carry the rest of art. 118 (118.1–5), so the pointer is good. Placed in the expediente section, before the 117.2 subsection: the subsection is a separate topic, so section order holds. | |
| 6 | m05-l06 | Restore art. 243.1 párr. 2 LCSP after the «Pago del precio» table | PASS | Three months from recepción, órgano de contratación, certificación final, abono a cuenta de la liquidación: all in art. 243.1 párr. 2 as written. conv2024_X sup. I 13 exists (supuesto I, key b) and option d («seis meses» for the certificación final) tests exactly this plazo. Placed after the 198.6 row, in LCSP order; the table's own 198.4 row already refers to 243.1. | |
| 7 | m05-l06 | Restore art. 56.1–3 RLGS (tramitación anticipada de la convocatoria) in «Procedimiento de gasto y pago» | FAIL | Content PASS: 56.1 (both circumstances a) and b), same-anualidad condition), 56.2 first sentence (cuantía estimada, condicionada a crédito) and 56.3 (certificado de la oficina presupuestaria) are faithful; the omitted 56.2 second sentence and 56.4 are whole facts. conv2020_X sup. I 12 exists and asks it (subvenciones in the 2023 PGE project; key c «No pueden convocarse durante el año 2022», ledger «Clave oficial discutida»): the lesson states the norm only and says nothing of the key. List form matches the lesson (as m05-l04's art. 1.1 list). Fails placement (spec, «Cuts restored»: in its place in the norm's order): the block sits between the art. 34.3 LGS paragraph and the art. 34.4 LGS paragraph, so it splits the LGS art. 34 run (34.1–3, then RLGS 56, then 34.4). | Move the three blocks unchanged (the «La convocatoria puede aprobarse …» paragraph, the a)/b) list and the «En estos casos …» paragraph) from after «… (art. 34.3 LGS).» to after the paragraph ending «… deben preverse expresamente en la normativa reguladora (art. 34.4 LGS).», immediately before «### Documentos contables de las subvenciones». No wording change. |
| 8 | m05-l06 | Restore art. 44.3 LGS as new subsection «### Control financiero de subvenciones» after «Reintegro» | PASS | Text is art. 44.3 verbatim except «esta ley» → «la LGS». Heading is the LGS título III name («Del control financiero de subvenciones»), so no invented term. conv2020_X sup. I 14 exists and asks it (key b: IGAE, sin perjuicio del Tribunal de Cuentas). Placed after Reintegro (arts. 37–42), in LGS order. Within the programme sentence «Gestión económica y financiera de subvenciones» (scope report lists it under S2 as programa anterior only, not as out of scope), so no «Fuera del enunciado» note is due. Ley 4/2026 does not change art. 44. | |
| 9 | m05-l06 | «Lo que más cae»: new line «En los contratos menores se requieren la aprobación del gasto y la incorporación de la factura (art. 118.3 LCSP).» | PASS | Asked by four questions (change 5), so the rule is met; block now 10 lines, the limit. Faithful to 118.3. Inserted as third line among the contract lines (the fix file says «line 10»; it means the count, not the position). Unwrapped like every other line of the block. | |
| 10 | m05-l06 | Normativa: LCSP + 118.3, 243.1; LGS + 44.3 (gloss now «(control financiero)»); RD 887/2006 «arts. 56.1–3 (tramitación anticipada) y 70.3 …» | PASS | Every newly cited article is listed; nothing listed is uncited. The LGS gloss moved from 42.4 to 44.3, the last article on the line, as the block does elsewhere. Wrap ≤ 120. | |

## Coverage re-check (no edit removed a covered fact)

- m05-l04: the 12 rows marked covered in `coverage/m05-l04.md` re-checked by searching each quoted passage in the lesson
  (line breaks joined): all 12 quotes are still present. The two rewrapped paragraphs keep every old word (`git diff
  --word-diff`: no deletion in either lesson outside the Normativa lines).
- m05-l06: `coverage/m05-l06.md` has no partial or miss; every change only adds text, so all covered rows stay covered.

## Form (check 5)

- Voice page: no filler, triad, rhetorical question, «no solo… sino», closer or hedge stack in the new prose. «También se
  reduce …» (m05-l04 change 1) carries a separate fact of its own letter, not the cut half of a sentence; left as is.
- Hard wrap ≤ 120 in all new prose lines (only tables, headings, the title line and «Lo que más cae» run longer, as before).
  No list marker mid-sentence. Cross-references bare (m03-l04, m05-l02). Peninsular Spanish.

## Counts

- Changes verified: 10 (m05-l04: 4; m05-l06: 6).
- PASS: 8.
- FAIL: 2 — m05-l04 #2 (unsupported linking sentence on art. 1.1.d) RD 462/2002), m05-l06 #7 (art. 56 RLGS placed
  inside the LGS art. 34 run).
- Questions opened: conv2024_X sup. II reserva 2, conv2022 sup. I reserva 2, conv2020_X sup. I 1, 12, 14, conv2020_X
  sup. II 13, conv2025_X sup. I 2, 3, conv2024_X sup. I 13 — all exist and ask the content the writer names.
- Coverage rows still covered: m05-l04 12/12; m05-l06 all.
