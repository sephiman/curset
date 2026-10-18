# Verification — esquemas of m02-l03 and m02-l04 (2026-10-18)

I am a blind reviewer: I wrote neither these esquemas nor the lessons, and I did not read the writer's notes. Scope:
the three `:::esquema` blocks of `C/es/lessons/m02-l03.md` and the four of `C/es/lessons/m02-l04.md`. Rules:
`../../bloque-i/esquemas/spec.md` (bloque II uses it) and the `::esquema` section of `docs/platform-delta-handoff.md`.
Format: `../../bloque-v/esquemas/verify-m05-l03.md`.

Diff: `git diff --numstat` shows 25 added and 0 deleted lines in m02-l03, and 39 added and 0 deleted in m02-l04. The
esquema blocks are the only additions and no prose line changed. Line numbers are those of the current files.

Sources (scratchpad `txt/`, read with `art.py` or `sed`; nothing taken from memory):

- `BOE-A-2021-5032_rd-203-2021-medios-electronicos_2025-04-02.txt`: arts. 3.2, 6.1, 7.3, 7.4, 10.1–10.3.
- `BOE-A-2015-10565_lpac_2024-11-06.txt`: arts. 9.2.c), 43.1–43.4.
- `CELEX-32016R0679_rgpd_2016-05-04.txt`: arts. 12.3–12.5, 15.1, 16, 21.1–21.6.
- `otros-doue-rgpd-correccion-2018.txt` (no correction to arts. 12, 15, 16 or 21) and
  `otros-doue-rgpd-correccion-2021.txt` (correction 3), art. 12.3; correction 9), art. 15.1.c)).
- `BOE-A-2018-16673_lopdgdd_2025-12-27.txt`: arts. 13, 14, 37, 48, 65.4–65.5, 78.

Load check: `load_check.py` on the course gives `LOAD OK`, so every row citation resolves to an anchor the prose cites.

---

## m02-l03

### tabla «Creación o supresión de portales en el ámbito estatal» (l. 122–128)

| # | row (short) | citation | PASS/FAIL | passage / reason | replacement |
|---|---|---|---|---|---|
| 1 | AGE: orden del titular del ministerio o resolución del titular del órgano superior | art. 6.1 RD 203/2021 | PASS | 6.1: «la creación o supresión de portales se llevará a cabo por orden de la persona titular del ministerio correspondiente o por resolución de la persona titular del órgano superior, en el caso de la Administración General del Estado». A verbatim shortening. In prose at l. 112–113. | — |
| 2 | Organismos públicos y entidades de derecho público vinculados o dependientes: resolución del titular de la Presidencia o de la Dirección | art. 6.1 RD 203/2021 | PASS | 6.1: «y por resolución de la persona titular de la Presidencia o de la Dirección en el caso de sus organismos públicos y entidades de derecho público vinculados o dependientes». Verbatim. The prose (l. 113–115) says «sus organismos públicos y entidades de derecho público», which is the same set. | — |
| 3 | Requisito de la creación: informe favorable de la CMAD y posterior comunicación a los dos ministerios | art. 6.1 RD 203/2021 | PASS | 6.1 párr. 2: «La creación requerirá informe favorable de la Comisión Ministerial de Administración Digital respectiva y posterior comunicación al Ministerio de Política Territorial y Función Pública y al Ministerio de Asuntos Económicos y Transformación Digital.» Verbatim. The label limits the row to creation. In prose at l. 117–120. See Notes on the ministry names. | — |

Title: it names the subject, and the two «Supuesto» rows cover both acts. Row 3 is labelled «de la creación», so the
table does not suggest that supresión has the same requirement. PASS.

### tabla «Plazos de la relación electrónica» (l. 183–190)

| # | row (short) | citation | PASS/FAIL | passage / reason | replacement |
|---|---|---|---|---|---|
| 1 | Communication by a persona física no obligada: effects from the quinto día hábil siguiente | art. 3.2 RD 203/2021 | PASS | 3.2: «En ambos casos, los efectos de la comunicación se producirán a partir del quinto día hábil siguiente a aquel en que el órgano competente para tramitar el procedimiento haya tenido constancia de la misma.» Verbatim. The label covers both cases of 3.2 (to relate electronically, «o, en su caso, de dejar de hacerlo»). In prose at l. 40–42. | — |
| 2 | Letra c) system: dos meses desde la comunicación before eficacia jurídica | art. 9.2.c) LPAC | PASS | 9.2.c): «De forma previa a la eficacia jurídica del sistema, habrán de transcurrir dos meses desde dicha comunicación». Verbatim. In prose at l. 58. A table may cite the letter. | — |
| 3 | Informe vinculante de la SES, if the competent organ goes to court during those two months: diez días desde su solicitud | art. 9.2.c) LPAC | PASS | 9.2.c): «…durante los cuales el órgano estatal competente por motivos de seguridad pública podrá acudir a la vía jurisdiccional, previo informe vinculante de la Secretaría de Estado de Seguridad, que deberá emitir en el plazo de diez días desde su solicitud.» The label carries the condition and the organ, and the plazo is verbatim. In prose at l. 59–61. | — |
| 4 | Notificación electrónica obligatoria o elegida: rechazada a los diez días naturales | art. 43.2 LPAC | PASS | 43.2 párr. 2: «Cuando la notificación por medios electrónicos sea de carácter obligatorio, o haya sido expresamente elegida por el interesado, se entenderá rechazada cuando hayan transcurrido diez días naturales desde la puesta a disposición de la notificación sin que se acceda a su contenido.» Verbatim, and both conditions are kept. In prose at l. 176–178. | — |

Title: it does not say «todos los plazos». The lesson's other plazos (RD 1112/2018, l. 147–149) are accessibility
plazos, not plazos of the relación electrónica. Not failed.

### arbol «El PAGe, su sede y las sedes asociadas» (l. 280–286)

| # | node (short) | citation | PASS/FAIL | passage / reason | replacement |
|---|---|---|---|---|---|
| 1 | Punto de Acceso General electrónico (PAGe) (root, label only) | art. 7.3 RD 203/2021 | PASS | 7.3: «El PAGe dispondrá de una sede electrónica…». A label with no fact field. In prose at l. 269. | — |
| 2 | Sede electrónica del PAGe, child of the PAGe: through it, access to all sedes and sedes asociadas | art. 7.3 RD 203/2021 | PASS | 7.3: «El PAGe dispondrá de una sede electrónica, a través de la cual se podrá acceder a todas las sedes electrónicas y sedes asociadas de la Administración Pública correspondiente.» Verbatim. «Dispondrá de» states belonging, so the nesting is supported. In prose at l. 269–270. | — |
| 3 | Dirección Electrónica Habilitada única, child of the PAGe's sede: hosted in the sede of the AGE's PAGe | art. 7.4 RD 203/2021 | PASS | 7.4 párr. 2: «En dicha sede electrónica está alojada la Dirección Electrónica Habilitada única a la que se refiere el artículo 43 de la Ley 39/2015» («dicha» refers to the sede of the PAGe de la Administración General del Estado, 7.4 párr. 1). «Está alojada en» states containment, so the nesting holds. The parent node (7.3) speaks of every Administration's PAGe. The child keeps «de la Administración General del Estado», so it does not read as true of every PAGe. In prose at l. 270–271. | — |
| 4 | Sede electrónica (root, label only) | art. 10.1 RD 203/2021 | PASS | A label. 10.1 names the sede electrónica. On its own the node states nothing. | — |
| 5 | Sede electrónica asociada, child of «Sede electrónica» | art. 10.1 RD 203/2021 | FAIL | 10.1: «Se podrán crear una o varias sedes electrónicas asociadas a una sede electrónica atendiendo a razones técnicas y organizativas. La sede electrónica asociada tendrá consideración de sede electrónica a todos los efectos.» The field is a faithful shortening, but the nesting is not supported. «Asociada a» states a link between two sedes, not that one belongs to, depends on or is part of the other. The same apartado then makes the sede asociada a sede «a todos los efectos», which is a peer and not a part. Arts. 10.2.b) and 10.3 say only that its address «se referenciará» in the address of the sede and speak again of «asociada a». No passage says dependency. An arbol child claims dependency (spec, Rule), so the node reads wider than the article. It also summarises l. 133–134, about 150 lines before the esquema, in another section («Creación de portales y sedes en el ámbito estatal»). | Delete l. 284–285 (the root «Sede electrónica» and its child). The fact stays in the prose at l. 133–134. Retitle the arbol «El PAGe y su sede electrónica»: node 2 still names the sedes asociadas, but only as something reached through the PAGe's sede. Writing node 5 as a single unnested root would fix the dependency but not the placement, so deletion is the fix. |

Nesting of nodes 1–3: supported («dispondrá de», «está alojada»). Node 5: not supported (see row).

---

## m02-l04

### tabla «Acceso, rectificación y oposición» (l. 158–167)

| # | row (short) | citation | PASS/FAIL | passage / reason | replacement |
|---|---|---|---|---|---|
| 1 | Acceso: confirmation and, if so, access to the data and to the information of 15.1 | art. 15.1 RGPD | PASS | 15.1: «El interesado tendrá derecho a obtener del responsable del tratamiento confirmación de si se están tratando o no datos personales que le conciernen y, en tal caso, derecho de acceso a los datos personales y a la siguiente información: a)…». A faithful shortening that keeps «en tal caso». Art. 15 sets no exception to the right in 15.1. Its only limit, 15.4, applies to the copy of 15.3, which the row does not state. The 2021 corrigendum (9) changes only letra c), which the row does not quote. In prose at l. 112–114. | — |
| 2 | Acceso, en la LOPDGDD: repetitivo más de una vez en seis meses, a menos que exista causa legítima | art. 13.3 LOPDGDD | PASS | 13.3: «A los efectos establecidos en el artículo 12.5 del Reglamento (UE) 2016/679 se podrá considerar repetitivo el ejercicio del derecho de acceso en más de una ocasión durante el plazo de seis meses, a menos que exista causa legítima para ello.» It keeps the number, the plazo and the exception «a menos que…». It leaves out the opening «a los efectos del 12.5» (see Notes). In prose at l. 115–117. | — |
| 3 | Rectificación: sin dilación indebida, datos inexactos | art. 16 RGPD | PASS | 16: «El interesado tendrá derecho a obtener sin dilación indebida del responsable del tratamiento la rectificación de los datos personales inexactos que le conciernan.» Verbatim. Art. 16 has no exception. The row leaves out the second sentence (completing incomplete data), which narrows the row and does not widen it. The prose (l. 121–122) leaves it out too. | — |
| 4 | Rectificación, en la LOPDGDD: what the request must indicate and the documentation «cuando sea preciso» | art. 14 LOPDGDD | PASS | 14: «…el afectado deberá indicar en su solicitud a qué datos se refiere y la corrección que haya de realizarse. Deberá acompañar, cuando sea preciso, la documentación justificativa de la inexactitud o carácter incompleto de los datos objeto de tratamiento.» Verbatim. «Cuando sea preciso» is kept. In prose at l. 122–124. | — |
| 5 | Oposición por motivos de su situación particular: 6.1 e) o f); the salvo (motivos legítimos imperiosos / reclamaciones) | art. 21.1 RGPD | PASS | 21.1: «…a oponerse en cualquier momento, por motivos relacionados con su situación particular, a que datos personales que le conciernan sean objeto de un tratamiento basado en lo dispuesto en el artículo 6, apartado 1, letras e) o f) … El responsable del tratamiento dejará de tratar los datos personales, salvo que acredite motivos legítimos imperiosos para el tratamiento que prevalezcan sobre los intereses, los derechos y las libertades del interesado, o para la formulación, el ejercicio o la defensa de reclamaciones.» The condition goes in the label, «en cualquier momento» is kept, and both limbs of the exception are verbatim. The row keeps «sobre los intereses, los derechos y las libertades del interesado», which the prose (l. 148) shortens to «que prevalezcan». Same fact. In prose at l. 146–149. | — |
| 6 | Oposición, mercadotecnia directa: en todo momento | art. 21.2 RGPD | PASS | 21.2: «Cuando el tratamiento de datos personales tenga por objeto la mercadotecnia directa, el interesado tendrá derecho a oponerse en todo momento al tratamiento…». The condition goes in the label. 21.2 has no exception. In prose at l. 149–150. | — |

Title: it names three rights, which is exactly what the table holds. It does not read as the complete list of rights.
PASS. Rows 1–6 drop no exception or limit of their articles.

### tabla «La Presidencia de la Agencia Española de Protección de Datos y su Adjunto» (l. 291–300)

| # | row (short) | citation | PASS/FAIL | passage / reason | replacement |
|---|---|---|---|---|---|
| 1 | Funciones: dirige, representa, dicta resoluciones, circulares y directrices | art. 48.1 LOPDGDD | PASS | 48.1: «La Presidencia de la Agencia Española de Protección de Datos la dirige, ostenta su representación y dicta sus resoluciones, circulares y directrices.» Verbatim. In prose at l. 276–277. | — |
| 2 | Propuesta: nombrados por el Gobierno, a propuesta del Ministerio de Justicia, reconocida competencia profesional | art. 48.3 LOPDGDD | PASS | 48.3 párr. 1: «La Presidencia … y su Adjunto serán nombrados por el Gobierno, a propuesta del Ministerio de Justicia, entre personas de reconocida competencia profesional, en particular en materia de protección de datos.» Verbatim. In prose at l. 279–280. | — |
| 3 | Ratificación: Comisión de Justicia, tres quintos en primera / absoluta en segunda; then votes from at least two groups | art. 48.3 LOPDGDD | PASS | 48.3 párr. 3: «…deberá ser ratificada por la Comisión de Justicia en votación pública por mayoría de tres quintos de sus miembros en primera votación o, de no alcanzarse ésta, por mayoría absoluta en segunda votación, que se realizará inmediatamente después de la primera. En este último supuesto, los votos favorables deberán proceder de Diputados pertenecientes, al menos, a dos grupos parlamentarios diferentes.» Both majorities, the order of the votes and the two-groups requirement are verbatim, and «en este último supuesto» ties that requirement to the second vote only. The row leaves out «en votación pública», «que se realizará inmediatamente después de la primera» and the earlier «tras la celebración de la preceptiva audiencia de los candidatos». The prose (l. 281–283) leaves out the same three. They are requirements of form and timing, not exceptions, and none changes a majority. As in the bloque V precedent (art. 155 LGP, «con cita de los preceptos»), I did not fail the row. See Notes. | — |
| 4 | Nombramiento: Consejo de Ministros mediante real decreto | art. 48.4 LOPDGDD | PASS | 48.4: «La Presidencia y el Adjunto … serán nombrados por el Consejo de Ministros mediante real decreto.» Verbatim. In prose at l. 284. | — |
| 5 | Mandato: cinco años, renovable una vez por igual período | art. 48.5 LOPDGDD | PASS | 48.5: «El mandato … tiene una duración de cinco años y puede ser renovado para otro período de igual duración.» Verbatim. In prose at l. 286. The cese rules of 48.5 párr. 2 are not in the row or the prose. They do not limit the duration rule, so they are not a dropped exception (see Notes). | — |
| 6 | Actos y disposiciones: ponen fin a la vía administrativa; recurribles directamente ante la Sala de lo C-A de la AN | art. 48.6 LOPDGDD | PASS | 48.6: «Los actos y disposiciones dictados por la Presidencia … ponen fin a la vía administrativa, siendo recurribles, directamente, ante la Sala de lo Contencioso-administrativo de la Audiencia Nacional.» Verbatim. In prose at l. 288–289. | — |

Title: it names the organ, not «todo el régimen». The table leaves out 48.2 (the Adjunto's delegation and substitution)
and the cese rules of 48.5, neither of which the prose covers. Not failed.

### tabla «Plazos de respuesta a las solicitudes y reclamaciones» (l. 315–322)

| # | row (short) | citation | PASS/FAIL | passage / reason | replacement |
|---|---|---|---|---|---|
| 1 | Responsable: sin dilación indebida, at most one month; prórroga of two more months; notice of the prórroga within one month, with reasons | art. 12.3 RGPD | PASS | Corrected text (2021 corrigendum, 3): «…facilitará al interesado información relativa a sus actuaciones sobre la base de una solicitud con arreglo a los artículos 15 a 22, sin dilación indebida y, en cualquier caso, en el plazo de un mes a partir de la recepción de la solicitud.» The 2016 text (l. 2711) lacks «sin dilación indebida», and the row and the prose (l. 101–102) both follow the corrected text. The rest of the row is word for word the 2016 text, which no corrigendum changes: «Dicho plazo podrá prorrogarse otros dos meses en caso necesario, teniendo en cuenta la complejidad y el número de solicitudes. El responsable informará al interesado de cualquiera de dichas prórrogas en el plazo de un mes a partir de la recepción de la solicitud, indicando los motivos de la dilación.» Every plazo and condition is kept. The label «ante la solicitud del interesado» stands for «sobre la base de una solicitud con arreglo a los artículos 15 a 22». The prose has the same reference, set under «Ejercicio de los derechos». | — |
| 2 | Delegado, if the afectado goes to him before reclaiming: decision within two months at most | art. 37.1 LOPDGDD | PASS | 37.1: «…el afectado podrá, con carácter previo a la presentación de una reclamación … ante la Agencia … o, en su caso, ante las autoridades autonómicas …, dirigirse al delegado … En este caso, el delegado de protección de datos comunicará al afectado la decisión que se hubiera adoptado en el plazo máximo de dos meses a contar desde la recepción de la reclamación.» The plazo is verbatim and the condition is in the label. «La autoridad de protección de datos» is the prose's own shortening (l. 251). | — |
| 3 | Delegado, when the authority sends him the reclamación: «Responderá en el plazo de un mes» | art. 37.2 LOPDGDD | FAIL | 37.2: «…aquellas podrán remitir la reclamación al delegado de protección de datos a fin de que este responda en el plazo de un mes. Si transcurrido dicho plazo el delegado … no hubiera comunicado … la respuesta …, dicha autoridad continuará el procedimiento…». The article gives the plazo as the purpose of a remisión the authority may make («a fin de que este responda»). The row rewrites it as a flat future duty, «Responderá». That is a reworded fact, and it makes the rule read as a stronger obligation than the article states (the article's consequence of missing the plazo is that the authority carries on). The prose (l. 253–254) keeps the article's wording. | `\| El delegado de protección de datos, cuando la autoridad le remita la reclamación \| La autoridad podrá remitirla al delegado a fin de que este responda en el plazo de un mes \| art. 37.2 LOPDGDD \|` (in prose at l. 252–254) |
| 4 | Agencia: decision on admisión or inadmisión notified within three months | art. 65.5 LOPDGDD | PASS | 65.5: «La decisión sobre la admisión o inadmisión a trámite, así como la que determine, en su caso, la remisión de la reclamación a la autoridad de control principal …, deberá notificarse al reclamante en el plazo de tres meses.» A verbatim shortening. In prose at l. 312–313, which says only «sobre la admisión»; the row's «o inadmisión» is the article's own wording. The silence rule in the next sentence is not in the row or the prose (see Notes). | — |

Title: every plazo of response that the prose states between l. 99 and l. 313 is in the table. Arts. 12.4 RGPD and
65.4 párr. 2 LOPDGDD (a plazo of one month each) are not in the prose either. PASS.

### tabla «Prescripción de las sanciones» (l. 344–350)

| # | row (short) | citation | PASS/FAIL | passage / reason | replacement |
|---|---|---|---|---|---|
| 1 | ≤ 40.000 euros: un año | art. 78.1 LOPDGDD | PASS | 78.1.a): «Las sanciones por importe igual o inferior a 40.000 euros, prescriben en el plazo de un año.» In prose at l. 341. | — |
| 2 | 40.001 to 300.000 euros: dos años | art. 78.1 LOPDGDD | PASS | 78.1.b): «…comprendido entre 40.001 y 300.000 euros prescriben a los dos años.» In prose at l. 341–342. | — |
| 3 | > 300.000 euros: tres años | art. 78.1 LOPDGDD | PASS | 78.1.c): «…por un importe superior a 300.000 euros prescriben a los tres años.» In prose at l. 342. | — |

Title: the rows are the complete 78.1 scale. PASS.

---

## Placement

- m02-l03 tabla «Creación o supresión de portales» (l. 122): directly after the two paragraphs it summarises
  (l. 112–120), before 6.2. PASS.
- m02-l03 tabla «Plazos de la relación electrónica» (l. 183): after every paragraph it summarises (l. 40–42, 58–61,
  176–178). It closes «Las notificaciones electrónicas», the section of its last row. Rows 1–3 summarise paragraphs
  from earlier sections. That is the same spread the bloque V precedent accepted (m05-l03, phases table). PASS.
- m02-l03 arbol (l. 280): nodes 1–3 come after l. 269–271. The Carpeta Ciudadana paragraph (l. 273–278) sits in
  between, and the arbol does not summarise it. Node 5 summarises l. 133–134, in another section about 150 lines
  earlier (part of its FAIL). With node 5 deleted as proposed, PASS.
- m02-l04 tabla «Acceso, rectificación y oposición» (l. 158): after «Acceso» to «Oposición» (l. 110–150). It sits at
  the end of «## Derechos», after «Decisiones individuales automatizadas» (l. 152–156), which it does not summarise.
  It is still the last spot inside the section. PASS.
- m02-l04 tabla Presidencia (l. 291): directly after l. 276–289. PASS.
- m02-l04 tabla «Plazos de respuesta» (l. 315): after l. 101–104, 251–254 and 310–313. It closes «Reclamaciones ante
  la Agencia». PASS.
- m02-l04 tabla «Prescripción de las sanciones» (l. 344): directly after l. 341–342. The prose table on the
  prescription of infracciones (l. 331–335) sits just above it. The esquema does not repeat that table: it covers
  sanctions, not infractions. PASS.

## Notes

- Glossary marks (`gl.py`). The esquemas contain these glossary terms: g-sede-electronica, g-punto-de-acceso-general,
  g-direccion-electronica-habilitada-unica and g-interesado (m02-l03); g-datos-personales, g-interesado and
  g-oposicion (m02-l04). In each case the term's first prose occurrence comes before the esquema, so no first mark
  moves and no new mark appears ahead of the prose one.
- Voice: the labels and titles contain no filler, triad, rhetorical question or coined word. Nothing on the «never
  does» list.
- m02-l03 tabla 1, row 3, and tabla 2: the row quotes art. 6.1 with the ministry names of 2021. The prose (l. 119–120)
  adds «hoy: Ministerio para la Transformación Digital y de la Función Pública» from RD 829/2023, which a
  one-norm row cannot cite. This is the same situation as the m05-l03 note on the Ministro de Economía. Not a FAIL,
  but a reader of the table alone sees the 2021 names.
- m02-l03 tabla 1: under 6.1 párr. 3, supresión requires «la previa comunicación» to the two ministries. Neither the
  table nor the prose states this. The row label keeps the table from implying otherwise. Possible prose gap.
- m02-l03 tabla 2, row 1: under 3.2 the choice is made per procedure («al inicio del procedimiento … en una fase
  posterior del procedimiento»). Neither the row nor the prose (l. 40–42) says so. «El órgano competente para
  tramitar el procedimiento» implies it. Not a FAIL.
- m02-l04 Presidencia row 3: «en votación pública», «que se realizará inmediatamente después de la primera» and
  «tras la celebración de la preceptiva audiencia de los candidatos» (art. 48.3) are missing from both the row and
  the prose at l. 281–283. They could be added to both together. This is the only gap I found in the majorities, and
  it is not a dropped exception.
- m02-l04 Presidencia: the cese rules (48.5 párr. 2) are in neither the table nor the prose. Separation in the
  cases of letras a)–c) needs «la ratificación de la separación por las mayorías parlamentarias previstas en el
  apartado 3». This is a possible prose gap, exam-relevant next to the majorities.
- m02-l04 Acceso table, row 2: art. 13.3 opens with «A los efectos establecidos en el artículo 12.5 del Reglamento».
  The row and the prose (l. 115–117) leave it out. The consequence of «repetitivo» (canon razonable or refusal,
  art. 12.5) is in the prose at l. 106–108, so the row does not mislead.
- m02-l04 «Plazos de respuesta», row 4: the 65.5 silence rule (the reclamación «prosigue» after three months without
  notification) is in neither the row nor the prose. Leaving it out narrows the row and does not widen it.
- m02-l04: the spec's per-subject choice is «derecho, artículo, plazo de respuesta» in one table. The writer split
  it in two: the rights table has no plazo column, and the single art. 12.3 plazo, common to every right, has its
  own table. Supresión, limitación, portabilidad and decisiones automatizadas have no row. The prose on supresión
  says «entre otros casos» and leaves out the 17.3 exceptions, so a supresión row would have needed a clause the
  prose lacks. Their absence is consistent with the rule.

## Counts

31 rows and nodes: 29 PASS, 2 FAIL.

- m02-l03 (12): tabla portales 3/3 PASS; tabla plazos 4/4 PASS; arbol 4 PASS, 1 FAIL (node 5, sede electrónica
  asociada nested under «Sede electrónica»).
- m02-l04 (19): Acceso/rectificación/oposición 6/6 PASS; Presidencia 6/6 PASS; plazos de respuesta 3 PASS, 1 FAIL
  (row 3, art. 37.2 «Responderá»); prescripción 3/3 PASS.

Titles: PASS. Order and nesting: PASS except arbol node 5. Placement: PASS, with arbol node 5 failing as part of its
row.
