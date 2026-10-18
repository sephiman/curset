# Verification — esquemas of m01-l09, m01-l10 and m01-l11 (2026-10-18)

I am a blind reviewer: I wrote neither these esquemas nor the lessons, and I did not open the writer's notes. Scope: the
`:::esquema` blocks that `git diff C/es/lessons/m01-l09.md m01-l10.md m01-l11.md` shows as added. The diffs only add
lines (0 removed lines in each of the three files), so no prose line changed. Rules: `spec.md` (this folder), the
`::esquema` section of `docs/platform-delta-handoff.md`, and `docs/prose-voice.md`. Line numbers are those of the
current lesson files.

Sources, all from the scratchpad `txt/` and read with `art.py` or `sed`. I took no norm wording from memory.

- CE (`BOE-A-1978-31229_ce_2026-05-20.txt`): arts. 140, 141, 143, 144, 145, 146, 147, 148, 149, 150, 151.
- LBRL (`BOE-A-1985-5392_lbrl_2026-10-03.txt`): arts. 20, 21, 22, 23, 32, 33, 35, 36.
- TUE (`CELEX-02016M-20250315_tue_2025-03-15.txt`, consolidated 15-03-2025): arts. 14, 15, 16, 17, 19.
- TFUE (`CELEX-02016E-20250315_tfue_2025-03-15.txt`, consolidated 15-03-2025): arts. 231, 232–234, 235, 236, 238, 250,
  252. Every treaty article cited in an esquema is in these saved files, so no row lacks its source text.

Mechanical checks:

- Citations: I dumped the current citation report (`tests/test_citations.py::_report`). Every esquema row of the three
  lessons resolves to a CE, LBRL, TUE or TFUE anchor that the lesson's prose also carries. `citations.es.txt` does not
  hold these esquema rows yet. The frozen-report test fails course-wide (279 → 480 esquema rows) because the round's
  esquemas are not yet regenerated. That is expected while writers are still at work, and it is not a finding on
  these lessons.
- Glossary: `npx vitest run src/lib/glossary/report.test.ts` passes (20/20) against the unchanged
  `glossary-links.es.txt`. No mark moved or appeared.

## m01-l09

### tabla «Las vías de acceso a la autonomía de los artículos 143 y 151» (l. 109–114)

| # | row (short) | citation | PASS/FAIL | passage / reason | replacement |
|---|---|---|---|---|---|
| 1 | Artículo 143: Diputaciones + 2/3 municipios / 6 meses desde el primer acuerdo / «—» / asamblea del art. 146, elevado a las Cortes | arts. 143.2 y 146 CE | PASS | 143.2: «La iniciativa del proceso autonómico corresponde a todas las Diputaciones interesadas o al órgano interinsular correspondiente y a las dos terceras partes de los municipios cuya población represente, al menos, la mayoría del censo electoral de cada provincia o isla. Estos requisitos deberán ser cumplidos en el plazo de seis meses desde el primer acuerdo adoptado al respecto por alguna de las Corporaciones locales interesadas.» 146: «El proyecto de Estatuto será elaborado por una asamblea compuesta por los miembros de la Diputación u órgano interinsular de las provincias afectadas y por los Diputados y Senadores elegidos en ellas y será elevado a las Cortes Generales para su tramitación como ley.» Both cells are verbatim. The prose places art. 146 under «La vía del artículo 143» (l. 68–70), so pairing 146 with this row follows the prose. The «—» in «Ratificación» is accurate: art. 143 sets no ratification, and the prose draws the contrast (l. 84–86: «En el artículo 151 hacen falta las tres cuartas partes y un referéndum…»). In prose at l. 57–70. | — |
| 2 | Artículo 151 (no five-year wait of 148.2): Diputaciones + 3/4 municipios / within the 143.2 plazo / referéndum, mayoría absoluta de los electores / Government convenes the Asamblea de Parlamentarios, mayoría absoluta | art. 151.1–2 CE | PASS | 151.1: «No será preciso dejar transcurrir el plazo de cinco años, a que se refiere el apartado 2 del artículo 148, cuando la iniciativa del proceso autonómico sea acordada dentro del plazo del artículo 143.2, además de por las Diputaciones o los órganos interinsulares correspondientes, por las tres cuartas partes de los municipios de cada una de las provincias afectadas que representen, al menos, la mayoría del censo electoral de cada una de ellas y dicha iniciativa sea ratificada mediante referéndum por el voto afirmativo de la mayoría absoluta de los electores de cada provincia en los términos que establezca una ley orgánica.» 151.2.1.º: «El Gobierno convocará a todos los Diputados y Senadores elegidos en las circunscripciones comprendidas en el ámbito territorial que pretenda acceder al autogobierno, para que se constituyan en Asamblea, a los solos efectos de elaborar el correspondiente proyecto de Estatuto de autonomía, mediante el acuerdo de la mayoría absoluta de sus miembros.» Every condition and both majorities are kept: 3/4, the census majority, the absolute majority of electors, the ley orgánica and the Asamblea's absolute majority. «es decir, seis meses» is the prose's own gloss (l. 77). In prose at l. 74–92. | — |

### tabla «Cinco materias en las dos listas de los artículos 148.1 y 149.1» (l. 288–296)

The prose pairs the two lists in one paragraph only (l. 282–286), and it pairs three materias: montes (148.1.8.ª /
149.1.23.ª), puertos deportivos / puertos de interés general (148.1.6.ª / 149.1.20.ª) and sanidad (148.1.21.ª /
149.1.16.ª). Tráfico appears there on the Estado side only. Each cell below is a verbatim item from the prose lists
at l. 213–244 and l. 251–280. The «Materia» column, however, states that the two cells of a row are the two halves
of one materia. That pairing is a fact the table adds wherever the prose does not make it.

| # | row (short) | citation | PASS/FAIL | passage / reason | replacement |
|---|---|---|---|---|---|
| 1 | Montes: 8.ª montes y aprovechamientos forestales / 23.ª legislación básica sobre montes… | arts. 148.1.8.ª y 149.1.23.ª CE | PASS | 148.1.8.ª: «Los montes y aprovechamientos forestales.» 149.1.23.ª, second sentence: «La legislación básica sobre montes, aprovechamientos forestales y vías pecuarias.» Both verbatim. The prose pairs them at l. 282–283. | — |
| 2 | Medio ambiente: 9.ª gestión / 23.ª legislación básica, sin perjuicio de normas adicionales | arts. 148.1.9.ª y 149.1.23.ª CE | FAIL | 148.1.9.ª: «La gestión en materia de protección del medio ambiente.» 149.1.23.ª: «Legislación básica sobre protección del medio ambiente, sin perjuicio de las facultades de las Comunidades Autónomas de establecer normas adicionales de protección.» Both cells are verbatim, and the second keeps its «sin perjuicio». The prose never pairs them: 9.ª sits at l. 227 and 23.ª at l. 275–277, and the pairing paragraph (l. 282–286) leaves medio ambiente out. The row adds a gestión / legislación básica comparison that the prose does not make (criterion 4). A replacement would need a clause the prose lacks, so the row is removed. Prose gap for the ledger: l. 282–286 does not pair medio ambiente. | Remove the row. Title: «Tres materias en las dos listas de los artículos 148.1 y 149.1» (after rows 3 and 5 are fixed as proposed). |
| 3 | Puertos y aeropuertos: 6.ª puertos de refugio, puertos y aeropuertos deportivos… / 20.ª puertos de interés general; aeropuertos de interés general | arts. 148.1.6.ª y 149.1.20.ª CE | FAIL | 148.1.6.ª: «Los puertos de refugio, los puertos y aeropuertos deportivos y, en general, los que no desarrollen actividades comerciales.» 149.1.20.ª: «…puertos de interés general; aeropuertos de interés general; …». The cells are verbatim fragments. The prose pairs puertos only: «Puertos deportivos: Comunidades (art. 148.1.6.ª CE); puertos de interés general: Estado (art. 149.1.20.ª CE).» The label «Puertos y aeropuertos» and the «aeropuertos de interés general» fragment add an aeropuertos pairing the prose does not make. | `\| Puertos \| 6.ª Los puertos de refugio, los puertos y aeropuertos deportivos y, en general, los que no desarrollen actividades comerciales \| 20.ª Puertos de interés general \| arts. 148.1.6.ª y 149.1.20.ª CE \|` |
| 4 | Sanidad: 21.ª sanidad e higiene / 16.ª sanidad exterior, bases y coordinación, productos farmacéuticos | arts. 148.1.21.ª y 149.1.16.ª CE | PASS | 148.1.21.ª: «Sanidad e higiene.» 149.1.16.ª: «Sanidad exterior. Bases y coordinación general de la sanidad. Legislación sobre productos farmacéuticos.» Both verbatim. The prose pairs them at l. 284–285. | — |
| 5 | Ferrocarriles: 5.ª ferrocarriles y carreteras íntegramente en la CA / 21.ª ferrocarriles y transportes terrestres de más de una CA | arts. 148.1.5.ª y 149.1.21.ª CE | FAIL | 148.1.5.ª: «Los ferrocarriles y carreteras cuyo itinerario se desarrolle íntegramente en el territorio de la Comunidad Autónoma y, en los mismos términos, el transporte desarrollado por estos medios o por cable.» 149.1.21.ª: «Ferrocarriles y transportes terrestres que transcurran por el territorio de más de una Comunidad Autónoma; …». Both are verbatim, and the norm's own words make the two items complementary. But the prose does not pair them. It cites 149.1.21.ª only for «Tráfico y circulación de vehículos a motor: Estado» (l. 285–286), and 148.1.5.ª appears only in the list (l. 221–222). As in row 2, the comparison is the table's own (criterion 4). A replacement would need a clause the prose lacks. | Remove the row. Prose gap for the ledger: l. 282–286 does not pair ferrocarriles. |

### tabla «Leyes marco, transferencia o delegación y armonización» (l. 329–335)

| # | row (short) | citation | PASS/FAIL | passage / reason | replacement |
|---|---|---|---|---|---|
| 1 | Leyes marco — Cortes atribuyen… en el marco de… / control de las Cortes, sin perjuicio de los Tribunales | art. 150.1 CE | PASS | 150.1: «Las Cortes Generales, en materias de competencia estatal, podrán atribuir a todas o a alguna de las Comunidades Autónomas la facultad de dictar, para sí mismas, normas legislativas en el marco de los principios, bases y directrices fijados por una ley estatal. Sin perjuicio de la competencia de los Tribunales, en cada ley marco se establecerá la modalidad del control de las Cortes Generales sobre estas normas legislativas de las Comunidades Autónomas.» Verbatim. In prose at l. 314–317. | — |
| 2 | Transferencia o delegación — mediante ley orgánica…; transferencia de medios financieros y formas de control | art. 150.2 CE | PASS | 150.2: «El Estado podrá transferir o delegar en las Comunidades Autónomas, mediante ley orgánica, facultades correspondientes a materia de titularidad estatal que por su propia naturaleza sean susceptibles de transferencia o delegación. La ley preverá en cada caso la correspondiente transferencia de medios financieros, así como las formas de control que se reserve el Estado.» Verbatim. It keeps «mediante ley orgánica». In prose at l. 319–322. | — |
| 3 | Leyes de armonización — aun en materias de las CCAA, cuando lo exija el interés general / mayoría absoluta de cada Cámara | art. 150.3 CE | PASS | 150.3: «El Estado podrá dictar leyes que establezcan los principios necesarios para armonizar las disposiciones normativas de las Comunidades Autónomas, aun en el caso de materias atribuidas a la competencia de éstas, cuando así lo exija el interés general. Corresponde a las Cortes Generales, por mayoría absoluta de cada Cámara, la apreciación de esta necesidad.» Verbatim. It keeps the condition and the majority («de cada Cámara»). In prose at l. 324–327. | — |

## m01-l10

### tabla «El municipio, la provincia y la isla en la Constitución» (l. 43–49)

| # | row (short) | citation | PASS/FAIL | passage / reason | replacement |
|---|---|---|---|---|---|
| 1 | Municipio — personalidad jurídica plena / Ayuntamientos, Alcaldes y Concejales | art. 140 CE | PASS | 140: «Estos gozarán de personalidad jurídica plena. Su gobierno y administración corresponde a sus respectivos Ayuntamientos, integrados por los Alcaldes y los Concejales.» Verbatim. In prose at l. 17–19. | — |
| 2 | Provincia — entidad local con personalidad jurídica propia… / Diputaciones u otras Corporaciones | art. 141.1–2 CE | PASS | 141.1: «La provincia es una entidad local con personalidad jurídica propia, determinada por la agrupación de municipios y división territorial para el cumplimiento de las actividades del Estado.» 141.2: «El gobierno y la administración autónoma de las provincias estarán encomendados a Diputaciones u otras Corporaciones de carácter representativo.» Verbatim. In prose at l. 28–35. | — |
| 3 | Isla, en los archipiélagos — «—» / administración propia, Cabildos o Consejos | art. 141.4 CE | FAIL | 141.4: «En los archipiélagos, las islas tendrán además su administración propia en forma de Cabildos o Consejos.» The second cell is verbatim and keeps «además». The «—» under «Personalidad jurídica» reads as «the island has no legal personality». Art. 141.4 does not say that. It is silent, and the LBRL counts the Isla among the «Entidades Locales territoriales» (art. 3, prose l. 55–56). Nothing in the prose says the Constitution is silent on it. The header «Gobierno y administración» also gives the island a «gobierno» that 141.4 does not name: the article says only «administración propia». Filling the cell would need a clause the prose lacks. The fix is to change the table's shape so that no cell is empty. | Merge the two fact columns: `\| Entidad \| Qué establece \| Artículo \|` with `\| Municipio \| Gozarán de personalidad jurídica plena. Su gobierno y administración corresponde a sus respectivos Ayuntamientos, integrados por los Alcaldes y los Concejales \| art. 140 CE \|`, `\| Provincia \| Entidad local con personalidad jurídica propia, determinada por la agrupación de municipios y división territorial para el cumplimiento de las actividades del Estado; el gobierno y la administración autónoma de las provincias estarán encomendados a Diputaciones u otras Corporaciones de carácter representativo \| art. 141.1–2 CE \|`, `\| Isla, en los archipiélagos \| Las islas tendrán además su administración propia en forma de Cabildos o Consejos \| art. 141.4 CE \|`. Or remove the Isla row and retitle «El municipio y la provincia en la Constitución». |

### tabla «Pleno, Junta de Gobierno, Tenientes de Alcalde y Vicepresidentes en el ayuntamiento y en la Diputación» (l. 266–273)

| # | row (short) | citation | PASS/FAIL | passage / reason | replacement |
|---|---|---|---|---|---|
| 1 | Dónde existe — 20.1 a)–b) / 32.1 | arts. 20.1 y 32.1 LBRL | PASS | 20.1: «a) El Alcalde, los Tenientes de Alcalde y el Pleno existen en todos los ayuntamientos. b) La Junta de Gobierno Local existe en todos los municipios con población superior a 5.000 habitantes y en los de menos, cuando así lo disponga su reglamento orgánico o así lo acuerde el Pleno de su ayuntamiento.» 32.1: «El Presidente, los Vicepresidentes, la Junta de Gobierno y el Pleno existen en todas las Diputaciones.» Verbatim, and the 5.000-habitantes condition is kept. Leaving out 20.1 c)–e) and 32.2 narrows the row and does not widen it: neither cell says «only». In prose at l. 120–125 and l. 253. See Notes on the header. | — |
| 2 | Pleno — todos los Concejales, presidido por el Alcalde / Presidente y Diputados | arts. 22.1 y 33.1 LBRL | PASS | 22.1: «El Pleno, integrado por todos los Concejales, es presidido por el Alcalde.» 33.1: «El Pleno de la Diputación está constituido por el Presidente y los Diputados.» Verbatim. In prose at l. 146 and l. 257. | — |
| 3 | Junta de Gobierno — no superior al tercio, nombrados y separados libremente, dando cuenta al Pleno | arts. 23.1 y 35.1 LBRL | PASS | 23.1: «La Junta de Gobierno Local se integra por el Alcalde y un número de Concejales no superior al tercio del número legal de los mismos, nombrados y separados libremente por aquél, dando cuenta al Pleno.» 35.1 has the same wording with «Presidente» and «Diputados». Verbatim. In prose at l. 165–167 and l. 260–262. | — |
| 4 | Tenientes de Alcalde y Vicepresidentes — sustitución por orden de nombramiento; designación (y remoción) | arts. 23.3 y 35.4 LBRL | PASS | 23.3: «Los Tenientes de Alcalde sustituyen, por el orden de su nombramiento y en los casos de vacante, ausencia o enfermedad, al Alcalde, siendo libremente designados y removidos por éste de entre los miembros de la Junta de Gobierno Local y, donde ésta no exista, de entre los Concejales.» 35.4: «Los Vicepresidentes sustituyen, por el orden de su nombramiento y en los casos de vacante, ausencia o enfermedad, al Presidente, siendo libremente designados por éste entre los miembros de la Junta de Gobierno.» Verbatim. The cells keep the difference between the two articles: «y removidos» and «donde ésta no exista» on the municipal side only. The pairing rests on the norm's own parallel wording, and the label names both organs, so no organ is presented as the other. In prose at l. 172–174 and l. 262–264. | — |

## m01-l11

### tabla «Composición del Consejo Europeo, el Consejo, el Parlamento Europeo y la Comisión» (l. 263–270)

| # | row (short) | citation | PASS/FAIL | passage / reason | replacement |
|---|---|---|---|---|---|
| 1 | Consejo Europeo — Jefes de Estado o de Gobierno, su Presidente y el de la Comisión; participa el Alto Representante | art. 15.2 TUE | PASS | 15.2: «El Consejo Europeo estará compuesto por los Jefes de Estado o de Gobierno de los Estados miembros, así como por su Presidente y por el Presidente de la Comisión. Participará en sus trabajos el Alto Representante de la Unión para Asuntos Exteriores y Política de Seguridad.» Verbatim. It keeps the distinction between members and participant. In prose at l. 66–68. | — |
| 2 | Consejo — un representante por Estado, de rango ministerial… | art. 16.2 TUE | PASS | 16.2: «El Consejo estará compuesto por un representante de cada Estado miembro, de rango ministerial, facultado para comprometer al Gobierno del Estado miembro al que represente y para ejercer el derecho de voto.» Verbatim. In prose at l. 106–107. | — |
| 3 | Parlamento Europeo — ≤ 750 más el Presidente; decrecientemente proporcional, mín. 6, máx. 96 | art. 14.2 TUE | PASS | 14.2 párr. 1: «…representantes de los ciudadanos de la Unión. Su número no excederá de setecientos cincuenta, más el Presidente. La representación de los ciudadanos será decrecientemente proporcional, con un mínimo de seis diputados por Estado miembro. No se asignará a ningún Estado miembro más de noventa y seis escaños.» Verbatim, with every number kept. The row does not carry the «a fecha de» figure of 720 from `sources/otros/`, which is correct. In prose at l. 171–174. | — |
| 4 | Comisión, a partir del 1-11-2014 — dos tercios del número de Estados, incl. Presidente y Alto Representante, salvo unanimidad del Consejo Europeo | art. 17.5 TUE | PASS | 17.5: «A partir del 1 de noviembre de 2014, la Comisión estará compuesta por un número de miembros correspondiente a los dos tercios del número de Estados miembros, que incluirá a su Presidente y al Alto Representante de la Unión para Asuntos Exteriores y Política de Seguridad, a menos que el Consejo Europeo decida por unanimidad modificar dicho número.» Verbatim. The label keeps the date and the cell keeps the unanimity exception. In prose at l. 229–231. | — |

### tabla «Cómo se pronuncian el Consejo Europeo, el Consejo, el Parlamento Europeo y la Comisión» (l. 272–282)

| # | row (short) | citation | PASS/FAIL | passage / reason | replacement |
|---|---|---|---|---|---|
| 1 | Consejo Europeo — consenso, salvo los Tratados | art. 15.4 TUE | PASS | 15.4: «El Consejo Europeo se pronunciará por consenso, excepto cuando los Tratados dispongan otra cosa.» Verbatim. In prose at l. 75. | — |
| 2 | Consejo Europeo, cuestiones de procedimiento y reglamento interno — mayoría simple | art. 235.3 TFUE | PASS | 235.3: «El Consejo Europeo se pronunciará por mayoría simple en las cuestiones de procedimiento y para la aprobación de su reglamento interno.» Verbatim. The label carries the condition. In prose at l. 75–77. | — |
| 3 | Consejo — mayoría cualificada, salvo los Tratados | art. 16.3 TUE | PASS | 16.3: «El Consejo se pronunciará por mayoría cualificada, excepto cuando los Tratados dispongan otra cosa.» Verbatim. In prose at l. 146–147. | — |
| 4 | Consejo, mayoría cualificada a partir del 1-11-2014 — 55 % / 15 / 65 %; minoría de bloqueo de 4 | art. 16.4 TUE | FAIL | 16.4: «A partir del 1 de noviembre de 2014, la mayoría cualificada se definirá como un mínimo del 55 % de los miembros del Consejo que incluya al menos a quince de ellos y represente a Estados miembros que reúnan como mínimo el 65 % de la población de la Unión. Una minoría de bloqueo estará compuesta por al menos cuatro miembros del Consejo, a falta de lo cual la mayoría cualificada se considerará alcanzada. Las demás modalidades reguladoras del voto por mayoría cualificada se establecen en el apartado 2 del artículo 238 del Tratado de Funcionamiento de la Unión Europea.» The cell is verbatim and keeps 55 %, 15, 65 % and 4. But the label presents it as the Consejo's qualified majority with no further condition, and the table has no row for 238.2 TFUE: «No obstante lo dispuesto en el apartado 4 del artículo 16 del [TUE] … cuando el Consejo no actúe a propuesta de la Comisión o del Alto Representante …, la mayoría cualificada se definirá como un mínimo del 72 % de los miembros del Consejo que represente a Estados miembros que reúnan como mínimo el 65 % de la población de la Unión.» Article 16.4 itself points to that rule, and the prose states it (l. 154–156, «art. 238.2 TFUE»). In a table titled «Cómo se pronuncian…», the row reads wider than the two articles (criterion 2). The prose holds everything the fix needs. | Label: `Consejo, mayoría cualificada a partir del 1 de noviembre de 2014, cuando actúa a propuesta de la Comisión o del Alto Representante` (cell and citation unchanged), and a new row right after it: `\| Consejo, cuando no actúa a propuesta de la Comisión o del Alto Representante \| La mayoría cualificada se definirá como un mínimo del 72 % de los miembros del Consejo que represente a Estados miembros que reúnan como mínimo el 65 % de la población de la Unión \| art. 238.2 TFUE \|` |
| 5 | Consejo, mayoría simple — mayoría de los miembros que lo componen | art. 238.1 TFUE | PASS | 238.1: «Cuando deba adoptar un acuerdo por mayoría simple, el Consejo se pronunciará por mayoría de los miembros que lo componen.» Verbatim. In prose at l. 158–159. | — |
| 6 | Parlamento Europeo, salvo disposición en contrario — mayoría de los votos emitidos; quórum por reglamento | art. 231 TFUE | PASS | 231: «Salvo disposición en contrario de los Tratados, el Parlamento Europeo decidirá por mayoría de los votos emitidos. El reglamento interno fijará el quórum.» Verbatim. The salvo sits in the label, so the row does not hide the exceptions, such as the moción de censura of art. 234 (prose l. 199–201). In prose at l. 190–191. | — |
| 7 | Comisión — mayoría de sus miembros; quórum por reglamento | art. 250 TFUE | PASS | 250: «Los acuerdos de la Comisión se adoptarán por mayoría de sus miembros. Su reglamento interno fijará el quórum.» Verbatim. In prose at l. 259–260. | — |

### arbol «El Tribunal de Justicia de la Unión Europea» (l. 314–319)

| # | node (short) | citation | PASS/FAIL | passage / reason | replacement |
|---|---|---|---|---|---|
| 1 | TJUE — garantizará el respeto del Derecho… | art. 19.1 TUE | PASS | 19.1: «…Garantizará el respeto del Derecho en la interpretación y aplicación de los Tratados.» Verbatim. In prose at l. 288–290. | — |
| 2 | └ Tribunal de Justicia — un juez por Estado miembro, asistido por abogados generales | art. 19.2 TUE | PASS | 19.2: «El Tribunal de Justicia estará compuesto por un juez por Estado miembro. Estará asistido por abogados generales.» A faithful shortening. The child sits under the TJUE because 19.1 says the TJUE «comprenderá el Tribunal de Justicia, el Tribunal General y los tribunales especializados». In prose at l. 294. | — |
| 3 | └ Tribunal General — al menos un juez por Estado miembro | art. 19.2 TUE | PASS | 19.2: «El Tribunal General dispondrá al menos de un juez por Estado miembro.» Verbatim, and «al menos» is kept. The dependency is supported by 19.1. In prose at l. 308. | — |
| 4 | └ Tribunales especializados | art. 19.1 TUE | PASS | 19.1 (above). A label-only node, and the dependency is supported by 19.1. In prose at l. 288–289. | — |

## Order

None of the six tablas claims an order. The arbol claims dependency only, and all three children rest on the
«comprenderá» of art. 19.1 TUE. No `plazos` or `pasos` lists appear in these lessons. PASS.

## Titles

- m01-l09 tabla 1: «de los artículos 143 y 151» limits the table to two routes. Arts. 144 and the disp. trans. 2.ª
  and 5.ª are other routes the lesson covers, and the title does not claim them. PASS.
- m01-l09 tabla 2: «Cinco materias» does not read as complete. The title has to become «Tres materias…» if rows 2
  and 5 are removed.
- m01-l09 tabla 3, m01-l10 tablas 1–2, m01-l11 tablas 1–2 and the arbol each name what they cover, and no selective
  list reads as complete. In m01-l11 tabla 2 the general rules carry their own «excepto / salvo» clauses. Once row 4
  is fixed, the Consejo's 72 % case is included as well. PASS.
- No title or label uses anything the voice page forbids (fillers, triads, questions, closers). PASS.

## Placement

- m01-l09 tabla 1 (l. 109): after the last paragraph it summarises (art. 151.3, l. 105–107), which closes the account
  of both routes (l. 57–107). It sits before the disp. trans. 2.ª paragraph, which it does not cover. PASS.
- m01-l09 tabla 2 (l. 288): right after the pairing paragraph (l. 282–286) and the two lists. PASS.
- m01-l09 tabla 3 (l. 329): right after the art. 150.3 paragraph. PASS.
- m01-l10 tabla 1 (l. 43): right after «La isla» (l. 40–41), at the end of the CE section. PASS.
- m01-l10 tabla 2 (l. 266): after the Diputación's organisation (l. 253–264), which is the later of the two passages
  it summarises (the municipal part is at l. 120–174). PASS.
- m01-l11 tablas 1–2 (l. 263, l. 272): after the Comisión section, which is the last of the four institutions
  summarised. They sit before the TJUE section. PASS.
- m01-l11 arbol (l. 314): after «El Tribunal General» (l. 308–312), before «Los recursos». PASS.

## Notes

- m01-l09 tabla 3 repeats the three bold-led paragraphs at l. 314–327 almost word for word. They are paragraphs, not
  a list or a table, so the spec's «none where the prose is already a list» does not strictly apply. The esquema adds
  only the column layout. Keeping it is the lead's call.
- m01-l10 tabla 2 row 1 repeats, for the ayuntamiento, two rows of the prose table at l. 122–128 (art. 20.1). The
  first-column header «Órgano» does not fit that row: «Dónde existe» is not an organ. A header such as «Órgano o
  regla» would fit, but this is a label issue, not a FAIL.
- m01-l09 tabla 1 row 2: the «Proyecto de Estatuto» cell stops at 151.2.1.º, while the art. 143 row goes as far as
  «elevado a las Cortes Generales». The row is narrower than the article but not wrong. The later steps are in the
  prose list at l. 90–103.
- m01-l11 tabla 2: art. 238.3 TFUE (qualified majority when not all members of the Consejo take part in the vote: 55 %
  of the participating members, 65 % of their population, and a blocking minority above 35 % plus one) is not in the
  prose either. It is not an exception that art. 16.4 refers to, so I do not count it against row 4. It is a prose gap
  the lead may want in the ledger. The same goes for art. 235.1 TFUE, under which 16.4 TUE and 238.2 TFUE apply to the
  Consejo Europeo when it votes by qualified majority.
- m01-l11: no esquema cites a `sources/otros/` file, so the «a fecha de» rule does not come into play.
- Citation grammar: «art. 151.1–2 CE», «art. 141.1–2 CE» and the «arts. X y Y» forms all parse to one norm (checked
  in the citation dump). No list-row citation ends in a letter.

## Counts

32 rows: 27 PASS, 5 FAIL.

- m01-l09: 10 rows, 7 PASS, 3 FAIL (tabla 2 rows 2, 3 and 5).
- m01-l10: 7 rows, 6 PASS, 1 FAIL (tabla 1 row 3).
- m01-l11: 15 rows, 14 PASS, 1 FAIL (tabla 2 row 4).

Order: PASS. Placement: PASS. Titles: PASS, except that m01-l09 tabla 2 needs a new title if its rows are removed.
