# Verification — esquemas of m01-l05 (2026-10-18)

I am a blind reviewer: I wrote neither these esquemas nor the lesson, and I did not read the writer's notes. Scope: the
three `:::esquema` blocks of `C/es/lessons/m01-l05.md`. `git diff` on the file shows only added lines (the three blocks
and their blank lines). No prose line changed. Rules: `spec.md` (this folder), the `::esquema` section of
`docs/platform-delta-handoff.md` and `docs/prose-voice.md`. I used the format of `../../bloque-v/esquemas/verify-m05-l03.md`.

Sources, from the scratchpad `txt/` (`pdftotext -layout`), read with `art.py` and `sed`:
`BOE-A-1978-31229_ce_2026-05-20.txt` (CE arts. 98, 99, 112, 113, 114, 115) and
`BOE-A-1997-25336_ley-gobierno_2025-01-03.txt` (Ley 50/1997: index, título I headings, arts. 1, 3, 4, 5, 6, 7, 8, 9, 10
and 21). I took no norm wording from memory. I also read the loader code that checks rows against the prose
(`backend/src/tradeschool/citations/{grammar,lesson,course}.py`). Line numbers are those of the current lesson file.

## arbol «El Gobierno y sus órganos de colaboración y apoyo» (l. 115–128)

| # | node (short) | citation | PASS/FAIL | passage / reason | replacement |
|---|---|---|---|---|---|
| 1 | Gobierno — se compone del Presidente, del Vicepresidente o Vicepresidentes, en su caso, y de los Ministros (root) | art. 1.2 Ley 50/1997 | PASS | 1.2: «El Gobierno se compone del Presidente, del Vicepresidente o Vicepresidentes, en su caso, y de los Ministros.» Verbatim. In prose at l. 11, with the same citation. | — |
| 2 | Presidente — dirige la acción del Gobierno y coordina…, sin perjuicio de… | art. 98.2 CE | PASS | 98.2: «El Presidente dirige la acción del Gobierno y coordina las funciones de los demás miembros del mismo, sin perjuicio de la competencia y responsabilidad directa de éstos en su gestión.» A verbatim shortening («del mismo» dropped) that keeps the «sin perjuicio». In prose at l. 25. Under node 1: art. 1.2 names him as a member. | — |
| 3 | Vicepresidentes, cuando existan — funciones que les encomiende el Presidente; el que asume un Departamento es además Ministro | art. 3 Ley 50/1997 | PASS | 3.1: «Al Vicepresidente o Vicepresidentes, cuando existan, les corresponderá el ejercicio de las funciones que les encomiende el Presidente.» 3.2: «El Vicepresidente que asuma la titularidad de un Departamento Ministerial, ostentará, además, la condición de Ministro.» The label carries «cuando existan». The fact is the prose's faithful shortening (l. 47), cited the same way. Under node 1 per art. 1.2. | — |
| 4 | Ministros — como titulares de sus Departamentos, tienen competencia y responsabilidad en la esfera específica de su actuación | art. 4.1 Ley 50/1997 | PASS | 4.1: «Los Ministros, como titulares de sus Departamentos, tienen competencia y responsabilidad en la esfera específica de su actuación, y les corresponde el ejercicio de las siguientes funciones: …». Verbatim first clause. The list of functions is left out, which narrows the node and does not widen it. In prose at l. 49. | — |
| 5 | Ministros sin cartera, si los hay — responsabilidad de determinadas funciones gubernamentales | art. 4.2 Ley 50/1997 | PASS | 4.2: «Además de los Ministros titulares de un Departamento, podrán existir Ministros sin cartera, a los que se les atribuirá la responsabilidad de determinadas funciones gubernamentales.» The label «si los hay» carries «podrán existir» (prose l. 51: «Puede haber»). They are Ministros, so they are members under art. 1.2. | — |
| 6 | Consejo de Ministros — el órgano colegiado del Gobierno | art. 5.1 Ley 50/1997 | PASS | 5.1: «Al Consejo de Ministros, como órgano colegiado del Gobierno, le corresponde…». Verbatim fragment. In prose at l. 57. Dependency: «órgano colegiado del Gobierno» and art. 1.3 («Los miembros del Gobierno se reúnen en Consejo de Ministros…», prose l. 13). See Notes on mixing members and organs. | — |
| 7 | Comisiones Delegadas del Gobierno — las integran miembros del Gobierno y, en su caso, Secretarios de Estado | art. 6.2 Ley 50/1997 | PASS | 6.2.b): the Real Decreto de creación specifies «Los miembros del Gobierno y, en su caso, Secretarios de Estado que la integran». A faithful shortening, word for word the prose at l. 78. Dependency: art. 1.3 (prose l. 13), «…y en Comisiones Delegadas del Gobierno». The list-row citation has no letter, as the spec requires. | — |
| 8 | Órganos de colaboración y apoyo del Gobierno (root, label only) | arts. 7–10 Ley 50/1997 | FAIL | The range is right. Título I, capítulo II of Ley 50/1997 is headed «De los órganos de colaboración y apoyo del Gobierno» and holds exactly arts. 7 (Secretarios de Estado), 8 (Comisión General), 9 (Secretariado) and 10 (Gabinetes); art. 11 opens título II. The loader also accepts it: `arts. 7–10` parses as units 7 and 10 plus the range (7, 10), and both articles have prose anchors (art. 7.1 at l. 86, art. 10.1 at l. 113). But the prose never carries this citation. The grouping appears only as the section heading at l. 82, which has no citation, and no prose sentence says that these four are the Gobierno's órganos de colaboración y apoyo under arts. 7–10. Criterion 4: a citation the prose lacks. Any correct citation for the node would need a prose clause the prose lacks, so the node goes and the gap is listed. | Remove the line `- Órganos de colaboración y apoyo del Gobierno (arts. 7–10 Ley 50/1997)` and outdent nodes 9–12 to roots (`- Secretarios de Estado — …` etc.). The esquema title still names the group, and no node then sits under «Gobierno», which would be a false dependency. Prose gap for the ledger: l. 82 states the grouping only as a heading, with no citation of arts. 7–10 (capítulo II, título I Ley 50/1997). |
| 9 | Secretarios de Estado — órganos superiores de la AGE, directamente responsables de la ejecución… | art. 7.1 Ley 50/1997 | PASS | 7.1: «Los Secretarios de Estado son órganos superiores de la Administración General del Estado, directamente responsables de la ejecución de la acción del Gobierno en un sector de actividad específica de un Departamento o de la Presidencia del Gobierno.» Verbatim. In prose at l. 86 («Responden directamente de…» is the prose's rewording of the same clause). | — |
| 10 | Comisión General de SE y Subsecretarios — la integran…; la preside un Vicepresidente o, en su defecto, el Ministro de la Presidencia | art. 8.1–2 Ley 50/1997 | PASS | 8.1: «…estará integrada por los titulares de las Secretarías de Estado y por los Subsecretarios de los distintos Departamentos Ministeriales.» 8.2: «La Presidencia … corresponde a un Vicepresidente del Gobierno o, en su defecto, al Ministro de la Presidencia.» A faithful shortening, the same as the prose at l. 92 and l. 94. «La integran» is exact: the Abogado General del Estado «asistirá» (8.1 párr. 2) and is not a member, so leaving him out does not widen the node. The ausencia rule of 8.2 is a substitution and not a limit on who presides; the prose leaves it out too (see Notes). | — |
| 11 | Secretariado del Gobierno — órgano de apoyo del Consejo de Ministros, de las Comisiones Delegadas y de la Comisión General | art. 9.1 Ley 50/1997 | PASS | 9.1: «El Secretariado del Gobierno, como órgano de apoyo del Consejo de Ministros, de las Comisiones Delegadas del Gobierno y de la Comisión General de Secretarios de Estado y Subsecretarios, ejercerá…». Verbatim. In prose at l. 102. | — |
| 12 | Gabinetes — órganos de apoyo político y técnico del Presidente, Vicepresidentes, Ministros y Secretarios de Estado | art. 10.1 Ley 50/1997 | PASS | 10.1: «Los Gabinetes son órganos de apoyo político y técnico del Presidente del Gobierno, de los Vicepresidentes, de los Ministros y de los Secretarios de Estado.» Verbatim («del Gobierno» dropped after «Presidente», which is unambiguous here). In prose at l. 113. | — |

Nesting: nodes 2–7 sit under «Gobierno». Nodes 2–5 are members under art. 1.2. Nodes 6–7 are where the members meet
(art. 1.3) and are «órgano(s) colegiado(s) del Gobierno» (arts. 5.1, 6.4). No node of capítulo II sits under
«Gobierno», which is right, because Secretarios de Estado are not members (art. 1.2). PASS apart from node 8.
Title: the tree lists all four organs of capítulo II and every member of art. 1.2, so it does not read a selective list
as complete. PASS.

## plazos «Votaciones y plazos de la investidura» (l. 149–155)

| # | step (short) | citation | PASS/FAIL | passage / reason | replacement |
|---|---|---|---|---|---|
| 1 | Propuesta de un candidato por el Rey, previa consulta…, a través del Presidente del Congreso — después de cada renovación del Congreso…, y en los demás supuestos… | art. 99.1 CE | PASS | 99.1: «Después de cada renovación del Congreso de los Diputados, y en los demás supuestos constitucionales en que así proceda, el Rey, previa consulta con los representantes designados por los Grupos políticos con representación parlamentaria, y a través del Presidente del Congreso, propondrá un candidato a la Presidencia del Gobierno.» Verbatim, reordered, keeping every condition. In prose at l. 138. | — |
| 2 | Primera votación; si obtiene la confianza, el Rey le nombra Presidente — mayoría absoluta de los miembros del Congreso | art. 99.3 CE | PASS | 99.3: «Si el Congreso de los Diputados, por el voto de la mayoría absoluta de sus miembros, otorgare su confianza a dicho candidato, el Rey le nombrará Presidente.» The majority is exact. «Primera votación» is the norm's own term (99.5, «a partir de la primera votación de investidura»), also used by the prose at l. 147. In prose at l. 144. Order 1 → 2: 99.2 has the candidate «propuesto conforme a lo previsto en el apartado anterior» ask for the confianza, and 99.3 follows. | — |
| 3 | Nueva votación de la misma propuesta, de no alcanzarse dicha mayoría; mayoría simple — cuarenta y ocho horas después de la anterior | art. 99.3 CE | PASS | 99.3: «De no alcanzarse dicha mayoría, se someterá la misma propuesta a nueva votación cuarenta y ocho horas después de la anterior, y la confianza se entenderá otorgada si obtuviere la mayoría simple.» Verbatim. The plazo is exact and counted from the first vote, as the step says. In prose at l. 145. Order 2 → 3 is stated by the norm. | — |
| 4 | Sucesivas propuestas, en la forma prevista… — si efectuadas las citadas votaciones no se otorga la confianza | art. 99.4 CE | PASS | 99.4: «Si efectuadas las citadas votaciones no se otorgase la confianza para la investidura, se tramitarán sucesivas propuestas en la forma prevista en los apartados anteriores.» Verbatim. Order 3 → 4 is stated («efectuadas las citadas votaciones»). In prose at l. 147. | — |
| 5 | Disolución de ambas Cámaras y nuevas elecciones por el Rey, con refrendo del Presidente del Congreso, si ningún candidato obtuvo la confianza — dos meses a partir de la primera votación | art. 99.5 CE | PASS | 99.5: «Si transcurrido el plazo de dos meses, a partir de la primera votación de investidura, ningún candidato hubiere obtenido la confianza del Congreso, el Rey disolverá ambas Cámaras y convocará nuevas elecciones con el refrendo del Presidente del Congreso.» Verbatim, keeping the plazo, its starting point, the condition and the refrendo. In prose at l. 147. Order: the step comes after 2–4, and its plazo field ties the two months to the first vote (step 2) and not to step 4, so the timeline does not suggest that the plazo starts after the sucesivas propuestas. | — |

Majorities and plazos: absolute majority of members (first vote), simple majority (second vote), 48 hours «después de
la anterior», two months «a partir de la primera votación de investidura». All are exact against art. 99. Title: the
block lists every vote and every plazo of art. 99. It leaves out 99.2 (the candidate's programme), which is neither a
vote nor a plazo, so the title does not overclaim. PASS.

## tabla «La cuestión de confianza y la moción de censura» (l. 241–252)

| # | row (short) | citation | PASS/FAIL | passage / reason | replacement |
|---|---|---|---|---|---|
| 1 | Cuestión de confianza — Presidente, previa deliberación del CM, ante el Congreso, sobre su programa o declaración de política general; mayoría simple | art. 112 CE | PASS | 112: «El Presidente del Gobierno, previa deliberación del Consejo de Ministros, puede plantear ante el Congreso de los Diputados la cuestión de confianza sobre su programa o sobre una declaración de política general. La confianza se entenderá otorgada cuando vote a favor de la misma la mayoría simple de los Diputados.» Verbatim («de la misma» dropped). In prose at l. 221. | — |
| 2 | Cuestión de confianza, con el Presidente en funciones — no puede plantearla | art. 21.4 Ley 50/1997 | PASS | 21.4: «El Presidente del Gobierno en funciones no podrá ejercer las siguientes facultades: … b) Plantear la cuestión de confianza.» Faithful. In prose at l. 175 and l. 277, cited «art. 21.4». One norm. | — |
| 3 | Cuestión de confianza, si el Congreso niega su confianza — dimisión al Rey; nuevo Presidente según el art. 99 | art. 114.1 CE | PASS | 114.1: «Si el Congreso niega su confianza al Gobierno, éste presentará su dimisión al Rey, procediéndose a continuación a la designación de Presidente del Gobierno, según lo dispuesto en el artículo 99.» A faithful shortening, word for word the prose at l. 223. | — |
| 4 | Moción de censura — mayoría absoluta; propuesta por al menos la décima parte de los Diputados; incluye un candidato | art. 113.1–2 CE | PASS | 113.1: «…mediante la adopción por mayoría absoluta de la moción de censura.» 113.2: «La moción de censura deberá ser propuesta al menos por la décima parte de los Diputados, y habrá de incluir un candidato a la Presidencia del Gobierno.» Faithful, with the majority and the threshold kept. In prose at l. 227 and l. 229, and the same range at l. 269. | — |
| 5 | Moción de censura, votación — no antes de cinco días; mociones alternativas en los dos primeros días | art. 113.3 CE | PASS | 113.3: «La moción de censura no podrá ser votada hasta que transcurran cinco días desde su presentación. En los dos primeros días de dicho plazo podrán presentarse mociones alternativas.» Verbatim. In prose at l. 230. | — |
| 6 | Moción de censura no aprobada — signatarios no pueden presentar otra en el mismo período de sesiones | art. 113.4 CE | PASS | 113.4: «Si la moción de censura no fuere aprobada por el Congreso, sus signatarios no podrán presentar otra durante el mismo período de sesiones.» The label carries the condition. In prose at l. 231. | — |
| 7 | Moción de censura adoptada — dimisión; candidato investido; el Rey le nombra | art. 114.2 CE | PASS | 114.2: «…el Gobierno presentará su dimisión al Rey y el candidato incluido en aquélla se entenderá investido de la confianza de la Cámara a los efectos previstos en el artículo 99. El Rey le nombrará Presidente del Gobierno.» The row, like the prose at l. 233, drops «a los efectos previstos en el artículo 99». It states that effect straight after («y el Rey le nombra Presidente del Gobierno»), so it does not read wider (see Notes). | — |
| 8 | Moción de censura en trámite — no puede proponerse la disolución | art. 115.2 CE | PASS | 115.2: «La propuesta de disolución no podrá presentarse cuando esté en trámite una moción de censura.» Faithful. In prose at l. 239. | — |

Order: a tabla makes no claim of order. One article per row, as the spec's choice for bloque I asks. Title: the table
covers every rule in CE arts. 112–114 and the two rules elsewhere that the prose ties to these figures (art. 21.4 Ley
50/1997, art. 115.2 CE), so it does not read a selective list as complete. PASS.

## Placement

- arbol (l. 115): after the last paragraph it summarises (Gabinetes, l. 113), closing «Los órganos de colaboración y
  apoyo del Gobierno», and before «Designación». Every node's fact is in prose above it (l. 11–113). PASS.
- plazos (l. 149): straight after the investidura paragraphs (l. 138–147), before «Vicepresidentes y Ministros». PASS.
- tabla (l. 241): after «La cuestión de confianza» (l. 221–223), «La moción de censura» (l. 227–233) and «La
  disolución» (l. 237–239), which holds row 8's art. 115.2. Row 2's art. 21.4 is at l. 175. It sits before the estados
  section. PASS.

## Notes

- arbol root 1: its fact is «se compone del Presidente, … y de los Ministros», but its children also include the Consejo
  de Ministros and the Comisiones Delegadas, which are organs and not members. The dependency is sound (arts. 1.3, 5.1),
  but a reader may take the two organs as components. Not a FAIL. A writer who wants it cleaner could cite art. 1.3 on
  those two nodes' labels. The prose cites it at l. 13, so the loader would accept it.
- arbol node 10, and the prose at l. 94: the 8.2 rule for when the Comisión's President is absent («la presidencia
  recaerá en el Ministro que corresponda según el orden de precedencia…») is in neither. It is a substitution, not a
  limit, so it is not a FAIL.
- plazos: steps 2 and 4 put a majority and a condition in the second field, where a timeline shows the plazo. The
  content is exact. This is a rendering choice, not a FAIL. The prose already numbers the two votes at l. 142–145, but
  the esquema adds 99.1, 99.4 and 99.5, so it does not just repeat a list the prose already has.
- tabla row 7, and the prose at l. 233: «a los efectos previstos en el artículo 99» is dropped in both. The effect is
  then stated (the Rey's nombramiento), so neither reads wider. It could be restored in both together.
- Glossary marks: every glossary term the esquemas write appears first in the prose above them: g-organo-colegiado
  l. 57, g-comisiones-delegadas l. 13, g-ministro-sin-cartera l. 51, g-organos-superiores l. 86, g-investidura l. 136,
  g-refrendo l. 147, g-cuestion-de-confianza l. 32, g-gobierno-en-funciones l. 163, g-mocion-de-censura l. 185. So I
  expect no mark to move and no new mark to appear. I did not regenerate `glossary-links.es.txt` (this review writes no
  content files), so the writer should confirm with the generator.
- Voice: nothing in the three blocks is on the voice page's «never does» list. Labels name the organ, step or figure.
  No list-row citation ends in a letter, and no field holds a spaced em dash.
- Citation forms «art. 8.1–2» and «art. 113.1–2 CE» are ranges of apartados. The loader reads them as art. 8 and
  art. 113, which the prose cites. «arts. 7–10» also resolves (see node 8), but that is a platform result and not a
  prose citation.

## Counts

25 rows: 24 PASS, 1 FAIL (arbol node 8, the «Órganos de colaboración y apoyo del Gobierno (arts. 7–10 Ley 50/1997)»
root). Nesting PASS otherwise. Order (plazos) PASS. Titles PASS. Placement PASS.
