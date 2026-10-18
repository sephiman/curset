# Verification — esquemas of m01-l04 (2026-10-18)

I am a blind reviewer: I wrote neither these esquemas nor the lesson, and I read none of the writer's notes. Scope: the
three `:::esquema` blocks that `git diff C/es/lessons/m01-l04.md` shows as added. The diff only adds lines: two hunks,
+28 and +18, with no `-` line, so no prose line changed. Rules: `spec.md` (this folder) and the `::esquema` section of
`docs/platform-delta-handoff.md`. Sources: scratchpad `txt/BOE-A-1978-31229_ce_2026-05-20.txt` (CE), arts. 122 and 123;
`txt/BOE-A-1985-12666_lopj_2025-02-17.txt` (LOPJ consolidated 2025-02-17), arts. 53–55, 61, 62–64, 70–72, 566, 567,
580, 582, 586–589, 595, 599, 604 and 630, plus the headings of Títulos IV–V of Libro VIII. I read them with `art.py` and
`grep`, and took no norm wording from memory. Line numbers are those of the current lesson file.

## arbol «Composición y órganos del Consejo General del Poder Judicial» (l. 188–200)

| # | node (short) | citation | PASS/FAIL | passage / reason | replacement |
|---|---|---|---|---|---|
| 1 | CGPJ — el órgano de gobierno del Poder Judicial | art. 122.2 CE | PASS | 122.2: «El Consejo General del Poder Judicial es el órgano de gobierno del mismo.» A faithful shortening, with «del mismo» resolved to the Poder Judicial as in the prose at l. 76. | — |
| 2 | Presidente — el Presidente del TS, que lo preside | art. 122.3 CE | PASS | 122.3: «…estará integrado por el Presidente del Tribunal Supremo, que lo presidirá, y por veinte miembros…». The text says the Presidente is part of the CGPJ, so the dependency holds. In prose at l. 81. | — |
| 3 | Veinte miembros nombrados por el Rey por un período de cinco años | art. 122.3 CE | PASS | 122.3: «…y por veinte miembros nombrados por el Rey por un período de cinco años.» Verbatim. The dependency holds («integrado por»). In prose at l. 81–82. | — |
| 4 | Pleno | art. 595.1 LOPJ | PASS | 595.1: «…el Consejo General del Poder Judicial ejerce sus atribuciones en Pleno o a través de las Comisiones previstas en esta Ley Orgánica.» The Pleno is a form of the Consejo, so the dependency holds. In prose at l. 159. | — |
| 5 | Comisiones | art. 595.2 LOPJ | PASS | 595.2: «En el Consejo General del Poder Judicial existirán las siguientes Comisiones:». The dependency holds. In prose at l. 159–161. | — |
| 6–11 | Permanente, De Calificación, Disciplinaria, De Asuntos Económicos, De Igualdad, De Supervisión y Control de Protección de Datos (children of Comisiones) | art. 595.2 LOPJ (Disciplinaria: 604.1) | PASS | 595.2: «Permanente, de Calificación, Disciplinaria, de Asuntos Económicos, de Igualdad y de Supervisión y Control de Protección de Datos.» All six are there, in the norm's order. The statutory list is complete. Art. 599.3, under which the Pleno may create other Comisiones, is a power and not part of the list (see Notes). In prose at l. 159–161. | — |
| 9 (detail) | Disciplinaria — resuelve los expedientes por infracciones graves y muy graves…, salvo cuando la sanción propuesta es la separación del servicio | art. 604.1 LOPJ | PASS | 604.1: «A la Comisión Disciplinaria compete resolver los expedientes disciplinarios incoados por infracciones graves y muy graves e imponer, en su caso, las sanciones que correspondan a Jueces y Magistrados, con la sola excepción de aquellos supuestos en que la sanción propuesta fuere de separación del servicio.» A faithful shortening that keeps the exception. It is word for word the prose at l. 179–180. | — |
| T | Title «Composición y órganos del Consejo General del Poder Judicial» | — | FAIL | The title reads as the full set of the Consejo's organs. Título IV of the LOPJ, «De los órganos del Consejo General del Poder Judicial», has more than the Pleno and the Comisiones. Its Capítulo I is «La Presidencia» and its Capítulo IV is «La Comisión Disciplinaria y el Promotor de la Acción Disciplinaria». Título V regulates «los órganos técnicos» (Secretaría General and others). The tree shows the Presidente only as a member (art. 122.3 CE), and the Promotor and the órganos técnicos are absent, as they are from the prose. The nodes are right. Only the title claims too much. | `:::esquema{kind=arbol title="El Consejo General del Poder Judicial: composición, Pleno y Comisiones"}` (needs no new prose) |

Nesting: one root. Its four children are the two elements of art. 122.3 CE and the two forms of action of art. 595.1
LOPJ. The six Comisiones sit under «Comisiones» as in art. 595.2. Every dependency is stated by the text. PASS.

## tabla «Mayorías en la elección de los Vocales y en los acuerdos del Consejo General del Poder Judicial» (l. 202–214)

| # | row (short) | citation | PASS/FAIL | passage / reason | replacement |
|---|---|---|---|---|---|
| 1 | Elección de los 4 + 4 a propuesta del Congreso y del Senado, entre abogados y otros juristas… más de quince años — Cada Cámara — Tres quintos de sus miembros | art. 122.3 CE | PASS | 122.3: «…cuatro a propuesta del Congreso de los Diputados, y cuatro a propuesta del Senado, elegidos en ambos casos por mayoría de tres quintos de sus miembros, entre abogados y otros juristas, todos ellos de reconocida competencia y con más de quince años de ejercicio en su profesión.» A faithful shortening that keeps the majority, its base and both requirements. In prose at l. 85–89. | — |
| 2 | Elección de diez Vocales por cada Cámara: cuatro juristas… y seis del turno judicial — Cada Cámara — Tres quintos de sus miembros | art. 567.2 LOPJ | PASS | 567.2: «Cada una de las Cámaras elegirá, por mayoría de tres quintos de sus miembros, a diez Vocales, cuatro entre juristas de reconocida competencia con más de quince años de ejercicio en su profesión y seis correspondientes al turno judicial…». A faithful shortening, the same as the prose at l. 97–98. It leaves out the next sentence (at least 40 % of each sex), which the prose keeps at l. 99. See Notes. | — |
| 3 | Cese de un Vocal por incapacidad, incompatibilidad o incumplimiento grave — El Pleno — Tres quintos | art. 582.1 LOPJ | PASS | 582.1: «…o por incapacidad, incompatibilidad o incumplimiento grave de los deberes del cargo, apreciadas por el Pleno del Consejo General del Poder Judicial mediante mayoría de tres quintos.» Verbatim. The norm gives no base for the majority, and the row adds none. The label carries only the causes that need the majority, and not the cese by the five years or by renuncia, so it does not read wider. In prose at l. 119–121. | — |
| 4 | Elección del Presidente del TS y del CGPJ, en votación nominal — El Pleno — Tres quintos de los miembros del Pleno | art. 586.3 LOPJ | PASS | 586.3: «…siendo elegido quien en votación nominal obtenga el apoyo de la mayoría de tres quintos de los miembros del Pleno.» Verbatim, with the base. In prose at l. 130–131. | — |
| 5 | Cese del Presidente por notoria incapacidad o incumplimiento grave — El Pleno — Tres quintos de sus miembros | art. 588.1 LOPJ | PASS | 588.1.3.ª: «Por decisión del Pleno del Consejo General del Poder Judicial, a causa de notoria incapacidad o incumplimiento grave de los deberes del cargo, apreciados por tres quintos de sus miembros.» Verbatim. The other two causes (expiry, renuncia) need no majority. In prose at l. 133–135. The row cites the apartado without the ordinal, which tables allow. | — |
| 6 | Nombramiento del Vicepresidente del TS, a propuesta del Presidente — El Pleno — Tres quintos | art. 589.2 LOPJ | PASS | 589.2: «El Vicepresidente del Tribunal Supremo será nombrado, por mayoría de tres quintos del Pleno del Consejo General del Poder Judicial, a propuesta del Presidente.» The majority is right, and the Órgano column carries «El Pleno». The norm's base «del Pleno» is not written in the Mayoría cell. See Notes. In prose at l. 137–138. | — |
| 7 | Propuesta de los dos Magistrados del TC, en el plazo máximo de tres meses… — El Pleno — Tres quintos | art. 599.1 LOPJ | PASS | 599.1.1.ª: «La propuesta de nombramiento, por mayoría de tres quintos, de los dos Magistrados del Tribunal Constitucional cuya designación corresponde al Consejo General del Poder Judicial, que tendrá que realizarse en el plazo máximo de tres meses a contar desde el día siguiente al vencimiento del mandato anterior.» A faithful shortening that keeps the plazo. The norm gives no base. In prose at l. 167–169. | — |
| 8 | Nombramiento de Presidentes de Sala y Magistrados del TS — Los órganos colegiados del Consejo — Tres quintos de los miembros presentes | art. 630.1 LOPJ | FAIL | 630.1: «…o cuando se trate del nombramiento de Presidentes de Sala y Magistrados del Tribunal Supremo, Presidente de la Audiencia Nacional y Presidentes de Sala de la Audiencia Nacional, Presidentes de los Tribunales Superiores de Justicia y Presidentes de Sala de los Tribunales Superiores de Justicia, y Presidentes de Audiencias Provinciales, en cuyo caso se requerirá una mayoría de tres quintos de los miembros presentes. Igualmente, se requerirá mayoría de tres quintos de los miembros presentes cuando se trate del nombramiento del Magistrado del Tribunal Supremo, y de su sustituto, competentes para conocer de las actividades del Centro Nacional de Inteligencia…». The row keeps the first item of the article's list and stops there. In a table set beside the default of row 9 (mayoría absoluta), the cut list reads as the article's own list. A reader concludes that the Presidente de la Audiencia Nacional or a Presidente de TSJ is appointed by mayoría absoluta, and 630.1 says the opposite. The prose has the same cut at l. 184–185, so a complete row would need a clause the prose lacks. | Remove the row. Prose gap for the ledger: art. 630.1 LOPJ also requires tres quintos de los miembros presentes for the Presidente de la Audiencia Nacional and its Presidentes de Sala, the Presidentes of the TSJ and their Presidentes de Sala, the Presidentes de Audiencias Provinciales, and the Magistrado del TS (and sustituto) for the CNI. Once the prose carries it, the row can return as `\| Nombramiento de Presidentes de Sala y Magistrados del Tribunal Supremo, Presidente y Presidentes de Sala de la Audiencia Nacional, Presidentes y Presidentes de Sala de los Tribunales Superiores de Justicia y Presidentes de Audiencias Provinciales \| Los órganos colegiados del Consejo \| Tres quintos de los miembros presentes \| art. 630.1 LOPJ \|` |
| 9 | Acuerdos, salvo que la ley disponga otra cosa — Los órganos colegiados del Consejo — Mayoría absoluta de los miembros presentes | art. 630.1 LOPJ | PASS | 630.1: «Los acuerdos de los órganos colegiados del Consejo General del Poder Judicial serán adoptados por mayoría absoluta de los miembros presentes, salvo cuando esta Ley Orgánica disponga otra cosa o cuando se trate del nombramiento de…». The prose shortening «salvo que la ley disponga otra cosa» (l. 183–184) covers the LOPJ's own exceptions, 630.1's list among them, so the rule does not read wider on its own. Its only problem is row 8, so it passes once row 8 is removed. The voto de calidad (l. 185–186) is left out, which narrows the row and does not widen it. | — |
| T | Title «Mayorías en la elección de los Vocales y en los acuerdos del Consejo General del Poder Judicial» | — | FAIL | The title reads as the full set of the Consejo's majorities, and the LOPJ has others that the table, like the prose, leaves out. Art. 580.4: «el Pleno por mayoría de tres quintos podrá destituir al Vocal infractor». Art. 589.5: the Vicepresidente «podrá ser cesado por el Pleno … con el voto favorable de tres quintos de los miembros del Pleno». Art. 599.3: other Comisiones may be created «por una mayoría de tres quintos de los vocales». Art. 630.1 has the further nominations of row 8. Art. 589.4 has a mayoría absoluta. | `:::esquema{kind=tabla title="Mayorías en la elección de los Vocales y en algunos acuerdos del Consejo General del Poder Judicial"}` (needs no new prose) |

Order: a table claims no order. The rows run CE, then Vocales, Presidente, Vicepresidente, TC, then the art. 630.1 rule, in
the order of the prose. PASS.

## arbol «Las Salas del Tribunal Supremo, de la Audiencia Nacional y de los Tribunales Superiores de Justicia» (l. 282–298)

| # | node (short) | citation | PASS/FAIL | passage / reason | replacement |
|---|---|---|---|---|---|
| 1 | Tribunal Supremo — con jurisdicción en toda España, órgano jurisdiccional superior…, salvo garantías constitucionales | art. 123.1 CE | PASS | 123.1: «El Tribunal Supremo, con jurisdicción en toda España, es el órgano jurisdiccional superior en todos los órdenes, salvo lo dispuesto en materia de garantías constitucionales.» Verbatim, with the exception kept. In prose at l. 218–219. | — |
| 2–6 | Sala Primera, de lo Civil … Sala Quinta, de lo Militar | art. 55 LOPJ | PASS | 55: «El Tribunal Supremo estará integrado por las siguientes Salas: Primera: De lo Civil. Segunda: De lo Penal. Tercera: De lo Contencioso-Administrativo. Cuarta: De lo Social. Quinta: De lo Militar, que se regirá por su legislación específica…». All five are there, in order. «Integrado por» states the dependency. The Quinta's «que se regirá…» is a rule on its sources of law, not a limit on its existence. The prose (l. 226–232) leaves it out too. | — |
| 7 | Audiencia Nacional — con sede en la villa de Madrid, tiene jurisdicción en toda España | art. 62 LOPJ | PASS | 62: «La Audiencia Nacional, con sede en la villa de Madrid, tiene jurisdicción en toda España.» Verbatim. In prose at l. 268. | — |
| 8–11 | Sala de Apelación, de lo Penal, de lo Contencioso-Administrativo, de lo Social | art. 64.1 LOPJ | PASS | 64.1: «La Audiencia Nacional estará integrada por las siguientes Salas: De Apelación. De lo Penal. De lo Contencioso-Administrativo. De lo Social.» All four are there, in order, and the dependency holds. In prose at l. 269–270. | — |
| 12 | Tribunal Superior de Justicia — culmina la organización judicial en el ámbito de la CA, sin perjuicio de la jurisdicción que corresponde al TS | art. 70 LOPJ | PASS | 70: «El Tribunal Superior de Justicia de la Comunidad Autónoma culminará la organización judicial en el ámbito territorial de aquélla, sin perjuicio de la jurisdicción que corresponde al Tribunal Supremo.» A faithful shortening that keeps the sin perjuicio. The prose (l. 274–275) says the same fact, in the same words except «de la jurisdicción del Tribunal Supremo». | — |
| 13 | Sala de lo Civil y Penal — el Presidente del TSJ lo es también de esta Sala | art. 72.2 LOPJ | PASS | 72.2: «Se compondrá de un Presidente, que lo será también de su Sala de lo Civil y Penal…». A faithful shortening. The Sala itself is listed in 72.1, and the node cites the apartado of its fact. In prose at l. 275–277. | — |
| 14–15 | Sala de lo Contencioso-Administrativo, Sala de lo Social | art. 72.1 LOPJ | PASS | 72.1: «El Tribunal Superior de Justicia estará integrado por las siguientes Salas: de lo Civil y Penal, de lo Contencioso-Administrativo y de lo Social.» The list is complete across nodes 13–15, and the dependency holds. In prose at l. 275–276. | — |

Nesting: three roots, each followed by the Salas of its own «estará integrado por las siguientes Salas» article. Every
list is complete. The title names only the Salas, so it does not read the tree as the whole organisation of the courts.
PASS for the nodes and the title.

## Placement

- arbol 1 (l. 188) and tabla (l. 202) close the «El Consejo General del Poder Judicial» section (l. 74–186). They
  follow every paragraph they summarise: composition at l. 76–92, designation at l. 96–99, cese at l. 119–121,
  Presidente at l. 130–138, órganos at l. 159–169, Disciplinaria at l. 179–180 and art. 630.1 at l. 183–186. PASS.
- arbol 2 (l. 282) comes after the TSJ section (l. 274–280) and before «Las Audiencias Provinciales». It follows
  every paragraph it summarises: TS at l. 218–232, AN at l. 268–270 and TSJ at l. 274–277. PASS. It splits the run of
  per-court subsections (AN, TSJ | AP, TI). That is acceptable, because it has to come after the TSJ paragraph.

## Notes

- arbol 2, TS branch: the five Salas are already a numbered list in the prose (l. 228–232). The spec discourages an
  esquema that only repeats a prose list. The AN and TSJ branches add structure, because their prose is sentence-form,
  so the esquema as a whole earns its place. Not a FAIL.
- arbol 2: the special Sala of art. 61 LOPJ («Una Sala formada por el Presidente del Tribunal Supremo, los Presidentes
  de Sala y el Magistrado más antiguo y el más moderno de cada una de ellas…») is not one of the Salas of art. 55, and
  the prose does not mention it. The title rests on art. 55, so this is not a FAIL.
- arbol 1: art. 599.3 LOPJ lets the Pleno create other Comisiones «además de las enumeradas en el artículo 595.2». The
  six-node list is the complete statutory list, and 599.3 is a power, as in the m05-l03 precedent. Not a FAIL.
- tabla row 2: the 40 % minimum of each sex (567.2, second sentence) is a separate sentence, not a clause of the one
  quoted, and the prose keeps it at l. 99. The row could carry it («…, con un mínimo del cuarenta por ciento de cada
  sexo») without new prose. Optional.
- tabla row 6: the Mayoría cell «Tres quintos» could read «Tres quintos del Pleno» (589.2 verbatim), so that it is not
  read against row 9's «de los miembros presentes». The prose says «lo nombra el Pleno por mayoría de tres quintos»,
  which carries the same content. Optional.
- tabla rows 1–2: the CE gives the Cámaras 4 + 4 Vocales and the LOPJ gives each Cámara 10. These are two norms, and
  the prose at l. 96–98 explains how they fit, so the table needs no change.
- Glossary: no mark moves. `g-tribunal-superior-de-justicia` first marks at l. 274, before arbol 2, and
  `g-separacion-del-servicio` has `link_except: m01-l04`. No other glossary term in `glossary.yaml` matches the
  esquema text. I did not regenerate `glossary-links.es.txt`. The writer's test run is what confirms this.
- Voice: no filler, triad, question or coined term in the titles or labels.

## Totals

38 checks: arbol 1 has 11 nodes and a title, the tabla has 9 rows and a title, and arbol 2 has 15 nodes and a title.
35 PASS, 3 FAIL: the arbol 1 title, the tabla title, and tabla row 8 (to be removed, because a complete row needs a
clause the prose lacks). Nesting: PASS. Order: PASS. Placement: PASS. The diff only adds lines.
