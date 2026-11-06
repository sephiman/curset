# Currency audit 2026-11 — Part P, saved pages whose live text changed

Verifier: blind (Part P of `spec.md`). Date 2026-11-05. Places = lesson sentences and esquema rows in
`content/age-administrativo-c1/es/lessons/`, glossary entries, and live (not already dropped) questions in
`docs/age-verification/bank/bloque-*/*.draft.json` and `docs/age-verification/cases/` that cite the file. No case
draft cites any of these pages. Questions already in a `drops.tsv` before this audit are listed but not counted
(m06-l04-q244, m06-l01-q350, m06-l02-q350, m06-l07-q226/227/228, m01-l01-q009). The «Fuentes» list lines of each
lesson and the «Otras fuentes» line of m01-l06 name files only; they state no fact and are not counted.

Extracted text, fetch scripts and candidate pages: `/tmp/claude-1000/-home-juanjo-PycharmProjects-curset/d5de772b-b314-4f5a-b041-68bab9a3784e/scratchpad/audit-pages/`
(`text/`, `fetch/`, `scripts/`).

**Ruling used for questions (flag for the coordinator).** A question FAILs (and is dropped) when the cited page's live
text no longer states its key or a fact a distractor or the explanation rests on, and no live page on the same site
states it either, or when a label in the key changed. Where the cited URL lost the text but one live page on the same
site states the key and every refutation, the question is marked **re-cite** (not dropped): the coordinator updates its
`citation` and saves the new page. If the coordinator reads Part P as «cited page only», the re-cite ids to add to
`bloque-vi/drops.tsv` are m06-l02-q026, q027, q028, q029, q030, q031, q034 and to `bloque-i/drops.tsv` m01-l06-q025,
q026, q027.

## Fetches made by this verifier (one each)

| URL | HTTP | final URL | use |
|---|---|---|---|
| https://learn.microsoft.com/es-es/microsoft-365-apps/compatibility/office-file-format-reference | 404 | same | format table: not found |
| https://learn.microsoft.com/es-es/deployoffice/compat/office-file-format-reference | 200 | https://learn.microsoft.com/es-es/office/ | index only |
| https://learn.microsoft.com/en-us/office/compatibility/office-file-format-reference | 200 | https://learn.microsoft.com/en-us/office/ | index only |
| https://learn.microsoft.com/api/search?search=Referencia de formatos de archivo para Word, Excel y PowerPoint&locale=es-es | 200 | — | no matching page in top 10 |
| https://learn.microsoft.com/es-es/entra/identity/authentication/concept-mfa-howitworks | 200 | same | MFA three factors |
| https://learn.microsoft.com/api/search?search=grupos de envío y recepción Outlook&locale=es-es | 200 | — | no send/receive page in top 10 |
| https://support.microsoft.com/es-es/accessibility/windows/magnifier/chapter-1-introducing-magnifier | 200 | same | Lupa on/off, path |
| …/magnifier/chapter-2-choosing-view | 200 | same | views, «Que la Lupa siga mi» |
| …/magnifier/chapter-3-zooming-panning | 200 | same | zoom, 1× toggle |
| …/magnifier/chapter-5-making-content-clearer | 200 | same | Ctrl+Alt+I |
| …/magnifier/appendix-b-magnifier-settings-troubleshooting | 200 | same | settings list |
| …/magnifier/keyboard-shortcuts-for-magnifier (Apéndice A) | 200 | same | every Lupa shortcut |
| https://transparencia.gob.es/gobierno-abierto/planes-accion/VPlan | 200 | same | V Plan summary |
| https://transparencia.gob.es/gobierno-abierto/planes-accion/ivplan | 200 | same | IV Plan summary |
| https://transparencia.gob.es/gobierno-abierto/planes-accion/VPlan/vplan | 200 | same | old `transparencia-v-plan.html` text, verbatim |
| https://support.microsoft.com/es-es/outlook/people/send-an-email-to-a-group-in-outlook | **200** | same | not refused today (item 11) |

## 1. `ms-office-formatos-archivo.html` — URL redirects to the Office documentation index

Live: «# Documentación de Microsoft Office» with links to Office LTSC 2024/2021, 2019, 2016, Mac, add-ins. No format
table. No same-site page found (table above).

| place | fact | stored text | live text | verdict | replacement / check |
|---|---|---|---|---|---|
| m06-l04:71-72 (esquema «Formatos») | .docx predeterminado; .doc Word 97-2003; .docm con macros; .dotx plantilla sin macros; .dotm plantilla con macros o personalizaciones | «.docx Documento de Word — Formato de archivo basado en XML predeterminado…»; «.dotm … Los usuarios que deseen incluir personalizaciones de la interfaz de usuario o macros en la plantilla deben usar este formato» | not on the live page | removed | delete the row. If a row must stay: «- **Plantilla Normal.dotm**: guarda las macros que quieres tener en todos los documentos futuros (fuente: `ms-word-macros.html`).» (`ms-word-macros.html` live text identical: «Para hacer que la macro de un documento esté disponible en todos los futuros documentos, agréguela a la plantilla Normal.dotm.») |
| m06-l04:117-118 («Lo que más cae») | .dotm habilitada para macros; .dotx sin macros | same rows | not on the live page | removed | delete |
| glossary `g-plantilla` (2179) | .dotx no contiene macros; .dotm habilitada para macros e interfaz | same rows | not on the live page | removed | «Archivo de Word que sirve de modelo para documentos nuevos. En la plantilla Normal.dotm se guardan las macros que quieres tener en todos los documentos futuros (fuente: ms-word-macros.html).» The first sentence has no live source either; drop it if the glossary needs one for every clause. |
| m06-l04-q243 | .dotx sin macros, .dotm con macros | «.dotx … que no contienen macros» | not on the live page | removed | FAIL check 3, dropped |
| m06-l04-q245 | .dot = plantilla Word 97-2003 | «.dot Plantilla de Word 97-2003» | not on the live page | removed | FAIL check 3, dropped |
| m06-l04-q246 | .docm almacena VBA | «Almacena código de macros Visual Basic para Aplicaciones (VBA)» | not on the live page | removed | FAIL check 3, dropped |
| m06-l04-q247 | .docx formato XML predeterminado | «Formato de archivo basado en XML predeterminado…» | not on the live page | removed | FAIL check 3, dropped |
| m06-l04-q248 | .doc binario Word 97-2003 | «Formato de archivo binario para Word 97-Word 2003» | not on the live page | removed | FAIL check 3, dropped |
| m06-l04-q249 | .txt pierde todo el formato | «…perderá todo el formato» | not on the live page | removed | FAIL check 3, dropped |
| m06-l04-q250 | .rtf transfiere entre sistemas | «…pueden transferirse entre los sistemas operativos y las aplicaciones» | not on the live page | removed | FAIL check 3, dropped |

Also cited by `exercises/m06-l04-ex-6.yaml`, `m06-l04-ex-7.yaml` and `excerpts.json` (outside Part P's place list; they
inherit these verdicts).

## 2. `ms-cuenta-mfa.html` — URL serves another page

Live: «# Cómo utilizar la verificación en dos pasos con su cuenta de Microsoft». It says «La verificación en dos pasos
(a veces denominada autenticación multifactor) … Usa dos formas diferentes de identidad: su contraseña y un método de
contacto». Same site: Microsoft Learn «Cómo funciona: autenticación multifactor de Microsoft Entra» (200) lists «Algo
que tú sabes, normalmente una contraseña. / Algo que tiene, como un dispositivo de confianza … (por ejemplo, un teléfono
o una clave de hardware). / Algo que eres - biometría como una huella digital o un escaneo facial.» It has no PIN, no
smartphone/USB, no 6-digit code, no 30 s.

| place | fact | stored text | live text | verdict | replacement / check |
|---|---|---|---|---|---|
| m06-l01:85-86 (esquema «Autenticación multifactor») | segundo factor: algo que sabes, que tienes o que eres | «Los tres tipos de factores más comunes son: Algo que sabe… Algo que tiene… Algo que eres…» | not on the live page; on the Entra page | removed | «- **Autenticación multifactor**: además de la contraseña, pide otra forma de identificación al iniciar sesión: algo que sabes, algo que tienes o algo que eres (fuente: `ms-entra-mfa.html`).» (save the Entra page under that name) |
| m06-l01-q344 | tres factores más comunes; ejemplos smartphone/USB, PIN | as above | not on the live page; Entra gives other examples and no «más comunes» | removed | FAIL check 3, dropped |
| m06-l01-q345 | «algo que sabe» = contraseña o PIN memorizado | «Algo que sabe: como una contraseña o un PIN memorizado.» | not on the live page; Entra: «normalmente una contraseña» | removed | FAIL check 3, dropped |
| m06-l01-q346 | «algo que eres» = huella o reconocimiento facial | «Algo que eres: como una huella dactilar o reconocimiento facial.» | not on the live page; distractor refutations (smartphone/USB, correo) on no live page | removed | FAIL check 3, dropped |
| m06-l01-q347 | código de 6 dígitos | «número único de 6 dígitos creado dinámicamente» | not on the live page | removed | FAIL check 3, dropped |
| m06-l01-q348 | cambia cada 30 s | «cambia cada 30 segundos» | not on the live page | removed | FAIL check 3, dropped |
| m06-l01-q349 | segundo factor la primera vez o tras cambiar contraseña | «por lo general solo se usa la primera vez…» | not on the live page (live: code «cada vez que inicies sesión en un dispositivo que no sea de confianza») | removed | FAIL check 3, dropped |
| m06-l01-q351 | usuario fácil de descubrir, contraseñas simples o repetidas | «Los nombres de usuario suelen ser fáciles de descubrir…» | not on the live page | removed | FAIL check 3, dropped |

Note: q350 (already dropped) keys «Verificación en dos pasos», which the live page still states.

## 3. `ms-copilot-introduccion.html` — redirects to learn.microsoft.com/es-es/copilot/plan/copilot-overview

| place | fact | stored text | live text | verdict | replacement / check |
|---|---|---|---|---|---|
| m06-l02:94-96 (esquema «Qué es») | LLM, fundamentación en datos web u organizativos (Microsoft Graph); Microsoft 365 Copilot ahora se llama Microsoft Copilot | «Modelos de lenguaje de gran tamaño (LLM)…»; «La aplicación Microsoft 365 Copilot ahora se denomina Microsoft Copilot.» | same two sentences | holds | update `fuentes.yaml` URL to the redirect target |
| m06-l02:112-113 («Lo que más cae») | Copilot genera lenguaje natural con LLM a partir de datos web y de la organización | same | same | holds | — |
| glossary `g-microsoft-copilot` (2115) | same two facts | same | same | holds | — |
| m06-l02-q335 | LLM + datos web u organizativos + permisos de usuario | «Sin embargo, todas las experiencias están impulsadas por: …» | same three lines | holds | 5 checks PASS |
| m06-l02-q336 | Microsoft Graph y Work IQ | «Fundamentación en datos web u organizativos (Microsoft Graph y Work IQ)» | same | holds | PASS |
| m06-l02-q337 | ahora se llama Microsoft Copilot; Cowork y Code por uso | same | same; «tienes acceso a Cowork a través de la facturación basada en el uso» | holds | PASS |

## 4. `ms-win-lupa.html` — restructured into a table of contents with chapter pages

Live keeps only «Amplía parte o toda la pantalla para que las palabras, las imágenes y los controles sean más fáciles
de ver» and the chapter list. Shortcuts and paths moved to the chapter pages (fetched, table above). Apéndice A lists:
«Activar la Lupa — Tecla de Windows +Signo más (+)», «Desactivar la Lupa — Tecla Windows + Esc», «Alejar — Tecla de
Windows +Signo menos (−)», «Alternar entre el aumento establecido y 1× (normal) — Ctrl+Alt+Signo menos (-)», «Vista de
pantalla completa Ctrl+Alt+F / Vista de lente Ctrl+Alt+L / Vista acoplada Ctrl+Alt+D / Desplazarse a través de las
vistas Ctrl+Alt+M», «Invertir colores (y volver a cambiar) Ctrl+Alt+I», «Abrir la configuración de la Lupa — Tecla
Windows + Ctrl + M».

| place | fact | stored text | live text | verdict | replacement / check |
|---|---|---|---|---|---|
| m06-l02:16-17 (esquema «Lupa») | amplía toda o parte; Windows+(+) activa, Windows+Esc desactiva; «Configuración › Accesibilidad › Lupa» | «Para activar la Lupa, presiona … Signo Más(+). Para desactivar … +Esc»; «Ve a Inicio, selecciona Configuración y elige Accesibilidad» | first clause holds; shortcuts and path not on the page (on Capítulo 1: «Activar: Tecla Windows + Signo más (+) / Desactivar: Tecla Windows + Esc»; Capítulo 2: «Configuración>,Accesibilidad>,Lupa>») | removed (2 of 3 facts) | «- **Lupa**: amplía toda la pantalla o parte de ella (fuente: `ms-win-lupa.html`). Windows+signo más (+) la activa y Windows+Esc la desactiva; está en «Configuración › Accesibilidad › Lupa» (fuente: `ms-win-lupa-cap1.html`).» |
| m06-l02:118-119 («Lo que más cae») | Lupa en «Configuración › Accesibilidad», Windows+(+) | as above | not on the page; on Capítulo 1 | removed | «- La Lupa está en «Configuración › Accesibilidad» y se activa con Windows+signo más (+) (fuente: `ms-win-lupa-cap1.html`).» |
| m06-l02-q026 | Windows+(+) activa, Windows+Esc desactiva | as above | Apéndice A | removed | re-cite to Apéndice A; checks PASS there |
| m06-l02-q027 | ruta Configuración › Accesibilidad › Lupa, interruptor | «…elige Accesibilidad. Selecciona la Lupa y luego activa el interruptor» | Capítulo 1: «Seleccionala Lupade accesibilidad>de la configuración>. Encienda el interruptor de la Lupa.» (garbled localisation of the same path) | removed | re-cite to Capítulo 1; PASS; the explanation's «Inicio» is not on that page |
| m06-l02-q028 | Ctrl+Alt+I invierte | «…presione Ctrl+Alt+I» | Apéndice A, Capítulo 5 | removed | re-cite to Apéndice A; PASS |
| m06-l02-q029 | Ctrl+Alt+L = lente | «…vista de lente, presione Ctrl+Alt+L» | Apéndice A | removed | re-cite to Apéndice A; PASS |
| m06-l02-q030 | Ctrl+Alt+M recorre las vistas | «Para desplazarse entre las vistas, presione Ctrl+Alt+M» | Apéndice A «Desplazarse a través de las vistas Ctrl+Alt+M» | removed | re-cite; PASS; explanation quote is not verbatim on the new page, re-quote |
| m06-l02-q031 | Windows+Ctrl+M abre la configuración | «…para abrir la vista de configuración de la Lupa» | Capítulo 2 verbatim; Apéndice A | removed | re-cite to Capítulo 2; PASS |
| m06-l02-q032 | «Que mi Lupa lo siguiera» en Ver, cuatro casillas en cualquier combinación | «Seleccione Ver y, a continuación, en Que mi Lupa lo siguiera…» | Capítulo 2: «En Que la Lupa siga mi, selecciona o desactiva cualquier combinación de…»; Apéndice B: «Hacer que la Lupa siga mis» | removed (label changed) | FAIL check 3, dropped |
| m06-l02-q033 | amplía toda la pantalla o parte | «La Lupa amplía toda la pantalla o parte de ella…» | «Amplía parte o toda la pantalla para que las palabras, las imágenes y los controles sean más fáciles de ver» | holds | PASS; the explanation quotes the Windows 10 wording (Capítulo 1), re-quote |
| m06-l02-q034 | Ctrl+Alt+(−) alterna con 1x | «…cambiar entre el nivel de ampliación establecido y el aumento de 1x…» | Apéndice A «Alternar entre el aumento establecido y 1× (normal)» | removed | re-cite; PASS; re-quote |

## 5. `ms-outlook-grupos-envio-recepcion.html` — URL serves the Office documentation index

The OCT 2016 help page is gone (Office 2016 out of support). No send/receive group page on Learn search.

| place | fact | stored text | live text | verdict | replacement / check |
|---|---|---|---|---|---|
| m06-l07:66-69 (esquema «Enviar y recibir», last sentence) | un grupo de envío y recepción contiene cuentas y carpetas; se programa cada n minutos o al salir | «Un grupo de envío y recepción contiene una colección de cuentas y carpetas de Outlook»; «Programar un envío o recepción automáticos cada n minutos»; «Realizar un envío/recepción automático al salir» | not on the live page | removed | delete that sentence; the row keeps «Ctrl+M o F9 … Ctrl+Alt+S define los grupos Enviar y recibir. Ctrl+Entrar envía en los dos clientes (fuente: `ms-outlook-atajos.html`).» |

## 6. `ms-excel-copilot.html` — two sentences changed

Changes: «También puede grabar una aptitud demostrando una tarea en el libro.» added; the Stop button moved from «la
esquina inferior derecha del campo de entrada del chat» to «el lado derecho del campo de entrada del chat».

| place | fact | stored text | live text | verdict | replacement / check |
|---|---|---|---|---|---|
| m06-l02:101-102 (esquema «Copilot en Excel») | icono abajo a la derecha; datos y fórmulas, gráficos y tablas dinámicas | «Seleccione el icono de Copilot en la esquina inferior derecha de Excel»; «Generar datos y fórmulas…»; «Crear gráficos, tablas dinámicas y formas…» | unchanged | holds | — |
| m06-l02-q345 | icono en la esquina inferior derecha de Excel | same | unchanged | holds | PASS |
| m06-l02-q346 | se abre en modo de edición | same | unchanged | holds | PASS |
| m06-l02-q347 | modo plan genera un plan | same | unchanged | holds | PASS |
| m06-l02-q348 | solo chat analiza sin cambiar | same | unchanged; distractor d «Detener … botón de la esquina inferior derecha» now «lado derecho del campo de entrada del chat» | holds | PASS: d stays wrong (Detener is not a mode); its location wording is now stale |
| m06-l02-q349 | Windows: edición, chat y planeación | same table | unchanged | holds | PASS |
| m06-l02-q356 | OneDrive, SharePoint o equipo | same | unchanged | holds | PASS |
| m06-l02-q359 | búsqueda web con citas | same | unchanged | holds | PASS |

## 7. `transparencia-planes-accion.html` — restructured

The submenu of plan pages is replaced by the plans and their periods on the page itself.

| place | fact | stored text | live text | verdict | replacement / check |
|---|---|---|---|---|---|
| m01-l06:94-97 | los planes recogen las actuaciones de la AGE con otras Administraciones y la sociedad civil, en participación, transparencia, integridad y sensibilización social | «Los Planes de Gobierno Abierto de España recogen el conjunto de actuaciones…» | same sentence | holds | — |
| m01-l06-q023 | AGE con otras Administraciones y sociedad civil | same | same | holds | PASS |
| m01-l06-q024 | los cuatro ámbitos | same | same | holds | PASS |

## 8. `whatwg-html-scripting.html` — spec wording edits

Edits touch the «intended document» of script elements and noscript parsing; none touches the cited sentences.

| place | fact | stored text | live text | verdict | replacement / check |
|---|---|---|---|---|---|
| m06-l08:55-57 | scripts dan interactividad; muchos usuarios los desactivan | «Scripts allow authors to add interactivity…»; «…many users disable scripting» | same | holds | — |
| m06-l08-q144 | alternativas declarativas: más mantenibles, usuarios desactivan scripts | same | same | holds | PASS |
| m06-l08-q145 | details en lugar de script | «…the details element could be used» | same | holds | PASS |
| m06-l08-q146 | sin scripts, botón para calcular en el servidor | «When script is disabled, a button appears…» | same | holds | PASS |

## 9. `boe-analisis-ce.xml` — new posterior reference, two relabels

Live adds «BOE-A-2026-22710 — SE DICTA — que no existe contradicción entre el art. 2.4 del Tratado de amistad y
cooperación entre el Reino de España y la República Francesa … por Declaración 1/2026, de 23 de septiembre» and
relabels the two TC declarations from «SE DECLARA» to «SE DICTA» (the 2004 one now «Declaración 1/2004, de 13 de
diciembre»). The four «SE MODIFICA … por Reforma» entries are unchanged.

| place | fact | stored text | live text | verdict | replacement / check |
|---|---|---|---|---|---|
| m01-l01:66-71 | cuatro reformas, un artículo cada una (13.2 en 1992, 135 en 2011, 49 en 2024, 69.3 en 2026) | four «SE MODIFICA el art. …, por Reforma de …» | same four | holds | — |
| m01-l01-q010 | cuatro reformas, un artículo cada una | same | same | holds | PASS (a TC declaration is not a reform) |

No place in the lesson or glossary states the TC declarations.

## 10. `transparencia-planes-anteriores.html`, `transparencia-iv-plan.html`, `transparencia-v-plan.html` — 404

- `transparencia-iv-plan.html`: no place cites it (lessons cite `transparencia-iv-plan.pdf`, unchanged). Its summary is
  now at `/gobierno-abierto/planes-accion/ivplan` («El IV Plan de Gobierno Abierto 2020-2024 se aprobó el 29 de octubre
  de 2020»).
- `transparencia-planes-anteriores.html`: the periods are now on the live `transparencia-planes-accion.html`: «I Plan de
  Gobierno Abierto 2012-2014», «II Plan de Gobierno Abierto 2014-2016», «III Plan de Gobierno Abierto 2017-2019», «IV
  Plan de Gobierno Abierto 2020-2024», «V Plan de Gobierno Abierto 2025-2029».
- `transparencia-v-plan.html`: the page moved to `/gobierno-abierto/planes-accion/VPlan/vplan` with the same body
  (menus differ only), including «El V Plan de Gobierno Abierto 2025-2029 fue aprobado en la reunión del pleno del Foro
  de 6 de octubre de 2025». `/VPlan` adds «El plan se estructura en 10 compromisos y 218 iniciativas.»

| place | fact | stored text | live text | verdict | replacement / check |
|---|---|---|---|---|---|
| m01-l06:99-109 (table, I–IV periods; source line 107-108) | I 2012-2014, II 2014-2016, III 2017-2019, IV 2020-2024 | «Avances del I Plan de Gobierno Abierto 2012-2014» etc. | URL 404; same periods on `transparencia-planes-accion.html` | removed | replace lines 107-109 with: «Periodos: Portal de la Transparencia, «Conoce los Planes de Acción de España» (fuente: `transparencia-planes-accion.html`).» (that page also gives V Plan 2025-2029) |
| m01-l06-q025 | I Plan 2012-2014 | same | on planes-accion | removed | re-cite to `transparencia-planes-accion.html`; PASS |
| m01-l06-q026 | III Plan 2017-2019 | same | on planes-accion | removed | re-cite; PASS |
| m01-l06-q027 | IV Plan 2020-2024 | same | on planes-accion; stem's 29-10-2020 on `/ivplan` | removed | re-cite; PASS |
| m01-l06:108-109 (V Plan period) | V Plan 2025-2029 | «Diseño del V Plan de Gobierno Abierto 2025-2029» | same text at `/VPlan/vplan` | holds (page moved) | update `fuentes.yaml` URL |
| m01-l06:117-118 | pleno del Foro lo aprobó el 6-10-2025 | «…aprobado en la reunión del pleno del Foro de 6 de octubre de 2025» | same at `/VPlan/vplan` | holds (page moved) | URL update |
| m01-l06:213 («Lo que más cae») | same | same | same at `/VPlan/vplan` | holds (page moved) | URL update |
| m01-l06-q028 | V Plan = 2025-2029 | same | same at `/VPlan/vplan` | holds (page moved) | PASS |
| m01-l06-q034 | 6-10-2025; distractors 9-2-2024 Documento Marco, 17-6-2025 fin de la consulta | same | same at `/VPlan/vplan` («Documento Marco aprobado por el Foro el 9 de febrero», «del 3 al 17 de junio de 2025») | holds (page moved) | PASS |
| m01-l06-q035 | órgano: pleno del Foro | same | same at `/VPlan/vplan` | holds (page moved) | PASS |

## 11. `ms-outlook-grupo-enviar.html` — fetched once, **200** (not refused today)

Live text differs from the stored copy in wording throughout (machine retranslation): «se producen» → «ocurren»,
«Para un grupo privado» → «En el caso de un grupo privado», «Seleccione Nuevo correo» → «Seleccione Correo nuevo»,
«Nuevo Email» → «Nuevo email», «Solo los propietarios del grupo pueden eliminar las conversaciones de todos los usuarios»
→ «…pueden eliminar conversaciones para todos», «seleccione > gruposde correo>» → «seleccione Configuración>Grupos de
correo>».

| place | fact | stored text | live text | verdict | replacement / check |
|---|---|---|---|---|---|
| m06-l07:19-24 | cualquiera de la organización inicia conversación; en clásico todos los miembros reciben; público: toda la organización lee y responde; privado: solo miembros | «Cualquier persona de su organización puede iniciar una conversación de grupo»; «Todos los miembros del grupo recibirán el correo electrónico»; «Para un grupo público…»; «Para un grupo privado…» | «…iniciar una conversación grupal»; «Todos los miembros del grupo recibirán…»; «Para un grupo público, cualquier persona de su organización puede leer y responder…»; «En el caso de un grupo privado, solo los miembros…» | holds | — |
| m06-l07-q037 | privado: solo miembros | «Para un grupo privado, solo…» | «En el caso de un grupo privado, solo…» | holds | PASS; explanation quote to refresh |
| m06-l07-q038 | público: toda la organización | same | same | holds | PASS |
| m06-l07-q039 | Nuevo Email; alias en Para | «seleccione Nuevo Email. Observe que el alias del grupo se agrega automáticamente…» | «seleccione Nuevo email. Observe que el alias…» | holds | PASS (case only) |
| m06-l07-q040 | todos los miembros reciben | same | same | holds | PASS |
| m06-l07-q041 | Responder: solo al remitente | «El mensaje se envía solo a esa persona y no al grupo.» | «El mensaje se envía únicamente a esa persona, pero no al grupo.» | holds | PASS |
| m06-l07-q042 | borrado personal: sigue en el buzón del grupo | same | same (wording) | holds | PASS |
| m06-l07-q043 | solo propietarios eliminan para todos | «…eliminar las conversaciones de todos los usuarios» | «…eliminar conversaciones para todos» | holds | PASS; explanation quote to refresh |
| m06-l07-q044 | Grupos › nombre › **Nuevo correo** | «Seleccione Nuevo correo.» | «Seleccione Correo nuevo.» | changed | FAIL check 1 (key label), dropped |
| m06-l07-q045 | casilla «Enviarme una copia…» | «Active la casilla enviarme una copia…» | «Active la casilla Enviarme una copia…» | holds | PASS |

## 12. `ms-win-directivas-explorador.html`, `ms-win-opciones-inicio-sesion.html` — date and related-links box

Visible text identical except «2025-03-12» → «2026-10-14» (directivas) and the removed «Obtener ayuda con Copilot» box
with three suggested questions (inicio de sesión). No cited fact is affected.

| place | fact | stored text | live text | verdict | replacement / check |
|---|---|---|---|---|---|
| m06-l03:33-36 | directiva «No mover archivos eliminados a la papelera»: se eliminan permanentemente | «…no se colocarán en la Papelera de reciclaje y, por tanto, se eliminarán permanentemente» | identical | holds | — |
| m06-l03:122-124 | same | same | identical | holds | — |
| m06-l03-q116 | habilitada: eliminación permanente | same | identical | holds | PASS |
| m06-l03-q117 | deshabilitada: a la Papelera | same | identical | holds | PASS |
| m06-l02:9-11 | «Configuración › Cuentas › Opciones de inicio de sesión»; Windows Hello: rostro, huella o PIN | identical | identical | holds | — |
| m06-l02:122 | Windows Hello: rostro, huella o PIN | identical | identical | holds | — |
| glossary `g-windows-hello` (2108) | same | identical | identical | holds | — |
| m06-l02-q005 … q012 (8) | ruta, Windows Hello, cámara externa, solo Windows Hello, bloqueo dinámico (Bluetooth, un minuto), detalles de cuenta | identical | identical | holds | PASS each |

## Counts

| page | places | holds | changed | removed | question FAIL | re-cite |
|---|---|---|---|---|---|---|
| ms-office-formatos-archivo | 10 | 0 | 0 | 10 | 7 | 0 |
| ms-cuenta-mfa | 8 | 0 | 0 | 8 | 7 | 0 |
| ms-copilot-introduccion | 6 | 6 | 0 | 0 | 0 | 0 |
| ms-win-lupa | 11 | 1 | 0 | 10 | 1 | 7 |
| ms-outlook-grupos-envio-recepcion | 1 | 0 | 0 | 1 | 0 | 0 |
| ms-excel-copilot | 8 | 8 | 0 | 0 | 0 | 0 |
| transparencia-planes-accion | 3 | 3 | 0 | 0 | 0 | 0 |
| whatwg-html-scripting | 4 | 4 | 0 | 0 | 0 | 0 |
| boe-analisis-ce | 2 | 2 | 0 | 0 | 0 | 0 |
| transparencia-planes-anteriores | 4 | 0 | 0 | 4 | 0 | 3 |
| transparencia-iv-plan.html | 0 | — | — | — | — | — |
| transparencia-v-plan.html | 6 | 6 (moved) | 0 | 0 | 0 | 0 |
| ms-outlook-grupo-enviar | 10 | 9 | 1 | 0 | 1 | 0 |
| ms-win-directivas-explorador | 4 | 4 | 0 | 0 | 0 | 0 |
| ms-win-opciones-inicio-sesion | 11 | 11 | 0 | 0 | 0 | 0 |
| **total** | **88** | **54** | **1** | **33** | **16** | **10** |

Question FAILs (16, appended to `bank/bloque-vi/drops.tsv`, batch `audit-2026-11`): m06-l04-q243, q245, q246, q247,
q248, q249, q250 (citation); m06-l01-q344, q345, q346, q347, q348, q349, q351 (citation); m06-l02-q032 (citation);
m06-l07-q044 (key).

Lesson and glossary places that need a replacement (8): m06-l04:71-72 (delete), m06-l04:117-118 (delete),
glossary `g-plantilla`, m06-l01:85-86, m06-l02:16-17, m06-l02:118-119, m06-l07:66-69 (delete last sentence),
m01-l06:107-109 (source line). `fuentes.yaml` URL updates: `ms-copilot-introduccion.html` (redirect target),
`transparencia-v-plan.html` (`/VPlan/vplan`); new pages to save if the replacements are taken: Entra MFA
(`ms-entra-mfa.html`), Lupa Capítulo 1 (`ms-win-lupa-cap1.html`), and for the re-cites Lupa Apéndice A and Capítulo 2.
