# Closing check — R2 bloque VI (m06-l01…m06-l08), blind

Reviewer did not write any of it. No repo file edited. Sources read with `pagetext.py` (HTML) and `pdftotext`
(INCIBE glossary PDF). Family counts from `docs/age-ofimatica-index.md` § Recurring feature families.

## Part 1 — recheck-queue items after the last «(… re-checked …)» line

| # | item | PASS/FAIL | reason | replacement |
|---|---|---|---|---|
| 1 | m06-l08 «JavaScript»: «se ejecuta en el equipo del cliente al cargar el documento o con un evento, como activar un enlace» | PASS | `w3c-html401-scripts.html` §18.1: «The program executes on the client's machine when the document loads, or at some other time such as when a link is activated»; «Scripts may be triggered by events». The rest of the item (Consola, Ctrl+Mayús+J) is also printed in `ms-edge-consola-javascript.html`. | — |
| 2 | m06-l08 LQMC order (Navegación, Lenguajes, Red, HTTP/HTTPS, Diseño adaptable) | PASS | Index: Navegación y servicios web 3 conv./6 q.; Lenguajes web 3/5; Red 3/5; Diseño web adaptable 2/2; HTTP y HTTPS 2/2. LQMC lines 1–3 Navegación (Web 4.0, spam, cookies de sesión), 4–5 Lenguajes, 6–8 Red, 9 HTTP/HTTPS, 10 Diseño adaptable: non-increasing. Lenguajes/Red and HTTP/Diseño are ties, so either order is correct. | — |
| 3 | course.yaml: eight m06 lesson summaries and the m06 module summary | PASS | The three named strings are in place (VI.4 «barra de herramientas de acceso rápido»; VI.5 «…BUSCARV y el error #N/A» and «…Power Query, Validación de datos, Imprimir y la cinta»; VI.8 «En el navegador (Microsoft Edge)»). Support check of each sentence is in Part 2. | — |
| 4 | link_except g-plantilla in m01-l10 | PASS | m01-l10:146 «aprobación de la plantilla de personal»: staff establishment, not a document template. | — |
| 5 | link_except g-informacion-general in m06-l05 | PASS | The only occurrence is the Fuentes title «Información general sobre fórmulas en Excel» (overview), not the RD 208/1996 sense. | — |
| 6 | link_except g-acceso-directo in m06-l04 | PASS | m06-l04:8 «los accesos directos de la cinta, llamados Sugerencias de teclas»: keyboard access keys, not a shortcut file. | — |
| 7 | link_except g-acceso-rapido in m06-l02 | PASS | m06-l02:43 and :114 «da acceso rápido a una aplicación…»: generic phrase in the shortcut definition, not the Explorer section. | — |
| 8 | link_except g-acceso-rapido in m06-l04 | PASS | Only inside «Barra de herramientas de acceso rápido» (lines 81, 82, 94, Fuentes). | — |
| 9 | link_except g-acceso-rapido in m06-l05 | PASS | Only inside «Barra de herramientas de acceso rápido» (line 101, Fuentes). | — |
| 10 | Kept links: glossary-links.es.txt, m06 lines | PASS | All 11 marks use the entry's sense. See Part 3b. | — |

Part 1: 10 PASS, 0 FAIL.

## Part 2 — course.yaml m06 summaries against the lesson text

The check covered: every term the summary names is in the lesson, in the same sense; the summary says nothing the
lesson does not; three sentences at most; the voice «never does» list; Peninsular Spanish.

| # | summary | sentences | PASS/FAIL | reason | replacement |
|---|---|---|---|---|---|
| 1 | m06 (module) | 2 | PASS | Hardware, software, almacenamiento, seguridad (l01); entorno gráfico (l02 title); Explorador de archivos, accesorios, herramientas del sistema (l03); Word, Excel, Access, Outlook (l04–l07); Internet, protocolos, navegador (l08). | — |
| 2 | m06-l01 | 2 | PASS | CPU, RAM, caché, múltiplos del byte, NTFS, malware, antivirus, cortafuegos, requisitos de Windows 11, RAID, nube («Almacenamiento en la nube»), autenticación multifactor, ENS: all items of the lesson. | — |
| 3 | m06-l02 | 3 | PASS | Ventanas, menús contextuales, cuadros de diálogo with their keys; escritorio, barra de tareas, notificaciones, varios escritorios, varias pantallas, menú Inicio; Copilot in Windows («Abrir Copilot»), Word, Excel, Outlook. | — |
| 4 | m06-l03 | 3 | PASS | Diseños, extensiones, menú contextual, rutas UNC, Inicio, Acceso rápido, Este equipo, keys, indexación, Buscar en Windows, Bloc de notas, Recortes, Paint, Calculadora, Administrador de tareas, Visor de eventos, Historial de archivos: all items. | — |
| 5 | m06-l04 | 3 | PASS | Cinta, barra de estado, revisión (F7), Lectura en voz alta, Transcribir, combinar correspondencia, macros, tabla de contenido, índice, notas, secciones, encabezados, tablas, formatos, plantillas (.dotx/.dotm), Autoguardado, Autorrecuperación, PDF, impresión, cinta, barra de herramientas de acceso rápido. «Estilos» appears only as «Los estilos de título forman la tabla de contenido» (LQMC) and «aplica Título 1, Título 2…» (same sense, but thin). | Optional: «Estilos de título, tabla de contenido, …» |
| 6 | m06-l05 | 3 | PASS | Hojas, rangos (no adyacentes), protección, Inmovilizar paneles, formato de fecha personalizado, referencias relativas/absolutas/a otras hojas/estructuradas, SI, NO, O, SI.ERROR, CONTARA, BUSCARV, #N/A, Gráficos recomendados, ordenar, Autofiltro, Subtotales, tablas dinámicas, segmentación de datos, Power Query, Validación de datos, Imprimir, cinta. | — |
| 7 | m06-l06 | 3 | PASS | Objetos, límites, Compactar y reparar, dividir, tipos de datos, propiedades de campo, clave principal, reglas de validación, consultas de selección/acción/parámetros («Parámetros» item under Consultas), criterios, WHERE, formularios, subformularios, informes, secciones, relaciones, integridad referencial, importar/vincular/exportar. | — |
| 8 | m06-l07 | 3 | PASS | Two clients named as the lesson names them; IMAP, POP, S/MIME, grupos, permisos de carpeta, acceso delegado, Búsqueda, Buzón actual, categorías, Limpieza de buzón, Archivar, responder, reenviar, recuperar mensaje, programar envío, importancia, firmas, reglas on new and existing messages, libreta de direcciones, grupos de contactos. | — |
| 9 | m06-l08 | 3 | PASS | ARPANET, NCP→TCP/IP on 1-1-1983, World Wide Web, Web 4.0, capas TCP/IP, dirección IP, direcciones privadas, DNS, HTTP, HTTPS, FTP, SMTP, HTML, JavaScript, diseño adaptable, spam; Edge: cookies, historial, favoritos, descargas, InPrivate, extensiones, anclar un sitio a Inicio. | — |

Voice: no fillers, rhetorical questions, «no solo… sino», closers or hedges. The three-item enumerations (l02 «ventanas,
menús contextuales y cuadros de diálogo», l07 «IMAP, POP y S/MIME», l03's parenthetical lists) are lists of lesson
items, not rhythmic triads, so I did not count them as violations. Spanish: Peninsular, with no voseo or American forms.
Small readability point, not a FAIL: l06 «Compactar y reparar y dividir la base de datos» has two «y» in a row.

Part 2: 9 PASS, 0 FAIL (1 optional wording note).

## Part 3a — glossary entries with origin m06-l0N (43)

The check covered: the term (or a `match` form) appears in its origin lesson; the definition is supported by the
named saved source; no duplicate of an older entry's sense. Older entries were scanned for overlap (certificado
electrónico, portal de internet, sede electrónica, datos personales…): none share a sense with these 43.

| # | id | origin | in lesson | source support | dup | PASS/FAIL |
|---|---|---|---|---|---|---|
| 1 | g-malware | l01 | yes (2+2) | INCIBE 2.13.2 Malware, incl. virus, gusanos, troyanos, backdoors, spyware | no | PASS |
| 2 | g-cortafuegos | l01 | yes | INCIBE 2.3.33 (software or hardware, puntos limítrofes, permitir y limitar, conjunto de normas) | no | PASS |
| 3 | g-phishing | l01 | yes | INCIBE 2.16.9, near-verbatim | no | PASS |
| 4 | g-copia-de-seguridad | l01 | yes (plural ×3) | INCIBE 2.3.30, near-verbatim | no | PASS |
| 5 | g-doble-factor-de-autenticacion | l01 | yes (ENS item) | INCIBE 2.4.20 (código a un móvil, huella dactilar, OTP) | no | PASS |
| 6 | g-saas | l01 | yes | INCIBE 2.18.1 | no | PASS |
| 7 | g-ntfs | l01 | yes | ms-win-ntfs: «predeterminado… descriptores de seguridad, cifrado, cuotas de disco» | no | PASS |
| 8 | g-barra-de-tareas | l02 | yes | ms-win-barra-tareas: «iniciar aplicaciones, cambiar entre ventanas abiertas y acceder a… notificaciones, búsqueda y el menú Inicio» | no | PASS |
| 9 | g-menu-inicio | l02 | yes | ms-win-menu-inicio: «acceso rápido a las aplicaciones, la configuración y los archivos… anclar… aplicaciones, carpetas y sitios web» | no | PASS |
| 10 | g-acceso-directo | l02 | yes | ms-win-iconos-escritorio: «accesos directos para un acceso rápido», «sin tener que navegar por varios menús o carpetas», «Seleccionar nuevo>acceso directo… archivo, carpeta o página web» | no | PASS |
| 11 | g-papelera-de-reciclaje | l02 | yes | ms-win-iconos-escritorio «donde se almacenan temporalmente los archivos eliminados»; ms-onedrive-restaurar «se restaura a su carpeta original» | no | PASS |
| 12 | g-windows-hello | l02 | yes | ms-win-opciones-inicio-sesion: «reconocimiento facial, una huella digital o un PIN, en lugar de una contraseña» | no | PASS |
| 13 | g-microsoft-copilot | l02 | yes | ms-copilot-introduccion: experiences powered by LLM and «Fundamentación en datos web u organizativos (Microsoft Graph…)»; «La aplicación Microsoft 365 Copilot ahora se denomina Microsoft Copilot» | no | PASS |
| 14 | g-explorador-de-archivos | l03 | yes | ms-win-explorador: «encontrar, abrir, organizar y administrar archivos y carpetas en tu PC y en la nube» | no | PASS |
| 15 | g-acceso-rapido | l03 | yes | ms-win-explorador: 22H2, carpetas conocidas «ancladas en Acceso rápido» | no | PASS |
| 16 | g-indexacion | l03 | yes | ms-win-indexacion: «proceso de buscar archivos, mensajes… y catalogar su información, como las palabras y los metadatos… resultados más rápidamente» | no | PASS |
| 17 | g-editor-del-registro | l03 | yes | ms-win-herramientas-sistema, near-verbatim | no | PASS |
| 18 | g-historial-de-archivos | l03 | yes | ms-win-historial-archivos: automatic copies of all libraries, «copias de seguridad periódicas en una unidad externa o ubicación de red» | no | PASS |
| 19 | g-plantilla | l04 | yes | ms-office-formatos-archivo: .dotx «Plantilla para crear nuevos archivos… que no contienen macros»; .dotm «habilitada para macros… personalizaciones de la interfaz de usuario o macros» | no | PASS |
| 20 | g-macro | l04 | yes | ms-word-macros, near-verbatim | no | PASS |
| 21 | g-combinacion-de-correspondencia | l04 | yes («combinar correspondencia») | ms-word-combinar-correspondencia: «lote de documentos personalizados para cada destinatario… listas, hojas de cálculo o bases de datos… campos de combinación» | no | PASS |
| 22 | g-autoguardado | l04 | yes | ms-office-autoguardado: «Excel, Word y PowerPoint para Microsoft 365 suscriptores… cada pocos segundos»; enabled by default on OneDrive / SharePoint Online | no | PASS |
| 23 | g-autorrecuperacion | l04 | yes | ms-word-opciones-guardar: interval in minutes, «deja de responder o se queda sin energía… se abrirá la próxima vez», «no reemplaza el comando Guardar» | no | PASS |
| 24 | g-coautoria | l04 | yes | ms-word-coautoria: «verá su presencia y los cambios… Esto se denomina coautoría o colaboración en tiempo real» | no | PASS |
| 25 | g-referencia-relativa | l05 | yes | ms-excel-formulas, near-verbatim, incl. «De forma predeterminada, las nuevas fórmulas usan referencias relativas» | no | PASS |
| 26 | g-tabla-dinamica | l05 | yes | ms-excel-tabla-dinamica: «calcular, resumir y analizar datos… comparaciones, patrones y tendencias» | no | PASS |
| 27 | g-segmentacion-de-datos | l05 | yes | ms-excel-segmentacion: «botones… para filtrar tablas o tablas dinámicas… indican el estado de filtrado actual» | no | PASS |
| 28 | g-clave-principal | l06 | yes | ms-access-clave-principal: valores únicos, «solo puede tener una», «comprueba que cada registro tiene un valor… y que este es siempre distinto» | no | PASS |
| 29 | g-clave-externa | l06 | yes | ms-access-clave-principal: «Una clave externa es, sencillamente, la clave principal de otra tabla»; it refers to the source table | no | PASS |
| 30 | g-integridad-referencial | l06 | yes | ms-access-relaciones: keeps FK/PK references «sincronizadas», «evitar los registros huérfanos», «Una vez habilitada, Access rechazará todas las operaciones que infrinjan» | no | PASS |
| 31 | g-regla-de-validacion | l06 | yes | ms-access-reglas-validacion: «forma de limitar la información que se escribe en un campo de tabla o en un control… de un formulario»; «los datos… no se aceptan y Access muestra un mensaje»; rules contain expressions | no | PASS |
| 32 | g-tabla-vinculada | l06 | yes | ms-access-importar-excel: «muestra los datos… pero no almacena realmente los datos en la base de datos»; «Cualquier cambio… se refleja automáticamente» | no | PASS |
| 33 | g-imap | l07 | yes | ms-outlook-imap-pop: «no lo descarga ni almacena en el equipo… lo está leyendo en el servicio… desde diferentes dispositivos» | no | PASS |
| 34 | g-pop | l07 | yes | ms-outlook-imap-pop: downloads new messages, then «se eliminan del servicio… solo se puede acceder a él con el mismo equipo» | no | PASS |
| 35 | g-s-mime | l07 | yes | ms-outlook-smime: «Cifrar este mensaje (S/MIME)», «Firmar digitalmente este mensaje (S/MIME)», «desbloquee el mensaje con un certificado en su equipo» | no | PASS |
| 36 | g-acceso-delegado | l07 | yes | ms-outlook-delegados: «permiso para acceder a su buzón o a carpetas específicas… crear y responder mensajes en su nombre» | no | PASS |
| 37 | g-lista-de-contactos | l07 | yes | ms-outlook-listas-contactos: «colección de contactos y direcciones de correo… a un grupo de personas»; classic Outlook «Crear un grupo de contactos» | no | PASS |
| 38 | g-tcp-ip | l08 | yes | INCIBE 2.19.2 TCP/IP | no | PASS |
| 39 | g-direccion-ip | l08 | yes | INCIBE 2.4.12 (único, todo sistema conectado; públicas/privadas) | no | PASS |
| 40 | g-dns | l08 | yes | INCIBE 2.4.17 (servicio and servidor; nombres inteligibles → direcciones IP) | no | PASS |
| 41 | g-https | l08 | yes | INCIBE HTTPS: «versión segura de HTTP… clave… previamente intercambiada entre el navegador y el servidor» | no | PASS |
| 42 | g-cookie | l08 | yes | INCIBE 2.3.29, near-verbatim | no | PASS |
| 43 | g-spam | l08 | yes | INCIBE 2.3.32 «Correo spam», synonym «Correo basura» | no | PASS |

Part 3a: 43 PASS, 0 FAIL.

## Part 3b — m06 lines of glossary-links.es.txt (11)

| # | lesson | term id | marked occurrence | sense | PASS/FAIL | note |
|---|---|---|---|---|---|---|
| 1 | m06-l02 | g-tabla-dinamica | Copilot en Excel «genera… gráficos y «tablas dinámicas»» | Excel PivotTable | PASS | — |
| 2 | m06-l03 | g-barra-de-tareas | Abrir el Explorador «desde la «barra de tareas»» | Windows taskbar | PASS | — |
| 3 | m06-l03 | g-menu-inicio | «desde el «menú Inicio»» | Start menu | PASS | — |
| 4 | m06-l03 | g-papelera-de-reciclaje | «Supr o Ctrl+D mueve a la «Papelera de reciclaje»» | Recycle Bin | PASS | — |
| 5 | m06-l03 | g-acceso-directo | «con Alt, crea un «acceso directo» al original» | shortcut to a file | PASS | — |
| 6 | m06-l03 | g-copia-de-seguridad | «Guardar «copias de seguridad» de los archivos con Historial de archivos» | backup copies | PASS | The mark falls inside a Control Panel label; the sense is right. |
| 7 | m06-l06 | g-macro | Access objects «…informes, «macros» y módulos» | macro (automates a task) | PASS | Access macros are actions, not recorded commands, but they fit the entry's general sense. |
| 8 | m06-l08 | g-pop | «se usa para enviar, y «POP» o IMAP para recibir» | POP mail access | PASS | — |
| 9 | m06-l08 | g-imap | «POP o «IMAP» para recibir» | IMAP mail access | PASS | — |
| 10 | m06-l08 | g-phishing | «junto a ataques de «phishing»» | phishing | PASS | — |
| 11 | m06-l08 | g-menu-inicio | Fuentes title «Personalizar el «menú Inicio» de Windows» | Start menu | PASS | The sense is right, but the mark sits inside a source title (nested «»). Optional link_except m06-l08 for tidiness. Not required, because the sense is correct (unlike the g-informacion-general case). |

Part 3b: 11 PASS, 0 FAIL.

## Counts

| part | PASS | FAIL |
|---|---|---|
| 1 — recheck queue | 10 | 0 |
| 2 — summaries | 9 | 0 |
| 3a — glossary entries | 43 | 0 |
| 3b — link lines | 11 | 0 |
| total | 73 | 0 |

Optional notes, none blocking: the l04 summary's «Estilos» rests only on heading styles; the l06 summary has «… y
reparar y dividir …»; links line 11 marks a term inside a Fuentes title.
