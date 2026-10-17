# Coverage fix — m06-l05 (writer, 2026-10-17)

Lesson: `content/age-administrativo-c1/es/lessons/m06-l05.md`. Applies the rule change (requirements v1.5, no word
ceiling): nothing cut. Words (`wc -w`): 1498 before, **1580** after. Lines ≤ 120 (only the `#` title line is longer,
unchanged). Fuentes reordered with `fuentes_order.py` (in order, none missing or uncited).

## Changes

### 1. 2024 X 63 — DIVIDIRTEXTO spills the parts into adjacent cells

Old (Texto y fecha): «… DIVIDIRTEXTO divide el texto por delimitadores (fuente: `ms-excel-funciones-categoria.html`).
DIA da el día …»
New: «… DIVIDIRTEXTO divide el texto por delimitadores (fuente: `ms-excel-funciones-categoria.html`). DIVIDIRTEXTO
desborda el texto entre columnas o hacia abajo por filas (fuente: `ms-excel-funcion-dividirtexto.html`). […] DIA da el
día …»

Source `ms-excel-funcion-dividirtexto.html` (new): «La función DIVIDIRTEXTO funciona igual que el asistente de texto a
columnas, pero en formato de fórmula. Permite dividir entre columnas o hacia abajo por filas.» / «col_delimiter El texto
que marca el punto donde se va desbordar el texto entre columnas. / row_delimiter El texto que marca el punto donde se
va desbordar el texto hacia las filas inferiores.» The page does not say «celdas contiguas»; the lesson says «desborda
entre columnas», as printed.

### 2. 2022 54 — #¿NOMBRE? when Excel does not recognise a name

New item after #N/A:
`- **#¿NOMBRE?**: sale por un error ortográfico en el nombre de la fórmula, un nombre no definido o un texto sin`
`  comillas dobles (fuente: `ms-excel-error-nombre.html`).`

Source `ms-excel-error-nombre.html` (new, title «Cómo corregir un error #¿NOMBRE?»): «La principal razón por la que el
#NAME? aparece en la fórmula es que hay un error ortográfico en el nombre de la fórmula.» / «Cuando la fórmula tiene una
referencia a un nombre no definido en Excel, ¿ve la #NAME? error.» / «Si la sintaxis omite las comillas dobles "" para un
valor de texto, verá el #NAME error.» The body prints «#NAME?» (untranslated); the Spanish label «#¿NOMBRE?» is in the
page title, in «la fórmula de ÍNDICE genera el error ¿#NOMBRE?», and on `ms-excel-funcion-sierror.html`. The page does
not name SIERROR; the lesson does not either (the key is disputed).

## Restored (earlier cut, asked by an exam)

| Restored | Exam row | Text and source |
|---|---|---|
| EXTRAE syntax (the «MID (función)» page, cut in R2) | 2020 ord. 60 (EXTRAE(A1;12;2) → 01) | «EXTRAE(texto; posición_inicial; núm_de_caracteres): el primer carácter del texto es la posición 1 (fuente: `ms-excel-funcion-extrae.html`).» Page: «EXTRAE(texto, posición_inicial, núm_de_caracteres)» / «posición_inicial para el primer carácter de texto es 1, y así sucesivamente.» Separator «;» per the lesson's intro and the page's own examples («=EXTRAE(A2;1;5)»). |

Checked and not restored: the other function pages cut in R2 (MAX, BUSCARV, FORMULATEXTO, FILAS, DIA) — the asked fact
is already stated from `ms-excel-funciones-categoria.html` / `ms-excel-funcion-dia.html`; MAX's asked fact (the «,»
separator, 2022 X 60) is on the «Sin fuente oficial» list. 1900/1904 dates, referencia 3D, Ctrl+Av Pág/Re Pág, «con
contraseña o sin ella» and the other within-item cuts: no index row asks them. The «20-2» date row (2024 A 60) stays
out (sin fuente oficial).

## Cuts

None. (A first draft of this fix cut six clauses for the 1,500 ceiling; all undone under the rule change.)

Re-checked: every covered row of `m06-l05.md` (coverage report) still has its quoted text in the lesson.

## New sources (for `fuentes.yaml`; not edited)

```yaml
- file: ms-excel-funcion-dividirtexto.html
  url: "https://support.microsoft.com/es-es/excel/functions/textsplit-function"
  title: "Microsoft, «Función TEXTSPLIT»"
  consultado: "2026-10-17"
  sha256: 2f5061bea91748aa85c2b200ca3223553a76516dd71c4f3cd99150f4f072aaf4
  lessons: [m06-l05]
- file: ms-excel-error-nombre.html
  url: "https://support.microsoft.com/es-es/excel/how-to-correct-a-name-error"
  title: "Microsoft, «Cómo corregir un error #¿NOMBRE?»"
  consultado: "2026-10-17"
  sha256: c4ac8cd988905e88866743e1569c56e7817731c48f70a46df3225a7d59788ec0
  lessons: [m06-l05]
- file: ms-excel-funcion-extrae.html
  url: "https://support.microsoft.com/es-es/excel/functions/mid-function"
  title: "Microsoft, «MID (función)»"
  consultado: "2026-10-17"
  sha256: a992485b4cae69ccd697797aa42920b1dd55cd5669f4716e079b777d65eccb61
  lessons: [m06-l05]
```

The DIVIDIRTEXTO and EXTRAE pages are Spanish (`lang="es-ES"`) but their `<title>` prints the English names «Función
TEXTSPLIT» and «MID (función)»; the bodies use DIVIDIRTEXTO and EXTRAE. Cited with the titles as printed.

Sin fuente oficial: none new.
