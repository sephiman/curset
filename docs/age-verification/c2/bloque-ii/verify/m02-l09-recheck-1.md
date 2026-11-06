# Verification — `m02-l09`, re-check 1

Verifier: blind verifier (opus), 2026-11-06. Did not write the lesson.

Files read: `docs/age-verification/c2/bloque-ii/pending/m02-l09.md`, `content/age-auxiliar-c2/es/lessons/m02-l09.md`, and in
`content/age-auxiliar-c2/sources/otros/` (HTML stripped to text; raw HTML split at the `data-tab` offsets where a page has
Windows and Web tabs): `ms-office-recuperar-version.html`, `ms-excel-porcentaje.html`, `ms-excel-formato-fecha.html`
(Windows tab), `ms-excel-formato-condicional.html` (Windows tab, offsets 55685–154431, and Web tab),
`ms-excel-funcion-regexprueba.html`.

Result: 6 PASS, 1 FAIL.

| id | verdict | precept checked | note | replacement |
|---|---|---|---|---|
| `d4fb1066c7` | PASS | ms-office-recuperar-version.html; «Si no ha guardado el archivo» | page: «Vaya a Información del archivo>, Administrar documentos>>, Recuperar libros no guardados en Excel»; «Seleccione el archivo y… haga clic en Abrir»; «seleccione Guardar como»; the labels are the page's, including «Administrar documentos» | — |
| `3ad58ff27f` | PASS | ms-excel-porcentaje.html | «Excel multiplica esos números por 100… si una celda contiene el número 10… se verá 1000,00% después de aplicar el formato de porcentaje» | — |
| `e64e513c95` | PASS | ms-excel-porcentaje.html | «si desea ver 10% en vez de 10,00%, escriba 0 en el cuadro de diálogo Posiciones decimales» | — |
| `d949d2fb18` | PASS | ms-excel-formato-fecha.html; Windows tab | «Es probable que la celda no sea lo suficientemente ancha como para mostrar el número completo. Trate de hacer doble clic en el borde derecho de la columna…»; the same text for «Si una celda se muestra ##### después de aplicarle formato de fecha» | — |
| `2626d3e58c` | FAIL | ms-excel-formato-condicional.html; Windows tab | path and data-bar sentence right («En la pestaña Inicio, en el grupo Estilos… Formato condicional»; «La longitud de la barra de datos representa el valor de la celda»). The menu labels do not match the Windows tab: it reads «haga clic en Barras de datos» and «haga clic en Conjunto de iconos» (singular), and gives no menu label for color scales. «Escalas de color» and «Conjuntos de iconos» appear as labels only in the Web tab. The Windows tab names the three types in lower case: «barras de datos, conjuntos de iconos y escalas de colores» | **Formato condicional**: «Inicio › Estilos › Formato condicional» aplica, entre otros, barras de datos, escalas de colores y conjuntos de iconos; la longitud de la barra de datos representa el valor de la celda (fuente: `ms-excel-formato-condicional.html`). |
| `460169dacd` | PASS | ms-excel-porcentaje.html | multiplication by 100 and «10% en vez de 10,00%» with 0 decimal places, as above | — |
| `37324152cb` | PASS | ms-excel-funcion-regexprueba.html | «permite comprobar si alguna parte del texto suministrado coincide con una expresión regular… Se devolverá VERDADERO si hay una coincidencia y FALSO si no la hay»; «La función REGEXPRUEBA determina si alguna parte del texto coincide con el patrón» | — |
