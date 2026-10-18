# Blind verification — m05-l02, m05-l04, m05-l06 (prose fixes and new esquema rows), 2026-10-18

Reviewer did not write the changes. No lesson or content file was edited.

Read: `docs/age-verification/bloque-v/esquemas/spec.md`, the `::esquema` section of `docs/platform-delta-handoff.md`,
`docs/prose-voice.md`, `CLAUDE.md`, `git diff -- C/es/lessons/` (m05-l02, m05-l04, m05-l06) and
`git diff -- C/citations.es.txt`, plus the surrounding prose of each lesson (m05-l02 l. 312–341, m05-l04 l. 206–220 and
240–256, m05-l06 l. 102–131).

Sources (scratchpad `txt/`, never memory): Ley 31/2022 (BOE-A-2022-22128, `ley31.txt`, tag-stripped HTML) art. 1.a),
art. 10 (apartado Seis) and art. 23.Uno.B and D; LGP (BOE-A-2003-21614) art. 58; LGS (BOE-A-2003-20977) art. 34. The
HTML anchors were checked in the source file: `#a1-2` opens «Artículo 10. De las limitaciones presupuestarias.»,
`#a2-5` opens «Artículo 23. Retribuciones de los funcionarios del Estado …». LGS PDF page 35 holds the heading
«Artículo 34. Procedimiento de aprobación del gasto y pago.».

Ley 31/2022 art. 10 carries the note «Se añade un apartado 4 y los actuales 4, 5 y 6 se renumeran como 5, 6 y 7 por la
disposición final 12.1 del Real Decreto-ley 7/2026». In the consolidated text in force the incorporation rule is
apartado Seis, so «art. 10.Seis» is the right citation.

## m05-l02 — prose on art. 10.Seis Ley 31/2022 (l. 325–330)

Norm, art. 10.Seis: «Durante la vigencia de estos presupuestos no se podrán incorporar los remanentes de créditos
derivados de generaciones aprobadas en el ejercicio anterior, quedando por tanto sin efecto lo previsto en la letra b)
del artículo 58 de la Ley 47/2003 … Esta restricción no afectará a los remanentes de créditos que se hubieran generado en
el servicio 50 «Mecanismo de Recuperación y Resiliencia» de cada sección, así como el resto de los créditos vinculados al
Mecanismo de Recuperación y Resiliencia consignados en los presupuestos de gastos de las entidades referidas en los
apartados 2.º, 3.º y 4.º de la letra a) del artículo 1 de la presente ley. A estas incorporaciones les será de
aplicación, respecto a su financiación, lo previsto en el artículo 42 del Real Decreto-ley 36/2020 …»

| # | sentence (short) | citation | PASS/FAIL | passage / reason | replacement |
|---|---|---|---|---|---|
| 1 | Durante la vigencia de la Ley 31/2022 no se pueden incorporar los remanentes de generaciones aprobadas en el ejercicio anterior, y queda sin efecto la letra b) | art. 10.Seis Ley 31/2022 | PASS | First sentence of art. 10.Seis, verbatim shortening. «la letra b)» follows the list of art. 58 LGP (l. 317–323), so it reads as art. 58.b) LGP. «estos presupuestos» → «la Ley 31/2022» is the lesson's existing usage. Voice: one fact, no filler. | — |
| 2 | La restricción no afecta a los remanentes del servicio 50 «MRR» de cada sección, ni al resto de créditos vinculados al MRR de las entidades de los apartados 2.º, 3.º y 4.º del art. 1.a) | art. 10.Seis Ley 31/2022 | PASS | Second sentence of art. 10.Seis, verbatim («así como» → «ni», correct after a negation). Both exceptions and the three apartados are kept; nothing wider. The omitted third sentence (financing under art. 42 RDL 36/2020) states how the excepted incorporations are financed; it is not a condition of the exception, so its absence does not widen the sentence. Long sentence, but one idea; the repeated «Mecanismo de Recuperación y Resiliencia» follows the voice page (no synonym rotation). Peninsular Spanish. | — |

## m05-l02 — tabla «Qué es cada modificación de crédito», new row (l. 340)

| # | row (short) | citation | PASS/FAIL | passage / reason | replacement |
|---|---|---|---|---|---|
| 1 | Incorporación, durante la vigencia de la Ley 31/2022 — no se incorporan remanentes de generaciones del ejercicio anterior, sin efecto la letra b) del art. 58 LGP; no afecta al servicio 50 MRR ni al resto de créditos MRR de los apartados 2.º–4.º del art. 1.a) | art. 10.Seis Ley 31/2022 | PASS | Same passage as above; the cell repeats prose l. 325–330 word for word, adding «del artículo 58 LGP», which is the norm's own «letra b) del artículo 58 de la Ley 47/2003». The label carries the norm's temporal condition. Two norms for the same act sit in two rows (art. 58 LGP, art. 10.Seis Ley 31/2022) and the table does not say which applies. Placement: right after the paragraph it summarises. | — |
| T | Title «Qué es cada modificación de crédito» with the new row | — | PASS | The title names the figures, not the full rules of each one. The new row adds a temporal rule for one of them, which is a case and not another figure, so the title is not read as a complete list of rules. Placement unchanged, at the end of «## Incorporaciones de crédito». | — |

## m05-l04 — citation fixes and pagas table

Norm, art. 23.Uno.B Ley 31/2022: «Las pagas extraordinarias, que serán dos al año, una en el mes de junio y otra en el
mes de diciembre, y que se devengarán de acuerdo con lo previsto en el artículo 33 de la Ley 33/1987 … Cada una de dichas
pagas incluirá las cuantías de sueldo y trienios fijadas en el artículo 19. Cinco.2 de esta ley y del complemento de
destino mensual que se perciba. Cuando los funcionarios hubieran prestado una jornada de trabajo reducida durante los
seis meses inmediatos anteriores a los meses de junio o diciembre, el importe de la paga extraordinaria experimentará la
correspondiente reducción proporcional.»

Art. 23.Uno.D, párr. 2: «El complemento específico anual se percibirá en catorce pagas iguales de las que doce serán de
percepción mensual y dos adicionales, del mismo importe que una mensual, en los meses de junio y diciembre,
respectivamente.»

| # | row/sentence (short) | citation | PASS/FAIL | passage / reason | replacement |
|---|---|---|---|---|---|
| 1 | Prose l. 210–212: cada paga incluye sueldo y trienios del art. 19.Cinco.2 y el complemento de destino mensual; reducción proporcional por jornada reducida | art. 23.Uno.B Ley 31/2022 | PASS | Only the citation form changed. `citations.es.txt` l. 3076 now resolves it to `boe-a-2022-22128-art-23`, `#a2-5` (previously Ley 30/1984). | — |
| 2 | Prose l. 252–253: complemento específico en catorce pagas iguales | art. 23.Uno.D Ley 31/2022 | PASS | Only the citation form changed. `citations.es.txt` l. 3082 resolves it to `boe-a-2022-22128-art-23`, `#a2-5`. | — |
| 3 | Row «Ley 31/2022» — cada una incluye sueldo y trienios del art. 19.Cinco.2 y el complemento de destino mensual; si jornada reducida en los seis meses inmediatos anteriores a junio o diciembre, reducción proporcional | art. 23.Uno.B Ley 31/2022 | PASS | Verbatim shortening of both paragraphs of 23.Uno.B; «su artículo 19.Cinco.2» = «el artículo 19. Cinco.2 de esta ley». The reduction keeps its condition and the six-month window. The omitted «dos al año … junio … diciembre … artículo 33 de la Ley 33/1987» restricts nothing. Every fact is in prose l. 210–212. Resolves (`citations.es.txt` l. 3079). | — |
| T | Title «Las pagas extraordinarias en el TREBEP, en la Ley 30/1984 y en la Ley 31/2022» | — | PASS | The summarised paragraph (l. 206–212) gives exactly these three norms, and the table has one row per norm, so the title does not overclaim. This closes the table-level FAIL and the Note of `bloque-v/esquemas/verify-m05-l04-l06.md`. Placement unchanged (after l. 212). | — |

## m05-l06 — new prose sentence (l. 118–120)

Norm, art. 34.5 LGS: «No podrá realizarse el pago de la subvención en tanto el beneficiario no se halle al corriente en
el cumplimiento de sus obligaciones tributarias y frente a la Seguridad Social o sea deudor por resolución de procedencia
de reintegro.»

| # | sentence (short) | citation | PASS/FAIL | passage / reason | replacement |
|---|---|---|---|---|---|
| 1 | No podrá realizarse el pago en tanto el beneficiario no se halle al corriente … o sea deudor por resolución de procedencia de reintegro | art. 34.5 LGS | PASS | Verbatim, the whole apartado. A flat rule, no filler. It sits after 34.4 in the article's order. | — |

## m05-l06 — tabla «Del gasto al pago de la subvención» (l. 122–130)

Norm, art. 34.1–4 LGS: «1. Con carácter previo a la convocatoria de la subvención o a la concesión directa de la misma,
deberá efectuarse la aprobación del gasto en los términos previstos en la Ley General Presupuestaria o en las normas
presupuestarias de las restantes Administraciones públicas. 2. La resolución de concesión de la subvención conllevará el
compromiso del gasto correspondiente. 3. El pago de la subvención se realizará previa justificación, por el beneficiario,
de la realización de la actividad, proyecto, objetivo o adopción del comportamiento para el que se concedió en los
términos establecidos en la normativa reguladora de la subvención. Se producirá la pérdida del derecho al cobro … 4.
Cuando la naturaleza de la subvención así lo justifique, podrán realizarse pagos a cuenta. Dichos abonos a cuenta podrán
suponer la realización de pagos fraccionados …, abonándose por cuantía equivalente a la justificación presentada. También
se podrán realizar pagos anticipados que supondrán entregas de fondos con carácter previo a la justificación, … Dicha
posibilidad y el régimen de garantías deberán preverse expresamente en la normativa reguladora de la subvención. En
ningún caso podrán realizarse pagos anticipados a beneficiarios cuando se haya solicitado la declaración de concurso
voluntario, haber sido declarados insolventes en cualquier procedimiento, hallarse declarado en concurso, salvo que en
éste haya adquirido la eficacia un convenio, estar sujetos a intervención judicial o haber sido inhabilitados conforme a
la Ley 22/2003, de 9 de julio, Concursal, sin que haya concluido el período de inhabilitación fijado en la sentencia de
calificación del concurso. La realización de pagos a cuenta o pagos anticipados, así como el régimen de garantías,
deberán preverse expresamente en la normativa reguladora de la subvención.»

| # | row (short) | citation | PASS/FAIL | passage / reason | replacement |
|---|---|---|---|---|---|
| 1 | Aprobación del gasto — previa a la convocatoria o a la concesión directa, en los términos de la LGP | art. 34.1 LGS | PASS | 34.1, copying prose l. 104–105. «o en las normas presupuestarias de las restantes Administraciones públicas» is dropped by row and prose alike; for the AGE this narrows the scope, it does not widen it. | — |
| 2 | Compromiso del gasto — la resolución de concesión lo conlleva | art. 34.2 LGS | PASS | 34.2, verbatim shortening. Prose l. 105. | — |
| 3 | Pago — previa justificación por el beneficiario … en los términos de la normativa reguladora | art. 34.3 LGS | PASS | 34.3 párr. 1, verbatim shortening. Prose l. 106–107. The pérdida del derecho al cobro (párr. 2) is absent from both row and prose; the row does not claim the opposite. | — |
| 4 | Pagos a cuenta y pagos anticipados — cuando la naturaleza lo justifique, caben pagos a cuenta … y pagos anticipados …; deben preverse en la normativa reguladora | art. 34.4 LGS | FAIL | (a) The row drops the exception «En ningún caso podrán realizarse pagos anticipados a beneficiarios cuando …», which the prose states (l. 111–115). Without it the row says anticipated payments are possible with no bar, which is wider than the article. (b) It drops «el régimen de garantías» from the «deberán preverse expresamente» requirement; the prose keeps it (l. 115–116). (c) In one clause, the condition «Cuando la naturaleza de la subvención lo justifique» covers both kinds, whereas the norm and the prose (l. 109–110, «Cabe también el pago anticipado») attach it to pagos a cuenta only. | Split into two rows, both from prose l. 109–116: «\| Pagos a cuenta \| Cuando la naturaleza de la subvención lo justifique, caben pagos a cuenta, abonados por cuantía equivalente a la justificación presentada; deben preverse expresamente en la normativa reguladora, con el régimen de garantías \| art. 34.4 LGS \|» and «\| Pagos anticipados \| Entrega de fondos con carácter previo a la justificación; deben preverse expresamente en la normativa reguladora, con el régimen de garantías. En ningún caso podrán realizarse pagos anticipados a beneficiarios cuando se haya solicitado la declaración de concurso voluntario, haber sido declarados insolventes en cualquier procedimiento, hallarse declarado en concurso, salvo que en éste haya adquirido la eficacia un convenio, estar sujetos a intervención judicial o haber sido inhabilitados conforme a la Ley 22/2003, de 9 de julio, Concursal, sin que haya concluido el período de inhabilitación fijado en la sentencia de calificación del concurso \| art. 34.4 LGS \|». Needs no clause the prose lacks. |
| 5 | Ningún pago — no podrá realizarse el pago en tanto no se halle al corriente … o sea deudor por resolución de procedencia de reintegro | art. 34.5 LGS | PASS | 34.5, verbatim. Prose l. 118–120 (the new sentence). Label: see Notes. | — |
| T | Title «Del gasto al pago de la subvención»; placement | — | PASS | The rows cover art. 34.1–34.5 and the title does not claim more. A `tabla` claims no order, and the rows follow the article's order. Placement: right after the paragraphs summarised (l. 104–120), before the art. 56 RLGS paragraph. | — |

## Citation resolution (`C/citations.es.txt`)

| # | citation | PASS/FAIL | where it resolves |
|---|---|---|---|
| 1 | art. 23.Uno.B Ley 31/2022 (prose, esquema) | PASS | l. 3076, 3079: `boe-a-2022-22128-art-23`, `…pge-2023_2026-09-30.html#a2-5` (art. 23) |
| 2 | art. 23.Uno.D Ley 31/2022 (prose) | PASS | l. 3082: same anchor |
| 3 | art. 10.Seis Ley 31/2022 (two prose citations, one esquema row) | PASS | l. 2933–2934, 2940: `boe-a-2022-22128-art-10`, `#a1-2` (art. 10) |
| 4 | art. 34.1–34.5 LGS (prose 34.5, esquema 34.1–34.5) | PASS | l. 3247–3252: `boe-a-2003-20977-art-34`, LGS PDF `#page=35` (heading of art. 34) |

## Notes

- Row 5 of the m05-l06 table: the «Fase» column holds «Ningún pago» (and «Pagos a cuenta y pagos anticipados»), which
  are not fases. The cell is right; a label that names the case (for example «Beneficiario no al corriente o deudor por
  reintegro», in the norm's words) would read better. This is not counted as a FAIL.
- m05-l04 l. 255 «actualización del artículo 23.Uno.C) Ley 31/2022» and the Normativa line l. 339 «23.Uno.B)–D)» still
  carry the «)» form. Neither is a citation lead today (written «artículo» / inside a list of articles), so nothing
  resolves wrongly. They are out of scope; listed only in case they become citations.
- Ley 31/2022 art. 23.Uno opens «En el año 2023 las retribuciones de los funcionarios serán las siguientes». Neither
  the prose nor the row carries the year; the lesson treats the PGE 2023 as prorrogados (l. 339). Not a FAIL.

## Totals

- Prose sentences: 5 checked, 5 PASS (m05-l02 ×2, m05-l04 ×2 citation fixes, m05-l06 ×1).
- Esquema rows: 7 checked, 6 PASS, 1 FAIL (m05-l06 row 4, art. 34.4 LGS).
- Table-level (title, placement): 3 checked (m05-l02 table after the new row, m05-l04, m05-l06), 3 PASS.
- Citation resolution: 4 checked, 4 PASS.
- Overall: 18 PASS, 1 FAIL. The FAIL's replacement needs no clause the prose lacks.
