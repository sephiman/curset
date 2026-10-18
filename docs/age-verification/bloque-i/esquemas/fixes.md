# R2c esquemas bloque I and bloque V items — fixes after the blind pass, 2026-10-18

Writer's record of what changed for each FAIL in `verify-m05.md`, `verify-m01-l01.md`, `verify-m01-l02-l03.md`,
`verify-m01-l03-mayorias.md`, `verify-m01-l04.md`, `verify-m01-l05.md`, `verify-m01-l07-l08.md` and
`verify-m01-l09-l10-l11.md`. Bloque I prose untouched.

| # | Lesson · item | FAIL | Fix applied |
|---|---|---|---|
| 1 | m05-l06 · «Pagos a cuenta y pagos anticipados» (art. 34.4 LGS) | verify-m05 #4: dropped the «En ningún caso…» exception and «régimen de garantías»; extended «cuando la naturaleza…» to anticipados | Reviewer's split: rows «Pagos a cuenta» and «Pagos anticipados»; header «Fase o caso» (note) |
| 2 | m01-l03 · title of the mayorías table | verify-m01-l03-mayorias T: reads as complete (93.1 RS and 39.1 RC missing) | Title «Algunos quórum y mayorías de las Cortes Generales» |
| 3 | m01-l07 · plazos row 2 citation | verify-m01-l07-l08: «arts. 23.2 y 24.1–2» parses «24.1–2» as a range art. 24 → art. 2 | «(arts. 23.2, 24.1 y 24.2 Ley 19/2013)» |
| 4 | m01-l08 · arbol node «Director Insular» (art. 70 LRJSP) | verify-m01-l07-l08: placed under the Delegado in every case; art. 70 makes it depend on the Subdelegado where one exists | Node removed; title «El Delegado del Gobierno y los Subdelegados» |
| 5 | m01-l01 · title of esquema 2 | verify-m01-l01 T2: reads as every plazo of the three (arts. 76, 35.2 LOTC give more; prose lacks them) | Title «Tres plazos ante el Tribunal Constitucional» |
| 6 | m01-l03 · plazos Senado, step 2 (art. 90.2–3 CE) | verify-m01-l02-l03 #2: dropped the veto's mayoría absoluta; read the veto/enmiendas as always happening | Reviewer's step: «El Senado puede … el veto deberá ser aprobado por mayoría absoluta — …» |
| 7 | m01-l03 · plazos Senado, step 3 (art. 90.2 CE) | verify-m01-l02-l03 #3: enmiendas branch missing, so enmiendas → sanción read as the order | Reviewer's step «Pronunciamiento del Congreso, antes de la sanción», both branches |
| 8 | m01-l03 · arbol node Comisiones del Senado (art. 53.2 RS) | verify-m01-l02-l03 #12: «en su primera reunión», «de entre sus miembros» not in the prose | The prose's wording |
| 9 | m01-l05 · arbol root «Órganos de colaboración y apoyo del Gobierno (arts. 7–10 Ley 50/1997)» | verify-m01-l05: the prose never cites the range; the grouping is only a heading | Root removed; its four children become roots |
| 10 | m01-l04 · arbol 1 title | verify-m01-l04 T1: reads as all the CGPJ's organs (Presidencia, Promotor, órganos técnicos missing) | «El Consejo General del Poder Judicial: composición, Pleno y Comisiones» |
| 11 | m01-l04 · tabla title | verify-m01-l04 T2: reads as all its majorities (580.4, 589.4–5, 599.3) | «… en algunos acuerdos …» |
| 12 | m01-l04 · tabla row 8 (art. 630.1 LOPJ, tres quintos) | verify-m01-l04 #8: cuts the 630.1 list after its first item; the prose (l. 184–185) has the same cut | Row removed; prose gap |
| 13 | m01-l09 · «Cinco materias…», Medio ambiente row (148.1.9.ª / 149.1.23.ª) | verify-m01-l09-l10-l11: the prose never pairs them | Row removed; prose gap |
| 14 | m01-l09 · same table, Ferrocarriles row (148.1.5.ª / 149.1.21.ª) | Same | Row removed; prose gap; title «Tres materias…» |
| 15 | m01-l09 · same table, «Puertos y aeropuertos» | The prose pairs puertos only | Label «Puertos»; 149 cell «20.ª Puertos de interés general» |
| 16 | m01-l10 · «El municipio, la provincia y la isla…», Isla row | «—» under «Personalidad jurídica» reads as a denial; «Gobierno» not in 141.4 | Reviewer's shape: one «Qué establece» column |
| 17 | m01-l11 · votación table, art. 16.4 TUE row | Reads as the only mayoría cualificada rule (238.2 TFUE left out) | Not the reviewer's fix: a 238.2 row would drop its «a reserva de … Protocolo» clause, which the prose lacks. The cell takes 16.4's own last párrafo («Las demás modalidades … en el apartado 2 del artículo 238 …»), and the title becomes «Algunas reglas de votación…» |

## After `recheck.md` (5 FAILs)

| # | Lesson · item | FAIL | Fix applied |
|---|---|---|---|
| 21 | m01-l01 · title of «Tres plazos ante el Tribunal Constitucional» | Only 33.1 is a plazo before the TC; 161.2 is the TC's own, 35.2 the parties' before the judge | «Tres plazos: la suspensión del artículo 161.2, el recurso y la cuestión de inconstitucionalidad» |
| 22 | m01-l04 · row «Acuerdos, salvo que la ley disponga otra cosa» (art. 630.1 LOPJ) | With the nombramientos row gone (fix 9), the default reads as covering the three-fifths appointments; the prose names only part of 630.1's list | Row removed; prose gap (the table now has no 630.1 row) |
| 23 | m01-l10 · header «Qué establece» | With the title, read as all that arts. 140–141 say | «Personalidad, gobierno y administración» |
| 24 | m01-l10 · municipio row (art. 140 CE) | «Gozarán…» had no subject | «Los municipios gozarán de personalidad jurídica plena. …» |
| 25 | m01-l11 · art. 16.4 TUE row | The pointer sentence to 238.2 is not in the prose; the label let the 55 % rule read as the only definition | Label «…, salvo el caso del artículo 238.2 del Tratado de Funcionamiento de la Unión Europea»; pointer sentence cut. The reviewer's 238.2 TFUE row is not added: 238.2 opens «a reserva de las disposiciones fijadas en el Protocolo sobre las disposiciones transitorias», which the prose leaves out (listed as a prose gap) |

## Round prompt follow-up (m01-l07, m01-l08)

The user asked for four things: fix the Director Insular placement (already fix 4: the node was removed); fix the
CTBG naming in the m01-l07 timeline; close the two m01-l08 prose gaps (arts. 58.1 and 58.4 LRJSP); and add the Ministry
tree those gaps blocked. Blind check: `verify-m01-l07-l08-adiciones.md`.

| # | Lesson · item | FAIL | Fix applied |
|---|---|---|---|
| 26 | m01-l07 · plazos row 2, first draft «salvo en los supuestos de la disposición adicional cuarta» | Read wider than DA 4.ª (the CTBG resolves under a convenio, DA 4.ª.2; DA 4.ª.1 párr. 2 and 4.ª.3 not in the prose); the norm's own wording for the exception is art. 24.6, which the prose did not cite | Reviewer's option A. New prose bullet, verbatim: «La competencia para conocer de las reclamaciones corresponde al Consejo, salvo en aquellos supuestos en que las Comunidades Autónomas atribuyan dicha competencia a un órgano específico, de acuerdo con la disposición adicional cuarta (art. 24.6 Ley 19/2013).» The row's label takes the 24.6 wording and cites «arts. 23.2, 24.1, 24.2 y 24.6 Ley 19/2013»; the title drops «ante el Consejo…» |
| 27 | m01-l07 · plazos row 2 label (art. 24.6) | recheck-3: «dicha competencia» without its referent, «de acuerdo con la disposición adicional cuarta» dropped; two tangled «salvo» clauses | Reviewer's label: «…, potestativa y previa a la vía contencioso-administrativa, salvo en aquellos supuestos en que las Comunidades Autónomas atribuyan la competencia a un órgano específico, de acuerdo con la disposición adicional cuarta; contra las resoluciones de los órganos del artículo 2.1.f) solo cabe recurso contencioso-administrativo» |
| 28 | m01-l07 · plazos row 2 label | recheck-4: «solo cabe recurso contencioso-administrativo» right before the plazo read as a one-month contencioso plazo; the 24.6 «salvo» read as an exception to «potestativa y previa» | Reviewer's order: 2.1.f) exclusion first, then «potestativa y previa…», then «la competencia corresponde al Consejo, salvo … de acuerdo con la disposición adicional cuarta» |
