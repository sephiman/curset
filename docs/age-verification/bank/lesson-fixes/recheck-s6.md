# Lesson-fix recheck — session 6 (verifier 1, 2026-10-24)

Three edits re-checked under `lesson-fixes-check-brief.md`, judged from `git diff HEAD -- <lesson>` and the norm
(`pdftotext -layout`: LGSS 2026-10-03, RD 33/1986, LPAC 2024-11-06, LGP 2022-12-24, RD 829/2023). Checks: 1 Faithful,
2 Cited (`CourseCitations.build(...)._anchor(lesson, citation, 'es')`), 3 Placed and scoped, 4 Voice.

| # | Item | Lesson, lines | 1 | 2 | 3 | 4 | Verdict | Reason |
|---|---|---|---|---|---|---|---|---|
| a | Indemnización/demanda condition, causas 1.ª and 2.ª, art. 207.1 LGSS (m04 check item 6) | m04-l09, 150–156 | ✓ | ✓ | ✓ | ✓ | PASS | The requested wording is in place: «en cuyo caso exige además haber percibido la indemnización correspondiente o haber interpuesto demanda judicial en reclamación de dicha indemnización o de impugnación de la decisión extintiva», matching 207.1 final párrafo («En los supuestos contemplados en las causas 1.ª, 2.ª y 6.ª … será necesario que el trabajador acredite haber percibido la indemnización correspondiente … o haber interpuesto demanda judicial en reclamación de dicha indemnización o de impugnación de la decisión extintiva»). It is attached only to the two causes named, and «entre ellas» keeps the list open, so leaving out 6.ª is not wider. Age (four years under 205.1.a)), six months' inscription, 33 years without pagas extraordinarias all match 207.1.a)–c). `art. 207.1 LGSS` → `boe-a-2015-11724-art-207`. Only the cause clause changed. |
| b | Months in RD 33/1986 vs art. 30.4 LPAC (m04 check item 11) | m04-l06, 337–341 | ✓ | ✓ | ✓ | ✓ | PASS | The parenthesis is now «como el del pliego de cargos y el de las pruebas», so the two months read as examples and art. 49's third month («en el plazo máximo de un mes») is no longer excluded. Art. 35.1 («en un plazo no superior a un mes») and 37.1 («se dispondrá del plazo de un mes») match. «Tampoco tienen regla de cómputo propia» holds: the RD has none outside art. 7.2, which is limited to that article. The LPAC clause matches 30.4 («se computarán a partir del día siguiente a aquel en que tenga lugar la notificación o publicación … concluirá el mismo día … Si en el mes de vencimiento no hubiera día equivalente … el último día del mes»), and it does not apply the rule to the pliego month, which runs from the incoación. `art. 30.4 LPAC` → `boe-a-2015-10565-art-30`. |
| c | «(hoy: titular del Ministerio de Hacienda) (art. 5.1 RD 829/2023)» | m05-l02, 220 | ✓ | ✓ | ✓ | ✓ | PASS | The line now reads «El Ministro de Hacienda y Administraciones Públicas (hoy: titular del Ministerio de Hacienda) (art. 5.1 RD 829/2023) propone al Consejo de Ministros …» (HEAD l. 192 had «(hoy: Ministerio de Hacienda, art. 5.1 RD 829/2023)»). Art. 55.2 LGP names «El Ministro de Hacienda y Administraciones Públicas»; art. 5.1 RD 829/2023 gives the function («Corresponde al Ministerio de Hacienda la propuesta y ejecución de la política del Gobierno en materia de hacienda pública, de presupuestos y de gastos»). The «hoy» names a titular after a «Ministro», and the citation is its own parenthesis, as at l. 208 and l. 309. `art. 5.1 RD 829/2023` → `boe-a-2023-23537-art-5`; `art. 55.2 LGP` still → `boe-a-2003-21614-art-55`. |

Counts: 3 checked, PASS 3, FAIL 0.

## Notes (no verdict)

- (a) The 207.1 sentence now runs about 75 words. It still carries one idea (the requirements of one modality). If the
  coordinator wants it shorter, splitting before «entre ellas» with «Entre esas causas están el despido colectivo y el
  despido por causas objetivas; en ellas se exige además …» keeps the content and avoids the blacklisted openers.
