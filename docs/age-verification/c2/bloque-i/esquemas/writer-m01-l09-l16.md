# Esquema writer notes, C2 bloque I, m01-l09 … m01-l16 (2026-11-06)

## m01-l09 (C1 sources: m01-l09, m01-l10)

Esquemas added (4):

1. «Las vías de acceso a la autonomía de los artículos 143 y 151», tabla, after the paragraph «La diferencia entre las dos vías está en las cifras…». C1 origin: m01-l09 same title. Header and both rows NEW (5 columns). C1's table had a «Proyecto de Estatuto» column; the 151 row's cell for it rests on art. 151.2 CE, which the C2 prose does not cite or state, so the column went and the table is rebuilt (cells otherwise copied from C1's cells). Citation of the 151 row: art. 151.1 CE (C1: «151.1–2»). The «—» in the Ratificación cell of the 143 row is C1's own and says only that art. 143 has none; the verifier should judge it.
2. «Cinco materias en las dos listas de los artículos 148.1 y 149.1», tabla, after the paragraph «El examen mezcla materias de las dos listas…». C1 origin: m01-l09 same title. Header + 5 rows inherited, 0 dropped, 0 new.
3. «Leyes marco, transferencia o delegación y armonización», tabla, after the armonización paragraph (art. 150.3 CE). C1 origin: m01-l09 same title. Header + 3 rows inherited, 0 dropped, 0 new.
4. «Existencia, Pleno y Junta de Gobierno en el ayuntamiento y en la Diputación», tabla, after the Vicepresidentes paragraph (art. 35.4 LBRL). C1 origin: m01-l10 «Pleno, Junta de Gobierno, Tenientes de Alcalde y Vicepresidentes…». Header + 3 rows inherited; the «Tenientes de Alcalde y Vicepresidentes» row DROPPED: C1's Diputación cell says Vicepresidentes are «libremente designados», the C2 prose says only «los designa». Title rewritten to name the three rows left (new title, verified as a title).

Considered and not made: C1 m01-l10 «El municipio, la provincia y la isla en la Constitución» (rows would inherit; left out for the four-per-lesson cap, the prose is three short paragraphs; weaker exam weight than organs/majorities/plazos). Entidades locales (art. 3 LBRL), servicios mínimos, competencias del Estado, artículo 155: already a list or table in the prose.

Rows: inherited 12 (incl. 3 headers) / new 3 / dropped 1 row (+ the unmade 3-row esquema).
prov.sh plan: `m01-l09: 249 inherited, 17 verified, 3 pending` (pending = the 3 new vías lines only).

## m01-l10 (C1 source: m01-l11)

Environment note: `prov.sh plan m01-l10 m01-l11` raises `LookupError: no C1 report known for commit 10dbeef` for the inherited intro sentence «Este tema se estudia en dos tratados…» (C1 m01-l11 line 3 was edited in commit 10dbeef, which `_C1_REPORTS` does not know). Not an esquema issue; I ran the plan through a scratch wrapper that tolerates the lookup (pending output is the real one). The coordinator needs a `_C1_REPORTS` marker or `_C1_SENTENCE_REPORTS` entry for it.

Esquemas added (4):

1. «Composición del Consejo Europeo, el Consejo, el Parlamento Europeo y la Comisión», tabla, after the paragraph ending «(art. 247 TFUE)» (end of «El Presidente y los acuerdos»). C1 origin: m01-l11 same title. Header + 4 rows inherited. Placement matters: a header's governing citation is the previous cited sentence, so it must follow the art. 247 TFUE paragraph as in C1 or it does not inherit.
2. «Algunas reglas de votación del Consejo Europeo, el Consejo, el Parlamento Europeo y la Comisión», tabla, directly after esquema 1. C1 origin: m01-l11 same title. Header + 11 rows inherited; 2 NEW rows: «Consejo, en las cuestiones de procedimiento y para la aprobación de su reglamento interno | Se pronunciará por mayoría simple | art. 240.3 TFUE» (a «Lo que más cae» fact, 240.3 TFUE p. of tfue pdf, art. 240 apartado 3) and «Parlamento Europeo, para aprobar la moción de censura sobre la gestión de la Comisión | Mayoría de dos tercios de los votos emitidos que representen, a su vez, la mayoría de los diputados que componen el Parlamento Europeo | art. 234 TFUE».
3. «El Tribunal de Justicia de la Unión Europea», arbol, after the Tribunal General paragraph (ends «curia-tribunal-general.html»). C1 origin: m01-l11 same title. 4 nodes inherited.
4. «Duración de algunos mandatos en las instituciones de la Unión», tabla, directly after the arbol. No C1 esquema: new header + 5 new rows (art. 15.5 TUE, 14.3 TUE, 17.3 TUE, 253 TFUE twice); cells are verbatim fragments of the articles; «algunos» in the title because the list is selective (no Consejo mandate, no Tribunal General).

Considered and not made: Nombramiento de la Comisión (already a numbered list in the prose), instituciones (list), recursos (narrative).

Rows: inherited 21 (2 headers, 15 rows, 4 nodes) / new 8 (1 header + 7 rows) / dropped 0.
prov.sh plan: `m01-l10: 165 inherited, 16 verified, 8 pending` (pending = my 8 new lines only).

## m01-l11 (C1 sources: m03-l03, m03-l02)

Esquemas added (4), all fully inherited:

1. «Desde cuándo produce efectos el acto: la regla general, la eficacia demorada y la retroactividad», tabla, after the Efectos paragraph (art. 39.3 LPAC). C1 origin: m03-l02 «Desde cuándo produce efectos el acto». Header + 3 rows inherited; the «Los actos producidos por silencio administrativo | … | art. 24.4 LPAC» row DROPPED (the C2 prose cites art. 24.4 only for the certificado, not for the efectos of the silencio). Title rewritten (new title) because without the silencio row the old one read as complete.
2. «Plazos de la notificación», plazos, after the Notificación electrónica paragraph (art. 43.2 LPAC). C1 origin: m03-l02 same title. 3 steps inherited.
3. «Cómputo de plazos», tabla, after the paragraph «Los plazos en meses o años…» (arts. 30.4–5 y 122.1 LPAC). C1 origin: m03-l03 same title. Header + 4 rows inherited.
4. «Plazos de los recursos administrativos», tabla, after the extraordinario de revisión paragraph (art. 126.3 LPAC). C1 origin: m03-l03 same title. Header + 3 rows inherited.

Considered and not made (cap of four): «Los recursos administrativos» (m03-l03; 3 rows would inherit), «Plazos del procedimiento administrativo común» (m03-l03; row 8 «Emisión de informes» cannot inherit because the C2 prose says only «salvo otro plazo» for art. 80.2, and dropping it renumbers rows 9–12 into new rows), «Conversión, conservación y convalidación» (m03-l02; 5 rows would inherit). Any of them can be added by the coordinator if a fifth is wanted.

Rows: inherited 16 lines (efectos 4, notificación 3, cómputo 5, plazos de recursos 4) / new 0 / dropped 1.
prov.sh plan: `m01-l11: 236 inherited, 63 verified, 0 pending`.

## m01-l12 (C1 source: m02-l04)

Esquemas added (2):

1. «Algunos derechos del interesado», tabla, after the Decisiones individuales automatizadas paragraph (art. 22.4 RGPD). C1 origin: m02-l04 same title. Header + 9 rows inherited (acceso x3, rectificación x2, supresión, portabilidad, oposición por mercadotecnia, decisiones automatizadas); 1 row DROPPED: «Oposición, por motivos relacionados con su situación particular | … | art. 21.1 RGPD», because the C2 prose cuts «sobre los intereses, los derechos y las libertades del interesado» from the exception («motivos legítimos imperiosos que prevalezcan o los necesite…»).
2. «Plazos de respuesta del responsable y del delegado de protección de datos», tabla, after «Reclamaciones ante el delegado» (art. 37.2 LOPDGDD). C1 origin: m02-l04 «Plazos de respuesta a las solicitudes y reclamaciones». 3 rows inherited (art. 12.3 RGPD, 37.1 and 37.2 LOPDGDD); the «La Agencia, sobre la admisión a trámite…» row (art. 65.5 LOPDGDD) DROPPED, the C2 lesson does not cover it. Title rewritten (new title) to name the two responders left. The HEADER is NEW (1 pending line): a header's governing citation is the previous cited sentence and C1's was art. 65.5 LOPDGDD, which C2 does not cite.

Considered and not made: «La Presidencia de la AEPD y su Adjunto», «Prescripción de las sanciones» (C2 lesson does not cover the AEPD or the infracciones); principios, licitud, supresión exceptions, DPD designation (already lists in the prose).

Rows: inherited 13 lines (derechos: header + 9 = 10; plazos: 3) / new 1 (header) / dropped 2.
prov.sh plan: `m01-l12: 107 inherited, 25 verified, 1 pending`.

## m01-l13 (C1 sources: m04-l01 … m04-l05)

Esquemas added (4):

1. «Plazos de solicitud, informe y nombramiento en la libre designación», plazos, after the paragraph ending «(art. 58.2 RD 364/1995)» (end of «Libre designación»). C1 origin: m04-l05 «Plazos de la libre designación». 3 steps inherited. Title new (C1's read as the full list of plazos; the cese/toma de posesión plazos are in the next section and not in the list).
2. «Plazos del concurso», plazos, after the «Toma de posesión y cese» bullet list (art. 48.3 RD 364/1995). C1 origin: m04-l05 same title. Steps 1–2 inherited; steps 3 (Cese) and 4 (Toma de posesión) are NEW: C1's text says «publicación de la resolución del concurso en el «Boletín Oficial del Estado»» (step 3) and «desde la publicación de la resolución del concurso» (step 4), which the C2 prose does not state («publicación de la resolución», «En el reingreso cuenta desde la publicación»). The new rows use the C2 lesson's wording for those two phrases, the rest copied from C1; the verifier must check the shortenings against art. 48.1–3 RD 364/1995.
3. «Efectos de algunas situaciones administrativas», tabla, after «Suspensión de funciones» (art. 22.5 RD 365/1995). C1 origin: m04-l04 «Efectos de las situaciones administrativas». Header + 10 rows inherited; DROPPED: «Excedencia voluntaria incentivada» (C2 prose says «no se puede trabajar en el sector público», cutting «bajo ningún tipo de relación funcionarial o contractual») and «Excedencias voluntarias, salvo esa mensualidad de la incentivada» (its «salvo esa mensualidad» points to the dropped row). Title new («algunas»: servicio activo, servicio en otras AAPP and others are not rows).
4. «Duración de algunas situaciones administrativas», tabla, directly after esquema 3. C1 origin: m04-l04 «Duración de las situaciones». Header + 10 rows inherited, 0 dropped. Title new («algunas»).

Considered and not made (cap of four): «Clases de empleados públicos» and «La Secretaría de Estado de Función Pública…» (arbol, m04-l01), «Clases de órganos de selección», «Quién no puede formar parte de los órganos de selección», «El cupo de reserva para personas con discapacidad», «Los sistemas selectivos…», «Aprobados y plazas convocadas», «Jubilación forzosa y prolongación», «Intervalos de niveles», «Requisitos de la promoción interna» (rows would mostly inherit; plazos and durations took the slots). The C2 prose already has its own table for «Otras formas de provisión».

Rows: inherited 36 lines (libre designación 3, concurso 2, efectos 11 incl. header, duración 11 incl. header; header lines of the tables included) / new 2 / dropped 2.
prov.sh plan: `m01-l13: 353 inherited, 50 verified, 2 pending` (the 2 pending lines are the new concurso steps; the Normativa/R2b-note lines listed pending before I started are no longer listed, so a verify report must have been added meanwhile).

## m01-l14 (C1 sources: m04-l05, m05-l04, m04-l06, m04-l07)

Esquemas added (4), all fully inherited (0 new rows, 0 dropped from the four made):

1. «Intervalos de niveles hasta que se apruebe la normativa reglamentaria», tabla, after the Grado personal paragraph ending «(art. 71.2 RD 364/1995)». C1 origin: m04-l05 same title. Header + 5 rows (A1–C2) inherited. A «Lo que más cae» fact (C2: 14 a 18).
2. «Fases del expediente disciplinario», pasos, after the «Resolución» section (art. 61.s) LRJSP). C1 origin: m04-l06 same title. 4 steps inherited.
3. «Plazos del expediente disciplinario», plazos, directly after esquema 2. C1 origin: m04-l06 same title. 7 steps inherited.
4. «Retribuciones y subsidio en la incapacidad temporal y en el riesgo durante el embarazo», tabla, after «Riesgo durante el embarazo y la lactancia natural» (art. 22.4 RDL 4/2000). C1 origin: m04-l07 same title. Header + 6 rows inherited.

Considered and not made (cap of four; most would inherit): «Requisitos de la promoción interna» (m04-l05), «Las pagas extraordinarias en el TREBEP, en la Ley 30/1984 y en la Ley 31/2022» (m05-l04; 3 rows would inherit), «Suspensión provisional: el TREBEP y el RD 365/1995» (m04-l06), «Alta, conservación y baja como mutualista» (m04-l07; 5 rows would inherit), «Plazos de la libre designación» / «Plazos del concurso» (in l13). Not covered by the C2 prose, so not made: «Devengo y liquidación de las retribuciones…» (m05-l04), «Autorización y reconocimiento de compatibilidad» (m04-l06). The C2 prose has its own tables for sanciones and prescripción.

Rows: inherited 24 lines (intervalos 6, fases 4, plazos 7, IT 7) / new 0 / dropped 0.
prov.sh plan: `m01-l14: 379 inherited, 49 verified, 0 pending`.

## m01-l15 (C1 sources: m05-l01, m05-l02, m05-l03)

Esquemas added (4):

1. «Estructura de los estados de gastos de los Presupuestos Generales del Estado», arbol, after the clasificación económica table (end of «Los estados de gastos»). C1 origin: m05-l02 same title. 7 nodes inherited.
2. «Aprobación, compromiso y reconocimiento de la obligación del gasto del Estado», tabla, after the paragraph ending «(art. 74.2 LGP)» in «Ejecución». C1 origin: m05-l03 «Fases del gasto del Estado hasta la ordenación del pago». 3 rows inherited (aprobación, compromiso, reconocimiento); the «Ordenación del pago» row DROPPED (arts. 75.1 and 75.3 LGP are not cited in the C2 prose, and the prose says nothing of the Ordenador general de pagos beyond art. 74.1). Title new, names the three phases left. The HEADER is NEW (1 pending line): its governing citation is the previous cited sentence («art. 74.2 LGP»), C1's was a different one (Orden PRE/1576/2002).
3. «Control de la gestión económico-financiera del sector público estatal», arbol, after the «Cuentas… por conducto de la IGAE (art. 137 LGP)» paragraph. C1 origin: m05-l03 same title. 6 nodes inherited.
4. «Plazos del ciclo presupuestario», tabla, at the end of «Control y liquidación» (art. 131.1 LGP). C1 origin: m05-l01 same title. Header + 6 rows inherited, 0 dropped.

Considered and not made: «Qué es cada modificación de crédito» (m05-l02: the C2 prose describes only the transferencias, a one-row table); «Reparo y discrepancia» (m05-l03: not in the C2 lesson). The C2 prose has its own tables for the clasificación económica, ingresos and the elaboración steps.

Rows: inherited 7 + 4 + 6 + 7 = 24 lines / new 1 (header) / dropped 1.
prov.sh plan: `m01-l15: 100 inherited, 30 verified, 1 pending`.

## m01-l16 (C1 source: m03-l07)

Esquemas added (2):

1. «Discriminación y acoso por razón de sexo», tabla, after the acoso paragraph (art. 7.2 LO 3/2007). C1 origin: m03-l07 same title. Header + 4 rows inherited.
2. «Órganos en materia de igualdad, violencia de género, igualdad de trato y personas LGTBI», tabla, after the Consejo de Participación paragraph (art. 9.3 Ley 4/2023). C1 origin: m03-l07 «Órganos de igualdad y contra la violencia de género». 5 rows inherited (Comisión Interministerial, Delegación del Gobierno, Observatorio, Inspección de Trabajo, Autoridad Independiente); 1 NEW row: «Consejo de Participación de las Personas LGTBI | Órgano de participación ciudadana en materia de derechos y libertades de las personas LGTBI. El Consejo dependerá del Ministerio de Igualdad a través de la Secretaría de Estado de Igualdad y contra la Violencia de Género | arts. 9.1 y 9.3 Ley 4/2023» (a «Lo que más cae» fact; art. 9.1 is cut before «y tiene por finalidad…», as in the prose; art. 9.3 first sentence verbatim). The HEADER is NEW: its governing citation is now «art. 9.3 Ley 4/2023» (C1's was another). Title new (names the LGTBI council and the igualdad de trato rows too).

Considered and not made: grados de dependencia, niveles de protección, infracciones de discapacidad (already lists or running prose in the lesson; no C1 esquema to inherit).

Rows: inherited 10 lines (sexo: header + 4; órganos: 5 rows) / new 2 (1 header + 1 row) / dropped 0.
prov.sh plan: `m01-l16: 71 inherited, 36 verified, 2 pending`.
