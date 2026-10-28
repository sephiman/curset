# Lesson fixes, m05 (bloque V): writer's record, 2026-10-23

Course `content/age-administrativo-c1`, lessons under `es/lessons/`. Nothing committed. This is the relaunch run: the
stopped run's hunks in m05-l02 and m05-l03 were checked one by one against the norm and are recorded below as items
«from the stopped run». Norm texts are `pdftotext -layout` of the files named in `sources/normativa.yaml`: LGP
`BOE-A-2003-21614_…_2022-12-24`, Resolución de 20-01-2014 `BOE-A-2014-879_…_2014-01-29`, Orden HAC/557/2026
`BOE-A-2026-12037_…_2026-06-05`, RD 2188/1995 `BOE-A-1996-1578_…_2015-02-26`, RD 1009/2023
`BOE-A-2023-24842_…_2026-07-29`, Orden PRE/1576/2002 `BOE-A-2002-12506_…_2026-06-26`, RD 462/2002
`BOE-A-2002-10337_…_2022-12-24`, LCSP `BOE-A-2017-12902_…_2026-04-09`, and the HTML of Ley 31/2022
`BOE-A-2022-22128_pge-2023_2026-09-30.html`. None of them has `cambios_pendientes`. Line numbers are those of the lesson
files after this round. Added words are in bold.

Checks: `uv run pytest tests/test_esquema.py -q` (10 passed) and `uv run pytest tests/test_citations.py -q -k "not
frozen"` (60 passed). Every new or changed citation resolves with `CourseCitations.build(...)._anchor(lesson, citation,
'es')` (list at the end). Goldens not regenerated: `citations.es.txt` will show the moved and added citations.

## m05-l01

### Decision 2d: «de carácter plurianual» (l. 136–140), no change

Lesson: «Los programas presupuestarios, de carácter plurianual y bajo la responsabilidad del titular del centro gestor
del gasto, consisten en el conjunto de gastos …» (art. 35.2 LGP).

Norm (art. 35.2 LGP): «Los programas presupuestarios de carácter plurianual y bajo la responsabilidad del titular del
centro gestor del gasto, consisten en el conjunto de gastos que se considera necesario realizar en el desarrollo de
actividades orientadas a la consecución de determinados objetivos preestablecidos …»

The LGP says it; kept.

### Programas finalistas, art. 6 apartado 1.1 Orden HAC/557/2026 (l. 153–154 and 201), no change

The lesson already states it plainly: «Los programas finalistas son aquellos a los que se puede asignar objetivos
cuantificables e indicadores de ejecución mensurables» (l. 153–154, and the «Lo que más cae» row at l. 201).

Norm (art. 6, apartado 1.1): «Los programas finalistas son aquellos a los que se puede asignar objetivos cuantificables
e indicadores de ejecución mensurables.» Verbatim; nothing to do.

## m05-l02

### Criterion between arts. 62 and 63 (l. 67–75), from the stopped run, corrected (addition)

The stopped run added one paragraph with both articles under a single citation «(anexo IV, arts. 62 y 63, Resolución
de 20-01-2014)» and shortened art. 62's «Administración del Estado, organismos autónomos, agencias estatales y otros
organismos públicos» to «la Administración». Corrected: the entity list restored, and the paragraph split so each
article has its own citation (one article per unit). Final text:

- «El artículo 62 recoge los proyectos de inversión que incrementan el stock de capital público, con la finalidad de
  mejorar cuantitativa o cualitativamente el funcionamiento interno de la Administración del Estado, organismos
  autónomos, agencias estatales y otros organismos públicos (anexo IV, art. 62, Resolución de 20-01-2014).»
- «El 63 recoge los proyectos de inversión destinados al funcionamiento interno de la Administración con la finalidad
  de mantener o reponer los bienes deteriorados, prorrogar la vida útil del bien o ponerlo en un estado de uso que
  aumente su eficacia, o reponer los bienes afectos al servicio que hayan devenido inútiles para su prestación como
  consecuencia de su uso normal (anexo IV, art. 63, Resolución de 20-01-2014).»
- «Al concepto 630 se imputan los mismos gastos que al 620, siempre que se trate de sustitución de los bienes
  existentes por otros análogos (anexo IV, art. 63, Resolución de 20-01-2014).» (kept from the stopped run)

Norm (anexo IV, art. 62): «Recoge aquellos proyectos de inversión que incrementan el stock de capital público, con la
finalidad de mejorar cuantitativa o cualitativamente el funcionamiento interno de la Administración del Estado,
organismos autónomos, agencias estatales y otros organismos públicos.»

Norm (anexo IV, art. 63): «Recoge proyectos de inversión destinados al funcionamiento interno de la Administración, con
la finalidad de: – Mantener o reponer los bienes deteriorados, de forma que puedan seguir siendo utilizados para cumplir
la finalidad a que estaban destinados. – Prorrogar la vida útil del bien o a poner éste en un estado de uso que aumente
la eficacia en la cobertura de las necesidades derivadas de la prestación del servicio. – Reponer los bienes afectos al
servicio, que hayan devenido inútiles para la prestación del mismo como consecuencia de su uso normal.» Concepto 630:
«Se imputan a este concepto los mismos gastos que los indicados para el concepto 620, siempre que se trate de
sustitución de los bienes existentes por otros análogos.»

The anexo IV of the Resolución is the norm that states the criterion; the anexo II of Orden HAC/557/2026 only lists the
codes and names. Normativa (l. 404): «anexo IV, artículos 22 (concepto 221), 62 y 63» (stopped run, kept).

### Retención adicional del 10 % en obras (l. 139–143), from the stopped run, kept (addition)

«En los contratos de obra de carácter plurianual, salvo los realizados bajo la modalidad de abono total del precio, se
efectúa una retención adicional de crédito del 10 por ciento del importe de adjudicación, en el momento en que esta se
realice; se aplica al ejercicio en que finalice el plazo fijado en el contrato para la terminación de la obra o al
siguiente, según el momento en que se prevea realizar el pago de la certificación final, y computa dentro de los
porcentajes anteriores (art. 47.2 LGP).»

Norm (art. 47.2 párr. 2 LGP): «En los contratos de obra de carácter plurianual, con excepción de los realizados bajo la
modalidad de abono total del precio, se efectuará una retención adicional de crédito del 10 por ciento del importe de
adjudicación, en el momento en que ésta se realice. Esta retención se aplicará al ejercicio en que finalice el plazo
fijado en el contrato para la terminación de la obra o al siguiente, según el momento en que se prevea realizar el
pago de la certificación final. Estas retenciones computarán dentro de los porcentajes establecidos en este artículo.»

The lesson's «Gastos plurianuales» section reaches it (it already sets out art. 47.1–3). Faithful; kept.

### Art. 47.4–6 LGP (l. 145–155), from the stopped run, kept (addition)

- «Los compromisos plurianuales se especifican en los escenarios presupuestarios plurianuales y son objeto de
  contabilización separada (art. 47.4 LGP).»
- «No pueden adquirirse compromisos de gasto con cargo a ejercicios futuros cuando se trate de la concesión de
  subvenciones a las que resulte de aplicación el artículo 22.2.a) de la Ley 38/2003, de 17 de noviembre, General de
  Subvenciones (art. 47.5 LGP).»
- «En la tramitación anticipada de expedientes de contratación del artículo 117.2 de la Ley de Contratos del Sector
  Público, de encargos a medios propios y de convenios, puede ultimarse incluso la adjudicación y formalización del
  contrato, la formalización del encargo o la suscripción del convenio, aun cuando su ejecución, en una o en varias
  anualidades, deba iniciarse en ejercicios posteriores (art. 47.6 LGP).»
- «En esa tramitación anticipada, y en la de otros expedientes de gasto cuya normativa reguladora permita llegar a la
  formalización del compromiso de gasto, deben cumplirse los límites y anualidades o importes autorizados de los
  apartados 2 a 5 del artículo 47 (art. 47.6 LGP).»

Norm (art. 47.4): «Los compromisos a que se refiere este artículo se especificarán en los escenarios presupuestarios
plurianuales y deberán ser objeto de contabilización separada.» (47.5): «No podrán adquirirse compromisos de gasto con
cargo a ejercicios futuros cuando se trate de la concesión de subvenciones a las que resulte de aplicación lo dispuesto
en el artículo 22.2.a) de la Ley 38/2003, de 17 de noviembre, General de Subvenciones.» (47.6): «En el caso de la
tramitación anticipada de expedientes de contratación a que se refiere el artículo 117.2 de la Ley de Contratos del
Sector Público, de encargos a medios propios y de convenios, podrá ultimarse incluso con la adjudicación y formalización
del correspondiente contrato, la formalización del encargo o la suscripción del convenio, aun cuando su ejecución, ya sea
en una o en varias anualidades, deba iniciarse en ejercicios posteriores. En la tramitación anticipada de los
expedientes correspondientes a los negocios jurídicos referidos en el párrafo anterior, así como de aquellos otros
expedientes de gasto cuya normativa reguladora permita llegar a la formalización del compromiso de gasto, se deberán
cumplir los límites y anualidades o importes autorizados a que se refieren los apartados 2 a 5 de este artículo.»

Faithful; kept. Normativa (l. 398): «47.1–6» (stopped run, kept).

### Esquema «Estructura de los estados de gastos» (l. 82–84), from the stopped run, kept (correction)

- Root row: «(art. 40.1.a) LGP)» → «(art. 40.1 LGP)»: the three classifications are in the lead-in of 40.1.
- Clasificación orgánica: «(art. 40.1.b) LGP)» → «(art. 40.1.a) LGP)».
- Clasificación por programas: «(art. 40.1.c) LGP)» → «(art. 40.1.b) LGP)».

Norm (art. 40.1 LGP): «Los estados de gastos … se estructurarán de acuerdo con las siguientes clasificaciones: a) La
clasificación orgánica que agrupará por secciones y servicios … b) La clasificación por programas, que permitirá a los
centros gestores agrupar sus créditos conforme a lo señalado en el artículo 35 … c) La clasificación económica …»

### «Ministro de Economía», art. 60.1 LGP (l. 208 and 373), from the stopped run, corrected (correction)

The stopped run wrote, in the «Anticipo de tesorería» row: «Gobierno, a propuesta del Ministro de Economía (hoy:
Ministerio de Economía, Comercio y Empresa) (art. 15.A).1.º RD 1009/2023) (art. 60.1 LGP)». Corrected to the form the
other lessons use (name quoted, one parenthesis for the norm and the «hoy» source) and to a «hoy» that names a person,
as the norm does:

- l. 208, cell: «Gobierno, a propuesta del **«**Ministro de Economía**»** (hoy: titular del Ministerio de Economía,
  Comercio y Empresa) (art. 60.1 LGP; art. 15.A).1.º RD 1009/2023)».
- l. 373: «Con carácter excepcional, el Gobierno, a propuesta del **«**Ministro de Economía**»**, podrá conceder
  anticipos de Tesorería …» (quotes only; the «hoy» sits on the first mention, as convention 1 says).

Norm (art. 60.1 LGP): «Con carácter excepcional, el Gobierno, a propuesta del Ministro de Economía, podrá conceder
anticipos de Tesorería …». RD 1009/2023, art. 15: «El Ministerio de Economía, Comercio y Empresa se estructura en los
siguientes órganos superiores y directivos: A) La Secretaría de Estado de Economía y Apoyo a la Empresa, de la que
dependen … 1.º La Secretaría General del Tesoro y Financiación Internacional, de la que dependen la Dirección General del
Tesoro y Política Financiera …». The Treasury function that art. 60 gives the Ministro sits in that department; RD
829/2023 art. 16 does not name the Tesoro, so the «hoy» source is RD 1009/2023, as in m05-l03. Normativa (l. 407): the
RD 1009/2023 line (stopped run, kept).

### Art. 9.Dos.2–5 Ley 31/2022 (l. 330–333), no change

Lesson: «El artículo 52.1.b) LGP no se aplica a las transferencias del Ministro de Hacienda del artículo 9.Dos.2 a 5
(art. 10.Dos Ley 31/2022).»

Norm (art. 9.Dos): «Durante la vigencia de estos presupuestos, corresponden a la persona titular del Ministerio de
Hacienda y Función Pública las siguientes competencias específicas en materia de modificaciones presupuestarias: … 5.
Autorizar transferencias de crédito entre servicios u Organismos autónomos de distintos Departamento ministeriales,
cuando ello fuere necesario para hacer efectiva la redistribución, reasignación o movilidad de los efectivos de
personal …». Art. 10.Dos: «Las limitaciones contenidas en el artículo 52.1.b) … no serán de aplicación cuando las
transferencias se efectúen en uso de la autorización contenida en los apartados 2, 3, 4 y 5 del artículo 9.Dos de la
presente ley.»

9.Dos.5 belongs to the titular of Hacienda, like 9.Dos.2–4. What belongs to department heads is apartado Cinco of art.
9 (9.Cinco), not 9.Dos.5; the verifier read one for the other. Not an error; no change. (The lesson already gives
Hacienda's current name at l. 309.)

## m05-l03

### Art. 13.2 RD 2188/1995 (l. 226–229), from the stopped run, corrected (addition)

«La Intervención fiscaliza el expediente en el plazo máximo de 10 días contado desde el siguiente a la fecha de
recepción, que se reduce a cinco días, **computados de igual forma,** cuando se haya declarado urgente la tramitación
del expediente o se aplique el régimen especial de fiscalización e intervención previa de los artículos 19 y
siguientes del RD 2188/1995 (art. 13.2 RD 2188/1995).»

Norm (art. 13.2 RD 2188/1995): «La Intervención fiscalizará el expediente en el plazo máximo de 10 días contado desde el
siguiente a la fecha de recepción. Este plazo se reducirá a cinco días computados de igual forma cuando se haya
declarado urgente la tramitación del expediente o se aplique el régimen especial de fiscalización e intervención previa
regulado en los artículos 19 y siguientes de este real decreto.»

The stopped run dropped «computados de igual forma», which fixes the start of the five days; restored. Normativa
(l. 317): «arts. 13.2 y 16.1–2» (stopped run, kept).

### `art. 15.A).1.º RD 1009/2023` citation form (l. 128–130), from the stopped run, corrected (citation form)

At HEAD the citation sat inside the «hoy» parenthesis («(hoy: Ministerio de Economía, Comercio y Empresa, art.
15.A).1.º RD 1009/2023)»), whose «A)» left it unbalanced, and it was split across lines. The stopped run closed the
«hoy» and put the citation on the next line, mid-sentence. Final sentence, in the form of the other lessons:

«Bajo la superior autoridad del Ministro de Economía (hoy: **titular del** Ministerio de Economía, Comercio y Empresa),
competen al Director General del Tesoro y Política Financiera las funciones de Ordenador General de pagos del Estado
(art. 75.1 LGP**; art. 15.A).1.º RD 1009/2023**).»

«titular del» added because the norm names the Ministro, not the Ministerio (same wording as m05-l02, l. 208). Norm
(art. 75.1 LGP): «Bajo la superior autoridad del Ministro de Economía, competen al Director General del Tesoro y Política
Financiera las funciones de Ordenador General de pagos del Estado.» RD 1009/2023 art. 15.A).1.º as quoted under m05-l02.

### «art. 34.1.b) LGP» (l. 69–71), corrected (citation form)

«Al ejercicio presupuestario, que coincide con el año natural, se imputan las obligaciones económicas reconocidas hasta
el fin del mes de diciembre, siempre que correspondan a adquisiciones, obras, servicios, prestaciones o, en general,
gastos realizados dentro del ejercicio y con cargo a los respectivos créditos (art. **34.1** LGP).» (was «art. 34.1.b)
LGP»).

Norm (art. 34.1 LGP): «El ejercicio presupuestario coincidirá con el año natural, y a él se imputarán: … b) Las
obligaciones económicas reconocidas hasta el fin del mes de diciembre, siempre que correspondan a adquisiciones, obras,
servicios, prestaciones o, en general, gastos realizados dentro del ejercicio y con cargo a los respectivos créditos.»

The clause «que coincide con el año natural» is in 34.1's lead-in, not in letter b); 34.1 covers both. Normativa
(l. 309): «arts. 34.1.b)» → «arts. 34.1». A question citing «art. 34.1.b) LGP» still anchors at `…-art-34`.

## m05-l04

### Anexo II RD 462/2002 (l. 104–107), corrected (citation form)

«… publicado por la Resolución de 2 de diciembre de 2005, de la Secretaría de Estado de Hacienda y Presupuestos (**anexo
II RD 462/2002; puntos primero y cuarto del Acuerdo**):» (was «(puntos primero y cuarto del Acuerdo; anexo II RD
462/2002)»).

The parser reads a parenthetical only when it opens with a unit (`art.`, `anexo`, `apartado` …); «puntos …» made it skip
the whole parenthesis, anexo II included. Same two references, reordered; the fact is unchanged. Anexo II of the RD is
«Dietas en territorio nacional» (index of the consolidated text), whose amounts the 2005 Acuerdo revised.

### «Formas de pago», apartado noveno.1 Orden PRE/1576/2002 (l. 316–318), corrected (citation form)

«Las formas de pago de las obligaciones de la Administración General del Estado son la transferencia bancaria, el
cheque nominativo no a la orden en casos excepcionales y los pagos en formalización (**apartado noveno.1 Orden
PRE/1576/2002**; m05-l03).» (was «… son las del apartado noveno.1 de la Orden PRE/1576/2002: transferencia bancaria,
cheque nominativo no a la orden en los casos excepcionales que prevé y pagos en formalización (m05-l03).»)

Norm (apartado noveno.1): «El pago de las obligaciones a cargo de la Administración General del Estado se efectuará
mediante transferencia bancaria … Excepcionalmente, cuando concurran circunstancias que lo justifiquen y sólo para las
personas físicas, el Director General del Tesoro y Política Financiera podrá autorizar el pago mediante cheque nominativo
no a la orden. Asimismo, se podrán cancelar las obligaciones mediante pagos en formalización …»

## m05-l05

### Concepto 630 and «inútiles por su uso normal» (l. 440), corrected (correction)

«Los bienes inventariables necesarios para el funcionamiento operativo de los servicios van al capítulo 6**; la
reposición de bienes que han devenido inútiles por su uso normal, al artículo 63, y la sustitución de los bienes
existentes por otros análogos,** al concepto 630 (anexo IV, capítulo 6 y art. 63, Resolución de 20-01-2014).» (was «…
van al capítulo 6, y la sustitución por otros análogos de bienes que han devenido inútiles por su uso normal, al
concepto 630 …»).

Norm: anexo IV, art. 63 and concepto 630, quoted under m05-l02. «Inútiles por su uso normal» is one of art. 63's three
purposes; concepto 630's only condition is substitution by analogous goods. The worked example at l. 100–103 already
keeps them apart.

## m05-l06

### DA 12.ª LCSP (l. 69–70), corrected (correction)

«Los días son naturales**, y si el último día del plazo es inhábil, se prorroga al primer día hábil siguiente**
(disposición adicional duodécima LCSP). **En este ejemplo** ningún vencimiento cae en sábado ni domingo.» (was «Los días
son naturales y ningún vencimiento cae en sábado ni domingo (disposición adicional duodécima LCSP).»)

Norm (DA 12.ª LCSP): «Los plazos establecidos por días en esta Ley se entenderán referidos a días naturales, salvo que en
la misma se indique expresamente que solo deben computarse los días hábiles. No obstante, si el último día del plazo
fuera inhábil, este se entenderá prorrogado al primer día hábil siguiente.»

The example's dates (2027-06-02 Wednesday, 2027-06-17 Thursday) were checked; the last sentence now states that as a
fact of the example, not of the DA.

## Resolver check

Each resolves in its lesson: m05-l02 `anexo IV, art. 62/63, Resolución de 20-01-2014` → `boe-a-2014-879-anexo-iv`;
`art. 47.2/47.4/47.5/47.6 LGP` → `…-art-47`; `art. 40.1`, `40.1.a)`, `40.1.b) LGP` → `…-art-40`; `art. 60.1 LGP` →
`…-art-60`; `art. 15.A).1.º RD 1009/2023` → `boe-a-2023-24842-art-15`. m05-l03 `art. 34.1 LGP` → `…-art-34`;
`art. 75.1 LGP` → `…-art-75`; `art. 15.A).1.º RD 1009/2023` → `…-art-15`; `art. 13.2 RD 2188/1995` →
`boe-a-1996-1578-art-13`. m05-l04 `anexo II RD 462/2002` → `boe-a-2002-10337-anexo-ii` (was None);
`apartado noveno.1 Orden PRE/1576/2002` → `boe-a-2002-12506-apartado-noveno` (was None). m05-l05 `anexo IV, art. 63,
Resolución de 20-01-2014` → `…-anexo-iv`. m05-l06 `disposición adicional duodécima LCSP` → `boe-a-2017-12902-da-duodecima`.

## Not done

- m05-l01 «de carácter plurianual»: art. 35.2 LGP says it; kept.
- m05-l01 programas finalistas: already stated in the norm's words; nothing to add.
- m05-l02 art. 9.Dos.5 Ley 31/2022: not an error (9.Dos.5 is Hacienda's; department heads hold 9.Cinco).

Noticed, outside the item list, not changed: m05-l04 l. 312 «(apartado séptimo.1.1 y 2.a) Orden PRE/1576/2002)» has a
sub-unit «2.a)» with no apartado name before it; it resolves to `…-apartado-septimo`.
