# Prose gaps of «Esquemas bloque I» (open item 1): writer's record, 2026-10-18

Course `content/age-administrativo-c1`, lessons under `es/lessons/`. Nothing committed. Norm texts are
`pdftotext -layout` of the files named in `sources/normativa.yaml`: LOTC `BOE-A-1979-23709_lotc_2024-08-02`, LO 3/1981
`BOE-A-1981-10325_…_2009-11-04`, Reglamento del Congreso `BOE-A-1982-5196_…_2026-07-28` (the only pending change,
art. 23, is not touched here), Reglamento del Senado `BOE-A-1994-10830_…_2025-11-14`, LOPJ `BOE-A-1985-12666_…_2025-02-17`,
Ley 19/2013 `BOE-A-2013-12887_…_2022-07-09`, CE `BOE-A-1978-31229_…_2026-05-20`, TFUE
`CELEX-02016E-20250315_tfue_2025-03-15`. None of these has `cambios_pendientes` that affects the articles used.
Line numbers are those of the lesson files after this round.

Where a new fact had to be joined to an existing sentence (the gap was a clause of a sentence already there), the
sentence is given whole and the added words are named.

Per the coordinator's change of plan, **pytest was not run and no golden (`citations.es.txt`, `glossary-links.es.txt`,
`lesson-refs.es.txt`) was regenerated.** See «Not run» at the end.

## m01-l01

### Art. 76 LOTC (l. 275–277)

Added: «El plazo para impugnar las disposiciones normativas sin fuerza de ley y las resoluciones es de dos meses desde
su publicación o, en defecto de esta, desde que llegan a su conocimiento (art. 76 LOTC).»

Norm: «Dentro de los dos meses siguientes a la fecha de su publicación o, en defecto de la misma, desde que llegare a
su conocimiento, el Gobierno podrá impugnar ante el Tribunal Constitucional las disposiciones normativas sin fuerza de
Ley y resoluciones emanadas de cualquier órgano de las Comunidades Autónomas.»

Placed after the art. 161.2 CE paragraph (the Gobierno's impugnación), as its own sentence so the 161.2 citation keeps
its scope. «sin fuerza de ley» keeps the article as narrow as the norm (laws go by recurso, 33.1).

### Art. 33.2 LOTC, requisito c) and purpose clause (l. 286–291)

Two existing sentences joined to the new clauses (added words in bold here only):

«El Presidente del Gobierno y los órganos colegiados ejecutivos autonómicos disponen de nueve meses cuando, **con la
finalidad de evitar la interposición del recurso,** se reúne la Comisión Bilateral de Cooperación y acuerda iniciar
negociaciones. Ese acuerdo debe comunicarse al Tribunal dentro de los tres meses siguientes a la publicación **e
insertarse en el «Boletín Oficial del Estado» y en el «Diario Oficial» de la Comunidad Autónoma correspondiente** (art.
33.2 LOTC).»

Norm: «… podrán interponer el recurso de inconstitucionalidad en el plazo de nueve meses contra leyes, disposiciones o
actos con fuerza de Ley en relación con las cuales, y con la finalidad de evitar la interposición del recurso, se
cumplan los siguientes requisitos: … c) Que el acuerdo sea puesto en conocimiento del Tribunal Constitucional por los
órganos anteriormente mencionados dentro de los tres meses siguientes a la publicación de la Ley, disposición o acto
con fuerza de Ley, y se inserte en el "Boletín Oficial del Estado'' y en el "Diario Oficial'' de la Comunidad Autónoma
correspondiente.»

### Art. 35.2 LOTC (l. 297–301)

Two sentences added around the existing audiencia sentence:

- «El órgano judicial solo puede plantearla una vez concluso el procedimiento y dentro del plazo para dictar sentencia,
  o la resolución jurisdiccional que proceda (art. 35.2 LOTC).»
- «Seguidamente y sin más trámite, el juez resuelve en el plazo de tres días (art. 35.2 LOTC).»

Norm: «El órgano judicial sólo podrá plantear la cuestión una vez concluso el procedimiento y dentro del plazo para
dictar sentencia, o la resolución jurisdiccional que procediese, …» and «… seguidamente y sin más trámite, el juez
resolverá en el plazo de tres días.»

### Art. 7.2 LO 3/1981 (l. 390–392)

Existing sentence joined (added words in bold): «Debe cesar en toda situación de incompatibilidad dentro de los diez
días siguientes a su nombramiento y antes de tomar posesión**; en caso contrario, se entiende que no acepta el
nombramiento** (art. 7.2 LO 3/1981).»

Norm: «El Defensor del Pueblo deberá cesar, dentro de los diez días siguientes a su nombramiento y antes de tomar
posesión, en toda situación de incompatibilidad que pudiera afectarle, entendiéndose en caso contrario que no acepta el
nombramiento.»

### Normativa list (l. 483)

«LO 2/1979 (LOTC): arts. 1, 6, 7, 9, 16–18, 32, 33, 35, 41–44, 49 y 76.» (76 added).

### Rows restored in the TC plazos table (l. 304–313)

Title: «Tres plazos: la suspensión del artículo 161.2, el recurso y la cuestión de inconstitucionalidad» →
**«Algunos plazos de la impugnación del Gobierno, del recurso y de la cuestión de inconstitucionalidad»**. With seven
rows «Tres plazos» is false. «Algunos» marks it as a selection: art. 34.2 LOTC (quince días de alegaciones, sentencia
en diez) and art. 77 LOTC are not in the table or the prose. The «ante el Tribunal Constitucional» wording of fix 21 is
not brought back.

| Row (l.) | Text | Support |
|---|---|---|
| 306 | Impugnación por el Gobierno de las disposiciones normativas sin fuerza de ley y las resoluciones de cualquier órgano de las Comunidades Autónomas \| Dentro de los dos meses siguientes a la fecha de su publicación o, en defecto de la misma, desde que llegare a su conocimiento \| art. 76 LOTC | Art. 76 verbatim; prose l. 275–277 |
| 309 | Recurso de inconstitucionalidad del Presidente del Gobierno y de los órganos colegiados ejecutivos autonómicos cuando, con la finalidad de evitar la interposición del recurso, se reúne la Comisión Bilateral de Cooperación, acuerda iniciar negociaciones y el acuerdo se comunica al Tribunal dentro de los tres meses siguientes a la publicación y se inserta en el «Boletín Oficial del Estado» y en el «Diario Oficial» de la Comunidad Autónoma correspondiente \| Nueve meses \| art. 33.2 LOTC | The nine-month row. Every requisito (a, b, c) and the purpose clause, in the prose's words (l. 286–291); «se inserte» is the norm's verb |
| 310 | Cuestión de inconstitucionalidad: el órgano judicial solo puede plantearla una vez concluso el procedimiento \| Dentro del plazo para dictar sentencia, o la resolución jurisdiccional que proceda \| art. 35.2 LOTC | Prose l. 297–299; 35.2 first sentence |
| 312 | Cuestión de inconstitucionalidad: tras oír a las partes y al Ministerio Fiscal, el juez resuelve sin más trámite \| Tres días \| art. 35.2 LOTC | Prose l. 300–301; 35.2 «seguidamente y sin más trámite, el juez resolverá en el plazo de tres días» |

The 161.2 CE, 33.1 and 35.2 (10 días) rows are unchanged. No row for 7.2 LO 3/1981: the Defensor table is titled for
arts. 2 and 5, and the gap list did not ask for one.

## m01-l03

### Art. 93.1 Reglamento del Senado (l. 213–216)

Existing sentence joined (added words in bold): «En el Senado, **sin perjuicio de las mayorías especiales que
establezcan la Constitución o las leyes orgánicas y las que para la elección de personas dispone su Reglamento,** los
acuerdos se adoptan por la mayoría simple de Senadores presentes, siempre que lo esté la mitad más uno de los miembros
del órgano (art. 93.1 Reglamento del Senado).»

Norm: «Sin perjuicio de las mayorías especiales que establezcan la Constitución o las leyes orgánicas, y las que para
la elección de personas se dispone en este Reglamento, los acuerdos se adoptarán por la mayoría simple de Senadores
presentes, siempre que lo esté la mitad más uno de los miembros del órgano de que se trate.»

### Art. 41.1 Reglamento del Congreso (l. 259–260)

Existing sentence joined: «Cada Comisión, **con las excepciones previstas en el Reglamento,** elige una Mesa compuesta
por una Presidencia, dos Vicepresidencias y dos Secretarías (art. 41.1 Reglamento del Congreso).»

Norm: «Las Comisiones, con las excepciones previstas en este Reglamento, eligen de entre sus miembros una Mesa,
compuesta por una Presidencia, dos Vicepresidencias y dos Secretarías.»

### Art. 46.2 Reglamento del Congreso (l. 262–264)

Existing sentence joined: «Son también Comisiones Permanentes, además de las legislativas, **aquellas que deban
constituirse por disposición legal y** las de Reglamento, Estatuto y Peticiones (art. 46.2 Reglamento del Congreso).»

Norm: «Son también Comisiones Permanentes aquellas que deban constituirse por disposición legal y las siguientes: 1ª.
Reglamento. 2ª. Estatuto. 3ª. Peticiones.»

The paragraph l. 259–264 was re-wrapped; only the two clauses above are new.

### Row restored in «Algunos quórum y mayorías de las Cortes Generales» (l. 422)

| Row | Support |
|---|---|
| Acuerdos del Senado, sin perjuicio de las mayorías especiales que establezcan la Constitución o las leyes orgánicas y las que para la elección de personas dispone su Reglamento \| La mayoría simple de Senadores presentes, siempre que lo esté la mitad más uno de los miembros del órgano de que se trate \| art. 93.1 Reglamento del Senado | Prose l. 213–216; «de que se trate» is the norm verbatim |

Title unchanged: the art. 39.1 Reglamento del Congreso petition is still not a row, so «Algunos» stays true.

Not added: a 41.1 row. Art. 41.1 sets the composition of a Comisión's Mesa, not a quórum or majority, so it does not
fit this table. The Congreso «Comisiones» node of the Cortes tree cites art. 75.1 CE, and a node cites one norm, so
41.1 cannot join it without replacing that node. Left out.

## m01-l04

### Art. 595.1 LOPJ (l. 159–160)

Existing sentence joined: «**Además de las funciones encomendadas a la Presidencia,** el Consejo ejerce sus
atribuciones en Pleno o a través de sus Comisiones (art. 595.1 LOPJ).»

Norm: «Además de las funciones encomendadas a la Presidencia, el Consejo General del Poder Judicial ejerce sus
atribuciones en Pleno o a través de las Comisiones previstas en esta Ley Orgánica.»

### Art. 630.1 LOPJ (l. 183–190)

The existing three-fifths sentence now carries the whole first list, and one sentence is added for the second list
of the same apartado:

- «El nombramiento de Presidentes de Sala y Magistrados del Tribunal Supremo, Presidente de la Audiencia Nacional y
  Presidentes de Sala de la Audiencia Nacional, Presidentes de los Tribunales Superiores de Justicia y Presidentes de
  Sala de los Tribunales Superiores de Justicia, y Presidentes de Audiencias Provinciales exige tres quintos de los
  miembros presentes (art. 630.1 LOPJ).»
- «El nombramiento del Magistrado del Tribunal Supremo, y de su sustituto, competentes para conocer de las actividades
  del Centro Nacional de Inteligencia que afecten a los derechos fundamentales del artículo 18, apartados 2 y 3, de la
  Constitución exige la misma mayoría (art. 630.1 LOPJ).»

Norm: «… salvo cuando esta Ley Orgánica disponga otra cosa o cuando se trate del nombramiento de Presidentes de Sala y
Magistrados del Tribunal Supremo, Presidente de la Audiencia Nacional y Presidentes de Sala de la Audiencia Nacional,
Presidentes de los Tribunales Superiores de Justicia y Presidentes de Sala de los Tribunales Superiores de Justicia, y
Presidentes de Audiencias Provinciales, en cuyo caso se requerirá una mayoría de tres quintos de los miembros
presentes. Igualmente, se requerirá mayoría de tres quintos de los miembros presentes cuando se trate del nombramiento
del Magistrado del Tribunal Supremo, y de su sustituto, competentes para conocer de las actividades del Centro
Nacional de Inteligencia que afecten a los derechos fundamentales reconocidos en el artículo 18, apartados 2 y 3, de
la Constitución.»

The CNI sentence goes beyond the ledger's item. It is there because recheck.md (row 8) failed the default row for
letting a three-fifths nombramiento read as mayoría absoluta. Without the CNI sentence the restored rows would leave
the same hole for that nombramiento.

### Rows restored in «Mayorías en la elección de los Vocales y en algunos acuerdos del CGPJ» (l. 216–218)

Fixes 12 and 22:

| Row | Support |
|---|---|
| Nombramiento de Presidentes de Sala y Magistrados del Tribunal Supremo, Presidente de la Audiencia Nacional y Presidentes de Sala de la Audiencia Nacional, Presidentes de los Tribunales Superiores de Justicia y Presidentes de Sala de los Tribunales Superiores de Justicia, y Presidentes de Audiencias Provinciales \| Los órganos colegiados del Consejo \| Tres quintos de los miembros presentes \| art. 630.1 LOPJ | Prose l. 184–187; the whole first list, verbatim |
| Nombramiento del Magistrado del Tribunal Supremo, y de su sustituto, competentes para conocer de las actividades del Centro Nacional de Inteligencia que afecten a los derechos fundamentales del artículo 18, apartados 2 y 3, de la Constitución \| Los órganos colegiados del Consejo \| Tres quintos de los miembros presentes \| art. 630.1 LOPJ | Prose l. 187–190 |
| Los demás acuerdos, salvo que la ley disponga otra cosa \| Los órganos colegiados del Consejo \| Mayoría absoluta de los miembros presentes \| art. 630.1 LOPJ | Prose l. 183–184. «Los demás» points to the two nombramiento rows directly above. «Salvo que la ley disponga otra cosa» is the prose's shortening, which verify-m01-l04 #9 passed. The voto de calidad stays out of the row: the norm states it for every acuerdo, so putting it in this row alone would read narrower than the norm |

Title unchanged: arts. 580.4, 589.4–5 and 599.3 are still not rows, so «algunos acuerdos» stays true.

## m01-l07

### Art. 19.3 Ley 19/2013 (l. 163–165)

Existing sentence joined: «…se les concede un plazo de quince días para alegaciones, con suspensión del plazo para
resolver **hasta que se hayan recibido las alegaciones o haya transcurrido el plazo para su presentación** (art. 19.3
Ley 19/2013).»

Norm: «… así como de la suspensión del plazo para dictar resolución hasta que se hayan recibido las alegaciones o haya
transcurrido el plazo para su presentación.»

Row (l. 171), «Efecto» cell, extended to match the prose: «Suspensión del plazo para resolver hasta que se hayan
recibido las alegaciones o haya transcurrido el plazo para su presentación». The row passed before. It now carries the
end point of the suspension.

### DA 4.ª.3 Ley 19/2013 (l. 224–226)

Added: «Las Ciudades con Estatuto de Autonomía pueden designar sus propios órganos independientes o bien atribuir la
competencia al Consejo mediante un convenio en los mismos términos (disposición adicional cuarta Ley 19/2013).»

Norm: «3. Las Ciudades con Estatuto de Autonomía podrán designar sus propios órganos independientes o bien atribuir la
competencia al Consejo de Transparencia y Buen Gobierno, celebrando al efecto un Convenio en los términos previstos en
el apartado anterior.»

The citation keeps the lesson's form for the DA, with no apartado, as l. 224 already writes it. No row: the plazos
timeline already sends the reader to DA 4.ª through art. 24.6.

## m01-l09

### Medio ambiente and ferrocarriles (l. 282–290)

Two pairs added to the «El examen mezcla…» paragraph, in its own shape («X: Comunidades (art.); Y: Estado (art.)»):

- «Gestión en materia de protección del medio ambiente: Comunidades (art. 148.1.9.ª CE); legislación básica sobre
  protección del medio ambiente, sin perjuicio de las facultades de las Comunidades Autónomas de establecer normas
  adicionales de protección: Estado (art. 149.1.23.ª CE).»
- «Ferrocarriles y carreteras cuyo itinerario se desarrolle íntegramente en el territorio de la Comunidad: Comunidades
  (art. 148.1.5.ª CE); ferrocarriles y transportes terrestres que transcurran por el territorio de más de una
  Comunidad: Estado (art. 149.1.21.ª CE).»

Norm (CE): 148.1 «9.ª La gestión en materia de protección del medio ambiente.»; 149.1 «23.ª Legislación básica sobre
protección del medio ambiente, sin perjuicio de las facultades de las Comunidades Autónomas de establecer normas
adicionales de protección. …»; 148.1 «5.ª Los ferrocarriles y carreteras cuyo itinerario se desarrolle íntegramente en
el territorio de la Comunidad Autónoma y, en los mismos términos, el transporte desarrollado por estos medios o por
cable.»; 149.1 «21.ª Ferrocarriles y transportes terrestres que transcurran por el territorio de más de una Comunidad
Autónoma; …».

Medio ambiente sits after montes (both 149.1.23.ª). Ferrocarriles sits before tráfico (both 149.1.21.ª). The paragraph
was re-wrapped; the other pairs are unchanged.

### Rows restored (fixes 13–14; l. 297 and l. 300)

| Row | Support |
|---|---|
| Medio ambiente \| 9.ª La gestión en materia de protección del medio ambiente \| 23.ª Legislación básica sobre protección del medio ambiente, sin perjuicio de las facultades de las Comunidades Autónomas de establecer normas adicionales de protección \| arts. 148.1.9.ª y 149.1.23.ª CE | CE verbatim; pair in prose l. 283–285 |
| Ferrocarriles \| 5.ª Los ferrocarriles y carreteras cuyo itinerario se desarrolle íntegramente en el territorio de la Comunidad Autónoma y, en los mismos términos, el transporte desarrollado por estos medios o por cable \| 21.ª Ferrocarriles y transportes terrestres que transcurran por el territorio de más de una Comunidad Autónoma \| arts. 148.1.5.ª y 149.1.21.ª CE | CE verbatim; pair in prose l. 287–289 |

Title: «Tres materias…» → **«Cinco materias en las dos listas de los artículos 148.1 y 149.1»**. The table holds
exactly the five pairs the prose makes. Tráfico has no 148.1 counterpart, so it is not a pair.

## m01-l11

### Art. 235.1 TFUE (l. 77–79)

Added after the 235.3 sentence:
- «Cuando se pronuncia por mayoría cualificada, se le aplican el artículo 16.4 del TUE y el artículo 238.2 del TFUE
  (art. 235.1 TFUE).»
- «Su Presidente y el Presidente de la Comisión no participan en las votaciones (art. 235.1 TFUE).»

Norm: «El apartado 4 del artículo 16 del Tratado de la Unión Europea y el apartado 2 del artículo 238 del presente
Tratado se aplicarán al Consejo Europeo cuando se pronuncie por mayoría cualificada. El Presidente del Consejo Europeo
y el Presidente de la Comisión no participarán en las votaciones del Consejo Europeo cuando éste se pronuncie por
votación.»

The first párrafo of 235.1 (each member may act for one other) and its third (abstention and unanimity) are left out.
Neither is a condition of the two facts added.

### Art. 238.2 TFUE (l. 156–159)

Existing sentence joined: «**A reserva de las disposiciones fijadas en el Protocolo sobre las disposiciones
transitorias,** cuando el Consejo no actúa a propuesta de la Comisión o del Alto Representante, la mayoría cualificada
sube a un mínimo del 72 % … (art. 238.2 TFUE).»

Norm: «No obstante lo dispuesto en el apartado 4 del artículo 16 del Tratado de la Unión Europea, a partir del 1 de
noviembre de 2014, a reserva de las disposiciones fijadas en el Protocolo sobre las disposiciones transitorias, cuando
el Consejo no actúe a propuesta de la Comisión o del Alto Representante … la mayoría cualificada se definirá como un
mínimo del 72 % …»

### Art. 238.3 TFUE (l. 161–169)

New paragraph, three sentences. The apartado has two letters plus the blocking minority, and dropping any of them
would make the 55 % read wider:

- «Con la misma reserva, cuando, en aplicación de los Tratados, no todos los miembros del Consejo participan en la
  votación, la mayoría cualificada es un mínimo del 55 % de los miembros del Consejo que represente a Estados miembros
  participantes que reúnan como mínimo el 65 % de la población de dichos Estados (art. 238.3 TFUE).»
- «La minoría de bloqueo está compuesta al menos por el número mínimo de miembros del Consejo que represente más del
  35 % de la población de los Estados miembros participantes, más un miembro; sin ella, la mayoría cualificada se
  considera alcanzada (art. 238.3 TFUE).»
- «Si el Consejo no actúa a propuesta de la Comisión o del Alto Representante, el mínimo es del 72 % de los miembros
  del Consejo que represente a Estados miembros participantes que reúnan como mínimo el 65 % de la población de dichos
  Estados (art. 238.3 TFUE).»

Norm: «3. A partir del 1 de noviembre de 2014, a reserva de las disposiciones fijadas en el Protocolo sobre las
disposiciones transitorias, en aquellos casos en que, en aplicación de los Tratados, no todos los miembros del Consejo
participen en la votación, la mayoría cualificada se definirá como sigue: a) La mayoría cualificada se definirá como un
mínimo del 55 % de los miembros del Consejo que represente a Estados miembros participantes que reúnan como mínimo el
65 % de la población de dichos Estados. Una minoría de bloqueo estará compuesta al menos por el número mínimo de
miembros del Consejo que represente más del 35 % de la población de los Estados miembros participantes, más un
miembro, a falta de lo cual la mayoría cualificada se considerará alcanzada. b) No obstante lo dispuesto en la letra
a), cuando el Consejo no actúe a propuesta de la Comisión o del Alto Representante de la Unión para Asuntos Exteriores
y Política de Seguridad, la mayoría cualificada se definirá como un mínimo del 72 % de los miembros del Consejo que
represente a Estados miembros participantes que reúnan como mínimo el 65 % de la población de dichos Estados.»

The 238.2 and 238.3 sentences leave out «a partir del 1 de noviembre de 2014». The 16.4 sentence just above opens
with «Desde el 1 de noviembre de 2014», and the earlier 238.2 sentence passed without the date. The rows carry the
date, verbatim.

### Rows in «Algunas reglas de votación…» (fixes 17 and 25; l. 290–294)

| Row | Support |
|---|---|
| Consejo Europeo, cuando se pronuncie por mayoría cualificada \| Se aplicarán el apartado 4 del artículo 16 del Tratado de la Unión Europea y el apartado 2 del artículo 238 del Tratado de Funcionamiento de la Unión Europea. El Presidente del Consejo Europeo y el Presidente de la Comisión no participarán en las votaciones \| art. 235.1 TFUE | 235.1 verbatim; prose l. 77–79 |
| 16.4 TUE row, label changed: «…, salvo los casos de los apartados 2 y 3 del artículo 238 del Tratado de Funcionamiento de la Unión Europea» (was «salvo el caso del artículo 238.2…») | 238.2 opens «No obstante lo dispuesto en el apartado 4 del artículo 16»; 238.3 gives a different definition when not all members vote. Both are now rows and in the prose, so a label naming only 238.2 would let 16.4 read as covering the 238.3 case. Cell unchanged |
| Consejo, mayoría cualificada a partir del 1 de noviembre de 2014, cuando no actúe a propuesta de la Comisión o del Alto Representante, a reserva de las disposiciones fijadas en el Protocolo sobre las disposiciones transitorias \| Un mínimo del 72 % de los miembros del Consejo que represente a Estados miembros que reúnan como mínimo el 65 % de la población de la Unión \| art. 238.2 TFUE | The reviewers' 238.2 row, now with its «a reserva de» clause (prose l. 156–159); date from the norm, verbatim |
| Consejo, mayoría cualificada a partir del 1 de noviembre de 2014 cuando, en aplicación de los Tratados, no todos los miembros del Consejo participen en la votación, a reserva de las disposiciones fijadas en el Protocolo sobre las disposiciones transitorias \| Un mínimo del 55 % de los miembros del Consejo que represente a Estados miembros participantes que reúnan como mínimo el 65 % de la población de dichos Estados; del 72 % cuando el Consejo no actúe a propuesta de la Comisión o del Alto Representante. Una minoría de bloqueo estará compuesta al menos por el número mínimo de miembros del Consejo que represente más del 35 % de la población de los Estados miembros participantes, más un miembro, a falta de lo cual la mayoría cualificada se considerará alcanzada \| art. 238.3 TFUE | 238.3 a) and b), verbatim or shortened in the prose's words (l. 161–169) |

Title unchanged: «Algunas» is still true (the moción de censura, art. 234 TFUE, is not a row).

## Not closed

- **41.1 Reglamento del Congreso row:** the prose gap is closed, but no row was added. The reason is in the m01-l03
  section: it is not a majority, and the tree node it would join cites another norm.
- **7.2 LO 3/1981 and DA 4.ª.3 Ley 19/2013:** the prose gaps are closed. No row was asked for and none was added.

Every other gap listed in the ledger's open item 1 is closed, and every row it blocked has been restored.

## Watch points for the blind check and the goldens

- New prose citations (all anchors that the lessons already cite, except one): art. 76 LOTC (new anchor in m01-l01);
  art. 33.2, 35.2 LOTC; art. 7.2 LO 3/1981; arts. 93.1 RS, 41.1, 46.2 RC (existing citations, longer sentences); art.
  595.1, 630.1 LOPJ (one extra 630.1 citation); art. 19.3 and DA 4.ª Ley 19/2013 (one extra DA 4.ª citation); arts.
  148.1.9.ª, 149.1.23.ª, 148.1.5.ª, 149.1.21.ª CE (four extra citations); art. 235.1 TFUE (two, new apartado of art.
  235), art. 238.3 TFUE (three).
- New esquema rows: m01-l01 +4, m01-l03 +1, m01-l04 +3, m01-l09 +2, m01-l11 +3. Changed rows: m01-l07 19.3 cell, m01-l11
  16.4 label.
- Glossary marks that may move: «mayoría cualificada» and «mayoría simple» (m01-l11, l. 77–79 now writes «mayoría
  cualificada» earlier than before), «Comisión Bilateral de Cooperación» and «Ministerio Fiscal» (m01-l01), «Audiencia
  Nacional» and «Tribunales Superiores de Justicia» (m01-l04, l. 185–186, ahead of the TS/AN sections), «Defensor del
  Pueblo» is unaffected.
- Prose in parentheses only cites: «artículo 16.4 del TUE», «artículo 18, apartados 2 y 3, de la Constitución» are
  outside parentheses and are not citation leads (the grammar only reads parentheticals).
- The reading-time check may move for m01-l01, m01-l04 and m01-l11 (the largest additions).

## Not run

On the coordinator's instruction (another task is changing the test suite), pytest was not run, and
`citations.es.txt`, `glossary-links.es.txt` and `lesson-refs.es.txt` were not regenerated. Expected on the next run:
`test_every_citation_has_its_anchors_and_target_as_frozen[age-administrativo-c1]` fails until `citations.es.txt` is
regenerated (new prose citations and esquema rows above). Glossary-links / lesson-refs may move per the watch points.
