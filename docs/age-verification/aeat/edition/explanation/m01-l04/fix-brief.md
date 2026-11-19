# Fix brief — `m01-l04`

## caso:### Reforma#1

Current: La Comunidad A aprobó su Estatuto por la vía del artículo 151 y la Comunidad B, por una vía distinta. La reforma del Estatuto de B se ajusta al procedimiento que él mismo establece y requiere la aprobación de las Cortes Generales mediante ley orgánica; no exige referéndum (art. 147.3 CE). La reforma del Estatuto de A exige además un referéndum entre los electores inscritos en los censos correspondientes (art. 152.2 CE).

Blind verifier: FAIL — «La reforma del Estatuto de B… no exige referéndum (art. 147.3 CE)»: el art. 147.3 no excluye el referéndum; remite al «procedimiento establecido en los mismos» más la ley orgánica de las Cortes, y ese procedimiento estatutario puede incluir un referéndum (p. ej. el Estatuto valenciano reformado en 2006, aprobado por vía no 151, lo exige). Lo correcto: la CE solo impone el referéndum a los Estatutos del art. 151 (art. 152.2); para los demás depende de lo que diga cada Estatuto.
Student reader: KEEP — The A/B contrast shows exactly when a referéndum is or is not required.

## caso:### Cláusulas de cierre#1

Current: Una materia no está atribuida expresamente al Estado por la Constitución y el Estatuto de la Comunidad D la asume: puede corresponder a D (art. 149.3 CE). Otra materia no la asume ningún Estatuto: corresponde al Estado (art. 149.3 CE). En caso de conflicto, las normas del Estado prevalecen en todo lo que no esté atribuido a la exclusiva competencia de las Comunidades, y el derecho estatal es supletorio (art. 149.3 CE).

Blind verifier: PASS — Las tres reglas del art. 149.3 (materias no atribuidas expresamente al Estado «podrán» corresponder a las CCAA vía Estatuto; las no asumidas, al Estado; prevalencia salvo competencia exclusiva autonómica y supletoriedad) están bien.
Student reader: REWRITE — "Una materia" and "otra materia" are abstract; use concrete subjects so I can see which rule of art. 149.3 applies.

## caso:### Leyes marco, transferencia o delegación y armonización#1

Current: El Estado quiere armonizar las disposiciones normativas de varias Comunidades en una materia atribuida a su competencia, porque lo exige el interés general (art. 150.3 CE). La apreciación de esta necesidad corresponde a las Cortes Generales, por mayoría absoluta de cada Cámara (art. 150.3 CE). Para transferir o delegar facultades de titularidad estatal, el Estado puede usar una ley orgánica, que prevé en cada caso la transferencia de medios financieros (art. 150.2 CE).

Blind verifier: FAIL — (1) «armonizar… en una materia atribuida a su competencia»: «su» se lee como la del Estado, pero el art. 150.3 permite las leyes de armonización «aun en el caso de materias atribuidas a la competencia de éstas» (las CCAA), que es justamente su rasgo. (2) «el Estado puede usar una ley orgánica» para transferir o delegar «facultades de titularidad estatal»: el art. 150.2 exige la ley orgánica («mediante ley orgánica»; no es una opción) y solo para facultades «que por su propia naturaleza sean susceptibles de transferencia o delegación», condición omitida; la ley prevé también las formas de control que se reserve el Estado.
Student reader: REWRITE — It skips leyes marco and does not contrast the three techniques; give one short scenario per technique.

## caso:### El Alcalde#1

Current: La Alcaldesa Rosa nombra a los Tenientes de Alcalde (art. 21.2 LBRL). Delega una de sus atribuciones, algo que el Alcalde puede hacer (art. 21.3 LBRL). No puede delegar la convocatoria y presidencia de las sesiones del Pleno y de la Junta de Gobierno Local ni la decisión de los empates con el voto de calidad (art. 21.3 LBRL).

Blind verifier: PASS — Nombramiento de Tenientes de Alcalde (art. 21.2); delegación permitida salvo, entre otras, convocar y presidir Pleno y Junta de Gobierno Local y decidir empates con voto de calidad (art. 21.3); no presenta la lista como completa.
Student reader: REWRITE — "Delega una de sus atribuciones" is vague; name a delegable power (e.g. licencias) and a non-delegable one (e.g. dictar bandos) so I can tell them apart.

## caso:### La Presidencia#1

Current: En el segundo semestre de 2026 Irlanda ejerce la Presidencia del Consejo y preside durante seis meses todas las formaciones salvo la de Asuntos Exteriores (arts. 16.9 TUE y 1.4 Reglamento interno del Consejo; anexo I Decisión 2009/908/UE). El Alto Representante preside el Consejo de Asuntos Exteriores (art. 18.3 TUE). Irlanda forma con Lituania y Grecia un grupo que ejerce la Presidencia durante dieciocho meses (art. 1.4 Reglamento interno del Consejo).

Blind verifier: PASS — Comprobado en el PDF: el anexo I de la Decisión 2009/908/UE (sustituido por la Decisión 2016/1316) fija Irlanda julio-diciembre 2026, en el grupo Irlanda–Lituania–Grecia (julio 2026–diciembre 2027); el art. 1.4 del anexo del Reglamento interno (el extracto de la entrada tomó por error el art. 1 de la Decisión) fija grupos de tres durante dieciocho meses y presidencia de seis meses de todas las formaciones salvo Asuntos Exteriores; el Alto Representante la preside (art. 18.3 TUE).
Student reader: REWRITE — Right idea (Ireland in H2 2026, Foreign Affairs chaired by the Alto Representante) but three stacked citations make it hard to follow.

## caso:### Las mayorías#1

Current: El Consejo, con 27 miembros, vota una propuesta de la Comisión. La mayoría cualificada exige al menos el 55 % de los miembros, que incluya al menos a quince, y Estados con al menos el 65 % de la población de la Unión (art. 16.4 TUE). Votan a favor 16 Estados con el 68 %, y se alcanza. Si el Consejo no actuara a propuesta de la Comisión, haría falta el 72 % de los miembros (art. 238.2 TFUE).

Blind verifier: FAIL — «Si el Consejo no actuara a propuesta de la Comisión, haría falta el 72 % de los miembros (art. 238.2 TFUE)»: el art. 238.2 se aplica cuando el Consejo no actúa a propuesta «de la Comisión o del Alto Representante» (a propuesta del Alto Representante sigue bastando el 55 %) y exige además que esos miembros «represente[n] a Estados miembros que reúnan como mínimo el 65 % de la población»; ambas condiciones se omiten. La primera parte es correcta: con 27 miembros el 55 % exige 15, y 16 Estados con el 68 % alcanzan la mayoría (art. 16.4 TUE).
Student reader: KEEP — 27 members, 16 states, 68 % checked against 55 %/15/65 %, then the 72 % variant.

