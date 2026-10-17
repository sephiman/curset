# Blind verification of the coverage fix — m06-l06 (2026-10-17), with the m06-l08 check

Spec: `fix-spec.md` («Verifier» and «Rule change»: no word ceiling; restorations allowed). Inputs: `fix-m06-l06.md`
and `fix-m06-l08.md` (writers' claims), `m06-l06.md` (coverage report). Lesson as it now stands:
`content/age-administrativo-c1/es/lessons/m06-l06.md` (compared with `git diff HEAD`). Pages read with `pagetext.py`.
Exam texts read from `sources/examenes-oficiales/` (`conv2020_cuestionario.pdf` 61, 62, 64; `conv2022_cuestionario.pdf`
57). Cut lists read: ledger bloque VI «Cut for length» and «Decisions after bloque VI» item 4, the «Cuts made for length»
sections of `bloque-vi/m06-l06.md` and `bloque-vi/m06-l08.md`, `recheck-queue.md`; checked against the Access and
Internet tables of `docs/age-ofimatica-index.md`.

## Changes (m06-l06)

| # | Change | Check | PASS/FAIL | Reason | Replacement |
|---|---|---|---|---|---|
| 1 | New item «SiInm»: «recibe tres argumentos: una expresión, el valor que devuelve si es verdadera y el que devuelve si es falsa» | literal on page | PASS | `ms-access-expresiones.html`, «Condiciones de solo dos valores»: «Se pasan tres argumentos a la función SiInm: El primer argumento es una expresión que debe devolver un valor o TrueFalse . El segundo argumento es el valor que se devuelve si la expresión es verdadera y el tercer argumento es el valor devuelto si la expresión es falsa.» The item gives no syntax line; the page's examples print `IIf(…, …, …)` with English identifiers and commas, so nothing printed is misquoted | — |
| 1 | 2020 ord. 61 now stated | fact asked | PASS | Key d («Si el campo País contiene el valor Francia, se mostrará Francés. En caso contrario se mostrará Español»): condition, value if true, value if false rules out a, b and c | — |
| 2 | Campo calculado: «columna de la consulta con el resultado de una expresión» | literal on page | PASS | `ms-access-expresiones.html`, «Consultas y filtros»: «Un campo calculado es una columna en una consulta que es el resultado de una expresión.» | — |
| 2 | Campo calculado: «lo que va delante de los dos puntos es el nombre del campo» | literal on page | FAIL | `ms-access-expresiones.html` never says it; the writer infers it from table rows such as «FullName: [FirstName] & " " & [LastName] \| Crea un campo llamado NombreCompleto», where the printed name before the colon is not even the name the description gives (also «ExtendedPrice: … \| Designa el campo calculado PrecioTotal»). No saved page states it («dos puntos» does not occur in any saved Access page in this sense). An official Spanish page states it literally: https://support.microsoft.com/es-es/access/create-a-simple-select-query (HTTP 200, no redirect, `lang="es-ES"`, canonical = URL, title «Crear una consulta de selección sencilla»), «Usar una expresión como campo de salida»: «En el cuadro Zoom, escriba o pegue la expresión. Anteponga la expresión con el nombre que desea utilizar en la expresión de salida, seguido de dos puntos.» Downloaded copy: `/tmp/claude-1000/-home-juanjo-PycharmProjects-curset/3bfdbef1-0a20-46f7-a34d-245ff55c6923/scratchpad/dl-l06/q_create-a-simple-select-query.html`, sha256 `14a9c039b0109d90ed940cd6c0a0d4977bd946424a62df27aa59552e9e910647` | `- **Campo calculado**: columna de la consulta con el resultado de una expresión (fuente:` / `` `ms-access-expresiones.html`). Se escribe en la fila Campo, precedida del nombre del campo de salida y dos puntos, `` / `como Subtotal: ([Cantidad]*[Precio unitario])-([Cantidad]*[Precio unitario]*[Descuento]) (fuente:` / `` `ms-access-consulta-seleccion.html`, `ms-access-consultas.html`). `` Save the page as `ms-access-consulta-seleccion.html`; fuentes.yaml entry: url above, title «Microsoft, «Crear una consulta de selección sencilla»», consultado "2026-10-17", the sha256 above (re-hash after saving), lessons [m06-l06]; Fuentes line after `ms-access-expresiones.html`, before `ms-access-funcion-ano.html` |
| 2 | New item «Año»: «devuelve un número entero que representa el año de una fecha» | literal on page | PASS | `ms-access-funcion-ano.html`: «Devuelve un valor de tipo Variant (Integer) que contiene un número entero que representa el año.»; argument: «cualquier variante, expresión numérica, expresión de cadena o cualquier combinación de estos que pueda representar una fecha». No syntax line in the item; the page prints `Year(date)` only | — |
| 2 | 2020 ord. 62 now stated | fact asked | PASS (once row above is fixed) | Key c (the year, column A_N): Año gives the year (rules out b); the name before the colon names the column (rules out d); nothing prompts for a value (rules out a). The column-name half rests on the FAIL row above | — |
| 3 | New item «Control calculado», first sentence: «la expresión se escribe en la propiedad ControlSource del control, no en un campo de tabla o consulta» | literal on page; label | PASS | `ms-access-expresiones.html`, «Formularios e informes»: «Para crear control calculado, escriba una expresión en la ControlSource propiedad del control en lugar de en un campo de tabla o consulta.» «ControlSource» is the name as printed (English, the page's own word order garbled); the lesson fixes only the word order. The exam's label «Origen del control» is printed by no saved page and the lesson does not print it, nor does it claim ControlSource and «origen de control» are the same property — correct under «labels as printed» | — |
| 3 | «Control calculado», second sentence: «En vista Diseño, el origen de control de un cuadro de texto se edita en el propio cuadro, sin la hoja de propiedades» | literal on page; scope | FAIL | `ms-access-formularios.html`, list under «vista Diseño» of a form: «Editar orígenes de control de cuadro de texto en los propios cuadros de texto, sin usar la hoja de propiedades.» The wording is faithful («orígenes de control» singularised, lower case, not shown as a label), but the page speaks only of forms; the item sits in «Informes» and opens with «en un formulario o informe», so the unqualified «En vista Diseño» reads as covering reports too | `En la vista Diseño de un formulario, el origen de control de un cuadro de texto se edita en el propio cuadro, sin` / `` la hoja de propiedades (fuente: `ms-access-formularios.html`). `` |
| 3 | New item «Conmutador»: «recibe pares de expresión y valor; evalúa las expresiones de izquierda a derecha y devuelve el valor de la primera verdadera» | literal on page | PASS | `ms-access-funcion-conmutador.html`, «Observaciones»: «La lista de argumentos de la función Switch consta de pares de expresiones y valores. Las expresiones se evalúan de izquierda a derecha y se devuelve el valor asociado a la primera expresión que se evalúa como verdadera.» Name «Conmutador» as in the title and «el conmutador devuelve el valor 2»; no syntax line in the item (the page prints `Switch(expr-1, value-1 [, expr-2, value-2 ] …)`) | — |
| 3 | 2020 ord. 64 now stated | fact asked | PASS | Key b `=Conmutador([País]="UK";"Libra";[País]="USA";"Dólar")`: pairs of expression and value rules out d («… O "Libra"») and c; a is Elegir. The expression in a control rules in the Origen del control setting of the stem | — |
| 3 | Writer's note on the page's names | notes accuracy | PASS | Correct in substance; minor: «la función CAMBIAR» occurs twice (syntax table intro and the VBA example), plus «la fórmula "Cambiar"» in the query example, not «one sentence». Lesson unaffected | — |
| 4 | Restoration: Límites «en un campo Texto largo, 65.535 caracteres al introducir los datos en la interfaz de usuario» | literal; exam row | PASS | `ms-access-especificaciones.html`: «Número de caracteres de un campo Texto largo \| 65.535 al introducir datos a través de la interfaz de usuario; 1 gigabyte de almacenamiento de caracteres al escribir datos mediante programación». Exam row 2022 ord. 57 (anulada; index Access table «Especificaciones de Access»), option a «Un campo de Texto largo puede contener hasta 65.535 caracteres». Tipos de datos keeps «hasta 1 GB aproximadamente» (the programmatic figure), consistent | — |
| 5 | Restorations not made (Número sizes, Sí/No, 32 tables per query, 10 fields per key, Autonumeración start, types without rules, Crear tabla deleting a same-name table, report tools, Detalle, macro/module export; pages read, not saved) | rule change | PASS | None has an index row (any year) in the Access table (34 rows read). Número sizes appear only as a distractor of 2024 A 56 (anulada, row «Tipo de datos Moneda», covered by the Moneda item). The «read, not saved» pages relate to covered rows | — |
| 6 | Nothing cut; covered rows re-checked | no asked fact removed | PASS | `git diff HEAD` shows additions only, plus the Límites line (its quoted text «nombre de objeto, de tabla o de campo, hasta 64 caracteres» unchanged) and the Campo calculado item (not quoted by any row). All 24 covered rows' quotes found verbatim in the lesson | — |

## Form

| Check | PASS/FAIL | Reason |
|---|---|---|
| Words | PASS | 1660 (`wc -w`); no ceiling under requirements v1.5 |
| Lines ≤ 120 | PASS | Only line 1 (the fixed `#` title, 168) is longer |
| Fuentes complete and in order | PASS | `fuentes_order.py`: missing [], uncited [], in order True. Three new lines in place (expresiones and funcion-ano after criterios; funcion-conmutador after informes). After the row-2 fix, `ms-access-consulta-seleccion.html` goes after `ms-access-expresiones.html` |
| List-shape hygiene | PASS | No `- `, `* ` or `1. ` after sentence punctuation mid-line |
| Voice | PASS | Terse, no fillers, questions or closers; no coined terms (SiInm, Año, Conmutador, ControlSource, campo calculado are Microsoft's). Note, not a FAIL: «Campo calculado» and «Control calculado» run to four lines against R2 rule 3's «one line or two»; the lesson already had three-line items that passed, and the word ceiling is lifted |

## New sources

| File | sha256 vs fix notes | Official, Spanish | Final URL | Re-download | PASS/FAIL |
|---|---|---|---|---|---|
| `ms-access-expresiones.html` | match (`2e00d3d2…`) | support.microsoft.com, `lang="es-ES"`, title «Ejemplos de expresiones» | canonical = recorded URL | fetched 2026-10-17: HTTP 200, same final URL; bytes differ (page chrome, sha256 `8e7cdf18…`), extracted text identical (700 lines, empty diff) | PASS |
| `ms-access-funcion-ano.html` | match (`2972a4d8…`) | support.microsoft.com, `lang="es-ES"`, title «Función Año» | canonical = recorded URL | not re-downloaded | PASS |
| `ms-access-funcion-conmutador.html` | match (`21d12736…`) | support.microsoft.com, `lang="es-ES"`, title «Función Conmutador» | canonical = recorded URL | fetched 2026-10-17: HTTP 200, same final URL; bytes differ (sha256 `aceb9b5c…`), extracted text identical (226 lines, empty diff) | PASS |

None is in `fuentes.yaml` yet (expected; coordinator merges). The three YAML entries in `fix-m06-l06.md` match file,
URL, title and hash.

## m06-l08 (claims of `fix-m06-l08.md`)

| Check | PASS/FAIL | Reason |
|---|---|---|
| No restorable cut an exam asked | PASS | Ledger «Cut for length» (bloque VI) has no m06-l08 entry; «Decisions after bloque VI» item 4 is m06-l02. Writer notes: «None forced (1438 words)»; the items left out by choice (NSFNET/1985 mandate, HTML 2.0–4.01 history, RFC 1918 block names, DNSSEC, Edge Ctrl+L/Ctrl+Entrar, «Bloquear cookies de terceros», InPrivate search with Bing) have no index row; InPrivate is in the VI.8 «Never» list. RFC 1918: 2022 X 64 asks a block, and the lesson's «Direcciones privadas» item gives all three ranges (key a 172.16.0.0–172.31.255.255). `recheck-queue.md` WHATWG section: Mosaic/NCSA and the English expansion removed for lack of a source, not for space; 2020 ord. 65 (sigla of «Lenguaje de Marcado de Hipertexto») and 2020 X 69 (standard markup language) stay answered by the HTML item («lenguaje de marcado principal de la World Wide Web»; «.htm y .html son páginas de lenguaje de marcado de hipertexto») |
| Lesson unchanged by this pass | PASS | `git diff HEAD` and `git status` show nothing for `m06-l08.md`; the WHATWG edits (World Wide Web y HTML, HTML, JavaScript items citing `whatwg-html-*.html`) are already in HEAD (commit 7391bb1, «AGE-C1: r2 block 6») and present in the file. 1471 words, as the notes say |

## Counts

- m06-l06 change rows: 14; PASS 12, FAIL 2 (row 2 «dos puntos» sentence; row 3 «En vista Diseño» scope).
- Form: 5 PASS. New sources: 3 PASS (2 re-downloaded, text identical).
- m06-l08: 2 PASS.
- Total: 24 checks, 22 PASS, 2 FAIL.
