# C2 currency audit (R2b part C) — saved pages that changed live

- Verifier: blind verifier (Claude Opus 5.5), read-only except this report.
- Date: 2026-11-06.
- Method: `docs/age-verification/tools/check_pages.py` compared the visible `<main>` text of each saved page under
  `content/age-auxiliar-c2/sources/otros/` with a live copy fetched today (scripts stripped on both sides). Ten pages
  differ; their diffs are in `pages-live/<file>.diff` (`-` stored, `+` live). For each page the change was classified
  from the diff, every C2 place citing the file was found by searching `es/lessons/*.md` and `glossary.yaml` for the
  file name (also `excerpts.json`, `source-index.json`, `exercises/`: no hits), and each place was checked against the
  live copy: PASS when the live page still states the fact with every quoted label in the same words. Bloque II
  places were also checked for a page that applies to Windows 11 / Microsoft 365 desktop. The C1 report
  (`docs/age-verification/audit-2026-11/pages.md`) was read only after the verdicts were set.
- Extractor note: the `<main>` text extractor drops content inside collapsed tab/expander panels. On
  `ms-copilot-introduccion.html` the note «La aplicación Microsoft 365 Copilot ahora se denomina Microsoft Copilot.»
  sits inside `<main>` (live HTML lines 826-929) but is absent from the extracted text; it was checked in the raw
  live HTML. A «same text» result from the tool therefore says nothing about such panels.
- «Fuentes» list items: PASS means the file still exists live under the same URL and title. Their «consultado el»
  dates are not judged here.

## 1. `ms-copilot-introduccion.html`

Change: structure. A new paragraph on the «Inicio» tab (Chat and Cowork; «Cowork y Code requieren una licencia de
Microsoft 365 Copilot…») and a «Nota» heading; the «Comparar licencias» heading moves. No cited sentence changed.

| Place (lesson:line or glossary id) | Verdict | Live passage / note | Replacement |
|---|---|---|---|
| m02-l06:102-104 («Qué es») | PASS | «Sin embargo, todas las experiencias están impulsadas por: Modelos de lenguaje de gran tamaño (LLM) para la comprensión y generación del lenguaje natural; Fundamentación en datos web u organizativos (Microsoft Graph y Work IQ)» | — |
| m02-l06:176 (Fuentes) | PASS | heading «Introducción a Microsoft Copilot», learn.microsoft.com | — |
| glossary `g-microsoft-copilot` | PASS | same LLM and grounding lines; «La aplicación Microsoft 365 Copilot ahora se denomina Microsoft Copilot.» (raw HTML, inside a collapsed panel; see extractor note). The entry gives «(Microsoft Graph)» where the page says «(Microsoft Graph y Work IQ)»: shorter, not wrong | — |

## 2. `ms-outlook-listas-contactos.html`

Change: wording of facts and structure. New Outlook and web: creation now goes through «la flecha angular v situado
junto a Nuevo contacto › Nueva lista de contactos» (was «Agregar a la lista» on a contact); new sections «Agregar más
contactos a una lista» and «Quitar contactos de una lista»; «Todas las listas de contactos» becomes «Sus listas de
contactos» with an Editar/Eliminar button on hover; several labels re-cased («Guardar & Cerrar» → «Guardar & cerrar»,
«la versión clásica de Outlook» → «Outlook clásico»).

No C2 place cites the undated file (`fuentes.yaml`: `lessons: []`). The places on this URL cite
`ms-outlook-listas-contactos_2026-11-06.html`, whose extracted text is identical to today's live copy (0 diff lines),
so they were checked against the live page here.

| Place (lesson:line or glossary id) | Verdict | Live passage / note | Replacement |
|---|---|---|---|
| m02-l11:133-135 («Grupo de contactos», via `_2026-11-06` copy) | PASS | «En Outlook clásico, en el panel lateral, seleccione :People. Seleccione Nuevo grupo de contactos en la cinta de opciones. … seleccione Agregar miembros»; «las "listas de contactos" se conocen anteriormente como "grupos de contactos" en el Outlook clásico»; «Los contactos no se eliminan, solo la lista de contactos.» | — |
| m02-l11:136-137 («Editar un grupo de contactos», via `_2026-11-06` copy) | PASS | «haga doble clic en el grupo para abrirlo. En la cinta de opciones, seleccione Agregar o quitar miembros. Cuando haya terminado de actualizar, seleccione Guardar & cerrar.» | — |
| m02-l11:220 (Fuentes, `_2026-11-06` copy) | PASS | title «Crear, editar o eliminar una lista de contactos (o grupo de contactos) en Outlook», support.microsoft.com | — |
| glossary `g-lista-de-contactos` (via `_2026-11-06` copy) | PASS | «Una lista de contactos es una colección de contactos y direcciones de correo electrónico que es muy útil para enviar mensajes de correo electrónico a un grupo de personas.»; grupo de contactos in Outlook clásico as above | — |

Note: the undated file is orphaned and its `fuentes.yaml` line still reads «live check pending (403 on 2026-11-05)»; it
now differs from live by 100 lines.

## 3. `dominios-es-sobre-nosotros.html`

Change: label/translation. The related-links heading «También te puede interesar» is served in English («You may also
be interested in»).

| Place (lesson:line or glossary id) | Verdict | Live passage / note | Replacement |
|---|---|---|---|
| — | — | no C2 lesson or glossary entry cites the file (`fuentes.yaml`: `lessons: []`) | — |

## 4. `ms-copilot-windows.html`

Change: structure. A «Nota» is added: «Inicio, el nuevo punto de inicio de Copilot donde se unen Chat y Cowork, todavía
se está implementando…». No cited sentence changed.

| Place (lesson:line or glossary id) | Verdict | Live passage / note | Replacement |
|---|---|---|---|
| m02-l06:100-101 («Abrir Copilot») | PASS | «Presione la tecla Copilot del teclado. Use el método abreviado de teclado Windows tecla + C.»; «En equipos nuevos con Windows 11, la aplicación Copilot ya debería estar instalada de forma predeterminada. Puede encontrar la aplicación Copilot anclada a la barra de tareas o en el menú Inicio.» | — |
| m02-l06:105-106 («Quién lo ofrece») | PASS | «Si la aplicación Copilot aún no está en su PC Windows, descárguela de la Microsoft Store.»; the page names it «la aplicación Microsoft Copilot» | — |
| m02-l06:174 (Fuentes) | PASS | title «Acceso a Microsoft Copilot en Windows», support.microsoft.com | — |

## 5. `ms-excel-copilot.html`

Change: wording of facts. «También puede grabar una aptitud demostrando una tarea en el libro» added; the Detener
button moves from «la esquina inferior derecha» to «el lado derecho» of the chat input.

| Place (lesson:line or glossary id) | Verdict | Live passage / note | Replacement |
|---|---|---|---|
| — | — | no C2 lesson or glossary entry cites the file (`fuentes.yaml`: `lessons: []`) | — |

## 6. `ms-excel-ordenar.html`

Change: structure. A new section «Más información sobre los criterios de ordenación» (ascending-order table: números,
fechas, texto, valores lógicos, errores, celdas en blanco; «Los criterios de ordenación varían según la configuración
regional») is added above the Windows/Web tabs. Nothing removed.

| Place (lesson:line or glossary id) | Verdict | Live passage / note | Replacement |
|---|---|---|---|
| m02-l09:127-128 («Ordenar») | PASS | Windows tab: «En la ficha Datos, en el grupo Ordenar y filtrar…»; «Si no lo hace, los números almacenados como números se ordenarán antes que los números almacenados como texto.» The lesson says «guardados» for the page's «almacenados»: a paraphrase, no quoted label | — |
| m02-l09:225 (Fuentes) | PASS | title «Ordenar datos de una tabla o un rango en Excel», support.microsoft.com | — |

## 7. `ms-win-directivas-explorador.html`

Change: dates. «Se actualizó por última vez el 2025-03-12» → «2026-10-14». Nothing else.

| Place (lesson:line or glossary id) | Verdict | Live passage / note | Replacement |
|---|---|---|---|
| m02-l06:62-65 («Papelera de reciclaje») | PASS | NoRecycleFiles, «Nombre descriptivo — No mover archivos eliminados a la papelera de reciclaje»; «Si habilita esta configuración, los archivos y carpetas que se eliminan mediante Explorador de archivos no se colocarán en la Papelera de reciclaje y, por tanto, se eliminarán permanentemente.» Applies to «Windows 11, versión 21H2 [10.0.22000] y versiones posteriores» | — |
| m02-l06:162 (Fuentes) | PASS | «CSP de directiva de ADMX_WindowsExplorer», learn.microsoft.com | — |
| m02-l07:34-37 («Papelera de reciclaje») | PASS | same passage as m02-l06:62-65 | — |
| m02-l07:160 (Fuentes) | PASS | as m02-l06:162 | — |

## 8. `pag-oficina-informacion.html`

Change: wording of facts. «sin necesidad de cita previa, tanto para información como para registro en clave» becomes
«sin necesidad de cita previa» plus a new block «Cita previa opcional para registro en Cl@ve» (documents to bring, in
person only); hours become «De lunes a viernes laborables de 9:00 a 14:30 h.»

| Place (lesson:line or glossary id) | Verdict | Live passage / note | Replacement |
|---|---|---|---|
| m02-l04:349-352 (Oficina del PAG) | PASS | «Nuestra Oficina de Información y Atención a la Ciudadanía»; «Dirección: Calle Francisco Gervás, 7. 28020 - Madrid». The lesson does not use the appointment or hours sentences | — |
| m02-l04:400-401 («Otras fuentes» list) | PASS | page still served at the same URL with the same title | — |

## 9. `whatwg-html-introduccion.html`

Change: dates. «Last Updated 16 October 2026» → «5 November 2026». Nothing else.

| Place (lesson:line or glossary id) | Verdict | Live passage / note | Replacement |
|---|---|---|---|
| m02-l12:12-15 («World Wide Web y HTML») | PASS | «For its first five years (1990-1995), HTML went through a number of revisions and experienced a number of extensions, primarily hosted first at CERN, and then at the IETF.» | — |
| m02-l12:63-64 («JavaScript», first sentence) | PASS | «Scripts (typically in JavaScript) are small programs that can be embedded using the script element…»; «inline client-side scripts»; «the browser will generally run the script uninterrupted» | — |
| m02-l12:152 (Fuentes) | PASS | «HTML Standard: 1 Introduction», html.spec.whatwg.org | — |

## 10. `whatwg-html-scripting.html`

Change: dates and wording of spec algorithms. «Last Updated» date; a new «intended document» concept in the script
preparation algorithm; XSLT note «its parser document» → «their parser document and intended document»; noscript text
«context element» → «target», «scripting mode was Disabled» → «scripting was disabled». None of it touches the
section's introduction.

| Place (lesson:line or glossary id) | Verdict | Live passage / note | Replacement |
|---|---|---|---|
| m02-l12:64-65 («JavaScript», second sentence) | PASS | «Scripts allow authors to add interactivity to their documents. … and many users disable scripting.» | — |
| m02-l12:166 (Fuentes) | PASS | «HTML Standard: 4.12 Scripting», html.spec.whatwg.org | — |

## Summary

| Page | Change class | Places | PASS | FAIL |
|---|---|---|---|---|
| ms-copilot-introduccion.html | structure | 3 | 3 | 0 |
| ms-outlook-listas-contactos.html | wording of facts, structure | 4 (all via `_2026-11-06` copy; undated file has 0) | 4 | 0 |
| dominios-es-sobre-nosotros.html | label/translation (related links) | 0 | 0 | 0 |
| ms-copilot-windows.html | structure (added note) | 3 | 3 | 0 |
| ms-excel-copilot.html | wording of facts | 0 | 0 | 0 |
| ms-excel-ordenar.html | structure (added section) | 2 | 2 | 0 |
| ms-win-directivas-explorador.html | dates | 4 | 4 | 0 |
| pag-oficina-informacion.html | wording of facts | 2 | 2 | 0 |
| whatwg-html-introduccion.html | dates | 3 | 3 | 0 |
| whatwg-html-scripting.html | dates, wording of spec algorithms | 2 | 2 | 0 |
| **Total** | | **23** | **23** | **0** |

## Checked by the coordinator (not read by `check_pages.py`)

- `transparencia-v-plan.html`: the download URL gives 404; its `url_actual`
  (`…/planes-accion/VPlan/vplan`, recorded on 2026-11-05) gives 200 and the same visible text (71 of 71 blocks).
- `boe-analisis-ce.xml`: the open-data API answers 400 without `Accept: application/xml`. With it: 17 references
  (16 stored); new BOE-A-2026-22710 (Declaración 1/2026 del TC), and the two older TC declarations now read «SE DICTA …
  por Declaración 1/2004» / «de 1 de julio de 1992» for «SE DECLARA …». Same change as C1's run of 2026-11-05. The
  only C2 place resting on the file after R2b is m02-l01 (art. 49 has the wording of the reform of 15-02-2024): the
  reform entries are unchanged. PASS.
- Re-tries for HTTP 403 (browser, 20 s then 60 s between fetches; `pages-live-retry/`, `pages-live-retry2/`): 7 of
  8 read, all same text. `consilium-presidencia.html` still 403 (saved on 2026-11-06 in R2 with the e2e browser and a
  wait for network idle; no live check this run).
- Extractor note: `html_blocks` skips any `div`/`section` whose id contains «copilot» (`_FURNITURE` in
  `backend/src/tradeschool/citations/excerpts.py`, meant for Microsoft's Ask-Copilot widget). On Copilot pages it
  also drops content tab panels (`tabpanel_1_microsoft-365-copilot-basic` …), so «same text» does not cover them:
  `ms-copilot-introduccion.html`'s note on the renaming was checked in the raw HTML (PASS above). Open item, not
  patched in this round (changing it moves C1 excerpts).
