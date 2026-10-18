# R2c esquemas, bloque II — blind recheck, 2026-10-18

Second reviewer, blind: no `verify-*.md`, `fixes.md` or scratchpad notes read. Judged against
`../../bloque-i/esquemas/spec.md`, the `::esquema` section of `docs/platform-delta-handoff.md`, the lesson prose and
the norm texts (scratchpad `txt/`, read with `art.py`; RGPD art. 12.3 read with its 2021 corrigendum,
`otros-doue-rgpd-correccion-2021.txt` item 3, which adds «sin dilación indebida»). No lesson or content file edited.

## 1. m02-l03 — arbol «El PAGe y su sede electrónica» (lines 280–284)

Placement: after the «En el RD 203/2021» paragraphs (art. 7.3, 7.4; the Carpeta Ciudadana paragraph, art. 8, sits
between them and the arbol and is not summarised, which is allowed), before «La Orden HAP/1949/2014». Title names
the two nodes it shows and does not claim the PAGe's full content (art. 7.2, 7.4 third paragraph, 7.5 and art. 8 are
not drawn, and the title does not say they are). Fields: 1, 2, 2; « — » separator; citations 7.3 and 7.4 RD 203/2021
are both cited by the prose.

| # | row (short) | citation | PASS/FAIL | passage / reason | replacement |
|---|---|---|---|---|---|
| 1 | Punto de Acceso General electrónico (PAGe) | art. 7.3 RD 203/2021 | PASS | Label only. Art. 7.3 «El PAGe dispondrá de una sede electrónica…» names the PAGe; prose line 270. | — |
| 2 | Sede electrónica del PAGe — a través de ella se podrá acceder a todas las sedes electrónicas y sedes asociadas de la Administración Pública correspondiente (child of 1) | art. 7.3 RD 203/2021 | PASS | Verbatim: «El PAGe dispondrá de una sede electrónica, a través de la cual se podrá acceder a todas las sedes electrónicas y sedes asociadas de la Administración Pública correspondiente». «dispondrá de» supports the dependency. Prose line 270 carries the fact. | — |
| 3 | Dirección Electrónica Habilitada única — alojada en la sede electrónica del PAGe de la Administración General del Estado (child of 2) | art. 7.4 RD 203/2021 | PASS | Art. 7.4: «El PAGe de la Administración General del Estado y su sede electrónica… En dicha sede electrónica está alojada la Dirección Electrónica Habilitada única». «alojada en» supports the dependency; the node itself restricts it to the AGE's sede, so it does not read as hosted in every Administración's PAGe sede. Prose lines 271–272. | — |

## 2. m02-l04 — tabla «Plazos de respuesta a las solicitudes y reclamaciones» (lines 315–322)

Placement: after the last paragraph it summarises (art. 65.5, line 313); the 12.3 and 37 paragraphs (lines 101–104,
251–254) come earlier, so it follows all of them. Title: the table carries every response plazo the prose states
(12.3 RGPD, 37.1, 37.2, 65.5 LOPDGDD); the prose states no other (12.4 RGPD and the 65.4 second-paragraph one month
for the responsable are not in the prose), so the title does not make a selective list read as complete relative to
the lesson. One norm per row.

| # | row (short) | citation | PASS/FAIL | passage / reason | replacement |
|---|---|---|---|---|---|
| 1 | El responsable, sobre sus actuaciones ante la solicitud del interesado — sin dilación indebida y, en cualquier caso, un mes; prórroga de otros dos meses; información de la prórroga en un mes con los motivos | art. 12.3 RGPD | PASS | Verbatim of 12.3 as corrected in 2021: «…sin dilación indebida y, en cualquier caso, en el plazo de un mes a partir de la recepción de la solicitud. Dicho plazo podrá prorrogarse otros dos meses en caso necesario, teniendo en cuenta la complejidad y el número de solicitudes. El responsable informará al interesado de cualquiera de dichas prórrogas en el plazo de un mes…, indicando los motivos de la dilación». Keeps every plazo and condition; the omitted last sentence (medio electrónico) is not a plazo. Prose lines 101–104. | — |
| 2 | El delegado de protección de datos, cuando el afectado se dirija a él antes de reclamar ante la autoridad — dos meses desde la recepción de la reclamación | art. 37.1 LOPDGDD | PASS | Verbatim of 37.1 second paragraph: «comunicará al afectado la decisión que se hubiera adoptado en el plazo máximo de dos meses a contar desde la recepción de la reclamación». The label carries the «con carácter previo a la presentación de una reclamación» condition in the prose's words (line 251); the designación of a delegado is presupposed by the row's subject, as in the prose. | — |
| 3 | El delegado de protección de datos — si la reclamación se presenta ante la autoridad, esta podrá remitirla al delegado a fin de que responda en el plazo de un mes | art. 37.2 LOPDGDD | PASS | Art. 37.2: «Cuando el afectado presente una reclamación ante la Agencia… o, en su caso, ante las autoridades autonómicas…, aquellas podrán remitir la reclamación al delegado de protección de datos a fin de que este responda en el plazo de un mes». The cell is the prose's own faithful shortening, word for word (lines 252–254): keeps the condition (reclamación ante la autoridad), the discretionary «podrá remitirla», the organ and the plazo; not wider. The consequence of silence (the authority continues under Título VIII) is left out by the prose as well and does not widen the plazo. Cosmetic only: the bare label could mirror row 2 («…, cuando la autoridad le remita la reclamación»), not required since the cell carries the condition. | — |
| 4 | La Agencia, sobre la admisión a trámite de la reclamación — tres meses | art. 65.5 LOPDGDD | PASS | Verbatim shortening of 65.5: «La decisión sobre la admisión o inadmisión a trámite… deberá notificarse al reclamante en el plazo de tres meses». The dropped object (remisión a la autoridad de control principal) and the effect of silence narrow, not widen; prose line 312–313 carries the fact. | — |

## 3. m02-l01 — peticiones (LO 4/2001)

| # | check | PASS/FAIL | evidence |
|---|---|---|---|
| 1 | No esquema covers the «Peticiones» section | PASS | The lesson's only esquemas are at lines 210 (tabla, RD 208/1996 arts. 2–3) and 268 (pasos, RD 951/2005 arts. 15–16); «## Peticiones» runs lines 293–341 with none. |
| 2 | `git diff` only adds lines | PASS | `git diff --numstat`: 13 insertions, 0 deletions (two hunks, the two esquemas above). Also 0 deletions for m02-l03 (23) and m02-l04 (39), and no `<` lines against scratchpad `before/`. |
| 3 | Section reads intact | PASS | Lines 293–341 unchanged: intro (art. 4.f) RD 208/1996), «Titulares, destinatarios y objeto» (arts. 1.1, 2, 3), «Forma y presentación» (arts. 4.1, 6.2), «Admisión y contestación» (arts. 7.2, 8, 9.1, 9.2, 11.1), then «## Lo que más cae». |

## Totals

- Esquema 1 (m02-l03 arbol): 3 PASS, 0 FAIL.
- Esquema 2 (m02-l04 tabla): 4 PASS, 0 FAIL.
- Check 3 (m02-l01 peticiones): 3 PASS, 0 FAIL.
- Overall: 10 PASS, 0 FAIL.
