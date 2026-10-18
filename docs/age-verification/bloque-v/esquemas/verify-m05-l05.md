# Verification — esquemas of m05-l05 (blind review, 2026-10-18)

Read: `spec.md` (this folder), the `::esquema` section of `docs/platform-delta-handoff.md`, `git diff` of
`content/age-administrativo-c1/es/lessons/m05-l05.md` (three `:::esquema` blocks added, prose unchanged), the prose of
the lesson at lines 228–250 and 321–409, and the `esquema` rows of `citations.es.txt` (every row citation resolves to
the cited article: RD 725/1989 art. 7, RD 640/1987 arts. 10 and 12, LGP art. 79; «art. 12.1 y 12.3 RD 640/1987»
resolves to art. 12).

Sources (scratchpad `txt/`, pdftotext of `C/sources/normativa/`, read with `art.py`):
`BOE-A-1989-14441_rd-725-1989-caja-fija_2026-10-08` (art. 7), `BOE-A-1987-12158_rd-640-1987-pagos-justificar_2026-10-08`
(arts. 10, 12), `BOE-A-2003-21614_lgp_2022-12-24` (art. 79).

Result: 15 rows, 14 PASS, 1 FAIL.

## Esquema 1 — pasos «Las cuentas de los anticipos de caja fija, hasta el Tribunal de Cuentas» (lines 252–258)

| # | row (short) | citation | PASS/FAIL | passage / reason | replacement |
|---|---|---|---|---|---|
| 1 | Rendición — Cajeros pagadores, a medida que necesidades de tesorería aconsejen la reposición y, necesariamente, en diciembre | art. 7.1 RD 725/1989 | PASS | «Los Cajeros pagadores rendirán cuentas por los gastos atendidos con anticipos de Caja fija a medida que sus necesidades de tesorería aconsejen la reposición de los fondos utilizados y, necesariamente, en el mes de diciembre de cada año.» Verbatim; the omitted sentence (estructura fijada por la IGAE) carries no condition. Prose l. 230–231. | — |
| 2 | Aprobación — Jefes de las Unidades Administrativas o, si la organización lo requiere, Órganos centrales | art. 7.2 RD 725/1989 | PASS | «Las indicadas cuentas, acompañadas de las facturas y demás documentos originales que justifiquen la aplicación de los fondos, debidamente relacionados, serán aprobadas por los Jefes de las Unidades Administrativas a las que las Cajas estén adscritas. En los casos en que la organización administrativa lo requiera, las cuentas podrán ser aprobadas por los Órganos centrales…» Condition kept. Prose l. 231–234 (same shortening). | — |
| 3 | Examen — Intervención delegada, central o territorial; muestreo; informe a los Jefes que aprobaron | art. 7.4 RD 725/1989 | PASS | «La Intervención delegada, central o territorial, que corresponda a la Unidad que apruebe las cuentas examinará éstas y los documentos que las justifiquen, pudiendo utilizar procedimientos de muestreo de acuerdo con las instrucciones que al efecto dicte la IGAE. El órgano de control emitirá informe en el que pondrá de manifiesto los defectos o anomalías observadas o su conformidad con la cuenta. Dicho informe, junto con la cuenta, será remitido a los Jefes…» Same shortening as prose l. 243–245 (both drop «de acuerdo con las instrucciones… IGAE»; see Notes). | — |
| 4 | Alegaciones y subsanación si el informe señala defectos — quince días, antes de remitir al TCu; cuenta al Interventor en quince días — órgano gestor | art. 7.4 RD 725/1989 | PASS | «Caso de que en el informe se hagan constar defectos o anomalías, el Órgano gestor, en un plazo de quince días, realizará las alegaciones que estime oportunas, y, en su caso, las subsanará, dejando constancia de ello en la cuenta, antes de su remisión al Tribunal de Cuentas. De estas actuaciones se dará cuenta al Interventor en el plazo de quince días.» Both plazos, the condition and «en su caso» kept. Prose l. 245–247 (same «defectos» for «defectos o anomalías»). | — |
| 5 | Envío al Tribunal de Cuentas — Jefes de las Unidades que la aprobaron | art. 7.4 RD 725/1989 | PASS | «…será remitido a los Jefes de las Unidades Administrativas que aprobaron la cuenta para su conocimiento, y envío de ésta al Tribunal de Cuentas.» Prose l. 245. | — |

## Esquema 2 — pasos «La cuenta justificativa de los pagos a justificar» (lines 411–417)

| # | row (short) | citation | PASS/FAIL | passage / reason | replacement |
|---|---|---|---|---|---|
| 1 | Formación y rendición — debe/haber, facturas y documentos originales, carta de pago del reintegro — Cajeros pagadores | art. 12.1 y 12.3 RD 640/1987 | PASS | 12.1: «En las cuentas justificativas de la inversión figurará en el debe el importe percibido y en el haber el de las obligaciones satisfechas con cargo a aquél. La cantidad no invertida será justificada con la carta de pago demostrativa de su reintegro. A las indicadas cuentas se acompañarán debidamente relacionadas las facturas y demás documentos originales…»; 12.3: «Las cuentas se formarán y rendirán por los Cajeros pagadores…». Prose l. 388–392 and 394. The prose states the carta de pago with art. 79.3 LGP, not 12.1; 12.1 carries it verbatim and the prose already cites 12.1, so no new citation. | — |
| 2 | Conformidad y remisión a la Unidad Central — Jefes de las Unidades Administrativas | art. 12.3 RD 640/1987 | PASS | «…se conformarán por los Jefes de las Unidades Administrativas a las que las Cajas estén adscritas, quienes para su comprobación y tramitación posterior las remitirán a la Unidad Central…» Prose l. 394–395. | — |
| 3 | Intervención de la inversión — auditoría o muestreo; devolución a la Unidad Central con informe — Intervención Delegada | art. 12.4 RD 640/1987 | PASS | «La Intervención Delegada realizará la intervención de la inversión examinando las cuentas y los documentos que las justifiquen mediante procedimientos de auditoria o de muestreo. Examinadas las cuentas se devolverán a la Unidad Central… con el informe correspondiente.» Prose l. 395–397. | — |
| 4 | Aprobación, si procede — recabada por la Unidad Central — autoridad que dispuso la expedición | art. 12.5 RD 640/1987 | PASS | «Recibidas las cuentas por la Unidad Central, ésta procederá: a) A recabar, si procede, la aprobación de las mismas por la autoridad que dispuso la expedición de las correspondientes órdenes de pago.» «si procede» kept. Prose l. 397–398. | — |
| 5 | Envío al TCu — cuentas aprobadas; en OOAA, a elección del Tribunal, en poder del Organismo — Unidad Central | art. 12.5 RD 640/1987 | PASS | «b) Aprobadas las mismas las enviará al Tribunal de Cuentas. En los Organismos autónomos, las cuentas justificativas podrán, a elección del Tribunal de Cuentas, quedar en poder del Organismo a disposición del Tribunal o enviarlas al mismo.» Prose l. 398–400 uses the same «a su disposición». See Notes (optional wording). | — |

## Esquema 3 — tabla «Plazos de la cuenta justificativa de los pagos a justificar» (lines 419–427)

| # | row (short) | citation | PASS/FAIL | passage / reason | replacement |
|---|---|---|---|---|---|
| 1 | LGP, en general — tres meses — excepcionalmente a seis (Ministro…, a propuesta del órgano gestor, con informe) | art. 79.4 LGP | PASS | «El plazo de rendición de las cuentas será de tres meses, excepto las correspondientes a pagos de expropiaciones y pagos en el extranjero… El Ministro, o en quien éste delegue, y, en su caso, los presidentes o directores de los organismos autónomos del Estado y de las entidades gestoras y servicios comunes de la Seguridad Social podrán, excepcionalmente, ampliar estos plazos a seis y doce meses respectivamente, a propuesta del órgano gestor del crédito y con informe de sus respectivas Intervenciones.» «En general» is a label; the exception sits in the next row. Prose l. 366–370. | — |
| 2 | LGP, expropiaciones y extranjero — seis meses — «excepcionalmente, a doce meses, por los mismos órganos y con los mismos trámites» | art. 79.4 LGP | FAIL | Meaning is right, but «con los mismos trámites» is wording neither in the article nor in the prose: it rewords «a propuesta del órgano gestor del crédito y con informe de sus respectivas Intervenciones». The rule asks for a verbatim fragment or faithful verbatim shortening. Prose l. 367–370 states every clause needed. | Ampliación cell: «Excepcionalmente, a doce meses: el Ministro, o en quien delegue, y, en su caso, los presidentes o directores de los organismos autónomos del Estado y de las entidades gestoras y servicios comunes de la Seguridad Social, a propuesta del órgano gestor del crédito y con informe de sus Intervenciones» (no clause the prose lacks). |
| 3 | RD 640/1987, Cajeros pagadores — mes siguiente a la inversión y en todo caso tres meses desde la percepción — excepcionalmente hasta seis (DG Tesoro, Presidentes/Directores OOAA) | art. 10.1 RD 640/1987 | PASS | «…dentro del mes siguiente a la inversión de las mismas y en todo caso en el plazo de tres meses desde la percepción de los correspondientes fondos, sin perjuicio de lo que al efecto establece el artículo 11… El Director general del Tesoro y Política Financiera y, en su caso, los Presidentes o Directores de los Organismos autónomos del Estado podrán, excepcionalmente, ampliar este plazo hasta seis meses.» The «sin perjuicio» points to art. 11, derogated, so dropping it narrows nothing. Prose l. 372–375. | — |
| 4 | RD 640/1987, FSE y expropiaciones — seis meses — prorrogable un año más; solicitudes a la DGTPF | art. 10.2 RD 640/1987 | PASS | «…los pagos «a justificar» correspondientes a créditos del Fondo Social Europeo y a expropiaciones tendrán un plazo de seis meses, prorrogable en un año más, cuando ello sea necesario, para rendir las cuentas justificativas de su inversión. … en caso necesario, el órgano gestor del crédito, con informe de la Intervención Delegada remitirá las solicitudes de ampliación de plazo a la Dirección General del Tesoro y Política Financiera para su aprobación.» Prose l. 375–379 (both leave out the fecha límite set by Ministerios u Organismos, which is not a condition of the plazo). | — |
| 5 | LGP, aprobación o reparo — dos meses desde la aportación de los justificantes | art. 79.6 LGP | PASS | «En el curso de los dos meses siguientes a la fecha de aportación de los documentos justificativos … se llevará a cabo la aprobación o reparo de la cuenta por la autoridad competente.» Prose l. 400–401. | — |

## Order

- Esquema 1: 1→2 (7.2 «Las indicadas cuentas» are those rendered under 7.1); 2→3 (7.4: the Intervención «que corresponda a la
  Unidad que apruebe las cuentas»; its informe goes «a los Jefes… que aprobaron la cuenta», so approval comes first); 3→4
  (alegaciones respond to «el informe»); 4→5 (alegaciones and subsanación «antes de su remisión al Tribunal de Cuentas»). No
  false order. Step 4 is conditional and its label says so («si el informe señala defectos»).
- Leaving art. 7.3 out of esquema 1 is correct. The title scopes the list to the path of the cuenta up to the Tribunal de
  Cuentas, and 7.3 (documentos contables a favor del Cajero, checked by the Intervención for matching totals) runs «con
  independencia del resultado del examen fiscal»: it is a parallel track, not a step between 2 and 3 or after 5. Putting
  it in the stepper would claim an order the article denies. Since the reposición is not named in the title, the list
  does not read as the complete reposición procedure, and the prose paragraph on 7.3 (l. 236–241) sits directly above. The
  last párrafo of 7.4 (medidas legales and reintegro if defects are not corrected) is also absent from prose and esquema;
  the title stops at the Tribunal, so the list does not claim to cover it.
- Esquema 2: 12.3 (Cajeros → Jefes → Unidad Central) → 12.4 (Intervención Delegada, returns to the Unidad Central) → 12.5
  («Recibidas las cuentas por la Unidad Central»: a) aprobación, b) «Aprobadas las mismas las enviará al Tribunal»). Every
  step follows the one before in the article. No false order.
- Esquema 3 is a `tabla`, so it claims no order. Using `tabla` instead of `plazos` is right here: the LGP and RD 640/1987
  rules for the same act sit side by side, one row per norm, and the table does not say which applies (spec rule).

## Placement

- Esquema 1 (l. 252) follows the paragraphs it summarises (l. 230–247), with one paragraph in between (l. 249–250, art.
  9.1 estados de situación de Tesorería), which the esquema does not summarise. Acceptable; placing it before l. 249 would
  sit tighter, but this is not a FAIL.
- Esquema 2 (l. 411) follows l. 388–401, under «Las cuentas justificativas». The IOC paragraph (l. 403–409) is in between and
  cannot become a row (platform limit on «regla … IOC»). Fine.
- Esquema 3 (l. 419) summarises «Plazos de la cuenta justificativa» (l. 366–379) plus art. 79.6 LGP (l. 400–401). It comes
  after both, so it does follow its paragraphs, but it sits under the heading «Las cuentas justificativas» rather than the
  «Plazos» subsection. Defensible because of row 5. Alternative if the writer prefers: move the table to after l. 384
  and drop row 5. Not a FAIL.

## Notes

- No esquema repeats a list or table already in the prose: the three summarise running paragraphs.
- Esquema 1 row 3 and prose l. 243–244: both drop «de acuerdo con las instrucciones que al efecto dicte la IGAE» from the
  muestreo clause. It reads as a framework reference rather than a condition that widens the fact, so it is not counted as a
  gap. Listed so the ledger can decide.
- Esquema 1 row 4 and prose l. 245: «defectos» for the article's «defectos o anomalías» narrows the trigger slightly; it is
  in both, so the row matches the prose. A ledger candidate, not a FAIL.
- Esquema 2 row 5 and prose l. 399–400: «quedar en poder del Organismo a su disposición» can be read as the Organismo's
  disposal; the article says «a disposición del Tribunal». Optional: «a disposición del Tribunal» in the row (verbatim, and
  the prose's «su» refers to the Tribunal). The same wording in the prose is outside this round's scope (prose not touched).
- Esquema 2 row 1 joins 12.1 (content of the cuenta) and 12.3 (who forms it) into one step with a two-apartado citation;
  it resolves to art. 12 in `citations.es.txt`.
