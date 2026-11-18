# Build — I.7 (`m01-l07`), 2026-11-17

Builder: Sonnet. Method: pool structure (the R2d expansion) taken as the skeleton; every sentence kept is a HEAD
sentence or a pool sentence with a PASS verdict, byte-identical; lists that are legal enumerations became esquemas
(one row per sentence, citation = the lead-in's). Scratch scripts: `/tmp/claude-1000/-home-juanjo-PycharmProjects-curset/82b57970-32c9-4fcd-9a63-714f54d4eded/scratchpad/b-m01-l07/` (`build.py`, `post.py`, `finalize.py`,
`policy.py`). The previous working-tree lesson (the 62 803-word writers' version) is saved in the scratch
directory as `prev-worktree.md`.

## Size

| | words |
|---|---|
| HEAD (`wc -w`) | 17952 |
| HEAD, esquema rows excluded | 16556 (esquema rows 1371) |
| built, whole file | 47615 |
| built, esquema rows excluded (every `:::esquema` row, new and old) | 34187 |
| esquema rows only | 13428 |

Ratio excl. rows to HEAD (17952): 1.90. Ratio to the 1.6 target (28 723): 1.19. The target is passed by 19 %: the
range is 303 article rows (57 full, 98 part, 131 not treated in HEAD) and 87 enumerations (57 incomplete); every
added article is kept to the sentences the pool holds with a PASS verdict for its rule, conditions and exceptions
(the pool sentences left out are listed below), every enumeration is an esquema or an already complete HEAD list.

## Sentences added

Kept non-HEAD units: 872 (793 with a PASS verdict, byte-identical; 79 without one, listed under «not in pool»).
(a) 0 (R2b removed nothing from I.7: map, «R2b removals») · (b) 115 · (c) 748 · (d) 9 · (e) 32 HEAD sentences
replaced (their pool versions are counted in (b) and (c)).

- (b) review items the map confirmed: art. 14 TREBEP (all eighteen letters, 19 units), art. 37.1 and 37.2 (21), arts.
  52, 53 and 54 (29, the three lists whole), art. 87.1.f) whole (1), art. 87.3 second and third sentences and 87.4
  (4), arts. 2 and 3 RD 365/1995 (26: the eleven situaciones and the twelve supuestos), art. 2.1 TRLCPE whole (13),
  art. 4.2 RDL 1/2013 (2). The «entre otros/otras» of these items are gone; the ones left are the law's own words
  (art. 13, 17, 24, 85.2 TREBEP, art. 31.3 RDL 4/2000) or HEAD's art. 7 derogation note.
- (c) every other article of the ranges that HEAD did not treat or treated in part, as far as the pool holds PASS
  sentences: TREBEP 1, 2.2–4, 3–7, 11.2–3, 12, 13, 16.2, 16.4, 17–20, 21–28 (25.2 included), 31–36, 37, 38–45, 46.2,
  47, 47 bis, 48.e–f párr. 2, 50.3, 55–58, 59.2, 60, 61–71, 72–74, 78–81, 83–84, 85.2, 86.2, 88, 89, 90.3, 94–96,
  98.2–4, 99–100, DA 17.ª, DT 3.ª and DA 6.ª; RDL 6/2023 109–111, 116–127; Ley 30/1984 21; RD 364/1995 38–40, 41,
  42, 44–46, 47.2, 48.4, 49–52, 54–56, 61, 64–66, 68–70, 72–80; RD 365/1995 6–8, 10–13, 14–16, 18, 21–22; Ley 53/1984
  1–3, 5, 8, 10–16, 18, 20; RD 598/1985 6, 8–11, 13–17; RD 33/1986 18–19, 27–28, 31–33, 35, 37, 45, 48–51, DA 1.ª;
  RDL 4/2000 7–12, 15–32, 34, 37, DA 1.ª, DA 10.ª; RD 375/2003 6–13, 15–19, 22–29, 33, 41, 53–56, 88–101, 159–161;
  TRLCPE 2–3, 19, 21–30, 32–33, 35, 38–39, 41–42, 44–45, 47–48, 50; LGSS DA 3.ª.2 and 3.ª.4, DA 4.ª.
- (d) the three «No confundir» blocks (derechos individuales / colectivos; plazos de cese y toma de posesión; excedencia
  por interés particular / por cuidado de familiares): 9 units, three of them without a PASS verdict (see below).
- (e) HEAD sentences replaced by their pool version: the art. 14 lead and eight letters, the art. 37.1 and 37.2 leads,
  the art. 52, 53 and 54 leads and items, the art. 4.2 RDL 1/2013 sentence, the art. 3 RD 365/1995 lead, art. 87.1.f),
  the art. 29 Ley 30/1984 derogation sentence («entre otros»), the art. 16.1 Ley 53/1984 sentence, the arts. 8.1,
  19.1 RDL 4/2000 and 2.1, 38, 41 TRLCPE leads/rows (the «Entre otros» of the viudedad and orfandad rows), and the
  Normativa lines.
- HEAD sentences not carried: the two «Fuera del enunciado literal…» notes (coordinator note), the sentences just
  named under (e), and the HEAD Normativa lines (rebuilt). The two HEAD `kind=plazos` esquemas (Plazos del concurso,
  Plazos del expediente disciplinario) stay as HEAD has them: the pool's versions of their items carry no verdict.

## Enumerations as esquemas

66 esquemas in the built lesson (HEAD had 6 `tabla`/`plazos` ones, kept). Built from pool items by the
build script, one row per sentence under the item's marker, the citation of the lead-in:

- Principios del personal directivo
- Equivalencia de los Grupos anteriores a la Ley 7/2007
- Fundamentos de actuación del Estatuto
- Personal con legislación específica propia
- Causas de pérdida de la condición de funcionario de carrera
- Clases de jubilación
- Derechos individuales de los empleados públicos
- Retribuciones básicas
- Factores de las retribuciones complementarias
- Materias objeto de negociación
- Materias excluidas de la negociación
- Escala de miembros de la Junta de Personal
- Funciones de las Juntas y los Delegados de Personal
- Garantías de los representantes
- Promotores de las elecciones
- Normas del procedimiento electoral
- Principios éticos
- Principios de conducta
- Méritos del concurso
- Supuestos de puntuación específica en el concurso
- Funciones directivas profesionales
- Principios de actuación del personal directivo público profesional
- Requisitos del personal directivo público profesional
- Causas de cese del personal directivo público profesional
- Plazos del concurso
- Reglas de la carrera horizontal
- Fines de la evaluación del desempeño
- Criterios de la evaluación del desempeño
- Efectos de la evaluación del desempeño
- Elementos del sistema de acreditación de méritos de la carrera horizontal
- Grado personal y garantía del nivel en la Ley 30/1984
- Circunstancias que permiten otras situaciones administrativas
- Situaciones administrativas del RD 365/1995
- Supuestos de servicios especiales
- Servicios especiales según el RD 365/1995
- Causas de excedencia forzosa
- Efectos de algunas situaciones administrativas
- Duración de algunas situaciones administrativas
- Ámbito de la Ley 53/1984
- Actividades privadas incompatibles
- Principios de la potestad disciplinaria
- Circunstancias de las faltas graves
- Plazos del expediente disciplinario
- Supuestos especiales de afiliación
- Causas de baja como mutualista obligatorio
- Mutualistas
- Situaciones que mantienen el alta obligatoria
- Jubilados en alta obligatoria
- Contingencias protegidas
- Prestaciones del régimen especial
- Beneficiarios del mutualismo administrativo
- Requisitos de los beneficiarios
- Incompatibilidades de la condición de beneficiario
- Recursos económicos de la Mutualidad
- Contenido de la asistencia sanitaria
- Circunstancias de la incapacidad temporal
- Extinción del derecho a la incapacidad temporal
- Denegación, anulación o suspensión del derecho a la incapacidad temporal
- Extinción del derecho en el riesgo durante el embarazo y la lactancia natural
- Grados de incapacidad permanente
- Revisión directa de prestaciones
- Sanciones a los mutualistas y beneficiarios
- Ámbito personal de Clases Pasivas
- Personal cuyos derechos pasivos regula el título I
- Órgano que acuerda la jubilación o retiro
- Años de servicio efectivo al Estado

Lists kept as prose lists: HEAD lists that were already complete (art. 10.1 and 10.3 TREBEP, 85.1, 95.2, 96.1,
12.1, 19 Ley 53/1984, 6, 7.1, 8 RD 33/1986, 3 RDL 4/2000, 28.2 TRLCPE …) and the lists whose items each cite their
own article (the title IV and V indexes, the comisiones de servicios and the other RD 364/1995 rules). The
pool tables whose rows carry no verdict (arts. 122.3 RDL 6/2023, 21.1 Ley 30/1984, 85.2 TREBEP, 4 RD 365/1995, DA 1.ª.1
RDL 4/2000, 34 RDL 4/2000, 3.1, 28.3 and 32.1 TRLCPE) are kept as esquemas because dropping them leaves the
enumeration incomplete; their rows cite the lead-in's unit.

## Checks

- build_check: `m01-l07: HEAD 534 · added byte-identical 542 · esquema rows from items 322 · not in pool 85`
- cites.py: 1221 citations, 0 unresolved. `index_sources.py --course aeat-agentes-hacienda`: exit 0, no validation
  error naming the lesson (see the final message for the last run).
- split_paragraphs: 11 paragraphs split.
- Every esquema row's citation cell is covered by the prose (the course loader enforces it; it loaded).

## «not in pool» (85)

Kept only because dropping them breaks a complete enumeration or a pair, or because they are new «Normativa» lines:
- 63 pool-table rows and lead-ins (list above, from `build_check`): art. 63 TREBEP lead-in and items a), b), c), e)
  (d) matched a verified sentence); art. 122.3 RDL 6/2023 (lead-in and a)–c)); art. 21.1 Ley 30/1984 (lead-in and
  1.b), 1.c), 1.e), 1.f)); art. 85.2 TREBEP (lead-in, a), b)); art. 4 RD 365/1995 (lead-in and a)–n) without k),
  no current effect, as the map says); DA 1.ª.1 RDL 4/2000 (lead-in, a)–d)); art. 34 RDL 4/2000 (lead-in, a)–f));
  art. 3.1 TRLCPE (lead-in, a)–f)); art. 28.3 TRLCPE (lead-in, a)–g)); art. 32.1 TRLCPE (lead-in, a)–g)); art.
  160.1.c) RD 375/2003 (the «Las muy graves» row).
- 3 «No confundir» sentences without a verdict (art. 14 TREBEP and art. 15 TREBEP lines of the derechos block; art.
  48.1 RD 364/1995 line of the plazos block): the other half of each pair has a verdict, a block needs both.
- the new «Normativa» lines (TREBEP, Ley 30/1984, RD 364/1995, RD 365/1995, RDL 6/2023, RD 33/1986, Ley 53/1984,
  RD 598/1985, RDL 4/2000, RD 375/2003, RDL 670/1987, the cambio pendiente of the TRLCPE, LGSS, the closing «no
  figuran en `normativa.yaml`» line). Rebuilt from the citations of the built lesson; format of R2.

Full list: `r2d/m01-l07/verify-build.md` is written by the tool; the `not in pool` lines are in the scratch file
`/tmp/claude-1000/-home-juanjo-PycharmProjects-curset/82b57970-32c9-4fcd-9a63-714f54d4eded/scratchpad/b-m01-l07/bcheck.out`.

## Pool sentences left out (reason per sentence)

Left out because they state no rule, condition or exception (development, procedure, organisational detail,
repetition). Sentences without a PASS verdict are not listed here (see «Pool gaps»).

**Negotiation machinery of arts. 32–39 TREBEP (informing the unions, encargo, Mesas competences and process, constitution, reglamento, comisiones paritarias): procedure, not a rule, condition or exception of the article**

- En ese supuesto, las Administraciones Públicas deberán informar a las or… (art. 32.2 TREBEP)
- Las Administraciones Públicas podrán encargar el desarrollo de las activ… (art. 33.2 TREBEP)
- Dependiendo de las Mesas Generales de Negociación y por acuerdo de las m… (art. 34.4 TREBEP)
- La competencia de las Mesas Sectoriales se extenderá a los temas comunes… (art. 34.5 TREBEP)
- El proceso de negociación se abrirá, en cada Mesa, en la fecha que, de c… (art. 34.6 TREBEP)
- A falta de acuerdo, el proceso se iniciará en el plazo máximo de un mes … (art. 34.6 TREBEP)
- Ambas partes estarán obligadas a negociar bajo el principio de la buena … (art. 34.7 TREBEP)
- Las Mesas quedarán válidamente constituidas cuando, además de la represe… (art. 35.1 TREBEP)
- Las variaciones en la representatividad sindical serán acreditadas por l… (art. 35.2 TREBEP)
- Para la negociación de las materias y condiciones de trabajo comunes al … (art. 36.3 TREBEP)
- Se establecerán Comisiones Paritarias de seguimiento de los Pactos y Acu… (art. 38.5 TREBEP)
- El reglamento y sus modificaciones deberán ser aprobados por los votos f… (art. 39.6 TREBEP)

**Procedure or mechanics (who proposes, who coordinates, where it is filed, how it is proved, how the amount is computed or collected, what is communicated): not a rule, condition or exception**

- La Administración Pública competente deberá resolver de forma motivada l… (art. 67.3 TREBEP)
- La Secretaría de Estado para la Administración Pública, a iniciativa de … (art. 39 RD 364/1995)
- El Ministerio para las Administraciones Públicas coordina los concursos … (art. 40.2 RD 364/1995)
- La valoración de los méritos deberá efectuarse mediante puntuación obten… (art. 45.5 RD 364/1995)
- La propuesta de resolución deberá recaer sobre el candidato que haya obt… (art. 45.6 RD 364/1995)
- Las Comisiones propondrán al candidato que haya obtenido mayor puntuació… (art. 46.2 RD 364/1995)
- Recibido el parecer de la Junta de Personal, o transcurrido el plazo sin… (art. 50.4 RD 364/1995)
- Los requisitos, méritos y baremos de estos concursos se fijan previo acu… (art. 68.2 RD 364/1995)
- Los funcionarios seleccionados, una vez toman posesión de su nuevo puest… (art. 68.3 RD 364/1995)
- Si el que accede a un puesto público viniere realizando una actividad pr… (art. 13.3 RD 598/1985)
- Si sólo se trata de cambio de puesto de trabajo y existiere un anterior … (art. 13.4 RD 598/1985)
- El reconocimiento de compatibilidad para el ejercicio con carácter gener… (art. 12 RD 598/1985)
- Este requisito será indispensable, en el primer caso, para que puedan ac… (art. 18 Ley 53/1984)
- La abstención y la recusación se plantearán ante la Autoridad que acordó… (art. 32.3 RD 33/1986)
- El tiempo de permanencia en suspensión provisional será de abono para el… (art. 98.4 TREBEP)
- La condición de afiliado se acredita mediante el documento de afiliación… (art. 8 RD 375/2003)
- Si no se ejercita el derecho de opción en el plazo señalado o se pierde … (art. 10.4 RD 375/2003)
- Los funcionarios indicados en el apartado 3 del artículo 8 del RDL 4/200… (art. 10.6 RD 375/2003)
- Para determinar los derechos que puedan causar para sí o para sus famili… (art. 12.4 RD 375/2003)
- Los funcionarios en prácticas que no llegan a alcanzar la condición de f… (art. 13.2 RD 375/2003)
- El reconocimiento de la condición de beneficiario compete a la Mutualida… (art. 17.1 RD 375/2003)
- La petición de reconocimiento de la condición de beneficiario de los fam… (art. 17.2 RD 375/2003)
- Las variaciones de las circunstancias familiares que afectan al derecho … (art. 17.4 RD 375/2003)
- Si la variación conlleva la baja de un beneficiario, los gastos que se o… (art. 17.4 RD 375/2003)
- La Mutualidad General puede comprobar el grado de parentesco y demás cir… (art. 17.5 RD 375/2003)
- La condición de beneficiario a cargo de un mutualista se acredita median… (art. 18.1 RD 375/2003)
- En los casos de fallecimiento, separación, divorcio o nulidad de matrimo… (art. 18.2 RD 375/2003)
- Reglamentariamente se establecen los mecanismos necesarios para coordina… (art. 20.3 RDL 4/2000)
- Este examen determina si el estado de incapacitación del funcionario da … (art. 20.4 RDL 4/2000)
- El parte de baja se ajusta al modelo oficial que se establezca por Orden… (art. 89.2–3 RD 375/2003)
- La concesión o denegación de la licencia inicial o de sus posibles prórr… (art. 90.2 RD 375/2003)
- La duración de las sucesivas prórrogas de la licencia se vincula en requ… (art. 90.4 RD 375/2003)
- Si el resultado del reconocimiento no confirma la existencia de un proce… (art. 91.3 RD 375/2003)
- En estos casos, la Mutualidad General y los órganos de personal competen… (art. 93.3 RD 375/2003)
- El derecho a la prestación económica por incapacidad temporal se extingu… (art. 94.3 RD 375/2003)
- No se tienen en cuenta para el cálculo del subsidio, de acuerdo con su n… ()
- Con carácter general, y sin perjuicio de lo que se disponga para el cálc… (art. 97.3 RD 375/2003)
- Se aplican a efectos de incompatibilidades las prescripciones efectuadas… (art. 98.2 RD 375/2003)
- La acreditación del proceso patológico o período de observación puede se… (art. 89.4 RD 375/2003)
- La orden ministerial del artículo 89.2 establece los términos y plazos a… (art. 90.5 RD 375/2003)
- El cómputo de plazos de la duración máxima de la incapacidad temporal se… (art. 92.2 RD 375/2003)
- Las remuneraciones del artículo 94.1 se abonan con cargo a los mismos co… (art. 94.2 RD 375/2003)
- Si se lleva a efecto la encomienda de gestión del pago del subsidio, cor… (art. 97.2 RD 375/2003)
- La concesión y seguimiento de las licencias y de sus prórrogas a las mut… (art. 99.3 RD 375/2003)
- El derecho al reconocimiento de estas situaciones de riesgo puede ser de… (art. 100.2 RD 375/2003)
- Las reclamaciones previas, en asuntos civiles y laborales, serán resuelt… (art. 37.4 RDL 4/2000)
- En las prestaciones periódicas, el derecho al percibo de cada mensualida… (art. 54.2 RD 375/2003)
- No puede exigirse el reintegro de lo indebidamente percibido sin previa … (art. 55.4 RD 375/2003)
- La Mutualidad General puede reformar o modificar en cualquier tiempo, me… (art. 55.5 RD 375/2003)
- El carácter revisable, condicional o provisional de los actos debe const… (art. 55.5 RD 375/2003)
- La obligación de reintegro del importe de las prestaciones indebidamente… (art. 56 RD 375/2003)

**Organisational detail of RDL 6/2023 arts. 109–110, 123, 125, 127 (instruments, áreas funcionales, who holds the puestos, repertorio, directorio, formación, solicitudes): the map allows «organisational detail» for this in-doubt block**

- En ámbitos específicos pueden existir otros instrumentos de ordenación d… (art. 109.3 RDL 6/2023)
- Con carácter general, los puestos de trabajo están adscritos a una o var… (art. 110.3 RDL 6/2023)
- Los puestos de una misma área funcional pueden agruparse en función de s… (art. 110.4 RDL 6/2023)
- Tienen esa consideración las personas titulares de las subdirecciones ge… (art. 123.3 RDL 6/2023)
- En el ámbito de la Administración periférica, la tienen las personas tit… (art. 123.4 RDL 6/2023)
- Los puestos correspondientes a subdirecciones generales adjuntas y aquel… (art. 123.5 RDL 6/2023)
- El personal directivo público profesional del sector público institucion… (art. 123.6 RDL 6/2023)
- El departamento ministerial competente en materia de función pública dic… (art. 125.2 RDL 6/2023)
- En el ámbito de la Administración del Estado se relacionan en el reperto… (art. 125.3 RDL 6/2023)
- Para cada puesto de trabajo debe determinarse en el repertorio el perfil… (art. 125.3 RDL 6/2023)
- Corresponde al departamento ministerial con competencias en materia de f… (art. 125.3 RDL 6/2023)
- Se crea un directorio dependiente del departamento ministerial con compe… (art. 125.4 RDL 6/2023)
- El personal directivo y predirectivo debe participar en las actividades … (art. 125.5 RDL 6/2023)
- El plazo máximo de presentación de solicitudes es de diez días naturales… (art. 127.1 RDL 6/2023)
- Las convocatorias deben incluir los requisitos y las competencias a valo… (art. 127.1 RDL 6/2023)

**Development or repetition of a rule a kept sentence already states (evaluación del desempeño, funciones del RD 365/1995, cotización of RD 375/2003)**

- Serán objeto de negociación colectiva las normas que fijen los criterios… (art. 116.3 RDL 6/2023)
- La conducta profesional se valorará conforme al código de conducta estab… (art. 118.3 RDL 6/2023)
- Los resultados de la evaluación del desempeño serán de conocimiento por … (art. 119.3 RDL 6/2023)
- El complemento de desempeño es el que retribuye el rendimiento o resulta… (art. 119.4 RDL 6/2023)
- Las evaluaciones realizadas mediante dicho modelo no tendrán consecuenci… (art. 120.2 RDL 6/2023)
- Se entienden como puestos de similares características aquellos que guar… (art. 12.3 RD 365/1995)
- Corresponde a la Secretaría de Estado para la Administración Pública efe… (art. 12.4 RD 365/1995)
- Corresponde a la Secretaría de Estado para la Administración Pública aco… (art. 13.7 RD 365/1995)
- La declaración de excedencia forzosa prevista en la letra b) y, en su ca… (art. 13.7 RD 365/1995)
- La cotización de los mutualistas voluntarios retrotrae sus efectos al dí… (art. 24.3–4 RD 375/2003)
- La cotización es mensual para los mutualistas en alta y su devengo tiene… (art. 25.2 RD 375/2003)
- La cuota expresa el importe de la obligación de cotizar a la Mutualidad … (art. 25.1 RD 375/2003)
- El período de liquidación se refiere a mensualidades naturales completas… (art. 25.3 RD 375/2003)
- La base reguladora se reduce en la misma proporción que las retribucione… ()
- Las liquidaciones mensuales de los mutualistas en el mes en que causan a… ()
- Se toma como base de cotización de los funcionarios en prácticas que ya … ()
- Las habilitaciones u oficinas pagadoras retienen el importe de la cuota … (art. 27.3 RD 375/2003)
- Las cotizaciones por esos períodos se realizan desde la fecha en que se … (art. 27.5 RD 375/2003)
- El régimen singular consiste en el pago de las cuotas directamente por e… (art. 28.2 RD 375/2003)
- Las cuotas ingresadas fuera de plazo por los mutualistas que solicitan e… (art. 33.1 RD 375/2003)


## Pool gaps (article of the range with no PASS sentence)

The pool was verified in part: of its 1837 sentences, 934 have a PASS verdict, 3 FAIL and 900 none. The articles
below have no PASS sentence in the pool, so nothing of them is stated in the lesson (the pool's sentences for them,
if any, carry no verdict). Rows of the «After build» section of the map marked «pool gap»:

| arts. 2–3 RD 33/1986 | pool gap | no PASS sentence in the pool for RD 33/1986 |
| arts. 105, 123–127 RDL 6/2023 (directivo público profesional AGE) | treated (rule, conditions, exceptions) | pool gap: 105 (no PASS sentence) |
| art. 77 TREBEP | pool gap | no PASS sentence in the pool for TREBEP |
| arts. 26–29 TREBEP | treated (rule, conditions, exceptions) | pool gap: 29 (no PASS sentence) |
| art. 49 TREBEP | treated (HEAD table 49.a)–g)); pool gap for the sub-rules | no pool sentence for fallecimiento del hijo / de la madre, cursos de formación, inicio anticipado en adopción |
| art. 51 TREBEP | pool gap | no PASS sentence in the pool for TREBEP |
| DA 16.ª TREBEP | pool gap | no PASS sentence in the pool |
| art. 20 Ley 30/1984 | pool gap | no PASS sentence in the pool for Ley 30/1984 |
| art. 22 Ley 30/1984 | pool gap | no PASS sentence in the pool for Ley 30/1984 |
| art. 92 TREBEP | pool gap | no PASS sentence in the pool for TREBEP |
| art. 5 RD 365/1995 | pool gap | no PASS sentence in the pool for RD 365/1995 |
| art. 20 RD 365/1995 | pool gap | no PASS sentence in the pool for RD 365/1995 |
| art. 23 RD 365/1995 | pool gap | no PASS sentence in the pool for RD 365/1995 |
| DA 1.ª–2.ª RD 365/1995 | pool gap | no PASS sentence in the pool |
| DA 5.ª RD 365/1995 | pool gap | no PASS sentence in the pool |
| art. 4 Ley 53/1984 | pool gap | no PASS sentence in the pool for Ley 53/1984 |
| art. 6 Ley 53/1984 | pool gap | no PASS sentence in the pool for Ley 53/1984 |
| DA 1.ª, 9.ª Ley 53/1984 | pool gap | no PASS sentence in the pool |
| arts. 1–2 RD 598/1985 | pool gap | no PASS sentence in the pool for RD 598/1985 |
| arts. 3–4 RD 598/1985 | pool gap | no PASS sentence in the pool for RD 598/1985 |
| art. 12 RD 598/1985 | pool gap | no PASS sentence in the pool for RD 598/1985 |
| arts. 15–17 RD 598/1985 | treated (rule, conditions, exceptions) | pool gap: 16 (no PASS sentence) |
| arts. 1–4 RD 33/1986 | treated (rule, conditions, exceptions) | pool gap: 2, 3, 4 (no PASS sentence) |
| art. 5 RD 33/1986 | pool gap | no PASS sentence in the pool for RD 33/1986 |
| arts. 9–11 RD 33/1986 | pool gap | no PASS sentence in the pool for RD 33/1986 |
| arts. 12–13 RD 33/1986 | pool gap | no PASS sentence in the pool for RD 33/1986 |
| art. 22 RD 33/1986 | pool gap | no PASS sentence in the pool for RD 33/1986 |
| art. 24 RD 33/1986 | pool gap | no PASS sentence in the pool for RD 33/1986 |
| arts. 25–26 RD 33/1986 | pool gap | no PASS sentence in the pool for RD 33/1986 |
| art. 34 RD 33/1986 | pool gap | no PASS sentence in the pool for RD 33/1986 |
| arts. 38–40 RD 33/1986 | pool gap | no PASS sentence in the pool for RD 33/1986 |
| art. 44 RD 33/1986 | pool gap | no PASS sentence in the pool for RD 33/1986 |
| art. 46 RD 33/1986 | pool gap | no PASS sentence in the pool for RD 33/1986 |
| art. 1 RDL 4/2000 | pool gap | no PASS sentence in the pool for RDL 4/2000 |
| arts. 13–14 RDL 4/2000 | pool gap | no PASS sentence in the pool for RDL 4/2000 |
| arts. 23–28 RDL 4/2000 | treated (rule, conditions, exceptions) | pool gap: 28 (no PASS sentence) |
| arts. 33–36 RDL 4/2000 | treated (rule, conditions, exceptions) | pool gap: 33, 35, 36 (no PASS sentence) |
| RD 375/2003, asistencia sanitaria (arts. 65–87) | pool gap | no PASS sentence |
| RD 375/2003, incapacidad permanente y familia (arts. 102–128) | pool gap | no PASS sentence |
| RD 375/2003, servicios sociales y asistencia social (arts. 129–139) | pool gap | no PASS sentence |
| arts. 1, 3–4 TRLCPE | treated (rule, conditions, exceptions) | pool gap: 1, 4 (no PASS sentence) |
| arts. 5–17 TRLCPE | pool gap | no PASS sentence in the pool for TRLCPE |
| arts. 18–27 TRLCPE | treated (rule, conditions, exceptions) | pool gap: 18, 20 (no PASS sentence) |
| arts. 31–33 TRLCPE | treated (rule, conditions, exceptions) | pool gap: 31 (no PASS sentence) |
| arts. 34–37 bis TRLCPE | treated (rule, conditions, exceptions) | pool gap: 34, 36, 37 (no PASS sentence) |
| arts. 39–40 TRLCPE | treated (rule, conditions, exceptions) | pool gap: 40 (no PASS sentence) |
| arts. 42–43 TRLCPE | treated (rule, conditions, exceptions) | pool gap: 43 (no PASS sentence) |
| arts. 44–46 TRLCPE | treated (rule, conditions, exceptions) | pool gap: 46 (no PASS sentence) |
| arts. 47–50 TRLCPE | treated (rule, conditions, exceptions) | pool gap: 49 (no PASS sentence) |

Pool sentences without a PASS verdict that the build did not use (their citations; the sentences are in the pool and need the blind check before a rebuild can add them): (no citation: lead-in or heading sentence) ×10; art. 1 RD 598/1985; art. 1 RDL 4/2000; art. 1.1 TRLCPE; art. 1.2 TRLCPE; art. 10 RD 33/1986 ×2; art. 10 TRLCPE; art. 11.1 RD 33/1986; art. 11.1 TRLCPE; art. 11.2 RD 33/1986; art. 11.2 TRLCPE; art. 12 RD 33/1986; art. 12.1 TREBEP; art. 12.1–2 TRLCPE; art. 12.2 Ley 53/1984; art. 12.3 RDL 4/2000; art. 12.3–4 TRLCPE; art. 122.2 RDL 6/2023; art. 122.4 RDL 6/2023 ×2; art. 122.7 RDL 6/2023; art. 13 RD 33/1986; art. 13.1 RDL 4/2000; art. 13.1 TRLCPE; art. 13.2 RDL 4/2000; art. 14 Ley 53/1984; art. 14 RD 375/2003; art. 14 RDL 4/2000; art. 14.1 RD 365/1995; art. 14.1 TRLCPE; art. 14.2 TRLCPE; art. 14.3–4 RD 365/1995; art. 15 Ley 53/1984; art. 15.1 TRLCPE; art. 15.2 RD 365/1995; art. 15.2 RD 598/1985; art. 15.2 RDL 4/2000 ×2; art. 15.3 RDL 4/2000; art. 156.1–2 RD 375/2003; art. 157 RD 375/2003; art. 16 RD 33/1986; art. 16 RD 598/1985; art. 16.1 TRLCPE; art. 16.1–4 RD 365/1995; art. 16.2 TREBEP; art. 16.2 TRLCPE; art. 16.3 Ley 53/1984; art. 16.5–6 RD 365/1995; art. 162 RD 375/2003; art. 163 RD 375/2003; art. 17 TRLCPE; art. 17.2 RDL 4/2000; art. 18.1 TREBEP; art. 18.2 TRLCPE; art. 18.3 TREBEP; art. 18.4 TREBEP; art. 18.5 RD 365/1995; art. 2 RD 33/1986; art. 2 RD 598/1985; art. 2.2 TREBEP; art. 2.3 TREBEP; art. 2.4 TREBEP; art. 20.1 RDL 4/2000; art. 20.1 TRLCPE; art. 20.2 RD 365/1995; art. 20.2 RDL 4/2000; art. 20.2–3 Ley 30/1984; art. 20.5 TREBEP; art. 21.5 RD 365/1995; art. 22 RD 33/1986; art. 22.1 Ley 30/1984; art. 22.3 RD 365/1995; art. 22.3 RDL 4/2000; art. 23.2 RD 365/1995; art. 24 RD 33/1986 ×2; art. 25 RD 33/1986; art. 26 RD 33/1986; art. 28 RDL 4/2000; art. 28.1 TRLCPE; art. 29 TREBEP; art. 29.2 RD 33/1986; art. 3 RD 33/1986; art. 3 RD 598/1985; art. 3.2 Ley 53/1984 ×2; art. 3.2 TRLCPE; art. 3.3 TRLCPE; art. 30.2 TRLCPE ×2; art. 30.3 TRLCPE; art. 30.4 TRLCPE; art. 30.5 TRLCPE; art. 31.1 TRLCPE; art. 31.2 TRLCPE; art. 31.5 TRLCPE; art. 33.1 RDL 4/2000; art. 33.1 TRLCPE ×2; art. 33.2 RD 33/1986; art. 33.2 RDL 4/2000; art. 33.2 TRLCPE ×3; art. 33.3 TRLCPE; art. 33.4 TRLCPE; art. 34.1 RD 33/1986; art. 34.1–2 TRLCPE; art. 34.2 RD 33/1986 ×2; art. 35.1 RD 33/1986; art. 35.1 RDL 4/2000; art. 35.2 RD 33/1986 ×2; art. 35.2 RDL 4/2000; art. 35.3 RDL 4/2000; art. 36 RD 33/1986; art. 36 TRLCPE; art. 36.1 RDL 4/2000; art. 36.2 RDL 4/2000; art. 37 bis TRLCPE; art. 37.2 RD 33/1986; art. 38 RD 33/1986; art. 38.10 TREBEP; art. 38.2 TRLCPE; art. 38.6 TREBEP; art. 38.7 TREBEP; art. 39 RD 33/1986; art. 39.1 TRLCPE; art. 39.3 TRLCPE; art. 39.4 TRLCPE; art. 39.6 TREBEP; art. 4 RD 33/1986; art. 4 RD 375/2003; art. 4 RD 598/1985; art. 4.1 Ley 53/1984; art. 4.1 TRLCPE; art. 4.2 Ley 53/1984; art. 4.2 RD 364/1995; art. 4.2 RDL 1/2013; art. 4.2 TRLCPE; art. 4.2 y 4.4 Ley 53/1984; art. 4.3 Ley 53/1984; art. 40 RD 33/1986; art. 41 RD 33/1986; art. 41.1 RD 364/1995; art. 41.2 RD 364/1995; art. 41.3 RD 364/1995; art. 41.4 RD 364/1995; art. 42 RD 33/1986; art. 42.1 RD 364/1995; art. 42.3 TRLCPE; art. 42.4 TRLCPE; art. 42.6 TRLCPE; art. 42.7 TRLCPE; art. 42.8 TRLCPE; art. 42.9 TRLCPE; art. 43 TRLCPE; art. 44 RD 33/1986; art. 44.2 TRLCPE; art. 44.3 RD 364/1995; art. 45.1 RD 33/1986; art. 45.2 RD 33/1986; art. 45.2 RD 364/1995; art. 45.2 TREBEP; art. 45.2 TRLCPE; art. 45.3 RD 364/1995; art. 45.3 TREBEP; art. 45.4 RD 364/1995; art. 45.4 TREBEP; art. 45.4 TRLCPE; art. 46 RD 33/1986; art. 46.2 TREBEP; art. 47.2 RD 364/1995; art. 48.2 RD 33/1986; art. 48.3 RD 33/1986; art. 48.3 RD 364/1995; art. 5 RD 33/1986; art. 5 RD 365/1995; art. 5 RD 375/2003; art. 5 TRLCPE; art. 5.1 RDL 4/2000; art. 5.2 Ley 53/1984; art. 5.2 RDL 4/2000; art. 5.3 RDL 4/2000; art. 50 RD 33/1986; art. 51 RD 33/1986; art. 51.1 RD 364/1995; art. 54.1–2 RD 364/1995; art. 56.2 RD 364/1995; art. 59.1 RD 364/1995; art. 59.2 TREBEP; art. 6 RDL 4/2000; art. 6.1 Ley 53/1984; art. 6.1 TRLCPE; art. 6.2 TRLCPE; art. 60.1 RD 364/1995; art. 60.1 TREBEP; art. 60.2 RD 364/1995; art. 60.3 RD 364/1995; art. 60.3 TREBEP; art. 61.2 RD 364/1995; art. 64.3, 64.5 y 64.6 RD 364/1995; art. 7 TREBEP; art. 7.1 TRLCPE; art. 7.2 RD 33/1986; art. 7.2 RDL 4/2000; art. 7.2 TRLCPE; art. 7.3 RDL 4/2000 ×3; art. 70.10 RD 364/1995; art. 70.12 RD 364/1995; art. 70.4 RD 364/1995; art. 70.5 RD 364/1995; art. 72.2 RD 364/1995; art. 72.3 RD 364/1995; art. 77 TREBEP; art. 79.3 TREBEP; art. 8.1 Ley 53/1984; art. 8.1 RD 365/1995; art. 8.2 TRLCPE; art. 8.3 RDL 4/2000; art. 80.2 TREBEP; art. 80.3 TREBEP; art. 82.1 TREBEP; art. 82.2 TREBEP; art. 85.2 TREBEP; art. 86.2 TREBEP; art. 88.3 TREBEP; art. 88.4 TREBEP; art. 9 RD 33/1986; art. 9 TRLCPE; art. 9.1 RD 365/1995; art. 90.3 TREBEP; art. 92 TREBEP; art. 92.1 RD 375/2003; arts. 102 a 117 RD 375/2003; arts. 118 a 128 RD 375/2003; arts. 129 a 139 RD 375/2003; arts. 140 a 155 RD 375/2003; arts. 20 y 21 RD 375/2003; arts. 30 a 44 RD 375/2003; arts. 40 y 46 TRLCPE; arts. 45 a 64 RD 375/2003; arts. 65 a 87 RD 375/2003; disposición adicional decimosexta TREBEP; disposición adicional decimoséptima.1 TREBEP; disposición adicional decimoséptima.2 TREBEP; disposición adicional decimoséptima.3 TREBEP; disposición adicional decimoséptima.5 TREBEP; disposición adicional novena Ley 53/1984; disposición adicional primera Ley 53/1984; disposición adicional primera.3 RDL 4/2000; disposición adicional primera.4 RDL 4/2000; disposición adicional quinta RD 365/1995; nota del BOE al art. 23 Ley 30/1984

Also: art. 49 TREBEP sub-rules (fallecimiento del hijo / de la madre, cursos de formación, inicio anticipado en
adopción), art. 21.2.a)–c) Ley 30/1984 (the pool has the rows but no sentence citing 21.2 for them to hang from) and
the scale of art. 31.1 TRLCPE (its table rows have no verdict) are not stated.

## Sentences that do not stand on their own where they now sit

- The continuing rows of an esquema (one sentence per row under the item's marker): e.g. art. 13 TREBEP 4, 87.1 TREBEP
  items with a second sentence, 41.1 TREBEP d) and e), 124.1 RDL 6/2023, 159–161 RD 375/2003 items.
- Prose sentences that open on a reference to the previous one: «En todo caso, tendrá carácter voluntario…» (47 bis.3
  TREBEP), «A estos efectos se podrá prever la creación…» (54.10), «De no solicitarse el reingreso…» (84.3), «En tal
  supuesto los funcionarios continúan percibiendo…» (66.2 RD 364/1995), «Asimismo, cuando presten servicios en
  puestos de niveles…» (3.d RD 365/1995), «En todo caso les son aplicables…» (11.2 RD 365/1995), «En cualquier
  caso, el desempeño de un puesto…» (1.3 Ley 53/1984), «Dicha notificación…» and «También deberá efectuarse…» (DA 1.ª
  RD 33/1986), «Asimismo, se encontrarán en situación de incapacidad temporal…» (19.1 RDL 4/2000), «También puede ser
  suspendido…» (93.2 RD 375/2003), «Esos servicios y auxilios…» (31.2 RDL 4/2000), «Este ámbito personal…» (2.2
  TRLCPE), «También tendrán derecho a la pensión de viudedad…» (38.4 TRLCPE).
- «Estas normas regulan el tema:» (HEAD opening).

## New Normativa lines

All lines of the section are new (rebuilt from the citations of the built lesson, `r2d` format: article.apartado,
ranges with «–», «y …» before the last). Ancillary lines (nombradas / citadas en …, Cambio pendiente, CE) are the
pool's or HEAD's wording, kept only for norms the built lesson names.
