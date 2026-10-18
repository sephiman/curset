# Prose gaps of «Esquemas bloque I» (open item 1): blind verification, 2026-10-18

Reviewer did not write the change. Scope: `git diff -- content/age-administrativo-c1/es/lessons/` (m01-l01, m01-l03,
m01-l04, m01-l07, m01-l09, m01-l11). Norm texts: `pdftotext -layout` of the files named in `sources/normativa.yaml`
(LOTC `BOE-A-1979-23709_…_2024-08-02`, LO 3/1981 `BOE-A-1981-10325_…_2009-11-04`, Reglamento del Senado
`BOE-A-1994-10830_…_2025-11-14`, Reglamento del Congreso `BOE-A-1982-5196_…_2026-07-28`, LOPJ
`BOE-A-1985-12666_…_2025-02-17`, Ley 19/2013 `BOE-A-2013-12887_…_2022-07-09`, CE `BOE-A-1978-31229_…_2026-05-20`, TFUE
`CELEX-02016E-20250315`, TUE `CELEX-02016M-20250315`). Line numbers are those of the lesson files after the change.
Judgments were made before reading `writer.md`; it was read afterwards only to confirm every item is covered.
pytest not run and goldens not touched (per instruction).

Totals: **39 items, 37 PASS, 2 FAIL.**

| # | Lesson | Line | Item | Result | Reason (norm quoted) |
|---|---|---|---|---|---|
| 1 | m01-l01 | 275–277 | Prose: plazo de dos meses, art. 76 LOTC | PASS | «Dentro de los dos meses siguientes a la fecha de su publicación o, en defecto de la misma, desde que llegare a su conocimiento, el Gobierno podrá impugnar … las disposiciones normativas sin fuerza de Ley y resoluciones emanadas de cualquier órgano de las Comunidades Autónomas.» «sin fuerza de ley» kept; «las resoluciones» takes its CCAA scope from the 161.2 sentence before it. Form «art. N LOTC» is the lesson's |
| 2 | m01-l01 | 286–291 | Prose: purpose clause and BOE/Diario Oficial insertion, art. 33.2 LOTC | PASS | «con la finalidad de evitar la interposición del recurso»; c) «… dentro de los tres meses siguientes a la publicación … y se inserte en el "Boletín Oficial del Estado'' y en el "Diario Oficial'' de la Comunidad Autónoma correspondiente». Norm's phrase verbatim; «» quotes match l. 332 |
| 3 | m01-l01 | 297–299 | Prose: «solo puede plantearla una vez concluso el procedimiento…», art. 35.2 LOTC | PASS | «El órgano judicial sólo podrá plantear la cuestión una vez concluso el procedimiento y dentro del plazo para dictar sentencia, o la resolución jurisdiccional que procediese» |
| 4 | m01-l01 | 300–301 | Prose: «Seguidamente y sin más trámite, el juez resuelve en el plazo de tres días», art. 35.2 LOTC | PASS | «seguidamente y sin más trámite, el juez resolverá en el plazo de tres días». Note: l. 299 runs past the file's wrap width (cosmetic) |
| 5 | m01-l01 | 390–392 | Prose: «en caso contrario, se entiende que no acepta el nombramiento», art. 7.2 LO 3/1981 | PASS | «deberá cesar, dentro de los diez días siguientes a su nombramiento y antes de tomar posesión, en toda situación de incompatibilidad …, entendiéndose en caso contrario que no acepta el nombramiento» |
| 6 | m01-l01 | 483 | Normativa list: LOTC «…, 49 y 76» | PASS | Art. 76 is now cited in the prose; no sub-range |
| 7 | m01-l01 | 303 | Title «Algunos plazos de la impugnación del Gobierno, del recurso y de la cuestión de inconstitucionalidad» | PASS | «Algunos» marks a selection (art. 34.2 and 77 LOTC plazos are not rows); the old «Tres plazos» would be false with seven rows |
| 8 | m01-l01 | 306 | Row art. 76 LOTC | PASS | Plazo cell verbatim; label «resoluciones de cualquier órgano» is the norm's «resoluciones emanadas de cualquier órgano»; citation in prose (l. 277) |
| 9 | m01-l01 | 309 | Row nueve meses, art. 33.2 LOTC | PASS | Every requisito a)–c) and the purpose clause in the prose's words (l. 286–291); «Nueve meses» = «en el plazo de nueve meses» |
| 10 | m01-l01 | 310 | Row «solo puede plantearla una vez concluso el procedimiento», art. 35.2 LOTC | PASS | As item 3; tabla claims no order |
| 11 | m01-l01 | 312 | Row «el juez resuelve sin más trámite — Tres días», art. 35.2 LOTC | PASS | As item 4 |
| 12 | m01-l03 | 213–216 | Prose: «sin perjuicio de las mayorías especiales…», art. 93.1 Reglamento del Senado | PASS | «Sin perjuicio de las mayorías especiales que establezcan la Constitución o las leyes orgánicas, y las que para la elección de personas se dispone en este Reglamento, los acuerdos se adoptarán por la mayoría simple de Senadores presentes, siempre que lo esté la mitad más uno de los miembros del órgano de que se trate.» Long sentence but one idea |
| 13 | m01-l03 | 259–260 | Prose: «con las excepciones previstas en el Reglamento», art. 41.1 RC | PASS | «Las Comisiones, con las excepciones previstas en este Reglamento, eligen de entre sus miembros una Mesa, compuesta por una Presidencia, dos Vicepresidencias y dos Secretarías» |
| 14 | m01-l03 | 262–264 | Prose: «aquellas que deban constituirse por disposición legal», art. 46.2 RC | PASS | «Son también Comisiones Permanentes aquellas que deban constituirse por disposición legal y las siguientes: 1ª. Reglamento. 2ª. Estatuto. 3ª. Peticiones.» |
| 15 | m01-l03 | 422 | Row «Acuerdos del Senado, sin perjuicio de…», art. 93.1 RS | PASS | Verbatim (item 12); citation in prose; title «Algunos quórum y mayorías» stays a selection |
| 16 | m01-l04 | 159–160 | Prose: «Además de las funciones encomendadas a la Presidencia», art. 595.1 LOPJ | PASS | «Además de las funciones encomendadas a la Presidencia, el Consejo General del Poder Judicial ejerce sus atribuciones en Pleno o a través de las Comisiones previstas en esta Ley Orgánica» |
| 17 | m01-l04 | 184–187 | Prose: full first list of three-fifths nombramientos, art. 630.1 LOPJ | PASS | «nombramiento de Presidentes de Sala y Magistrados del Tribunal Supremo, Presidente de la Audiencia Nacional y Presidentes de Sala de la Audiencia Nacional, Presidentes de los Tribunales Superiores de Justicia y Presidentes de Sala de los Tribunales Superiores de Justicia, y Presidentes de Audiencias Provinciales, en cuyo caso se requerirá una mayoría de tres quintos de los miembros presentes» |
| 18 | m01-l04 | 187–190 | Prose: CNI Magistrate «exige la misma mayoría», art. 630.1 LOPJ | PASS | «Igualmente, se requerirá mayoría de tres quintos de los miembros presentes cuando se trate del nombramiento del Magistrado del Tribunal Supremo, y de su sustituto, competentes para conocer de las actividades del Centro Nacional de Inteligencia que afecten a los derechos fundamentales reconocidos en el artículo 18, apartados 2 y 3, de la Constitución» («reconocidos en» shortened to «del», no change of meaning) |
| 19 | m01-l04 | 216 | Row first list, three fifths, art. 630.1 LOPJ | PASS | Verbatim list; organ «Los órganos colegiados del Consejo» = «Los acuerdos de los órganos colegiados del Consejo General del Poder Judicial» |
| 20 | m01-l04 | 217 | Row CNI Magistrate, art. 630.1 LOPJ | PASS | As item 18 |
| 21 | m01-l04 | 218 | Row «Los demás acuerdos, salvo que la ley disponga otra cosa — Mayoría absoluta de los miembros presentes» | PASS | «serán adoptados por mayoría absoluta de los miembros presentes, salvo cuando esta Ley Orgánica disponga otra cosa o cuando se trate del nombramiento …». «Los demás» points to the two nombramiento rows; the other Pleno rows (3/5) are covered by the «salvo» clause. «la ley» for «esta Ley Orgánica» is the prose's existing wording (l. 183–184), not new in this change |
| 22 | m01-l07 | 163–165 | Prose: suspension «hasta que se hayan recibido las alegaciones o haya transcurrido el plazo para su presentación», art. 19.3 Ley 19/2013 | PASS | «la suspensión del plazo para dictar resolución hasta que se hayan recibido las alegaciones o haya transcurrido el plazo para su presentación» |
| 23 | m01-l07 | 171 | Row 19.3, «Efecto» cell | PASS | Verbatim, as item 22; citation in prose |
| 24 | m01-l07 | 224–226 | Prose: Ciudades con Estatuto de Autonomía, DA 4.ª Ley 19/2013 | PASS | DA 4.ª.3: «podrán designar sus propios órganos independientes o bien atribuir la competencia al Consejo de Transparencia y Buen Gobierno, celebrando al efecto un Convenio en los términos previstos en el apartado anterior». Citation form without apartado matches l. 224 |
| 25 | m01-l09 | 283–285 | Prose: medio ambiente pair, arts. 148.1.9.ª and 149.1.23.ª CE | PASS | 148.1 «9.ª La gestión en materia de protección del medio ambiente.»; 149.1 «23.ª Legislación básica sobre protección del medio ambiente, sin perjuicio de las facultades de las Comunidades Autónomas de establecer normas adicionales de protección.» Exception kept |
| 26 | m01-l09 | 287–289 | Prose: ferrocarriles pair, arts. 148.1.5.ª and 149.1.21.ª CE | PASS | 148.1 «5.ª Los ferrocarriles y carreteras cuyo itinerario se desarrolle íntegramente en el territorio de la Comunidad Autónoma …»; 149.1 «21.ª Ferrocarriles y transportes terrestres que transcurran por el territorio de más de una Comunidad Autónoma». The omitted «transporte … por cable» is a further item, not a condition |
| 27 | m01-l09 | 292 | Title «Cinco materias en las dos listas de los artículos 148.1 y 149.1» | PASS | Five rows; indefinite «Cinco materias» (no article) reads as a selection, as the old «Tres materias» did |
| 28 | m01-l09 | 296 | Row Medio ambiente | PASS | Both cells verbatim CE; «arts. 148.1.9.ª y 149.1.23.ª CE» in the table's form, both anchors in prose |
| 29 | m01-l09 | 299 | Row Ferrocarriles | PASS | Both cells verbatim CE; both anchors in prose |
| 30 | m01-l11 | 77–78 | Prose: «Cuando se pronuncia por mayoría cualificada, se le aplican el artículo 16.4 del TUE y el artículo 238.2 del TFUE», art. 235.1 TFUE | PASS | «El apartado 4 del artículo 16 del Tratado de la Unión Europea y el apartado 2 del artículo 238 del presente Tratado se aplicarán al Consejo Europeo cuando se pronuncie por mayoría cualificada» |
| 31 | m01-l11 | 78–79 | Prose: «Su Presidente y el Presidente de la Comisión no participan en las votaciones», art. 235.1 TFUE | PASS | «… no participarán en las votaciones del Consejo Europeo cuando éste se pronuncie por votación». Stated as its own sentence, so not tied to the QMV condition |
| 32 | m01-l11 | 156–159 | Prose: «A reserva de las disposiciones fijadas en el Protocolo…», art. 238.2 TFUE | PASS | «a reserva de las disposiciones fijadas en el Protocolo sobre las disposiciones transitorias». Date «a partir del 1 de noviembre de 2014» carried by the 16.4 paragraph just above |
| 33 | m01-l11 | 161–164 | Prose: 55 % when not all members vote, art. 238.3 TFUE | PASS | 238.3 a): «un mínimo del 55 % de los miembros del Consejo que represente a Estados miembros participantes que reúnan como mínimo el 65 % de la población de dichos Estados»; lead-in «en aplicación de los Tratados, no todos los miembros del Consejo participen en la votación» kept |
| 34 | m01-l11 | 164–166 | Prose: blocking minority, art. 238.3 TFUE | PASS | «Una minoría de bloqueo estará compuesta al menos por el número mínimo de miembros del Consejo que represente más del 35 % de la población de los Estados miembros participantes, más un miembro, a falta de lo cual la mayoría cualificada se considerará alcanzada». Sits right after the 55 % sentence, as in letter a) |
| 35 | m01-l11 | 166–169 | Prose: 72 % when not on a proposal, art. 238.3 TFUE | PASS | 238.3 b): «cuando el Consejo no actúe a propuesta de la Comisión o del Alto Representante …, la mayoría cualificada se definirá como un mínimo del 72 % … participantes … de dichos Estados» |
| 36 | m01-l11 | 290 | Row «Consejo Europeo, cuando se pronuncie por mayoría cualificada», art. 235.1 TFUE | **FAIL** | The cell's second sentence («El Presidente del Consejo Europeo y el Presidente de la Comisión no participarán en las votaciones») sits under the label's QMV condition and drops the norm's own condition, «del Consejo Europeo cuando éste se pronuncie por votación». The row reads as if the two Presidents stay out only of QMV votes; the norm keeps them out of every vote. False condition, narrower than the article |
| 37 | m01-l11 | 292 | Row 16.4 TUE, label «salvo los casos de los apartados 2 y 3 del artículo 238 del TFUE» | PASS | 238.2: «No obstante lo dispuesto en el apartado 4 del artículo 16 …»; 238.3 gives its own definition «en aquellos casos en que … no todos los miembros del Consejo participen en la votación», which the prose (l. 161–169) states. Without 238.3 in the label the row would read wider |
| 38 | m01-l11 | 293 | Row 238.2 TFUE | PASS | Verbatim, with date and «a reserva de» clause; citation in prose |
| 39 | m01-l11 | 294 | Row 238.3 TFUE | **FAIL** | The cell gives the 55 %, then «del 72 % cuando el Consejo no actúe a propuesta…», and only then the blocking minority. In the norm the blocking minority belongs to letter a) only, and letter b) opens «No obstante lo dispuesto en la letra a)». Placed last, the blocking minority reads as covering the 72 % case too: wider than the article. The prose (l. 161–169) keeps the norm's order, so only the row needs fixing |

## Replacements for the FAILs

**#36, m01-l11 l. 290.** Split into two rows, both in the norm's words and both already supported by the prose
(l. 77–79, where the non-participation is a sentence of its own):

```
| Consejo Europeo, cuando se pronuncie por mayoría cualificada | Se aplicarán el apartado 4 del artículo 16 del Tratado de la Unión Europea y el apartado 2 del artículo 238 del Tratado de Funcionamiento de la Unión Europea | art. 235.1 TFUE |
| Consejo Europeo, cuando se pronuncie por votación | El Presidente del Consejo Europeo y el Presidente de la Comisión no participarán en las votaciones del Consejo Europeo | art. 235.1 TFUE |
```

**#39, m01-l11 l. 294.** Same label. Reorder the cell to the order of letters a) and b):

```
| Consejo, mayoría cualificada a partir del 1 de noviembre de 2014 cuando, en aplicación de los Tratados, no todos los miembros del Consejo participen en la votación, a reserva de las disposiciones fijadas en el Protocolo sobre las disposiciones transitorias | Un mínimo del 55 % de los miembros del Consejo que represente a Estados miembros participantes que reúnan como mínimo el 65 % de la población de dichos Estados. Una minoría de bloqueo estará compuesta al menos por el número mínimo de miembros del Consejo que represente más del 35 % de la población de los Estados miembros participantes, más un miembro, a falta de lo cual la mayoría cualificada se considerará alcanzada. No obstante, cuando el Consejo no actúe a propuesta de la Comisión o del Alto Representante, un mínimo del 72 % de los miembros del Consejo que represente a Estados miembros participantes que reúnan como mínimo el 65 % de la población de dichos Estados | art. 238.3 TFUE |
```

Neither replacement needs a clause the prose lacks.

## Notes outside the PASS/FAIL count (none blocks)

- m01-l01 l. 299 is longer than the file's wrap width (cosmetic re-wrap).
- m01-l01 l. 299–300, unchanged words: «Antes de plantearla, el juez oye…». The norm says «Antes de adoptar mediante
  auto su decisión definitiva», which is the decision whether to raise the question. Not part of this change; the two
  new sentences around it are correct.
- m01-l07 l. 221–224, unchanged sentence: DA 4.ª.1 párrafo 2 (against resolutions of the Asambleas Legislativas and the
  bodies similar to the Consejo de Estado, CES, Tribunal de Cuentas and Defensor del Pueblo «sólo cabrá la
  interposición de recurso contencioso-administrativo») is not in the prose. Pre-existing gap, not introduced here.
- Voice: no filler, rhetorical question, triad, blacklisted split opener or coined term in the added text. The added
  sentences in m01-l03 (93.1) and m01-l04 (630.1) are long, but each carries one idea and follows the norm's list.
