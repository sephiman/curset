# Standalone read — I.2 (`m01-l02`), R2d fix pass, 2026-11-18

| id | line | sentence (start) | problem | minimal fix |
|---|---|---|---|---|
| 1 | 176 | Sin perjuicio de lo anterior, el resultado de la investigación… (76.1) | «lo anterior» two sentences and a paragraph away from its 76.1 referent (76.2 sentence sat between) | move: 76.1 pair together, 76.2 pair together |
| 2 | 460 | Durante ese plazo, las Cortes podrán tramitarlos… (86.3) | «ese plazo» and «-los» point two sentences back | reword |
| 3 | 255 | En el Congreso, el suplicatorio se entiende denegado… (14.2 RC) | sits after the «No confundir» block, far from the art. 71.2 authorisation it concerns | move next to art. 71.2 |
| 4 | 340 | Son también Comisiones Permanentes, además de las legislativas… | «las legislativas» named only in the next sentence | move after the Legislativas esquema |
| 5 | 685 | Se dirige a ellas a través de los Presidentes… | elided subject (Defensor) after a sentence whose subject is the Cortes | reword |
| 6 | 743 | Debe cesar en toda situación de incompatibilidad… | elided subject after an esquema | reword |
| 7 | 796 | Da cuenta anualmente a las Cortes Generales… | elided subject under a heading only | reword |
| 8 | 865 | Corresponde al Ministerio Fiscal esta denominación… (2.2 EOMF) | «esta denominación» has no antecedent | reword |
| 9 | 899 | Ejerce sus competencias en todo el territorio nacional… (558) | elided subject; previous sentence's subject is «La ley orgánica» | reword |
| 10 | 939 | …no ha designado a sus Vocales en plazo (570.2) | «en plazo» without which plazo | reword |
| 11 | 1017 | El Consejo emite su informe en el plazo improrrogable… (561.2) | «su informe» after an esquema; which report | reword |
| 12 | 1062 | Se compone de su Presidente… (54 LOPJ) | elided subject; previous sentence's subject is the Presidente | reword |
| 13 | 1083 | …números segundo y tercero del párrafo anterior (57.2) | «párrafo anterior» is an esquema | reword |
| 14 | 1199 | Sus libros I a IV y VIII… | «Sus» follows «El título preliminar regula…» | reword |

Reviewed and not flagged (referent in the same or the immediately preceding sentence/bullet): 162.3 «restantes», 166.1,
77.2, 78.4, 82.3 sentences (same bullet), 95.2 «esa contradicción», 96.1, LO 3/1984 7.3 «Este plazo/Agotado el plazo»,
RC 110–123 «Si…», «Las enmiendas…», «Concluido el informe…» (each follows its own bullet), 124.2, 439 ter.2 «En ella»,
«Sus capítulos regulan:», «estos medios de control» (its lead-in names arts. 108–111). Normativa: matches the citations
(cites.py 0 unresolved). Flagged 14

## Fixes

| id | action | old → new (source checked) |
|---|---|---|
| 1 | moved | 76.1 second sentence placed straight after 76.1 first; 76.2 pair follows |
| 2 | reworded | «Durante ese plazo, las Cortes podrán tramitarlos» → «Durante el plazo de treinta días del artículo 86.2, las Cortes podrán tramitar los Decretos-leyes» (CE 86.2–3) |
| 3 | moved | suplicatorio paragraph now follows art. 71.2 paragraph |
| 4 | moved | sentence now follows the 23-row esquema |
| 5 | reworded | «Se dirige a ellas» → «El Defensor se dirige a ellas» (LO 3/1981 2.1) |
| 6 | reworded | «Debe cesar» → «El Defensor debe cesar» (7.2) |
| 7 | reworded | «Da cuenta anualmente» → «El Defensor da cuenta anualmente» (32.1) |
| 8 | reworded | «esta denominación» → «la denominación «Ministerio Fiscal»» (EOMF 2.Dos) |
| 9 | reworded | «Ejerce sus competencias» → «El Consejo ejerce sus competencias» (LOPJ 558) |
| 10 | reworded | «en plazo» → «en el plazo legalmente previsto» (LOPJ 570.2 wording) |
| 11 | reworded | «su informe en el plazo» → «su informe sobre los anteproyectos de ley y disposiciones generales de esas materias en el plazo» (561.1–2) |
| 12 | reworded | «Se compone de su Presidente» → «El Tribunal Supremo se compone de su Presidente» (54) |
| 13 | reworded | «del párrafo anterior» → «del apartado 1» (57.1–2) |
| 14 | reworded | «Sus libros I a IV y VIII» → «Los libros I a IV y VIII de la LOPJ» |

Removed: 0. Pool sentences added: 0.
