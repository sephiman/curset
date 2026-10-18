# Verification — esquemas of m02-l01 and m02-l02 (2026-10-18)

I am a blind reviewer: I wrote neither these esquemas nor the lessons, and I did not read the writer's notes. Scope:
the three `:::esquema` blocks of `C/es/lessons/m02-l01.md` and the three of `C/es/lessons/m02-l02.md`. Rules:
`../../bloque-i/esquemas/spec.md` (bloque II uses it) and the `::esquema` section of `docs/platform-delta-handoff.md`.
Format: `../../bloque-v/esquemas/verify-m05-l03.md`.

Diff: `git diff -U0` shows 18 added lines and 0 deleted lines in m02-l01, and 26 added and 0 deleted in m02-l02. The
esquema blocks are the only additions and no prose line changed. Line numbers are those of the current files.

Sources (scratchpad `txt/`, read with `art.py` or `sed`; nothing taken from memory):

- `BOE-A-1996-4997_rd-208-1996-informacion-administrativa_2011-06-04.txt`: arts. 2, 3.
- `BOE-A-2005-14836_rd-951-2005-calidad_2009-06-30.txt`: arts. 14, 15, 16, 17.
- `BOE-A-2001-21090_lo-derecho-peticion_2011-07-28.txt`: arts. 6, 7, 9, 10, 11.
- `BOE-A-2015-10565_lpac_2024-11-06.txt`: art. 16.1–16.6.
- `BOE-A-2021-5032_rd-203-2021-medios-electronicos_2025-04-02.txt`: art. 53.
- `BOE-A-2011-18541_rd-1708-2011-archivos_2024-03-27.txt`: arts. 8, 9, 10, 11, 12.

Load check: `load_check.py` on `content/age-administrativo-c1` gives `LOAD OK`, so every row citation resolves to an
anchor the prose cites, «art. 15.2 y 15.4 RD 951/2005» and the «art. 2.1–2» / «art. 16.1–2» / «art. 12.1–2» ranges
included.

Glossary marks: the terms that appear inside the esquemas (`g-unidades-administrativas`, `g-interesado`,
`g-registro-electronico-general`, `g-archivo-intermedio`) all have an earlier occurrence in the prose of the same
lesson (m02-l01 l. 192, 203; m02-l02 l. 48, 91, 198, 203–204). So no first mark can move into an esquema, and
`glossary-links.es.txt` and `lesson-refs.es.txt` are unchanged in the working tree. I did not regenerate them.

---

## m02-l01

### tabla «Información general e información particular sobre los procedimientos» (l. 210–215)

| # | row (short) | citation | PASS/FAIL | passage / reason | replacement |
|---|---|---|---|---|---|
| 1 | General: definition list; se facilitará obligatoriamente, sin acreditación de legitimación | art. 2.1–2 RD 208/1996 | PASS | 2.1: «Es la información administrativa relativa a la identificación, fines, competencia, estructura, funcionamiento y localización de organismos y unidades administrativas; la referida a los requisitos jurídicos o técnicos que las disposiciones impongan a los proyectos, actuaciones o solicitudes que los ciudadanos se propongan realizar; la referente a la tramitación de procedimientos, a los servicios públicos y prestaciones, así como a cualesquiera otros datos que aquellos tengan necesidad de conocer en sus relaciones con las Administraciones públicas…». 2.2: «La información general se facilitará obligatoriamente a los ciudadanos, sin exigir para ello la acreditación de legitimación alguna.» Both cells are verbatim. The cut catch-all «así como a cualesquiera otros datos…» narrows the definition. It does not widen it, and the prose (l. 191–194) leaves it out too. See Notes. In prose at l. 191–197. | — |
| 2 | Particular sobre los procedimientos en tramitación: estado o contenido; identificación de autoridades y personal; sólo interesados o representantes legales | art. 3.1 RD 208/1996 | PASS | 3.1: «Es la concerniente al estado o contenido de los procedimientos en tramitación, y a la identificación de las autoridades y personal al servicio de la Administración General del Estado y de las entidades de derecho público vinculadas o dependientes de la misma bajo cuya responsabilidad se tramiten aquellos procedimientos. Esta información sólo podrá ser facilitada a las personas que tengan la condición de interesados en cada procedimiento o a sus representantes legales de acuerdo con lo dispuesto en los artículos 31 y 32 de a Ley 30/1992». A faithful shortening, the same words as the prose at l. 201–204. The label «sobre los procedimientos en tramitación» keeps out 3.2 (personal data), which the row does not cover. | — |

Title: it names the two kinds of art. 1 RD 208/1996 («Podrá ser general o particular», prose l. 186–187). Adding
«sobre los procedimientos» to the particular kind shows that 3.2 is left out. PASS.

### pasos «Presentación y contestación de las quejas y sugerencias» (l. 268–272)

| # | step (short) | citation | PASS/FAIL | passage / reason | replacement |
|---|---|---|---|---|---|
| 1 | Presentación — presencial, postal, telemática; firma electrónica for email/Internet; constancia through the chosen medium — los usuarios | art. 15.2 y 15.4 RD 951/2005 | PASS | 15.2: «Los usuarios podrán formular sus quejas o sugerencias presencialmente, por correo postal y por medios telemáticos. Las quejas y sugerencias presentadas por correo electrónico o a través de Internet deberán estar suscritas con la firma electrónica del interesado.» 15.4: «Formuladas las quejas y sugerencias de los modos señalados en los apartados anteriores, los usuarios recibirán constancia de su presentación a través del medio que indiquen.» Verbatim. In prose at l. 248–253. The third field («organ» role) holds the actor and not an organ. See Notes. | — |
| 2 | Contestación, recibida la queja — informará de las actuaciones en 20 días hábiles; suspension if aclaraciones are required in 10 días hábiles — la unidad responsable de la gestión de las quejas y sugerencias | art. 16.1–2 RD 951/2005 | PASS | 16.1: «Recibida la queja o sugerencia, la unidad a la que se refiere el artículo 14 informará al interesado de las actuaciones realizadas en el plazo de 20 días hábiles.» 16.2: «El transcurso de dicho plazo se podrá suspender en el caso de que deba requerirse al interesado para que, en un plazo de 10 días hábiles, formule las aclaraciones necesarias para la correcta tramitación de la queja o sugerencia.» Verbatim. The organ: art. 14 names «la unidad responsable de la gestión de las quejas y sugerencias», and the prose names it the same way at l. 244 and l. 257. Both plazos keep «hábiles», and the suspension keeps «se podrá». In prose at l. 257–261. | — |
| 3 | Falta de contestación, si transcurrido el plazo no hubiera respuesta — dirigirse a la IGS del departamento; la Inspección propondrá, en su caso, medidas — la Inspección General de Servicios del departamento correspondiente | art. 16.3 RD 951/2005 | PASS | 16.3: «Si, transcurrido el plazo establecido, no hubiera obtenido ninguna respuesta de la Administración, el ciudadano podrá dirigirse a la Inspección General de Servicios del departamento correspondiente para conocer los motivos de la falta de contestación y para que dicha Inspección proponga, en su caso, a los órganos competentes la adopción de las medidas oportunas.» A faithful shortening, the same as the prose at l. 263–266. It keeps «podrá» and «en su caso». The organ is the one the citizen goes to, which matches the handoff's «órgano» role. | — |

Order. 1 → 2 is supported: 16.1 opens «Recibida la queja o sugerencia», and the receipt is the presentation of step 1.
Inside step 1, the constancia comes after the formulation («Formuladas…», 15.4). 2 → 3 is supported: 16.3 «Si,
transcurrido el plazo establecido, no hubiera obtenido ninguna respuesta», where the plazo is the one in step 2.
Step 3 is conditional, and its label says «si…», so the stepper does not claim that it always happens. Every
step's order is stated by the norm. PASS.

Title: «Presentación y contestación» matches the headings of arts. 15 and 16. The Inspección's follow-up (art. 17)
and effects (art. 19) are not steps of a single queja, and the title does not claim them. PASS.

### plazos «Plazos de la admisión y la contestación de las peticiones» (l. 342–345)

| # | row (short) | citation | PASS/FAIL | passage / reason | replacement |
|---|---|---|---|---|---|
| 1 | Declaración de inadmisibilidad, siempre motivada — 45 días hábiles siguientes al de presentación; en otro caso, admitida a trámite | art. 9.1–2 LO 4/2001 | FAIL | 9.1: «La declaración de inadmisibilidad será siempre motivada y deberá acordarse y notificarse al peticionario en los cuarenta y cinco días hábiles siguientes al de presentación del escrito de petición.» 9.2: «En otro caso, se entenderá que la petición ha sido admitida a trámite.» The row is a verbatim shortening of art. 9. It still reads wider than the law. 10.1: «Siempre que la declaración de inadmisibilidad de una petición se base en la falta de competencia de su destinatario, éste la remitirá a la institución, administración u organismo que estime competente en el plazo de diez días y lo comunicará así al peticionario. En este caso, los plazos se computarán desde la recepción del escrito, aplicándose lo dispuesto en el artículo 6.2.» When a petición is remitted, the competent body's plazos run from its receipt of the escrito, not from the presentation. The first destinatario's 45 days are not affected. The row states the dies a quo with no condition. The prose has the same gap: neither l. 334–336 nor any other line of the lesson mentions art. 10. «Normativa» (l. 367) lists «arts. 1–4, 6–9 y 11». | Needs a clause the prose lacks (art. 10.1 LO 4/2001). Remove the row and list the prose gap. |
| 2 | Contestación, una vez admitida — contestar y notificar en el plazo máximo de tres meses desde la fecha de su presentación | art. 11.1 LO 4/2001 | FAIL | 11.1: «Una vez admitida a trámite una petición, la autoridad u órgano competente vendrán obligados a contestar y a notificar la contestación en el plazo máximo de tres meses a contar desde la fecha de su presentación.» Verbatim, and the same as the prose at l. 338–340. But art. 10.1 («En este caso, los plazos se computarán desde la recepción del escrito») moves the dies a quo for every petición that was remitted for lack of competence. The row says «desde la fecha de su presentación» with no condition, so it reads wider than the law. The prose has the same gap. | Needs a clause the prose lacks (art. 10.1 LO 4/2001). Remove the row and list the prose gap. |

Order. 1 → 2: row 2's label «una vez admitida a trámite la petición» and 9.2 («En otro caso, se entenderá que la
petición ha sido admitida a trámite») support the sequence. Inadmisión and contestación are alternatives, and each
label carries its condition, so the order on its own is not false. PASS. The rows fail on content.

Title: FAIL. «Plazos de la admisión y la contestación» reads as the complete set of plazos for those phases. The
admission phase also has the subsanación plazo, «se requerirá al peticionario para que subsane los defectos en el
plazo de quince días» (art. 7.2 LO 4/2001, prose l. 324–326, in the same «Admisión y contestación» subsection). Art.
7.1 places the subsanación inside the admission decision: «Como resultado de tal apreciación deberá declararse su
inadmisión o tramitarse la petición». The acuse de recibo in diez días (art. 6.2, prose l. 319–320) and the remisión
in diez días (art. 10.1, not in the prose) are left out as well. If the esquema is rebuilt after the prose gets
art. 10.1, either the title is narrowed («Inadmisibilidad y contestación de las peticiones») or the 7.2 row is added.

Result: neither row can stay without a clause the prose lacks. The esquema should be removed until the prose states
art. 10.1 LO 4/2001.

---

## m02-l02

### tabla «El asiento en el registro» (l. 96–103)

| # | row (short) | citation | PASS/FAIL | passage / reason | replacement |
|---|---|---|---|---|---|
| 1 | Qué se asienta en el REG de cada Administración: todo documento presentado o recibido…; también se podrá anotar la salida | art. 16.1 LPAC | PASS | 16.1: «Cada Administración dispondrá de un Registro Electrónico General, en el que se hará el correspondiente asiento de todo documento que sea presentado o que se reciba en cualquier órgano administrativo, Organismo público o Entidad vinculado o dependiente a éstos. También se podrán anotar en el mismo, la salida de los documentos oficiales dirigidos a otros órganos o particulares.» Verbatim, and it keeps «podrán». In prose at l. 48–51. | — |
| 2 | Orden y fecha | art. 16.2 LPAC | PASS | 16.2: «Los asientos se anotarán respetando el orden temporal de recepción o salida de los documentos, e indicarán la fecha del día en que se produzcan.» Verbatim. In prose at l. 87–88. | — |
| 3 | Contenido del asiento | art. 16.3 LPAC | PASS | 16.3: «…garantizará la constancia, en cada asiento que se practique, de un número, epígrafe expresivo de su naturaleza, fecha y hora de su presentación, identificación del interesado, órgano administrativo remitente, si procede, y persona u órgano administrativo al que se envía, y, en su caso, referencia al contenido del documento que se registra.» Verbatim, and it keeps «si procede» and «en su caso». In prose at l. 90–92. | — |
| 4 | Recibo: automático, copia autenticada, fecha y hora, número de entrada | art. 16.3 LPAC | PASS | 16.3: «…se emitirá automáticamente un recibo consistente en una copia autenticada del documento de que se trate, incluyendo la fecha y hora de presentación y el número de entrada de registro, así como un recibo acreditativo de otros documentos que, en su caso, lo acompañen…». A faithful shortening, the same as the prose at l. 92–94. Leaving out the second recibo narrows the row and does not widen it. The prose leaves it out too (see Notes). | — |

Title: it names the subject and does not claim to cover all of art. 16. PASS.

### tabla «Documentos presentados en papel» (l. 139–145)

| # | row (short) | citation | PASS/FAIL | passage / reason | replacement |
|---|---|---|---|---|---|
| 1 | Digitalización por la oficina de asistencia en materia de registros, para el expediente electrónico | art. 16.5 LPAC | PASS | 16.5: «Los documentos presentados de manera presencial ante las Administraciones Públicas, deberán ser digitalizados, de acuerdo con lo previsto en el artículo 27 y demás normativa aplicable, por la oficina de asistencia en materia de registros en la que hayan sido presentados para su incorporación al expediente administrativo electrónico». A faithful shortening, the same as the prose at l. 129–130. The cut is a cross-reference and not a condition. | — |
| 2 | Devolución de los originales, salvo custodia o soporte específico no digitalizable | art. 16.5 LPAC | PASS | 16.5: «…devolviéndose los originales al interesado, sin perjuicio de aquellos supuestos en que la norma determine la custodia por la Administración de los documentos presentados o resulte obligatoria la presentación de objetos o de documentos en un soporte específico no susceptibles de digitalización.» A faithful shortening that keeps both exceptions. It is the same as the prose at l. 131–133. | — |
| 3 | Conservación, si no se puede devolver: seis meses, salvo plazo mayor reglamentario | art. 53.1 RD 203/2021 | PASS | 53.1: «Los documentos presentados por el interesado en soporte papel que por cualquier circunstancia no le puedan ser devueltos en el momento de su presentación, una vez digitalizados serán conservados a su disposición durante seis meses para que pueda recogerlos, independientemente del procedimiento administrativo al que se incorporen o de la Administración Pública a que vayan dirigidos, salvo que reglamentariamente la Administración correspondiente establezca un plazo mayor.» A faithful shortening. The label carries the condition, and the row keeps the plazo and the «salvo». It is the same as the prose at l. 135–137. One norm per row. | — |

Title: «en papel» scopes out 53.2 (electronic documents in a device). PASS.

### tabla «Clases de archivo según el ciclo vital de los documentos» (l. 258–265)

| # | row (short) | citation | PASS/FAIL | passage / reason | replacement |
|---|---|---|---|---|---|
| 1 | Oficina o gestión, in every órgano and unidad: documents in tramitación or continuous use — transfer to the archivo central, per the plazos of the valoración | art. 9 RD 1708/2011 | PASS | 9 párr. 1: «Son aquellos archivos existentes en todos los órganos y unidades administrativas para la custodia de los documentos en fase de tramitación o sometidos a continua utilización y consulta administrativa. Estos documentos, una vez concluida su tramitación o su etapa de utilización y consulta, serán objeto de transferencia al archivo central del Departamento respectivo, de acuerdo con los plazos establecidos durante el proceso de valoración.» The transfer cell is a faithful shortening, the same words as the prose at l. 205–207 («se transfieren»). It names no plazo. «De acuerdo con los plazos establecidos durante el proceso de valoración» is the norm's own reference. | — |
| 2 | Generales o centrales, in Ministerios and organismos públicos: after tramitación and plazos — transferencias preceptivas y periódicas al intermedio, con relación de entrega | art. 10.1 RD 1708/2011 | PASS | 10.1: «Son aquellos archivos existentes en los Ministerios y organismos públicos para la custodia de los documentos, una vez finalizada su tramitación y transcurridos los plazos establecidos por la normativa vigente o en los calendarios de conservación.» 10.1.6.º: «Realizar las transferencias preceptivas y periódicas de documentos al archivo intermedio, acompañadas de su correspondiente relación de entrega.» Both are verbatim. «Periódicas» is the norm's word, and no frequency is stated or implied. In prose at l. 221–227, which cites «art. 10.1.2.º y 6.º», the same anchor. | — |
| 3 | Archivo intermedio; in the AGE, the AGA: documents after their fase activa — conservar los transferidos desde los Archivos Centrales | art. 11 RD 1708/2011 | PASS | 11: «El archivo intermedio es la institución responsable de la custodia de los documentos generados y reunidos por los diferentes Departamentos ministeriales y sus organismos públicos, una vez finalizada su fase activa conforme a lo establecido en los calendarios de conservación. El Archivo General de la Administración, es el archivo intermedio de la Administración General del Estado…» Función 1.º: «Conservar los documentos que son transferidos desde los Archivos Centrales de los Ministerios.» Verbatim. In prose at l. 231–237. The transfer cell names no plazo. | — |
| 4 | Archivos históricos; in the AGE, the AHN: fondos del patrimonio histórico documental… — conservar los documentos con valor histórico transferidos desde el AGA | art. 12.1–2 RD 1708/2011 | PASS | 12.1: «…instituciones responsables de la custodia, conservación y tratamiento de los fondos pertenecientes al patrimonio histórico documental español que sean reflejo de la trayectoria de la administración estatal a lo largo de la historia o que en todo caso resulten altamente significativos por su valor histórico, su singular importancia o su proyección internacional.» 12.2: «El Archivo Histórico Nacional ejerce las funciones de archivo histórico de la Administración General del Estado.» 12.2.a): «Conservar los documentos con valor histórico que le son transferidos desde el Archivo General de la Administración.» Verbatim, and it keeps «con valor histórico». In prose at l. 244–252. | — |

Transfer cells, as the brief asked: every one is verbatim or the prose's own faithful shortening. None states or
implies a plazo that neither the norm nor the prose states. The only time references are the norm's own:
«plazos establecidos durante el proceso de valoración», «periódicas», «calendarios de conservación». Read across,
the chain gestión → central → intermedio → histórico is the one arts. 9, 10.1.6.º, 11.1.º and 12.2.a) state.
Row 4 keeps the filter «con valor histórico», so the table does not say that everything reaches the AHN.

Title: the four rows are the complete list of art. 8 («atendiendo al ciclo vital de los documentos, se clasifican
en: a)…d)»). PASS.

---

## Placement

- m02-l01 tabla (l. 210): it follows «Información general» and «Información particular» (l. 189–208), which it
  summarises, and comes before «Iniciativas». PASS.
- m02-l01 pasos (l. 268): it follows «Presentación» and «Contestación» (l. 242–266) and comes before «Las
  Inspecciones Generales de Servicios». PASS.
- m02-l01 plazos (l. 342): it follows «Admisión y contestación» (l. 322–340). Its place is right, but the esquema
  should be removed (see above).
- m02-l02 «El asiento en el registro» (l. 96): it follows «Los asientos» (l. 87–94). Its row 1 summarises
  «Concepto de registro» (l. 48–51), which comes earlier, so the esquema still follows everything it summarises.
  PASS.
- m02-l02 «Documentos presentados en papel» (l. 139): it follows «Documentos en papel» (l. 129–137). PASS.
- m02-l02 archive table (l. 258): it follows «Clases de archivo» and the four subsections (l. 191–256), and comes
  before «Criterios de ordenación». The prose list at l. 196–199 holds the class names only. The table adds custody
  and transfers, so it does not repeat a list the prose already has. PASS.

## Notes

- m02-l01 tabla row 1: art. 2.1 ends with the catch-all «así como a cualesquiera otros datos que aquellos tengan
  necesidad de conocer en sus relaciones con las Administraciones públicas, en su conjunto, o con alguno de sus
  ámbitos de actuación». The row and the prose (l. 191–194) both leave it out. The cell keeps the article's
  semicolon list, so it looks like the full definition. This narrows the row and does not widen it, so following
  the bloque V precedent I did not fail it. It is a prose gap worth closing: exam questions quote art. 2.1 as
  written. Once the prose has it, the cell can end «…a los servicios públicos y prestaciones, así como a
  cualesquiera otros datos que aquellos tengan necesidad de conocer en sus relaciones con las Administraciones
  públicas».
- m02-l01 tabla row 2: «personal al servicio de la Administración General del Estado y de las entidades de derecho
  público vinculadas o dependientes de la misma» is cut to «personal», in the row and in the prose alike. The RD
  only covers the AGE, so the cut has no effect.
- m02-l01 pasos step 1: the third field (the «organ» role, `esquema.py`: paso — documento — órgano) is «los
  usuarios», who are the actor and not an organ. Steps 2 and 3 name organs. On screen the column has no header,
  and the fact is correct, so I did not fail it. If the writer wants the role to hold an organ, «la unidad
  responsable de la gestión de las quejas y sugerencias» is supported by art. 14 («con objeto de recoger y tramitar»)
  and by the prose at l. 224–225 and l. 244.
- m02-l01 pasos: art. 15.3 (the formulario for presencial quejas and help from staff) is missing from the step and
  from the prose. The omission narrows the step.
- m02-l01 plazos row 1: art. 9.1 párr. 2 is missing from the row and from the prose: when the inadmisión comes from
  another specific procedure, the declaration «deberá indicar expresamente las disposiciones a cuyo amparo deba
  sustanciarse, así como el órgano competente para ella». This is a content requirement, not a plazo condition.
  Add it to the prose together with art. 10.1.
- Prose gap to list (m02-l01, l. 334–340): art. 10.1 LO 4/2001 (remisión al competente within diez días, with notice
  to the peticionario; then «los plazos se computarán desde la recepción del escrito»). Art. 10.2 (direct remission
  inside the same institución) is missing as well. The lesson's «Normativa» line would then read «arts. 1–4, 6–11».
- m02-l02 tabla «El asiento» row 4 and the prose leave out the second recibo of 16.3 («así como un recibo
  acreditativo de otros documentos que, en su caso, lo acompañen, que garantice la integridad y el no repudio»).
  The omission narrows the row.
- m02-l02 the two registro tables (l. 96, l. 139) repeat the paragraphs just above them almost word for word, split
  into rows. They break no rule, but they add little apart from scanning.
- m02-l02 archive table rows 3–4: under art. 12.2 (the second apartado numbered 2), the Archivos Históricos
  Provinciales perform «idénticas funciones a las de los archivos intermedio e histórico» in the servicios
  periféricos. The prose states this at l. 254–256, and the table does not. The labels quote arts. 11 and 12.2
  verbatim («en la Administración General del Estado, el …») and do not say «only», so I did not fail them. A label
  addition such as «…; en los servicios periféricos, los Archivos Históricos Provinciales (art. 12.2)» is possible
  without new prose, but it would need a two-apartado citation (for example «arts. 11 y 12.2 RD 1708/2011»).
- Voice: no esquema title or label uses anything from the voice page's «never does» list.

## Counts

18 rows: 16 PASS, 2 FAIL (m02-l01 plazos rows 1 and 2). Titles: 5 PASS, 1 FAIL (m02-l01 plazos). Order: PASS for the
pasos and the plazos. Placement: PASS for all six. The m02-l01 plazos esquema should be removed until the prose
states art. 10.1 LO 4/2001.
