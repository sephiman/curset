# Verification — `m02-l05`, re-check 1

Verifier: blind verifier (opus), 2026-11-06. Did not write the lesson.

Files read: `docs/age-verification/c2/bloque-ii/pending/m02-l05.md`, `content/age-auxiliar-c2/es/lessons/m02-l05.md`,
`content/age-auxiliar-c2/sources/otros/fuentes.yaml`, and the text (HTML stripped) of `lenovo-perifericos.html`,
`corsair-disipador-termico.html`, `lenovo-flops.html`, `ms-excel-sistemas-numericos.html`,
`python-tutorial-introduccion.html`, `ms-mixed-reality-cad.html`, `ms-azure-ocr.html`, `moodle-open-source.html`,
`ms-win-cuentas-usuario.html`, `ms-win-configuracion-red.html`. All ten new pages: sha256 equal to fuentes.yaml.

Admissibility (Sources, hard rules: a vendor's page only for its own product):
- `lenovo-perifericos.html` (Lenovo México glossary, es-MX), `lenovo-flops.html` (Lenovo Argentina glossary, es-AR) and
  `corsair-disipador-termico.html` (Corsair glossary) state general hardware concepts, not Lenovo or Corsair products:
  not admissible. No saved official page states the heat-sink or FLOPS facts (searched all of `sources/otros/` and the
  INCIBE glossary). `ms-win-configuracion-red.html` (already cited in m02-l06) names peripherals.
- `moodle-open-source.html`: Moodle on its own product, admissible; but the page declares a Spanish version
  (`hreflang="es"` → https://moodle.com/es/acerca-de/open-source/). Fetched to the scratchpad on 2026-11-06 with a browser
  user agent: HTTP 200, `lang="es-ES"`, sha256 56bcbc47d3da3d966fd3e19ddc3793316c91965a4e67f210b6136890fd6c8ed5 (not
  saved to `sources/otros/`). It reads: «Como plataforma de código abierto, el código fuente de Moodle LMS tiene una
  licencia que permite a cualquiera descargar gratuitamente todo el software y personalizar su funcionamiento.»
- `python-tutorial-introduccion.html` (Python Software Foundation on Python), `ms-*` pages: admissible.

Result: 10 PASS, 10 FAIL.

| id | verdict | precept checked | note | replacement |
|---|---|---|---|---|
| `5436f3abf7` | FAIL | lenovo-perifericos.html | text matches the page («Un teclado, mouse, micrófono y cámara web son habituales entre los de entrada. Por su parte, impresoras, altavoces y pantallas son ejemplos de salida»), but a Lenovo glossary on a general concept is not an admissible source. Replace with the official page (the input/output split then needs an official page; otherwise drop it) | - **Periféricos**: la sección «Bluetooth y dispositivos» de Configuración administra los dispositivos conectados al equipo, incluidos periféricos inalámbricos como mouse, teclados, altavoces y auriculares (fuente: `ms-win-configuracion-red.html`). |
| `e2d2f9e706` | FAIL | corsair-disipador-termico.html | text matches the page, but a Corsair glossary on a general concept is not admissible; no saved official page has the fact | drop |
| `733bdf62ea` | FAIL | lenovo-flops.html | text matches the page («FLOPS es una unidad de medida que cuantifica la capacidad de cálculo de una computadora o procesador. Indica cuántas operaciones de punto flotante se pueden realizar en un segundo»), but a Lenovo glossary on a general concept is not admissible; no saved official page has the fact | drop |
| `6ac465f1c7` | PASS | ms-excel-sistemas-numericos.html, table «Sistema numérico / Valor base / Juego de caracteres simbólicos» | Binario 2 «0,1»; Octal 8; Decimal 10; Hexadecimal 16 «0 … 9, A, B, C, D, E, F» | — |
| `5b92844bab` | FAIL | python-tutorial-introduccion.html, 3.1.1 and 3.1.3 | int/float and the examples 5.0, 1.6 match. «(coma flotante)» is not on the page (it says «punto flotante» and never ties the name `float` to it), and the page calls the list the most versatile of the «tipos de datos compuestos», written «como una lista de valores separados por coma (ítems) entre corchetes», not «un valor compuesto» | - **Tipos de datos**: en Python, los números enteros (por ejemplo 2, 4 o 20) tienen tipo `int` y los que tienen parte fraccionaria, como 5.0 o 1.6, tienen tipo `float`; la lista, el más versátil de los tipos de datos compuestos, se escribe como una lista de valores separados por coma (ítems) entre corchetes (fuente: `python-tutorial-introduccion.html`). |
| `385836152b` | PASS | ms-mixed-reality-cad.html, «Crear sus propios modelos 3D» | «CAD (diseño asistido por ordenador)»; «Los programas CAD también le permiten crear modelos 3D» | — |
| `613b8628a4` | PASS | ms-azure-ocr.html | «El reconocimiento óptico de caracteres o OCR también se conoce como reconocimiento de texto o extracción de texto. Las técnicas de OCR basadas en aprendizaje automático permiten extraer texto impreso o manuscrito de imágenes … así como de documentos» | — |
| `a8782c2141` | FAIL | moodle-open-source.html | facts match the English page («open source learning platform», licence «allows anyone to download the entire software for free and customise how it works»), but «sin versión en español» is false: the page links its Spanish version (see above). Save https://moodle.com/es/acerca-de/open-source/ and cite it; until then drop the «sin versión en español» clause | - **Moodle**: Moodle LMS es una plataforma de aprendizaje de código abierto; su licencia permite a cualquiera descargar gratuitamente todo el software y personalizar su funcionamiento (fuente: `moodle-codigo-abierto.html`). [after saving the Spanish page under that name; with the English file the parenthesis is «(fuente: `moodle-open-source.html`; página en inglés)»] |
| `b89f1df25c` | PASS | ms-win-cuentas-usuario.html, «Tiene varias cuentas» | «Windows permite agregar varias cuentas de usuario para usar el mismo dispositivo, lo que permite a cada usuario tener su propia configuración, documentos y aplicaciones» | — |
| `f8b0b98b83` | FAIL | Fuentes line | title literal, but the file is not admissible and goes with `5436f3abf7` | drop |
| `c1d1093121` | FAIL | Fuentes line | as `f8b0b98b83` | drop |
| `254ce17fc9` | FAIL | Fuentes line | title literal («¿Qué es un disipador térmico?»), but the file goes with `e2d2f9e706` | drop |
| `9b617b5621` | FAIL | Fuentes line | as `254ce17fc9` | drop |
| `b91f4c46c9` | FAIL | Fuentes line | title literal, but the file goes with `733bdf62ea` | drop |
| `dda97766ee` | PASS | Fuentes line | title and host match; consultado 06-11-2026 as in fuentes.yaml | — |
| `78b9379f98` | PASS | Fuentes line | page title «3. Una introducción informal a Python»; docs.python.org; 06-11-2026 | — |
| `aa573b5242` | PASS | Fuentes line | «Trabajar con modelos 3D», learn.microsoft.com, 06-11-2026 | — |
| `295d0a0878` | PASS | Fuentes line | «OCR: reconocimiento óptico de caracteres», learn.microsoft.com, 06-11-2026 | — |
| `b1adffa7f7` | PASS | Fuentes line | matches the file as cited now; replace with the Spanish page's line if `a8782c2141` switches file | — |
| `eadb52a926` | PASS | Fuentes line | «Administrar cuentas de usuario en Windows», support.microsoft.com, 06-11-2026 | — |

Whole «Fuentes» section: lists exactly the files the lesson cites (checked by diff). After the drops above, remove the
three Lenovo/Corsair lines and, if `5436f3abf7` takes the replacement, add `ms-win-configuracion-red.html` (Microsoft,
«Comprender y explorar la configuración de Windows», support.microsoft.com, consultado el 06-11-2026).
