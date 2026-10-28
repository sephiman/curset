# Coordinator edits — blind recheck (2026-10-23)

Three edits the coordinator made after the module checks (m05 #13, m05 note on l. 309, m03 #16). No writer record;
judged from `git diff HEAD -- <lesson>` and the norm, extracted with `pdftotext -layout` (Ley 31/2022 from the HTML).
Checks: 1 Faithful, 2 Cited (resolver `CourseCitations.build(...)._anchor(lesson, citation, 'es')`), 3 Placed and
scoped, 4 Voice.

| # | Item | Lesson, lines | 1 | 2 | 3 | 4 | Verdict | Reason |
|---|---|---|---|---|---|---|---|---|
| 1 | Formas de pago, apartado noveno.1 Orden PRE/1576/2002 | m05-l04, 316–320 | ✓ | ✓ | ✓ | ✓ | PASS | Restores both cheque conditions as the norm states them: «Excepcionalmente, cuando concurran circunstancias que lo justifiquen y sólo para las personas físicas, el Director General del Tesoro y Política Financiera podrá autorizar el pago mediante cheque nominativo no a la orden». Transferencia bancaria as the rule («se efectuará mediante transferencia bancaria») and «Asimismo, se podrán cancelar las obligaciones mediante pagos en formalización … que no producirán variaciones efectivas de tesorería» match. The Dirección General del Tesoro y Política Financiera still exists (art. 15.A).1.º RD 1009/2023: «de la que dependen la Dirección General del Tesoro y Política Financiera»), so no «(hoy: …)» is owed. `apartado noveno.1 Orden PRE/1576/2002` → `boe-a-2002-12506-apartado-noveno`. Three sentences, one fact each; no blacklisted opener («también» is mid-sentence). |
| 2 | «(hoy: titular del Ministerio de Hacienda) (art. 5.1 RD 829/2023)» | m05-l02, 309–311 | ✓ | ✓ | ✓ | ✓ | PASS | Ley 31/2022 art. 9.Dos is quoted as written («corresponden a la persona titular del Ministerio de Hacienda y Función Pública»). The «hoy» now names a titular after «La persona titular», and art. 5.1 RD 829/2023 covers the function («Corresponde al Ministerio de Hacienda la propuesta y ejecución de la política del Gobierno en materia de hacienda pública, de presupuestos y de gastos»). It is the first mention of that name in the lesson. The citation is now its own parenthesis and resolves to `boe-a-2023-23537-art-5` (it resolved to None before). The two adjacent parentheses match the l. 208 table row («(hoy: titular del Ministerio de Economía, Comercio y Empresa) (art. 60.1 LGP; …)»). The rest of the sentence is unchanged; `art. 9.Dos.6` and `art. 10.Uno Ley 31/2022` still resolve. |
| 3 | Observatorio, art. 20 RD 829/2023 removed | m03-l07, 96–98 | ✓ | ✓ | ✓ | ✓ | PASS | Against HEAD the only change is the deleted «, art. 20 del Real Decreto 829/2023, … RD 829/2023» inside the «hoy». The two art. 20.1–2 sentences that the m03 check failed are gone, and the paragraph ends at «(art. 30.1 LO 1/2004).». Art. 30.1 LO 1/2004: «como órgano colegiado adscrito al Ministerio de Trabajo y Asuntos Sociales, al que corresponderá el asesoramiento, evaluación, colaboración institucional, elaboración de informes y estudios, y propuestas de actuación en materia de violencia de género», matched. «(hoy: Ministerio de Igualdad)» follows decision 1: art. 20.1 RD 829/2023 gives it «la erradicación de toda forma de discriminación», and art. 20.2 gives it the «Secretaría de Estado de Igualdad y para la Erradicación de la Violencia contra las Mujeres». It is left uncited, as in the I.8 precedent. The Normativa line «art. 20 (Ministerio de Igualdad)» (l. 222) stays. `art. 30.1 LO 1/2004` → `boe-a-2004-21760-art-30`. |

Counts: 3 checked, PASS 3, FAIL 0.

## Notes (no verdict)

- Item 1, optional: the m05-l04 sentence leaves out the norm's «a conceptos del Presupuesto de ingresos y a conceptos no
  presupuestarios». That is not wrong, because the sentence points to m05-l03 (l. 165–167), which states the full rule.
  If you want parity, use: «Las obligaciones también pueden cancelarse mediante pagos en formalización a conceptos del
  Presupuesto de ingresos y a conceptos no presupuestarios, que no producen variaciones efectivas de tesorería (apartado
  noveno.1 Orden PRE/1576/2002; m05-l03).»
- Outside the three items: m05-l02 l. 220 still has the old form, «El Ministro de Hacienda y Administraciones Públicas
  (hoy: Ministerio de Hacienda, art. 5.1 RD 829/2023)». It has the same two defects l. 309 had: the citation sits
  inside the «hoy», and the note names a ministry after a «Ministro». Suggested: «El Ministro de Hacienda y
  Administraciones Públicas (hoy: titular del Ministerio de Hacienda) (art. 5.1 RD 829/2023) propone …».
- `citations.es.txt` is frozen and was not regenerated. It has no m05-l04 `apartado-noveno` row and no m05-l02 body row
  for `boe-a-2023-23537-art-5`. The frozen golden test will show both new citations when the goldens are next
  regenerated.
- Tests (from `backend/`): `tests/test_esquema.py` passed (10). `tests/test_citations.py -k "not frozen"` gave 56
  passed and 4 setup errors. All 4 errors are `docker.errors.DockerException` (no Docker socket in this session), not
  content failures.
