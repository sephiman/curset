# Blind check of the R2b/R2c edits — common part (m01-l02, m01-l03, m01-l04, m01-l07, m02-l02, m02-l04), 2026-11-11

Verifier spec `docs/age-verification/aeat/r2b/verify/spec.md`. Norm texts from `content/aeat-agentes-hacienda/sources/normativa/`;
exams from `docs/age-verification/aeat/r0a/parsed/master.json` and `docs/aeat-official-exams-ledger.md`; programme
`sources/programa.md`, Anexo I.

## m01-l02

| id | verdict | reason | replacement |
|---|---|---|---|
| `a2a239d34b` | PASS | Header of «Algunos quórum y mayorías de las Cortes Generales»; the three columns fit every row (acuerdo, quórum or mayoría, article). | |
| `a1324b7157` | PASS | Note heads «El Ministerio Fiscal». Tema I.2 literal: «Las Cortes Generales… El Poder Judicial. El Consejo General del Poder Judicial. El Tribunal Supremo. La organización judicial española»; the Ministerio Fiscal is not named. 2024-56 (art. 124.1 CE, misión del Ministerio Fiscal; key B) and 2020-9 (art. 124.4 CE, nombramiento del Fiscal General; key A) exist, both `vigente`, both answered by the section's sentences (art. 124.1 and 124.4 CE). | |

## m01-l03

| id | verdict | reason | replacement |
|---|---|---|---|
| `60730cee68` | PASS | Note heads «Las Comisiones Delegadas del Gobierno»; tema I.3 literal names «El Gobierno: Nombramiento y cese. Las funciones del Gobierno», not the Comisiones Delegadas. 2023-84 exists, `vigente`, key C: «permite al Consejo de Ministros, a propuesta del Presidente del Gobierno, reclamar para sí un asunto cuya decisión corresponda a las Comisiones Delegadas» = the section's art. 20.4 Ley 50/1997 sentence. | |
| `6a128f558c` | PASS | Note heads «Competencia de los órganos» (arts. 8–14 LRJSP); tema I.3 does not name competence, delegation or avocación. 2020-7 (desconcentración, art. 8.2 LRJSP; key A) and 2020-12 (irrenunciabilidad, art. 8.1 LRJSP; key A) exist, both `vigente`; both keys are the section's art. 8.1 and 8.2 sentences. | |
| `65fed94ad5` | PASS | Note heads «Inscripción en el Inventario de Entidades»; tema I.3 names «Tipos de Entes Públicos», not the Inventario. 2023-35 exists, `vigente`, key B: «se practicará dentro del plazo de 15 días hábiles siguientes a la recepción de la solicitud de inscripción» = the section's art. 83.2.b LRJSP sentence; options a/d (plazo of art. 83.1) and c (NIF, art. 83.2.c) are also answered by the section. | |
| `03f6e23f71` | FAIL | Prose citations of Ley 50/1997 are arts. 1.2–1.3, 2.2, 3, 4.1–4.2, 5.1–5.3, 6.1–6.5, 7.1–7.2, 11, 12.2, 12.2 bis, 13.1–13.2, 15.1, 18.1–18.4, 20.2–20.4, 21.1–21.6, 24.2, 29.2–29.3: the ranges match, but «12 bis» names an article the law does not have. The snapshot (BOE-A-1997-25336) has an apartado «2 bis» inside art. 12 (line 127 cites «art. 12.2 bis Ley 50/1997»), already covered by «11–13». | Ley 50/1997 (Gobierno): arts. 1–7, 11–13, 15, 18, 20–21, 24 y 29. |

## m01-l04

| id | verdict | reason | replacement |
|---|---|---|---|
| `82c70886c5` | PASS | Note heads «Las sedes» (Protocolo n.º 6); tema I.4 literal names the Consejo, the Parlamento Europeo, the Comisión and the Tribunal de Justicia, not their sedes nor the Tribunal de Cuentas. 2024-62 («¿Dónde está la sede del Tribunal de Cuentas de la Unión Europea?», key D Luxemburgo) exists, `vigente`; the section's table gives «Tribunal de Cuentas — Luxemburgo». | |
| `cd40510915` | PASS | Note heads «El Consejo Europeo»; tema I.4 names «El Consejo», not the Consejo Europeo. 2025-50 exists, `vigente`, key D «Los Jefes de Estado o de Gobierno de los Estados miembros, así como por su Presidente y el Presidente de la Comisión» = the section's art. 15.2 TUE sentence. | |
| `60e4d0a52a` | PASS | Header of «Duración de algunos mandatos en las instituciones de la Unión»; columns fit every row (cargo u órgano, duración, artículo). The governing citation listed (`curia-tribunal-general.html`) is only the preceding prose sentence; no row cites it. | |
| `f0c145859e` | PASS | Starts with the `short` «TUE». Prose cites arts. 13.1–13.2, 13.4, 14.1–14.4, 15.2, 16.1–16.9, 17.1–17.3, 17.5–17.8, 19.1–19.3 TUE: exactly arts. 13–17 and 19. Art. 18 TUE (removed with the Alto Representante paragraph) is no longer cited. | |
| `0da7e9b3ac` | PASS | Starts with the `short` «TFUE». Prose cites arts. 229, 231, 234, 236, 238.1–238.3, 240.3, 244, 247, 250, 252, 253, 254, 256.3, 258, 259, 260.2, 263, 264 and 289.1 TFUE: the list matches; art. 235 (removed with the Consejo Europeo voting paragraph) is no longer cited. «artículo 255 del TFUE» at line 856 and «artículo 267» are textual references inside sentences, not citations. | |

## m01-l07

| id | verdict | reason | replacement |
|---|---|---|---|
| `f1077d3d6d` | PASS | Note heads «Órganos de selección»; tema I.7 literal (régimen jurídico, EBEP, derechos y deberes, provisión y carrera, situaciones, incompatibilidades y régimen disciplinario, Seguridad Social) does not name selection or its organs. 2021-20 («No podrán formar parte de los órganos de selección», key C «Los funcionarios interinos») exists, `vigente`; answered by the section's art. 60.2 TREBEP sentence. | |
| `44dcb152ab` | PASS | Note heads «Acceso de las personas con discapacidad»; tema I.7 literal does not name access to public employment or the cupo de discapacidad (I.6 names «Discapacidad y dependencia: régimen jurídico», another tema). 2022X-17 (llamamiento extraordinario OEP 2022, pregunta 17: cupo del art. 59.1 TREBEP, key A «Siete por ciento») exists, `vigente`; answered by the section's art. 59.1 TREBEP sentence. | |

## m02-l02

| id | verdict | reason | replacement |
|---|---|---|---|
| `446789b9e6` | PASS | Verbatim art. 39.4 LPAC: «Las normas y actos dictados por los órganos de las Administraciones Públicas en el ejercicio de su propia competencia deberán ser observadas por el resto de los órganos administrativos, aunque no dependan jerárquicamente entre sí o pertenezcan a otra Administración.» | |
| `8f29d28221` | PASS | Header of «Desde cuándo produce efectos el acto»; columns fit the rows (supuesto, efectos, artículo). | |
| `dcc89e5e7e` | PASS | Art. 107.4 LPAC: «Si el acto proviniera de la Administración General del Estado o de las Comunidades Autónomas, la declaración de lesividad se adoptará por el órgano de cada Administración competente en la materia.» Faithful; «la declara» refers back to «La lesividad» of the paragraph; nothing dropped or added. | |

## m02-l04

| id | verdict | reason | replacement |
|---|---|---|---|
| `c67b19c84e` | PASS | Art. 80.1 «Salvo disposición expresa en contrario, los informes serán facultativos y no vinculantes»; 80.2 «…en el plazo de diez días, salvo que una disposición o el cumplimiento del resto de los plazos del procedimiento permita o exija otro plazo mayor o menor». Faithful; only the medium («a través de medios electrónicos… artículo 26») is left out, no plazo or exception lost. | |
| `e65b9fe575` | PASS | Art. 95.1: «Consumido este plazo sin que el particular requerido realice las actividades necesarias para reanudar la tramitación, la Administración acordará el archivo de las actuaciones, notificándoselo al interesado.» Faithful. | |
| `c3f52e07d8` | PASS | Header of «Algunos plazos de las fases del procedimiento»; every row states a plazo or time limit of the act named. | |
| `ce94a8baea` | PASS | Art. 56.2: measures adopted before the iniciación «en los casos de urgencia inaplazable… deberán ser confirmadas, modificadas o levantadas en el acuerdo de iniciación del procedimiento, que deberá efectuarse dentro de los quince días siguientes a su adopción». Faithful shortening, same words as the prose (line 8, art. 56.2 LPAC). | |
| `b00e86b6d5` | PASS | Art. 68.1, near verbatim («previa resolución que deberá ser dictada en los términos previstos en el artículo 21» shortened). The label names only art. 66, which is narrower than the article (66, 67 and specific legislation), never wider; in the prose with the same citation. | |
| `c521f0e990` | PASS | Art. 68.2: «Siempre que no se trate de procedimientos selectivos o de concurrencia competitiva, este plazo podrá ser ampliado prudencialmente, hasta cinco días, a petición del interesado o a iniciativa del órgano, cuando la aportación de los documentos requeridos presente dificultades especiales.» Exception and condition kept; in the prose. | |
| `4cb02f050a` | PASS | Art. 76.1: «Los interesados podrán, en cualquier momento del procedimiento anterior al trámite de audiencia, aducir alegaciones y aportar documentos…». Faithful; in the prose. | |
| `fe0ec2c2d7` | PASS | Art. 77.2: «…un período de prueba por un plazo no superior a treinta días ni inferior a diez». The plazo is exact; in the prose with art. 77.2 LPAC. | |
| `8b1e2faa07` | PASS | Same text and passage as `c67b19c84e` (art. 80.1–2 LPAC), in the prose. | |
| `ee5b98e3da` | PASS | Art. 82.1–2: «inmediatamente antes de redactar la propuesta de resolución, se pondrán de manifiesto a los interesados… Los interesados, en un plazo no inferior a diez días ni superior a quince, podrán alegar y presentar los documentos…». Cited 82.2 (where the plazo is), as in the prose. | |
| `c2d56aae47` | PASS | Art. 83.2: «el plazo para formular alegaciones, que en ningún caso podrá ser inferior a veinte días». In the prose. | |
| `8ab6739cad` | PASS | Art. 87: «un plazo de siete días para formular las alegaciones… tras la finalización de las mismas. Las actuaciones complementarias deberán practicarse en un plazo no superior a quince días. El plazo para resolver el procedimiento quedará suspendido hasta la terminación…». All three plazos kept; in the prose. | |
| `8d643ca0f4` | PASS | Art. 88.1, second paragraph, near verbatim; in the prose. | |
| `036eb1b205` | PASS | Art. 95.1: «En los procedimientos iniciados a solicitud del interesado, cuando se produzca su paralización por causa imputable al mismo, la Administración le advertirá que, transcurridos tres meses, se producirá la caducidad». «Solicitante» carries the condition; in the prose. | |
| `5480d3dcd9` | PASS | Art. 96.3: «podrá desestimar dicha solicitud, en el plazo de cinco días desde su presentación, sin que exista posibilidad de recurso». Condition in the label; in the prose. | |
| `ea4d818964` | PASS | Art. 96.6: «Salvo que reste menos para su tramitación ordinaria… deberán ser resueltos en treinta días, a contar desde el siguiente al que se notifique al interesado el acuerdo de tramitación simplificada». In the prose. | |
| title m02-l04 «Algunos plazos de las fases del procedimiento» | PASS | Selective list of plazos from iniciación, instrucción and finalización; «Algunos» marks it; placed after the finalización paragraphs, i.e. after all the paragraphs it draws from; voice clean. | |
