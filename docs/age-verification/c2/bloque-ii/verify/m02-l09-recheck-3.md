# Verification — `m02-l09`, re-check 3 (blind)

Verifier: blind, 2026-11-06. Did not write the lesson; checked against the saved pages in `content/age-auxiliar-c2/sources/otros/` (HTML stripped to text; Windows desktop sections, located by the pages' `data-tab` panels). Input: `docs/age-verification/c2/bloque-ii/pending/m02-l09.md` (18 items), lesson
`content/age-auxiliar-c2/es/lessons/m02-l09.md`. Pages read: `ms-excel-numeros-redondeados.html`, `ms-excel-rellenar-datos.html`,
`ms-excel-error-almohadillas.html`, `ms-excel-prioridad-operadores.html`, `ms-excel-si-anidadas.html`,
`ms-excel-funcion-dias.html`, `ms-excel-funcion-diasem.html`, `ms-excel-funcion-truncar.html`, `ms-excel-funciones-categoria.html`.

New pages (`descarga nueva`, 2026-11-06): the sha256 of each of the eight files matches `writer/m02-l09-fix-fuentes.yaml`
and `sources/otros/fuentes.yaml`; each has `lang="es-ES"`, a canonical URL equal to the recorded one, and the Spanish
article title recorded. `ms-excel-funciones-categoria.html` is an earlier copy; its sha256 matches `fuentes.yaml`.
Arguments written with «;» follow the course convention (exam style §12 item 20); the pages print «,».

| id | verdict | precept checked | note | replacement |
|---|---|---|---|---|
| `720b704e97` | PASS | ms-excel-numeros-redondeados.html | «cuando el formato se establece para mostrar un número menor de posiciones decimales que el que contiene el número real»; «el número completo sigue siendo visible en la barra de fórmulas» | — |
| `fdb6daec2a` | PASS | ms-excel-rellenar-datos.html | «Para una serie como "1, 2, 3, 4, 5…", escriba 1 y 2 en las primeras dos celdas»; «Para la serie "2, 2, 2, 2…", escriba 2 solo en la primera celda»; «Arrastre el controlador de relleno» | — |
| `3f6460a0d4` | PASS | ms-excel-error-almohadillas.html | «Las fórmulas que devuelven fechas y horas como valores negativos también pueden mostrarse como #####» | — |
| `6c6719dac1` | PASS | ms-excel-error-almohadillas.html; «Corregir horas o fechas negativas» | «Use una fórmula para restar fechas, o sumar o restar tiempo correctamente para evitar resultados negativos»; «Cambie los resultados negativos de la fórmula … a otro formato de número». The page's third point (positive values under the 1900 date system) is not stated; the sentence does not present its list as complete | — |
| `b0659f42ca` | PASS | ms-excel-prioridad-operadores.html | «Si una fórmula contiene operadores con la misma prioridad (por ejemplo … multiplicación y otro de división), Excel evaluará los operadores de izquierda a derecha»; =5+2*3 → 11; =(5+2)*3 → 21 | — |
| `5f7ca35aa0` | PASS | ms-excel-si-anidadas.html | the formula is on the page with «,» (=SI(D2>89,"A",SI(D2>79,"B",…))); «;» per §12 item 20 | — |
| `4383340f4d` | PASS | ms-excel-funcion-dias.html | syntax DIAS(fecha_final, fecha_inicial); «DIAS usa FechaFinal – FechaInicial»; data 31 DE DICIEMBRE DE 2021 (A2), 1 DE ENERO DE 2021 (A3); =DIAS(A2,A3) → 364 | — |
| `3a9bcd0fce` | PASS | ms-excel-funcion-diasem.html | DIASEM(núm_de_serie,[tipo]); tipo table: «1 u omitido» 1 (domingo)–7 (sábado), 2: 1 (lunes)–7 (domingo), 3: 0 (lunes)–6 (domingo) | — |
| `de917bcc5d` | PASS | ms-excel-funcion-truncar.html | «TRUNCAR(número; [núm_decimales])»; «Opcional. Es un número que especifica la precisión del truncamiento. El valor predeterminado del argumento núm_decimales es 0» | — |
| `849057270b` | PASS | ms-excel-funciones-categoria.html; Funciones financieras | RENDTO «Devuelve el rendimiento de un valor bursátil que paga intereses periódicos»; CUPON.DIAS.L1 and CUPON.DIAS.L2 listed; entry printed «COUPDACUPON.DIAS» with «el número de días del período (entre dos cupones) donde se encuentra la fecha de liquidación» | — |
| `865cf13876` | PASS | Fuentes | title and date match the saved page; cited in the prose | — |
| `44415fb5b9` | PASS | Fuentes | title and date match the saved page; cited in the prose | — |
| `137c57676a` | PASS | Fuentes | title and date match the saved page; cited in the prose | — |
| `53a1d6f5eb` | PASS | Fuentes | title and date match the saved page; cited in the prose | — |
| `79c21c92e5` | PASS | Fuentes | title and date match the saved page; cited in the prose | — |
| `243435c7ca` | PASS | Fuentes | title and date match the saved page; cited in the prose | — |
| `86b91f80a1` | PASS | Fuentes | title and date match the saved page; cited in the prose | — |
| `d40af354ef` | PASS | Fuentes | title and date match the saved page; cited in the prose | — |

PASS 18, FAIL 0.

«Fuentes» section: 40 files cited in the prose, 40 listed, the same set.
