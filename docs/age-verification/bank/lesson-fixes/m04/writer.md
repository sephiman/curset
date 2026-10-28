# Lesson fixes, module m04 (bloque IV): writer's record, 2026-10-23

Course `content/age-administrativo-c1`, lessons under `es/lessons/`. Nothing committed. Norm texts are `pdftotext -layout`
of the files named in `sources/normativa.yaml`: Ley 29/1975 `BOE-A-1975-13887_…_1975-06-30`, RDL 4/2000
`BOE-A-2000-12140_…_2024-12-21`, RD 577/1997 `BOE-A-1997-9874_…_2026-06-12` (already carries RD 466/2026), TRLCPE
`BOE-A-1987-12636_…_2025-01-29`, RD 829/2023 `BOE-A-2023-23537_…_2023-12-29`, LGSS `BOE-A-2015-11724_…_2026-10-03`
(its `cambios_pendientes`, Ley 4/2026, touch arts. 190.5 and 363.1.d) only), RD 33/1986 `BOE-A-1986-1216_…_1991-12-31`,
LRJSP `BOE-A-2015-10566_…_2024-08-02`, LPAC `BOE-A-2015-10565_…_2024-11-06`, Ley 30/1984 `BOE-A-1984-17387_…_2015-10-31`,
TREBEP `BOE-A-2015-11719_…_2026-10-03` (Ley 4/2026 touches art. 49.e) only), RD 365/1995 `BOE-A-1995-8730_…_2006-03-04`.
Line numbers are those of the lesson files after this round. Added words are in bold where a sentence was joined.

Checks: `uv run pytest tests/test_esquema.py -q` 10 passed; `uv run pytest tests/test_citations.py -q -k "not frozen"`
60 passed. Every new citation resolves with `CourseCitations.build(...)._anchor(lesson, citation, 'es')` (anchors given
per item). Goldens not regenerated.

## m04-l07: hunks from the stopped run

The stopped run left five hunks in `git diff HEAD`. Each was checked against the norm; four kept as they were, one kept
and reordered.

### 1. Ley 29/1975 citation form (l. 25 and Normativa l. 232–233), citation form, kept

`(arts. tercero.uno y diez.uno Ley 29/1975)` → `(arts. 3.1 y 10.1 Ley 29/1975)`. The resolver gives `None` for
«art. tercero.uno Ley 29/1975» and `boe-a-1975-13887-art-3` / `-art-10` for the new form. The fact is unchanged. The
Normativa line now reads «arts. 3.1 y 10.1 (artículos tercero, apartado uno, y diez, apartado uno, en el texto)».

Norm: «Artículo diez.—Uno. Todos los funcionarios de carrera de la Administración Civil del Estado en situación de
activo, excedencia especial excedencia forzosa, supernumerario y suspensión de funciones, y los demás comprendidos en el
artículo tercero, uno, serán obligatoriamente incorporados, como mutualistas, a la Mutualidad General de Funcionarios
Civiles del Estado.»

### 2. Art. 4.1 RDL 4/2000 old ministry name (l. 87–89), correction, kept

Whole sentence: «El sistema de mutualismo administrativo se gestiona y presta a través de la Mutualidad General de
Funcionarios Civiles del Estado (MUFACE), «dependiente del Ministerio de Administraciones Públicas» (hoy: Ministerio
para la Transformación Digital y de la Función Pública) (art. 4.1 RDL 4/2000; art. 22.2 RD 829/2023).» Added: the
quotation marks, the «(hoy: …)» and the RD 829/2023 citation.

Norm (art. 4.1 RDL 4/2000): «El sistema de mutualismo administrativo, al que se refiere esta Ley, se gestionará y
prestará a través de la Mutualidad General de Funcionarios Civiles del Estado (MUFACE), dependiente del Ministerio de
Administraciones Públicas.» Norm (art. 22.2 RD 829/2023): «Asimismo corresponde al Ministerio para la Transformación
Digital y de la Función Pública la propuesta y ejecución de la política del Gobierno en materia de administración
pública, función pública, y gobernanza pública.» Convention 1 (theory ledger): the «hoy» department is the one whose RD
829/2023 competences cover the function. Anchors: `boe-a-2000-12140-art-4`, `boe-a-2023-23537-art-22`.

### 3. MUFACE as organismo autónomo, art. 1.1 RD 577/1997 (l. 98–100), addition, kept and moved

The stopped run put the sentence between «El RD 577/1997 la denomina …» and «La adscribe …», so «La adscribe» lost its
subject (the RD). The sentence now follows the Secretaría de Estado sentence, with «La MUFACE» as subject:

«La MUFACE es un organismo autónomo de los previstos en el artículo 98.1 de la Ley 40/2015, de 1 de octubre, de Régimen
Jurídico del Sector Público, con personalidad jurídica diferenciada y plena capacidad de obrar, tesorería y patrimonio
propios y autonomía en su gestión (art. 1.1 RD 577/1997).»

Norm (art. 1.1 RD 577/1997, text after RD 466/2026): «La Mutualidad General de Funcionarias y Funcionarios Civiles del
Estado es un organismo autónomo de los previstos en el artículo 98.1 de la Ley 40/2015, de 1 de octubre, de Régimen
Jurídico del Sector Público, adscrito a través de la Secretaría de Estado de Función Pública al Ministerio del que ésta
dependa, con personalidad jurídica diferenciada y plena capacidad de obrar, tesorería y patrimonio propios y autonomía
en su gestión.» The adscripción clause is already stated in the preceding sentence. The l. 91–93 sentence («organismo
público», art. 5.1 RDL 4/2000) stays: both norms say it, and an organismo autónomo is an organismo público. Anchor:
`boe-a-1997-9874-art-1`.

### 4. Art. 5.1 RD 577/1997 old ministry name (l. 106–108), correction, kept

Bullet: «… y siete representantes de la Administración Civil del Estado designados por el «Ministro de Hacienda y
Función Pública» (hoy: titular del Ministerio para la Transformación Digital y de la Función Pública) (art. 22.2 RD
829/2023).» Added: the quotation marks, the «(hoy: …)» and the citation.

Norm (art. 5.1.a).3.º RD 577/1997): «Siete representantes de la Administración Civil del Estado designados por el
Ministro de Hacienda y Función Pública.» Art. 22.2 RD 829/2023 as in item 2. Anchor: `boe-a-2023-23537-art-22`.

### 5. Art. 28.3.b) TRLCPE, organ deciding jubilación voluntaria (l. 196–200), addition, kept

«La jubilación voluntaria de un funcionario civil de la Administración del Estado la acuerda el Subsecretario del
Departamento ministerial al que esté adscrito su Cuerpo o Escala; si el Cuerpo o Escala está adscrito al «Ministerio
para las Administraciones Públicas» (hoy: Ministerio para la Transformación Digital y de la Función Pública) y depende
de la «Secretaría de Estado para la Administración Pública» (hoy: Secretaría de Estado de Función Pública), la acuerda
el Director general de la Función Pública (art. 28.3.b) TRLCPE; art. 22.3.c) RD 829/2023).»

Norm (art. 28.3.b) TRLCPE): «Cuando se trate de jubilación voluntaria de funcionario civil de la Administración del
Estado, por el Subsecretario del Departamento ministerial al que esté adscrito el Cuerpo o Escala a que pertenezca el
funcionario, siendo el Director general de la Función Pública del Ministerio para las Administraciones Públicas la
autoridad competente para acordarla, en caso de que el funcionario pertenezca a un Cuerpo o Escala adscrito al
Ministerio para las Administraciones Públicas y dependiente de la Secretaría de Estado para la Administración
Pública.» Art. 22.3.c) RD 829/2023 places the Secretaría de Estado de Función Pública in the Ministerio para la
Transformación Digital y de la Función Pública. The lesson's section on jubilación voluntaria (art. 28.2.b)) reaches
it; the bank ledger lists the organ as an official fact (conv2020_X·S2R·1). Normativa: art. 28.3.b) TRLCPE and art.
22.2 RD 829/2023 added. Anchors: `boe-a-1987-12636-art-28`, `boe-a-2023-23537-art-22`.

All brief items for m04-l07 are covered by these hunks; nothing further was added.

## m04-l09

### Jubilación anticipada, arts. 207.1 and 208.1 LGSS (l. 150–157), addition

New paragraph after the jubilación ordinaria paragraph:

- «La jubilación anticipada derivada del cese en el trabajo por causa no imputable a la libre voluntad del trabajador
  exige una edad inferior en cuatro años, como máximo, a la del art. 205.1.a), estar inscrito como demandante de
  empleo durante, al menos, los seis meses inmediatamente anteriores a la solicitud, 33 años de cotización efectiva sin
  contar la parte proporcional por pagas extraordinarias y que el cese se deba a una de las causas que el artículo
  enumera, entre ellas el despido colectivo y el despido por causas objetivas (art. 207.1 LGSS).»
- «La jubilación anticipada por voluntad del interesado exige una edad inferior en dos años, como máximo, a la del art.
  205.1.a), treinta y cinco años de cotización efectiva sin contar esa parte proporcional y que la pensión resulte
  superior a la pensión mínima que le correspondería por su situación familiar al cumplir sesenta y cinco años (art.
  208.1 LGSS).»

Norm (art. 207.1): «a) Tener cumplida una edad que sea inferior en cuatro años, como máximo, a la edad que en cada caso
resulte de aplicación según lo establecido en el artículo 205.1.a) sin que a estos efectos resulten de aplicación los
coeficientes reductores a que se refieren los artículos 206 y 206 bis. b) Encontrarse inscrito en las oficinas de
empleo como demandante de empleo durante un plazo de, al menos, seis meses inmediatamente anteriores a la fecha de la
solicitud de la jubilación. c) Acreditar un período mínimo de cotización efectiva de 33 años, sin que, a tales efectos,
se tenga en cuenta la parte proporcional por pagas extraordinarias. […] d) Que el cese en el trabajo se haya producido
por alguna de las causas siguientes: 1.ª El despido colectivo por causas económicas, técnicas, organizativas o de
producción […]. 2.ª El despido por causas objetivas […]» (seven causes in all).

Norm (art. 208.1): «a) Tener cumplida una edad que sea inferior en dos años, como máximo, a la edad que en cada caso
resulte de aplicación según lo establecido en el artículo 205.1.a), sin que a estos efectos resulten de aplicación los
coeficientes reductores a que se refieren los artículos 206 y 206 bis. b) Acreditar un período mínimo de cotización
efectiva de treinta y cinco años, sin que, a tales efectos, se tenga en cuenta la parte proporcional por pagas
extraordinarias. […] c) Una vez acreditados los requisitos generales y específicos de dicha modalidad de jubilación, el
importe de la pensión a percibir ha de resultar superior a la cuantía de la pensión mínima que correspondería al
interesado por su situación familiar al cumplimiento de los sesenta y cinco años de edad.»

Core conditions only, as the brief asks: the reduction coefficients (arts. 207.2, 208.2), the 206/206 bis proviso and
the service-militar computation are left out; «entre ellas» marks the cause list as partial. Normativa: arts. 207.1 and
208.1 added. Anchors: `boe-a-2015-11724-art-207`, `boe-a-2015-11724-art-208`.

### Grade names in force, DT 26.ª LGSS (l. 135–138), addition

After the grades table: «El art. 194 solo se aplica desde que entren en vigor las disposiciones reglamentarias de su
apartado 3; hasta que no se desarrolle, rige la redacción de la disposición transitoria vigésima sexta, que llama a los
grados incapacidad permanente parcial para la profesión habitual, incapacidad permanente total para la profesión
habitual, incapacidad permanente absoluta para todo trabajo y gran incapacidad (disposición transitoria vigesimosexta
LGSS).»

Norm: «Uno. Lo dispuesto en el artículo 194 de esta ley únicamente será de aplicación a partir de la fecha en que
entren en vigor las disposiciones reglamentarias a que se refiere el apartado 3 del mencionado artículo 194. Hasta que
no se desarrolle reglamentariamente dicho artículo será de aplicación la siguiente redacción: «Artículo 194. […] 1. […]
a) Incapacidad permanente parcial para la profesión habitual. b) Incapacidad permanente total para la profesión
habitual. c) Incapacidad permanente absoluta para todo trabajo. d) Gran incapacidad.»»

Citation form: «disposición transitoria vigésima sexta LGSS» parses as ordinal «vigésima» plus a norm «sexta LGSS»
(anchor `sexta-lgss-dt-vigesima`, no norm). The parser takes a one-word ordinal, as m03-l07's «vigesimoctava»; the
citation and the Normativa line use «vigesimosexta». Anchor: `boe-a-2015-11724-dt-vigesimosexta`. The table and the
«Lo que más cae» line keep citing art. 194.1 for the four grades: the short names are the same in both texts.

## m04-l06

### Faltas muy graves of the RD, art. 6 RD 33/1986 (l. 173–191), addition

After the art. 95.2 TREBEP list, under «Faltas muy graves»: «El RD 33/1986 tipifica como faltas muy graves (art. 6 RD
33/1986):» and the fourteen letters a)–n) in the norm's words. A list, not one sentence: the lesson lists arts. 7.1 and 8
RD 33/1986 the same way, and art. 47.2 (l. 360–362) already refers to art. 6.h).

Norm: «Son faltas muy graves: a) El incumplimiento del deber de fidelidad a la Constitución en el ejercicio de la
Función Pública. b) Toda actuación que suponga discriminación por razón de raza, sexo, religión, lengua, opinión, lugar
de nacimiento, vecindad, o cualquier otra condición o circunstancia personal o social. c) El abandono de servicio. d)
La adopción de acuerdos manifiestamente ilegales que causen perjuicio grave a la Administración o a los ciudadanos. e)
La publicación o utilización indebida de secretos oficiales así declarados por Ley o clasificados como tales. f) La
notoria falta de rendimiento que comporte inhibición en el cumplimiento de las tareas encomendadas. g) La violación de
la neutralidad o independencia políticas, utilizando las facultades atribuidas para influir en procesos electorales de
cualquier naturaleza y ámbito. h) El incumplimiento de las normas sobre incompatibilidades. i) La obstaculización al
ejercicio de las libertades públicas y derechos sindicales. j) La realización de actos encaminados a coartar el libre
ejercicio del derecho de huelga. k) La participación en huelgas, a los que la tengan expresamente prohibida por la ley.
l) El incumplimiento de la obligación de atender los servicios esenciales en caso de huelga. m) Los actos limitativos
de la libre expresión de pensamiento, ideas y opiniones. n) Haber sido sancionado por la comisión de tres faltas graves
en un período de un año.» Normativa: art. 6 added. Anchor: `boe-a-1986-1216-art-6`.

### Interruption of prescription, arts. 25.3 and 30.2 LRJSP (l. 274–280), addition (re-verifier note)

Art. 25.3 LRJSP was read: it extends «las disposiciones de este Capítulo» (capítulo III of título preliminar,
«Principios de la potestad sancionadora», arts. 25–31) to the potestad disciplinaria over the personal «cualquiera que
sea la naturaleza jurídica de la relación de empleo», so it reaches funcionarios; art. 30 is in that chapter. Joined to
the end of the art. 20.2 RD 33/1986 paragraph, the conflict (RD: six months of paralysis; LRJSP: one month and «con
conocimiento del interesado») left unresolved:

«La Ley 40/2015, de 1 de octubre, de Régimen Jurídico del Sector Público (LRJSP), extiende las disposiciones de su
capítulo sobre los principios de la potestad sancionadora a la potestad disciplinaria de las Administraciones respecto
del personal a su servicio, cualquiera que sea la naturaleza jurídica de la relación de empleo (art. 25.3 LRJSP), y en
ese capítulo la prescripción de las infracciones la interrumpe la iniciación, con conocimiento del interesado, de un
procedimiento administrativo de naturaleza sancionadora, y el plazo se reinicia si el expediente está paralizado más de
un mes por causa no imputable al presunto responsable (art. 30.2 LRJSP).»

Norm (art. 25.3): «Las disposiciones de este Capítulo serán extensivas al ejercicio por las Administraciones Públicas
de su potestad disciplinaria respecto del personal a su servicio, cualquiera que sea la naturaleza jurídica de la
relación de empleo.» Norm (art. 30.2, párr. 2): «Interrumpirá la prescripción la iniciación, con conocimiento del
interesado, de un procedimiento administrativo de naturaleza sancionadora, reiniciándose el plazo de prescripción si el
expediente sancionador estuviera paralizado durante más de un mes por causa no imputable al presunto responsable.»

The lesson did not say the RD is the only rule («El artículo 97 del TREBEP no regula la interrupción. En el RD 33/1986 la
interrumpe…»); nothing there was changed. Art. 30.3 (interruption for sanciones) is not added: the note was about
faltas. The LRJSP is new to the lesson, so it is named in full here, its first mention. Normativa: new line «Ley
40/2015 (LRJSP): arts. 25.3, 30.2 y 61.s).», in the form other lessons use. Anchors: `boe-a-2015-10566-art-25`,
`boe-a-2015-10566-art-30`.

### Months date to date, art. 30.4 LPAC (l. 337–341), addition

Joined to the end of the diez días paragraph in «Instrucción»: «Los plazos en meses del RD 33/1986 (el del pliego de
cargos y el de las pruebas) tampoco tienen regla de cómputo propia; en la LPAC, el plazo fijado en meses se computa a
partir del día siguiente a aquel en que tenga lugar la notificación o publicación del acto y concluye el mismo día en
que se produjo la notificación o publicación en el mes de vencimiento, o el último día del mes si en este no hay día
equivalente (art. 30.4 LPAC).»

Norm: «4. Si el plazo se fija en meses o años, éstos se computarán a partir del día siguiente a aquel en que tenga
lugar la notificación o publicación del acto de que se trate, o desde el siguiente a aquel en que se produzca la
estimación o desestimación por silencio administrativo. El plazo concluirá el mismo día en que se produjo la
notificación, publicación o silencio administrativo en el mes o el año de vencimiento. Si en el mes de vencimiento no
hubiera día equivalente a aquel en que comienza el cómputo, se entenderá que el plazo expira el último día del mes.»
RD 33/1986 has no computation rule (searched for «cómputo», «hábil», «computar», «naturales»: only arts. 16 and 51,
unrelated). The sentence does not say the LPAC rule governs the RD's months, since art. 35.1 RD counts the pliego month
«a partir de la incoación», not from a notification. Silencio and años are left out: no plazo of the procedure uses
them. Normativa: «arts. 30.2–3» → «arts. 30.2–4». Anchor: `boe-a-2015-10565-art-30`.

### Separación del servicio, art. 61.s) LRJSP beside art. 47.1 RD 33/1986 (l. 366–367), addition

New paragraph after the art. 47 list in «Resolución», the art. 47.1 bullet left as it is: «La LRJSP atribuye a los
Ministros, como titulares del departamento, la función de imponer la sanción de separación del servicio por faltas muy
graves (art. 61.s) LRJSP).»

Norm (art. 61 LRJSP): «Los Ministros, como titulares del departamento sobre el que ejercen su competencia, dirigen los
sectores de actividad administrativa integrados en su Ministerio, […] A tal fin, les corresponden las siguientes
funciones: […] s) Imponer la sanción de separación del servicio por faltas muy graves.» Norm (art. 47.1 RD 33/1986):
«El Consejo de Ministros, a propuesta del Ministro de la Presidencia, quien con carácter previo oirá a la Comisión
Superior de Personal, para imponer la separación del servicio.» Both stated, the conflict not resolved (bank ledger open
item 9). Anchor: `boe-a-2015-10566-art-61`.

## m04-l04

### Trienios in excedencia por prestación de servicios en el sector público, art. 29.3 Ley 30/1984 (l. 246–249), addition

Joined to the art. 15.3 RD 365/1995 paragraph: «En la Ley 30/1984 el tiempo de excedencia voluntaria no computa a
efectos de trienios, salvo el período de prestación de servicios en organismos o entidades del sector público, con la
excepción de los prestados en sociedades mercantiles en cuyo capital sea mayoritaria la participación directa o
indirecta de las Administraciones públicas (art. 29.3 Ley 30/1984).»

Norm (art. veintinueve.3, after letter d)): «Los funcionarios excedentes no devengarán retribuciones, ni les será
computable el tiempo permanecido en tal situación a efectos de ascensos, trienios y derechos pasivos. No obstante lo
dispuesto en el párrafo anterior, se computará a efectos de trienios, el período de prestación de servicios en
organismos o entidades del sector público, con la excepción de los prestados en sociedades mercantiles en cuyo capital
sea mayoritaria la participación directa o indirecta de las Administraciones públicas.» It stays applicable through
the BOE note and DF 4.ª.2 TREBEP, which the lesson already states at l. 110–118. Art. 19 RD 365/1995 (l. 263–264,
excedencia time does not compute for trienios) is not contradicted: the Ley counts the services rendered, not the
excedencia as such. Normativa: «arts. 29.3.c), 29.5 …» → «arts. 29.3, 29.5 …». Anchor: `boe-a-1984-17387-art-29`.

### Suspensión provisional in a judicial procedure, art. 98.3 TREBEP (l. 275–278), addition

Joined after «el procedimiento está en m04-l06.»: «La acordada durante un procedimiento judicial se mantiene por el
tiempo a que se extienda la prisión provisional u otras medidas decretadas por el juez que determinen la imposibilidad
de desempeñar el puesto de trabajo, y si excede de seis meses no supone pérdida del puesto de trabajo (art. 98.3
TREBEP).»

Norm: «La suspensión provisional podrá acordarse también durante la tramitación de un procedimiento judicial, y se
mantendrá por el tiempo a que se extienda la prisión provisional u otras medidas decretadas por el juez que determinen
la imposibilidad de desempeñar el puesto de trabajo. En este caso, si la suspensión provisional excediera de seis meses
no supondrá pérdida del puesto de trabajo.» Normativa: art. 98.3 TREBEP added. Anchor: `boe-a-2015-11719-art-98`.

## m04-l02 and m04-l05: tables checked, no change

m04-l02 «Convocatoria y plazos del proceso» (l. 106–111): arts. 18.1, 20.1, 16.j) and 23.1 RD 364/1995 are read as prose
citations and resolve to `boe-a-1995-8729-art-18`, `-art-20`, `-art-16`, `-art-23`. m04-l05 «Otras formas de provisión»
(l. 130–138): arts. 64.1 y 64.3, 64.2–3, 63 y 72.2, 59.1, 60.1 y 60.3, 66 bis, 66 ter RD 364/1995 and 82.1 TREBEP all
resolve (`-art-64`, `-art-63`, `-art-72`, `-art-59`, `-art-60`, `-art-66-bis`, `-art-66-ter`,
`boe-a-2015-11719-art-82`). No cell is misread.

## Items not done

None. RD 466/2026 is not a separate file in `sources/`, but the RD 577/1997 file is consolidated to 12-06-2026 and
carries its text, so the m04-l07 item could be done from it.
