# Psicotécnicos in the official exams — index

Round R0a, 2026-11-05. Every psicotécnico question of the six distinct Auxiliar questionnaires (2025 ordinario, 2024 ordinario and extraordinario, 2022, OEP 2020 ordinario and extraordinario), part 1, questions 31–60, and the psicotécnico reserve questions. Modelo B (2025, 2024) repeats modelo A in another order: its numbers are given next to A's and its questions are not counted twice. There are no Auxiliar extraordinarios for 2025 or 2022 (the INAP page publishes none). Input for R6.1–R6.5 of `docs/age-auxiliar-course-requirements.md`: this index fixes which psicotécnico types exist and their weights.

Classification is one pass per question (type, subtype, parameters, rule, difficulty) with every arithmetic, table and count item recomputed in Python and every verbal item decided against the DLE. The computed answer matches the official key in 192 of 193 non-annulled items; the four disputed keys and the two annulled items are listed in section 5 and in `docs/age-c2-official-exams-ledger.md`. Rendered pages of the whole psicotécnico section show no chart, drawing or picture item: the only visual content is tables. One table is an image (2024 «Cuadro Laboratorios», questions 55–60); it is transcribed in the ledger and its render is in `content/age-auxiliar-c2/sources/examenes-oficiales/renders/`.

Anexo I 2.1 calls these «preguntas de carácter psicotécnico dirigidas a evaluar aptitudes administrativas, numéricas o verbales». The types below are this index's grouping, not an official one.

## 1. Counts per type and exam

Part 1, questions 31–60 plus psicotécnico reserves (2025 and 2024: reserves 3–5; 2024X: 2 and 4; 2022: 3 and 5; OEP 2020: 1 and 2; OEP 2020 extr.: 3–5). «Exams» counts the distinct questionnaires (of six) that ask the type.

| Type | 2025 ord. (A/B) | 2024 ord. (A/B) | 2024 extr. | 2022 | OEP 2020 ord. | OEP 2020 extr. | Total | Exams |
|---|---|---|---|---|---|---|---|---|
| Lectura de tablas (`tablas-lectura`) | 12 | 8 | 6 | 12 | 12 | 12 | 62 | 6 |
| Codificación y equivalencias (`atencion-codificacion`) | 0 | 3 | 7 | 0 | 3 | 3 | 16 | 4 |
| Sinónimos (`verbal-sinonimos`) | 3 | 3 | 2 | 3 | 2 | 2 | 15 | 6 |
| Antónimos (`verbal-antonimos`) | 4 | 4 | 2 | 1 | 1 | 1 | 13 | 6 |
| Ecuaciones (`calculo-ecuaciones`) | 3 | 1 | 3 | 1 | 2 | 3 | 13 | 6 |
| Definiciones (`verbal-definicion`) | 0 | 0 | 4 | 2 | 3 | 3 | 12 | 4 |
| Ortografía (`verbal-ortografia`) | 4 | 3 | 0 | 1 | 1 | 2 | 11 | 5 |
| Problemas aritméticos (`calculo-problemas`) | 1 | 0 | 4 | 4 | 1 | 1 | 11 | 5 |
| Porcentajes (`calculo-porcentajes`) | 3 | 4 | 1 | 2 | 0 | 0 | 10 | 4 |
| Series numéricas (`serie-numerica`) | 2 | 3 | 1 | 2 | 1 | 0 | 9 | 5 |
| Clasificación y archivo (`administrativo-clasificacion`) | 0 | 4 | 0 | 1 | 2 | 2 | 9 | 4 |
| Fracciones y repartos (`calculo-fracciones-proporciones`) | 1 | 0 | 0 | 1 | 1 | 1 | 4 | 4 |
| Ordenación alfabética (`administrativo-ordenacion`) | 0 | 0 | 1 | 1 | 1 | 1 | 4 | 4 |
| Series alfanuméricas (`serie-alfanumerica`) | 0 | 0 | 0 | 0 | 1 | 1 | 2 | 2 |
| Analogías (`verbal-analogia`) | 0 | 0 | 0 | 0 | 1 | 1 | 2 | 2 |
| Palabra intrusa (`verbal-intrusa`) | 0 | 0 | 1 | 1 | 0 | 0 | 2 | 2 |
| **Total** | **33** | **33** | **32** | **32** | **32** | **33** | **195** | |

### Weights in the 30 scored questions

Questions 31–60 only (no reserves): the weights R6.5 asks for («the type weights of the last official exam»). 2025 is the last one.

| Type | 2025 ord. (A/B) | 2024 ord. (A/B) | 2024 extr. | 2022 | OEP 2020 ord. | OEP 2020 extr. |
|---|---|---|---|---|---|---|
| Lectura de tablas | 12 | 8 | 6 | 12 | 12 | 12 |
| Codificación y equivalencias | – | 3 | 7 | – | 3 | 3 |
| Sinónimos | 3 | 3 | 2 | 2 | 2 | 2 |
| Antónimos | 3 | 3 | 1 | 1 | 1 | 1 |
| Ecuaciones | 3 | – | 2 | 1 | 1 | 2 |
| Definiciones | – | – | 4 | 2 | 2 | 3 |
| Ortografía | 3 | 3 | – | 1 | 1 | 1 |
| Problemas aritméticos | – | – | 4 | 3 | 1 | 1 |
| Porcentajes | 3 | 3 | 1 | 2 | – | – |
| Series numéricas | 2 | 3 | 1 | 2 | 1 | – |
| Clasificación y archivo | – | 4 | – | 1 | 2 | 2 |
| Fracciones y repartos | 1 | – | – | 1 | 1 | 1 |
| Ordenación alfabética | – | – | 1 | 1 | 1 | 1 |
| Series alfanuméricas | – | – | – | – | 1 | – |
| Analogías | – | – | – | – | 1 | 1 |
| Palabra intrusa | – | – | 1 | 1 | – | – |

Every exam has two six-question sets on a table (12 of 30). In 2025, 2022 and both OEP 2020 exams all 12 are table reading. In 2024 four of the twelve are filing-location items on the «Biblioteca» table; in 2024X the second set is six code items on a filing-code table. Outside the tables, verbal items take 7–9 of the 30 questions and calculation (cálculo plus series) 3–9; codes and filing/ordering items fill the rest.

## 2. First generator batch: recurring types

Recurring = asked in 3 or more of the six questionnaires. These go to the first generator batch (R3p); the rest wait for the open decision 1 of the requirements.

| Type | Exams | Questions | First batch |
|---|---|---|---|
| Lectura de tablas (`tablas-lectura`) | 6: 2025 ord. (A/B), 2024 ord. (A/B), 2024 extr., 2022, OEP 2020 ord., OEP 2020 extr. | 62 | yes |
| Sinónimos (`verbal-sinonimos`) | 6: 2025 ord. (A/B), 2024 ord. (A/B), 2024 extr., 2022, OEP 2020 ord., OEP 2020 extr. | 15 | yes |
| Antónimos (`verbal-antonimos`) | 6: 2025 ord. (A/B), 2024 ord. (A/B), 2024 extr., 2022, OEP 2020 ord., OEP 2020 extr. | 13 | yes |
| Ecuaciones (`calculo-ecuaciones`) | 6: 2025 ord. (A/B), 2024 ord. (A/B), 2024 extr., 2022, OEP 2020 ord., OEP 2020 extr. | 13 | yes |
| Ortografía (`verbal-ortografia`) | 5: 2025 ord. (A/B), 2024 ord. (A/B), 2022, OEP 2020 ord., OEP 2020 extr. | 11 | yes |
| Problemas aritméticos (`calculo-problemas`) | 5: 2025 ord. (A/B), 2024 extr., 2022, OEP 2020 ord., OEP 2020 extr. | 11 | yes |
| Series numéricas (`serie-numerica`) | 5: 2025 ord. (A/B), 2024 ord. (A/B), 2024 extr., 2022, OEP 2020 ord. | 9 | yes |
| Codificación y equivalencias (`atencion-codificacion`) | 4: 2024 ord. (A/B), 2024 extr., OEP 2020 ord., OEP 2020 extr. | 16 | yes |
| Definiciones (`verbal-definicion`) | 4: 2024 extr., 2022, OEP 2020 ord., OEP 2020 extr. | 12 | yes |
| Porcentajes (`calculo-porcentajes`) | 4: 2025 ord. (A/B), 2024 ord. (A/B), 2024 extr., 2022 | 10 | yes |
| Clasificación y archivo (`administrativo-clasificacion`) | 4: 2024 ord. (A/B), 2022, OEP 2020 ord., OEP 2020 extr. | 9 | yes |
| Fracciones y repartos (`calculo-fracciones-proporciones`) | 4: 2025 ord. (A/B), 2022, OEP 2020 ord., OEP 2020 extr. | 4 | yes |
| Ordenación alfabética (`administrativo-ordenacion`) | 4: 2024 extr., 2022, OEP 2020 ord., OEP 2020 extr. | 4 | yes |
| Series alfanuméricas (`serie-alfanumerica`) | 2: OEP 2020 ord., OEP 2020 extr. | 2 | no |
| Analogías (`verbal-analogia`) | 2: OEP 2020 ord., OEP 2020 extr. | 2 | no |
| Palabra intrusa (`verbal-intrusa`) | 2: 2024 extr., 2022 | 2 | no |

Types that R6.1 of the requirements lists and that no Auxiliar questionnaire of 2020–2025 asks: counting symbols, finding differences and comparing copied data (attention and perception other than codes), error detection in copied records, spatial reasoning, logical reasoning (syllogisms, order puzzles). They have no official example to copy a style from.

## 3. Types

Each type: what is asked, the parameters that vary inside the type, the difficulty note, and one official question verbatim with its definitive key. Difficulty is the classifier's 1–3 for a C2 candidate without a calculator (90 minutes for 110 questions).

### Lectura de tablas (`tablas-lectura`) — 62 questions, 6 exams

**What is asked.** Questions on a table given once before a set of six. Every exam has two such sets; in 2024 four items of the «Biblioteca» set are filing items (administrativo-clasificacion) and in 2024X the «Archivos» set is all code items (atencion-codificacion). Operations: filter on 1–5 conditions; sum by group and max/min; mean by group; ratio per row and max/min; ratio of group sums; share of a group in the total (options with 2 decimals); count of rows meeting conditions.

**Subtypes** (classifier's labels): cociente por fila y máximo (8); suma por grupo y máximo (6); filtro con tres condiciones (6); filtro con tres condiciones y suma (4); recuento con tres condiciones (4); filtro con dos condiciones y mínimo (3); cociente por fila y mínimo (3); filtro con cuatro condiciones (3); media por grupo y máximo (2); porcentaje de un grupo sobre el total (2); filtro con una condición y máximo (2); media de una columna (2); filtro con dos condiciones y suma (2); suma por fila y máximo (2); cociente de sumas por grupo y máximo (1); grupo por encima de la media (1); suma por grupo y mínimo (1); porcentaje restante de un dato (1); diferencia por fila y máximo (1); cociente de dos columnas en una fila (1); filtro con cinco condiciones (1); filtro con tres condiciones y máximo (1); filtro con tres condiciones y media (1); suma por fila y mínimo (1); porcentaje de una columna sumada (1); recuento con dos condiciones (1); máximo de una columna (1).

**Parameters.** Tables of 7–12 rows × 5–9 columns (2022 «Flores»: three linked 10-row tables). Conditions per question 1–5. Options are names from the table or numbers with 0–2 decimals. Unwritten conventions the tribunal applies: «Proyector y Megafonía» counts as «Proyector» (2020, 33); «asistentes» = alumnos + ponentes (2022 «Ponencias»).

**Difficulty.** Levels 1/2/3: 19/31/12. The slowest items of part 1: group sums and ratios over 10 rows without a calculator. Level 3 when the four candidate ratios are close (2025 «Desplazamientos» 57–60, 2020 «Academia», 2020X «Excursiones», 2024X «Academia»). Filter items with one row passing all conditions are level 1.

**Example.** 2025 ord. (A/B), parte 1 51 (modelo B 50); clave c:

```text
   Préstamos
                                                    Lugar          Año de                        Ejemplares    Ejemplares    Préstamos
   Título                    Autor                                               Editorial
                                                    edición        publicación                   disponibles   prestados     realizados
   Aranmanoth                Matute, Ana María      Barcelona         2000       Destino              5             2           249
   Contra Vosotros           Soriano, Mercedes      Madrid            1998       Alfaguara            5             4           114
   Mano de sombra            Marías, Javier         Madrid            1997       Santillana           7             5           311
   Adiós a las novias        Puértolas, Soledad     Barcelona         1998       Anagrama             14            6           201
   La temporada de caza      Camilleri, Andrea      Barcelona         2000       Anagrama             15            5           154
   El equipaje del viajero   Saramago, José         Madrid            1999       Alfaguara            11            3           248
   El amante lesbiano        Sampedro, José Luis    Barcelona         2000       Plaza & Janés        8             7           130
   Entre visillos            Martín Gaite, Carmen   Barcelona         1998       Destino              10            3           268
   Un calor tan cercano      Torres, Maruja         Madrid            1997       Santillana           15            5           290
   Hija de la fortuna        Allende, Isabel        Barcelona         1999       Plaza & Janés        13            7           206
```

  > Responda a las siguientes preguntas según la tabla llamada Préstamos:
  > ¿Cuál de los siguientes títulos está publicado en una editorial de Barcelona, en un año posterior a 1998 y cuenta con más de 10 ejemplares disponibles?
  > a) Entre visillos.
  > b) El amante lesbiano.
  > c) Hija de la fortuna.
  > d) Un calor tan cercano.

Questions: 2025-P1-49, 2025-P1-50, 2025-P1-51, 2025-P1-52, 2025-P1-53, 2025-P1-54, 2025-P1-55, 2025-P1-56, 2025-P1-57, 2025-P1-58, 2025-P1-59, 2025-P1-60, 2024-P1-51, 2024-P1-52, 2024-P1-55, 2024-P1-56, 2024-P1-57, 2024-P1-58, 2024-P1-59, 2024-P1-60, 2024X-P1-49, 2024X-P1-50, 2024X-P1-51, 2024X-P1-52, 2024X-P1-53, 2024X-P1-54, 2022-P1-49, 2022-P1-50, 2022-P1-51, 2022-P1-52, 2022-P1-53, 2022-P1-54, 2022-P1-55, 2022-P1-56, 2022-P1-57, 2022-P1-58, 2022-P1-59, 2022-P1-60, 2020-P1-31, 2020-P1-32, 2020-P1-33, 2020-P1-34, 2020-P1-35, 2020-P1-36, 2020-P1-44, 2020-P1-45, 2020-P1-46, 2020-P1-47, 2020-P1-48, 2020-P1-49, 2020X-P1-46, 2020X-P1-47, 2020X-P1-48, 2020X-P1-49, 2020X-P1-50, 2020X-P1-51, 2020X-P1-55, 2020X-P1-56, 2020X-P1-57, 2020X-P1-58, 2020X-P1-59, 2020X-P1-60.

### Codificación y equivalencias (`atencion-codificacion`) — 16 questions, 4 exams

**What is asked.** Decode a string by an equivalence table: 4-digit binary or 0/2 blocks to letters; digits standing for letters inside a word; the value of a word when letter classes carry values (consonante mayúscula, vocal minúscula…). 2024X adds a six-position filing code with 4 values per position, asked as «cuál es FALSO/CIERTO».

**Subtypes** (classifier's labels): descodificar binario de 4 cifras a letras (4); valor de una palabra por tipo de letra (3); descodificar clave de seis cifras (FALSO) (3); descodificar palabra con cifras (2); razonar sobre posiciones del código (FALSO) (1); codificar un archivo en clave de seis cifras (1); descodificar clave de seis cifras (CIERTO) (1); descodificar cifras de 4 a letras (1).

**Parameters.** Binary/0-2 blocks: 6 equivalences, 4 blocks of 4 digits. Digit words: 4 equivalences, 8 characters. Letter values: 4–5 classes, words of 6–8 letters. Filing code: 6 positions × 4 values.

**Difficulty.** Levels 1/2/3: 10/6/0. Level 1 when the string splits cleanly into blocks; level 2 for the letter-class sums and the negative code questions.

**Example.** 2024 ord. (A/B), parte 1 38 (modelo B 39); clave b:

  > Dadas las siguientes equivalencias: a=0001, b=0010, c=0100, d=1000, e=0011, f=0101 ¿Qué serie de letras corresponde a la siguiente serie de números?: 0001010001000010
  > a) faeb
  > b) accb
  > c) baed
  > d) ecbd

Questions: 2024-P1-38, 2024-P1-42, 2024-P1-43, 2024X-P1-37, 2024X-P1-55, 2024X-P1-56, 2024X-P1-57, 2024X-P1-58, 2024X-P1-59, 2024X-P1-60, 2020-P1-39, 2020-P1-42, 2020-P1-43, 2020X-P1-31, 2020X-P1-52, 2020X-P1-53.

### Sinónimos (`verbal-sinonimos`) — 15 questions, 6 exams

**What is asked.** One word in capitals, four single-word options, one synonym («sinónimo o afín», «significado más parecido»). 2020 and 2020X also ask «¿Qué pareja de SINÓNIMOS es INCORRECTA?» with four pairs.

**Subtypes** (classifier's labels): sinónimo de una palabra (11); pareja de sinónimos incorrecta (2); significado más parecido (2).

**Parameters.** Four options; stem words of everyday to cultured register (HEREJE, DESLAVAZADO, ACÉRRIMO, SIBILINO). The antonym of the stem word often appears among the distractors.

**Difficulty.** Levels 1/2/3: 11/4/0. Level 1 for common words; level 2 when the stem word is rare (DESLAVAZADO, ACÉRRIMO).

**Example.** 2025 ord. (A/B), parte 1 38 (modelo B 37); clave d:

  > Indique entre las siguientes palabras cuál es el sinónimo o afín de la palabra HEREJE.
  > a) Ortodoxo.
  > b) Arrepentido.
  > c) Penitente.
  > d) Heterodoxo.

Questions: 2025-P1-37, 2025-P1-38, 2025-P1-39, 2024-P1-31, 2024-P1-34, 2024-P1-37, 2024X-P1-40, 2024X-P1-44, 2022-P1-40, 2022-P1-41, 2022-R1-3, 2020-P1-37, 2020-P1-38, 2020X-P1-36, 2020X-P1-37.

### Antónimos (`verbal-antonimos`) — 13 questions, 6 exams

**What is asked.** One word in capitals, four options, one antonym («antónimo u opuesto»). Distractors are usually synonyms of the stem word.

**Subtypes** (classifier's labels): antónimo de una palabra (13).

**Parameters.** Four options. The same item can return: VENTURA → «Desdicha» is 2024 reserve 3 and 2025, 36.

**Difficulty.** Levels 1/2/3: 12/1/0. Nearly all level 1: three distractors are synonyms, so the odd one out is the key.

**Example.** 2025 ord. (A/B), parte 1 35 (modelo B 36); clave b:

  > Indique entre las siguientes palabras cuál es el antónimo u opuesto de la palabra ERIAL.
  > a) Páramo.
  > b) Vergel.
  > c) Desierto.
  > d) Descampado.

Questions: 2025-P1-34, 2025-P1-35, 2025-P1-36, 2025-R1-4, 2024-P1-32, 2024-P1-33, 2024-P1-35, 2024-R1-3, 2024X-P1-41, 2024X-R1-2, 2022-P1-42, 2020-P1-54, 2020X-P1-38.

### Ecuaciones (`calculo-ecuaciones`) — 13 questions, 6 exams

**What is asked.** «Halla el valor de x en la siguiente ecuación»: one linear equation with a bracket.

**Subtypes** (classifier's labels): ecuación lineal con paréntesis (13).

**Parameters.** Form a(bx ± c) = dx (+ e). Coefficients up to 32, constants up to 832. The solution is an integer once (2025, 48); otherwise options carry 2 decimals (3 in 2025, 46), often negative. Two official options truncate instead of rounding (2020, 41: −0,6757 printed −0,67; 2020 reserve 2: −3,0476 printed −3,04).

**Difficulty.** Levels 1/2/3: 1/12/0. Level 2 by default: a division to 2 decimals by hand. Level 1 when the answer is an integer and options can be substituted.

**Example.** 2025 ord. (A/B), parte 1 48 (modelo B 46); clave b:

  > Halla el valor de x en la siguiente ecuación: 10 - 9x = 4(x - 4)
  > a) 1
  > b) 2
  > c) 3
  > d) 4

Questions: 2025-P1-46, 2025-P1-47, 2025-P1-48, 2024-R1-5, 2024X-P1-31, 2024X-P1-36, 2024X-R1-4, 2022-P1-31, 2020-P1-41, 2020-R1-2, 2020X-P1-33, 2020X-P1-54, 2020X-R1-3.

### Definiciones (`verbal-definicion`) — 12 questions, 4 exams

**What is asked.** Two directions: the word that matches a definition, or the definition that matches a word. Definitions are the DLE's.

**Subtypes** (classifier's labels): palabra que corresponde a una definición (6); definición que corresponde a una palabra (6).

**Parameters.** Four options; the words are often rare (alfaguara, hebetar, venada).

**Difficulty.** Levels 1/2/3: 5/5/2. Level 1–2; level 3 for rare words (hebetar, venada).

**Example.** 2024 extr., parte 1 42; clave a:

  > Señale qué palabra corresponde a la siguiente definición: "Manantial copioso que surge con violencia".
  > a) Alfaguara.
  > b) Vulcano.
  > c) Hurtadilla.
  > d) Escisión.

Questions: 2024X-P1-42, 2024X-P1-43, 2024X-P1-45, 2024X-P1-48, 2022-P1-44, 2022-P1-45, 2020-P1-56, 2020-P1-57, 2020-R1-1, 2020X-P1-40, 2020X-P1-41, 2020X-P1-42.

### Ortografía (`verbal-ortografia`) — 11 questions, 5 exams

**What is asked.** Two forms: which of four words is misspelt (or which one is right: 2025 reserve 3), and how many spelling errors a sentence has (2020, 2020X).

**Subtypes** (classifier's labels): palabra con error ortográfico (7); número de errores en una frase (3); palabra correctamente escrita (1).

**Parameters.** Word form: 4 words, one wrong (b/v, h, s/x, tildes). Sentence form: 15–17 words with 4–6 errors, options are counts.

**Difficulty.** Levels 1/2/3: 6/5/0. Level 1 for the word form; level 2 for counting errors in a sentence.

**Example.** 2025 ord. (A/B), parte 1 32 (modelo B 33); clave c:

  > Indique cuál de las siguientes palabras contiene un error ortográfico:
  > a) Duermevela.
  > b) Diéresis.
  > c) Exhuberante.
  > d) Viudedad.

Questions: 2025-P1-31, 2025-P1-32, 2025-P1-33, 2025-R1-3, 2024-P1-36, 2024-P1-39, 2024-P1-41, 2022-P1-46, 2020-P1-58, 2020X-P1-43, 2020X-R1-5.

### Problemas aritméticos (`calculo-problemas`) — 11 questions, 5 exams

**What is asked.** Short word problems of 1–4 steps: capacity filling, sharing among a subgroup, unit price, sums of products, two numbers from ratio and sum, and the «operadores que faltan» item (four numbers, three gaps, a target result).

**Subtypes** (classifier's labels): operadores que faltan (3); tiempo para completar una capacidad (2); dos números con razón y suma (1); problema de multiplicación con decimales (1); reparto igualitario entre un subgrupo (1); recuento por multiplicación (1); precio unitario y parte (1); suma de productos (1).

**Parameters.** 1–4 steps; integer or 1-decimal results. Operator items: 4 numbers, 3 gaps. The tribunal evaluates operator items left to right, not by precedence (2022, 39).

**Difficulty.** Levels 1/2/3: 5/6/0. Level 1–2. Two official keys are disputed (2022, 39 and 2022 reserve 5).

**Example.** 2024 extr., parte 1 39; clave b:

  > Un almacén tiene una capacidad de 1500 unidades. Si el almacén tiene 525 unidades en stock y todos los días se reciben y almacenan 65 unidades, ¿cuántos días necesita para alcanzar su máxima capacidad?
  > a) 28 días.
  > b) 15 días.
  > c) 17 días.
  > d) 12 días.

Questions: 2025-R1-5, 2024X-P1-34, 2024X-P1-35, 2024X-P1-38, 2024X-P1-39, 2022-P1-35, 2022-P1-38, 2022-P1-39, 2022-R1-5, 2020-P1-51, 2020X-P1-35.

### Porcentajes (`calculo-porcentajes`) — 10 questions, 4 exams

**What is asked.** Price after a discount or an increase, the complement of a percentage of a total, the share of a part, simple probability as a percentage.

**Subtypes** (classifier's labels): porcentaje complementario de un total (2); probabilidad simple en porcentaje (2); precio tras descuento (1); precio tras incremento (1); porcentaje del resto sobre un total (1); porcentaje de una parte sobre el total (1); porcentaje de una cantidad y precio unitario (1); porcentaje de un total (1).

**Parameters.** Percentages 4–64 %; bases from 45 to 47 million; options with 2 decimals.

**Difficulty.** Levels 1/2/3: 7/3/0. Level 1 for one multiplication; level 2 for large bases (2024X, 32) or two steps (2022, 32).

**Example.** 2025 ord. (A/B), parte 1 40 (modelo B 41); clave b:

  > Si hay un 8 % de descuento en un producto cuyo precio original es de 45 €, ¿qué importe se pagará una vez aplicado el descuento?
  > a) 40,25 €
  > b) 41,40 €
  > c) 38,72 €
  > d) 39,05 €

Questions: 2025-P1-40, 2025-P1-41, 2025-P1-42, 2024-P1-40, 2024-P1-44, 2024-P1-47, 2024-R1-4, 2024X-P1-32, 2022-P1-32, 2022-P1-36.

### Series numéricas (`serie-numerica`) — 9 questions, 5 exams

**What is asked.** «¿Qué número continúa la secuencia…?»: geometric series and interleaved series where one subsequence drives the other.

**Subtypes** (classifier's labels): serie intercalada con producto acumulado (2); progresión geométrica decreciente (2); serie intercalada con divisor constante (1); serie de suma con sumandos intercalados (1); serie recurrente a·2+3 (1); serie intercalada con factor constante (1); serie intercalada ambigua (1).

**Parameters.** Length 4–7. Rules seen: ÷3, ÷4; interleaved product (5, 3, 15, 4, 60, 5 → ×3, ×4, ×5); interleaved constant divisor or factor; sum with interleaved addends; aₙ₊₁ = 2aₙ + 3. 2020, 53 was annulled: two rules fit.

**Difficulty.** Levels 1/2/3: 4/5/0. Level 1 for geometric series; level 2 when interleaved.

**Example.** 2025 ord. (A/B), parte 1 44 (modelo B 43); clave a:

  > ¿Qué número continúa la secuencia 5, 3, 15, 4, 60, 5, _?
  > a) 300
  > b) 320
  > c) 280
  > d) 340

Questions: 2025-P1-44, 2025-P1-45, 2024-P1-45, 2024-P1-46, 2024-P1-48, 2024X-P1-33, 2022-P1-34, 2022-P1-37, 2020-P1-53.

### Clasificación y archivo (`administrativo-clasificacion`) — 9 questions, 4 exams

**What is asked.** Where an item is filed under a stated scheme: cabinet and drawer by type and size; drawer or folder for a surname by alphabetical ranges; shelf location of a title by topic and initial (2024 «Biblioteca»).

**Subtypes** (classifier's labels): ubicación de un título según tabla de clasificación (2); título que corresponde a una ubicación (2); pasillo para un nombre en orden alfabético (1); ubicación armario-cajón (1); cajón para un nombre en orden alfabético (1); ubicación armario-cajón por apellido (1); carpeta para un nombre en orden alfabético (1).

**Parameters.** 6–8 alphabetical ranges, or 8 cabinets × 3 drawers, or a 10-row classification table with two criteria.

**Difficulty.** Levels 1/2/3: 4/5/0. Level 1–2. Alphabetical-range items need the ordering rules of administrativo-ordenacion.

**Example.** OEP 2020 ord., parte 1 40; clave d:

  > En un almacén guardan cada tipo de tela en un armario: la Batista en el número 1, el Tweed en el 2, la Gabardina en el 3, el Lino en el 4, la Franela en el 5, el Crepé en el 6, el Encaje en el 7 y el Raso en el 8. Cada armario tiene tres cajones para los distintos tamaños de rollos de tela: el cajón A para 10 metros, el B para 15 metros y el C para 25 metros. ¿En qué ubicación guardarán un rollo de 10 metros de Franela?
  > a) 4B
  > b) 5B
  > c) 7C
  > d) 5A

Questions: 2024-P1-49, 2024-P1-50, 2024-P1-53, 2024-P1-54, 2022-P1-48, 2020-P1-40, 2020-P1-60, 2020X-P1-32, 2020X-P1-45.

### Fracciones y repartos (`calculo-fracciones-proporciones`) — 4 questions, 4 exams

**What is asked.** What remains of a total after fractions are used; proportional sharing among 3–4 parts.

**Subtypes** (classifier's labels): fracción restante de un total (2); reparto proporcional (2).

**Parameters.** Denominators 8, 9 or 18; totals chosen to divide exactly (616 / 8 = 77). Sharing among 3–4 parts with 1–2 decimals.

**Difficulty.** Levels 1/2/3: 1/3/0. Level 1 when the total divides exactly; level 2 for proportional sharing.

**Example.** 2025 ord. (A/B), parte 1 43 (modelo B 45); clave b:

  > Tenemos que preparar 616 paquetes de bienvenida. El primer día preparamos tres octavos del total de paquetes y el segundo día preparamos dos octavos de total. ¿Cuántos paquetes nos quedan por preparar?
  > a) 259.
  > b) 231.
  > c) 212.
  > d) 244.

Questions: 2025-P1-43, 2022-P1-33, 2020-P1-52, 2020X-P1-34.

### Ordenación alfabética (`administrativo-ordenacion`) — 4 questions, 4 exams

**What is asked.** «¿Qué serie indica el orden alfabético correcto…?»: four orderings of the same 4–5 words.

**Subtypes** (classifier's labels): orden alfabético de palabras (4).

**Parameters.** 4–5 words sharing a 2–4 letter prefix; the order is decided at the 3rd–5th letter.

**Difficulty.** Levels 1/2/3: 3/1/0. Level 1–2.

**Example.** 2024 extr., parte 1 46; clave c:

  > ¿Qué serie indica el orden alfabético correcto de las siguientes palabras?
  > a) giramiento, girada, giraldete, girándula.
  > b) girada, girándula, giraldete, giramiento.
  > c) girada, giraldete, giramiento, girándula.
  > d) giraldete, girada, giramiento, girándula.

Questions: 2024X-P1-46, 2022-P1-47, 2020-P1-59, 2020X-P1-44.

### Series alfanuméricas (`serie-alfanumerica`) — 2 questions, 2 exams

**What is asked.** Letters with digits between them that give the jump to the next letter.

**Subtypes** (classifier's labels): letras con saltos crecientes indicados por cifras (2).

**Parameters.** Length 7; jumps n = 2–5. One series wraps from Z to A (2020X); one only works counting Ñ (2020, 50: without Ñ the answer would be Q).

**Difficulty.** Levels 1/2/3: 0/2/0. Level 2: the alphabet convention (Ñ, wrap) decides the key.

**Example.** OEP 2020 extr., parte 1, reserva 4; clave c:

  > ¿Qué letra completa la serie? X, 2, A, 3, E, 4, _
  > a) F
  > b) U
  > c) J
  > d) K

Questions: 2020-P1-50, 2020X-R1-4.

### Analogías (`verbal-analogia`) — 2 questions, 2 exams

**What is asked.** «¿Qué par de palabras NO mantiene la relación que encontramos entre A y B?»: four pairs, container–contents.

**Subtypes** (classifier's labels): par que no mantiene la relación (continente–contenido) (2).

**Parameters.** Four pairs, negative stem.

**Difficulty.** Levels 1/2/3: 0/0/2. Level 3, and both official items have a disputed key: more than one pair breaks the relation (see the ledger).

**Example.** OEP 2020 extr., parte 1 39; clave c:

  > ¿Qué par de palabras NO mantiene la relación que encontramos entre BOTELLA y LIQUIDO?
  > a) Billetera y Dinero.
  > b) Calle y Semáforo.
  > c) Televisor y Cama.
  > d) Bandera y Asta.

Questions: 2020-P1-55, 2020X-P1-39.

### Palabra intrusa (`verbal-intrusa`) — 2 questions, 2 exams

**What is asked.** «Señale la palabra que NO pertenece al grupo»: four words, one outside the category.

**Subtypes** (classifier's labels): palabra intrusa (2).

**Parameters.** Four words; one category (colectivos de animales, …).

**Difficulty.** Levels 1/2/3: 1/1/0. Level 1–2.

**Example.** 2024 extr., parte 1 47; clave b:

  > Señale la palabra que NO pertenece al grupo.
  > a) Rebaño.
  > b) Flora.
  > c) Colmena.
  > d) Piara.

Questions: 2024X-P1-47, 2022-P1-43.

## 4. Format

- Four options, one correct, as in bloque I. Options are one word or one number in most types (mean option length 1–3 words).
- Stems are short (mean 17–23 words), except table items, which add the table once before the set and repeat «según los datos del cuadro…» or «Responda a las siguientes preguntas según la tabla llamada…».
- Numbers use the Spanish decimal comma and thousands point; money as «41,40 €», percentages as «25,83 %».
- Psicotécnico items are questions 31–60, grouped by kind. Since 2022 the two table sets close the section (49–60); in the OEP 2020 exams the table sets sit in the middle (2020: 31–36 and 44–49; 2020 extr.: 46–51 and 55–60). The part-1 reserve mixes bloque I and psicotécnico items.
- No calculator (cover instructions of the OEP 2020 questionnaires: «no puede utilizar calculadora ni ningún otro dispositivo electrónico»).

## 5. Keys, notes and anomalies

- 2024-R1-5 (calculo-ecuaciones), vigente. Errata: enunciado «Halle el valor de 21(4x – 6) = x» sin «x en».
- 2024X-P1-32 (calculo-porcentajes), vigente. Errata: «mayores de 4 años» por «de 4 años o más» (el complementario de «menores de 4»); no cambia la clave.
- 2024X-P1-53 (tablas-lectura), vigente. Errata: la clase «alumnos sin pelo» es todo alumno que no sea rubio, moreno ni pelirrojo (nota bajo la tabla).
- 2024X-P1-56 (atencion-codificacion), vigente. Errata: opción c «Puedan ser tener el mismo soporte».
- 2024X-R1-4 (calculo-ecuaciones), vigente. Errata: reserva idéntica a 2024X-P1-36 (mismo enunciado, opciones y clave).
- 2022-P1-39 (calculo-problemas), vigente-con-nota. Clave oficial discutida: «b» solo da 52 operando de izquierda a derecha; con la prioridad habitual de la multiplicación ninguna opción da 52 (b = −118).
- 2022-P1-44 (verbal-definicion), vigente. Errata: opción d «Enjuciable» por «Enjuiciable».
- 2022-P1-48 (administrativo-clasificacion), vigente. Errata: los rótulos D2 «Rota, Peter» y D3 «Rota, Marta» no están en orden alfabético; no afecta a la clave.
- 2022-R1-5 (calculo-problemas), vigente-con-nota. Clave oficial discutida: 1.105/85 = 13 contrataciones, pero con una contratación cada dos días se llega el día 24 o 26; ninguna opción lo recoge y la clave «el día 13» confunde contrataciones con días.
- 2020-P1-41 (calculo-ecuaciones), vigente. Redondeo: la opción oficial trunca el valor exacto en vez de redondearlo; sigue siendo la única cercana (−0,6757 → «−0,67»).
- 2020-P1-53 (serie-numerica), anulada. Anulada en la plantilla definitiva. Lectura de la ronda: el siguiente término es par de la subserie 1,2,… → 3 (c); si se toma la siguiente suma, 10 (b): ambigua.
- 2020-P1-55 (verbal-analogia), vigente-con-nota. Clave oficial discutida: «Gafa y Ojo» tampoco mantiene la relación continente–contenido (y «Mar y Arena» es dudosa); la respuesta no es única.
- 2020-R1-2 (calculo-ecuaciones), vigente. Redondeo: la opción oficial trunca el valor exacto en vez de redondearlo; sigue siendo la única cercana (−3,0476 → «−3,04»).
- 2020X-P1-39 (verbal-analogia), vigente-con-nota. Clave oficial discutida: «Bandera y Asta» tampoco es continente–contenido (y «Calle y Semáforo» es dudosa); la respuesta no es única. Errata: «LIQUIDO» sin tilde.
- 2020X-P1-54 (calculo-ecuaciones), anulada. Anulada en la plantilla definitiva. Lectura de la ronda: 45x−60=−x → x=60/46=1,304; ninguna opción coincide (explica la anulación).

Repeated items: 2024X reserve 4 is identical to 2024X, 36. 2024 reserve 3 (antónimo de VENTURA) repeats 2025, 36.

