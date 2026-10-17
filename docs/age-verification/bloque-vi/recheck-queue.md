# Edits applied after a tema's last blind pass (to be re-checked blind)

(VI.1 edits re-checked in VI.2 verify-pass1: both PASS.)

- m06-l02 «Acoplar»: «arrastra una ventana al borde izquierdo o derecho para acoplarla a ese lado, o a una esquina para que ocupe un cuarto» (ms-win-acoplar.html).
- m06-l02 «Cambiar de ventana»: parenthetical removed (word budget); now «Alt+Tab; Windows+Tab abre la Vista de tareas» (ms-win-atajos.html).
- m06-l02 «Varios escritorios»: «Vista de tareas › Nuevo escritorio» now cited to ms-win-escritorios.html; Windows+Ctrl+D to ms-win-atajos.html.
- m06-l02 LQMC line 1 («centrado de forma predeterminada»): second source ms-win-barra-tareas.html added.

(m06-l02 edits re-checked in VI.3 verify-pass1: 4 PASS.)

- m06-l03 «Buscar en Windows»: path now as printed «Configuración › Privacidad & seguridad › Buscar en Windows» (ms-win-indexacion.html).
- m06-l03 «Recortes»: Impr Pant clause dropped.
- m06-l03 LQMC line «Ver»: «"Ver" muestra iconos, listas y detalles; los diseños de iconos van de extra grandes a pequeños» (ms-win-explorador.html, ms-win-explorador-lector.html); LQMC lines reordered (most repeated families first).
- m06-l03 glossary: g-registro-de-windows replaced by g-editor-del-registro (ms-win-herramientas-sistema.html).

(m06-l03 edits re-checked in VI.4 verify-pass1: 4 PASS.)

- m06-l04 «Macros»: tab and button dropped; «el menú Macros tiene «Ver macros» y «Detener grabación»; guardada en Normal.dotm sirve en todos los documentos» (ms-word-macros.html).
- m06-l04 «Historial de versiones»: path now «… › Historial de versiones › Abrir versión › Restaurar» (ms-office-autoguardado.html).
- m06-l04 «Delimitador de objeto»: «ancla» → «anclaje» (the page's noun; ms-word-ajustar-imagenes.html).
- m06-l04 summary: «barra de herramientas de acceso rápido» (coordinator writes it into course.yaml).

(m06-l04 edits re-checked in VI.5 verify-pass1: 4 PASS.)

- m06-l05 «Fechas»: «por defecto, el 1-1-1900 es el 1» (ms-excel-funcion-dia.html).
- m06-l05 «Rangos no adyacentes»: added «el punto y coma (;) es el operador de unión: C2:C7;E2:E7» (ms-excel-referencias-estructuradas.html).
- m06-l05 cuts for words: «Ctrl+Av Pág y Ctrl+Re Pág cambian de hoja» and «con contraseña o sin ella» removed (check nothing left unsupported).
- m06-l05 LQMC: CONTARA/CONTAR line moved to the top; Fuentes reordered by first citation.
- m06-l05 summary: «…BUSCARV y el error #N/A» and «…Power Query, Validación de datos, Imprimir y la cinta» replace «los valores de error» and «impresión» (coordinator writes it into course.yaml).

(m06-l05 edits re-checked in VI.6 verify-pass1: 5 PASS.)

- m06-l06 «Compactar y reparar»: «Se ejecuta con la base abierta o sin abrirla; sin abrirla, desde «Herramientas de base de datos»» (ms-access-compactar.html).
- m06-l06 «Gráfico moderno» (singular, as printed; ms-access-graficos.html).
- m06-l06 «Agrupación, orden y total»: «panel que se abre desde «Diseño de informe › Agrupación y totales»» (ms-access-informes.html).
- m06-l06 «Importar o vincular»: «Datos externos › Importar & vínculo › Nuevo origen de datos › Desde archivo › Excel» (ms-access-importar-excel.html).
- m06-l06 LQMC: «La regla de validación limita los valores que se pueden escribir en un campo» (ms-access-reglas-validacion.html).

(m06-l06 edits re-checked in VI.7 verify-pass1: 5 PASS.)

- m06-l07 «Acceso delegado»: «exige cuenta profesional o educativa en Microsoft 365 o con Exchange Online» (ms-outlook-delegados.html).
- m06-l07 «Búsqueda»: «en Outlook clásico, Ctrl+E o F3 busca y Ctrl+Mayús+P crea una carpeta de búsqueda» (ms-outlook-atajos.html).
- m06-l07 «Responder y Reenviar»: «Reenviar admite destinatarios nuevos e incluye los datos adjuntos» (ms-outlook-responder-reenviar.html).
- m06-l07 Fuentes line and fragment title of ms-outlook-recuperar.html: «requisitos, limitaciones & pasos» (as printed).

(m06-l07 edits re-checked in VI.8 verify-pass1: 4 PASS.)

- m06-l08 «JavaScript»: «se ejecuta en el equipo del cliente al cargar el documento o con un evento, como activar un enlace» (w3c-html401-scripts.html).
- m06-l08 LQMC reordered by family size (Navegación, Lenguajes, Red, HTTP/HTTPS, Diseño adaptable).
- course.yaml: the eight m06 lesson summaries (VI.4 with «barra de herramientas de acceso rápido»; VI.5 with «…BUSCARV y el error #N/A» and «…Power Query, Validación de datos, Imprimir y la cinta»; VI.8 with «En el navegador (Microsoft Edge)») and the m06 module summary (new, coordinator's wording).
- glossary.yaml: link_except added — g-plantilla in m01-l10 («plantilla de personal»); g-informacion-general in m06-l05 (a Fuentes title); g-acceso-directo in m06-l04 (keyboard access keys of the ribbon); g-acceso-rapido in m06-l02 (a definition sentence) and m06-l04/m06-l05 (Barra de herramientas de acceso rápido). Kept links: content/age-administrativo-c1/glossary-links.es.txt, m06 lines.

## WHATWG replacement (m06-l08)

The two HTML 4.01 pages (`w3c-html401-introduccion.html`, `w3c-html401-scripts.html`) are deleted and replaced by the
HTML Standard: `whatwg-html-introduccion.html` (https://html.spec.whatwg.org/multipage/introduction.html, «1
Introduction») and `whatwg-html-scripting.html` (https://html.spec.whatwg.org/multipage/scripting.html, «4.12
Scripting»). Read with `python3 -I SP/tools/pagetext.py FILE REGEX`. The HTML item also cites the already-saved
`ms-win-extensiones.html` (added `m06-l08` to its `lessons`).

1. Item «World Wide Web y HTML» (Origen).
   - Old: «Tim Berners-Lee desarrolló HTML en el CERN; lo popularizó el navegador Mosaic, del NCSA, y creció con la Web
     en los años noventa (fuente: `w3c-html401-introduccion.html`).»
   - New: «Tim Berners-Lee inventó la World Wide Web (fuente: `isoc-historia-internet.html`). En sus cinco primeros
     años (1990-1995), HTML tuvo varias revisiones, primero en el CERN y después en el IETF (fuente:
     `whatwg-html-introduccion.html`).»
   - Support: ISOC: «Tim Berners-Lee (the inventor of the WWW)». WHATWG §1.6 History: «For its first five years
     (1990-1995), HTML went through a number of revisions and experienced a number of extensions, primarily hosted
     first at CERN, and then at the IETF.» Mosaic/NCSA cut: neither saved source names them.
2. Item «HTML» (Servicios).
   - Old: «**HTML** (*HyperText Markup Language*, lenguaje de marcado de hipertexto): lenguaje de publicación de la
     World Wide Web (fuente: `w3c-html401-introduccion.html`).»
   - New: «**HTML**: lenguaje de marcado principal de la World Wide Web (fuente: `whatwg-html-introduccion.html`). Los
     archivos .htm y .html son páginas de lenguaje de marcado de hipertexto (fuente: `ms-win-extensiones.html`).»
   - Support: WHATWG §1.3 Background: «HTML is the World Wide Web's core markup language.» ms-win-extensiones table:
     «htm, html | Página de lenguaje de marcado de hipertexto». The English expansion is cut (not in either page).
3. Item «JavaScript» (Servicios), first two sentences; the Edge sentence is unchanged.
   - Old: «lenguaje de script del lado del cliente: el programa va con el documento HTML y se ejecuta en el equipo del
     cliente al cargar el documento o con un evento, como activar un enlace (fuente: `w3c-html401-scripts.html`).»
   - New: «los scripts, normalmente en JavaScript, son pequeños programas que se insertan en la página con el elemento
     script; van del lado del cliente y los ejecuta el navegador (fuente: `whatwg-html-introduccion.html`). Dan
     interactividad al documento, y muchos usuarios los desactivan (fuente: `whatwg-html-scripting.html`).»
   - Support: WHATWG §1.10: «This DOM tree can be manipulated from scripts in the page. Scripts (typically in
     JavaScript) are small programs that can be embedded using the script element or using event handler content
     attributes.» §1.10.2: «the browser will generally run the script uninterrupted before doing anything else».
     §1.7.2: «Authors can include data for inline client-side scripts or server-side site-wide scripts» (the only
     literal «client-side»; check it is enough for «del lado del cliente», else drop that clause). Scripting §4.12:
     «Scripts allow authors to add interactivity to their documents.» … «many users disable scripting.»
4. «Lo que más cae», JavaScript line.
   - Old: «JavaScript es un lenguaje de script que se ejecuta en el equipo del cliente, en el navegador (fuente:
     `w3c-html401-scripts.html`, `ms-edge-consola-javascript.html`).»
   - New: «Los scripts en JavaScript los ejecuta el navegador, del lado del cliente (fuente:
     `whatwg-html-introduccion.html`, `ms-edge-consola-javascript.html`).»
   - Support: as in 3 (§1.10, §1.10.2, §1.7.2); Edge: «Puede escribir cualquier … código de JavaScript en la consola y
     se ejecuta». Exams: 2024 ord. 69, 2022 extr. 70, 2020 ord. 70.
5. «Lo que más cae», HTML line.
   - Old: «HTML es el lenguaje de marcado de hipertexto con el que se publica la Web (fuente:
     `w3c-html401-introduccion.html`).»
   - New: «HTML es el lenguaje de marcado principal de la World Wide Web (fuente: `whatwg-html-introduccion.html`).»
   - Support: §1.3 «HTML is the World Wide Web's core markup language.» Exams: 2020 ord. 65, 2020 extr. 69.
6. Fuentes: the two W3C lines replaced by `whatwg-html-introduccion.html` (2nd) and `whatwg-html-scripting.html`;
   `ms-win-extensiones.html` added; order by first citation checked with `fuentes_order.py` (in order: True).
   fuentes.yaml: W3C entries replaced, sha256 7fb8136b… (introduccion), 6ee86392… (scripting). Word count 1,471.

## Decisions of 2026-10-17 (after the bloque VI close)

- m06-l02 «Captura de pantalla»: «Windows+Impr Pant guarda la pantalla completa en Imágenes › Capturas de pantalla (fuente: ms-win-atajos.html). Las páginas de Microsoft describen Impr Pant de dos formas: deja seleccionar una zona y la copia al portapapeles (fuente: ms-win-atajos.html); copia la pantalla completa al portapapeles (fuente: ms-win-recortes.html).» Fuentes block gains ms-win-recortes.html.
- m06-l02 cuts for words (check nothing left unsupported or misleading): Narrador «para personas invidentes o con visión reducida» removed; Cuadros de diálogo «Barra espaciadora marca una casilla; Esc descarta el cuadro» removed; Iconos «Clic derecho en el escritorio › Ver: tamaño grande, mediano o pequeño y Mostrar iconos del escritorio» removed.
- course.yaml m06-l04 summary: «Estilos de título, tabla de contenido, índice, notas, …» (was «Estilos, …»).
- course.yaml m06-l06 summary: «objetos, límites, Compactar y reparar base de datos y Dividir la base de datos» (was «Compactar y reparar y dividir la base de datos»).
- m06-l04 LQMC: «Lectura en voz alta está en Revisar; Transcribir graba en Word o carga un audio» (ms-word-lectura-voz-alta.html, ms-word-transcribir.html); asked fact of 2025 A 53 (key c).

## After the post-close check (2026-10-17)

- m06-l02 «Narrador»: «lee la pantalla si eres invidente o tienes visión reducida; Windows+Ctrl+Entrar lo inicia y lo detiene» (ms-win-narrador.html) — the post-close checker's wording (D2).
- m06-l02 Búsqueda item: «(aplicaciones, configuración y archivos)» removed to stay at 1,500 words.
