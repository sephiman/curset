# R2b fixes — bloque IV (m04), writer report (2026-10-17)

Spec: `spec.md` (this folder). Inputs: `coverage/m04.md`, `scope/m04.md`, the bloque IV section of
`docs/age-theory-ledger.md`. Sources read with `pdftotext -layout` from `content/age-administrativo-c1/sources/normativa/`.
Questionnaires searched: every `*cuestionario.txt` in `SP/exams/` (conv2020, conv2020_X, conv2022, conv2022_X,
conv2024_A, conv2024_X, conv2025_A, conv2025_X; modelo B repeats A). Nothing committed. No `:::note` added: the scope
audit has no «unmapped-keep» section in bloque IV.

## m04-l03

1. **removal** — section «Cuerpos y escalas» (### under «El personal funcionario al servicio de las Administraciones
   públicas»), heading and both paragraphs, deleted (scope verdict: remove; no 2020–2025 question). It alone cited
   art. 75.2 TREBEP, art. 26 Ley 30/1984 and its BOE note, and art. 22.2 RD 829/2023. Normativa: «75.2» dropped from the
   TREBEP line; the line «Ley 30/1984 (reforma de la Función Pública): art. 26 y su nota del BOE.» deleted; RD 829/2023
   line changed (see 3). Disposición final cuarta.2 TREBEP stays (still quoted in «Sistemas selectivos»). No «Lo que más
   cae» line rested on it. No cross-reference in any lesson pointed to it (`grep -rn` of the course).
2. **removal (intro)** — the intro paragraph named Ley 30/1984, now cited nowhere in the lesson.
   Old: «Estado (RD 364/1995). Siguen vigentes preceptos de la Ley 30/1984, de 2 de agosto, de medidas para la reforma
   de la Función Pública (Ley 30/1984).» New: «Estado (RD 364/1995).»
3. **coverage** — conv2025_A Sup. I reserva 3 (appointing organ, promoción interna). «(hoy: …)» per the standing
   convention, at the first mention (art. 27.1) and at the asked sentence (art. 25.1), plus one paragraph from the
   structure decrees.
   - «Selección de los interinos». Old: «…dependientes de la Secretaría de Estado para la Administración Pública. El
     procedimiento debe posibilitar la máxima agilidad en la selección (art. 27.1 RD 364/1995).» New: «…dependientes de
     la Secretaría de Estado para la Administración Pública (hoy: Secretaría de Estado de Función Pública). El
     procedimiento debe posibilitar la máxima agilidad en la selección (art. 27.1 RD 364/1995; art. 22.3.c) Real Decreto
     829/2023, de 20 de noviembre, por el que se reestructuran los departamentos ministeriales).»
   - «Nombramiento». Old: «…son nombrados funcionarios de carrera por el Secretario de Estado para la Administración
     Pública. Cualquier resolución…» New: «…son nombrados funcionarios de carrera por el Secretario de Estado para la
     Administración Pública (hoy: titular de la Secretaría de Estado de Función Pública). Cualquier resolución…» (the
     rest of the paragraph unchanged, rewrapped). New paragraph after it: «La Secretaría de Estado de Función Pública es
     un órgano superior del Ministerio para la Transformación Digital y de la Función Pública (art. 22.3.c) RD 829/2023).
     De ella dependen la Dirección General de Función Pública, con rango de subsecretaría, y la Dirección General de
     Gobernanza Pública (art. 21.C) Real Decreto 1009/2023, de 5 de diciembre, por el que se establece la estructura
     orgánica básica de los departamentos ministeriales).»
   - Sources: RD 364/1995 art. 25.1 «…serán nombrados funcionarios de carrera mediante resolución del Secretario de
     Estado para la Administración Pública…» (`BOE-A-1995-8729_…pdf`); RD 829/2023 art. 22.2 «Asimismo corresponde al
     Ministerio para la Transformación Digital y de la Función Pública la propuesta y ejecución de la política del
     Gobierno en materia de administración pública, función pública, y gobernanza pública.» and 22.3 «c) La Secretaría
     de Estado de Función Pública.» (`BOE-A-2023-23537_…pdf`); RD 1009/2023 art. 21 «C) La Secretaría de Estado de
     Función Pública, de la que dependen la Dirección General de Función Pública, con rango de subsecretaría, y la
     Dirección General de Gobernanza Pública.» (`BOE-A-2023-24842_…pdf`).
   - «Lo que más cae». Old: «- Los funcionarios de carrera los nombra el Secretario de Estado para la Administración
     Pública (art. 25.1 RD 364/1995).» New: «- Los funcionarios de carrera los nombra el Secretario de Estado para la
     Administración Pública, hoy titular de la Secretaría de Estado de Función Pública (art. 25.1 RD 364/1995; art.
     22.3.c) RD 829/2023).»
   - Normativa: «RD 829/2023 (departamentos ministeriales): art. 22.3.c).» (was 22.2); new line «RD 1009/2023 (estructura
     orgánica básica): art. 21.C).» (label as in m04-l01).

## m04-l04

4. **coverage** — conv2022_X Sup. II 9 (spouse in a private company). «Excedencia voluntaria por agrupación familiar».
   Old: «Puede concederse sin el periodo mínimo de servicios a quien tenga el cónyuge en otra localidad por desempeñar un
   puesto definitivo como funcionario de carrera o laboral fijo en cualquier Administración Pública o sus entidades,
   entre otros empleadores que enumera el artículo. No se devengan…» New: «Puede concederse sin el periodo mínimo de
   servicios a los funcionarios cuyo cónyuge resida en otra localidad por haber obtenido y estar desempeñando un puesto
   de trabajo de carácter definitivo como funcionario de carrera o como laboral fijo en cualquiera de las
   Administraciones Públicas, organismos públicos y entidades de derecho público dependientes o vinculados a ellas, en
   los Órganos Constitucionales o del Poder Judicial y órganos similares de las comunidades autónomas, así como en la
   Unión Europea o en organizaciones internacionales (art. 89.3 TREBEP). El artículo no menciona otros empleadores: el
   puesto del cónyuge en una empresa privada no da lugar a esta excedencia. No se devengan…» Source: TREBEP art. 89.3,
   first paragraph, quoted above almost verbatim (`BOE-A-2015-11719_trebep_2026-10-03.pdf`). Normativa unchanged (89.3
   already cited).

## m04-l05

5. **coverage** — conv2025_X Sup. II 8 and 9 (art. 30 TREBEP). New paragraph in «Derechos», after the art. 15 sentence:
   «Sin perjuicio de la sanción disciplinaria que pueda corresponder, la parte de jornada no realizada da lugar a la
   deducción proporcional de haberes, que no tiene carácter sancionador (art. 30.1 TREBEP). Quienes ejercen el derecho
   de huelga no devengan ni perciben las retribuciones del tiempo en que han permanecido en esa situación. La deducción
   de haberes no tiene carácter de sanción ni afecta al régimen respectivo de sus prestaciones sociales (art. 30.2
   TREBEP).» Source: art. 30.1 «Sin perjuicio de la sanción disciplinaria que pueda corresponder, la parte de jornada no
   realizada dará lugar a la deducción proporcional de haberes, que no tendrá carácter sancionador.»; art. 30.2 «Quienes
   ejerciten el derecho de huelga no devengarán ni percibirán las retribuciones correspondientes al tiempo en que hayan
   permanecido en esa situación sin que la deducción de haberes que se efectúe tenga carácter de sanción, ni afecte al
   régimen respectivo de sus prestaciones sociales.» m05-l04 still states it too; m04-l05 already points there.
6. **coverage (disputed key)** — conv2024_X Sup. II reserva 1 (art. 46 TREBEP). New paragraph after 5: «Están
   legitimados para convocar una reunión, además de las organizaciones sindicales, directamente o a través de los
   Delegados Sindicales, los Delegados de Personal, las Juntas de Personal, los Comités de Empresa y los empleados
   públicos de las Administraciones respectivas en número no inferior al 40 por 100 del colectivo convocado (art. 46.1
   TREBEP).» Source: art. 46.1 «Están legitimados para convocar una reunión, además de las organizaciones sindicales,
   directamente o a través de los Delegados Sindicales: a) Los Delegados de Personal. b) Las Juntas de Personal. c) Los
   Comités de Empresa. d) Los empleados públicos de las Administraciones respectivas en número no inferior al 40 por 100
   del colectivo convocado.» The norm's list only; the key is not followed.
7. **restore** — remoción (art. 50.1 and 50.5 RD 364/1995), asked by conv2020 Sup. I 16 (after remoción the
   Administración assigns a post by adscripción provisional, key d). New paragraph at the end of «Concurso»: «Quien accede
   a un puesto por concurso puede ser removido por causas sobrevenidas, derivadas de una alteración en el contenido del
   puesto, realizada a través de las relaciones de puestos de trabajo, que modifique los supuestos que sirvieron de base
   a la convocatoria, o de una falta de capacidad para su desempeño manifestada por rendimiento insuficiente, que no
   comporte inhibición y que impida realizar con eficacia las funciones atribuidas al puesto. En los supuestos de los
   artículos 42.3 y 74.2 de la Ley de Régimen Jurídico de las Administraciones Públicas y del Procedimiento
   Administrativo Común no se puede formular propuesta de remoción en tanto no quede establecida la ausencia de
   responsabilidad disciplinaria del funcionario, y sólo cuando la causa del incumplimiento le sea imputable (art. 50.1
   RD 364/1995). Al removido se le atribuye el desempeño provisional de un puesto de su Cuerpo o Escala, en el mismo
   municipio, no inferior en más de dos niveles al de su grado personal, en tanto no obtenga otro con carácter
   definitivo, con efectos del día siguiente al de la fecha del cese y de acuerdo con el procedimiento que fije el
   Ministerio para las Administraciones Públicas (hoy: Ministerio para la Transformación Digital y de la Función
   Pública) (art. 50.5 RD 364/1995; art. 22.2 Real Decreto 829/2023, de 20 de noviembre, por el que se reestructuran los
   departamentos ministeriales).» Source: art. 50.1 (both paragraphs) and 50.5 RD 364/1995, e.g. 50.5 «A los
   funcionarios removidos se les atribuirá el desempeño provisional de un puesto correspondiente a su Cuerpo o Escala,
   en el mismo municipio, no inferior en más de dos niveles al de su grado personal, en tanto no obtengan otro con
   carácter definitivo, con efectos del día siguiente al de la fecha del cese y de acuerdo con el procedimiento que fije
   el Ministerio para las Administraciones Públicas.» The procedure of 50.2–50.4 (diez días hábiles) is not asked and
   stays out.
8. **restore** — art. 51.2 RD 364/1995, used in conv2022_X Sup. II 19 option a) («Sí, al ser un puesto que se cubre por
   el procedimiento de libre designación», Subdirector General; key b) and in the stem of conv2025_A Sup. I 19. New
   paragraph in «Libre designación» after art. 80.1: «Sólo pueden cubrirse por este sistema los puestos de Subdirector
   general, Delegados y Directores territoriales, provinciales o Comisionados de los Departamentos ministeriales, de sus
   Organismos autónomos y de las Entidades Gestoras y Servicios Comunes de la Seguridad Social, Secretarías de Altos
   Cargos de la Administración y aquellos otros de carácter directivo o de especial responsabilidad para los que así se
   determine en las relaciones de puestos de trabajo (art. 51.2 RD 364/1995).» Source: art. 51.2, verbatim.
9. **restore** — art. 58.2 RD 364/1995, asked by conv2020_X Sup. I reserva 5 (cesado Subdirector General with grado 26,
   key d «no inferior a 24»). New paragraph after the cese sentence in «Libre designación»: «El funcionario cesado en un
   puesto de libre designación queda adscrito provisionalmente a un puesto de su Cuerpo o Escala no inferior en más de
   dos niveles al de su grado personal en el mismo municipio, en tanto no obtenga otro con carácter definitivo, con
   efectos del día siguiente al de la fecha del cese y de acuerdo con el procedimiento que fije el Ministerio para las
   Administraciones Públicas. El requisito del mismo municipio no se aplica al cese de funcionarios destinados en el
   exterior (art. 58.2 RD 364/1995).» Source: art. 58.2, both paragraphs.
10. **restore** — vacaciones worked example, asked by conv2025_A Sup. I reserva 1 (vacaciones of 2026 not taken because
    of a permiso por nacimiento: «Hasta junio de 2028»). Appended to the art. 50.2 paragraph: «Si una de esas situaciones
    impide iniciar en 2026 las vacaciones de ese año, pueden disfrutarse hasta el 30 de junio de 2028, dieciocho meses
    después del final de 2026.» Source: art. 50.2 TREBEP «…siempre que no hayan transcurrido más de dieciocho meses a
    partir del final del año en que se hayan originado.» (31-12-2026 + 18 months = 30-06-2028). Note for the exams
    ledger: art. 50.2 names the «permiso de maternidad», the stem a father's permiso por nacimiento.
11. **restore** — art. 54 TREBEP bullets used as the three distractors of conv2024_A P1 30 (a) = 54.2, c) = 54.5,
    d) = 54.11). Old: «Entre los principios de conducta está mantener actualizada su formación y cualificación (art. 54.8
    TREBEP). Las instrucciones y órdenes profesionales de los superiores se obedecen, salvo que constituyan una infracción
    manifiesta del ordenamiento jurídico; en ese caso se ponen inmediatamente en conocimiento de los órganos de
    inspección procedentes (art. 54.3 TREBEP).» New: «Entre los principios de conducta están estos (art. 54 TREBEP):» and
    the list «- Desempeñan las tareas de su puesto de trabajo de forma diligente y cumpliendo la jornada y el horario
    establecidos (art. 54.2 TREBEP).», the 54.3 sentence unchanged as a bullet, «- Administran los recursos y bienes
    públicos con austeridad y no los utilizan en provecho propio o de personas allegadas. Tienen, asimismo, el deber de
    velar por su conservación (art. 54.5 TREBEP).», «- Mantienen actualizada su formación y cualificación (art. 54.8
    TREBEP).», «- Garantizan la atención al ciudadano en la lengua que lo solicite siempre que sea oficial en el
    territorio (art. 54.11 TREBEP).» Source: art. 54.2, 54.3, 54.5, 54.8, 54.11 TREBEP.
12. **«Lo que más cae»** — art. 30 is asked twice (conv2025_X Sup. II 8 and 9). The block was full (10). Replaced
    «- El concurso se resuelve en dos meses desde el día siguiente al de la finalización del plazo de solicitudes, salvo
    que la convocatoria fije otro (art. 47.1 RD 364/1995).» (asked once, conv2020_X Sup. I reserva 1, programa anterior;
    the fact stays in the text) by «- La parte de jornada no realizada, y el tiempo de huelga, dan lugar a una deducción
    de haberes que no tiene carácter sancionador; la de huelga no afecta al régimen de prestaciones sociales (art.
    30.1–2 TREBEP).»
13. **Normativa** — TREBEP: added 30.1–2, 46.1, 54.2, 54.5, 54.11 («…, 53.7, 54.2–3, 54.5, 54.8, 54.11, 80.1, 80.4 y
    82.1»; line rewrapped). RD 364/1995: added 50.1, 50.5, 51.2, 58.2 («…48.1–3, 50.1, 50.5, 51.2, 53, 54.1, 56.1, 57,
    58.1–2, …»). New line «RD 829/2023 (departamentos ministeriales): art. 22.2.»

## m04-l07

14. **coverage** — conv2022 P1 32 (year MUFACE was created as single compulsory body: 1975). New source saved (see
    below). New paragraph in «Régimen especial y mecanismos de cobertura», after the art. 2.1 sentence: «La Ley 29/1975
    creó una Mutualidad General única para todos los funcionarios de carrera de la Administración Civil del Estado
    (preámbulo Ley 29/1975). Todos los funcionarios de carrera de la Administración Civil del Estado en situación de
    activo, excedencia especial, excedencia forzosa, supernumerario y suspensión de funciones, y los demás incluidos
    obligatoriamente en su campo de aplicación, quedaban obligatoriamente incorporados, como mutualistas, a la Mutualidad
    General de Funcionarios Civiles del Estado (arts. tercero.uno y diez.uno Ley 29/1975). El RDL 4/2000 derogó la Ley
    29/1975 en su totalidad (disposición derogatoria única a).1 RDL 4/2000).» Sources: Ley 29/1975 preámbulo, apartado
    «Cinco. La nueva Ley crea una Mutualidad General única para todos los funcionarios de carrera de la Administración
    Civil del Estado.»; art. tercero.uno «Quedan obligatoriamente incluidos en el campo de aplicación de este Régimen
    Especial: a) Los funcionarios de carrera de la Administración Civil del Estado. b) Los funcionarios en prácticas…
    c) Los funcionarios interinos…»; art. diez.uno «Todos los funcionarios de carrera de la Administración Civil del
    Estado en situación de activo, excedencia especial excedencia forzosa, supernumerario y suspensión de funciones, y
    los demás comprendidos en el artículo tercero, uno, serán obligatoriamente incorporados, como mutualistas, a la
    Mutualidad General de Funcionarios Civiles del Estado.» (`BOE-A-1975-13887_…pdf`, original text, BOE 30-06-1975);
    RDL 4/2000 DD única «a) En su totalidad: 1. La Ley 29/1975, de 27 de junio, sobre Seguridad Social de los
    Funcionarios Civiles del Estado…» (`BOE-A-2000-12140_trlssfce_2024-12-21.pdf`).
15. **«Lo que más cae»** — Old: «- El régimen especial lo estableció la Ley 29/1975, de 27 de junio (preámbulo RDL
    4/2000).» New: «- El régimen especial lo estableció la Ley 29/1975, de 27 de junio (preámbulo RDL 4/2000), que creó
    una Mutualidad General única para todos los funcionarios de carrera de la Administración Civil del Estado (preámbulo
    Ley 29/1975).» Still 8 lines.
16. **Normativa** — RDL 4/2000 line adds «disposición derogatoria única a).1»; new line «Ley 29/1975 (Seguridad Social
    de los Funcionarios Civiles del Estado; derogada): preámbulo; arts. tercero.uno y diez.uno.»

## m04-l08

17. **removal** — section «Vigencia» (### under «El IV Convenio único…»), heading and paragraph, deleted (scope verdict:
    remove; no question). It alone cited art. 3.1–3 Convenio único: «3.1–3» dropped from the Convenio line. No «Lo que
    más cae» line or cross-reference rested on it.
18. **coverage (disputed key)** — conv2024_X Sup. II 19 (crédito horario, up to 200 workers). New paragraph and table in
    «Derechos y deberes», after the art. 4.1 ET paragraph: «Los miembros del comité de empresa y los delegados de
    personal, a salvo de lo que dispongan los convenios colectivos, tienen cada uno un crédito de horas mensuales
    retribuidas en cada centro de trabajo para el ejercicio de sus funciones de representación, según esta escala (art.
    68.e) ET):» table «Hasta cien | Quince; De ciento uno a doscientos cincuenta | Veinte; De doscientos cincuenta y uno a
    quinientos | Treinta; De quinientos uno a setecientos cincuenta | Treinta y cinco; De setecientos cincuenta y uno en
    adelante | Cuarenta», then «El Convenio único fija la misma escala para los miembros de los Comités de Empresa y los
    Delegados y Delegadas de Personal (art. 86.1.d) Convenio único).» Sources: ET art. 68 opening («…tendrán, a salvo de
    lo que se disponga en los convenios colectivos, las siguientes garantías:») and 68.e) («Disponer de un crédito de
    horas mensuales retribuidas cada uno de los miembros del comité o delegado de personal en cada centro de trabajo…
    1.º Hasta cien trabajadores, quince horas. 2.º De ciento uno a doscientos cincuenta trabajadores, veinte horas. 3.º
    De doscientos cincuenta y uno a quinientos trabajadores, treinta horas. 4.º De quinientos uno a setecientos cincuenta
    trabajadores, treinta y cinco horas. 5.º De setecientos cincuenta y uno en adelante, cuarenta horas.»)
    (`BOE-A-2015-11430_et_2026-10-03.pdf`); Convenio art. 86.1.d) same five steps (`BOE-A-2019-7414_…pdf`). The norm's
    scale only; the key is not followed.
19. **coverage** — conv2022_X P1 15 (complemento personal de encuadramiento, key c). New paragraph at the end of «Sistema
    de clasificación»: «El Convenio único asigna un complemento personal de encuadramiento al personal que, a su entrada
    en vigor, prestaba servicios en puestos de los anteriores grupos profesionales 3, 4 y 5 cuando, de acuerdo con su
    anexo I, quedan encuadrados en los nuevos grupos E2, E1 y E0 respectivamente. Su finalidad es mantener en su
    totalidad el nivel retributivo de ese personal y adecuar la clasificación profesional y el encuadramiento en los
    nuevos grupos. Tiene carácter personal y deja de percibirse cuando se pasa a ocupar un puesto de distinto grupo
    profesional mediante alguno de los procedimientos del Convenio (disposición adicional tercera Convenio único). Figura
    entre las otras retribuciones de carácter personal de la estructura retributiva (art. 56.1 Convenio único). Se
    actualiza anualmente, con efectos de 1 de enero, en el porcentaje de incremento general de retribuciones que se fije
    para todos los empleados públicos de la Administración General del Estado (art. 56.2 Convenio único; disposición
    adicional tercera Convenio único). Las retribuciones están en m05-l04.» Sources: Convenio DA 3.ª («Con la finalidad
    de mantener en su totalidad el nivel retributivo del personal incluido en el ámbito de aplicación del presente
    Convenio y adecuar la clasificación profesional y el encuadramiento en los nuevos grupos, se acuerda la asignación de
    un complemento personal de encuadramiento al personal que se encuentre prestando servicios a la entrada en vigor del
    presente Convenio en puestos de trabajo de los anteriores grupos profesionales 3, 4 y 5 en aquellos casos en que los
    mismos, de acuerdo con el anexo I del presente Convenio, quedan encuadrados en los nuevos grupos E2, E1 y E0
    respectivamente. Este complemento tiene carácter personal y dejará de percibirse cuando se pase a ocupar un puesto
    de trabajo de distinto grupo profesional mediante alguno de los procedimientos previstos en el presente Convenio.
    Asimismo, este complemento se actualizará anualmente en los términos previstos en el punto 2 del artículo 56…»);
    art. 56.1.C).5 («Complemento personal de encuadramiento.») and 56.2. The Convenio does not use the word «novedad»;
    the lesson states what it creates and for whom.
20. **Normativa** — ET: «arts. 4.1, 5, 15.1, 34.1, 35.1 y 68.e).» Convenio: «arts. 1.1–2, 2, 7.1, 7.3–6, 8.1, 8.4, 10.1,
    11, 27.1–2, 29, 31.1–4, 32.1, 33.1, 56.1–2, 64.1, 64.3, 64.5, 70, 72.1–3, 73.1, 86.1.d) y 92; disposiciones
    adicionales tercera y undécima; disposición transitoria tercera.» «Lo que más cae» unchanged (each new fact asked
    once).

## m04-l09

21. **restore (pointer)** — the cut pointer to the Convenio complement, asked by conv2022_X P1 33 (ledger IV.8 o IV.9:
    Administración complements the Seguridad Social benefit to 100 %). New last paragraph of «Incapacidad temporal»: «El
    complemento de la Administración General del Estado a su personal laboral hasta el 100 % del salario en la
    incapacidad temporal está en m04-l08.» (art. 70 Convenio único, stated in m04-l08). Worded without «Convenio» so
    that g-convenio (LRJSP sense, no `link_except` for m04-l09) does not link here.

## Cut items checked (bloque IV ledger: «Cut for length», «Cuts of note», «Cut», coordinator restorations)

| Lesson | Cut item | Verdict | Questions found |
|---|---|---|---|
| m04-l03 | DT 3.ª.2 TREBEP (Grupos A–E → A1–E) | not asked | conv2024_X P1 38 names grupos A and E under art. 23 Ley 30/1984 (sueldo ratio, V.4), not the equivalence |
| m04-l05 | méritos (art. 44 RD 364/1995) | not asked | conv2025_A Sup. II 17 asks the Comisión de Valoración's composición equilibrada (covered, LO 3/2007) |
| m04-l05 | concurso específico (art. 45) | not asked | — |
| m04-l05 | remoción (art. 50; 50.5 in the list) | **restored** (50.1, 50.5) | conv2020 Sup. I 16 |
| m04-l05 | arts. 47 and 47 bis TREBEP (jornada, teletrabajo) | not asked | conv2025_A Sup. II reserva 5 mentions teletrabajo in a contract question (III.6) |
| m04-l05 | art. 51.2 RD 364/1995 list | **restored** | conv2022_X Sup. II 19 option a); conv2025_A Sup. I 19 stem |
| m04-l05 | art. 58.2 RD 364/1995 | **restored** | conv2020_X Sup. I reserva 5 |
| m04-l05 | art. 74.1 RD 364/1995 | not asked | conv2024_X P1 27 is art. 4.1 (covered) |
| m04-l05 | arts. 78–79 RD 364/1995 | not asked | — |
| m04-l05 | art. 54 bullets other than 54.3 and 54.8 | **restored** 54.2, 54.5, 54.11; 54.1, 54.4, 54.6, 54.7, 54.9, 54.10 not asked | conv2024_A P1 30 (distractors a, c, d) |
| m04-l05 | art. 14 TREBEP letters not kept (b, d, e, h, i, j, l, m, o, q) | not asked | conv2024_X P1 29 uses only k) and p) as distractors, both already in the lesson |
| m04-l05 | vacaciones worked example | **restored** | conv2025_A Sup. I reserva 1 |
| m04-l07 | cotización, financiación | not asked | — |
| m04-l07 | nine-item prestaciones list (art. 12 RDL 4/2000) | not asked | — |
| m04-l07 | incapacidad permanente in MUFACE (art. 23), gran invalidez | not asked | conv2024_A Sup. I 15 asks the LGSS grados (m04-l09, covered) |
| m04-l07 | art. 28.2.a) TRLCPE prórroga | already restored (second blind pass) | — |
| m04-l09 | art. 155.1 LGSS | not asked | — |
| m04-l09 | corresponsabilidad en el cuidado del lactante (arts. 183–184) | not asked | — |
| m04-l09 | art. 195.1 LGSS | not asked | — |
| m04-l09 | desempleo duration scale (art. 269.1) | not asked | conv2022_X P1 9 asks art. 264 (covered) |
| m04-l09 | pointer to the Convenio complement in m04-l08 | **restored** | conv2022_X P1 33 |

Ledger lists for IV.1, IV.2, IV.4, IV.6 and IV.8 hold no cut items; the IV.5 and IV.6 coordinator restorations are in
the lessons.

## New source

Saved `content/age-administrativo-c1/sources/normativa/BOE-A-1975-13887_ley-29-1975-seguridad-social-funcionarios_1975-06-30.pdf`
(original text, BOE núm. 155, 30-06-1975, pp. 14171–14177; downloaded from
`https://www.boe.es/boe/dias/1975/06/30/pdfs/A14171-14177.pdf`; identifier from the BOE sumario API for 19750630;
sha256 `8817cca80eb175def197ce385b51e98788b6680f713bf2e826e91da9dcaa8c1f`). Repealed in full by RDL 4/2000 (DD única
a).1). Entry for `normativa.yaml`:

```yaml
- short: "Ley 29/1975 (Seguridad Social de los Funcionarios Civiles del Estado)"
  title: "Ley 29/1975, de 27 de junio, sobre Seguridad Social de los Funcionarios Civiles del Estado."
  boe_id: "BOE-A-1975-13887"
  url: "https://www.boe.es/buscar/doc.php?id=BOE-A-1975-13887"
  consolidated_as_of: "1975-06-30"
  temas: ["IV.7"]
  amended_2025_2026: null
  note: "Texto original (BOE 30-06-1975); derogada en su totalidad por el RDL 4/2000 (disposición derogatoria única a).1). Se guarda solo para la creación de la MUFACE como Mutualidad General única (preámbulo, apartado cinco; arts. tercero.uno y diez.uno), preguntada en conv2022 P1 32."
  unverified: false
  file: "sources/normativa/BOE-A-1975-13887_ley-29-1975-seguridad-social-funcionarios_1975-06-30.pdf"
  tags: []
  version_vigente:
    consolidated_as_of: "1975-06-30"
  cambios_pendientes: []
```

## Glossary

- Removals: neither removed section carried a glossary mark (`glossary-links.es.txt` has none in «Cuerpos y escalas»
  of m04-l03 or «Vigencia» of m04-l08), so no entry loses its second lesson. Nothing moves to the waiting list.
- New text that will move the goldens (coordinator regenerates): m04-l05 «Secretarías de Altos Cargos» (art. 51.2)
  should now link g-alto-cargo (match «altos cargos»; same sense); m04-l07 «mutualistas» now first occurs in the new
  Ley 29/1975 paragraph (g-mutualista, origin lesson). `lesson-refs.es.txt` gains m04-l08 → m05-l04 and m04-l09 →
  m04-l08.

## Word counts (`wc -w`)

| Lesson | Before | After |
|---|---|---|
| m04-l03 | 2,597 | 2,525 |
| m04-l04 | 3,995 | 4,057 |
| m04-l05 | 4,003 | 4,649 |
| m04-l07 | 2,439 | 2,574 |
| m04-l08 | 3,171 | 3,375 |
| m04-l09 | 2,401 | 2,426 |

m04-l01, m04-l02 and m04-l06 unchanged. Check run after the edits: `uv run pytest -k "glossary or registry or content
or pipeline" -m "not integration"` in `backend/`: 68 passed. Goldens not regenerated.

## Open for the coordinator

- m04-l05 still names the «Secretario de Estado para la Administración Pública» (arts. 48.2, 54.1) without «(hoy: …)»;
  not in this round's work list.
- conv2025_A Sup. I reserva 1: art. 50.2 TREBEP names the «permiso de maternidad»; the stem is a father's permiso por
  nacimiento (exams ledger).
