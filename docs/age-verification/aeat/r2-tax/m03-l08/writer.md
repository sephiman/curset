# m03-l08 — notas del redactor

## 1. Fuentes
- LGT (`BOE-A-2003-23186_lgt_2024-12-21.pdf`): arts. 99, 101, 113, 141–158 leídos enteros; art. 159 leído y dejado fuera (ver 7).
- RGAT (`BOE-A-2007-15984_rgat_2026-10-07.pdf`): arts. 87, 166–167, 171–192 leídos; 168–170 y 193 en adelante no usados.
- LPAC (`lpac.txt`, art. 30.4) para el cómputo de meses del ejemplo.
- Resolución de 24-03-1992: no se usa; ninguna pregunta se apoya en ella. La he quitado de «Normativa» (el stub la listaba).
- Ningún precepto citado tiene cambio pendiente ni RDL sin convalidar.

## 2. Preguntas del pack (22 coverage, 11 reference; 33 en total)
- 2025-25, 2023-26, 2020-57 (155.1–3, 155.6): «Actas con acuerdo».
- 2025-39, 2022-53 (157.2, 158.1): «Actas de disconformidad», «Estimación indirecta». El pack cita 158.3 para el informe razonado; en este snapshot es 158.1 (158.3 es la lista de fuentes de datos). La lección cita 158.1.
- 2025-59 (143.1, 143.2, 144): «Actas».
- 2024-20 (87.3.f RGAT): «Comunicaciones, diligencias e informes» (lista a–f completa).
- 2024-36 (155.1): «Actas con acuerdo».
- 2024-47 (141.b): «Funciones de la inspección tributaria» (lista completa; el párrafo siguiente pone las funciones de gestión de las otras opciones).
- 2024-73 (reference, anulada): «Plazo de las actuaciones» (150.1.b.2.º, 150.2).
- 2023-4, 2022-57, 2022X-57, 2022X-58, 2020-64, 2020-66 (181 RGAT): «Medidas cautelares».
- 2023-7, 2022-51, 2020-60 (172 RGAT, 113 LGT): «Entrada y reconocimiento de fincas», «Domicilio constitucionalmente protegido».
- 2023-66 (149.3): «Solicitud de una inspección de carácter general».
- 2022-50 (101.4.a, 148.3): «Alcance de las actuaciones», «Liquidaciones provisionales y definitivas» (190.3 RGAT).
- 2022-52, 2022X-53 (150): «Plazo de las actuaciones inspectoras» y ejemplo. En 2022X-53 la opción d dice 30 días; el artículo dice 60 (150.4). La a se desmiente con 150.2 (último párrafo).
- 2022-54, 2020-92 (146): «Medidas cautelares». El pack cita 146.2; en este snapshot la ratificación a los 15 días es 146.3 (146.2 es la proporcionalidad). La lección cita 146.3.
- 2022-56 (reference de III.8, por el pack «coverage»): «Comunicaciones, diligencias e informes» da 99.7 (diligencia = documento que hace constar hechos). No está: la entrega de ficheros informáticos en diligencia no consta en LGT ni en RGAT de este snapshot (es instrucción interna de la AEAT).
- 2022-55 (reference, fuera de temario): no está: instrucciones internas de la AEAT sobre conservación informática.
- 2022X-55 (189.5): «Terminación del procedimiento de inspección».
- 2022X-56 (171.3): «Examen de la documentación» (10 y 5 días hábiles).
- 2021-62 (reference): «Actas de disconformidad» (157.3, 157.5) y 185.4 RGAT.
- 2020-59 (reference, 57.1 RGAT: autorización del director de departamento o de los delegados para requerimientos de movimientos de cuentas): no está: obtención de información, de III.5; la pack lo marca «cobertura discutible».
- 2020-62 (99.7): «Comunicaciones, diligencias e informes».
- 2020-90 (reference, 196 RGAT, responsabilidad): no está: tema III.12.

## 3. «Lo que más cae» → preguntas
1: 2022-54, 2020-92. 2: 2023-4, 2022-57. 3: 2025-25, 2023-26, 2020-57. 4: 2022-52, 2024-73. 5: 2025-39, 2022-53. 6: 2022-51, 2023-7, 2020-60. 7: 2022X-57, 2020-66. 8: 2023-66. 9: 2025-59. 10: 2022X-53.
Quedan fuera de las diez líneas, pero en el cuerpo: 2024-47 (141.b), 2024-20 (87.3.f), 2024-36 (155.1), 2022-50 (101.4.a), 2022X-55 (189.5), 2022X-56 (171.3), 2022X-58 (181.4), 2020-62.

## 4. Ejemplos
Un ejemplo (plazo de las actuaciones, 150.1, 150.2, 150.4, 150.5). Fechas comprobadas con `python3 datetime`: 02-03-2026 lunes, 02-12-2026 miércoles (nueve meses), 15-01-2027 viernes, 02-06-2028 viernes (27 meses de fecha a fecha, art. 30.4 LPAC), 02-09-2028 (tres meses más), 22-09-2028 viernes (20 días naturales más), 02-09-2027 jueves (18 meses, contraste). El 02-09-2028 es sábado, no se afirma su día. Cómputo: los meses de la extensión se suman a la fecha de fin; la LGT no lo dice, el ejemplo lo presenta como suma sin atribuirle cita propia más allá de 150.4 y 150.5.

## 5. Resumen para course.yaml
La lección recorre las funciones y facultades de la inspección, la documentación de sus actuaciones y su personación en domicilios y locales. Explica el procedimiento inspector, su plazo de 18 o 27 meses, las actas con acuerdo, de conformidad y de disconformidad, y las medidas cautelares. Resuelve con un ejemplo el cómputo del plazo y de sus extensiones.

## 6. Propuestas de glosario (ninguna existe en `glossary.yaml`)
```yaml
- id: g-diligencia
  es: diligencia
  origin: m03-l08
  definition: {es: Documento público que se extiende para hacer constar hechos, así como las manifestaciones del obligado tributario o de la persona con la que se entienden las actuaciones. No puede contener propuestas de liquidaciones tributarias (art. 99.7 LGT).}
- id: g-comunicacion-tributaria
  es: comunicación
  origin: m03-l08
  definition: {es: Documento a través del cual la Administración notifica al obligado tributario el inicio del procedimiento u otros hechos o circunstancias relativos al mismo o efectúa los requerimientos que sean necesarios a cualquier persona o entidad (art. 99.7 LGT).}
- id: g-acta-de-inspeccion
  es: acta de inspección
  origin: m03-l08
  definition: {es: «Los documentos públicos que extiende la inspección de los tributos con el fin de recoger el resultado de las actuaciones inspectoras de comprobación e investigación, proponiendo la regularización que estime procedente de la situación tributaria del obligado o declarando correcta la misma» (art. 143.2 LGT).}
```

## 7. Pendiente
- Citas sin resolver: ninguna (`cites.py`: 160 citas, 0 sin resolver).
- Fuera de la lección: LGT 159 (informe preceptivo del conflicto, Comisión consultiva) y 150.3.d solo como mención: el programa no nombra el conflicto y ninguna pregunta de coverage lo pidió; RGAT 166.2–3, 167–170 (competencias, planes, colaboración), 190.2 y 190.4 en detalle, 192–197; la desagregación de plazos de 150.3 en detalle. Decisión del coordinador: si se quiere 159 por «full», añadir.
- Dos normas nombradas dentro de 150.3 LGT (Concierto Económico con el País Vasco, Convenio Económico con Navarra) están en «Normativa» sin precepto citado: el artículo (47 ter) está en el texto de 150.3 pero la lección no lo cita. Para que la lista sea estricta, decidir si se citan con precepto o se quitan los nombres de la lista de suspensiones.
- Discrepancias del pack con el snapshot: 146.2→146.3; 158.3→158.1; 2022X-53 d (30 días, el artículo dice 60).
