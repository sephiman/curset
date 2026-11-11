# Notas del redactor — III.13 (`m03-l13`)

## 1. Fuentes
- LGT (`BOE-A-2003-23186_lgt_2024-12-21.pdf`, pdftotext del snapshot): arts. 178–212 completos (198–206 solo títulos y 198.1, 198.2, 198.4, 198.5), 27 (pointer), 62.2.
- RGRST (`BOE-A-2004-18398_rgrst_2019-09-20.pdf`): arts. 1–7, 20–24, 29 leídos; citados 2, 3, 4, 5.1, 6, 7.1–2, 20.1, 21.1, 22.1, 23.4, 24.2 y 29.2. Ninguna pregunta del pack cita el RGRST.
- Código Aduanero de la Unión: solo el art. 127 nombrado dentro del art. 198.4 LGT (no se lee el reglamento).

## 2. Preguntas del pack (30: 20 coverage + 10 reference)
- 2025-10 → Dejar de ingresar (191.2)
- 2025-14 → Solicitar indebidamente devoluciones (194.1; 188.1 alcanza a 191–197; 193.1 si se obtiene)
- 2025-34 → Ocultación y medios fraudulentos (184.3.a, 2.º; 10 % en 184.3.b; 50 % en 184.3.a.3.º)
- 2025-45 → Criterios de graduación (187.1)
- 2025-72 → Reducción de las sanciones (188.1.a; 188.3, último párrafo)
- 2024-30 → Extinción de la responsabilidad (189.1)
- 2024-41 → Tramitación separada (208.1); Instrucción (210.4, 15 días); Terminación (211.2, seis meses)
- 2024-48 → Terminación (211.2, 211.4); Iniciación (209.2, seis meses desde la liquidación)
- 2024-74 → Presentar declaraciones (tabla art. 192.2–4)
- 2023-6 → Criterios de graduación, comisión repetida (187.1.a)
- 2023-10 → No concurrencia (180.3)
- 2023-70 → Solicitar indebidamente devoluciones (194.1)
- 2022-46 → Principio de responsabilidad (179.3 y pointer a `m03-l03`; el art. 27.2 con 1 % + 1 % por mes y el 25 % lo explica m03-l03)
- 2022-71 → Principio de responsabilidad (179.2.a)
- 2022-72 → Terminación (211.1)
- 2022-73 → Solicitar indebidamente devoluciones (194.1)
- 2022-74 → No concurrencia (180.3)
- 2022X-82 → Principio de responsabilidad (179.2.e)
- 2022X-83 → Dejar de ingresar (191.2)
- 2022X-86 → Recursos contra sanciones (212.3.a)
- Reference: 2022-70 → 212.3 · 2021-87 → Responsables y sucesores (182.3) · 2021-92 → 187.2 · 2021-93 → Otras infracciones (198.4) · 2020-78 → Dejar de ingresar (191.4 y 184.3) · 2020-82 → Ocultación y medios fraudulentos (art. 184 define ocultación y medios fraudulentos; 187.1 los criterios de graduación) · 2021-58 → no está: es art. 27.2 LGT (III.3, m03-l03) · 2021-88, 2021-89, 2020-91 → no están: fuera de temario (delito fiscal).

## 3. «Lo que más cae» → preguntas
1 → 2023-70, 2022-73, 2025-14; 2 → 2023-10, 2022-74; 3 → 2022X-86, 2022-70; 4 → 2022-71, 2022X-82; 5 → 2025-10, 2022X-83; 6 → 2025-45 (y 2023-6); 7 → 2025-72; 8 → 2024-30; 9 → 2024-48 (y 2022-72); 10 → 2024-41.

## 4. Ejemplo
Graduación y reducciones (Talleres Ribera, S.L.): base 20.000; 50 + 15 (comisión repetida, grave) + 15 (perjuicio 50 %, tramo «superior al 25 % e inferior o igual al 50 %») = 80 % → 16.000; reducción 30 % → 11.200; reducción 40 % → 6.720. Aritmética comprobada a mano (16.000 × 0,70 = 11.200; 11.200 × 0,60 = 6.720). Fechas comprobadas con `python3 datetime`: 18-05-2026 lunes; 05-07-2026 domingo; 06-07-2026 lunes (art. 62.2.b LGT, «inmediato hábil siguiente»); no hay festivo nacional el 6 de julio.

## 5. Resumen para `course.yaml`
La potestad sancionadora tributaria se rige por los principios de legalidad, tipicidad, responsabilidad, proporcionalidad y no concurrencia, y la sanción pecuniaria se gradúa con la comisión repetida, el perjuicio económico y el incumplimiento sustancial de la facturación, y se reduce un 30 % o un 65 % por conformidad o acta con acuerdo y un 40 % por pronto pago. El procedimiento sancionador se tramita por separado, salvo renuncia, y caduca a los seis meses de la notificación de su inicio. Recurrir una sanción en tiempo y forma suspende su ejecución en voluntaria sin garantías.

## 6. Glosario propuesto
- id: g-infraccion-tributaria
  es: infracción tributaria
  origin: m03-l13
  definition: {es: «Son infracciones tributarias las acciones u omisiones dolosas o culposas con cualquier grado de negligencia que estén tipificadas y sancionadas como tales en esta u otra ley» (art. 183.1 LGT).}
- id: g-ocultacion-de-datos
  es: ocultación de datos a la Administración tributaria
  origin: m03-l13
  definition: {es: Existe cuando no se presentan declaraciones o se presentan con hechos u operaciones inexistentes o con importes falsos, o con omisión total o parcial de operaciones, ingresos, rentas, productos, bienes o cualquier otro dato que incida en la determinación de la deuda, «siempre que la incidencia de la deuda derivada de la ocultación en relación con la base de la sanción sea superior al 10 por ciento» (art. 184.2 LGT).}
- id: g-medios-fraudulentos
  es: medios fraudulentos
  origin: m03-l13
  definition: {es: Se consideran medios fraudulentos las anomalías sustanciales en la contabilidad y en los libros o registros, el empleo de facturas, justificantes u otros documentos falsos o falseados con incidencia superior al 10 por ciento de la base de la sanción, y la utilización de personas o entidades interpuestas (art. 184.3 LGT).}
- id: g-comision-repetida
  es: comisión repetida de infracciones tributarias
  origin: m03-l13
  definition: {es: Se produce cuando el sujeto infractor hubiera sido sancionado por una infracción de la misma naturaleza «en virtud de resolución firme en vía administrativa dentro de los cuatro años anteriores a la comisión de la infracción» (art. 187.1.a LGT).}
- id: g-regularizacion-voluntaria-sancionadora
  es: regularización voluntaria (orden sancionador)
  origin: m03-l13
  definition: {es: A efectos del art. 179.3 LGT, la efectuada «antes de la notificación de un requerimiento para el cumplimiento de la obligación tributaria o de la notificación del inicio de un procedimiento de comprobación o investigación o de un procedimiento sancionador» (art. 2 RGRST).}

## 7. Citas sin resolver, omisiones, ambigüedades
- cites.py: 202 citas, 0 sin resolver (tras escribir «arts. 179.2.a y 179.2.e LGT»).
- Discrepancia con el encargo: el encargo decía «209 plazo de tres meses»; el art. 209.2 LGT del snapshot dice seis meses desde la notificación de la liquidación o resolución (la lección lo recoge así). El plazo de resolución del art. 211.2 también es de seis meses.
- Omitido: arts. 199–206 más allá de su título (ninguna pregunta los pide); art. 198.3 y 198.6; art. 206 bis; RGRST arts. 8–19, 25–28, 30–33 (cálculos de incidencias, tramitación especial por inspección y conjunta, delitos). Texto de los arts. 191–193 repetido solo donde cambia.
- Pack: la evidencia R0a de 2025-34 no cita el apartado 3.º (la lección recoge 184.3.a, 1.º–3.º; el distractor «25 por ciento» es el 50 por ciento del 184.3.a.3.º y el «10 por ciento» corresponde a los documentos falsos del 184.3.b).
- El art. 187.1 LGT, además de los tres criterios, incluye d) acuerdo o conformidad; la lección lo recoge como cuarto criterio y en «Lo que más cae» lo dice.
