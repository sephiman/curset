# Verification — esquemas of m01-l01 (2026-10-18)

I am a blind reviewer: I wrote neither these esquemas nor the lesson, and I read none of the writer's notes. Scope: the
four `:::esquema` blocks that `git diff C/es/lessons/m01-l01.md` shows as added. The diff is 42 lines added and 0
removed (`git diff --numstat`), so no prose line changed. Rules: `spec.md` (this folder), the `::esquema` section of
`docs/platform-delta-handoff.md`, `docs/prose-voice.md`. Format follows `../../bloque-v/esquemas/verify-m05-l03.md`.

Sources, from the scratchpad `txt/` with `art.py` (`pdftotext -layout`, page headers removed). I took no norm wording
from memory.

- `BOE-A-1978-31229_ce_2026-05-20.txt` (CE): arts. 53, 161, 167, 168.
- `BOE-A-1979-23709_lotc_2024-08-02.txt` (LOTC): arts. 33, 35, and 76–77 to check the title of esquema 2.
- `BOE-A-1981-10325_lo-defensor-pueblo_2009-11-04.txt` (LO 3/1981): arts. 2 and 5.

Line numbers are those of the current lesson file.

Load check: I generated the citations report in memory with `tests/test_citations.py::_report` and did not write the
golden. All 22 rows resolve to an anchor that the prose already cites: CE arts. 53, 161, 167, 168; LOTC arts. 33, 35;
LO 3/1981 arts. 2, 5. None is unresolved. The golden `citations.es.txt` has not yet been regenerated for the esquema
rows, so `test_every_citation_has_its_anchors_and_target_as_frozen[age-administrativo-c1]` fails at present. This is
expected while the round is open, and it is not caused only by this lesson: m01-l02 and m01-l03 rows also show in the
diff. Glossary: `src/lib/glossary/report.test.ts` passes against the committed `glossary-links.es.txt`, so no mark moved
or appeared. The candidate terms in these blocks («Ministerio Fiscal» at l. 302, «Comisión Mixta» at l. 365) all come
after their first marks in the prose (l. 295, l. 338).

## tabla «Niveles de protección de los derechos (art. 53 CE)» (l. 167–174)

| # | row (short) | citation | PASS/FAIL | passage / reason | replacement |
|---|---|---|---|---|---|
| 1 | Capítulo segundo entero (arts. 14–38): vinculan; solo por ley… contenido esencial; recurso de inconstitucionalidad | art. 53.1 CE | PASS | 53.1: «Los derechos y libertades reconocidos en el Capítulo segundo del presente Título vinculan a todos los poderes públicos. Sólo por ley, que en todo caso deberá respetar su contenido esencial, podrá regularse el ejercicio de tales derechos y libertades, que se tutelarán de acuerdo con lo previsto en el artículo 161, 1, a).» The first two sentences are verbatim. «Se tutelan mediante el recurso de inconstitucionalidad» resolves the cross-reference to 161.1.a), which is «Del recurso de inconstitucionalidad». The prose says the same thing in the same words at l. 154–156, with «(arts. 14–38)». | — |
| 2 | Artículo 14 y sección 1.ª (arts. 15–29): tutela ante los Tribunales ordinarios… preferencia y sumariedad… y, en su caso, amparo | art. 53.2 CE | PASS | 53.2: «Cualquier ciudadano podrá recabar la tutela de las libertades y derechos reconocidos en el artículo 14 y la Sección primera del Capítulo segundo ante los Tribunales ordinarios por un procedimiento basado en los principios de preferencia y sumariedad y, en su caso, a través del recurso de amparo ante el Tribunal Constitucional.» Verbatim, apart from «pedir» for «recabar», which is the prose's word. «En su caso» is kept. The prose has it at l. 158–160. | — |
| 3 | Objeción de conciencia del artículo 30: recurso de amparo | art. 53.2 CE | PASS | 53.2: «Este último recurso será aplicable a la objeción de conciencia reconocida en el artículo 30.» The prose has it at l. 160–161. | — |
| 4 | Principios del capítulo tercero (arts. 39–52): informan…; solo pueden alegarse… leyes que los desarrollen | art. 53.3 CE | PASS | 53.3: «El reconocimiento, el respeto y la protección de los principios reconocidos en el Capítulo tercero informarán la legislación positiva, la práctica judicial y la actuación de los poderes públicos. Sólo podrán ser alegados ante la Jurisdicción ordinaria de acuerdo con lo que dispongan las leyes que los desarrollen.» The row is a faithful shortening, the same one the prose makes at l. 163–165. Shortening «el reconocimiento, el respeto y la protección de los principios» to «los principios» does not widen the row. | — |

Title: art. 53 has three apartados and the table covers all of them. Row 3 is the second sentence of 53.2. The title
does not overstate. PASS.

## tabla «Plazos de la impugnación del Gobierno, del recurso y de la cuestión de inconstitucionalidad» (l. 297–303)

| # | row (short) | citation | PASS/FAIL | passage / reason | replacement |
|---|---|---|---|---|---|
| 1 | Impugnación por el Gobierno… que suspende…; el Tribunal, en su caso, ratifica o levanta en no más de cinco meses | art. 161.2 CE | PASS | 161.2: «El Gobierno podrá impugnar ante el Tribunal Constitucional las disposiciones y resoluciones adoptadas por los órganos de las Comunidades Autónomas. La impugnación producirá la suspensión de la disposición o resolución recurrida, pero el Tribunal, en su caso, deberá ratificarla o levantarla en un plazo no superior a cinco meses.» A faithful shortening. The row keeps «en su caso», which the prose (l. 273–275) leaves out. So the row is closer to the norm than the prose, and narrower, not wider (see Notes). | — |
| 2 | Recurso de inconstitucionalidad, salvo los nueve meses del 33.2: tres meses desde la publicación | art. 33.1 LOTC | PASS | 33.1: «El recurso de inconstitucionalidad se formulará dentro del plazo de tres meses a partir de la publicación de la Ley, disposición o acto con fuerza de Ley impugnado…». The plazo cell is verbatim. 33.2 opens «No obstante lo dispuesto en el apartado anterior … en el plazo de nueve meses». The label carries that exception, so the row does not read as the only plazo. The prose has both at l. 284–288. The words «artículo 33.2» in the label do not parse as a second citation: the report shows one anchor for the row. | — |
| 3 | Cuestión de inconstitucionalidad: audiencia a las partes y al Ministerio Fiscal antes de plantearla; diez días, común e improrrogable | art. 35.2 LOTC | PASS | 35.2: «Antes de adoptar mediante auto su decisión definitiva, el órgano judicial oirá a las partes y al Ministerio Fiscal para que en el plazo común e improrrogable de 10 días puedan alegar lo que deseen…». The row repeats the prose (l. 294–295) word for word. «Antes de plantearla» is the prose's reading of «antes de adoptar … su decisión definitiva». It is not wider, because the cuestión is only raised by that auto (see Notes). | — |

Title: FAIL. «Plazos de la impugnación del Gobierno, del recurso y de la cuestión de inconstitucionalidad» reads as
the full set of plazos for those three, but the table holds one plazo for each.

- Impugnación del Gobierno: LOTC 76 also sets the plazo to impugn: «Dentro de los dos meses siguientes a la fecha de su
  publicación o, en defecto de la misma, desde que llegare a su conocimiento, el Gobierno podrá impugnar…».
- Cuestión: LOTC 35.2 also says the órgano judicial may raise it only «una vez concluso el procedimiento y dentro del
  plazo para dictar sentencia», and that after the audiencia «el juez resolverá en el plazo de tres días».

The prose states none of these, so they cannot be added as rows. The title has to mark the table as a selection.

Replacement title: `Tres plazos ante el Tribunal Constitucional`. Prose gaps for the ledger: art. 76 LOTC (two months
to impugn); art. 35.2 LOTC (raised only once the procedure is concluded and within the plazo para dictar sentencia;
three days to resolve after the audiencia).

## tabla «Elección y cese del Defensor del Pueblo: mayorías y plazos (arts. 2 y 5 LO 3/1981)» (l. 361–372)

| # | row (short) | citation | PASS/FAIL | passage / reason | replacement |
|---|---|---|---|---|---|
| 1 | Elección por las Cortes Generales — periodo de cinco años | art. 2.1 LO 3/1981 | PASS | 2.Uno: «El Defensor del Pueblo será elegido por las Cortes Generales para un periodo de cinco años…». Verbatim. The prose has it at l. 335. | — |
| 2 | Propuesta del candidato o candidatos por la Comisión Mixta — mayoría simple | art. 2.3 LO 3/1981 | PASS | 2.Tres: «…para proponer a los Plenos de las Cámaras el candidato o candidatos a Defensor del Pueblo. Los acuerdos de la Comisión se adoptarán por mayoría simple.» The prose has it at l. 339–340. | — |
| 3 | Elección por el Pleno del Congreso — tres quintas partes de los miembros — convocatoria no antes de diez días desde la propuesta | art. 2.4 LO 3/1981 | PASS | 2.Cuatro: «Propuesto el candidato o candidatos, se convocará en término no inferior a diez días al Pleno del Congreso para que proceda a su elección. Será designado quien obtuviese una votación favorable de las tres quintas partes de los miembros del Congreso…». A faithful shortening, the same as the prose at l. 342–343. | — |
| 4 | Ratificación por el Senado — esta misma mayoría — después, en un plazo máximo de veinte días | art. 2.4 LO 3/1981 | PASS | 2.Cuatro: «…y posteriormente, en un plazo máximo de veinte días, fuese ratificado por esta misma mayoría del Senado.» Verbatim («después» stands for «posteriormente»). Read with row 3, «esta misma mayoría» is the three fifths of the members, as in the norm. The prose has it at l. 343–344. | — |
| 5 | Si no se alcanzan esas mayorías: sucesivas propuestas de la Comisión, en un mes como máximo — tres quintos del Congreso y, después, mayoría absoluta del Senado | art. 2.5 LO 3/1981 | PASS | 2.Cinco: «Caso de no alcanzarse las mencionadas mayorías, se procederá en nueva sesión de la Comisión, y en el plazo máximo de un mes, a formular sucesivas propuestas. En tales casos, una vez conseguida la mayoría de los tres quintos en el Congreso, la designación quedará realizada al alcanzarse la mayoría absoluta del Senado.» A faithful shortening. «Y, después» is supported by «una vez conseguida». The prose has it at l. 345–347 («nuevas propuestas»; the row uses the norm's «sucesivas»). | — |
| 6 | Vacante por muerte, renuncia y expiración del plazo del mandato — la declara el Presidente del Congreso | art. 5.2 LO 3/1981 | PASS | 5.Dos: «La vacante en el cargo se declarará por el Presidente del Congreso en los casos de muerte, renuncia y expiración del plazo del mandato.» Verbatim. The prose has it at l. 355–356. | — |
| 7 | Vacante en los demás casos — las Cámaras, tres quintas partes de los componentes de cada una, debate y audiencia | art. 5.2 LO 3/1981 | PASS | 5.Dos: «En los demás casos se decidirá, por mayoría de las tres quintas partes de los componentes de cada Cámara, mediante debate y previa audiencia del interesado.» The row keeps the majority and both conditions. «Las Cámaras» as the subject is the prose's reading (l. 356–358) of the impersonal «se decidirá». | — |
| 8 | Nombramiento del nuevo Defensor — el procedimiento se inicia en plazo no superior a un mes | art. 5.3 LO 3/1981 | PASS | 5.Tres: «Vacante el cargo se iniciará el procedimiento para el nombramiento de nuevo Defensor del Pueblo en plazo no superior a un mes.» The row follows the prose (l. 358–359) and leaves out «Vacante el cargo». It sits right after the two vacancy rows, so the point from which the plazo runs is clear. It does not read wider (see Notes). | — |

Title: every majority and plazo of arts. 2 and 5 is in the table. 2.Seis (the conformidad for the adjuntos) and
5.Cuatro (the interim) carry neither a majority nor a plazo. The causes of cese (5.Uno) are not a majority or a plazo,
and the title does not claim them. PASS.

## tabla «Mayorías y referéndum de la reforma constitucional (arts. 167 y 168 CE)» (l. 444–454)

| # | row (short) | citation | PASS/FAIL | passage / reason | replacement |
|---|---|---|---|---|---|
| 1 | Ordinario — aprobación de los proyectos — tres quintos de cada Cámara | art. 167.1 CE | PASS | 167.1: «Los proyectos de reforma constitucional deberán ser aprobados por una mayoría de tres quintos de cada una de las Cámaras.» Verbatim. The prose has it at l. 421. | — |
| 2 | Ordinario — si no hay acuerdo — Comisión paritaria; texto votado por Congreso y Senado | art. 167.1 CE | PASS | 167.1: «Si no hubiera acuerdo entre ambas, se intentará obtenerlo mediante la creación de una Comisión de composición paritaria de Diputados y Senadores, que presentará un texto que será votado por el Congreso y el Senado.» A faithful shortening, the same as the prose at l. 422–423. | — |
| 3 | Ordinario — si así no se aprueba — dos tercios del Congreso, siempre que mayoría absoluta del Senado | art. 167.2 CE | PASS | 167.2: «De no lograrse la aprobación mediante el procedimiento del apartado anterior, y siempre que el texto hubiere obtenido el voto favorable de la mayoría absoluta del Senado, el Congreso, por mayoría de dos tercios, podrá aprobar la reforma.» The condition is kept. The prose has it at l. 425–426. | — |
| 4 | Ordinario — referéndum, aprobada la reforma — si lo pide una décima parte de una Cámara, en quince días | art. 167.3 CE | PASS | 167.3: «Aprobada la reforma por las Cortes Generales, será sometida a referéndum para su ratificación cuando así lo soliciten, dentro de los quince días siguientes a su aprobación, una décima parte de los miembros de cualquiera de las Cámaras.» A faithful shortening. The prose has it at l. 428–430. | — |
| 5 | Agravado: revisión total o parcial (título preliminar, sección 1.ª cap. 2.º tít. I, tít. II) — aprobación del principio — dos tercios de cada Cámara, disolución inmediata | art. 168.1 CE | PASS | 168.1: «Cuando se propusiere la revisión total de la Constitución o una parcial que afecte al Título preliminar, al Capítulo segundo, Sección primera del Título I, o al Título II, se procederá a la aprobación del principio por mayoría de dos tercios de cada Cámara, y a la disolución inmediata de las Cortes.» The label keeps all three titles of the partial case. The prose has it at l. 434–439. | — |
| 6 | Agravado — Cámaras elegidas ratifican y estudian — dos tercios de ambas Cámaras | art. 168.2 CE | PASS | 168.2: «Las Cámaras elegidas deberán ratificar la decisión y proceder al estudio del nuevo texto constitucional, que deberá ser aprobado por mayoría de dos tercios de ambas Cámaras.» A faithful shortening. The prose has it at l. 440–441, under «(art. 168 CE)». | — |
| 7 | Agravado — referéndum, aprobada la reforma — siempre obligatorio | art. 168.3 CE | PASS | 168.3: «Aprobada la reforma por las Cortes Generales, será sometida a referéndum para su ratificación.» The norm sets no condition. «Siempre obligatorio» is the prose's wording (l. 442), and it is the faithful contrast with 167.3. | — |

Title: it names majorities and the referéndum. It leaves out iniciativa (art. 166) and the time limit (art. 169)
without claiming them. Every majority and every referéndum condition of arts. 167–168 is a row. PASS.

## Order

All four esquemas are `tabla`, so none claims an order or a dependency. Where a cell says «después» (esquema 3, rows
4 and 5), the norm says so too: «posteriormente» in 2.Cuatro and «una vez conseguida» in 2.Cinco. PASS.

## Placement

- Esquema 1 (l. 167): right after the three paragraphs of «La garantía de los derechos» (l. 152–165), and before the
  art. 81 paragraph, which it does not summarise. Those paragraphs are bold-led prose, not a list. PASS.
- Esquema 2 (l. 297): it summarises l. 273–275 (art. 161.2, under «Competencias»), l. 284–288 and l. 292–295. It sits
  at the end of «Cuestión de inconstitucionalidad», after the last of these, and before «Recurso de amparo». The
  amparo has its own plazos table at l. 314–318, which the esquema does not repeat. PASS.
- Esquema 3 (l. 361): right after «Elección» (l. 335–350) and «Cese» (l. 354–359), and before «Prerrogativas». PASS.
- Esquema 4 (l. 444): right after «Procedimiento ordinario» (l. 421–430) and «Procedimiento agravado» (l. 434–442),
  and before «Lo que más cae». PASS, with one caution. Rows 5–7 repeat the numbered list at l. 438–442, and the spec
  says «none where the prose is … already a list». The table earns its place because it puts the ordinary procedure's
  paragraphs and the agravado list side by side, and the ordinary half is plain prose. I did not count this as a FAIL,
  but the writer may want to record the choice in the ledger.

## Notes

- Voice: the titles and cells use no filler, no rhetorical question, no «no solo… sino» and no closer. The «—» in
  table cells is an empty-cell marker, not a list field separator, so the limit on « — » inside a field does not apply.
- Esquema 2, row 1: the row has «en su caso» from 161.2 and the prose at l. 274–275 does not. Read alone, the prose
  is slightly wider than the norm («debe ratificar o levantar», with no «en su caso»: art. 77 LOTC adds «salvo que,
  con anterioridad, hubiera dictado sentencia»). The row is fine. The prose sentence could take «en su caso» in a
  later prose round.
- Esquema 2, row 3, and the prose at l. 294: «antes de plantearla» narrows «antes de adoptar mediante auto su decisión
  definitiva», because the decision may be not to raise the cuestión. This is not a FAIL, because the audiencia does
  come before any raising. Writing «antes de decidir si la plantea» in both would be stricter.
- Esquema 3, row 8: 5.Tres opens «Vacante el cargo». The label «Nombramiento del nuevo Defensor» could read
  «Vacante el cargo: nombramiento del nuevo Defensor» to carry the starting point in the norm's words. Optional.
- Esquema 4, rows 6–7 cite 168.2 and 168.3, while the prose cites the list as «(art. 168 CE)». Both resolve to the same
  anchor, and the apartados are correct, so this is a more precise citation and not a new one.
- Esquema 4, row 2: the header «Qué exige» fits this row loosely, because the cell describes what happens (the Comisión
  presents a text). It does not reword the fact. Cosmetic.

## Counts

22 rows: 22 PASS, 0 FAIL. Titles: 3 PASS, 1 FAIL (esquema 2, a selective list read as complete; it needs a retitle,
and the missing plazos are prose gaps). Order: PASS. Placement: PASS (one caution on esquema 4). Glossary marks: none
moved. Citations: all 22 resolve; the golden is still to be regenerated.
