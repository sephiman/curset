# R2b fixes — bloque III (m03)

Writer: R2b fix round, 2026-10-17. Spec: `spec.md` (this folder). Coverage input: `../coverage/m03.md` and
`../coverage/m03-l03.md`, `../coverage/m03-l04.md`. Cut lists: `docs/age-theory-ledger.md`, bloque III (III.1–III.7
writer's notes). Nothing committed. Sources quoted from `content/age-administrativo-c1/sources/normativa/`
(`pdftotext -layout`): LPAC = `BOE-A-2015-10565_lpac_2024-11-06.pdf`, LRJSP = `BOE-A-2015-10566_lrjsp_2024-08-02.pdf`,
LCSP = `BOE-A-2017-12902_lcsp_2026-04-09.pdf`, CC = `BOE-A-1889-4763_codigo-civil_2025-01-03.pdf`. Exam questions
read in `SP/exams/` (questionnaires and definitive keys); tema and estado from `docs/age-official-exams-ledger.md`.

The exact old → new text of every change is the unified diff in the appendix at the end (one block per lesson).
Each numbered item below names its hunk by the new text's first words.

## m03-l01

1. **note** — section «El procedimiento de elaboración» (### heading). Added right after the heading:
   «:::note{type=info} Fuera del enunciado literal del programa; preguntado en la convocatoria 2025 (llamamiento
   extraordinario), primera parte, pregunta de reserva 4. :::». Question checked: conv2025_X P1 reserva 4 («De
   acuerdo con el artículo 26 de la Ley 50/1997 … ¿cuándo podrá prescindirse del trámite de consulta pública …?»,
   key d, tema III.1 (o I.5), vigente). The section states art. 26.2.e) Ley 50/1997 (aspectos parciales de una
   materia). No Normativa or «Lo que más cae» change.

## m03-l03

1. **coverage** — 2024 extr. S I res. 2; 2024 extr. S II 12. Section «Interesados y representación». Old: «(art. 5.6
   LPAC). La relación electrónica de los representantes está en m02-l03, el tema de la administración electrónica.»
   New: the art. 5.6 sentence kept, then a new paragraph «Las personas físicas podrán elegir en todo momento … (art.
   14.1 LPAC). Están obligados a relacionarse electrónicamente … quienes representen a un interesado que esté obligado
   … y los empleados de las Administraciones Públicas … (art. 14.2.d) y e) LPAC). La lista completa está en m02-l03, el
   tema de la administración electrónica.» Source (LPAC art. 14): «1. Las personas físicas podrán elegir en todo
   momento si se comunican con las Administraciones Públicas para el ejercicio de sus derechos y obligaciones a través
   de medios electrónicos o no, salvo que estén obligadas a relacionarse a través de medios electrónicos con las
   Administraciones Públicas.» «2. En todo caso, estarán obligados a relacionarse a través de medios electrónicos con
   las Administraciones Públicas para la realización de cualquier trámite de un procedimiento administrativo, al
   menos, los siguientes sujetos: […] d) Quienes representen a un interesado que esté obligado a relacionarse
   electrónicamente con la Administración. e) Los empleados de las Administraciones Públicas para los trámites y
   actuaciones que realicen con ellas por razón de su condición de empleado público, en la forma en que se determine
   reglamentariamente por cada Administración.» Art. 14.1 is added because res. 2 keys b (a representative of a
   non-obliged natural person is not obliged) and S II 12 option b quotes it.
2. **coverage** — 2025 extr. S I res. 5; 2024 extr. P1 res. 3. New subsection «### Registros y archivo» (heading words
   from the titles of LPAC arts. 16 «Registros» and 17 «Archivo de documentos») after «Interesados y representación»,
   two paragraphs: «Los registros electrónicos de todas y cada una de las Administraciones deberán ser plenamente
   interoperables … (art. 16.4 LPAC).» and «Los documentos electrónicos deberán conservarse … La eliminación de dichos
   documentos deberá ser autorizada de acuerdo a lo dispuesto en la normativa aplicable (art. 17.2 LPAC).» Source
   (LPAC art. 16.4, último párrafo): «Los registros electrónicos de todas y cada una de las Administraciones, deberán
   ser plenamente interoperables, de modo que se garantice su compatibilidad informática e interconexión, así como la
   transmisión telemática de los asientos registrales y de los documentos que se presenten en cualquiera de los
   registros.» (LPAC art. 17.2): «Los documentos electrónicos deberán conservarse en un formato que permita garantizar
   la autenticidad, integridad y conservación del documento, así como su consulta con independencia del tiempo
   transcurrido desde su emisión. Se asegurará en todo caso la posibilidad de trasladar los datos a otros formatos y
   soportes que garanticen el acceso desde diferentes aplicaciones. La eliminación de dichos documentos deberá ser
   autorizada de acuerdo a lo dispuesto en la normativa aplicable.»
3. **coverage + restore** — 2022 ord. S II 2; ledger III.3 cut «14.2 LRJSP». Section «Competencia», new last
   paragraph «El órgano que se estime incompetente … (art. 14.1 LRJSP). Los interesados que sean parte en el
   procedimiento podrán dirigirse al órgano que esté conociendo del asunto para que decline su competencia … También
   podrán dirigirse al órgano que estimen competente para que requiera de inhibición … (art. 14.2 LRJSP).» Source
   (LRJSP art. 14): «1. El órgano administrativo que se estime incompetente para la resolución de un asunto remitirá
   directamente las actuaciones al órgano que considere competente, debiendo notificar esta circunstancia a los
   interesados. 2. Los interesados que sean parte en el procedimiento podrán dirigirse al órgano que se encuentre
   conociendo de un asunto para que decline su competencia y remita las actuaciones al órgano competente. Asimismo,
   podrán dirigirse al órgano que estimen competente para que requiera de inhibición al que esté conociendo del
   asunto.» (14.1 answers option d of the same question.)
4. **coverage** — 2025 extr. S I 17 (partial); 2022 extr. S I res. 3 (partial). Section «Abstención y recusación»,
   new paragraph after the art. 23.2 list: «En la línea colateral se sube hasta el tronco común y después se baja hasta
   la persona con quien se hace la computación. El hermano dista dos grados del hermano, tres del tío y cuatro del
   primo hermano (art. 918 Código Civil). Un primo hermano está dentro del cuarto grado de consanguinidad de la letra
   b) (art. 23.2.b) LRJSP).» Source (CC art. 918, párrafo tercero): «En la colateral se sube hasta el tronco común y
   después se baja hasta la persona con quien se hace la computación. Por esto, el hermano dista dos grados del
   hermano, tres del tío, hermano de su padre o madre, cuatro del primo hermano y así en adelante.» The Código Civil is
   already in sources (no download).
5. **coverage + restore** — 2022 extr. S II 5 (coverage); cut item «30.1 LRJSP» of III.5, also asked in conv2020 S II 1
   and conv2020_X S II 6. New subsection «### Potestad sancionadora» (the LRJSP's own term, título preliminar, capítulo
   III) between «Abstención y recusación» and «Convenios»: «Las infracciones y sanciones prescribirán según lo
   dispuesto en las leyes que las establezcan. Si éstas no fijan plazos de prescripción, las infracciones muy graves
   prescribirán a los tres años, las graves a los dos años y las leves a los seis meses; las sanciones impuestas por
   faltas muy graves prescribirán a los tres años, las impuestas por faltas graves a los dos años y las impuestas por
   faltas leves al año (art. 30.1 LRJSP). Los principios de la potestad sancionadora están en m03-l05.» Source (LRJSP
   art. 30.1): «Las infracciones y sanciones prescribirán según lo dispuesto en las leyes que las establezcan. Si éstas
   no fijan plazos de prescripción, las infracciones muy graves prescribirán a los tres años, las graves a los dos años
   y las leves a los seis meses; las sanciones impuestas por faltas muy graves prescribirán a los tres años, las
   impuestas por faltas graves a los dos años y las impuestas por faltas leves al año.» New pointer to m03-l05.
6. **coverage** — 2025 ord. S II 14. Section «Convenios», new paragraph and list «Los convenios se extinguen … (art.
   51.1 LRJSP). Son causas de resolución (art. 51.2 LRJSP):» a)–e). Source (LRJSP art. 51): «1. Los convenios se
   extinguen por el cumplimiento de las actuaciones que constituyen su objeto o por incurrir en causa de resolución.
   2. Son causas de resolución: a) El transcurso del plazo de vigencia del convenio sin haberse acordado la prórroga
   del mismo. b) El acuerdo unánime de todos los firmantes. c) El incumplimiento de las obligaciones y compromisos
   asumidos por parte de alguno de los firmantes. En este caso, cualquiera de las partes podrá notificar a la parte
   incumplidora un requerimiento para que cumpla en un determinado plazo con las obligaciones o compromisos que se
   consideran incumplidos. Este requerimiento será comunicado al responsable del mecanismo de seguimiento, vigilancia y
   control de la ejecución del convenio y a las demás partes firmantes. Si trascurrido el plazo indicado en el
   requerimiento persistiera el incumplimiento, la parte que lo dirigió notificará a las partes firmantes la
   concurrencia de la causa de resolución y se entenderá resuelto el convenio. La resolución del convenio por esta
   causa podrá conllevar la indemnización de los perjuicios causados si así se hubiera previsto. d) Por decisión
   judicial declaratoria de la nulidad del convenio. e) Por cualquier otra causa distinta de las anteriores prevista en
   el convenio o en otras leyes.»
7. **coverage + restore** — 2025 extr. S II 19; ledger III.3 cut «53.1 LRJSP» (removed in the FAIL round, then cut).
   Section «Convenios»: «Dentro de los tres meses siguientes a la suscripción de cualquier convenio cuyos compromisos
   económicos asumidos superen los 600.000 euros, el convenio se remite electrónicamente al Tribunal de Cuentas u
   órgano externo de fiscalización de la Comunidad Autónoma, según corresponda (art. 53.1 LRJSP).» Source (LRJSP art.
   53.1): «Dentro de los tres meses siguientes a la suscripción de cualquier convenio cuyos compromisos económicos
   asumidos superen los 600.000 euros, estos deberán remitirse electrónicamente al Tribunal de Cuentas u órgano externo
   de fiscalización de la Comunidad Autónoma, según corresponda.»
8. **coverage** — 2025 extr. S II 7. Organismos públicos have no section in III.3; placed in «Convenios», the nearest
   LRJSP section: «Los estatutos de los organismos públicos se aprobarán por Real Decreto del Consejo de Ministros a
   propuesta conjunta del Ministerio de Hacienda y Administraciones Públicas y del Ministerio al que el organismo esté
   vinculado o sea dependiente (art. 93.2 LRJSP).» Source (LRJSP art. 93.2), identical wording: «Los estatutos de los
   organismos públicos se aprobarán por Real Decreto del Consejo de Ministros a propuesta conjunta del Ministerio de
   Hacienda y Administraciones Públicas y del Ministerio al que el organismo esté vinculado o sea dependiente.» No
   «(hoy: …)»: the organisation competences of the old ministry went to Transformación Digital y Función Pública
   (m01-l08 at art. 54.2) and the budget ones to Hacienda; which one now co-proposes statutes is in no source file.
   Same treatment as m01-l08 at art. 59.1–2 and the III.4 note on «Ministerio de Hacienda y Función Pública».
9. **coverage** — 2025 extr. S II res. 5. Section «Convenios» (consortium creation convenio): «Los consorcios se crean
   mediante convenio … (art. 123.1 LRJSP). Si participa la Administración General del Estado … su creación se autoriza
   por ley y el convenio de creación precisa autorización previa del Consejo de Ministros. La competencia para
   suscribirlo no podrá ser objeto de delegación y corresponde al titular del departamento ministerial participante;
   en los organismos autónomos, al titular del máximo órgano de dirección del organismo, previo informe del Ministerio
   del que dependa o al que esté vinculado (art. 123.2.a) y b) LRJSP).» Source (LRJSP art. 123): «1. Los consorcios se
   crearán mediante convenio suscrito por las Administraciones, organismos públicos o entidades participantes. 2. En
   los consorcios en los que participe la Administración General del Estado o sus organismos públicos y entidades
   vinculados o dependientes se requerirá: a) Que su creación se autorice por ley. b) El convenio de creación precisará
   de autorización previa del Consejo de Ministros. La competencia para la suscripción del convenio no podrá ser objeto
   de delegación, y corresponderá al titular del departamento ministerial participante, y en el ámbito de los
   organismos autónomos, al titular del máximo órgano de dirección del organismo, previo informe del Ministerio del
   que dependa o al que esté vinculado.»
10. **coverage + restore** — 2022 extr. P1 29 (coverage); also asked in 2022 extr. S II 4 (covered via m03-l05);
    ledger III.3 cut «63.1». Section «Iniciación»: «Los procedimientos de naturaleza sancionadora se iniciarán siempre
    de oficio por acuerdo del órgano competente y establecerán la debida separación entre la fase instructora y la
    sancionadora, que se encomendará a órganos distintos (art. 63.1 LPAC).» Source (LPAC art. 63.1): «Los
    procedimientos de naturaleza sancionadora se iniciarán siempre de oficio por acuerdo del órgano competente y
    establecerán la debida separación entre la fase instructora y la sancionadora, que se encomendará a órganos
    distintos.»
11. **coverage + restore** — 2024 extr. S I 7; ledger III.3 cut «66.1». Same paragraph: «La solicitud debe contener,
    entre otros datos, la identificación del medio electrónico, o en su defecto, lugar físico en que el interesado
    desea que se practique la notificación (art. 66.1.b) LPAC).» Source (LPAC art. 66.1): «Las solicitudes que se
    formulen deberán contener: […] b) Identificación del medio electrónico, o en su defecto, lugar físico en que desea
    que se practique la notificación.»
12. **restore** — ledger III.3 cut «85 LPAC», asked in conv2020 S II 5 (key c: pago voluntario terminates the
    procedure except reposición and indemnización) and conv2022_X S II 4 (options a and d rest on 85.1 and 85.3; both
    rows tema «III.3 (o III.5)»). Section «Terminación», after art. 84.1: «Iniciado un procedimiento sancionador, si el
    infractor reconoce su responsabilidad … (art. 85.1 LPAC). Cuando la sanción tenga únicamente carácter pecuniario,
    o quepa además otra no pecuniaria cuya improcedencia se ha justificado, el pago voluntario … termina el
    procedimiento, salvo en lo relativo a la reposición de la situación alterada o a la determinación de la
    indemnización … (art. 85.2 LPAC). En ambos casos, si la sanción es únicamente pecuniaria, el órgano competente
    aplicará reducciones de, al menos, el 20 % … acumulables entre sí. Deben figurar en la notificación de iniciación,
    y su efectividad está condicionada al desistimiento o renuncia … El porcentaje podrá incrementarse
    reglamentariamente (art. 85.3 LPAC).» Source (LPAC art. 85): «1. Iniciado un procedimiento sancionador, si el
    infractor reconoce su responsabilidad, se podrá resolver el procedimiento con la imposición de la sanción que
    proceda. 2. Cuando la sanción tenga únicamente carácter pecuniario o bien quepa imponer una sanción pecuniaria y
    otra de carácter no pecuniario pero se ha justificado la improcedencia de la segunda, el pago voluntario por el
    presunto responsable, en cualquier momento anterior a la resolución, implicará la terminación del procedimiento,
    salvo en lo relativo a la reposición de la situación alterada o a la determinación de la indemnización por los
    daños y perjuicios causados por la comisión de la infracción. 3. En ambos casos, cuando la sanción tenga únicamente
    carácter pecuniario, el órgano competente para resolver el procedimiento aplicará reducciones de, al menos, el 20 %
    sobre el importe de la sanción propuesta, siendo éstos acumulables entre sí. Las citadas reducciones, deberán estar
    determinadas en la notificación de iniciación del procedimiento y su efectividad estará condicionada al
    desistimiento o renuncia de cualquier acción o recurso en vía administrativa contra la sanción. El porcentaje de
    reducción previsto en este apartado podrá ser incrementado reglamentariamente.»
13. **coverage + restore** — 2022 ord. S II 18 (disputed key; norm fact only: fifteen days, the key's option text is
    garbled and is not followed); ledger III.3 cut «88.1». Section «Terminación», after art. 87: «La resolución
    decidirá todas las cuestiones planteadas por los interesados y aquellas otras derivadas del procedimiento. Sobre
    cuestiones conexas que no hubieran planteado, el órgano competente podrá pronunciarse poniéndolo antes de
    manifiesto a los interesados por un plazo no superior a quince días, para que formulen alegaciones y aporten, en su
    caso, los medios de prueba (art. 88.1 LPAC).» Source (LPAC art. 88.1): «La resolución que ponga fin al procedimiento
    decidirá todas las cuestiones planteadas por los interesados y aquellas otras derivadas del mismo. Cuando se trate
    de cuestiones conexas que no hubieran sido planteadas por los interesados, el órgano competente podrá pronunciarse
    sobre las mismas, poniéndolo antes de manifiesto a aquéllos por un plazo no superior a quince días, para que
    formulen las alegaciones que estimen pertinentes y aporten, en su caso, los medios de prueba.»
14. **«Lo que más cae»** (block full at ten lines):
    - Line «El parentesco de consanguinidad dentro del cuarto grado es motivo de abstención (art. 23.2.b) LRJSP).» →
      «El parentesco de consanguinidad dentro del cuarto grado, en el que está el primo hermano, es motivo de
      abstención (art. 23.2.b) LRJSP; art. 918 Código Civil).» (the two partial rows ask exactly the cousin).
    - Line «La declaración de lesividad no podrá adoptarse pasados cuatro años desde que se dictó el acto (art. 107.2
      LPAC).» replaced by «Si la ley no fija plazos, las infracciones muy graves prescriben a los tres años, las graves a
      los dos y las leves a los seis meses; las sanciones por faltas muy graves, a los tres años, por graves a los dos y
      por leves al año (art. 30.1 LRJSP).» Why: art. 30.1 is asked three times (conv2022_X S II 5, conv2020 S II 1,
      conv2020_X S II 6); the lesividad line rests on two (conv2024_X P1 18, conv2025_A S I 3) and the fact stays in
      the body («La lesividad no podrá declararse pasados cuatro años…», art. 107.2 LPAC).
15. **Normativa**: LPAC line adds 14.1–14.2, 16.4, 17.2, 63.1, 66.1, 85 (82–84 → 82–85), 88.1; LRJSP line adds 14.1–14.2,
    30.1, 51, 53.1, 93.2, 123.1–123.2; new line «Código Civil: art. 918.» Nothing removed (no article lost its last
    citation; 107.2 is still cited in the body).

## m03-l04

1. **coverage + restore** — 2024 extr. S II 7; ledger III.4 cut «62». Section «Órgano de contratación», new first
   paragraph «Los órganos de contratación deberán designar un responsable del contrato … (art. 62.1 LCSP). En los
   contratos de obras, las facultades del responsable del contrato serán ejercidas por el Director Facultativo (art.
   62.2 LCSP).» Source (LCSP art. 62): «1. Con independencia de la unidad encargada del seguimiento y ejecución
   ordinaria del contrato que figure en los pliegos, los órganos de contratación deberán designar un responsable del
   contrato al que corresponderá supervisar su ejecución y adoptar las decisiones y dictar las instrucciones necesarias
   con el fin de asegurar la correcta realización de la prestación pactada, dentro del ámbito de facultades que
   aquellos le atribuyan. […] 2. En los contratos de obras, las facultades del responsable del contrato serán ejercidas
   por el Director Facultativo conforme con lo dispuesto en los artículos 237 a 246.»
2. **coverage + restore** — 2022 extr. S II 16; ledger III.4 cut «229.5». Section «Órgano de contratación», after art.
   323.1: «El órgano de contratación del sistema estatal de contratación centralizada es la Junta de Contratación
   Centralizada, adscrita a la Dirección General de Racionalización y Centralización de la Contratación, sin perjuicio
   de la competencia para contratar en el caso de contratos basados cuyos destinatarios sean entidades adheridas (arts.
   229.5 y 323.3 LCSP).» Source (LCSP art. 229.5): «El órgano de contratación del sistema estatal de contratación
   centralizada es la Junta de Contratación Centralizada, adscrita a la Dirección General de Racionalización y
   Centralización de la Contratación del Ministerio de Hacienda y Función Pública, sin perjuicio de lo dispuesto en el
   apartado 6 siguiente sobre la competencia para contratar en el caso de contratos basados cuyos destinatarios sean
   entidades adheridas.» (art. 323.3): «Corresponden al Ministerio de Hacienda y Función Pública, a través de la Junta de
   Contratación Centralizada, las funciones de órgano de contratación del sistema estatal de contratación
   centralizada…». The ministry name is omitted as in the III.4 writer's note (no source gives the DG's present
   adscription; no «hoy» possible).
3. **coverage + restore** — 2022 extr. P1 res. 5 (65.1); 2025 ord. S II 4 (66.1); ledger III.4 cut «aptitud (65–66)».
   New subsection «### Condiciones de aptitud» (title of LCSP art. 65) after «Órgano de contratación»: «Solo podrán
   contratar con el sector público las personas naturales o jurídicas, españolas o extranjeras, … (art. 65.1 LCSP).
   Las personas jurídicas solo podrán ser adjudicatarias … (art. 66.1 LCSP).» Source (LCSP art. 65.1): «Solo podrán
   contratar con el sector público las personas naturales o jurídicas, españolas o extranjeras, que tengan plena
   capacidad de obrar, no estén incursas en alguna prohibición de contratar, y acrediten su solvencia económica y
   financiera y técnica o profesional o, en los casos en que así lo exija esta Ley, se encuentren debidamente
   clasificadas.» (art. 66.1): «Las personas jurídicas solo podrán ser adjudicatarias de contratos cuyas prestaciones
   estén comprendidas dentro de los fines, objeto o ámbito de actividad que, a tenor de sus estatutos o reglas
   fundacionales, les sean propios.»
4. **coverage** — 2022 extr. S II 6. Same subsection: «En los contratos de obras, la solvencia técnica del empresario
   se acredita por uno o varios medios, a elección del órgano de contratación. Entre ellos está la relación de las
   obras ejecutadas en el curso de los cinco últimos años, avalada por certificados de buena ejecución que indican el
   importe, las fechas y el lugar de ejecución de las obras. Cuando sea necesario … los últimos diez años (art.
   88.1.a) LCSP).» Source (LCSP art. 88.1.a)): «Relación de las obras ejecutadas en el curso de los cinco últimos años,
   avalada por certificados de buena ejecución; estos certificados indicarán el importe, las fechas y el lugar de
   ejecución de las obras […]. Cuando sea necesario para garantizar un nivel adecuado de competencia, los poderes
   adjudicadores podrán indicar que se tendrán en cuenta las pruebas de las obras pertinentes ejecutadas en los
   últimos diez años.»
5. **coverage + restore** — 2022 extr. P1 20; ledger III.4 cut «99.1». Section «Pliegos, presupuesto base de licitación
   y valor estimado». Old: «El presupuesto base de licitación es el límite máximo …» New: «El objeto de los contratos
   del sector público deberá ser determinado (art. 99.1 LCSP). El presupuesto base de licitación es el límite máximo
   …» (rest of the paragraph unchanged, rewrapped). Source (LCSP art. 99.1): «El objeto de los contratos del sector
   público deberá ser determinado.»
6. **coverage + restore** — 2024 ord. P1 22 (145.1); 2022 extr. P1 30 (131.2); ledger III.4 cut «131.2». New text under
   «## Adjudicación», before «### Procedimiento abierto»: «La adjudicación se realizará, ordinariamente, utilizando una
   pluralidad de criterios de adjudicación basados en el principio de mejor relación calidad-precio, y utilizando el
   procedimiento abierto o el procedimiento restringido, salvo los contratos de concesión de servicios especiales del
   Anexo IV, que se adjudican por el procedimiento restringido (arts. 131.2 y 145.1 LCSP). Previa justificación en el
   expediente, … coste del ciclo de vida (art. 145.1 LCSP).» Source (LCSP art. 131.2): «La adjudicación se realizará,
   ordinariamente utilizando una pluralidad de criterios de adjudicación basados en el principio de mejor relación
   calidad-precio, y utilizando el procedimiento abierto o el procedimiento restringido, salvo los contratos de
   concesión de servicios especiales del Anexo IV, que se adjudicarán mediante este último procedimiento.» (art.
   145.1): «La adjudicación de los contratos se realizará utilizando una pluralidad de criterios de adjudicación en
   base a la mejor relación calidad-precio. Previa justificación en el expediente, los contratos se podrán adjudicar con
   arreglo a criterios basados en un planteamiento que atienda a la mejor relación coste-eficacia, sobre la base del
   precio o coste, como el cálculo del coste del ciclo de vida con arreglo al artículo 148.»
7. **coverage** — 2022 extr. S I res. 4 (partial). Same place: «El anuncio de licitación de los contratos de las
   Administraciones Públicas se publica en el perfil de contratante, salvo en los procedimientos negociados sin
   publicidad. En los contratos de la Administración General del Estado, o de las entidades vinculadas a ella que gocen
   de la naturaleza de Administraciones Públicas, se publica además en el «Boletín Oficial del Estado». Si el contrato
   está sujeto a regulación armonizada, la licitación se publica además en el «Diario Oficial de la Unión Europea»
   (art. 135.1 LCSP).» Source (LCSP art. 135.1): «El anuncio de licitación para la adjudicación de contratos de las
   Administraciones Públicas, a excepción de los procedimientos negociados sin publicidad, se publicará en el perfil de
   contratante. En los contratos celebrados por la Administración General del Estado, o por las entidades vinculadas a
   la misma que gocen de la naturaleza de Administraciones Públicas, el anuncio de licitación se publicará además en el
   «Boletín Oficial del Estado». Cuando los contratos estén sujetos a regulación armonizada la licitación deberá
   publicarse, además, en el «Diario Oficial de la Unión Europea» […]».
8. **coverage + restore** — 2025 extr. S I 5; ledger III.4 cut «223.2». Section «Acuerdos marco» (the nearest section
   of the same título, racionalización técnica): «El sistema dinámico de adquisición es un proceso totalmente
   electrónico, con una duración limitada y determinada en los pliegos, y debe estar abierto durante todo el período
   de vigencia a cualquier empresa interesada que cumpla los criterios de selección (art. 223.2 LCSP).» Source (LCSP
   art. 223.2), same wording.
9. **restore** — ledger III.4 cut «196», asked in conv2024_X S I 8 (key d, tema III.4 (o III.6); the coverage report
   counted it covered through m03-l06). Section «Ejecución, demora y penalidades», after art. 193.3: «Será obligación
   del contratista indemnizar todos los daños y perjuicios que se causen a terceros … (art. 196.1 LCSP). Cuando hayan
   sido ocasionados como consecuencia inmediata y directa de una orden de la Administración, será esta responsable
   dentro de los límites señalados en las leyes. También lo será de los daños … por los vicios del proyecto en el
   contrato de obras, sin perjuicio de repetir contra el redactor del proyecto, o en el contrato de suministro de
   fabricación (art. 196.2 LCSP).» Source (LCSP art. 196): «1. Será obligación del contratista indemnizar todos los
   daños y perjuicios que se causen a terceros como consecuencia de las operaciones que requiera la ejecución del
   contrato. 2. Cuando tales daños y perjuicios hayan sido ocasionados como consecuencia inmediata y directa de una
   orden de la Administración, será esta responsable dentro de los límites señalados en las leyes. También será la
   Administración responsable de los daños que se causen a terceros como consecuencia de los vicios del proyecto en el
   contrato de obras, sin perjuicio de la posibilidad de repetir contra el redactor del proyecto de acuerdo con lo
   establecido en el artículo 315, o en el contrato de suministro de fabricación.»
10. **coverage + restore** — 2022 ord. S I 14; ledger III.4 cut «49.1». Section «Recurso especial en materia de
    contratación», after art. 45.1. Old: «(art. 45.1 LCSP). El plazo es de quince días hábiles;» New: «(art. 45.1 LCSP).
    Antes de interponer el recurso especial, las personas legitimadas para ello podrán solicitar ante el órgano
    competente para resolverlo la adopción de medidas cautelares (art. 49.1 LCSP). El plazo es de quince días
    hábiles;». Source (LCSP art. 49.1): «Antes de interponer el recurso especial, las personas legitimadas para ello
    podrán solicitar ante el órgano competente para resolver el recurso la adopción de medidas cautelares.»
11. **«Lo que más cae»** (8 → 9 lines): added «La adjudicación se realiza ordinariamente con una pluralidad de criterios
    basados en la mejor relación calidad-precio, por el procedimiento abierto o el restringido, salvo la concesión de
    servicios especiales del Anexo IV, que va por el restringido (arts. 131.2 y 145.1 LCSP).» Asked twice (2024 ord. P1
    22, 2022 extr. P1 30; 2022 extr. S I res. 4 option c leans on it too).
12. **Normativa**: LCSP line adds 49, 62, 65–66, 88, 99, 131, 135, 145, 196, 223 and 229 (323 already listed).

## m03-l05

1. **restore** — ledger III.5 cut «30.1 LRJSP», asked in conv2020 S II 1 (key c, graves two years), conv2020_X S II 6
   (key d, sanción muy grave three years) and conv2022_X S II 5 (key c), all tema «III.3 (o III.5)». Section
   «Principios de la potestad sancionadora», after the art. 29.3 list: same sentence as m03-l03 change 5, without the
   pointer. Source: LRJSP art. 30.1, quoted under m03-l03 change 5.
2. **«Lo que más cae»** (8 → 9 lines): added the art. 30.1 line (same wording as in m03-l03), three questions.
3. **Normativa**: LRJSP line «arts. 4.1, 25.1, 27.1 y 29.3» → «arts. 4.1, 25.1, 27.1, 29.3 y 30.1».

## Cut items checked against every exam (2020–2025)

Method: every questionnaire in `SP/exams/` (conv2020, conv2020_X, conv2022, conv2022_X, conv2024_A, conv2024_X,
conv2025_A, conv2025_X; modelo B repeats A) split into questions and searched by article number and by the words of
each cut article; every hit read with its key. «Restored» items are in the lesson changes above.

**III.3 (m03-l03)** — writer's note «whole low-yield items were cut (4.1 a/c, 5.3, 63.1, 66.1, 73.1, 85, 88.1 LPAC;
14.2, 53.1 LRJSP; 19.2, 23.3, 28, 46.4 LJCA; one worked example)», plus the three sentences «removed rather than
fixed (5.3 LPAC, 53.1 LRJSP, 46.4 LJCA)».

| Item | Verdict | Questions |
|---|---|---|
| LPAC 4.1.a) and c) | not asked | conv2022 P1 9 asks 4.1.b) only (covered) |
| LPAC 5.3 | not asked | conv2020_X S I res. 4 keys 5.6 (option b, «se presume aquella representación para formular solicitudes», is a distractor only) |
| LPAC 63.1 | restored (m03-l03 10) | conv2022_X P1 29; conv2022_X S II 4 |
| LPAC 66.1 | restored (m03-l03 11) | conv2024_X S I 7 |
| LPAC 73.1 | not asked | — |
| LPAC 85 | restored (m03-l03 12) | conv2020 S II 5; conv2022_X S II 4 |
| LPAC 88.1 | restored (m03-l03 13) | conv2022 S II 18 (disputed key) |
| LRJSP 14.2 | restored (m03-l03 3) | conv2022 S II 2 |
| LRJSP 53.1 | restored (m03-l03 7) | conv2025_X S II 19 |
| LJCA 19.2 | not asked | — |
| LJCA 23.3 | not asked | — |
| LJCA 28 (also the III.2 note «actos consentidos») | not asked | — |
| LJCA 46.4 | not asked | the recurso questions (conv2020 S I 6, conv2022 S II 13, conv2022_X S I 13, conv2025_A S II 19, conv2025_X S II res. 4) rest on LPAC 114, 123–124 and LJCA 46.1 |
| one worked date example | not a norm fact | the three kept examples cover arts. 30.2–5; nothing to restore |

**III.4 (m03-l04)** — fix-round cuts «aptitud (65–66), prerrogativas (190–191), 131.2, 146.1, cesión letters a), c),
d), 223.2, 229.5, 323.2, 62, 116.1, 99.1, 326.3, 326.6, 159.4.b), 150.2 (retirada), 196, 210.3, 203.1–2, most of
211.1, 49.1, 177.1 and the DA undécima sentence».

| Item | Verdict | Questions |
|---|---|---|
| LCSP 65.1 | restored (m03-l04 3) | conv2022_X P1 res. 5 |
| LCSP 66.1 | restored (m03-l04 3) | conv2025_A S II 4 |
| LCSP 190–191 (prerrogativas) | not asked | — |
| LCSP 131.2 | restored (m03-l04 6) | conv2022_X P1 30 (and conv2022_X S I res. 4) |
| LCSP 146.1 | not asked | conv2025_A S II 6 («único criterio el precio») asks the plazo of art. 158.1, covered |
| LCSP 214.2.a), c), d) | not asked | conv2024_X P1 19 asks 214.2.b), covered |
| LCSP 223.2 | restored (m03-l04 8) | conv2025_X S I 5 |
| LCSP 229.5 | restored (m03-l04 2) | conv2022_X S II 16 |
| LCSP 323.2 | not asked | conv2024_X S II 2 keys the Ministro (323.1), covered |
| LCSP 62 | restored (m03-l04 1) | conv2024_X S II 7 |
| LCSP 116.1 | not asked | — |
| LCSP 99.1 | restored (m03-l04 5) | conv2022_X P1 20 |
| LCSP 326.3 | not asked | — |
| LCSP 326.6 | not asked | — |
| LCSP 159.4.b) | not asked | — |
| LCSP 150.2 (retirada de la oferta) | not asked | — |
| LCSP 196 | restored (m03-l04 9) | conv2024_X S I 8 |
| LCSP 210.3 | not asked | — |
| LCSP 203.1–2 | not asked | conv2022 S I res. 4 and conv2020 S I 9 ask 205 and 242.2, not 203 |
| LCSP 211.1 (rest of the list) | not asked | conv2020 S I 12 and S I res. 1 ask the supply-contract causes (arts. 306–307), not 211.1 |
| LCSP 49.1 | restored (m03-l04 10) | conv2022 S I 14 |
| LCSP 177.1 | not asked | — |
| DA undécima (revision of thresholds) | not asked | — |

**III.5 (m03-l05)** — «The fix round cut 29.1, 30.1, 31.1 LRJSP, 1.4 Ley 60/2003, 7.3 LGP, 15.2, 32.1 and 284.2 LCSP,
the art. 2.4.j) LGS sentence and two «Lo que más cae» lines».

| Item | Verdict | Questions |
|---|---|---|
| LRJSP 29.1 | not asked | — |
| LRJSP 30.1 | restored (m03-l05 1; m03-l03 5) | conv2020 S II 1; conv2020_X S II 6; conv2022_X S II 5 |
| LRJSP 31.1 | not asked | — |
| Ley 60/2003 art. 1.4 | not asked | conv2024_A P1 23 (anulada) asks art. 2 |
| LGP art. 7.3 | not asked | the LGP questions ask arts. 26, 37, 43, 47, 58, 60, 73–75, 79, 150 |
| LCSP 15.2 | not asked | — |
| LCSP 32.1 | not asked | conv2025_X S II 17 asks 32.2.b), covered |
| LCSP 284.2 | not asked | — |
| LGS 2.4.j) (desde 23-10-2026) | not asked | conv2025_A P1 21 asks 2.4.g), covered; the ledger notes no option carries j) |
| two «Lo que más cae» lines | not checkable | the ledger does not record their wording; the facts of the cut body items are all listed above |

**III.1, III.2, III.6, III.7** — no cut lists in the ledger beyond «Not in the sources, left out» (III.1:
classification of reglamentos, rank of ley orgánica, primacy of EU law — not norm text, nothing to restore) and the
III.2 «actos consentidos» (LJCA 28, not asked, above). Nothing restored.

## New sources

None. The Código Civil (`BOE-A-1889-4763_codigo-civil_2025-01-03.pdf`) and every other article cited were already in
`sources/normativa/`. No `normativa.yaml` entry needed.

## Glossary

No section removed, so no entry moves to the waiting list. No new term is defined. The new text adds occurrences of
existing glossary terms (convenio, interesado, contrato de obras, contrato sujeto a regulación armonizada) and a new lesson cross-reference (m03-l03 → m03-l05; the m03-l03 → m02-l03 pointer is kept, moved
one paragraph): `glossary-links.es.txt` and `lesson-refs.es.txt` need regenerating by the coordinator.

## Word counts (`wc -w`)

| Lesson | Before | After |
|---|---|---|
| m03-l01 | 2,285 | 2,306 |
| m03-l03 | 3,979 | 5,134 |
| m03-l04 | 3,991 | 4,709 |
| m03-l05 | 1,669 | 1,796 |

m03-l02, m03-l06 and m03-l07 unchanged.

## Appendix — exact diffs (old → new)

### m03-l01

```diff
@@ -139,0 +140,5 @@ carácter general, aunque procedan de un órgano de igual o superior jerarquía
+:::note{type=info}
+Fuera del enunciado literal del programa; preguntado en la convocatoria 2025 (llamamiento extraordinario), primera
+parte, pregunta de reserva 4.
+:::
+
```

### m03-l03

```diff
@@ -18,2 +18,21 @@ aporte o se subsane el defecto dentro del plazo de diez días que deberá conced
-las circunstancias lo requieran (art. 5.6 LPAC). La relación electrónica de los representantes está en m02-l03, el
-tema de la administración electrónica.
+las circunstancias lo requieran (art. 5.6 LPAC).
+
+Las personas físicas podrán elegir en todo momento si se comunican con las Administraciones Públicas a través de medios
+electrónicos o no, salvo que estén obligadas a relacionarse a través de medios electrónicos (art. 14.1 LPAC). Están
+obligados a relacionarse electrónicamente para cualquier trámite de un procedimiento administrativo, entre otros,
+quienes representen a un interesado que esté obligado a relacionarse electrónicamente con la Administración, y los
+empleados de las Administraciones Públicas para los trámites y actuaciones que realicen con ellas por razón de su
+condición de empleado público, en la forma en que se determine reglamentariamente por cada Administración (art. 14.2.d)
+y e) LPAC). La lista completa está en m02-l03, el tema de la administración electrónica.
+
+### Registros y archivo
+
+Los registros electrónicos de todas y cada una de las Administraciones deberán ser plenamente interoperables, de modo
+que se garantice su compatibilidad informática e interconexión, así como la transmisión telemática de los asientos
+registrales y de los documentos que se presenten en cualquiera de los registros (art. 16.4 LPAC).
+
+Los documentos electrónicos deberán conservarse en un formato que permita garantizar la autenticidad, integridad y
+conservación del documento, así como su consulta con independencia del tiempo transcurrido desde su emisión. Se
+asegurará en todo caso la posibilidad de trasladar los datos a otros formatos y soportes que garanticen el acceso desde
+diferentes aplicaciones. La eliminación de dichos documentos deberá ser autorizada de acuerdo a lo dispuesto en la
+normativa aplicable (art. 17.2 LPAC).
@@ -32,0 +52,6 @@ delegación se consideran dictadas por el órgano delegante (art. 9.4 LRJSP).
+El órgano que se estime incompetente para resolver un asunto remitirá directamente las actuaciones al órgano que
+considere competente y lo notificará a los interesados (art. 14.1 LRJSP). Los interesados que sean parte en el
+procedimiento podrán dirigirse al órgano que esté conociendo del asunto para que decline su competencia y remita las
+actuaciones al órgano competente. También podrán dirigirse al órgano que estimen competente para que requiera de
+inhibición al que esté conociendo del asunto (art. 14.2 LRJSP).
+
@@ -58,0 +84,4 @@ Quien se encuentre en un motivo de abstención se abstendrá de intervenir y lo
+En la línea colateral se sube hasta el tronco común y después se baja hasta la persona con quien se hace la computación.
+El hermano dista dos grados del hermano, tres del tío y cuatro del primo hermano (art. 918 Código Civil). Un primo
+hermano está dentro del cuarto grado de consanguinidad de la letra b) (art. 23.2.b) LRJSP).
+
@@ -64,0 +94,8 @@ procedimiento (art. 24.5 LRJSP).
+### Potestad sancionadora
+
+Las infracciones y sanciones prescribirán según lo dispuesto en las leyes que las establezcan. Si éstas no fijan plazos
+de prescripción, las infracciones muy graves prescribirán a los tres años, las graves a los dos años y las leves a los
+seis meses; las sanciones impuestas por faltas muy graves prescribirán a los tres años, las impuestas por faltas graves
+a los dos años y las impuestas por faltas leves al año (art. 30.1 LRJSP). Los principios de la potestad sancionadora
+están en m03-l05.
+
@@ -73,0 +111,30 @@ prevea un plazo superior. Los firmantes podrán acordar unánimemente su prórro
+Los convenios se extinguen por el cumplimiento de las actuaciones que constituyen su objeto o por incurrir en causa de
+resolución (art. 51.1 LRJSP). Son causas de resolución (art. 51.2 LRJSP):
+
+- a) El transcurso del plazo de vigencia del convenio sin haberse acordado la prórroga del mismo.
+- b) El acuerdo unánime de todos los firmantes.
+- c) El incumplimiento de las obligaciones y compromisos asumidos por parte de alguno de los firmantes. Cualquiera de
+  las partes podrá notificar a la incumplidora un requerimiento para que cumpla en un determinado plazo. El
+  requerimiento se comunica al responsable del mecanismo de seguimiento, vigilancia y control de la ejecución del
+  convenio y a las demás partes firmantes. Si persiste el incumplimiento, la parte que lo dirigió notifica a las
+  firmantes la causa de resolución y se entiende resuelto el convenio. La resolución por esta causa podrá conllevar la
+  indemnización de los perjuicios causados si así se hubiera previsto.
+- d) La decisión judicial declaratoria de la nulidad del convenio.
+- e) Cualquier otra causa distinta de las anteriores prevista en el convenio o en otras leyes.
+
+Dentro de los tres meses siguientes a la suscripción de cualquier convenio cuyos compromisos económicos asumidos superen
+los 600.000 euros, el convenio se remite electrónicamente al Tribunal de Cuentas u órgano externo de fiscalización de la
+Comunidad Autónoma, según corresponda (art. 53.1 LRJSP).
+
+Los estatutos de los organismos públicos se aprobarán por Real Decreto del Consejo de Ministros a propuesta conjunta del
+Ministerio de Hacienda y Administraciones Públicas y del Ministerio al que el organismo esté vinculado o sea dependiente
+(art. 93.2 LRJSP).
+
+Los consorcios se crean mediante convenio suscrito por las Administraciones, organismos públicos o entidades
+participantes (art. 123.1 LRJSP). Si participa la Administración General del Estado o sus organismos públicos y
+entidades vinculados o dependientes, su creación se autoriza por ley y el convenio de creación precisa autorización
+previa del Consejo de Ministros. La competencia para suscribirlo no podrá ser objeto de delegación y corresponde al
+titular del departamento ministerial participante; en los organismos autónomos, al titular del máximo órgano de
+dirección del organismo, previo informe del Ministerio del que dependa o al que esté vinculado (art. 123.2.a) y b)
+LRJSP).
+
@@ -152,0 +220,5 @@ siguientes (art. 56.2 LPAC).
+Los procedimientos de naturaleza sancionadora se iniciarán siempre de oficio por acuerdo del órgano competente y
+establecerán la debida separación entre la fase instructora y la sancionadora, que se encomendará a órganos distintos
+(art. 63.1 LPAC). La solicitud debe contener, entre otros datos, la identificación del medio electrónico, o en su
+defecto, lugar físico en que el interesado desea que se practique la notificación (art. 66.1.b) LPAC).
+
@@ -181,0 +254,10 @@ ordenamiento jurídico, y la declaración de caducidad (art. 84.1 LPAC).
+Iniciado un procedimiento sancionador, si el infractor reconoce su responsabilidad, se podrá resolver con la imposición
+de la sanción que proceda (art. 85.1 LPAC). Cuando la sanción tenga únicamente carácter pecuniario, o quepa además otra
+no pecuniaria cuya improcedencia se ha justificado, el pago voluntario en cualquier momento anterior a la resolución
+termina el procedimiento, salvo en lo relativo a la reposición de la situación alterada o a la determinación de la
+indemnización por los daños y perjuicios causados por la infracción (art. 85.2 LPAC). En ambos casos, si la sanción es
+únicamente pecuniaria, el órgano competente aplicará reducciones de, al menos, el 20 % sobre el importe de la sanción
+propuesta, acumulables entre sí. Deben figurar en la notificación de iniciación, y su efectividad está condicionada al
+desistimiento o renuncia de cualquier acción o recurso en vía administrativa contra la sanción. El porcentaje podrá
+incrementarse reglamentariamente (art. 85.3 LPAC).
+
@@ -185,0 +268,5 @@ para resolver queda suspendido hasta su terminación (art. 87 LPAC).
+La resolución decidirá todas las cuestiones planteadas por los interesados y aquellas otras derivadas del procedimiento.
+Sobre cuestiones conexas que no hubieran planteado, el órgano competente podrá pronunciarse poniéndolo antes de
+manifiesto a los interesados por un plazo no superior a quince días, para que formulen alegaciones y aporten, en su
+caso, los medios de prueba (art. 88.1 LPAC).
+
@@ -332,2 +419,2 @@ caso, por Abogado. Ante órganos colegiados, deberán conferirla a un Procurador
-- El parentesco de consanguinidad dentro del cuarto grado es motivo de abstención (art. 23.2.b) LRJSP).
-- La declaración de lesividad no podrá adoptarse pasados cuatro años desde que se dictó el acto (art. 107.2 LPAC).
+- El parentesco de consanguinidad dentro del cuarto grado, en el que está el primo hermano, es motivo de abstención (art. 23.2.b) LRJSP; art. 918 Código Civil).
+- Si la ley no fija plazos, las infracciones muy graves prescriben a los tres años, las graves a los dos y las leves a los seis meses; las sanciones por faltas muy graves, a los tres años, por graves a los dos y por leves al año (art. 30.1 LRJSP).
@@ -337,3 +424,4 @@ caso, por Abogado. Ante órganos colegiados, deberán conferirla a un Procurador
-- Ley 39/2015 (LPAC): arts. 4.1, 5.6, 21–25, 30–33, 56.2, 58, 68, 74, 76.1, 77.2, 80, 82–84, 87, 91.3, 94–96, 106–112,
-  114–115, 118 y 121–126.
-- Ley 40/2015 (LRJSP): arts. 8.1, 9, 17, 20.1, 23–24, 47.1 y 49.h).
+- Ley 39/2015 (LPAC): arts. 4.1, 5.6, 14.1–14.2, 16.4, 17.2, 21–25, 30–33, 56.2, 58, 63.1, 66.1, 68, 74, 76.1, 77.2, 80,
+  82–85, 87, 88.1, 91.3, 94–96, 106–112, 114–115, 118 y 121–126.
+- Ley 40/2015 (LRJSP): arts. 8.1, 9, 14.1–14.2, 17, 20.1, 23–24, 30.1, 47.1, 49.h), 51, 53.1, 93.2 y 123.1–123.2.
+- Código Civil: art. 918.
```

### m03-l04

```diff
@@ -67,0 +68,5 @@ HAC/1517/2025, artículo único):
+Los órganos de contratación deberán designar un responsable del contrato, al que corresponderá supervisar su ejecución y
+adoptar las decisiones y dictar las instrucciones necesarias con el fin de asegurar la correcta realización de la
+prestación pactada, dentro del ámbito de facultades que aquellos le atribuyan (art. 62.1 LCSP). En los contratos de
+obras, las facultades del responsable del contrato serán ejercidas por el Director Facultativo (art. 62.2 LCSP).
+
@@ -70,0 +76,19 @@ Los Ministros y los Secretarios de Estado son los órganos de contratación de l
+El órgano de contratación del sistema estatal de contratación centralizada es la Junta de Contratación Centralizada,
+adscrita a la Dirección General de Racionalización y Centralización de la Contratación, sin perjuicio de la competencia
+para contratar en el caso de contratos basados cuyos destinatarios sean entidades adheridas (arts. 229.5 y 323.3 LCSP).
+
+### Condiciones de aptitud
+
+Solo podrán contratar con el sector público las personas naturales o jurídicas, españolas o extranjeras, que tengan
+plena capacidad de obrar, no estén incursas en alguna prohibición de contratar, y acrediten su solvencia económica y
+financiera y técnica o profesional o, en los casos en que así lo exija la LCSP, se encuentren debidamente clasificadas
+(art. 65.1 LCSP). Las personas jurídicas solo podrán ser adjudicatarias de contratos cuyas prestaciones estén
+comprendidas dentro de los fines, objeto o ámbito de actividad que, a tenor de sus estatutos o reglas fundacionales, les
+sean propios (art. 66.1 LCSP).
+
+En los contratos de obras, la solvencia técnica del empresario se acredita por uno o varios medios, a elección del
+órgano de contratación. Entre ellos está la relación de las obras ejecutadas en el curso de los cinco últimos años,
+avalada por certificados de buena ejecución que indican el importe, las fechas y el lugar de ejecución de las obras.
+Cuando sea necesario para garantizar un nivel adecuado de competencia, los poderes adjudicadores podrán indicar que se
+tendrán en cuenta las pruebas de las obras pertinentes ejecutadas en los últimos diez años (art. 88.1.a) LCSP).
+
@@ -87,2 +111,3 @@ material, de hecho o aritmético (art. 122.1 LCSP).
-El presupuesto base de licitación es el límite máximo de gasto que puede comprometer el órgano de contratación,
-incluido el IVA, salvo disposición en contrario (art. 100.1 LCSP). El valor estimado de obras, suministros y servicios
+El objeto de los contratos del sector público deberá ser determinado (art. 99.1 LCSP). El presupuesto base de licitación
+es el límite máximo de gasto que puede comprometer el órgano de contratación, incluido el IVA, salvo disposición en
+contrario (art. 100.1 LCSP). El valor estimado de obras, suministros y servicios
@@ -131,0 +157,13 @@ Administración, mediante retención en el precio (art. 108.2 LCSP).
+La adjudicación se realizará, ordinariamente, utilizando una pluralidad de criterios de adjudicación basados en el
+principio de mejor relación calidad-precio, y utilizando el procedimiento abierto o el procedimiento restringido, salvo
+los contratos de concesión de servicios especiales del Anexo IV, que se adjudican por el procedimiento restringido
+(arts. 131.2 y 145.1 LCSP). Previa justificación en el expediente, los contratos se podrán adjudicar con criterios
+basados en la mejor relación coste-eficacia, sobre la base del precio o coste, como el cálculo del coste del ciclo de
+vida (art. 145.1 LCSP).
+
+El anuncio de licitación de los contratos de las Administraciones Públicas se publica en el perfil de contratante, salvo
+en los procedimientos negociados sin publicidad. En los contratos de la Administración General del Estado, o de las
+entidades vinculadas a ella que gocen de la naturaleza de Administraciones Públicas, se publica además en el «Boletín
+Oficial del Estado». Si el contrato está sujeto a regulación armonizada, la licitación se publica además en el «Diario
+Oficial de la Unión Europea» (art. 135.1 LCSP).
+
@@ -234,0 +273,4 @@ el pliego (art. 221.4.a) LCSP).
+El sistema dinámico de adquisición es un proceso totalmente electrónico, con una duración limitada y determinada en los
+pliegos, y debe estar abierto durante todo el período de vigencia a cualquier empresa interesada que cumpla los
+criterios de selección (art. 223.2 LCSP).
+
@@ -243,0 +286,7 @@ contrato lo hagan necesario para su correcta ejecución y así se justifique en
+Será obligación del contratista indemnizar todos los daños y perjuicios que se causen a terceros como consecuencia de
+las operaciones que requiera la ejecución del contrato (art. 196.1 LCSP). Cuando hayan sido ocasionados como
+consecuencia inmediata y directa de una orden de la Administración, será esta responsable dentro de los límites
+señalados en las leyes. También lo será de los daños que se causen a terceros como consecuencia de los vicios del
+proyecto en el contrato de obras, sin perjuicio de repetir contra el redactor del proyecto, o en el contrato de
+suministro de fabricación (art. 196.2 LCSP).
+
@@ -326,2 +375,3 @@ En el sector público estatal lo resuelve el Tribunal Administrativo Central de
-(art. 45.1 LCSP). El plazo
-es de quince días hábiles; contra la adjudicación, se cuenta desde el siguiente a su notificación (art. 50.1 LCSP). Si
+(art. 45.1 LCSP). Antes de interponer el recurso especial, las personas legitimadas para ello podrán solicitar ante
+el órgano competente para resolverlo la adopción de medidas cautelares (art. 49.1 LCSP). El plazo es de quince días
+hábiles; contra la adjudicación, se cuenta desde el siguiente a su notificación (art. 50.1 LCSP). Si
@@ -343,0 +394 @@ recurso especial no proceden (art. 44.5 LCSP).
+- La adjudicación se realiza ordinariamente con una pluralidad de criterios basados en la mejor relación calidad-precio, por el procedimiento abierto o el restringido, salvo la concesión de servicios especiales del Anexo IV, que va por el restringido (arts. 131.2 y 145.1 LCSP).
@@ -347,3 +398,3 @@ recurso especial no proceden (art. 44.5 LCSP).
-- LCSP (Ley 9/2017): arts. 2, 13–22, 25–26, 29, 32, 37, 39–40, 44–45, 50, 53, 100–103, 106–108, 118–120, 122,
-  150, 153, 156–162, 164, 167–169, 172, 193, 198, 204–206, 210–211, 213–215, 219, 221, 235, 238, 242–244, 323 y
-  326, y disposición adicional duodécima.
+- LCSP (Ley 9/2017): arts. 2, 13–22, 25–26, 29, 32, 37, 39–40, 44–45, 49–50, 53, 62, 65–66, 88, 99–103, 106–108,
+  118–120, 122, 131, 135, 145, 150, 153, 156–162, 164, 167–169, 172, 193, 196, 198, 204–206, 210–211, 213–215, 219,
+  221, 223, 229, 235, 238, 242–244, 323 y 326, y disposición adicional duodécima.
```

### m03-l05

```diff
@@ -61,0 +62,5 @@ La graduación de la sanción considerará especialmente estos criterios (art. 2
+Las infracciones y sanciones prescribirán según lo dispuesto en las leyes que las establezcan. Si éstas no fijan plazos
+de prescripción, las infracciones muy graves prescribirán a los tres años, las graves a los dos años y las leves a los
+seis meses; las sanciones impuestas por faltas muy graves prescribirán a los tres años, las impuestas por faltas graves
+a los dos años y las impuestas por faltas leves al año (art. 30.1 LRJSP).
+
@@ -143,0 +149 @@ de servicios y el encargo a medios propios están en m03-l04, el tema de los con
+- Si la ley no fija plazos, las infracciones muy graves prescriben a los tres años, las graves a los dos y las leves a los seis meses; las sanciones por faltas muy graves, a los tres años, por graves a los dos y por leves al año (art. 30.1 LRJSP).
@@ -149 +155 @@ de servicios y el encargo a medios propios están en m03-l04, el tema de los con
-- Ley 40/2015 (LRJSP): arts. 4.1, 25.1, 27.1 y 29.3.
+- Ley 40/2015 (LRJSP): arts. 4.1, 25.1, 27.1, 29.3 y 30.1.
```

