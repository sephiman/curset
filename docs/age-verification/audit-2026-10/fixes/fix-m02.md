# R2b fixes — bloque II (m02-l01 … m02-l04)

Writer, 2026-10-17, to `spec.md` (this folder). Inputs: `coverage/m02.md`, `coverage/m02-l0N.md`, `scope/m02.md`,
the bloque II section of `docs/age-theory-ledger.md`, the questionnaires and keys in `SP/exams/`. Sources read with
`pdftotext -layout` from `content/age-administrativo-c1/sources/normativa/`. Nothing committed.

## m02-l01

1. **note** — section «Las cartas de servicios» (kept by scope). Exam row: conv2025_A P1 12 (= B 13), «Las cartas de
   servicios, reguladas en el artículo 10.4 del Real Decreto 951/2005 … se actualizarán … al menos:», key c «Cada tres
   años»; checked in `2026-05-23_conv2025_modeloA_cuestionario.txt`.
   Old: (heading followed directly by the first paragraph). New, right after the heading:
   ```
   :::note{type=info}
   Fuera del enunciado literal del programa; preguntado en la convocatoria 2025 (modelo A), primera parte, pregunta 12.
   :::
   ```
   Normativa / «Lo que más cae»: unchanged.

## m02-l02

No change. Coverage 7/7; no note, removal, gap or cut item for this lesson (see «Cut items checked»).

## m02-l03

1. **coverage** — section «La oficina de asistencia en materia de registros». Exam row: conv2024_X S1 6 (II.3 o
   III.3, key b «La digitalización de su solicitud»), the miss in `coverage/m02.md`.
   Old:
   ```
   Entre las funciones de la oficina de asistencia en materia de registros de la Administración General del Estado
   están estas dos (art. 40.3 RD 203/2021):

   - f) La identificación …
   ```
   New:
   ```
   Entre las funciones de la oficina de asistencia en materia de registros de la Administración General del Estado
   están estas tres (art. 40.3 RD 203/2021):

   - a) La digitalización de las solicitudes, escritos y comunicaciones en papel que se presenten o sean recibidos en la
     Oficina y se dirijan a cualquier órgano, organismo público o entidad de derecho público de cualquier Administración
     Pública, así como su anotación en el Registro Electrónico General o Registro electrónico de cada organismo o entidad
     según corresponda.
   - f) La identificación …
   ```
   Source (`BOE-A-2021-5032_rd-203-2021-medios-electronicos_2025-04-02.pdf`, art. 40.3.a): «a) La digitalización de las
   solicitudes, escritos y comunicaciones en papel que se presenten o sean recibidos en la Oficina y se dirijan a
   cualquier órgano, organismo público o entidad de derecho público de cualquier Administración Pública, así como su
   anotación en el Registro Electrónico General o Registro electrónico de cada organismo o entidad según corresponda.»
   m02-l02 states the same function (art. 40.3.a) y c)); no extra pointer added, since m02-l03 already points to m02-l02
   for the registro in «Los servicios de la sede». Normativa: RD 203/2021 line already lists art. 40. «Lo que más cae»:
   unchanged (one question).

2. **restore** — section «En la LPAC» (PAG). Exam row: conv2020_X P1 22 (II.3 o III.3, «Señale la respuesta
   INCORRECTA … P.A.G.», key a); option d («Los interesados … tienen derecho a consultar la información y documentos
   relativos al procedimiento en el P.A.G.») is the art. 53.1.a), second paragraph, first sentence, which the lesson
   did not state (it stated only the second sentence, on copies). Added before the copies sentence:
   ```
   Quienes se relacionen con las Administraciones Públicas a través de medios electrónicos tienen derecho a consultar
   en el Punto de Acceso General electrónico de la Administración el estado de la tramitación de los procedimientos en
   los que sean interesados, el sentido del silencio administrativo que corresponda, el órgano competente para su
   instrucción, en su caso, y resolución, y los actos de trámite dictados (art. 53.1.a) LPAC).
   ```
   Source (`BOE-A-2015-10565_lpac_2024-11-06.pdf`, art. 53.1.a): «A conocer, en cualquier momento, el estado de la
   tramitación de los procedimientos en los que tengan la condición de interesados; el sentido del silencio
   administrativo que corresponda, en caso de que la Administración no dicte ni notifique resolución expresa en plazo;
   el órgano competente para su instrucción, en su caso, y resolución; y los actos de trámite dictados. […] Quienes se
   relacionen con las Administraciones Públicas a través de medios electrónicos, tendrán derecho a consultar la
   información a la que se refiere el párrafo anterior, en el Punto de Acceso General electrónico de la Administración
   que funcionará como un portal de acceso.» Normativa: LPAC line already lists 53.1.a). «Lo que más cae»: unchanged.

3. **optional precision not applied** — «Autoridad de Certificación» without «CA» (conv2022_X P1 44). No saved source
   prints «Autoridad de Certificación (CA)»: the RD 203/2021 anexo has «Autoridad de Certificación» only; the only «(CA)»
   in `sources/` is `sources/otros/ms-win-desuso.html` («entidades de certificación (CA) Enterprise», a Windows
   deprecation page, a different term). The row stays covered in m06-l01. No change.

## m02-l04

1. **restore** — section «La protección de datos personales y su régimen jurídico». Exam row: conv2020 P1 14 (II.4,
   vigente, key d «Sí, salvo que el fallecido lo hubiere prohibido expresamente o así lo establezca una ley»). The
   scope report flagged it; the lesson had no art. 3. Added after the definitions of art. 4.1–4.2 RGPD:
   ```
   La LOPDGDD no se aplica a los tratamientos de datos de personas fallecidas, sin perjuicio de lo establecido en su
   artículo 3 (art. 2.2.b) LOPDGDD). Las personas vinculadas al fallecido por razones familiares o de hecho, así como sus
   herederos, podrán dirigirse al responsable o encargado del tratamiento para solicitar el acceso a los datos personales
   de aquel y, en su caso, su rectificación o supresión. No podrán hacerlo cuando la persona fallecida lo hubiese
   prohibido expresamente o así lo establezca una ley. Esa prohibición no afecta al derecho de los herederos a acceder a
   los datos de carácter patrimonial del causante (art. 3.1 LOPDGDD).
   ```
   Source (`BOE-A-2018-16673_lopdgdd_2025-12-27.pdf`): art. 2.2.b) «A los tratamientos de datos de personas fallecidas,
   sin perjuicio de lo establecido en el artículo 3.»; art. 3.1 «Las personas vinculadas al fallecido por razones
   familiares o de hecho así como sus herederos podrán dirigirse al responsable o encargado del tratamiento al objeto de
   solicitar el acceso a los datos personales de aquella y, en su caso, su rectificación o supresión. Como excepción,
   las personas a las que se refiere el párrafo anterior no podrán acceder a los datos del causante, ni solicitar su
   rectificación o supresión, cuando la persona fallecida lo hubiese prohibido expresamente o así lo establezca una
   ley. Dicha prohibición no afectará al derecho de los herederos a acceder a los datos de carácter patrimonial del
   causante.» Option a (outside the law's scope) is answered by art. 2.2.b). Normativa: LOPDGDD «arts. 1, 5–7, …» →
   «arts. 1–3, 5–7, …». «Lo que más cae»: unchanged (one question, programa anterior).

2. **note** — section «Videovigilancia» (kept by scope). Exam row: conv2025_X P1 17 («¿En qué plazo serán suprimidos los
   datos tratados con fines de videovigilancia según … el artículo 22 de la Ley Orgánica 3/2018…?», key a). New, right
   after the heading:
   ```
   :::note{type=info}
   Fuera del enunciado literal del programa; preguntado en la convocatoria 2025 (llamamiento extraordinario), primera
   parte, pregunta 17.
   :::
   ```

3. **note** — section «Régimen sancionador» (kept by scope). Exam row: conv2025_X P1 18 («¿Cuál de las siguientes es una
   infracción considerada grave por el artículo 73 de la Ley Orgánica 3/2018…?», key a). New, right after the heading:
   ```
   :::note{type=info}
   Fuera del enunciado literal del programa; preguntado en la convocatoria 2025 (llamamiento extraordinario), primera
   parte, pregunta 18.
   :::
   ```

4. **coverage (precision)** — same section. `coverage/m02.md` notes that the lesson quoted only the first branch of
   art. 73.l); the spec forbids a cut clause inside a kept sentence. Exam row: conv2025_X P1 18 (option a is the whole
   letter).
   Old: «Entre las infracciones graves está la contratación por un encargado del tratamiento de otros encargados sin
   contar con la autorización previa del responsable (art. 73.l) LOPDGDD).»
   New: «Entre las infracciones graves está la contratación por un encargado del tratamiento de otros encargados sin
   contar con la autorización previa del responsable, o sin haberle informado sobre los cambios producidos en la
   subcontratación cuando fueran legalmente exigibles (art. 73.l) LOPDGDD).»
   Source (LOPDGDD, art. 73.l): «La contratación por un encargado del tratamiento de otros encargados sin contar con la
   autorización previa del responsable, o sin haberle informado sobre los cambios producidos en la subcontratación
   cuando fueran legalmente exigibles.»

5. **«Lo que más cae» check, art. 34.1.g) y l) LOPDGDD** — the letters are right: g) «Las entidades aseguradoras y
   reaseguradoras»; l) «Los centros sanitarios legalmente obligados al mantenimiento de las historias clínicas de los
   pacientes. Se exceptúan los profesionales de la salud que, aun estando legalmente obligados al mantenimiento de las
   historias clínicas de los pacientes, ejerzan su actividad a título individual.» The line, though, gave letter l)'s
   exception without letter l)'s entity, so it read as an exception to the insurers. Exam row: conv2025_X P1 reserva 1
   (key b, insurers; option c the health professionals).
   Old: «- Las entidades aseguradoras y reaseguradoras deben designar delegado de protección de datos en todo caso; los
   profesionales de la salud que ejercen su actividad a título individual están exceptuados (art. 34.1.g) y l)
   LOPDGDD).»
   New: «- Las entidades aseguradoras y reaseguradoras y los centros sanitarios legalmente obligados al mantenimiento de
   las historias clínicas de los pacientes deben designar delegado de protección de datos en todo caso; se exceptúan
   los profesionales de la salud que ejercen su actividad a título individual (art. 34.1.g) y l) LOPDGDD).»
   Same line count (ten).

## Cut items checked

The bloque II section of the ledger has no «Cuts» / «Cut for length» lists: each tema records only its first-draft size
(5,569 / 5,563 / 5,783 / 7,914 words) and the remark that «each writer cut first what no official question of
2022–2025 asks». The 2022–2025 rows are all covered after this round (coverage audit). So the check was done two ways:
(a) every item the ledger names as cut, omitted or not stated; (b) every bloque II row of conv2020 and conv2020_X, the
exams the R2 writers did not weigh (first tema II.1–II.4, from `docs/age-official-exams-ledger.md`), plus the annulled
conv2022 P1 41, read against the lessons.

(a) Items the ledger names:

| Item (ledger) | Exams searched | Verdict |
|---|---|---|
| m02-l01: LPAC articles dropped «after the cuts» | II.1 rows 2020–2025 (none needs LPAC beyond what m02-l02/m03 state) | not asked |
| m02-l01: art. 6.2.d) RD 208/1996 (Comisión Interministerial function) deleted | conv2024_A P1 15 names the Comisión only as a distractor (key a, art. 5.1, covered) | not asked |
| m02-l02: art. 13.3–13.4 RD 1708/2011 (Comisión de Archivos, «Ministerio de Presidencia») cut | grep «Comisión de Archivos»: no hit | not asked |
| m02-l02: criterios numérico, geográfico, temático omitted | grep «ordenación» (archival sense): no hit | not asked |
| m02-l02: plazos de transferencia in years (Decreto 914/1969) | grep «914/1969», transfer questions (conv2020 S2 7, covered) | not asked |
| m02-l02: further competences of art. 58 Ley 16/1985 | conv2020 P1 12 asks the AGA's functions (covered); nothing on art. 58 | not asked |
| m02-l03: «Observatorio de Accesibilidad Web» omitted | grep «Observatorio»: only igualdad (conv2020 P1, other tema) | not asked |
| m02-l03: «Lo que más cae» line on RD 1112/2018 as the regulating norm replaced | conv2022 P1 39 (key a RD 1112/2018): the lesson's opening paragraph still names it | not asked (fact still stated) |
| m02-l04: art. 34.1 LOPDGDD, ten of sixteen letters not named | conv2025_X P1R 1 asks g) and l) (stated) | not asked |
| m02-l04: exceptions of arts. 5.1.e), 17.3, 34.3 RGPD not stated | conv2022 P1 (rights list), conv2024_X P1 16, conv2025_A P1 15: all covered without them | not asked |
| conv2020_X P1 17 (old art. 13.1 RD 366/2007, versiones simplificadas) | ledger estado «norma modificada» | excluded by spec |

(b) conv2020 / conv2020_X / conv2022 P1 41 rows:

| Row | Asks | Verdict |
|---|---|---|
| conv2020 P1 8 | CIA: cursos with the INAP (art. 6.2.e) RD 208/1996) | covered |
| conv2020 P1 9 | constancia de presentación (art. 15.4 RD 951/2005) | covered |
| conv2020 P1 10 | telefonía de texto (art. 8.2.e) RD 366/2007) | covered |
| conv2020 P1 11 | asientos, orden temporal (art. 16.2 LPAC) | covered |
| conv2020 P1 12 | AGA applies Comisión Superior Calificadora resolutions (art. 11 RD 1708/2011) | covered |
| conv2020 P1 13 | archivo electrónico único (art. 55.1 RD 203/2021) | covered |
| conv2020 P1 14 | heirs' access to a deceased person's data (art. 3.1 LOPDGDD) | **restored** (m02-l04 #1) |
| conv2020 P1 40 | relación de oficinas (art. 16.7 LPAC), 14.3, 16.5, 31.2.a) | covered |
| conv2020 S1 1–3 | art. 16.4.a) LPAC; arts. 16.1, 16.3 RD 951/2005 | covered |
| conv2020 S2 7–8 | art. 9 RD 1708/2011 (transfer; documentos de apoyo) | covered |
| conv2020_X P1 15, 16, 18–21 | arts. 19 RD 951/2005; 10, 3.2, 2.2 RD 208/1996; 1.2 RD 366/2007; 11 RD 1708/2011 | covered |
| conv2020_X P1 22 | PAG, LPAC (arts. 13.a), 43.4, 53.1.a)) | key covered; option d **restored** (m02-l03 #2) |
| conv2020_X P1 23–24 | art. 39.1.e) RGPD; art. 44.1 LOPDGDD | covered |
| conv2020_X S1 7, S1R 2, S2 9 | arts. 15.2, 16.2 RD 951/2005; art. 7.a) RD 366/2007 | covered |
| conv2022 P1 41 (anulada) | RD 127/2015 arts. 1, 6; CIRCE | covered (options a–c stated) |

## New sources

None. No `normativa.yaml` entry needed.

## Glossary

No section removed; no glossary entry affected.

## Word counts (`wc -w`)

| Lesson | Before | After |
|---|---|---|
| m02-l01 | 3,491 | 3,510 |
| m02-l02 | 3,045 | 3,045 |
| m02-l03 | 3,460 | 3,583 |
| m02-l04 | 3,903 | 4,076 |
