# Verification — bloque IV open items: m04-l01, m04-l02, m04-l03, m04-l05 (2026-10-18)

Blind review; the reviewer wrote none of it. Read: `spec.md` (this folder), `docs/prose-voice.md`, the `::esquema` section
of `docs/platform-delta-handoff.md`, `../../bloque-iv/esquemas/verify-m04-l01-l02-l03.md`, `fixes.md` and
`verify-m04-l05-l06.md` (for what was removed and why). Scope: `git diff` of `C/es/lessons/m04-l01.md`, `m04-l02.md`,
`m04-l03.md`, `m04-l05.md` against HEAD (scratchpad `before/` is identical to HEAD), and the matching lines of
`C/citations.es.txt`. Norm texts: `pdftotext -layout` of `C/sources/normativa/` read with `art.py` — TREBEP arts. 18,
61.8 and disposición final cuarta; RDL 6/2023 art. 114.10; RD 364/1995 arts. 22 and 25; Ley 30/1984 disposición
adicional decimonovena; RD 2271/2004 art. 2; RD 829/2023 art. 22; RD 1009/2023 art. 21. Row and prose citations were
also run through `citations/grammar.py:parse_segment`; all parse to one norm with the expected units.

## m04-l01

| # | item | citation | PASS/FAIL | passage / reason | replacement |
|---|---|---|---|---|---|
| 1 | prose citation «(art. 21.C RD 1009/2023)» (l. 150) | art. 21.C RD 1009/2023 | PASS | Art. 21 C): «La Secretaría de Estado de Función Pública, de la que dependen la Dirección General de Función Pública, con rango de subsecretaría, y la Dirección General de Gobernanza Pública. Asimismo, depende de esta Secretaría de Estado la Oficina de Conflictos de Intereses, con rango de Dirección General.» The sentence matches. `citations.es.txt` now anchors it to boe-a-2023-24842-art-21 (before: RD 829/2023 art. 21, wrong). | — |
| 2 | arbol, root «Ministerio para la Transformación Digital y de la Función Pública — la propuesta y ejecución…» | art. 22.2 RD 829/2023 | PASS | Art. 22.2: «Asimismo corresponde al Ministerio … la propuesta y ejecución de la política del Gobierno en materia de administración pública, función pública, y gobernanza pública.» Verbatim (one comma dropped). Narrower than art. 22 (22.1 gives the digital matters too) and claims no completeness. In prose l. 146–147. | — |
| 3 | arbol, «Secretaría de Estado de Función Pública — órgano superior del Ministerio» | art. 22.3 RD 829/2023 | PASS | Art. 22.3: «Este Ministerio se estructura en los siguientes órganos superiores: […] c) La Secretaría de Estado de Función Pública.» Faithful shortening; apartado without the letter, as the spec asks for a list-type row. Prose l. 147–148 («Uno de sus órganos superiores»). Nested under the Ministry: right. | — |
| 4 | arbol, «Dirección General de Función Pública — con rango de subsecretaría» | art. 21.C RD 1009/2023 | PASS | Art. 21 C) as in #1. Child of the Secretaría de Estado: right («de la que dependen»). Prose l. 148–149. | — |
| 5 | arbol, «Dirección General de Gobernanza Pública» | art. 21.C RD 1009/2023 | PASS | Same passage; same nesting. Prose l. 149. | — |
| 6 | arbol, «Oficina de Conflictos de Intereses — con rango de Dirección General» | art. 21.C RD 1009/2023 | PASS | «Asimismo, depende de esta Secretaría de Estado la Oficina de Conflictos de Intereses, con rango de Dirección General.» Sibling of the two DGs under the Secretaría: right. Prose l. 150. Arbol placed right after that paragraph, before «El Registro Central de Personal». | — |

## m04-l02

| # | item | citation | PASS/FAIL | passage / reason | replacement |
|---|---|---|---|---|---|
| 1 | prose: «Las dos reservan el cupo para personas con discapacidad cuyo grado de minusvalía sea igual o superior al 33 por ciento, y la Ley 30/1984 añade «siempre que…»» (l. 154–157) | disposición adicional decimonovena Ley 30/1984; art. 2.1 RD 2271/2004 | PASS | DA 19.ª: «se reservará un cupo no inferior al cinco por ciento de las vacantes para ser cubiertas entre personas con discapacidad cuyo grado de minusvalía sea igual o superior al 33 por ciento, de modo que, progresivamente se alcance el dos por ciento de los efectivos totales de la Administración del Estado, siempre que superen las pruebas selectivas y que, en su momento, acrediten el indicado grado de minusvalía y la compatibilidad con el desempeño de las tareas y funciones correspondientes, según se determine reglamentariamente.» Art. 2.1 párr. 1 RD 2271/2004: same text up to «33 por ciento.» The 33 % is in both; the quotation is verbatim and keeps both «siempre que» conditions and «en su momento». Dropped: the 2 % objective (not a condition) and «según se determine reglamentariamente» (see Notes). Voice: one idea, no filler, no split opener. | — |
| 2 | tabla «El cupo de reserva…», row Ley 30/1984 | disposición adicional decimonovena Ley 30/1984 | FAIL | Wording is a faithful verbatim shortening of the DA 19.ª (drops only the 2 % objective and «según se determine reglamentariamente»; keeps 5 %, 33 % and both conditions). But «de las vacantes» is a fact the prose does not state: the prose says only «un cupo no inferior al cinco por ciento» (l. 153) and «reservan el cupo para personas con discapacidad…» (l. 154–155). The base of the percentage is what this table contrasts (vacantes / plazas convocadas), so it is a fact, not wording. | Row in the prose's own words: `\| Ley 30/1984 \| Un cupo no inferior al cinco por ciento, para personas con discapacidad cuyo grado de minusvalía sea igual o superior al 33 por ciento, siempre que superen las pruebas selectivas y que, en su momento, acrediten el indicado grado de minusvalía y la compatibilidad con el desempeño de las tareas y funciones correspondientes \| disposición adicional decimonovena Ley 30/1984 \|`. Alternative: keep the row and add «de las vacantes» to the prose at l. 153 («…un cupo no inferior al cinco por ciento de las vacantes:»), which is verbatim from both norms. |
| 3 | same tabla, row RD 2271/2004 | art. 2.1 RD 2271/2004 | FAIL | Wording is art. 2.1 párr. 1 verbatim. Same issue as #2: «de las vacantes» is not in the prose. | `\| RD 2271/2004 \| Un cupo no inferior al cinco por ciento, para personas con discapacidad cuyo grado de minusvalía sea igual o superior al 33 por ciento \| art. 2.1 RD 2271/2004 \|`, or the same prose addition as #2. |

Placement: the table follows the paragraph on the DA 19.ª, the RD 2271/2004 and the derogation clauses (l. 153–162). OK.

## m04-l03

| # | item | citation | PASS/FAIL | passage / reason | replacement |
|---|---|---|---|---|---|
| 1 | prose citation «(art. 21.C RD 1009/2023)» (l. 217) | art. 21.C RD 1009/2023 | PASS | As m04-l01 #1. `citations.es.txt` now anchors to boe-a-2023-24842-art-21. | — |
| 2 | prose: «Si los órganos de selección han propuesto … para su posible nombramiento como funcionarios de carrera (art. 61.8 TREBEP).» (l. 188–191) | art. 61.8 TREBEP | PASS | Art. 61.8 párr. 2: «No obstante lo anterior, siempre que los órganos de selección hayan propuesto el nombramiento de igual número de aspirantes que el de plazas convocadas, y con el fin de asegurar la cobertura de las mismas, cuando se produzcan renuncias de los aspirantes seleccionados, antes de su nombramiento o toma de posesión, el órgano convocante podrá requerir del órgano de selección relación complementaria de los aspirantes que sigan a los propuestos, para su posible nombramiento como funcionarios de carrera.» Condition («siempre que» → «Si»), trigger, timing, organs and purpose kept; only «con el fin de asegurar la cobertura» (a purpose) is dropped. See Notes on «antes de su nombramiento o toma de posesión». Voice OK. | — |
| 3 | prose: «En el RDL 6/2023, cuando se produzcan renuncias … sigan en orden de prelación a las propuestas (art. 114.10 RDL 6/2023).» (l. 191–194) | art. 114.10 RDL 6/2023 | PASS | Art. 114.10 párr. 2: «El órgano convocante, con el fin de asegurar la cobertura de las mismas, podrá requerir del órgano de selección una relación complementaria de las personas aspirantes que, habiendo obtenido la puntuación mínima exigida en la convocatoria, sigan en orden de prelación a las personas propuestas, para su posible nombramiento como personal funcionario de carrera cuando se produzcan renuncias de las personas aspirantes seleccionadas.» Puntuación mínima, orden de prelación, organs and trigger kept. Read alone it lacks the «igual número» limit, but the next sentence states it with the same citation. Voice OK. | — |
| 4 | prose: «El requerimiento se hace en todo caso antes de la toma de posesión y no procede si … (art. 114.10 RDL 6/2023).» (l. 194–196) | art. 114.10 RDL 6/2023 | PASS | «En todo caso, deberá realizarse antes de la de toma de posesión. No procederá dicho requerimiento en el supuesto de que los órganos de selección no hubieran propuesto el nombramiento de igual número de aspirantes que el de plazas convocadas.» Faithful; «deberá realizarse» → «se hace» is the course's flat-rule present. Voice OK (no split opener; two facts of one rule joined by «y»). | — |
| 5 | tabla «Aprobados y plazas convocadas», row TREBEP | art. 61.8 TREBEP | PASS | Art. 61.8 párr. 1 and 2 verbatim; the one «[…]» replaces «y con el fin de asegurar la cobertura de las mismas,» — a purpose, no condition lost. Exception «excepto cuando así lo prevea la propia convocatoria» and the relación complementaria with its «siempre que» condition are both in, so neither reads as the only exception. In prose l. 186–191. | — |
| 6 | same tabla, row RDL 6/2023 | art. 114.10 RDL 6/2023 | PASS | Art. 114.10 párr. 1–3 verbatim; the two «[…]» replace the purpose clauses «con el fin de asegurar la cobertura de las mismas,» and «para su posible nombramiento como personal funcionario de carrera». Puntuación mínima, timing («En todo caso…») and the «No procederá…» limit kept. «antes de la toma de posesión» silently corrects the BOE's «antes de la de toma de posesión». Párr. 4 (relaciones for interinos and laboral temporal) is off topic. In prose l. 186–196. | — |
| 7 | same tabla, row «RD 364/1995, con curso selectivo» | art. 22.3 RD 364/1995 | PASS | Art. 22.3: «El proceso selectivo podrá comprender, además de las pruebas selectivas, un curso selectivo o un período de prácticas. Sólo en el primer caso el número de aprobados en las pruebas selectivas podrá ser superior al de plazas convocadas.» The row is the prose's faithful shortening (l. 180–181), «primer caso» resolved to curso selectivo; nothing wider. | — |
| 8 | same tabla, row «RD 364/1995, nombramiento» | art. 25.1 RD 364/1995 | PASS | Art. 25.1: «Concluido el proceso selectivo, los aspirantes que lo hubieran superado, cuyo número no podrá exceder en ningún caso al de plazas convocadas, serán nombrados funcionarios de carrera por el Secretario de Estado para la Administración Pública. Cualquier resolución que contravenga lo anteriormente establecido será nula de pleno derecho.» Row = prose l. 198–200, faithful; «en ningún caso», organ and nullity kept. | — |

Placement: the table follows the «Nombramiento» paragraphs (l. 186–202); row 7 summarises l. 180–181 in the previous
subsection, which is also above it. The table states the four rules side by side and does not say which applies. OK.

## m04-l05

| # | item | citation | PASS/FAIL | passage / reason | replacement |
|---|---|---|---|---|---|
| 1 | prose: «El artículo 18 está en el capítulo II del título III, que produce efectos a partir de la entrada en vigor de las leyes de Función Pública (disposición final cuarta.1 TREBEP).» (l. 303–304) | disposición final cuarta.1 TREBEP | FAIL | DF 4.ª.1: «Lo establecido en los capítulos II y III del título III, excepto el artículo 25.2, y en el capítulo III del título V producirá efectos a partir de la entrada en vigor de las leyes de Función Pública que se dicten en desarrollo de este Estatuto.» Art. 18 is in capítulo II («Derecho a la carrera profesional y a la promoción interna») of título III: right. Three problems. (a) It drops «que se dicten en desarrollo de este Estatuto», which restricts which laws count; without it any ley de Función Pública (the Ley 30/1984 included, cited in this lesson) reads as enough, so it is wider than the norm. (b) «, que produce efectos» can attach to «título III», and the DF gives effect only to capítulos II and III, not to the whole título. (c) Inserted between the art. 18.2 sentence and «En la Administración del Estado consiste en…», it leaves «consiste» with «el artículo 18» / «el capítulo II» as nearest subject. | «El capítulo II del título III, donde está el artículo 18, produce efectos a partir de la entrada en vigor de las leyes de Función Pública que se dicten en desarrollo del TREBEP (disposición final cuarta.1 TREBEP).» and start the next sentence «En la Administración del Estado la promoción interna consiste en…». m04-l01 l. 97–99 already words the DF this way. |
| 2 | tabla «Requisitos de la promoción interna», row TREBEP (label and citation changed) | art. 18.2 y disposición final cuarta.1 TREBEP | FAIL | Body unchanged and verbatim art. 18.2 (the row's «Subgrupo, y superar» adds a comma the BOE text lacks). Citation parses to one norm with units art. 18 and DF cuarta. The label carries the same truncation as #1 (a): «con efectos a partir de la entrada en vigor de las leyes de Función Pública» without «que se dicten en desarrollo de este Estatuto». | Label: «TREBEP, con efectos a partir de la entrada en vigor de las leyes de Función Pública que se dicten en desarrollo del TREBEP». Needs the clause in the m04-l05 prose (the #1 replacement supplies it); the lesson's prose does not state it now. |

Placement: the table follows the arts. 18.2, DF 4.ª.1, 73 and 76 paragraph (l. 302–309). OK.

## Notes

- m04-l02 #1–#2: «según se determine reglamentariamente» closes the DA 19.ª sentence. It sends the conditions to a
  regulation; it adds no condition of its own, so leaving it out does not widen the row. Same for the 2 % efectivos
  objective, which the TREBEP and RDL rows also leave out.
- m04-l02: art. 2.1 párr. 2 RD 2271/2004 makes the option to the reserved plazas depend on a declaration in the
  solicitud that the grade is met, «acreditado mediante certificado». The prose says only that the Ley 30/1984 «añade»
  its conditions. It does not say the RD sets none, and párr. 2 governs the option, not the reserve, so it is not a
  FAIL. If a reader of the table should not take the RD 2271/2004 row as unconditional, the prose and the row would both
  need that párrafo.
- m04-l03 #2: in art. 61.8 the commas leave it open whether «antes de su nombramiento o toma de posesión» qualifies the
  renuncias or the requerimiento. The prose removes the commas and ties it to the renuncias. With «su» referring to the
  aspirantes seleccionados, that is the natural reading. Not a FAIL. The table row keeps the norm's commas.
- m04-l05: the unchanged opening quotation (l. 19–20) cuts the DF 4.ª.1 at «leyes de Función Pública», with the same
  gap as #1 (a). It is outside this round's diff. Fixing #1 makes the gap less of a problem but does not close it.
- RD 1009/2023: the change the spec required removed the norm's full title from the prose of m04-l01 and m04-l03. Both
  lessons now name it only as «RD 1009/2023»; the full title appears nowhere in either, and the Normativa list says
  «(estructura orgánica básica)». RD 829/2023 is still introduced in full at its first citation (m04-l01 l. 135,
  m04-l03 l. 57). The citation is right; first-mention style is the caller's call.
- `citations.es.txt`: the five m04-l01 arbol citations and the four m04-l03 row citations resolve to the expected anchors
  (RD 829/2023 art. 22, RD 1009/2023 art. 21, TREBEP art. 61, RDL 6/2023 art. 114, RD 364/1995 arts. 22 and 25).
- The course has no `en/` tree, so there is no EN mirror to check.

## Counts

| lesson | items | PASS | FAIL |
|---|---|---|---|
| m04-l01 | 6 | 6 | 0 |
| m04-l02 | 3 | 1 | 2 |
| m04-l03 | 8 | 8 | 0 |
| m04-l05 | 2 | 0 | 2 |
| total | 19 | 15 | 4 |
