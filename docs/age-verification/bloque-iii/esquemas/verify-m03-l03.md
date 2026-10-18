# Verification of the esquemas in m03-l03 (R2c, bloque III), 2026-10-18

The reviewer did not write the lesson or its esquemas. Every row was checked against the cited article in the
consolidated BOE text (pdftotext, `txt/BOE-A-2015-10565_lpac_2024-11-06.clean`, last match of each heading = body),
and against the lesson's own prose (`C/es/lessons/m03-l03.md`, lines 145–398). No memory of the norm was used.
Rule applied: `docs/age-verification/bloque-iii/esquemas/spec.md`.

Esquemas: A «Cómputo de plazos» (tabla, l. 163), B «Plazos del procedimiento administrativo común» (plazos, l. 294),
C «Los recursos administrativos» (tabla, l. 400), D «Plazos de los recursos administrativos» (tabla, l. 408).

| # | esquema / row (short) | citation | PASS/FAIL | passage / reason | replacement |
|---|---|---|---|---|---|
| A1 | Cómputo / Señalados por horas | art. 30.1 LPAC | PASS | «Salvo que por Ley o en el Derecho de la Unión Europea se disponga otro cómputo, cuando los plazos se señalen por horas, se entiende que éstas son hábiles. Son hábiles todas las horas del día que formen parte de un día hábil. … se contarán de hora en hora y de minuto en minuto desde la hora y minuto en que tenga lugar la notificación o publicación del acto … y no podrán tener una duración superior a veinticuatro horas». Exception kept; prose l. 147–149 states every fact. | — |
| A2 | Cómputo / Señalados por días | art. 30.2–3 LPAC | PASS | 30.2 «Siempre que por Ley o en el Derecho de la Unión Europea no se exprese otro cómputo, … se entiende que éstos son hábiles, excluyéndose del cómputo los sábados, los domingos y los declarados festivos»; 30.3 «a partir del día siguiente a aquel en que tenga lugar la notificación o publicación del acto …, o desde el siguiente a aquel en que se produzca la estimación o la desestimación por silencio administrativo». «o al silencio administrativo» is a faithful shortening; prose l. 151–154 has it. | — |
| A3 | Cómputo / Fijados en meses o años | art. 30.4 LPAC | PASS | «se computarán a partir del día siguiente … El plazo concluirá el mismo día en que se produjo la notificación, publicación o silencio administrativo en el mes o el año de vencimiento. Si en el mes de vencimiento no hubiera día equivalente …, se entenderá que el plazo expira el último día del mes». Prose l. 157–158. | — |
| A4 | Cómputo / Último día inhábil | art. 30.5 LPAC | PASS | «Cuando el último día del plazo sea inhábil, se entenderá prorrogado al primer día hábil siguiente». Prose l. 159. | — |
| B1 | Procedimiento / Subsanación | art. 68.1 LPAC | PASS | «se requerirá al interesado para que, en un plazo de diez días, subsane la falta o acompañe los documentos preceptivos». Prose l. 236–238. | — |
| B2 | Procedimiento / Ampliación de la subsanación | art. 68.2 LPAC | PASS | «Siempre que no se trate de procedimientos selectivos o de concurrencia competitiva, este plazo podrá ser ampliado prudencialmente, hasta cinco días, … cuando la aportación de los documentos requeridos presente dificultades especiales». Both conditions kept in the label; «hasta» keeps it a maximum. Prose l. 238–241. | — |
| B3 | Procedimiento / Alegaciones | art. 76.1 LPAC | PASS | «Los interesados podrán, en cualquier momento del procedimiento anterior al trámite de audiencia, aducir alegaciones». Prose l. 249. | — |
| B4 | Procedimiento / Período de prueba | art. 77.2 LPAC | PASS | «la apertura de un período de prueba por un plazo no superior a treinta días ni inferior a diez». Prose l. 250 states it in the same unconditioned form; the row is not wider than the prose (the extraordinary period of 77.2 is in neither). | — |
| B5 | Procedimiento / Emisión de informes | art. 80.2 LPAC | PASS | «en el plazo de diez días, salvo que una disposición o el cumplimiento del resto de los plazos del procedimiento permita o exija otro plazo mayor o menor». The prose (l. 251, cited «art. 80.1–2») states the plazo and the exception as «salvo otro plazo»; the row quotes that same exception in full, which keeps it rather than adding a fact. | — |
| B6 | Procedimiento / Audiencia | art. 82.2 LPAC | PASS | «Los interesados, en un plazo no inferior a diez días ni superior a quince, podrán alegar». Prose l. 255. | — |
| B7 | Procedimiento / Información pública | art. 83.2 LPAC | PASS | «determinará el plazo para formular alegaciones, que en ningún caso podrá ser inferior a veinte días». Prose l. 257–258. (Order: see Notes.) | — |
| B8 | Procedimiento / Actuaciones complementarias | art. 87 LPAC | PASS | «concediéndoseles un plazo de siete días para formular las alegaciones que tengan por pertinentes tras la finalización de las mismas. Las actuaciones complementarias deberán practicarse en un plazo no superior a quince días». Prose l. 275–277. | — |
| B9 | Procedimiento / Plazo máximo para resolver | art. 21.2 LPAC | FAIL (order) | Text is verbatim: «será el fijado por la norma reguladora … Este plazo no podrá exceder de seis meses salvo que una norma con rango de Ley establezca uno mayor o así venga previsto en el Derecho de la Unión Europea»; prose l. 189–191. But numbered 9, after the actuaciones complementarias, it reads as a stage that opens once instrucción ends, whereas art. 21.3 counts it «desde la fecha del acuerdo de iniciación» or from the entrada of the solicitud (prose l. 191–193). False chronology. | Move to position 1 (see reordered esquema below): `1. Plazo máximo para resolver — el fijado por la norma reguladora, que no podrá exceder de seis meses salvo que una norma con rango de Ley establezca uno mayor o así venga previsto en el Derecho de la Unión Europea (art. 21.2 LPAC)` |
| B10 | Procedimiento / Plazo máximo si la norma no lo fija | art. 21.3 LPAC | FAIL (order) | «Cuando las normas reguladoras de los procedimientos no fijen el plazo máximo, éste será de tres meses. Este plazo y los previstos en el apartado anterior se contarán: a) … desde la fecha del acuerdo de iniciación. b) … desde la fecha en que la solicitud haya tenido entrada en el registro electrónico …». Same false chronology as B9; the dies a quo, which the prose states (l. 191–193), is what places it. | Position 2: `2. Plazo máximo, si la norma reguladora no lo fija — tres meses, que se contarán en los procedimientos iniciados de oficio desde la fecha del acuerdo de iniciación, y en los iniciados a solicitud del interesado desde la fecha en que la solicitud haya tenido entrada en el registro electrónico de la Administración u Organismo competente para su tramitación (art. 21.3 LPAC)` |
| B11 | Procedimiento / Caducidad por paralización | art. 95.1 LPAC | FAIL | «En los procedimientos iniciados a solicitud del interesado, cuando se produzca su paralización por causa imputable al mismo, la Administración le advertirá que, transcurridos tres meses, se producirá la caducidad del procedimiento. Consumido este plazo sin que el particular requerido realice las actividades necesarias para reanudar la tramitación, la Administración acordará el archivo de las actuaciones». The row («— transcurridos tres meses») drops the advertencia and the condition that the interesado not perform the activities needed to resume, so it reads as caducidad running automatically from the paralysis. Prose l. 286–288 states both. | `11. Caducidad del procedimiento paralizado por causa imputable al solicitante, previa advertencia de la Administración — transcurridos tres meses sin que el particular requerido realice las actividades necesarias para reanudar la tramitación (art. 95.1 LPAC)` |
| C1 | Recursos / Alzada | art. 121.1 LPAC | PASS | «Las resoluciones y actos a que se refiere el artículo 112.1, cuando no pongan fin a la vía administrativa, podrán ser recurridos en alzada ante el órgano superior jerárquico del que los dictó». Prose l. 363–364. (Header nuance: see Notes.) | — |
| C2 | Recursos / Potestativo de reposición | art. 123.1 LPAC | PASS | «Los actos administrativos que pongan fin a la vía administrativa podrán ser recurridos potestativamente en reposición ante el mismo órgano que los hubiera dictado». «Potestativo» in the label carries the option. Prose l. 373–374. | — |
| C3 | Recursos / Extraordinario de revisión | art. 125.1 LPAC | PASS | «Contra los actos firmes en vía administrativa podrá interponerse el recurso extraordinario de revisión ante el órgano administrativo que los dictó, que también será el competente para su resolución, cuando concurra alguna de las circunstancias siguientes». «del artículo 125.1» stands for «siguientes», listed in the prose l. 384–394. | — |
| D1 | Plazos recursos / Alzada | art. 122.1–2 LPAC | PASS | 122.1 «será de un mes, si el acto fuera expreso. … Si el acto no fuera expreso … en cualquier momento a partir del día siguiente a aquel en que, de acuerdo con su normativa específica, se produzcan los efectos del silencio administrativo»; 122.2 «será de tres meses. Transcurrido este plazo sin que recaiga resolución, se podrá entender desestimado el recurso, salvo en el supuesto previsto en el artículo 24.1, tercer párrafo». Exception kept. Prose l. 366–368. | — |
| D2 | Plazos recursos / Reposición | art. 124.1–2 LPAC | PASS | 124.1 «será de un mes, si el acto fuera expreso»; 124.2 «El plazo máximo para dictar y notificar la resolución del recurso será de un mes». The «si el acto fuera expreso» condition keeps the row from reading wider; the non-express case is in neither prose nor row. Prose l. 375–376. | — |
| D3 | Plazos recursos / Extraordinario de revisión | arts. 125.2 y 126.3 LPAC | PASS | 125.2 «cuando se trate de la causa a) …, dentro del plazo de cuatro años siguientes a la fecha de la notificación de la resolución impugnada. En los demás casos, el plazo será de tres meses a contar desde el conocimiento de los documentos o desde que la sentencia judicial quedó firme»; 126.3 «Transcurrido el plazo de tres meses desde la interposición … sin haberse dictado y notificado la resolución, se entenderá desestimado». Prose l. 396–398. | — |

### Reordered esquema B (replaces l. 294–306)

```
:::esquema{kind=plazos title="Plazos del procedimiento administrativo común"}
1. Plazo máximo para resolver — el fijado por la norma reguladora, que no podrá exceder de seis meses salvo que una norma con rango de Ley establezca uno mayor o así venga previsto en el Derecho de la Unión Europea (art. 21.2 LPAC)
2. Plazo máximo, si la norma reguladora no lo fija — tres meses, que se contarán en los procedimientos iniciados de oficio desde la fecha del acuerdo de iniciación, y en los iniciados a solicitud del interesado desde la fecha en que la solicitud haya tenido entrada en el registro electrónico de la Administración u Organismo competente para su tramitación (art. 21.3 LPAC)
3. Subsanación de la solicitud — un plazo de diez días (art. 68.1 LPAC)
4. Ampliación de la subsanación, salvo en procedimientos selectivos o de concurrencia competitiva, cuando la aportación de los documentos requeridos presente dificultades especiales — hasta cinco días (art. 68.2 LPAC)
5. Alegaciones — en cualquier momento del procedimiento anterior al trámite de audiencia (art. 76.1 LPAC)
6. Período de prueba — no superior a treinta días ni inferior a diez (art. 77.2 LPAC)
7. Emisión de informes — diez días, salvo que una disposición o el cumplimiento del resto de los plazos del procedimiento permita o exija otro plazo mayor o menor (art. 80.2 LPAC)
8. Audiencia — un plazo no inferior a diez días ni superior a quince (art. 82.2 LPAC)
9. Información pública — un plazo para formular alegaciones que en ningún caso podrá ser inferior a veinte días (art. 83.2 LPAC)
10. Actuaciones complementarias — un plazo no superior a quince días, y siete días para formular alegaciones tras su finalización (art. 87 LPAC)
11. Caducidad del procedimiento paralizado por causa imputable al solicitante, previa advertencia de la Administración — transcurridos tres meses sin que el particular requerido realice las actividades necesarias para reanudar la tramitación (art. 95.1 LPAC)
:::
```

## Placement

- A follows the paragraphs on arts. 30.1–30.5 (l. 147–161) and precedes the paragraph on 30.6–31.2; correct.
- B closes the «Procedimiento administrativo común» section after every paragraph it draws on (21.2–21.3 at
  l. 189–193; 68, 76–87, 95.1 at l. 236–288); correct.
- C and D follow the alzada, reposición and revisión paragraphs (l. 361–398) and precede the contencioso section;
  correct. No esquema replaces prose.

## Notes

- B order. Rows on 68 → 76 → 77 → 80 → 82 → 83 → 87 follow the LPAC article order, which is also the order of the
  lesson's own sections (iniciación, instrucción, terminación); read as phases this is not a false chronology, with
  one soft spot: B7 (información pública) after B6 (audiencia) suggests a sequence neither art. 83 nor the prose
  states (art. 82.1 puts the audiencia «inmediatamente antes de redactar la propuesta de resolución»). Left PASS; the
  writer may prefer to put información pública before audiencia, which matches 82.1. Rows 9–10 were the real false
  chronology (fixed by the reorder above); row 11 is a contingency, which the fixed label now makes plain.
- C1 header «Ante qué órgano»: art. 121.2 lets the alzada be filed before the organ that dictated the act or the one
  that resolves it (prose l. 364–366). The cell is the verbatim wording of 121.1, so PASS, but a header such as
  «Órgano al que se recurre» would avoid reading as the filing desk.
- Citations: every row's article is cited in the prose (B5 cites 80.2, the prose «80.1–2»; D3 joins 125.2 and 126.3,
  each cited in the prose).
- Voice: Peninsular Spanish, the norm's own vocabulary; no invented terms.
