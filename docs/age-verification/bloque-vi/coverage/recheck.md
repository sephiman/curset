# Coverage fixes — blind re-check of `recheck-queue.md` (2026-10-17)

Checked against the saved pages in `content/age-administrativo-c1/sources/otros/` with `pagetext.py`; form with
`fuentes_order.py`, a character count of every line after line 1, and the «never does» list of `docs/prose-voice.md`.

## Edits

| # | Lesson | Edit | PASS/FAIL | Reason | Replacement |
|---|---|---|---|---|---|
| 1 | m06-l07 | Grupos: «Cualquier persona de la organización puede iniciar una conversación de grupo. En Outlook clásico, todos los miembros reciben el correo enviado al grupo.» | PASS | `ms-outlook-grupo-enviar.html`, general list: «Cualquier persona de su organización puede iniciar una conversación de grupo.» Classic tab only («Enviar un correo electrónico a un grupo en Outlook clásico»): «Todos los miembros del grupo recibirán el correo electrónico.» Client named as the page scopes it. Public/private sentence also literal | — |
| 2 | m06-l07 | **Gráficos** (Outlook clásico) | PASS | «Insertar», grupo «Ilustraciones», «Gráfico», «En la hoja de cálculo de Excel que aparece, escriba los datos» literal. The page does not print «Outlook clásico»; it scopes itself by «Se aplica a: Outlook para Microsoft 365 Outlook 2024 Outlook 2021» and «Outlook para PC», with no new Outlook, so the label matches the page's scope (lesson line 3 defines the two clients) | — |
| 3 | m06-l07 | **Limpiar** (Outlook clásico) | PASS | «(Cinta clásica) En la pestaña Inicio, en el grupo Eliminar, seleccione Limpiar»; the three options, «mensajes redundantes», default «Elementos eliminados» literal. «Se aplica a» has no new Outlook; same scoping as #2 | — |
| 4 | m06-l07 | **Correo no deseado** (Outlook clásico) | PASS | Path «Inicio › Eliminar › Bloquear › Opciones de correo electrónico no deseado», default «Sin filtrado automático», «Solo listas seguras … la opción más restrictiva» literal; the page names the client itself («… en Outlook clásico») and «Se aplica a» has no new Outlook | — |
| 5 | m06-l07 | Búsqueda and Grupos re-wrapped | PASS | Word diff shows no word change in the re-wrap beyond the content edits already listed; lines ≤ 120 | — |
| 6 | m06-l03 | Summary: «con la directiva «No mover archivos eliminados a la papelera de reciclaje» habilitada, lo que eliminas en el Explorador tampoco va a la Papelera» | PASS (content) | `ms-win-directivas-explorador.html`, NoRecycleFiles, nombre descriptivo «No mover archivos eliminados a la papelera de reciclaje»: «Si habilita esta configuración, los archivos y carpetas que se eliminan mediante Explorador de archivos no se colocarán en la Papelera de reciclaje». Scoped to Explorer and to «habilitada» as the page is. See form row F1 for the wrap | — |
| 7 | m06-l03 | Asistencia rápida: «Usa una conexión remota: quien ayuda comparte un código de 6 dígitos y, si la otra persona lo permite, ve su pantalla o controla su equipo; el control total se pide con «Solicitar control»» | PASS | `ms-win-asistencia-rapida.html`: «Asistencia rápida utiliza una conexión remota … pueden ver la pantalla del equipo o controlar el equipo (si lo permites)»; «Selecciona Ayudar a alguien y comparte el código de 6 dígitos»; «Si quieres solicitar el control total del equipo, selecciona Solicitar control»; Ctrl + logo de Windows + Q. Person is now consistent (the helper is the subject throughout) | — |
| 8 | m06-l04 | QAT: «Las páginas de Microsoft dan dos ubicaciones predeterminadas: encima de la cinta, en la barra de título (…`ms-office-barra-acceso-rapido.html`), y oculta debajo de la cinta (…`ms-office-barra-acceso-rapido-teclado.html`).» | PASS | First page: «Encima de la cinta de opciones, en la barra de título (ubicación predeterminada)». Keyboard page: «De forma predeterminada, la barra de herramientas está oculta debajo de la cinta de opciones» and «debajo de la cinta (la ubicación predeterminada)». Each side cited to its page; the conflict is stated, as in the m06-l02 Impr Pant item | — |
| 9 | m06-l06 | Campo calculado: «La expresión va precedida del nombre que quieres para el campo de salida, seguido de dos puntos» (`ms-access-consulta-seleccion.html`); old «lo que va delante de los dos puntos es el nombre del campo» gone | PASS | Section «Usar una expresión como campo de salida»: «Anteponga la expresión con el nombre que desea utilizar en la expresión de salida, seguido de dos puntos.» Old clause absent from the lesson. «fila Campo» and the Subtotal example stay literal on `ms-access-consultas.html` | — |
| 10 | m06-l06 | Control calculado: «En la vista Diseño de un formulario, el origen de control de un cuadro de texto se edita en el propio cuadro, sin la hoja de propiedades» | PASS | `ms-access-formularios.html`, under form Design view: «Editar orígenes de control de cuadro de texto en los propios cuadros de texto, sin usar la hoja de propiedades.» Now scoped to forms, as the page is | — |

## New page

| File | sha256 (file = queue) | Official, Spanish | PASS/FAIL |
|---|---|---|---|
| `ms-access-consulta-seleccion.html` | `b766e20dc658d9f32f5b83687a61aaccc63d2c0ea186caa67a9d5237f5892467` — matches | `<html lang="es-ES">`, canonical `https://support.microsoft.com/es-es/access/create-a-simple-select-query`, title «Crear una consulta de selección sencilla \| Microsoft Support», «Se aplica a: Access para Microsoft 365 … Access 2016»; Fuentes line «Microsoft, «Crear una consulta de selección sencilla» (support.microsoft.com, consultado el 17-10-2026)» | PASS |

The sha256 differs from the verifier's scratch download (`14a9c039…`): the page was re-saved, as the verifier asked
(«re-hash after saving»). Its fuentes.yaml entry is for the coordinator to merge; it is not in the lesson folder's
`fuentes.yaml` check here.

## Form

| # | Lesson | Check | PASS/FAIL | Note | Replacement |
|---|---|---|---|---|---|
| F1 | m06-l03 | List-shape hygiene, lines 122–125 | FAIL (minor) | The summary item breaks «(fuente:» alone on line 124 and puts the file on line 125, although «(fuente: `ms-win-directivas-explorador.html`).» fits on one line | Join lines 124–125: `  (fuente: \`ms-win-directivas-explorador.html\`).` |
| F2 | m06-l03 | Fuentes complete and in order | PASS | missing [], uncited [], in order | — |
| F3 | m06-l04 | Fuentes complete and in order | PASS | missing [], uncited [], in order | — |
| F4 | m06-l06 | Fuentes complete and in order | PASS | `ms-access-consulta-seleccion.html` after `ms-access-expresiones.html`, before `ms-access-funcion-ano.html`; missing [], uncited [], in order | — |
| F5 | m06-l07 | Fuentes complete and in order | PASS | missing [], uncited [], in order | — |
| F6 | all four | Lines ≤ 120 except line 1 | PASS | Longest: l03 120, l04 120, l06 119, l07 120 | — |
| F7 | all four | Voice («never does») | PASS | No fillers, triads, rhetorical questions («?» only in quoted page titles and the Access parameter example), «no solo… sino», closers or stacked hedges in the edited items; «tú» throughout | — |

## Counts

17 checks: 16 PASS, 1 FAIL (F1, a wrap in the m06-l03 summary; content of every queued edit passes).
