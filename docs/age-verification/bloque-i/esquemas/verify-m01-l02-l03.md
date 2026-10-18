# Verification — esquemas of m01-l02 and m01-l03 (2026-10-18)

I am a blind reviewer: I wrote neither these esquemas nor the lessons, and I did not read the writer's notes. Scope:
the tabla «La Regencia» in m01-l02 and, in m01-l03, the two `plazos` esquemas and the `arbol` «Las Cortes Generales:
las Cámaras y algunos de sus órganos». The tabla «Quórum y mayorías que recoge este tema» (m01-l03) is out of scope
(another reviewer). Rules: `spec.md` (this folder), the `::esquema` section of `docs/platform-delta-handoff.md`,
`docs/prose-voice.md`.

`git diff` of both lessons only adds lines (the five esquema blocks). No prose line changed.

Sources, all from the scratchpad `txt/` (`pdftotext -layout`), read with `art.py`; no norm wording taken from memory:

- CE (`BOE-A-1978-31229_ce_2026-05-20.txt`): arts. 59, 60, 61, 66, 68, 69, 75, 78, 90, 91.
- Reglamento del Congreso (`BOE-A-1982-5196_reglamento-congreso_2026-07-28.txt`): arts. 24, 25, 26, 27, 30, 39; the
  titles «De los Grupos Parlamentarios» and «De la organización del Congreso».
- Reglamento del Senado (`BOE-A-1994-10830_reglamento-senado_2025-11-14.txt`): arts. 5, 27, 28, 49, 53, 55.

`load_check.py` on the course: LOAD OK. `gl.py` (glossary marks): every term the esquemas write (g-regencia,
g-diputacion-permanente, g-grupo-parlamentario, g-grupo-mixto, g-junta-de-portavoces, g-veto) has its first prose
occurrence before the esquema, so no first mark moves.

Line numbers are those of the current files.

## m01-l02 — tabla «La Regencia» (l. 209–217)

| # | row (short) | citation | PASS/FAIL | passage / reason | replacement |
|---|---|---|---|---|---|
| 1 | Minoría de edad del Rey — padre o madre; en su defecto, pariente mayor de edad más próximo…; durante la minoría | art. 59.1 CE | PASS | 59.1: «Cuando el Rey fuere menor de edad, el padre o la madre del Rey y, en su defecto, el pariente mayor de edad más próximo a suceder en la Corona, según el orden establecido en la Constitución, entrará a ejercer inmediatamente la Regencia y la ejercerá durante el tiempo de la minoría de edad del Rey.» Verbatim. In prose at l. 192–195. | — |
| 2 | Inhabilitación…, si la imposibilidad es reconocida por las Cortes — Príncipe heredero si fuere mayor de edad; si no, como en la minoría | art. 59.2 CE | PASS | 59.2: «Si el Rey se inhabilitare para el ejercicio de su autoridad y la imposibilidad fuere reconocida por las Cortes Generales, entrará a ejercer inmediatamente la Regencia el Príncipe heredero de la Corona, si fuere mayor de edad. Si no lo fuere, se procederá de la manera prevista en el apartado anterior, hasta que el Príncipe heredero alcance la mayoría de edad.» The label keeps the condition. «se procede como en la minoría de edad» is the prose's own shortening (l. 201). In prose at l. 199–202. | — |
| 3 | No hay persona a quien corresponda — nombrada por las Cortes; una, tres o cinco personas | art. 59.3 CE | PASS | 59.3: «Si no hubiere ninguna persona a quien corresponda la Regencia, ésta será nombrada por las Cortes Generales, y se compondrá de una, tres o cinco personas.» Verbatim. In prose at l. 206–207. | — |
| 4 | Requisitos — ser español y mayor de edad | art. 59.4 CE | PASS | 59.4: «Para ejercer la Regencia es preciso ser español y mayor de edad.» In prose at l. 184–185. | — |
| 5 | Ejercicio — por mandato constitucional y siempre en nombre del Rey | art. 59.5 CE | PASS | 59.5: «La Regencia se ejercerá por mandato constitucional y siempre en nombre del Rey.» In prose at l. 184. | — |

Order: a tabla claims none; the rows follow 59.1–59.5. Title: the rows are all five apartados of art. 59, the whole
«Regencia» section of the lesson. PASS (see Notes on arts. 60.1 and 61.2).

## m01-l03 — plazos «Del fin del mandato a la convocatoria del Congreso electo» (l. 56–60)

| # | step (short) | citation | PASS/FAIL | passage / reason | replacement |
|---|---|---|---|---|---|
| 1 | Fin del mandato de los Diputados — cuatro años después de su elección o el día de la disolución | art. 68.4 CE | PASS | 68.4: «El mandato de los Diputados termina cuatro años después de su elección o el día de la disolución de la Cámara.» Verbatim. In prose at l. 46–47. | — |
| 2 | Elecciones — entre los treinta días y sesenta días desde la terminación del mandato | art. 68.6 CE | PASS | 68.6: «Las elecciones tendrán lugar entre los treinta días y sesenta días desde la terminación del mandato.» Verbatim. In prose at l. 52. | — |
| 3 | Convocatoria del Congreso electo — dentro de los veinticinco días siguientes a la celebración de las elecciones | art. 68.6 CE | PASS | 68.6: «El Congreso electo deberá ser convocado dentro de los veinticinco días siguientes a la celebración de las elecciones.» Verbatim. In prose at l. 52–54. | — |

Order: 1 → 2 rests on «desde la terminación del mandato», 2 → 3 on «siguientes a la celebración de las elecciones».
No false order. PASS.

## m01-l03 — plazos «Plazos de la tramitación en el Senado y de la sanción» (l. 359–364)

| # | step (short) | citation | PASS/FAIL | passage / reason | replacement |
|---|---|---|---|---|---|
| 1 | Remisión al Senado del proyecto aprobado por el Congreso — su Presidente dará inmediata cuenta… al Presidente del Senado, que lo somete a deliberación | art. 90.1 CE | PASS | 90.1: «Aprobado un proyecto de ley ordinaria u orgánica por el Congreso de los Diputados, su Presidente dará inmediata cuenta del mismo al Presidente del Senado, el cual lo someterá a la deliberación de éste.» The fact field is verbatim. In prose at l. 341–342. See Notes on the label «Remisión». | — |
| 2 | Veto o enmiendas del Senado, mediante mensaje motivado — dos meses…; veinte días naturales si urgente | art. 90.2–3 CE | FAIL | 90.2: «El Senado en el plazo de dos meses, a partir del día de la recepción del texto, puede, mediante mensaje motivado, oponer su veto o introducir enmiendas al mismo. El veto deberá ser aprobado por mayoría absoluta.» 90.3: «…se reducirá al de veinte días naturales en los proyectos declarados urgentes por el Gobierno o por el Congreso de los Diputados.» The plazos are exact. (a) The step drops the majority that 90.2 attaches to the veto, which the prose keeps at l. 345–346. Left out, a veto reads as an ordinary act of the Cámara (art. 79.2 CE, mayoría de los presentes), wider than the article. Step 3 gives the Congreso's majorities, so the omission is not a choice of the kind. (b) The label states veto o enmiendas as a step that always happens; 90.2 says «puede». The prose has both clauses. | `2. El Senado puede, mediante mensaje motivado, oponer su veto o introducir enmiendas; el veto deberá ser aprobado por mayoría absoluta — dos meses a partir del día de la recepción del texto; veinte días naturales en los proyectos declarados urgentes por el Gobierno o por el Congreso de los Diputados (art. 90.2–3 CE)` |
| 3 | Ratificación del texto inicial por el Congreso, en caso de veto — mayoría absoluta o, por mayoría simple, transcurridos dos meses | art. 90.2 CE | FAIL | 90.2: «El proyecto no podrá ser sometido al Rey para sanción sin que el Congreso ratifique por mayoría absoluta, en caso de veto, el texto inicial, o por mayoría simple, una vez transcurridos dos meses desde la interposición del mismo, o se pronuncie sobre las enmiendas, aceptándolas o no por mayoría simple.» The veto branch is faithful. The step leaves out the enmiendas branch. Step 2 opens two paths (veto o enmiendas) and step 3 closes only one, so on the enmiendas path the timeline reads 2 → 4: enmiendas, then sanción. 90.2 bars sanción until the Congreso «se pronuncie sobre las enmiendas». That is a false order and a dropped condition. The prose has the enmiendas clause at l. 349–351. | `3. Pronunciamiento del Congreso, antes de la sanción — en caso de veto, ratifica el texto inicial por mayoría absoluta o, por mayoría simple, una vez transcurridos dos meses desde la interposición del veto; en caso de enmiendas, se pronuncia sobre ellas, aceptándolas o no por mayoría simple (art. 90.2 CE)` |
| 4 | Sanción — el Rey las sancionará en quince días, las promulgará y ordenará su inmediata publicación | art. 91 CE | PASS | 91: «El Rey sancionará en el plazo de quince días las leyes aprobadas por las Cortes Generales, y las promulgará y ordenará su inmediata publicación.» Verbatim. In prose at l. 356–357. | — |

Order: 1 → 2 rests on 90.2 «a partir del día de la recepción del texto». 3 → 4 rests on 90.2 «no podrá ser sometido al
Rey para sanción sin que…». 2 → 3 holds only for the veto path as written. With the two replacements, every
conditional step carries its condition in the label: when the Senado neither vetoes nor amends, step 3 does not apply,
and the label says so. FAIL as written (steps 2–3), PASS with the replacements.

## m01-l03 — arbol «Las Cortes Generales: las Cámaras y algunos de sus órganos» (l. 279–296)

| # | node (short) | citation | PASS/FAIL | passage / reason | replacement |
|---|---|---|---|---|---|
| 1 | Cortes Generales — representan al pueblo español; Congreso y Senado | art. 66.1 CE | PASS | 66.1: «Las Cortes Generales representan al pueblo español y están formadas por el Congreso de los Diputados y el Senado.» Verbatim. In prose at l. 10–11. | — |
| 2 | Congreso — mínimo de 300 y máximo de 400 Diputados (under 1) | art. 68.1 CE | PASS | 68.1: «El Congreso se compone de un mínimo de 300 y un máximo de 400 Diputados, elegidos por sufragio universal…». A verbatim shortening that keeps both numbers. In prose at l. 37. The «formadas por» in 66.1 makes it a child of 1. | — |
| 3 | Pleno (under Congreso) | art. 75.1 CE | PASS | 75.1: «Las Cámaras funcionarán en Pleno y por Comisiones.» Label only. In prose at l. 162. | — |
| 4 | Comisiones (under Congreso) | art. 75.1 CE | PASS | Same passage. | — |
| 5 | Mesa — órgano rector; Presidencia, cuatro Vicepresidencias, cuatro Secretarías | art. 30 Reglamento del Congreso | PASS | 30.1: «La Mesa es el órgano rector de la Cámara y ostenta la representación colegiada de ésta en los actos a que asista.» 30.2: «La Mesa estará compuesta por la Presidencia del Congreso, cuatro Vicepresidencias y cuatro Secretarías.» A faithful shortening that drops the representación clause, which narrows. The citation matches the prose's «art. 30». In prose at l. 221–223. | — |
| 6 | Junta de Portavoces — las portavocías de los grupos; presidencia del Presidente del Congreso | art. 39.1 Reglamento del Congreso | PASS | 39.1: «Las personas designadas para las portavocías de los grupos parlamentarios constituyen la Junta de Portavoces, que se reunirá bajo la presidencia del Presidente o Presidenta del Congreso, que la convocará, a iniciativa propia o a petición de dos grupos parlamentarios o de la quinta parte de los miembros de la Cámara.» A verbatim fragment. Dropping the convocation clause narrows. In prose at l. 230–232. | — |
| 7 | Diputación Permanente (under Congreso) — mínimo de veintiún miembros… | art. 78.1 CE | PASS | 78.1: «En cada Cámara habrá una Diputación Permanente compuesta por un mínimo de veintiún miembros, que representarán a los grupos parlamentarios, en proporción a su importancia numérica.» Verbatim. «En cada Cámara» supports one under each Cámara. In prose at l. 184–185. | — |
| 8 | Grupos Parlamentarios — dentro de los cinco días siguientes a la sesión constitutiva, escrito a la Mesa | art. 24.1 Reglamento del Congreso | PASS | 24.1: «La constitución de Grupos Parlamentarios se hará, dentro de los cinco días siguientes a la sesión constitutiva del Congreso, mediante escrito dirigido a la Mesa de la Cámara.» Verbatim. In prose at l. 252–253. | — |
| 9 | Grupo Mixto (under Grupos Parlamentarios) — quien no queda integrado… | art. 25.1 Reglamento del Congreso | PASS | 25.1: «Los miembros de la Cámara que, conforme a lo establecido en los artículos precedentes, no quedarán integrados en un Grupo Parlamentario, en los plazos señalados, quedarán incorporados al Grupo Mixto.» Verbatim. Dependency: the Reglamento names it «Grupo Parlamentario Mixto» (art. 26) and «un Grupo Parlamentario, distinto del Mixto» (art. 27.2), so it is one of the Grupos. In prose at l. 253–254. | — |
| 10 | Senado — Cámara de representación territorial (under 1) | art. 69.1 CE | PASS | 69.1: «El Senado es la Cámara de representación territorial.» In prose at l. 64. | — |
| 11 | Pleno (under Senado) | art. 75.1 CE | PASS | As node 3. | — |
| 12 | Comisiones (under Senado) — en su primera reunión eligen de entre sus miembros una Mesa… | art. 53.2 Reglamento del Senado | FAIL | 53.2: «En su primera reunión, las Comisiones procederán a elegir de entre sus miembros una Mesa, que estará formada, por un Presidente, dos Vicepresidentes y dos Secretarios.» The node is faithful to the article, but the prose (l. 275–276) reads only «Cada Comisión elige una Mesa formada por un Presidente, dos Vicepresidentes y dos Secretarios». «En su primera reunión» and «de entre sus miembros» are facts the prose lacks. | `    - Comisiones — cada Comisión elige una Mesa formada por un Presidente, dos Vicepresidentes y dos Secretarios (art. 53.2 Reglamento del Senado)` (the prose's own wording, l. 275) |
| 13 | Comisión General de las CCAA (under Comisiones) — una excepción: Presidente, dos Vicepresidentes, cuatro Secretarios | art. 55 Reglamento del Senado | PASS | 55: «La Mesa de la Comisión General de las Comunidades Autónomas estará integrada por un Presidente, dos Vicepresidentes y cuatro Secretarios…». «Una excepción» is the prose's word (l. 276). Dependency: 49.2 «Serán Comisiones Legislativas la Comisión General de las Comunidades Autónomas…», and the prose presents it as an exception to «Cada Comisión». | — |
| 14 | Mesa (under Senado) — Presidente, dos Vicepresidentes, cuatro Secretarios | art. 5.1 Reglamento del Senado | PASS | 5.1: «…se procederá a la elección de la Mesa, que estará formada por el Presidente, dos Vicepresidentes y cuatro Secretarios.» In prose at l. 266–267. | — |
| 15 | Diputación Permanente (under Senado) | art. 78.1 CE | PASS | As node 7. | — |
| 16 | Grupos parlamentarios (under Senado) — al menos diez Senadores; ninguno en más de un Grupo | art. 27.1 Reglamento del Senado | PASS | 27.1: «Cada Grupo parlamentario estará compuesto, al menos, de diez Senadores. Ningún Senador podrá formar parte de más de un Grupo parlamentario.» Verbatim. In prose at l. 269–270. | — |

Nesting: the two Cámaras sit under the Cortes Generales («formadas por», 66.1). Each Cámara's Pleno, Comisiones and
Diputación Permanente rest on «las Cámaras» (75.1) and «en cada Cámara» (78.1). The Mesa, Junta and Grupos of each
Cámara rest on that Cámara's Reglamento. The Grupo Mixto sits under the Grupos and the CGCA under the Senado's
Comisiones, both supported as above. The arbol claims no order. No false dependency. Title: «algunos de sus órganos»
marks the selection (the Senado's Junta de Portavoces and the Congreso's Comisiones' Mesas, for example, are left
out). PASS.

## Placement

- m01-l02 tabla (l. 209): closes the «Regencia» section (l. 182–207), after all three supuestos and before «La tutela
  del Rey menor». PASS.
- m01-l03 plazos 1 (l. 56): directly after l. 46–54 (arts. 68.4 and 68.6), before «El Senado». PASS.
- m01-l03 arbol (l. 279): after «Los órganos del Senado» (l. 264–277), the last of the paragraphs it summarises
  (l. 10–11, 37, 64, 162, 184–185, 221–254, 266–277), before «La elaboración de las leyes». PASS.
- m01-l03 plazos 2 (l. 359): closes «Tramitación en el Senado, sanción y promulgación» (l. 341–357). PASS.

None of the four repeats a list or table that the prose already has.

## Notes

- Regencia, title: arts. 60.1 (Regente and tutor cannot be combined, except in the padre, madre or ascendientes
  directos) and 61.2 (the Regente's juramento) also deal with the Regencia, and the prose covers them in the next
  sections. The table holds all of art. 59 and matches the section heading, so it is not a FAIL. «La Regencia
  (art. 59 CE)» would rule out the reading.
- Regencia row 2 mixes the norm's «si fuere / Si no lo fuere» with the prose's present «se procede». Cosmetic.
- Regencia row 3 answers «quién la nombra», not «quién la ejerce», under the header «Quién la ejerce o qué se exige».
  The cell is verbatim, so it is not a FAIL.
- Plazos 2 step 1: the label «Remisión al Senado» is not in 90.1 or the prose (both say «dará / da inmediata
  cuenta»). It names the step and 90.2's «recepción del texto» implies it, so I did not fail it. «Aprobación del
  proyecto por el Congreso» would be the norm's own trigger, if the writer prefers. The label also drops «ordinaria u
  orgánica»; that does not widen it.
- Plazos 2 step 2: the citation «art. 90.2–3 CE» uses the range form that the prose uses elsewhere (m01-l01:
  «art. 18.2–3 CE», «art. 22.3–5 CE»), and the course loads OK with it.
- Arbol, title: the Reglamento del Congreso places the Grupos Parlamentarios in their own title («De los Grupos
  Parlamentarios»), apart from «De la organización del Congreso». The prose, though, lists them under «Los órganos
  del Congreso» (l. 217, l. 235), and the arbol follows the prose. Not a FAIL. «las Cámaras, sus órganos y sus grupos»
  would be stricter.
- Arbol node 9: that the Grupo Mixto is a Grupo Parlamentario comes from arts. 26–27 of the Reglamento, not the prose.
  The prose says only that members are «incorporado al Grupo Mixto». The node text is all from 25.1 and the prose, so
  only the nesting rests on the norm.
- Voice: no filler, triad or forbidden construction in any label or header.

## Counts

28 rows: 25 PASS, 3 FAIL (plazos «Plazos de la tramitación en el Senado y de la sanción» steps 2 and 3; arbol node 12,
Senado «Comisiones»). Order: plazos 1 PASS, plazos 2 FAIL as written (steps 2–3), arbol nesting PASS. Placement: PASS
(4/4). Glossary marks: none moves. Every replacement uses only clauses the prose already has.
