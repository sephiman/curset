# Verification — `m02-l10`, re-check 2 (blind)

Verifier: blind, 2026-11-06. Did not write the lesson; checked against the saved pages in `content/age-auxiliar-c2/sources/otros/` (HTML stripped to text; Windows desktop sections, located by the pages' `data-tab` panels). Input: `docs/age-verification/c2/bloque-ii/pending/m02-l10.md` (6 items), lesson
`content/age-auxiliar-c2/es/lessons/m02-l10.md`. Pages read: `ms-access-dias-entre-fechas.html`, `ms-access-tareas-basicas.html`,
`ms-access-informes-simples.html`.

New pages (`descarga nueva`, 2026-11-06): the sha256 of each of the three files matches `writer/m02-l10-fix-fuentes.yaml`
and `sources/otros/fuentes.yaml`; each has `lang="es-ES"`, a canonical URL equal to the recorded one, and the Spanish
article title recorded.

| id | verdict | precept checked | note | replacement |
|---|---|---|---|---|
| `6a3220b063` | PASS | ms-access-dias-entre-fechas.html | «En la pestaña Datos de la hoja de propiedades, en el cuadro de propiedades Origen del control»; «=DifFecha("d",Fecha(),[FechaDucido])» («;» per §12 item 20); «La "d" indica a Access que calcule el número de días»; «resta la fecha de hoy (Date()) de la Due Date» | — |
| `a67feb2d8a` | PASS | ms-access-tareas-basicas.html; «Cómo importar o vincular a datos» | table Origen / Importar / Vincular: row «Documento HTML», Importar «Sí», Vincular «Sí» | — |
| `c2cc1ed624` | PASS | ms-access-informes-simples.html | «Después de obtener una vista previa del informe, puede exportar los resultados a Word, Excel u otros programas de Office. En la pestaña Datos externos, en el grupo Exportar, haga clic en el botón del formato que desee» | — |
| `40da7799d6` | PASS | Fuentes | title and date match the saved page; cited in the prose | — |
| `c7336dcbd4` | PASS | Fuentes | title and date match the saved page; cited in the prose | — |
| `c55c230ac0` | PASS | Fuentes | title and date match the saved page; cited in the prose | — |

PASS 6, FAIL 0.

«Fuentes» section: 32 files cited in the prose, 32 listed, the same set.
