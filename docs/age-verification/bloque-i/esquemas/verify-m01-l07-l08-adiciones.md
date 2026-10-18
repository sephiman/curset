# Blind verification — m01-l07 plazos and m01-l08 art. 58 additions, 2026-10-18

Reviewer did not write the changes. Scope: (1) the two new prose sentences of m01-l08 «Organización interna»;
(2) the new m01-l08 arbol «Organización interna de los Ministerios»; (3) the m01-l07 plazos «Plazos de la
resolución de acceso y de la reclamación», whole. Other new esquemas in the same diff (m01-l07 art. 19 tabla,
m01-l08 art. 55 and Delegado arboles) were not in scope and were not checked.

Rule: `spec.md` in this folder. Norm texts: scratchpad `txt/` (LRJSP `BOE-A-2015-10566_lrjsp_2024-08-02.txt`, art. 58;
Ley 19/2013 `BOE-A-2013-12887_ley-transparencia_2022-07-09.txt`, arts. 2.1.f), 20, 23, 24, DA 4.ª). Voice:
`docs/prose-voice.md`. Citations were run through `tradeschool.citations.grammar.parse_segment`: every one parses
as one segment, one norm (row 2 of item 3 gives units art. 23, art. 24, da cuarta, norm Ley 19/2013), and every
anchor is one the prose already cites.

Glossary: no mark moves or appears. `silencio administrativo` (origin m01-l07) first occurs in the prose at
art. 24.2, before the plazos; `servicios comunes` (origin m01-l08) first occurs at art. 55.2, before both arboles.

## 1. m01-l08, «Organización interna» — new prose sentences

| # | row/sentence (short) | citation | PASS/FAIL | passage / reason | replacement |
|---|---|---|---|---|---|
| 1.1 | «De ellas dependen jerárquicamente los órganos directivos que se les adscriban» | art. 58.1 LRJSP | PASS | 58.1: «De ellas dependerán jerárquicamente los órganos directivos que se les adscriban.» Verbatim, future changed to present. «ellas» refers back to the Secretarías de Estado and Generales of the previous sentence, as in the article. Voice is fine: one fact, and the opener is not on the blacklist. | — |
| 1.2 | «Las Subdirecciones Generales pueden adscribirse también directamente a otros órganos directivos de mayor nivel o a órganos superiores del Ministerio» | art. 58.4 LRJSP | PASS | 58.4: «Sin perjuicio de lo anterior, podrán adscribirse directamente Subdirecciones Generales a otros órganos directivos de mayor nivel o a órganos superiores del Ministerio.» «también» renders «sin perjuicio de lo anterior», and both destinations are kept. It fits right after the DG/SG sentence it qualifies. «también» is mid-sentence, not the blacklisted «También es…» opener. | — |

## 2. m01-l08, arbol «Organización interna de los Ministerios»

| # | row/sentence (short) | citation | PASS/FAIL | passage / reason | replacement |
|---|---|---|---|---|---|
| 2.1 | Root: Secretarías de Estado y Secretarías Generales, cuando existan — gestión de un sector de actividad; de ellas dependen los órganos directivos que se les adscriban | art. 58.1 LRJSP | PASS | 58.1, both sentences. «cuando existan» = «pueden existir». «sector de actividad» drops «administrativa», as the prose does. Not wider. | — |
| 2.2 | Root: Subsecretaría — todo Ministerio cuenta con una, servicios comunes | art. 58.2 LRJSP | PASS | 58.2: «contarán, en todo caso, con una Subsecretaría … para la gestión de los servicios comunes». | — |
| 2.3 | Child of 2.2: Secretaría General Técnica — depende de la Subsecretaría | art. 58.2 LRJSP | PASS | 58.2: «y dependiendo de ella una Secretaría General Técnica». The text states the link. | — |
| 2.4 | Root: Direcciones Generales — una o varias áreas funcionalmente homogéneas | art. 58.3 LRJSP | PASS | 58.3 verbatim, shortened. | — |
| 2.5 | Child of 2.4: Subdirecciones Generales — en ellas se organizan las DG; may be attached directly to other higher directive organs or superior organs | art. 58.4 LRJSP | PASS | 58.4, both sentences. The parent–child link is stated («Las Direcciones Generales se organizan en Subdirecciones Generales»). The node itself states the alternative attachment, so the tree does not claim that SGs always hang from a DG. | — |
| 2.6 | Roots side by side (2.1, 2.2, 2.4) | — | PASS | The tree draws no dependency between the roots. Under 58.1, a DG attached to a Secretaría de Estado depends on it. Node 2.1 says this in words, and the tree does not deny it. | — |
| 2.7 | Title «Organización interna de los Ministerios» | — | PASS | This is art. 58's own heading, and the tree renders all four of its apartados. The art. 59–68 organs are not implied. | — |
| 2.8 | Placement | — | PASS | It comes straight after the paragraph it summarises. The art. 68.1 servicios comunes paragraph follows it, inside the same subsection, so the tree replaces nothing. | — |

## 3. m01-l07, plazos «Plazos de la resolución de acceso y de la reclamación»

| # | row/sentence (short) | citation | PASS/FAIL | passage / reason | replacement |
|---|---|---|---|---|---|
| 3.1 | 1. Resolución de la solicitud de acceso — un mes desde la recepción, ampliable por otro mes …; silencio desestimatorio | arts. 20.1 y 20.4 Ley 19/2013 | PASS | 20.1, both paragraphs: «plazo máximo de un mes desde la recepción de la solicitud por el órgano competente para resolver … podrá ampliarse por otro mes … previa notificación al solicitante». 20.4: «se entenderá que la solicitud ha sido desestimada». The prose words are kept, with no condition dropped. | — |
| 3.2 | 2. Reclamación ante el CTBG, «salvo en los supuestos de la disposición adicional cuarta», potestativa y previa …, salvo contra los órganos del art. 2.1.f) — un mes … | arts. 23.2, 24.1, 24.2 y disposición adicional cuarta Ley 19/2013 | FAIL | The 23.2, 24.1 and 24.2 parts are faithful. The DA 4.ª clause reads wider than the DA. (a) It takes every DA 4.ª supuesto away from the CTBG. But DA 4.ª.2 lets a Comunidad «atribuir la competencia para la resolución de la reclamación prevista en el artículo 24 al Consejo de Transparencia y Buen Gobierno» by convenio, and in that supuesto the CTBG does resolve. The prose states that convenio, so the row contradicts its own prose. (b) «los supuestos de la disposición adicional cuarta» also points at content the prose does not state: DA 4.ª.1, second paragraph (against the Asambleas Legislativas and the autonomous counterparts of the Consejo de Estado, CES, Tribunal de Cuentas and Defensor del Pueblo, only a contencioso-administrativo appeal lies) and DA 4.ª.3 (Ciudades con Estatuto de Autonomía). So the prose does not state DA 4.ª as the row relies on: it states DA 4.ª.1, first paragraph, and DA 4.ª.2 only. (c) The norm's own words for this exception are art. 24.6: «salvo en aquellos supuestos en que las Comunidades Autónomas atribuyan dicha competencia a un órgano específico, de acuerdo con lo establecido en la disposición adicional cuarta». The prose does not cite art. 24.6. Readability: the label has two «salvo» clauses in a row. | **Needs a clause the prose lacks.** A: add art. 24.6 to the prose (e.g. after the art. 24.5 bullet: «La competencia corresponde al Consejo, salvo en los supuestos en que las Comunidades Autónomas la atribuyan a un órgano específico, de acuerdo con la disposición adicional cuarta (art. 24.6 Ley 19/2013).»). Then row 2 becomes: «Reclamación ante el Consejo de Transparencia y Buen Gobierno, potestativa y previa a la vía contencioso-administrativa, salvo contra las resoluciones de los órganos del artículo 2.1.f), contra las que solo cabe recurso contencioso-administrativo, y salvo en los supuestos en que las Comunidades Autónomas atribuyan la competencia a un órgano específico — un mes desde el día siguiente al de la notificación del acto o desde el día siguiente a aquel en que se produzcan los efectos del silencio administrativo (arts. 23.2, 24.1, 24.2 y 24.6 Ley 19/2013)». No rewording that uses only the current prose is faithful: «salvo cuando resuelva el órgano independiente que determine la Comunidad Autónoma» puts the DA 4.ª.1 second-paragraph institutions and the Ciudades back under the CTBG. B, if the prose stays untouched: drop the esquema (one step alone carries no order) and record in the ledger the prose gaps art. 24.6, DA 4.ª.1 second paragraph and DA 4.ª.3. |
| 3.3 | 3. Resolución y notificación de la reclamación — tres meses; desestimación | art. 24.4 Ley 19/2013 | PASS | 24.4: «El plazo máximo para resolver y notificar la resolución será de tres meses, transcurrido el cual, la reclamación se entenderá desestimada.» Verbatim. No dies a quo is added. | — |
| 3.4 | Order 1 → 2 → 3 | — | PASS | 24.2 runs the reclamation plazo from the notification of the act, or from when the silence takes effect, so it follows step 1 (20.1/20.4). Step 3 resolves the reclamation filed in step 2. 20.5's direct contencioso route is not a step, and the list claims no exclusivity. | — |
| 3.5 | Title | — | PASS | It names exactly the two things whose plazos are listed. It does not claim to cover every plazo of the procedure: the art. 19.2/19.3 suspensions are in the tabla above, and the art. 22.1 formalisation plazo belongs to a different act. | — |

## Totals

- Item 1: 2 checked, 2 PASS, 0 FAIL.
- Item 2: 8 checked (5 nodes, roots, title, placement), 8 PASS, 0 FAIL.
- Item 3: 5 checked (3 rows, order, title), 4 PASS, 1 FAIL (3.2, and its replacement needs a clause the prose lacks).
- Overall: 15 checked, 14 PASS, 1 FAIL.
