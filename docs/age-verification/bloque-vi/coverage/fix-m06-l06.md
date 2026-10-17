# Coverage fix — m06-l06 (writer, 2026-10-17)

Lesson: `content/age-administrativo-c1/es/lessons/m06-l06.md`. Words (`wc -w`): 1477 before, **1660** after (no
ceiling, requirements v1.5). Lines ≤ 120 (only the `#` title line is longer, unchanged). Fuentes reordered with
`fuentes_order.py --write` (in order, none missing or uncited). Content tests (`pytest -m 'not integration' -k "glossary
or registry or content or pipeline"`): 68 passed.

`fixes.md` has no row for m06-l06 (coverage report: 24 asked, 24 covered). Every change below is a restoration under
«Rule change (2026-10-17, requirements v1.5)». Nothing was cut.

## Restorations

Cut lists read: the ledger (bloque VI, «Cut for length» under Open items: «m06-l06 Expresiones (2020 61, 62, 64)»;
«Decisions after bloque VI» item 4 concerns m06-l02 only), the «Cuts made for length» section of
`docs/age-verification/bloque-vi/m06-l06.md`, and `recheck-queue.md` (no m06-l06 cut). Each candidate was checked
against `docs/age-ofimatica-index.md` and the questionnaires.

### 1. 2020 ord. 61 — SiInm in a calculated field (key d)

Asked: `SiInm([País]="Francia";"Francés";"Español")` shows Francés if País is Francia, otherwise Español.

New item (Consultas, after Campo calculado):
`- **SiInm**: recibe tres argumentos: una expresión, el valor que devuelve si es verdadera y el que devuelve si es`
`  falsa (fuente: `ms-access-expresiones.html`).`

Source `ms-access-expresiones.html` (new), «Condiciones de solo dos valores»: «Se pasan tres argumentos a la función
SiInm: El primer argumento es una expresión que debe devolver un valor o TrueFalse . El segundo argumento es el valor
que se devuelve si la expresión es verdadera y el tercer argumento es el valor devuelto si la expresión es falsa.»

### 2. 2020 ord. 62 — Campo calculado `A_N: Año([FechaNacimiento])` (key c)

Asked: the query returns, for each row, the year of FechaNacimiento in a column named A_N. Two parts: the name before
the colon names the column; Año returns the year.

Old (Consultas):
`- **Campo calculado**: en la fila Campo, una expresión con nombre, como`
`  Subtotal: ([Cantidad]*[Precio unitario])-([Cantidad]*[Precio unitario]*[Descuento]) (fuente:`
`  `ms-access-consultas.html`).`

New:
`- **Campo calculado**: columna de la consulta con el resultado de una expresión; lo que va delante de los dos puntos`
`  es el nombre del campo (fuente: `ms-access-expresiones.html`). Se escribe en la fila Campo, como`
`  Subtotal: ([Cantidad]*[Precio unitario])-([Cantidad]*[Precio unitario]*[Descuento]) (fuente:`
`  `ms-access-consultas.html`).`

New item (after SiInm):
`- **Año**: devuelve un número entero que representa el año de una fecha (fuente: `ms-access-funcion-ano.html`).`

Sources: `ms-access-expresiones.html`, «Consultas y filtros»: «Un campo calculado es una columna en una consulta que es el
resultado de una expresión.»; table row «FullName: [FirstName] & " " & [LastName] | Crea un campo llamado NombreCompleto
donde se muestran los valores de los campos Nombre y Apellidos» (the name before the colon is the new field's name; the
expressions are printed with English identifiers, the descriptions in Spanish). `ms-access-consultas.html` (unchanged
support): «En el cuadro Zoom, escriba o pegue lo siguiente: Subtotal: ([Cantidad]*…)», reached from «la fila Campo».
`ms-access-funcion-ano.html` (new): «Devuelve un valor de tipo Variant (Integer) que contiene un número entero que
representa el año.»; argument: «cualquier variante, expresión numérica, expresión de cadena o cualquier combinación de
estos que pueda representar una fecha».

### 3. 2020 ord. 64 — Conmutador in Origen del control (key b)

Asked: in a report text box, `=Conmutador([País]="UK";"Libra";[País]="USA";"Dólar")` written in Origen del control
shows Libra for UK and Dólar for USA.

New items (Informes, after Agrupación, orden y total):
`- **Control calculado**: en un formulario o informe, la expresión se escribe en la propiedad ControlSource del`
`  control, no en un campo de tabla o consulta (fuente: `ms-access-expresiones.html`). En vista Diseño, el origen de`
`  control de un cuadro de texto se edita en el propio cuadro, sin la hoja de propiedades (fuente:`
`  `ms-access-formularios.html`).`
`- **Conmutador**: recibe pares de expresión y valor; evalúa las expresiones de izquierda a derecha y devuelve el valor`
`  de la primera verdadera (fuente: `ms-access-funcion-conmutador.html`).`

Sources: `ms-access-expresiones.html`, «Formularios e informes»: «Para crear control calculado, escriba una expresión en
la ControlSource propiedad del control en lugar de en un campo de tabla o consulta.» `ms-access-formularios.html`
(already saved), vista Diseño list: «Editar orígenes de control de cuadro de texto en los propios cuadros de texto, sin
usar la hoja de propiedades.» `ms-access-funcion-conmutador.html` (new), «Observaciones»: «La lista de argumentos de la
función Switch consta de pares de expresiones y valores. Las expresiones se evalúan de izquierda a derecha y se devuelve
el valor asociado a la primera expresión que se evalúa como verdadera.»

Labels: no saved page prints «Origen del control» (the exam's label). The expresiones page prints the property name
«ControlSource»; the formularios page prints «orígenes de control de cuadro de texto», the official label the ledger's
table gives for 2020 64. The lesson prints both as printed and does not state that they are the same property. The
function is «Conmutador» in the page title and body («el conmutador devuelve el valor 2»); the syntax line prints
`Switch(…)` and one sentence «la función CAMBIAR»; the lesson uses «Conmutador», as the title does.

### 4. 2022 ord. 57 (anulada) — Texto largo, 65.535 characters

Asked (stem: which statement on Access 2019 is incorrect): option a «Un campo de Texto largo puede contener hasta 65.535
caracteres». The writer cut «Texto largo 65.535 characters via the UI» within items (notes, «Cuts made for length»).

Old (Principales funciones y utilidades):
`- **Límites**: 2 GB por base de datos; nombre de objeto, de tabla o de campo, hasta 64 caracteres; 255 campos por`
`  tabla (fuente: `ms-access-especificaciones.html`).`

New:
`- **Límites**: 2 GB por base de datos; nombre de objeto, de tabla o de campo, hasta 64 caracteres; 255 campos por`
`  tabla; en un campo Texto largo, 65.535 caracteres al introducir los datos en la interfaz de usuario (fuente:`
`  `ms-access-especificaciones.html`).`

Source `ms-access-especificaciones.html` (already saved): «Número de caracteres de un campo Texto largo | 65.535 al
introducir datos a través de la interfaz de usuario; 1 gigabyte de almacenamiento de caracteres al escribir datos
mediante programación». The Tipos de datos item keeps «Texto largo, hasta 1 GB aproximadamente».

## Considered, not restored

| Cut | Why not |
|---|---|
| Número sizes (1–16 bytes) | Only a distractor of 2024 A 56 (anulada, «Números hasta 16 bytes»); the stem asks Moneda, which the lesson states. The index row is «Tipo de datos Moneda». Coordinator may decide otherwise. |
| Sí/No (1 byte, 0/-1); 32 tables per query; 10 fields per primary key; Autonumeración starting at 1; types without validation rules; Crear tabla deleting a same-name table; report tools list; the Detalle section; macros and modules not exportable to Excel | No index row asks them (any year). |
| Pages read, not saved (parámetros prompt, Indizado refusing a repeated value, informe agrupado, origen de registros, atajos, funciones por categoría) | Not cuts of asked facts: the rows they relate to (2025 A 60, 2025 X 59, 2022 60, 2024 A 57) are covered by the lesson. |

Re-checked: every covered row of `coverage/m06-l06.md` still has its quoted text in the lesson (nothing was cut; the
Límites quote «nombre de objeto, de tabla o de campo, hasta 64 caracteres» is unchanged).

## New sources (for `fuentes.yaml`; not edited)

Saved with `curl -sL` from the final URL (HTTP 200, no redirect), `lang="es-ES"`, canonical = URL.

```yaml
- file: ms-access-expresiones.html
  url: "https://support.microsoft.com/es-es/access/examples-of-expressions"
  title: "Microsoft, «Ejemplos de expresiones»"
  consultado: "2026-10-17"
  sha256: 2e00d3d268c2f6ed9434da086f8769a235979a3986800d584036301439f933ab
  lessons: [m06-l06]
- file: ms-access-funcion-ano.html
  url: "https://support.microsoft.com/es-es/access/year-function"
  title: "Microsoft, «Función Año»"
  consultado: "2026-10-17"
  sha256: 2972a4d8685b5a2cb7fe8a6c1281b1212dba0e915ccc040e2250159a43687105
  lessons: [m06-l06]
- file: ms-access-funcion-conmutador.html
  url: "https://support.microsoft.com/es-es/access/switch-function"
  title: "Microsoft, «Función Conmutador»"
  consultado: "2026-10-17"
  sha256: 21d127369e903fabd9cdcf74c6d043c455829e4ff3a84ab51926c5befe228971
  lessons: [m06-l06]
```

Ledger follow-up for the coordinator: the «Cut for length» line «m06-l06 Expresiones (2020 61, 62, 64)» and the label
table row «Origen del control» («item cut») are now restored.

Sin fuente oficial: none new.
