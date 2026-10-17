# Post-close check: WHATWG replacement and 2026-10-17 decisions

Blind pass. No repo file edited. Sources read with `pagetext.py`; exams with `pdftotext -layout`.

| # | item (first words) | field(s) | PASS/FAIL | reason | replacement |
|---|---|---|---|---|---|
| W1 | m06-l08 «World Wide Web y HTML» | inventor; HTML 1990-1995 CERN→IETF | PASS | ISOC: «Tim Berners-Lee (the inventor of the WWW)». WHATWG §1.6: «For its first five years (1990-1995), HTML went through a number of revisions … primarily hosted first at CERN, and then at the IETF». Mosaic/NCSA gone. Note: «primarily» is not rendered; harmless here | optional: «…tuvo varias revisiones, sobre todo primero en el CERN y después en el IETF» |
| W2 | m06-l08 «HTML» (Servicios) | definition; .htm/.html | PASS | §1.3 «HTML is the World Wide Web's core markup language» = «lenguaje de marcado principal»; ms-win-extensiones: «htm, html \| Página de lenguaje de marcado de hipertexto». English expansion correctly cut | — |
| W3 | m06-l08 «JavaScript» (Servicios) | scripts = small programs, script element, client side, browser runs them; interactivity; users disable | PASS | §1.10 «Scripts (typically in JavaScript) are small programs that can be embedded using the script element»; §1.10.2 «the browser will generally run the script uninterrupted»; §1.7.2 «inline client-side scripts» (inline = embedded in the page, so the clause holds, narrowly); §4.12 «add interactivity to their documents», «many users disable scripting». Edge sentence unchanged and supported. Style note: «van del lado del cliente» is loose; «se ejecutan del lado del cliente» is the standard phrasing | optional: «…con el elemento script; se ejecutan del lado del cliente, en el navegador (fuente: …)» |
| W4 | m06-l08 LQMC «Los scripts en JavaScript…» | asked fact; support | PASS | Asked: browser runs JavaScript directly / natively (2024 A 69 key b; 2022 X 70 d; 2020 70 d). Line states it; WHATWG §1.10/§1.10.2 and Edge consola («código de JavaScript en la consola y se ejecuta») support it | — |
| W5 | m06-l08 LQMC «HTML es el lenguaje de marcado principal…» | asked fact; support | PASS | Matches 2020 X 69 («lenguaje de marcado estándar para … páginas web»); §1.3 supports it. Coverage note: 2020 ord. 65 asked the expansion (Lenguaje de Marcado de Hipertexto); no LQMC line states it any more, only the HTML item's ms-win-extensiones sentence does | optional: append «; los archivos .html son páginas de lenguaje de marcado de hipertexto (fuente: `ms-win-extensiones.html`)» |
| W6 | m06-l08 Fuentes block | exactly the cited files, first-citation order | PASS | `fuentes_order.py`: missing [], uncited [], in order True. whatwg-introduccion 2nd, ms-win-extensiones before whatwg-scripting as first cited | — |
| W7 | WHATWG sha256 | fuentes.yaml | PASS | introduccion 7fb8136b…4ada and scripting 6ee86392…6ac7 match `sha256sum`; URLs html.spec.whatwg.org; titles «HTML Standard: 1 Introduction» / «4.12 Scripting»; lessons [m06-l08] | — |
| W8 | no w3c-html401 left | lessons, fuentes.yaml, sources/otros | PASS | No file in sources/otros; `grep -rl w3c-html401 content/age-administrativo-c1` empty. Note: docs/age-theory-ledger.md:2933 still lists both W3C files under «Files resting on superseded or non-UI sources» (stale doc line, not a citation or index entry) | update that ledger line to drop the two W3C files |
| W9 | ms-win-extensiones.html entry | lessons | PASS | `lessons: [m06-l03, m06-l08]` | — |
| W10 | m06-l08 form | words; line length | PASS | `wc -w` 1,471 ≤ 1,500; longest non-title line 120 | — |
| D1 | m06-l02 «Captura de pantalla» | Windows+Impr Pant; two Impr Pant descriptions | PASS | ms-win-atajos (Windows 11 tab): «Tecla Windows + PrtScn \| … guárdela en un archivo en la subcarpeta Capturas de pantalla de la carpeta Imágenes»; «Impr Scn o Impr Pant \| Seleccione una zona de la pantalla para hacer una captura de pantalla en el portapapeles». ms-win-recortes (Windows 11 tab): «Presione Imprimir pantalla (PrtSc) para obtener una instantánea … de toda la pantalla y colóquela en el portapapeles». Both stated, each with its source, neither chosen. (The atajos Windows 10 tab's full-screen PrtScn row is correctly not used) | — |
| D2 | m06-l02 cut: Narrador | remaining text | FAIL | Remaining «lee los elementos de la pantalla; Windows+Ctrl+Entrar…» is supported, but the cut removed the only tie to accessibility. 2024 A 46 (key c) and 2020 50 ask Narrador as an accessibility tool; the lesson no longer says so (Lupa keeps «Accesibilidad», Narrador does not). Source: «si eres invidente o tienes visión reducida. Lee e interactúa con elementos en la pantalla» | «**Narrador**: lee la pantalla si eres invidente o tienes visión reducida; Windows+Ctrl+Entrar lo inicia y lo detiene (fuente: `ms-win-narrador.html`).» (+4 words: offset e.g. drop «(aplicaciones, configuración y archivos)» in Búsqueda) |
| D3 | m06-l02 cut: Cuadros de diálogo | remaining text | PASS | Tab/Mayús+Tab «Avanzar/Retroceder por las opciones», Ctrl+Tab «Avanzar a través de las pestañas», Windows+R «Abrir el cuadro de diálogo Ejecutar». The cut keys were never asked | — |
| D4 | m06-l02 cut: Iconos | remaining text | PASS | «Este equipo», «Papelera de reciclaje», «Red»; «Temas de personalización>» + «Configuración del icono de escritorio». Desktop-icon view sizes never asked | — |
| D5 | m06-l02 Fuentes, ms-win-recortes entry | order; lessons | PASS | `fuentes_order.py`: missing [], uncited [], in order True (recortes after varias-pantallas). fuentes.yaml `lessons: [m06-l02, m06-l03]` | — |
| D6 | m06-l02 form | words; line length | PASS | `wc -w` 1,500 (at the ceiling, so D2's fix needs an offset); longest non-title line 120 | — |
| D7 | course.yaml m06-l04 summary | names only what the lesson says; ≤ 3 sentences | PASS | 3 sentences. Every term found in the lesson; «Estilos de título» matches LQMC «Los estilos de título forman la tabla de contenido» and the Título 1/Título 2 item | — |
| D8 | course.yaml m06-l06 summary | same | PASS | 3 sentences. «Compactar y reparar base de datos», «Dividir la base de datos», objetos, límites and the rest all in the lesson | — |
| D9 | m06-l04 LQMC «Lectura en voz alta está en Revisar; Transcribir…» | asked fact; support | PASS | 2025 A 53 key c: «Se puede transcribir la voz grabando directamente en Word o cargando un archivo de audio». ms-word-transcribir: «Grabar directamente en Word / Cargar un archivo de audio». First half is also asked (2020 ord. 54, Leer en voz alta in Revisar); ms-word-lectura-voz-alta: «Seleccione Revisar>lectura en voz alta» | — |

## Counts

19 checks: 18 PASS, 1 FAIL (D2).

## Notes (not counted)

- W5: the HTML expansion asked in 2020 ord. 65 survives only in the Servicios item, not in «Lo que más cae».
- W8: docs/age-theory-ledger.md:2933 still names the two deleted W3C files; the same section's «Word budget» line
  (1,446–1,498) is also stale now that m06-l02 is at 1,500.
