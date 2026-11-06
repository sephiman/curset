# Currency audit 2026-11, follow-up: Part P on pages a browser fetch found changed

Verifier: blind (Part P of `../spec.md`). Date 2026-11-06. Live copies: Playwright Chromium render of 2026-11-06,
`/tmp/claude-1000/-home-juanjo-PycharmProjects-curset/a007fe03-3bc3-45f5-b6b2-5cb53489aae5/scratchpad/pages-browser-live/`
(all three HTTP 200, final URL = stored URL). Extracted text and fetches:
`/tmp/claude-1000/-home-juanjo-PycharmProjects-curset/a007fe03-3bc3-45f5-b6b2-5cb53489aae5/scratchpad/pbv/`.

Places: lesson sentences in `content/age-administrativo-c1/es/lessons/` (only m06-l07 and m06-l08 cite these files;
no esquema row cites them), `glossary.yaml`, and kept questions in `bank/bloque-vi/m06-l0*.draft.json` (merged
`m06-l07.draft.json`, `m06-l08.draft.json`). Already dropped and not counted: m06-l07-q044, m06-l07-q366,
m06-l08-q233, m06-l08-q236. «Fuentes» list lines are not counted. Questions get the five checks of
`bank/bloque-vi/verify-spec.md` (with the 2026-10-24 ruling) against the live text. Ruling carried over from
`../pages.md`: a question whose key and refutations sit on another live same-site page is **re-cite**, not dropped.

## Fetches made by this verifier (one each)

| URL | HTTP | final URL | finding |
|---|---|---|---|
| https://support.microsoft.com/en-us/microsoft-edge/browse-inprivate-in-microsoft-edge-cd2c9a48-0bc4-b98e-5e46-ac40c84e27e2 | 200 | https://support.microsoft.com/en-us/edge/browse-inprivate-in-microsoft-edge | The English source is cut the same way (Summary + one step, «select the Settings and More icon, and then New InPrivate window»). The loss is in the article, not the translation. |
| https://support.microsoft.com/es-es/microsoft-edge/microsoft-edge-datos-de-exploraci%C3%B3n-y-privacidad-bb8174ba-9d73-dcf2-9b4a-c582b4e640dd | 200 | https://support.microsoft.com/es-es/edge/microsoft-edge-browsing-data-and-privacy | «Microsoft Edge, datos de exploración y privacidad», Se aplica a Microsoft Edge Windows 10 Windows 11: «Microsoft Edge eliminará el historial de exploración, las cookies y los datos del sitio, así como las contraseñas, las direcciones y los datos de formulario al cerrar todas las ventanas de InPrivate. Para iniciar una nueva sesión de InPrivate, seleccione Configuración y más en un equipo…». Not saved in `sources/otros/` (suggested file `ms-edge-privacidad.html`). |

## 1. `ms-edge-inprivate.html`: article cut to a summary and one step

Live `<main>`: «Se aplica a Microsoft Edge Windows 10 Windows 11»; a Resumen («…navegar por la Web sin guardar el
historial de exploración, las cookies, los datos del sitio o las entradas de formularios en su dispositivo… permitir
guardar descargas y favoritos»); «Al usar las pestañas o ventanas InPrivate, los datos de exploración (por ejemplo, el
historial, archivos temporales de Internet y cookies) no se guardan en el equipo cuando terminas.»; and one step,
«En Microsoft Edge, seleccione el icono Configuración y más y, después, la ventana Nuevo InPrivate.» Everything else
is gone (taskbar and link paths, the «¿Qué hace…», «no hace», «¿Es más seguro…» and «¿Cuándo no está disponible…»
sections). No other saved page states the lost facts (grep of `sources/otros/` and the live set). `ms-edge-atajos.html`
live still has «Ctrl + Mayús + N Abrir una nueva ventana de InPrivate» and «F10 + Entrar Abrir el menú Configuración y
más».

| place | fact | stored text | live text | verdict | replacement / check |
|---|---|---|---|---|---|
| m06-l08:86-87 | path «Configuración y más › Nueva ventana InPrivate»; Ctrl+Mayús+N; F10+Entrar | «En Microsoft Edge, selecciona Configuración y más>Nueva ventana InPrivate.» | «…seleccione el icono Configuración y más y, después, la ventana Nuevo InPrivate.» (label garbled; EN «New InPrivate window»). Shortcuts hold on `ms-edge-atajos.html`. | changed (label) | «- **InPrivate**: se abre desde el icono Configuración y más o con Ctrl+Mayús+N; F10+Entrar abre el menú Configuración y más (fuente: `ms-edge-inprivate.html`, `ms-edge-atajos.html`).» |
| m06-l08:87-89 | on closing all InPrivate windows Edge deletes history, cookies and site data, passwords, form data; keeps favourites and downloads | «Microsoft Edge eliminará el historial…, así como las contraseñas, las direcciones y los datos de formulario al cerrar todas las ventanas de InPrivate.»; «Guarda tus favoritos y los archivos descargados…» | Cited page: «sin guardar el historial de exploración, las cookies, los datos del sitio o las entradas de formularios»; «permitir guardar descargas y favoritos»; no passwords, no «al cerrar todas las ventanas». The stored sentence is word for word on the privacy page fetched above. | changed | If the privacy page is saved: «Al cerrar todas las ventanas InPrivate, Edge borra el historial de exploración, las cookies y los datos del sitio, las contraseñas, las direcciones y los datos de formulario (fuente: `ms-edge-privacidad.html`). Las descargas y los favoritos se guardan (fuente: `ms-edge-inprivate.html`).» If not: «InPrivate no guarda en el equipo el historial de exploración, las cookies, los datos del sitio ni las entradas de formularios. Las descargas y los favoritos se guardan (fuente: `ms-edge-inprivate.html`).» |
| m06-l08:89-90 | ISP or workplace can see the activity | «…es posible que el proveedor de servicios de Internet o tu centro de trabajo o escuela puedan tener acceso a estos datos.» | not on the live page; not on the privacy page | removed | delete |
| m06-l08-q229 | key «Configuración y más › Nueva ventana InPrivate» | «selecciona Configuración y más>Nueva ventana InPrivate» | «seleccione el icono Configuración y más y, después, la ventana Nuevo InPrivate» | changed (label) | FAIL check 1: the key label is no longer the page's. Also check 4: the refutations of b and d quote removed sentences. Dropped. |
| m06-l08-q230 | right-click Edge logo on taskbar › Nueva ventana InPrivate | «…en el logotipo de Microsoft Edge en la barra de tareas y selecciona Nueva ventana InPrivate.» | not on the live page | removed | FAIL check 3. Dropped. |
| m06-l08-q231 | closing all windows deletes history, cookies, site data, passwords, form data | as row m06-l08:87-89 | cited page: no passwords, no «al cerrar todas las ventanas»; privacy page (200) states the stored sentence word for word | removed (stated on another page) | **re-cite** to the privacy page (`ms-edge-privacidad.html`): key, b and c are refuted there; a («favoritos y archivos descargados») is refuted by the live cited page («permitir guardar descargas y favoritos»). Not dropped. If the page is not saved: FAIL check 3. |
| m06-l08-q232 | key: favourites and downloads are kept | «Guarda tus favoritos y los archivos descargados…» | «permitir guardar descargas y favoritos» | holds (key) | FAIL check 2: c «Los permisos de sitio y los datos de aplicaciones hospedadas» is refuted by no live page (the list that named them is gone). Explanation states it too (check 4). Dropped. |
| m06-l08-q234 | uses InPrivate search with Bing; refutations from the «no hace» list | «Usa automáticamente la búsqueda InPrivate con Microsoft Bing» | not on the live page | removed | FAIL check 3. Dropped. |
| m06-l08-q235 | extensions with permission run; Edge cannot stop them saving history | «Permite que las extensiones…»; «Microsoft Edge no podrá impedir…» | not on the live page | removed | FAIL check 3. Dropped. |
| m06-l08-q237 | «no hace» list: reopen recently closed tabs | «Te permite volver a abrir las pestañas… cerrados recientemente.» | not on the live page | removed | FAIL check 3. Dropped. |
| m06-l08-q238 | children with Activity reporting or web filtering cannot use InPrivate | «Los niños con Informes de actividades o filtrado web…» | not on the live page | removed | FAIL check 3. Dropped. |
| m06-l08-q239 | sites personalise because cookies and permissions stay until all windows close | «Los sitios web también pueden personalizar contenido…» | not on the live page | removed | FAIL check 3. Dropped. |
| m06-l08-q265 | location permissions of the profile that started the session | «La exploración de InPrivate usa la configuración de permisos de ubicación del perfil…» | not on the live page | removed | FAIL check 3. Dropped. |

## 2. `ms-outlook-grupo-enviar.html`: retranslated, facts unchanged

Same facts, new wording throughout (as in `../pages.md` § 11). Two labels changed since the stored copy: «Nuevo correo»
→ «Correo nuevo» (new Outlook and web; q044 stays dropped), «Nuevo Email» → «Nuevo email» (classic). Headings: «…en
la versión clásica de Outlook» → «…en Outlook clásico»; «Eliminar una conversación para todos los usuarios…» →
«Eliminar una conversación de todos los usuarios…».

| place | fact | stored text | live text | verdict | replacement / check |
|---|---|---|---|---|---|
| m06-l07:21 | anyone in the organisation can start a group conversation | «…puede iniciar una conversación de grupo.» | «Cualquier persona de su organización puede iniciar una conversación grupal.» | holds | — |
| m06-l07:21-22 | classic Outlook: all members receive the mail | «Todos los miembros del grupo recibirán el correo electrónico.» | identical | holds | — |
| m06-l07:22-24 | public: anyone in the organisation reads and replies; private: members only | «Para un grupo público…»; «Para un grupo privado, solo los miembros…» | «Para un grupo público, cualquier persona de su organización puede leer y responder…»; «En el caso de un grupo privado, solo los miembros del grupo pueden participar en la conversación.» | holds | — |
| m06-l07-q037 | private group: members only | «Para un grupo privado, solo los miembros…» | «En el caso de un grupo privado, solo los miembros…» | holds | PASS. Edit required: the explanation quotes the old wording in «»; replace with «En el caso de un grupo privado, solo los miembros del grupo pueden participar en la conversación» (and `source_quote`). b refuted by «Cualquier persona de su organización puede iniciar una conversación grupal»; c, d by «solo los miembros». |
| m06-l07-q038 | public group: anyone in the organisation | identical | identical | holds | PASS |
| m06-l07-q039 | Nuevo Email; alias added to Para | «seleccione Nuevo Email. Observe que el alias…» | «seleccione Nuevo email. Observe que el alias del grupo se agrega automáticamente a la línea Para.» | holds | PASS (case only). Edit: «Nuevo email» in stem and explanation quote. |
| m06-l07-q040 | all members receive | identical | identical | holds | PASS |
| m06-l07-q041 | Responder: sender only | «El mensaje se envía solo a esa persona y no al grupo.» | «El mensaje se envía únicamente a esa persona, pero no al grupo.» | holds | PASS. Edit: citation heading «Responder a un correo electrónico a un grupo en Outlook clásico»; `source_quote`. |
| m06-l07-q042 | personal delete: still in group mailbox | «…el correo electrónico de grupo…» | «Si elimina el correo electrónico del grupo de su bandeja de entrada personal, el correo electrónico aún se puede encontrar en el buzón del grupo.» | holds | PASS |
| m06-l07-q043 | only owners delete for everyone | «Solo los propietarios del grupo pueden eliminar las conversaciones de todos los usuarios.» | «Solo los propietarios del grupo pueden eliminar conversaciones para todos.» | holds | PASS. Edit required: explanation quote → «Solo los propietarios del grupo pueden eliminar conversaciones para todos»; citation heading «Eliminar una conversación de todos los usuarios de un grupo en el nuevo Outlook». |
| m06-l07-q045 | checkbox «Enviarme una copia del correo electrónico que envío a un grupo» | «Active la casilla enviarme una copia…»; «seleccione > gruposde correo>» | «Active la casilla Enviarme una copia…»; «seleccione Configuración>Grupos de correo>» | holds | PASS |

## 3. `ms-outlook-listas-contactos.html`: new-Outlook and web steps rewritten

Classic-Outlook tab: same steps, headings «…en Outlook clásico», label «Guardar & Cerrar» → «Guardar & cerrar». New
Outlook and web: «Agregar a la lista › Nueva lista de contactos» and «Todas las listas de contactos» are gone. A list is
now created with «el botón desplegable de la flecha angular v situado junto a Nuevo contacto» › «Nueva lista de
contactos» › Crear, and edited or deleted from «Sus listas de contactos». New sections «Agregar más contactos a una
lista» and «Quitar contactos de una lista». No other saved page uses «Agregar a la lista» in this sense
(`ms-outlook-carpetas-busqueda.html` uses it for search-folder criteria).

| place | fact | stored text | live text | verdict | replacement / check |
|---|---|---|---|---|---|
| m06-l07:106-107 | classic: People › Nuevo grupo de contactos, then Agregar miembros | «Seleccione Nuevo grupo de contactos en la cinta de opciones.»; «…seleccione Agregar miembros…» | identical; People step now «En Outlook clásico, en el panel lateral, seleccione :People.» | holds | — |
| m06-l07:107 | in new Outlook it is called lista de contactos | «…las "listas de contactos" se denominan anteriormente "Grupos de contactos"…» | «En el nuevo Outlook, las "listas de contactos" se conocen anteriormente como "grupos de contactos" en el Outlook clásico.» | holds | — |
| m06-l07:107-108 | deleting the list does not delete the contacts | «Los contactos no se eliminan, solo la lista de contactos.» | identical (classic); new: «Al eliminar una lista de contactos, solo se elimina la lista en sí. Los contactos no se eliminan.» | holds | — |
| glossary `g-lista-de-contactos` (2360-2371) | collection of contacts and addresses for writing to a group; classic name grupo de contactos | «Una lista de contactos es una colección de contactos y direcciones de correo electrónico…» | identical; naming sentence as above | holds | — |
| m06-l07-q347 | definition | identical | identical | holds | PASS. Note, outside this page: the explanation's «grupo de envío y recepción» claim rests on `ms-outlook-grupos-envio-recepcion.html`, whose URL is gone (`../pages.md` § 5); the saved copy still states it. |
| m06-l07-q348 | new name lista de contactos | «…se denominan anteriormente…» | «…se conocen anteriormente como…» | holds | PASS. Edit: `source_quote`. |
| m06-l07-q349 | classic: Nuevo grupo de contactos › Agregar miembros | identical | identical | holds (key) | FAIL check 4: explanation says «Agregar a la lista › Nueva lista de contactos es el procedimiento del nuevo Outlook» and «Todas las listas de contactos también es del nuevo Outlook»; no live page states either. Dropped. |
| m06-l07-q350 | classic delete: contacts kept | identical | identical | holds | PASS. Edit: citation heading «Eliminar un grupo de contactos en Outlook clásico». |
| m06-l07-q351 | new Outlook: Agregar a la lista › Nueva lista de contactos | «Seleccione Agregar a la lista… y, a continuación, seleccione Nueva lista de contactos.» | «Seleccione el botón desplegable de la flecha angular v situado junto a Nuevo contacto y, después, seleccione Nueva lista de contactos.» | changed | FAIL check 1: the keyed path is no longer on the page. Dropped. |
| m06-l07-q352 | consider a group in Outlook for more | identical | identical | holds | PASS (same note as q347 on distractor a). |
| m06-l07-q364 | classic edit: double-click, Agregar o quitar miembros | identical | identical | holds (key) | FAIL check 4: explanation says «Todas las listas de contactos y Agregar a la lista son pasos del nuevo Outlook»; no live page states it. Dropped. |
| m06-l07-q365 | classic: Guardar & Cerrar | «Cuando haya terminado, seleccione Guardar & Cerrar.» | «Cuando haya terminado, seleccione Guardar & cerrar.» | holds (case only) | PASS. Edit: «Guardar & cerrar» in option c and explanation, as q039. |

## Counts

| page | places | holds | changed | removed | question FAIL | re-cite |
|---|---|---|---|---|---|---|
| ms-edge-inprivate | 13 | 1 | 3 | 9 | 9 | 1 |
| ms-outlook-grupo-enviar | 11 | 11 | 0 | 0 | 0 | 0 |
| ms-outlook-listas-contactos | 12 | 11 | 1 | 0 | 3 | 0 |
| **total** | **36** | **23** | **4** | **9** | **12** | **1** |

Question FAILs (12, appended to `bank/bloque-vi/drops.tsv`, batch `followup-2026-11`): m06-l08-q229 (key), q230,
q234, q235, q237, q238, q239, q265 (citation), q232 (unique); m06-l07-q349, q364 (style), q351 (key).

Re-cite (not dropped): m06-l08-q231 → `ms-edge-privacidad.html` (https://support.microsoft.com/es-es/edge/microsoft-edge-browsing-data-and-privacy).
If the coordinator does not save that page, add
`m06-l08-q231	VI.8	followup-2026-11	citation	key «contraseñas… al cerrar todas las ventanas» no longer on live ms-edge-inprivate.html`.

Lesson places needing a replacement (3, all m06-l08 «InPrivate» row): 86-87 (changed label), 87-89 (changed; new
page or fallback), 89-90 (delete). Edits to kept questions, no drop: q037 and q043 explanation quotes; q039 and q365
label case; q041, q043 and q350 citation headings; `source_quote` of q037, q041, q043, q348.

With 9 of 10 kept InPrivate questions dropped, VI.8 keeps only q231 (if re-cited) on InPrivate. The live page now supports
the path (without its label), the summary list of what is not saved, and «guardar descargas y favoritos».
