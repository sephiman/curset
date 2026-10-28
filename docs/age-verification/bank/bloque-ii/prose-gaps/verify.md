# Prose gaps of «Esquemas bloque II» (open item 1): blind verification, 2026-10-19

Reviewer did not write the change. Scope: `git diff -- content/age-administrativo-c1/es/lessons/` for m02-l01, m02-l02,
m02-l03 and m02-l04: the prose sentences that close the gaps of «Esquemas bloque II (R2c, 2026-10-18)», «Open items»
item 1, the esquema rows and titles they restore or change, and the rewrite of bare `sources/otros/<file>` citations to
«(fuente: `<file>`; <label>)». Norm texts: `pdftotext -layout` of the files named in `sources/normativa.yaml` (RD 208/1996
`BOE-A-1996-4997_…_2011-06-04`, LO 4/2001 `BOE-A-2001-21090_…_2011-07-28`, Ley 16/1985 `BOE-A-1985-12534_…_2026-10-03`
(its pending change, Ley 4/2026, only adds DA 12 and does not touch art. 49), LPAC `BOE-A-2015-10565_…_2024-11-06`,
RD 203/2021 `BOE-A-2021-5032_…_2025-04-02`, RD 1112/2018 `BOE-A-2018-12699_…_2019-08-12`, RD 127/2015
`BOE-A-2015-2671_…_2015-03-13`, RGPD `CELEX-32016R0679_…_2016-05-04` with the 2018 and 2021 corrigenda in `sources/otros/`
(neither touches arts. 15.3–4, 17, 20 or 22), LOPDGDD `BOE-A-2018-16673_…_2025-12-27`). The source rewrites were checked
against `sources/otros/` and `sources/otros/fuentes.yaml`. Every changed citation was run through the backend's own
parser (`tradeschool.citations`: `scan_lesson` and the esquema cross-check) from a scratch script. All parse, all
resolve to the intended norm and article, and the esquema check reports no problem in the four lessons. Line numbers
are those of the lesson files after the change. Judgments were made before reading `writer.md`; it was read afterwards
only to confirm every item is covered. pytest not run and goldens not touched (per instruction).

Totals: **65 items, 61 PASS, 4 FAIL.**

| # | Lesson | Line | Item | Result | Reason (norm quoted) |
|---|---|---|---|---|---|
| 1 | m02-l01 | 192–196 | Prose: catch-all of art. 2.1 RD 208/1996 | PASS | «la referente a la tramitación de procedimientos, a los servicios públicos y prestaciones, así como a cualesquiera otros datos que aquellos tengan necesidad de conocer en sus relaciones con las Administraciones públicas, en su conjunto, o con alguno de sus ámbitos de actuación». «aquellos» is spelt out as «los ciudadanos» |
| 2 | m02-l01 | 208–212 | Prose: «con las limitaciones y en los términos establecidos en la Ley Orgánica 5/1992 … y en el artículo 37 de la Ley 30/1992», art. 3.2 RD 208/1996 | PASS | Verbatim: «estará reservada a las personas a que se refieran con las limitaciones y en los términos establecidos en la Ley Orgánica 5/1992, de 29 de octubre, … y en el artículo 37 de la Ley 30/1992, de 26 de noviembre». See note 1 |
| 3 | m02-l01 | 217 | Row «General», art. 2.1–2 RD 208/1996 | PASS | Cell verbatim 2.1, including the catch-all; singular `art.` with a sub-range of one article parses (article 2) |
| 4 | m02-l01 | 339–342 | Prose: art. 9.1 párrafo 2 LO 4/2001 (inadmission because other procedures exist) | **FAIL** | The sentence is faithful to the norm («Cuando la inadmisión traiga causa de la existencia en el ordenamiento jurídico de otros procedimientos específicos …, la declaración de inadmisión deberá indicar expresamente las disposiciones a cuyo amparo deba sustanciarse, así como el órgano competente para ella»). Its placement is not. It now sits between the 45-day sentence and «En otro caso, se entenderá que la petición ha sido admitida a trámite (art. 9.2)». In the norm, «2. En otro caso» answers the whole of apartado 1, the apartado break marking it. In the prose it reads as «when the inadmission is not caused by other procedures, the petition is deemed admitted». That reworded fact is wrong. Replacement below |
| 5 | m02-l01 | 345–347 | Prose: remission for lack of competence, art. 10.1 LO 4/2001 | PASS | «Siempre que la declaración de inadmisibilidad de una petición se base en la falta de competencia de su destinatario, éste la remitirá a la institución, administración u organismo que estime competente en el plazo de diez días y lo comunicará así al peticionario» |
| 6 | m02-l01 | 347–348 | Prose: «los plazos se computarán desde la recepción del escrito, aplicándose lo dispuesto en el artículo 6.2», art. 10.1 LO 4/2001 | PASS | Verbatim. Art. 6.2 (acuse de recibo) is stated in the prose at l. 322–324 |
| 7 | m02-l01 | 350–352 | Prose: direct remission inside the same institution, art. 10.2 LO 4/2001 | PASS | «Cuando un órgano u autoridad se estime incompetente … remitirá directamente las actuaciones al órgano que considere competente, si ambos pertenecieran a la misma institución, administración u organismo». «u»→«o» and «pertenecieran»→«pertenecen» change no fact |
| 8 | m02-l01 | 358 | Title «Algunos plazos de las peticiones» (`plazos`) | PASS | «Algunos» marks a selection: art. 6.2 (acuse, diez días) and art. 7.2 (subsanación, quince días) are not rows |
| 9 | m02-l01 | 359 | Row 1: declaración de inadmisibilidad, arts. 9.1, 9.2 y 10.1 LO 4/2001 | PASS | 9.1 «siempre motivada … cuarenta y cinco días hábiles siguientes al de presentación del escrito de petición»; 9.2 «En otro caso …», here correctly after the plazo; 10.1 «los plazos se computarán desde la recepción del escrito». All three apartados written out (no sub-range); all cited in prose |
| 10 | m02-l01 | 360 | Row 2: remisión, art. 10.1 LO 4/2001 | PASS | As item 5. Order after row 1 is stated: «Siempre que la declaración de inadmisibilidad se base …» |
| 11 | m02-l01 | 361 | Row 3: contestación, arts. 10.1 y 11.1 LO 4/2001 | PASS | 11.1 «Una vez admitida a trámite una petición, … contestar y a notificar la contestación en el plazo máximo de tres meses a contar desde la fecha de su presentación», with the 10.1 cómputo that the R2c pass found missing. Order stated by «Una vez admitida a trámite» |
| 12 | m02-l01 | 384 | Normativa: LO 4/2001 «arts. 1–4 y 6–11» | PASS | Art. 10 is now cited in the prose; art. 5 is not cited and stays out |
| 13 | m02-l02 | 27–29 | Prose: art. 49.5 Ley 16/1985 | PASS | «La Administración del Estado podrá declarar constitutivos del Patrimonio Documental aquellos documentos que, sin alcanzar la antigüedad indicada en los apartados anteriores, merezcan dicha consideración». «esa antigüedad de cuarenta o cien años» is what apartados 3 and 4 indicate (apartado 2 sets none) |
| 14 | m02-l02 | 31 | Title «Documentos que forman parte del Patrimonio Documental» | PASS | Claims completeness and has it: art. 49.2–5 are every class of documents of the Patrimonio Documental (art. 49.1 is the definition of documento) |
| 15 | m02-l02 | 34 | Row art. 49.2 | PASS | Verbatim «documentos de cualquier época generados, conservados o reunidos en el ejercicio de su función por …» |
| 16 | m02-l02 | 35 | Row art. 49.3 | PASS | «con una antigüedad superior a los cuarenta años … por las entidades y asociaciones de carácter político, sindical o religioso y por las entidades, fundaciones y asociaciones culturales y educativas de carácter privado». Cell uses the prose's words (l. 24–26). See note 2 |
| 17 | m02-l02 | 36 | Row art. 49.4 | PASS | «antigüedad superior a los cien años generados, conservados o reunidos por cualesquiera otras entidades particulares o personas físicas» |
| 18 | m02-l02 | 37 | Row art. 49.5 | PASS | As item 13; «podrá declarar» kept as a power («Los que la Administración del Estado declare») |
| 19 | m02-l02 | 99–101 | Prose: «cursados sin dilación», art. 16.2 LPAC | PASS | «Concluido el trámite de registro, los documentos serán cursados sin dilación a sus destinatarios y a las unidades administrativas correspondientes desde el registro en que hubieran sido recibidas». «recibidos» fixes the norm's agreement, no fact changed |
| 20 | m02-l02 | 118 | Title «Del asiento a los destinatarios» (`pasos`) | PASS | Names its two ends; claims no more than art. 16.2 gives |
| 21 | m02-l02 | 119 | Step 1, asiento, art. 16.2 LPAC | PASS | Verbatim 16.2 first sentence. Actor «el registro»: the asiento is made in the registro (16.1 «en el que se hará el correspondiente asiento»; 16.3 «El registro electrónico … garantizará la constancia, en cada asiento») |
| 22 | m02-l02 | 120 | Step 2, curso de los documentos, art. 16.2 LPAC | PASS | Order stated in the text: «Concluido el trámite de registro». Actor «el registro en que hubieran sido recibidos» is the norm's «desde el registro en que hubieran sido recibidas» |
| 23 | m02-l02 | 288 | Source: `cultura-dta-presentacion.html`; DTA, «Presentación» | PASS | File exists; page `<title>` «Presentación - dta» and `fuentes.yaml` «… «Presentación»». Only the order of file and label changed |
| 24 | m02-l02 | 293 | Source: `cultura-dta-diccionario.html`; DTA, «Clasificación» | PASS | File exists; «Clasificación» is the dictionary entry used; no fact changed |
| 25 | m02-l02 | 299 | Source: `cultura-dta-diccionario.html`; DTA, «Ordenación» | PASS | As item 24 |
| 26 | m02-l03 | 69–70 | Source: `clave-que-es.html`; Cl@ve, «¿Qué es Cl@ve?», a fecha de 16-10-2026 | PASS | File exists; page `<title>` «Cl@ve \| ¿Qué es Cl@ve?»; date kept |
| 27 | m02-l03 | 81 | Source: `incibe-glosario-ciberseguridad.pdf`; INCIBE, «Glosario de términos de ciberseguridad», 2.1.30 | PASS | File exists; cover title «Glosario de términos de ciberseguridad»; entry «2.1.30. Autoridad de certificación … (AC o CA, por sus siglas en inglés, Certification Authority)» |
| 28 | m02-l03 | 119–120 | Prose: prior notice of a portal's supresión, art. 6.1 RD 203/2021 | PASS | «La supresión de portales requerirá la previa comunicación al Ministerio de Política Territorial y Función Pública y al Ministerio de Asuntos Económicos y Transformación Digital». «esos dos ministerios» points to the sentence before, which also gives today's ministry |
| 29 | m02-l03 | 128 | Row «Requisito de la supresión», art. 6.1 RD 203/2021 | PASS | Cell verbatim; title «Creación o supresión…» now has both requisites; citation in prose |
| 30 | m02-l03 | 148–149 | Prose: 20 días hábiles, art. 12.3 RD 1112/2018 (reworded) | PASS | «Recibidas las solicitudes de información accesible y quejas, la entidad obligada deberá responder a la persona interesada en el plazo de veinte días hábiles». See note 3 |
| 31 | m02-l03 | 149–151 | Prose: suspension, art. 12.4 RD 1112/2018 | PASS | «El transcurso de dicho plazo se podrá suspender en el caso de que deba requerirse a la persona interesada para que, en un plazo de diez días hábiles, formule las aclaraciones necesarias …. Transcurrido dicho plazo sin que la persona interesada haya realizado las aclaraciones oportunas, se continuará con su tramitación» |
| 32 | m02-l03 | 151–153 | Prose: effect of silence, art. 12.6 RD 1112/2018 | PASS | «Transcurrido el plazo máximo para resolver sin que se haya notificado la respuesta se entenderá que la solicitud de información accesible no ha sido aceptada o que la queja no ha sido considerada» |
| 33 | m02-l03 | 155–156 | Prose: dos meses, art. 13.4 RD 1112/2018 (reworded) | PASS | «Recibida la reclamación, la Unidad responsable de atenderla deberá responder a la persona interesada en el plazo máximo de dos meses». «posterior» is backed by 13.1 («una vez realizada una solicitud … o queja») |
| 34 | m02-l03 | 156–158 | Prose: suspension, art. 13.5 RD 1112/2018 | PASS | 13.5 repeats 12.4's wording for the reclamación; «de la misma forma, con un requerimiento de aclaraciones en diez días hábiles, y pasados esos días sin aclaraciones se continúa con la tramitación» drops no condition |
| 35 | m02-l03 | 158–159 | Prose: desestimación, art. 13.6 RD 1112/2018 (now cited alone) | PASS | «se entenderá que la reclamación ha sido desestimada»; the old «art. 13.4 y 13.6» is now one apartado per citation |
| 36 | m02-l03 | 161 | Title «Plazos de las solicitudes de información accesible, las quejas y las reclamaciones» (`plazos`) | PASS | Arts. 12 and 13 set no other plazo for these three; complete. Order «posterior» (l. 155) and 13.1 |
| 37 | m02-l03 | 162 | Row 1, arts. 12.3, 12.4 y 12.6 RD 1112/2018 | PASS | Verbatim, as items 30–32; each apartado written out; all cited in prose |
| 38 | m02-l03 | 163 | Row 2, arts. 13.4, 13.5 y 13.6 RD 1112/2018 | PASS | Verbatim, as items 33–35 |
| 39 | m02-l03 | 255–256 | Prose: «Sin perjuicio de la identidad definida en el marco de la Unión Europea», art. 6.1 RD 127/2015 | PASS | «Sin perjuicio de la identidad definida en el marco de la Unión Europea, la VUDS quedará integrada en el PAE electrónico». The joint «art. 6.1 y 6.3» citation is split in two |
| 40 | m02-l03 | 256–257 | Prose: «Emprende en 3», art. 6.3 RD 127/2015 | PASS | «La plataforma «Emprende en 3» queda integrada en el PAE electrónico» |
| 41 | m02-l03 | 261 | Source: `pae-circe.html`; PAE electrónico, «CIRCE» | PASS | File exists; label unchanged and the same as `fuentes.yaml` («…, «CIRCE»», page `CIRCE.aspx`). See note 5 |
| 42 | m02-l03 | 262 | Source: `pae-servicios.html`; PAE electrónico, «Servicios PAE» | PASS | File exists; label unchanged, as `fuentes.yaml` («Servicios PAE», page `ServiciosPae.aspx`). See note 5 |
| 43 | m02-l03 | 324 | Source: `pag-quienes-somos.html`; PAG, «¿Quiénes somos?» | PASS | File exists; page `<h1>` «¿Quiénes somos?» |
| 44 | m02-l03 | 327 | Source: `pag-telefono-060.html`; PAG, «Teléfono 060» | PASS | File exists; `<title>` «Punto de Acceso General \| Teléfono 060» |
| 45 | m02-l03 | 328–329 | Source: `pag-oficina-informacion.html`; PAG, «Nuestra Oficina de Información y Atención a la Ciudadanía» | PASS | File exists; `<h1>` verbatim |
| 46 | m02-l03 | 332 | Source: `sede-pag-portada.html`; sede del PAG, portada | PASS | File exists; it is the sede's home page (`fuentes.yaml` «… portada») |
| 47 | m02-l04 | 115–116 | Prose: art. 15.4 RGPD | PASS | «El derecho a obtener copia mencionado en el apartado 3 no afectará negativamente a los derechos y libertades de otros» |
| 48 | m02-l04 | 134 | Prose lead-in: «El derecho de supresión no se aplica cuando el tratamiento sea necesario (art. 17.3 RGPD):» | PASS | «Los apartados 1 y 2 no se aplicarán cuando el tratamiento sea necesario:». Apartado 2 (informing other controllers) is not taught in the lesson, so naming only the right drops nothing the reader has. Form (citation before the colon, then «- a)» items) matches m01-l02 l. 49, m03-l01 l. 70 |
| 49 | m02-l04 | 136–145 | Prose list a)–e), art. 17.3 RGPD | PASS | Letters a)–e) verbatim; d) «el derecho indicado en el apartado 1» → «el derecho de supresión». No list item carries a citation, so no letter-before-«)» misparse |
| 50 | m02-l04 | 157–158 | Prose: art. 20.3 RGPD | PASS | «se entenderá sin perjuicio del artículo 17. Tal derecho no se aplicará al tratamiento que sea necesario para el cumplimiento de una misión realizada en interés público o en el ejercicio de poderes públicos conferidos al responsable del tratamiento». Art. 17 is the derecho de supresión |
| 51 | m02-l04 | 158–159 | Prose: art. 20.4 RGPD | PASS | «El derecho mencionado en el apartado 1 no afectará negativamente a los derechos y libertades de otros». The citation wraps across lines («20.4⏎RGPD») and still parses |
| 52 | m02-l04 | 174–178 | Prose: exceptions, art. 22.2 RGPD | PASS | a) «es necesaria para la celebración o la ejecución de un contrato entre el interesado y un responsable del tratamiento»; b) «está autorizada por el Derecho de la Unión o de los Estados miembros … y que establezca asimismo medidas adecuadas …»; c) «se basa en el consentimiento explícito del interesado» |
| 53 | m02-l04 | 178–181 | Prose: safeguards, art. 22.3 RGPD | PASS | «En los casos a que se refiere el apartado 2, letras a) y c)» = «En los casos del contrato y del consentimiento explícito»; rest verbatim |
| 54 | m02-l04 | 181–183 | Prose: special categories, art. 22.4 RGPD | **FAIL** | The norm: «Las decisiones a que se refiere el apartado 2 no se basarán en las categorías especiales …», i.e. all three cases a), b) and c). The prose opens «Estas decisiones» right after the sentence on «los casos del contrato y del consentimiento explícito» (22.3), so it reads as covering a) and c) only and leaves out the decisions authorised by Union or Member State law. Narrower than the article. Replacement below |
| 55 | m02-l04 | 185 | Title «Algunos derechos del interesado» (was «Acceso, rectificación y oposición») | PASS | «Algunos» marks a selection: limitación (art. 18), art. 19 and art. 15.2 are not rows |
| 56 | m02-l04 | 189 | Row «Acceso, copia de los datos», arts. 15.3 y 15.4 RGPD | PASS | Cell is the prose (l. 114–116) word for word; each apartado written out |
| 57 | m02-l04 | 193 | Row «Supresión», arts. 17.1 y 17.3 RGPD | PASS | 17.1 in the prose's words («entre otros casos» keeps it a selection); the five 17.3 exceptions verbatim, as items 48–49 |
| 58 | m02-l04 | 194 | Row «Portabilidad», arts. 20.1, 20.3 y 20.4 RGPD | PASS | Label carries the 20.1 a)–b) conditions; cell as items 50–51 |
| 59 | m02-l04 | 197 | Row «Decisiones individuales automatizadas», arts. 22.1, 22.2, 22.3 y 22.4 RGPD | **FAIL** | Same defect as item 54: the cell's last sentence «Estas decisiones no se basarán …» follows «En los casos del contrato y del consentimiento explícito …» and reads as limited to them; art. 22.4 covers «Las decisiones a que se refiere el apartado 2» |
| 60 | m02-l04 | 317–320 | Prose: early cese, art. 48.5 párrafo 2 LOPDGDD | PASS | «La Presidencia y el Adjunto solo cesarán antes de la expiración de su mandato, a petición propia o por separación acordada por el Consejo de Ministros, por: a) Incumplimiento grave de sus obligaciones, b) incapacidad sobrevenida para el ejercicio de su función, c) incompatibilidad, o d) condena firme por delito doloso» |
| 61 | m02-l04 | 320–322 | Prose: ratification, art. 48.5 párrafo 3 LOPDGDD | PASS | «En los supuestos previstos en las letras a), b) y c) será necesaria la ratificación de la separación por las mayorías parlamentarias previstas en el apartado 3 de este artículo». Letters spelt out by name; the 48.3 majorities are stated at l. 309–314 |
| 62 | m02-l04 | 335 | Row «Cese de la Presidencia y del Adjunto antes de la expiración de su mandato», art. 48.5 LOPDGDD | PASS | Cell is items 60–61 verbatim; citation in prose |
| 63 | m02-l04 | 350–353 | Prose: the claim proceeds without notification, art. 65.5 LOPDGDD | PASS | «Si transcurrido este plazo no se produjera dicha notificación, se entenderá que prosigue la tramitación de la reclamación … a partir de la fecha en que se cumpliesen tres meses desde que la reclamación tuvo entrada en la Agencia …, sin perjuicio de la facultad de la Agencia de archivar posteriormente y de forma expresa la reclamación». «con arreglo a lo dispuesto en este título» left out; it is a reference, not a condition |
| 64 | m02-l04 | 353–355 | Prose: cómputo when another authority communicates, art. 65.5 párrafo 2 LOPDGDD | **FAIL** | The norm: «En el supuesto de que la Agencia … actúe como consecuencia de la comunicación que le hubiera sido remitida por la autoridad de control de otro Estado miembro de la Unión Europea, conforme al artículo 64.4 de esta ley orgánica, el cómputo … se iniciará una vez que se reciba en la Agencia toda la documentación necesaria». The prose drops «conforme al artículo 64.4». Art. 64.4 limits the case to the communication of a reclamación filed with that authority «cuando la Agencia … tuviese la condición de autoridad de control principal». Without it the rule covers any communication from another authority. Wider than the article. Replacement below |
| 65 | m02-l04 | 363 | Row «La Agencia, sobre la admisión a trámite de la reclamación», art. 65.5 LOPDGDD | **FAIL** | Its third sentence repeats item 64 and drops «conforme al artículo 64.4» in the same way. The first two sentences are correct (item 63) |

## Replacements for the FAILs

Each one fixes words only; none needs a clause the norm lacks, and none changes a citation.

**#4, m02-l01 l. 337–343.** Put «En otro caso» back right after the plazo it answers, then the 9.1 párrafo 2 sentence:

```
La declaración de inadmisibilidad será siempre motivada y deberá acordarse y notificarse al peticionario en los
cuarenta y cinco días hábiles siguientes al de presentación del escrito (art. 9.1 LO 4/2001). En otro caso, se
entenderá que la petición ha sido admitida a trámite (art. 9.2 LO 4/2001). Cuando la inadmisión traiga causa de la
existencia en el ordenamiento jurídico de otros procedimientos específicos para la satisfacción del objeto de la
petición, la declaración deberá indicar expresamente las disposiciones a cuyo amparo deba sustanciarse, así como el
órgano competente para ella (art. 9.1 LO 4/2001).
```

**#54, m02-l04 l. 181.** Replace «Estas decisiones no se basarán» with «Las decisiones de los tres casos del artículo 22.2 no
se basarán». **#59, l. 197:** the same replacement in the cell («… impugnar la decisión. Las decisiones de los tres casos
del artículo 22.2 no se basarán en las categorías especiales …»). Moving the 22.4 sentence before the 22.3 one would also
work, but the replacement is shorter.

**#64, m02-l04 l. 353–355.** Keep the norm's cross-reference:

```
Cuando la Agencia actúe por la comunicación que le haya remitido la autoridad de control de otro Estado miembro de la
Unión Europea conforme al artículo 64.4 de la LOPDGDD, el cómputo de ese plazo se inicia una vez que reciba toda la
documentación necesaria para su tramitación (art. 65.5 LOPDGDD).
```

**#65, l. 363:** in the cell, «… de otro Estado miembro de la Unión Europea, conforme al artículo 64.4, el cómputo se
inicia …». The reference stays in running text, not in parentheses, so the parser does not read it as a citation and
the row needs no 64.4 anchor in the prose.

## Notes outside the PASS/FAIL count (none blocks)

1. m02-l01 l. 210–212 (item 2): LO 5/1992 and art. 37 of Ley 30/1992 are both repealed. The sentence quotes RD 208/1996
   faithfully, and the RD has not been amended (consolidated 2011-06-04). Elsewhere the course marks such a lag with
   «(hoy: …)» (m02-l03 l. 119). A reader could take the two laws as in force. Not a fidelity fault; worth a
   «(hoy: …)» pointer in a later round if the course wants one.
2. m02-l02 l. 24–26 and row l. 35 (item 16): art. 49.3 says «generados, conservados o reunidos en el ejercicio de sus
   actividades por» the entities; prose and row say «Los documentos de las entidades». The prose sentence predates this
   round, the row copies it, and the omitted words hardly narrow anything («conservados» covers any document an entity
   holds). Row 49.2 keeps its parallel «en el ejercicio de su función» in full, so the two rows read unevenly. Not
   changed here.
3. m02-l03 l. 148–163 (items 30–38): the consolidated text of RD 1112/2018 notes that STC 100/2019 declares apartados 1,
   3, 4 and 6 of art. 12 and apartados 2 to 6 of art. 13 not basic («invaden las competencias autonómicas y carecen de
   carácter de legislación básica»). The lesson says the RD applies to the CCAA and local entities (art. 2.1) and states
   these plazos unconditionally, now also in a `plazos` esquema. This gap predates the round (arts. 12.3, 13.4 and 13.6
   were already there); the new sentences only follow the article text. Candidate for a later prose gap.
4. m02-l03 l. 148 and 155: two consecutive paragraphs open «Recibidas …» / «Recibida …». They follow the norm's own
   parallel openings (12.3, 13.4) and the pattern occurs nowhere else in the lesson, so it is not the tic the voice page
   forbids. Voice otherwise clean in all added text: no filler, rhetorical question, triad, «no solo… sino», closer,
   stacked hedge or blacklisted split opener («Es…», «Eso…», «Por eso…», «Y…», «También es…»). The long sentences
   (m02-l01 3.2, m02-l04 17.3 b) and 22.2–22.4, 48.5) each carry one idea and follow the norm's own list.
5. m02-l03 l. 261–262 (items 41–42): the labels «CIRCE» and «Servicios PAE» are the `fuentes.yaml` labels and the page
   slugs (`CIRCE.aspx`, `ServiciosPae.aspx`). The pages' `<title>`s read «Qué es CIRCE y trámites que se pueden realizar
   con CIRCE» and «Servicios que prestan los PAE». The round did not change these labels, only their position.
6. Wrap width: the rewritten source citations leave lines longer than the file's ~118-column wrap (m02-l02 l. 288, 293;
   m02-l03 l. 69, 81, 262, 328, 332). Cosmetic; a re-wrap would not change a citation.
7. m02-l02 l. 109–120: the new `pasos` step 1 repeats the «Orden y fecha» row of the table just above it word for word,
   the same kind of repetition the R2c pass already noted for the two registro tables.
