# Verify re-check 3 — `m01-l03` (round R2d, blind, Opus)

2026-11-18. 39 pending rows, one batch. Every sentence read as it stands in the lesson; all ids match the current text
(sha1[:10]). Sources: Ley 50/1997 (BOE-A-1997-25336, 2025-01-03), CE (2026-05-20), LRJSP (2024-08-02), RD 1009/2023
(2026-07-29), `normativa.yaml`.

Art. 2.2 Ley 50/1997 list (lines 26–41): fourteen items a)–n), complete and in order, n) last. Items b), f) and j) are
shortened (they omit «y velar por su cumplimiento», the Fuerzas Armadas clause and the approval of the Presidencia's
estructura orgánica); those rows are not pending here and are noted, not scored.

| id | verdict | precept checked | note | replacement |
|---|---|---|---|---|
| `13aa24e272` | PASS | art. 2.2.n) Ley 50/1997 | last item of the 2.2 list, in place; list a)–n) complete and in order | — |
| `575b51595b` | PASS | art. 13.1 Ley 50/1997 | the Ministers fallback and citation follow in the next sentence | — |
| `ae80eddfc3` | PASS | art. 6.1 Ley 50/1997 | — | — |
| `9a95f0d50d` | PASS | art. 6.4.a) Ley 50/1997 | «varios de sus Departamentos» keeps «que integren la Comisión»; citation in the next sentence | — |
| `ae8e7ca08a` | PASS | art. 113.4 CE | — | — |
| `17ecc63d36` | PASS | art. 24.1.b) Ley 50/1997 | verbatim | — |
| `b93206cf25` | PASS | art. 24.1.d) Ley 50/1997 | verbatim | — |
| `8f75369b5b` | PASS | art. 54.1 LRJSP (párrafo 2.º) | — | — |
| `dc05a48891` | PASS | art. 55.11 LRJSP | — | — |
| `fef5b496d7` | PASS | art. 21.2 LRJSP | sits under the AGE órganos colegiados paragraph (line 476) | — |
| `4a5ed551d1` | FAIL | art. 21.3 LRJSP | drops «en atención a la naturaleza de las funciones asignadas a tales órganos», the condition for designating the other members | En la composición de los órganos colegiados pueden participar, cuando así se determine, organizaciones representativas de intereses sociales, así como otros miembros que se designen por las especiales condiciones de experiencia o conocimientos que concurran en ellos, en atención a la naturaleza de las funciones asignadas a tales órganos (art. 21.3 LRJSP). |
| `2ba8b39add` | PASS | art. 22.2 LRJSP | «para los de este carácter» read as the ministeriales | — |
| `0830c59f94` | PASS | art. 22.3 LRJSP | citation in the next sentence | — |
| `2132a2e4a5` | PASS | art. 22.4 LRJSP | salvo and automatic extinction kept | — |
| `8baa77a33f` | PASS | arts. 19.2.d) and 15.2 LRJSP | the 15.2 description matches art. 15.2 | — |
| `4a59f59ece` | PASS | art. 19.2 LRJSP (último párrafo) and 15.2 | — | — |
| `287a0ecc45` | PASS | art. 19.3.a) LRJSP | «con la misma antelación mínima de dos días» = «en igual plazo» | — |
| `be50cd14d8` | FAIL | RD 1009/2023, preámbulo and articulado | «que cambia a menudo» is not in the norm | El Real Decreto 1009/2023, de 5 de diciembre, establece la estructura orgánica básica de los departamentos ministeriales y determina sus órganos directivos hasta el nivel de Dirección General. |
| `e1fd3c2bd7` | PASS | art. 62.2.j) LRJSP | — | — |
| `ff63132ff5` | PASS | art. 15.1 Ley 50/1997 | — | — |
| `74984020d5` | PASS | art. 63.1.g) LRJSP (párrafo 2.º) | «del párrafo anterior» resolved correctly | — |
| `4837e3257b` | PASS | art. 63.1.g) LRJSP (párrafo 3.º) | — | — |
| `993a7dc869` | PASS | art. 63.1.i) LRJSP | — | — |
| `ff8d381323` | PASS | art. 63.3 LRJSP | citation closes the next sentence | — |
| `55fd36d2d6` | FAIL | art. 64.3 LRJSP | the article states no such rule; it only sets «personas con cualificación y experiencia…» and the Ley 3/2015 idoneidad requirements (inference, not the norm's words). With this replacement, drop the next sentence «Se nombran entre personas…», which it absorbs | Los Secretarios generales se nombran entre personas con cualificación y experiencia en el desempeño de puestos de responsabilidad en la gestión pública o privada y han de reunir, en todo caso, los requisitos de idoneidad establecidos en la Ley 3/2015, de 30 de marzo, reguladora del ejercicio del alto cargo de la Administración General del Estado (art. 64.3 LRJSP). |
| `54b159f934` | PASS | art. 66.2 LRJSP | not scored: the next sentence (line 788) drops the «salvo que el Real Decreto de estructura permita que… su titular no reúna dicha condición de funcionario» exception | — |
| `d70ccab8ba` | PASS | art. 72.1 LRJSP | — | — |
| `c15ee2f166` | PASS | art. 73.1.c) 1.º LRJSP | — | — |
| `7288c5fb7e` | PASS | art. 73.3 LRJSP | verbatim | — |
| `02412ff0a1` | PASS | art. 73.4 LRJSP | — | — |
| `90843596b0` | PASS | art. 75.a) LRJSP | lead-in to 1.º–2.º | — |
| `43cd8d0ab2` | PASS | art. 75.a) 2.º LRJSP | — | — |
| `2c780d4edd` | FAIL | art. 75.b) LRJSP | «A estos efectos» covers «garantizando la seguridad ciudadana, todo ello dentro de las competencias estatales en la materia»; the row loses that scope | \| b) \| A los efectos de proteger el libre ejercicio de los derechos y libertades, garantizando la seguridad ciudadana dentro de las competencias estatales en la materia, el Subdelegado del Gobierno dirige las Fuerzas y Cuerpos de Seguridad del Estado en la provincia. \| art. 75 LRJSP \| |
| `f2449d93d7` | PASS | art. 79.1.c) LRJSP | — | — |
| `937c2454b9` | PASS | art. 79.2 LRJSP | — | — |
| `761b51cbd2` | PASS | art. 79.3 LRJSP | — | — |
| `a7e988856d` | PASS | CE | prose cites 97, 98, 99, 100, 101, 102, 103, 104, 107, 112–115 and nothing else; arts. 82, 86, 94 and 96.2 appear only in copied Ley 50/1997 text | — |
| `08ff372400` | PASS | LPAC | 117.2 in the 73.1.d) 2.º row; the law named at lines 476 (19.1), 1000 (89.2), 1014 (104) | — |
| `445e5b3a2a` | FAIL | normativa.yaml; arts. 55.10, 72.4 LRJSP, 11 Ley 50/1997 | Ley 3/2015 now has an entry in `normativa.yaml` (added in R2d, BOE-A-2015-3444), so «no figuran» is wrong for it: give it its own line «- Ley 3/2015 (alto cargo): nombrada en los arts. 55.10 y 72.4 LRJSP y en el art. 11 Ley 50/1997.». Also missing from the Normativa block: LOTC, named at line 294 (art. 29.4 Ley 50/1997, «Ley Orgánica reguladora del mismo»), and LO 3/1980 del Consejo de Estado, named at line 322 (disposición adicional segunda Ley 50/1997): both are in `normativa.yaml` and each needs its own line («- LO 2/1979 (LOTC): nombrada en el art. 29.4 Ley 50/1997.», «- LO 3/1980 (Consejo de Estado): nombrada en la disposición adicional segunda Ley 50/1997.»). The Reglamento del Consejo de Estado named at line 322 goes in this line | RDLeg 3/2011, Ley de Contratos del Sector Público, Ley 2/2014, Ley de Fundaciones, Ley de Organización y Funcionamiento de la Administración General del Estado y Reglamento del Consejo de Estado: nombrados en los arts. 62.2.e), 80, 103.1, 104 y 130 LRJSP, en el art. 7.3 Ley 50/1997 y en su disposición adicional segunda; no figuran en `normativa.yaml`. |

PASS 35 · FAIL 4
