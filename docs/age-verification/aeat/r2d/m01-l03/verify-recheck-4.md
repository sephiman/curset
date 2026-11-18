# Verify re-check 4 — `m01-l03`

Blind verifier (Opus), 2026-11-18. Input: `pending.md` (191 rows). Every pending id is present in the lesson as it
stands (ids recomputed with `provenance.sentences`), so no row records a new id. Sources: CE (BOE-A-1978-31229),
LO 3/1980 (BOE-A-1980-8648), Reglamento del Congreso (BOE-A-1982-5196), Ley 50/1997 (BOE-A-1997-25336), Ley 3/2015
(BOE-A-2015-3444), LRJSP (BOE-A-2015-10566), RD 1009/2023 (BOE-A-2023-24842).

| id | verdict | precept checked | note | replacement |
|---|---|---|---|---|
| `d30643b5ae` | PASS | art. 103.3 CE | — | — |
| `26a9b02896` | PASS | art. 104.2 CE | — | — |
| `b7d4f52a52` | PASS | art. 105 CE | lead-in; the table has a)–c), the whole article | — |
| `147af2ab70` | PASS | art. 105.a) CE | — | — |
| `73ca20ff99` | PASS | art. 105.b) CE | — | — |
| `41819ff450` | PASS | art. 105.c) CE | — | — |
| `f963f5ca3e` | PASS | art. 106.2 CE | — | — |
| `458fcff637` | PASS | LO 3/1980 (title) | — | — |
| `4b1a1c33e9` | PASS | art. 1.uno–dos LO 3/1980 | — | — |
| `b70b57b117` | PASS | art. 1.tres LO 3/1980 | — | — |
| `ffe1c6ccc0` | PASS | art. 2.1 LO 3/1980 | — | — |
| `dc9e63d745` | PASS | art. 2.2 LO 3/1980 | — | — |
| `898abdec1a` | PASS | art. 2.2 LO 3/1980 | — | — |
| `04ddea22c9` | PASS | art. 2.2 LO 3/1980 | — | — |
| `41dd757887` | PASS | art. 2.2 LO 3/1980 | — | — |
| `cf168db9e6` | PASS | art. 2.2.f) Ley 50/1997 | — | — |
| `bd5befa602` | PASS | art. 2.2.g) Ley 50/1997 | — | — |
| `6b9d1f0b36` | PASS | art. 2.2.h) Ley 50/1997 | — | — |
| `0d866e41b8` | PASS | art. 2.2.j) Ley 50/1997 | — | — |
| `e06a64980b` | PASS | art. 5.1.e) Ley 50/1997 | — | — |
| `9112c163e7` | PASS | art. 5.1.h) Ley 50/1997 | — | — |
| `69e74fbe15` | PASS | art. 10.2 Ley 50/1997 | — | — |
| `9eb35ae0bb` | PASS | art. 1.1 Ley 3/2015 | — | — |
| `93bde88c63` | PASS | art. 1.2 Ley 3/2015 | lead-in; table a)–g) is the whole list | — |
| `e754ab5664` | PASS | art. 1.2 Ley 3/2015 | header row | — |
| `4d1eea25bf` | PASS | art. 1.2.a) Ley 3/2015 | — | — |
| `963f5b761f` | PASS | art. 1.2.b) Ley 3/2015 | — | — |
| `b894e5a58f` | PASS | art. 1.2.c) Ley 3/2015 | — | — |
| `01a25ab0b5` | PASS | art. 1.2.d) Ley 3/2015 | — | — |
| `1f9ee2751a` | PASS | art. 1.2.e) Ley 3/2015 | — | — |
| `3908b76faa` | PASS | art. 1.2.f) Ley 3/2015 | — | — |
| `fe88e4046b` | PASS | art. 1.2.g) Ley 3/2015 | — | — |
| `0e0b394fe2` | PASS | art. 1.3 Ley 3/2015 | — | — |
| `88c4cd522f` | FAIL | art. 2.1 Ley 3/2015 | drops «y de acuerdo con lo dispuesto en su legislación específica», the second condition of the appointment | El nombramiento de los altos cargos se hace entre personas idóneas y de acuerdo con lo dispuesto en su legislación específica; son idóneos quienes reúnen honorabilidad y la debida formación y experiencia en la materia, en función del cargo que vayan a desempeñar (art. 2.1 Ley 3/2015). |
| `5da1a5349f` | PASS | art. 2.2 Ley 3/2015 | lead-in; table a)–e) is the whole list | — |
| `5b130723ce` | PASS | art. 2.2 Ley 3/2015 | header row | — |
| `827bceb800` | PASS | art. 2.2.a) Ley 3/2015 | — | — |
| `77d5f42c44` | PASS | art. 2.2.b) Ley 3/2015 | — | — |
| `1b837eef03` | PASS | art. 2.2.c) Ley 3/2015 | — | — |
| `6326ed26d2` | PASS | art. 2.2.d) Ley 3/2015 | — | — |
| `0f2a43f0c1` | PASS | art. 2.2.e) Ley 3/2015 | — | — |
| `9d97965feb` | FAIL | art. 2.2 (último párrafo) Ley 3/2015 | drops the second branch: where the alto cargo can only be removed for causas tasadas, the supervening lack is a grave breach declared through the procedure | La falta de honorabilidad sobrevenida es causa de cese y, en los supuestos en que el alto cargo solo puede ser cesado por determinadas causas tasadas, se considera un incumplimiento grave de sus obligaciones del cargo declarado a través del correspondiente procedimiento (art. 2.2 Ley 3/2015). |
| `22c6cc6b8d` | FAIL | art. 2.5 Ley 3/2015 | out of the norm's order: art. 2.5 sits before arts. 2.1 (idoneidad), 2.2, 2.3 and 2.4 of the next paragraph; move it to follow `093e79b580` (art. 2.4) | El alto cargo suscribe una declaración responsable de que cumple los requisitos de idoneidad y la remite a la Oficina de Conflictos de Intereses (art. 2.5 Ley 3/2015). |
| `69b794dff7` | FAIL | art. 2.7 Ley 3/2015 | out of order (art. 2.7 before 2.1–2.6); move it between `4e32250284` (art. 2.6) and `da84833d2e` (art. 2.8); also drops «Todos» and «de Derecho Público o Privado» | Todos los órganos, organismos y entidades del sector público estatal, de Derecho Público o Privado, deben informar a la Oficina de Conflictos de Intereses de los nombramientos de altos cargos que efectúen en el plazo de siete días a contar desde el nombramiento (art. 2.7 Ley 3/2015). |
| `05c25ebccc` | FAIL | art. 2.1 Ley 3/2015 | out of order: the last sentence of art. 2.1 sits after the whole of art. 2.2; move it to follow `88c4cd522f`, before the lead-in `5da1a5349f` | La idoneidad la aprecian tanto quien propone como quien nombra al alto cargo (art. 2.1 Ley 3/2015). |
| `700ad0dd74` | FAIL | art. 2.2 Ley 3/2015 | out of order: in art. 2.2 this sentence precedes the one on supervening lack (`9d97965feb`); move it before that sentence | La honorabilidad debe concurrir en el alto cargo durante el ejercicio de sus funciones (art. 2.2 Ley 3/2015). |
| `9525cf6fc8` | PASS | art. 2.3 Ley 3/2015 | — | — |
| `093e79b580` | PASS | art. 2.4 Ley 3/2015 | — | — |
| `a61c283467` | PASS | art. 2.6 Ley 3/2015 | — | — |
| `4e32250284` | PASS | art. 2.6 Ley 3/2015 | — | — |
| `da84833d2e` | PASS | art. 2.8 Ley 3/2015 | — | — |
| `18322cacdf` | PASS | Ley 3/2015 (structure) | structure sentence | — |
| `89a0aeee50` | FAIL | Título I, arts. 3–10 Ley 3/2015 | names the unit wrongly: Título I is «Nombramiento y ejercicio del alto cargo» (it holds art. 2, treated above); the five principles of art. 3.1 and the headings of arts. 4–10 are right | Título I, nombramiento y ejercicio del alto cargo, en sus arts. 3 a 10: los principios de interés general, integridad, objetividad, transparencia y responsabilidad y austeridad (art. 3 Ley 3/2015), el régimen retributivo (art. 4 Ley 3/2015), la protección social (art. 5 Ley 3/2015), la compensación tras el cese (art. 6 Ley 3/2015), la incompatibilidad de retribuciones (art. 7 Ley 3/2015), los recursos humanos y materiales (art. 8 Ley 3/2015), la diligencia debida respecto de las actuaciones de los altos cargos (art. 9 Ley 3/2015) y la obligación de formación (art. 10 Ley 3/2015). |
| `58f61995ad` | PASS | arts. 11–18 Ley 3/2015 | eight headings, in order | — |
| `7fbb4dc738` | PASS | arts. 19–24 Ley 3/2015 | six headings, in order | — |
| `42b1213c68` | PASS | arts. 25–28 Ley 3/2015 | — | — |
| `27c39a5eda` | PASS | art. 170 Reglamento del Congreso | — | — |
| `d6cfd13143` | PASS | art. 171.2 Reglamento del Congreso | — | — |
| `f4cb6da7c5` | PASS | art. 171.5 Reglamento del Congreso | — | — |
| `ede1f82390` | PASS | art. 171.6 Reglamento del Congreso | — | — |
| `31ed718b0c` | FAIL | art. 172.1–2 Reglamento del Congreso | drops the organ the Presidencia also informs: «y lo comunicará a la Presidencia del Senado» | Si no se otorga, se tramitan sucesivas propuestas por el mismo procedimiento y, si transcurren dos meses a partir de la primera votación de investidura y ninguna candidatura propuesta ha obtenido la confianza del Congreso, la Presidencia de la Cámara somete a la firma del Rey el Decreto de disolución de las Cortes Generales y de convocatoria de elecciones, y lo comunica a la Presidencia del Senado (art. 172 Reglamento del Congreso). |
| `a1de79de74` | PASS | art. 173 Reglamento del Congreso | — | — |
| `dfd5b89824` | PASS | art. 174.1 Reglamento del Congreso | — | — |
| `0dd1faa09e` | PASS | art. 174.4 Reglamento del Congreso | — | — |
| `b35446d84d` | PASS | art. 174.5 Reglamento del Congreso | — | — |
| `6c7b8c337c` | PASS | art. 174.6 Reglamento del Congreso | — | — |
| `ce04c59a89` | PASS | art. 175.1 Reglamento del Congreso | — | — |
| `f214c3e7ed` | PASS | art. 175.2 Reglamento del Congreso | — | — |
| `104cdfd5e4` | FAIL | art. 176.2 Reglamento del Congreso | drops the conditions on the alternative motions: same requisites as art. 175.2 and same admission procedure as art. 176.1 | Dentro de los dos días siguientes a la presentación de la moción de censura pueden presentarse mociones alternativas, que deben reunir los mismos requisitos señalados en el apartado 2 del artículo 175 y están sometidas a los mismos trámites de admisión que la moción de censura (art. 176.2 Reglamento del Congreso). |
| `bf13b5cc8c` | PASS | art. 177.4–5 Reglamento del Congreso | — | — |
| `32b6e6a657` | PASS | art. 177.6 Reglamento del Congreso | — | — |
| `397ff72a53` | PASS | art. 178 Reglamento del Congreso | — | — |
| `d59b51e039` | FAIL | art. 179 Reglamento del Congreso | drops the rule that fixes the period for a motion filed between sessions | Quienes hayan firmado una moción de censura rechazada no pueden firmar otra durante el mismo período de sesiones; a estos efectos, la presentada en período entre sesiones se imputa al siguiente período de sesiones (art. 179 Reglamento del Congreso). |
| `2fa8145b54` | PASS | art. 1 LRJSP | — | — |
| `1e51c12ad2` | PASS | art. 2.1 LRJSP | lead-in; table a)–d) is the whole list | — |
| `ae8503f8a1` | PASS | art. 2.1 LRJSP | header row | — |
| `a4b3298776` | PASS | art. 2.1.a) LRJSP | — | — |
| `eb5110306d` | PASS | art. 2.1.b) LRJSP | — | — |
| `ef5df00cc6` | PASS | art. 2.1.c) LRJSP | — | — |
| `3b503ccbf7` | PASS | art. 2.1.d) LRJSP | — | — |
| `e190cc816e` | PASS | art. 2.3 LRJSP | «previstos en la letra a) del apartado 2» spelled out with art. 2.2.a)'s words | — |
| `f72c599893` | PASS | art. 4.1 LRJSP | — | — |
| `19e0e3d7ec` | PASS | art. 4.1 LRJSP | — | — |
| `bf2b394254` | FAIL | art. 4.2 LRJSP | glosses «requisitos previstos en la legislación que resulte aplicable» as «requisitos legales», cuts the list «hechos, actos, elementos, actividades, estimaciones y demás circunstancias» to «hechos y circunstancias» and drops «en el ámbito de sus respectivas competencias» | Las Administraciones Públicas velan por el cumplimiento de los requisitos previstos en la legislación que resulte aplicable, para lo cual pueden, en el ámbito de sus respectivas competencias y con los límites establecidos en la legislación de protección de datos de carácter personal, comprobar, verificar, investigar e inspeccionar los hechos, actos, elementos, actividades, estimaciones y demás circunstancias que fueran necesarias (art. 4.2 LRJSP). |
| `ed6a223af7` | PASS | art. 5.1 LRJSP | — | — |
| `e6581022c7` | PASS | art. 5.2 LRJSP | — | — |
| `9c63254e90` | PASS | art. 5.3 LRJSP | lead-in; table a)–c) is the whole list | — |
| `1dbeb3da77` | PASS | art. 5.3 LRJSP | header row | — |
| `ba9bd8c67e` | PASS | art. 5.3.a) LRJSP | — | — |
| `0ca722b2f2` | PASS | art. 5.3.b) LRJSP | — | — |
| `c1d601d626` | PASS | art. 5.3.c) LRJSP | — | — |
| `0fc5cc9d89` | PASS | art. 5.4 LRJSP | — | — |
| `9fe6f591c9` | PASS | art. 5.4 LRJSP | — | — |
| `b5da97bf54` | PASS | art. 6.1 LRJSP | — | — |
| `b947f1032a` | PASS | art. 6.1 LRJSP | — | — |
| `de77cb3bf1` | PASS | art. 6.2 LRJSP | — | — |
| `9c2c1e41eb` | FAIL | art. 7 LRJSP | cuts the article's lists: «dependencia jerárquica, ya sea orgánica o funcional» and «instrucciones, directrices o cualquier clase de indicación» | La Administración consultiva puede articularse mediante órganos específicos dotados de autonomía orgánica y funcional con respecto a la Administración activa, o a través de los servicios de esta última que prestan asistencia jurídica; en tal caso, dichos servicios no pueden estar sujetos a dependencia jerárquica, ya sea orgánica o funcional, ni recibir instrucciones, directrices o cualquier clase de indicación de los órganos que hayan elaborado las disposiciones o producido los actos objeto de consulta (art. 7 LRJSP). |
| `9d8964d2cb` | PASS | art. 7 LRJSP | — | — |
| `85e77b9b5d` | FAIL | art. 8.1 LRJSP | out of order: the first sentence of art. 8.1 sits after the second paragraph of 8.1 and after 8.2; move it to follow «La competencia es irrenunciable.» at the head of the section | La competencia se ejerce por los órganos administrativos que la tengan atribuida como propia, salvo los casos de delegación o avocación, cuando se efectúen en los términos previstos en la LRJSP u otras leyes (art. 8.1 LRJSP). |
| `92bb27f107` | PASS | art. 8.3 LRJSP | — | — |
| `c216a7b9b9` | FAIL | art. 9.1, párrafo segundo, LRJSP | out of order: it opens the second paragraph of art. 9.1 but sits after its last sentence (órganos no relacionados jerárquicamente) and after arts. 9.2.c) and 9.4; move it to follow «Los órganos podrán delegar … aun cuando no sean jerárquicamente dependientes.» and precede «Entre órganos de la Administración General del Estado no relacionados jerárquicamente…» | En el ámbito de la Administración General del Estado, la delegación de competencias debe ser aprobada previamente por el órgano ministerial de quien dependa el órgano delegante y, en el caso de los Organismos públicos o Entidades vinculados o dependientes, por el órgano máximo de dirección, de acuerdo con sus normas de creación (art. 9.1 LRJSP). |
| `19465d2a3b` | FAIL | art. 9.1, párrafo tercero, LRJSP | out of order: the third paragraph of art. 9.1 sits after arts. 9.2.c) and 9.4; move it to follow the sentence on órganos no relacionados jerárquicamente (end of art. 9.1, párrafo segundo) and precede «No se delega la resolución de recursos…» | Los órganos de la Administración General del Estado pueden delegar también el ejercicio de sus competencias propias en sus Organismos públicos y Entidades vinculados o dependientes, cuando resulte conveniente para alcanzar los fines que tengan asignados y mejorar la eficacia de su gestión; la delegación debe ser previamente aprobada por los órganos de los que dependan el órgano delegante y el órgano delegado, o aceptada por este último cuando sea el órgano máximo de dirección del Organismo público o Entidad vinculado o dependiente (art. 9.1 LRJSP). |
| `884bba6a19` | PASS | art. 9.2 LRJSP | lead-in; table a)–d) is the whole list | — |
| `9f46d1c436` | PASS | art. 9.2 LRJSP | header row | — |
| `89116fe6ea` | PASS | art. 9.2.a) LRJSP | — | — |
| `7b2e0a4ffd` | PASS | art. 9.2.b) LRJSP | — | — |
| `f05441dca0` | PASS | art. 9.2.c) LRJSP | — | — |
| `bc0cd900e3` | PASS | art. 9.2.d) LRJSP | — | — |
| `990d7a8510` | PASS | art. 9.3 LRJSP | — | — |
| `f97bf2d48f` | PASS | art. 9.5 LRJSP | — | — |
| `08c68e6896` | PASS | art. 9.5 LRJSP | — | — |
| `f8dec50a82` | PASS | art. 9.6 LRJSP | — | — |
| `56dd098641` | PASS | art. 9.7 LRJSP | — | — |
| `721d8631de` | FAIL | art. 13.2 LRJSP | out of order: art. 13.2 says first that suplencia does not alter competence, then that its validity needs no publication; the lesson has them reversed; move this sentence before «Para la validez de la suplencia no es necesaria su publicación (art. 13.2 LRJSP).» | La suplencia no implica alteración de la competencia (art. 13.2 LRJSP). |
| `75df19a3ff` | PASS | art. 13.3 LRJSP | a)–b) is the whole list | — |
| `230cd8aef6` | PASS | art. 13.4 LRJSP | — | — |
| `505071ae47` | PASS | art. 21.3 LRJSP | — | — |
| `3a85507141` | FAIL | art. 15.1 LRJSP | wrong unit: art. 15.1 refers to «la presente sección», which is sección 3.ª (arts. 15–22), not arts. 15–18 (subsección 1.ª); also «Administraciones Públicas en que se integran» | El régimen jurídico de los órganos colegiados se ajusta a las normas de la sección 3.ª del capítulo II del título preliminar de la LRJSP (arts. 15 a 22), sin perjuicio de las peculiaridades organizativas de las Administraciones Públicas en que se integran (art. 15.1 LRJSP). |
| `7dc3c397a6` | FAIL | art. 15.2 LRJSP | the first paragraph of 15.2 is cut (drops «cuenten o no con participación de organizaciones representativas de intereses sociales») and its tail glosses the second paragraph («salvo que sus normas de creación, sus funciones o su naturaleza lo establezcan» for «salvo que así lo establezcan sus normas de creación, se desprenda de sus funciones o de la propia naturaleza»), which `be4984ae79` states in the norm's words | Los órganos colegiados de las distintas Administraciones Públicas en que participen organizaciones representativas de intereses sociales, así como aquellos compuestos por representaciones de distintas Administraciones Públicas, cuenten o no con participación de organizaciones representativas de intereses sociales, pueden establecer o completar sus propias normas de funcionamiento (art. 15.2 LRJSP). |
| `de7a50588f` | PASS | art. 15.3 LRJSP | — | — |
| `e953cdadaa` | FAIL | art. 16.1–2 LRJSP | «certifica» has lost its object («certificar las actuaciones del mismo»); «la Administración» for «la Administración Pública correspondiente» | Tienen un Secretario, que puede ser un miembro del propio órgano o una persona al servicio de la Administración Pública correspondiente, y al que corresponde velar por la legalidad formal y material de las actuaciones del órgano colegiado, certificar las actuaciones del mismo y garantizar que los procedimientos y reglas de constitución y adopción de acuerdos son respetadas (art. 16.1–2 LRJSP). |
| `c7195eb904` | PASS | art. 17.1 LRJSP | — | — |
| `a71e28e5ce` | FAIL | art. 17.2 LRJSP | drops «presencial o a distancia» (the attendance that counts) and «a efectos de la celebración de sesiones, deliberaciones y toma de acuerdos» | Para la válida constitución del órgano, a efectos de la celebración de sesiones, deliberaciones y toma de acuerdos, se requiere la asistencia, presencial o a distancia, del Presidente y Secretario o, en su caso, de quienes les suplan, y la de la mitad, al menos, de sus miembros (art. 17.2 LRJSP). |
| `6fb96d1604` | PASS | art. 17.4 LRJSP | — | — |
| `0692c3f13a` | PASS | art. 17.5 LRJSP | — | — |
| `37e881dfea` | PASS | art. 18.1 LRJSP | — | — |
| `51400e9462` | PASS | art. 18.2 LRJSP | — | — |
| `be4984ae79` | FAIL | art. 15.2, párrafo segundo, LRJSP | wording right; out of order: paragraphs 680–686 go back over arts. 15–18 after line 678 has reached art. 18.2; move it to follow `7dc3c397a6` | Los órganos colegiados del artículo 15.2 quedan integrados en la Administración Pública que corresponda, aunque sin participar en la estructura jerárquica de esta, salvo que así lo establezcan sus normas de creación, se desprenda de sus funciones o de la propia naturaleza del órgano colegiado (art. 15.2 LRJSP). |
| `af3e081b38` | FAIL | art. 15.3 LRJSP | wording right; out of order; move it to follow `de7a50588f` | Adicionalmente, las Administraciones pueden publicar el acuerdo de creación y las normas de funcionamiento en otros medios de difusión que garanticen su conocimiento (art. 15.3 LRJSP). |
| `9680e05c28` | FAIL | art. 15.3, párrafo segundo, LRJSP | wording right; out of order; move it to follow `af3e081b38` | Cuando se trate de un órgano colegiado del artículo 15.2, la publicidad la realiza la Administración a quien corresponda la Presidencia (art. 15.3 LRJSP). |
| `a2168d5ba3` | FAIL | art. 16.3 LRJSP | wording right; out of order; move it to follow `e953cdadaa` | Si el Secretario no miembro es suplido por un miembro del órgano colegiado, este conserva todos sus derechos como tal (art. 16.3 LRJSP). |
| `b38efdbff9` | FAIL | art. 17.1, párrafo segundo, LRJSP | wording right; out of order; move it to follow `c7195eb904` | En las sesiones que se celebren a distancia, los miembros pueden encontrarse en distintos lugares siempre que se asegure por medios electrónicos, considerándose también tales los telefónicos y audiovisuales, la identidad de los miembros o personas que los suplan, el contenido de sus manifestaciones, el momento en que estas se producen, así como la interactividad e intercomunicación entre ellos en tiempo real y la disponibilidad de los medios durante la sesión (art. 17.1 LRJSP). |
| `dcc7523704` | FAIL | art. 17.1, párrafo segundo, LRJSP | wording right («entre otros» is the article's own, quoted); out of order; move it to follow `b38efdbff9` | Se consideran incluidos entre los medios electrónicos válidos, «entre otros», el correo electrónico, las audioconferencias y las videoconferencias (art. 17.1 LRJSP). |
| `37dcaa3be1` | FAIL | art. 17.2, párrafo segundo, LRJSP | wording right; out of order; move it to follow `a71e28e5ce` | Cuando se trate de los órganos colegiados del artículo 15.2, el Presidente puede considerar válidamente constituido el órgano, a efectos de celebración de sesión, si asisten los representantes de las Administraciones Públicas y de las organizaciones representativas de intereses sociales miembros del órgano a los que se haya atribuido la condición de portavoces (art. 17.2 LRJSP). |
| `86e99a93b2` | FAIL | art. 17.2, párrafo tercero, LRJSP | wording right; out of order; move it to follow `37dcaa3be1` | Cuando estén reunidos, de manera presencial o a distancia, el Secretario y todos los miembros del órgano colegiado, o en su caso las personas que les suplan, pueden constituirse válidamente como órgano colegiado para la celebración de sesiones, deliberaciones y adopción de acuerdos sin necesidad de convocatoria previa cuando así lo decidan todos sus miembros (art. 17.2 LRJSP). |
| `262a6e4031` | FAIL | art. 17.3 LRJSP | wording right; out of order; move it to follow `86e99a93b2`, before `6fb96d1604` (art. 17.4) | Los órganos colegiados pueden establecer el régimen propio de convocatorias, si no está previsto por sus normas de funcionamiento, y tal régimen puede prever una segunda convocatoria y especificar para esta el número de miembros necesarios para constituir válidamente el órgano (art. 17.3 LRJSP). |
| `61c4c1a205` | FAIL | art. 17.3, párrafo segundo, LRJSP | wording right; out of order; move it to follow `262a6e4031` | Salvo que no resulte posible, las convocatorias se remiten a los miembros a través de medios electrónicos, haciendo constar en ellas el orden del día junto con la documentación necesaria para su deliberación cuando sea posible, las condiciones en las que se va a celebrar la sesión, el sistema de conexión y, en su caso, los lugares en que estén disponibles los medios técnicos necesarios para asistir y participar en la reunión (art. 17.3 LRJSP). |
| `817b228bd8` | FAIL | art. 17.5 LRJSP | wording right; out of order; move it to follow `0692c3f13a` | Cuando se asista a distancia, los acuerdos se entienden adoptados en el lugar donde tenga la sede el órgano colegiado y, en su defecto, donde esté ubicada la presidencia (art. 17.5 LRJSP). |
| `b478ad4662` | FAIL | art. 17.6 LRJSP | wording right; out of order; move it to follow `817b228bd8` | Los miembros que voten en contra o se abstengan quedan exentos de la responsabilidad que, en su caso, pueda derivarse de los acuerdos (art. 17.6 LRJSP). |
| `1c3b9feb0c` | FAIL | art. 17.7 LRJSP | wording right; out of order; move it to follow `b478ad4662`, before `37e881dfea` (art. 18.1) | Quienes acrediten la titularidad de un interés legítimo pueden dirigirse al Secretario de un órgano colegiado para que les sea expedida certificación de sus acuerdos; la certificación se expide por medios electrónicos, salvo que el interesado manifieste expresamente lo contrario y no tenga obligación de relacionarse con las Administraciones por esta vía (art. 17.7 LRJSP). |
| `aa0415a146` | FAIL | art. 18.1, párrafo segundo, LRJSP | wording right; out of order; move it to follow `37e881dfea` | Pueden grabarse las sesiones que celebre el órgano colegiado; el fichero resultante de la grabación, junto con la certificación del Secretario de la autenticidad e integridad del mismo y cuantos documentos en soporte electrónico se utilicen como documentos de la sesión, pueden acompañar al acta, sin necesidad de hacer constar en ella los puntos principales de las deliberaciones (art. 18.1 LRJSP). |
| `0b117320ee` | FAIL | art. 18.2 LRJSP | wording right; out of order; move it to follow `51400e9462` (art. 18.2's last paragraph, on keeping the recordings, is still untreated) | El Secretario elabora el acta con el visto bueno del Presidente y la remite a través de medios electrónicos a los miembros del órgano colegiado, quienes pueden manifestar por los mismos medios su conformidad o reparos al texto, a efectos de su aprobación, considerándose, en caso afirmativo, aprobada en la misma reunión (art. 18.2 LRJSP). |
| `d2023131ae` | PASS | RD 1009/2023 (title and preámbulo) | the title gives «estructura orgánica básica de los departamentos ministeriales»; the preámbulo: «En el articulado se determinan los órganos directivos … hasta el nivel de Dirección General» | — |
| `1fdbaa8111` | PASS | art. 64.3, párrafo segundo, LRJSP | the inherited art. 64.2 sentence that follows it belongs before the art. 64.3 sentences (structural note, not this row) | — |
| `6769bacf3c` | PASS | art. 69.2 LRJSP | — | — |
| `64b1ace5de` | PASS | art. 75.b) LRJSP | «A estos efectos» spelled out | — |
| `9fdac4141d` | PASS | art. 76.1 LRJSP | — | — |
| `81ff80a652` | PASS | art. 76.2 LRJSP | — | — |
| `685ac1196e` | PASS | art. 2.2.b) LRJSP | — | — |
| `022d4cebae` | PASS | art. 2.2.c) LRJSP | — | — |
| `c871209366` | PASS | art. 84.3 LRJSP | — | — |
| `918eb4b7d0` | PASS | art. 83.1 LRJSP | — | — |
| `0fab5b2969` | PASS | art. 83.2.a) LRJSP | — | — |
| `12f0095b93` | PASS | art. 89.2, párrafo segundo, LRJSP | — | — |
| `5705b605e4` | PASS | art. 91.2 LRJSP | a)–b) is the whole list | — |
| `9f8dfa9b7a` | PASS | art. 91.3 LRJSP | — | — |
| `6895fe0f84` | PASS | art. 100.1, párrafo segundo, LRJSP | — | — |
| `f5d7ae1768` | PASS | art. 100.1, párrafo tercero, LRJSP | — | — |
| `a2963c4627` | PASS | art. 100.1, párrafo cuarto, LRJSP | — | — |
| `134f3498de` | PASS | art. 100.2 LRJSP | — | — |
| `20670e4a8e` | PASS | art. 106.2 LRJSP | a)–b) is the whole list | — |
| `a475dd1db7` | PASS | art. 106.4 LRJSP | — | — |
| `672c54a965` | PASS | art. 106.5 LRJSP | — | — |
| `bab3cbf2f5` | PASS | art. 106.6 LRJSP | — | — |
| `0f304b6685` | FAIL | art. 110.1 LRJSP | the list of supplementary norms is cut: it leaves out the LPAC, the Ley 47/2003, the RDLeg 3/2011 and the Ley 33/2003, which the article names between «organismos autónomos» and «el resto de las normas» | Supletoriamente y en cuanto sea compatible con su naturaleza y autonomía, se rigen por lo dispuesto en la LRJSP, en particular lo dispuesto para organismos autónomos, la Ley del Procedimiento Administrativo Común de las Administraciones Públicas, la Ley 47/2003, de 26 de noviembre, el Real Decreto Legislativo 3/2011, de 14 de noviembre, la Ley 33/2003, de 3 de noviembre, así como el resto de las normas de derecho administrativo general y especial que les sea de aplicación; en defecto de norma administrativa, se aplica el derecho común (art. 110.1 LRJSP). |
| `73e6d13411` | FAIL | art. 110.2 LRJSP | drops the norm the article ties the principle to: «de acuerdo con lo previsto en la Ley Orgánica 2/2012, de 27 de abril» (the Normativa block then needs a line naming LO 2/2012) | Las autoridades administrativas independientes están sujetas al principio de sostenibilidad financiera de acuerdo con lo previsto en la Ley Orgánica 2/2012, de 27 de abril (art. 110.2 LRJSP). |
| `21b1d3ea91` | PASS | art. 118.2 LRJSP | the inherited art. 118.4 sentence before it belongs after `f81cfc4cce` (structural note) | — |
| `f81cfc4cce` | PASS | art. 118.3 LRJSP | — | — |
| `be964e8e51` | PASS | art. 119.2 LRJSP | — | — |
| `aaf2628296` | PASS | art. 119.3 LRJSP | — | — |
| `836af9c8ad` | FAIL | art. 120.2 LRJSP | «Según estos criterios» has no antecedent where it sits (the sentence before is art. 120.3, on ánimo de lucro); the article says «De acuerdo con los siguientes criterios». The inherited art. 120.3 sentence belongs after the table (structural note) | De acuerdo con los siguientes criterios, ordenados por prioridad en su aplicación y referidos a la situación en el primer día del ejercicio presupuestario, el consorcio queda adscrito, en cada ejercicio presupuestario y por todo este periodo, a la Administración Pública que (art. 120.2 LRJSP): |
| `50b9c5debc` | PASS | art. 120.2 LRJSP | header row | — |
| `75b1111576` | PASS | art. 120.2.a) LRJSP | — | — |
| `efaa817770` | PASS | art. 120.2.b) LRJSP | — | — |
| `538210c229` | PASS | art. 120.2.c) LRJSP | — | — |
| `c56d50ef45` | PASS | art. 120.2.d) LRJSP | — | — |
| `8d4e50777a` | PASS | art. 120.2.e) LRJSP | — | — |
| `78045385ec` | PASS | art. 120.2.f) LRJSP | — | — |
| `aa511a25ac` | PASS | art. 120.2.g) LRJSP | — | — |
| `2b6bd78977` | PASS | art. 120.2.h) LRJSP | — | — |
| `754dce056c` | PASS | art. 120.4 LRJSP | — | — |
| `f71b2dee87` | PASS | art. 133.1 LRJSP | — | — |
| `0ce31075e9` | PASS | art. 133.2 LRJSP | — | — |
| `1d611b25d9` | PASS | art. 133.3 LRJSP | — | — |
| `6b51d14fbd` | PASS | Normativa: Reglamento del Congreso | cites arts. 170, 171.2, 171.5–6, 172, 173, 174.1, 174.4–6, 175.1–2, 176.2, 177.4–6, 178, 179; the pending change of `normativa.yaml` touches only art. 23, so no note is owed | — |
| `e300e9c000` | PASS | Normativa: LO 3/1980 | cites arts. 1 and 2.1–2.2; also named as «su Ley Orgánica» in DA 2.ª Ley 50/1997 | — |
| `baa57aee11` | PASS | Normativa: Ley 3/2015 | arts. 1.1–1.3 and 2.1–2.8 cited; arts. 3–10 one by one and 11–28 by ranges | — |
| `664018dbc9` | PASS | Normativa: LRJSP | every article cited lies in 1–10, 13–22, 54–139 (incl. 55 bis, 84 bis, 108 bis–sexies) and every article of those ranges is cited singly or by a cited range; arts. 11–12 and 23–53 are not cited | — |
| `2263c7659b` | PASS | Normativa: Ley 47/2003 | named in art. 55.11.b) («Ley General Presupuestaria»), art. 61 (two rows) and art. 84.3 LRJSP; if the replacement of `0f304b6685` is applied, art. 110.1 joins the list | — |
| `84311266b7` | PASS | Normativa: norms named, not in `normativa.yaml` | RDLeg 3/2011 in arts. 62.2.e) and 104; Ley de Contratos del Sector Público in art. 103.1; Ley 2/2014 in art. 80; Ley de Fundaciones in art. 130; LOFAGE in art. 7.3 Ley 50/1997; Reglamento del Consejo de Estado in DA 2.ª Ley 50/1997; none has a `normativa.yaml` entry. If the replacement of `73e6d13411` is applied, LO 2/2012 (excluded in the `normativa.yaml` header) joins this line with «art. 110.2 LRJSP» | — |
| `624e9a1cef` | FAIL | Normativa: norms named in Ley 3/2015 and LRJSP | says none of the five is in `normativa.yaml`, but «Ley 19/2013 (transparencia)» (BOE-A-2013-12887) and «LBRL (Ley 7/1985)» (BOE-A-1985-5392) are; add two lines: «Ley 19/2013 (transparencia): nombrada en el art. 2.2 Ley 3/2015 y en el art. 6.1 LRJSP.» and «LBRL (Ley 7/1985): nombrada en el art. 119.3 LRJSP.» | Ley 22/2003 (Concursal), Ley 27/2013 (racionalización de la Administración Local) y RDLeg 1/2010 (Ley de Sociedades de Capital): nombradas en el art. 2.2 Ley 3/2015 y en el art. 119.2–3 LRJSP; no figuran en `normativa.yaml`. |

Findings outside the pending rows (no verdict; for the coordinator):

- Normativa block: the lesson names the Ley Orgánica del Tribunal Constitucional («en los términos de la Ley Orgánica reguladora del mismo», art. 29.4 Ley 50/1997, line 363), which `normativa.yaml` has as «LO 2/1979 (LOTC)»; no Normativa line names it. Line owed: «LO 2/1979 (LOTC): nombrada en el art. 29.4 Ley 50/1997.»
- Inherited sentences that drop the Ley 7/2007 reference: «Su personal es funcionario o laboral (art. 100.1 LRJSP).» (art. 100.1: «se regirá por lo previsto en la Ley 7/2007, de 12 de abril, y demás normativa reguladora de los funcionarios públicos y por la normativa laboral») and the two art. 106.1 sentences at lines 1156 and 1164 («quienes se regirán por lo previsto en la Ley 7/2007, de 12 de abril y demás normativa reguladora de los funcionarios públicos o por la normativa laboral»). If they are rewritten, TREBEP gets a Normativa line.
- Inherited sentences out of the norm's order (structural): art. 64.2 sentence after the art. 64.3 sentences (line 892); art. 118.4 sentence before arts. 118.2–3 (line 1219); art. 120.3 sentence before the art. 120.2 table (line 1221); art. 9.4 and 9.2.c) sentences before the art. 9.1 sentences of line 551.
- Inherited «Los órganos de la Administración General del Estado y de las Entidades de Derecho Público … (art. 19.1)» block: arts. 19–22 (subsección 2.ª) precede arts. 15–18 (subsección 1.ª) in the lesson.

PASS 152 · FAIL 39
