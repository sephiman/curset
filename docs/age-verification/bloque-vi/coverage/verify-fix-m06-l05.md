# Coverage fix — m06-l05: blind verification (2026-10-17)

Inputs: `fix-m06-l05.md` (writer's claims), `m06-l05.md` (coverage report), `fix-spec.md` incl. «Rule change»
(no word ceiling; restorations). Lesson `content/age-administrativo-c1/es/lessons/m06-l05.md` as it now stands (not
edited). Page text with `SP/tools/pagetext.py` on the files in `C/sources/otros/`.

## Changes, restorations, sources

| # | item (first words) | field(s) | PASS/FAIL | reason | replacement |
|---|---|---|---|---|---|
| 1 | Texto y fecha: «DIVIDIRTEXTO desborda el texto entre columnas o hacia abajo por filas» | behaviour | PASS | Page: «Permite dividir entre columnas o hacia abajo por filas» / «col_delimiter El texto que marca el punto donde se va desbordar el texto entre columnas» / «row_delimiter … hacia las filas inferiores». Coverage 2024 X 63: spilling across columns from the formula cell is the J44/K44 fact; row now covered. | — |
| 2 | **#¿NOMBRE?**: sale por un error ortográfico… | label, behaviour | PASS | Label as printed: the page title prints «Cómo corregir un error #¿NOMBRE?» and the body «la fórmula de ÍNDICE genera el error ¿#NOMBRE?»; `ms-excel-funcion-sierror.html` prints «#¿NOMBRE?». The body's «#NAME?» is untranslated text; the lesson rightly uses the Spanish label. Causes literal: «error ortográfico en el nombre de la fórmula», «nombre no definido», «omite las comillas dobles "" para un valor de texto». Coverage 2022 54: with the SI.ERROR item (official name), the reader can derive that «SIERROR» gives #¿NOMBRE?; row now covered. The lesson does not name SIERROR (key disputed): correct. | — |
| 3 | Restored: «EXTRAE(texto; posición_inicial; núm_de_caracteres): el primer carácter … es la posición 1» | syntax, behaviour | PASS | Page: «EXTRAE(texto, posición_inicial, núm_de_caracteres)» and «posición_inicial para el primer carácter de texto es 1». «;» per the lesson intro and the page's own examples («=EXTRAE(A2;1;5)»). Exam row 2020 ord. 60 (EXTRAE(A1;12;2) → 01), index `vigente`: restoration required and done. | — |
| 4 | Source `ms-excel-funcion-dividirtexto.html` | sha256, URL, lang, title | PASS | sha256 2f5061be… matches; canonical https://support.microsoft.com/es-es/excel/functions/textsplit-function; `lang="es-ES"`; `<title>` «Función TEXTSPLIT» (English name printed; body uses DIVIDIRTEXTO). | — |
| 5 | Source `ms-excel-error-nombre.html` | sha256, URL, lang, title, re-download | PASS | sha256 c4ac8cd9… matches; canonical …/es-es/excel/how-to-correct-a-name-error; `lang="es-ES"`; title «Cómo corregir un error #¿NOMBRE?». Re-downloaded 2026-10-17 (final URL unchanged, 200): extracted text identical to the saved file's. | — |
| 6 | Source `ms-excel-funcion-extrae.html` | sha256, URL, lang, title | PASS | sha256 a992485b… matches; canonical …/es-es/excel/functions/mid-function; `lang="es-ES"`; title «MID (función)» as printed (body: EXTRAE). | — |
| 7 | Fuentes: three new lines | titles, order | PASS | Titles as the pages print them («Función TEXTSPLIT», «MID (función)», «Cómo corregir un error #¿NOMBRE?»). `fuentes_order.py` (read-only): none missing, none uncited, in order. | — |
| 8 | «Checked and not restored» | restoration scope | PASS | Index VI.5 rows (28) checked: MAX's asked fact (2022 X 60) is «Sin fuente oficial»; BUSCARV (2020 58, anulada), FORMULATEXTO (2020 X 56), FILAS, DIA (2020 57) are stated from the category / DIA pages; no index row asks 1900/1904, referencia 3D, Ctrl+Av Pág/Re Pág or «con contraseña o sin ella». 2024 A 60 («20-2») stays out. | — |

## Coverage re-check (lesson as it now stands)

Every row of `m06-l05.md` marked covered (15) still has its quoted text in the lesson (string check after unwrapping):
FILAS/estructurada, dd/mmm/aa, «;» union, NO, relative reference B2→B3, #N/A, CONTARA/CONTAR, segmentación, Imprimir tabla
seleccionada, Anular dinamización, Ancho 1 página / Alto Automático, number-before-text sort, Lista + Detener, Hoja!Celda,
ESLOGICO. No cut was made. Both partial rows are now covered (#1, #2).

After the fix: asked 17; covered 17; partial 0; miss 0 (sin fuente 3 unchanged).

## Form

- Words: 1,580 (`wc -w`), allowed under the rule change. Lines ≤120 except line 1 (the `#` title, unchanged).
- List-shape hygiene: no `-`, `*` or `1.` after sentence punctuation mid-line. Spanish quotes. Voice: terse items, no
  fillers or closers; no invented vocabulary.

## Counts

Checked 8: PASS 8, FAIL 0. Coverage re-check: 15/15 covered rows intact; 2 partial → covered.
