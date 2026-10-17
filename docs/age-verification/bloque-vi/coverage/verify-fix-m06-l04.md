# Blind verification of the coverage fix — m06-l04 (2026-10-17)

Spec: `fix-spec.md` («Verifier» and «Rule change»: no word ceiling; restorations allowed). Inputs: `fix-m06-l04.md`
(writer's claims), `m06-l04.md` (coverage report), `fixes.md` rows 2025 X 51, 2025 X 53, 2022 X 52, 2022 X 56,
2024 A 53. Lesson as it now stands: `content/age-administrativo-c1/es/lessons/m06-l04.md` (compared with
`git diff HEAD`). Pages read with `pagetext.py`.

## Changes

| # | Change | Check | PASS/FAIL | Reason | Replacement |
|---|---|---|---|---|---|
| 1a | Ortografía: «Si marca como incorrecta una palabra escrita como quieres, «Agregar al diccionario» hace que no vuelva a marcarla» | literal on page | PASS | `ms-office-ortografia.html` (Windows tab): «Si Office marca como incorrectas palabras que están escritas de la manera que usted quiere, seleccione Agregar al diccionario para que Office no las vuelva a marcar como incorrectas.» | — |
| 1b | LQMC: «…; «Agregar al diccionario» evita que vuelva a marcar una palabra bien escrita» | literal on page | PASS | Same passage | — |
| 1c | 2025 X 51 now stated | fact asked | PASS | The red underline and the dictionary are now both in the item. On the saved page, the literal «palabra que no está en el diccionario» for Word desktop is missing (no «no reconoce» or «no está en el diccionario» in `ms-office-ortografia.html`). The writer records it as sin fuente oficial: only a Web tab on another page says it. I agree. | — |
| 2a | Coautoría: «guarda el documento en OneDrive o SharePoint y compártelo para trabajar en él a la vez» | literal on page | PASS | `ms-word-coautoria-documentos.html` («Se aplica a» Word para Microsoft 365, 2024, 2021): «Guarde el documento en OneDrive o SharePoint y compártalo con otros usuarios para que pueda trabajar en él al mismo tiempo.» | — |
| 2b | 2025 X 53 now stated | fact asked | PASS | The cloud storage half of the key is now stated. The version-history half is already in the separate «Historial de versiones» item, and the key is disputed in the ledger. | — |
| 3a | New item «Nuevo comentario»: «Revisar › Nuevo comentario», Ctrl+Alt+M or right-click › Nuevo comentario | literal on page | PASS | `ms-word-comentarios.html`: «En la pestaña Revisar , seleccione Nuevo comentario.»; «Presiona Ctrl + Alt + M.»; «Haga clic con el botón derecho en cualquier texto y seleccione Nuevo comentario en el menú contextual.» The path is printed plainly. | — |
| 3b | Ctrl+Alt+M removed from «Sinónimos y mayúsculas» | no fact lost | PASS | The shortcut moved into the new item, cited to a page that prints it | — |
| 3c | 2022 X 52 now stated | fact asked | PASS | Annulled row; the ribbon path is now given | — |
| 4 | Contar palabras, characters with and without spaces: no change (sin fuente oficial) | sin fuente | PASS | `ms-word-contar-palabras.html` has no «espacio» at all. The ledger's sin fuente list is unchanged. | — |
| 5a | QAT: «accesos directos a los comandos que usas con frecuencia (fuente: `ms-office-barra-acceso-rapido-teclado.html`), independientes de la pestaña activa» | literal on page | PASS | Keyboard page: «una colección de accesos directos a las características, opciones, comandos o grupos de opciones que usa con frecuencia»; main page: «un conjunto de comandos que son independientes de la pestaña que se muestra actualmente». «Accesos directos» does not auto-link to g-acceso-directo, because m06-l04 is in its `link_except`. | — |
| 5b | QAT: «por defecto encima de la cinta» kept, in an item that now also cites the keyboard page | no contradiction left unstated | **FAIL** | The two cited pages disagree on the default position. `ms-office-barra-acceso-rapido.html`: «Encima de la cinta de opciones, en la barra de título (ubicación predeterminada)». `ms-office-barra-acceso-rapido-teclado.html`, cited in the same item, says: «De forma predeterminada, la barra de herramientas está oculta debajo de la cinta de opciones en las aplicaciones de Microsoft 365» and «debajo de la cinta (la ubicación predeterminada)». The lesson states one side and does not say that a cited page contradicts it. The writer's note («does not cite the keyboard page for the position») does not help a reader, who sees both citations on one item. The position is not what 2024 A 53 asked. | Drop the default: «…independientes de la pestaña activa; va encima de la cinta, en la barra de título, o debajo de ella. Clic derecho en un comando › Agregar a la barra de herramientas de acceso rápido (fuente: `ms-office-barra-acceso-rapido.html`).» Or keep it and state the conflict: «…; «Personalizar la barra de herramientas de acceso rápido» la sitúa por defecto encima de la cinta y «Usar un teclado para personalizar…», oculta debajo.» |
| 5c | LQMC: «reúne los comandos que usas con frecuencia, independientes de la pestaña activa» | literal on page | PASS | Same passages as 5a. The line states no position. 2024 A 53 (key c: quick access to frequently used commands) is now stated literally. | — |
| R1 | Restoration: item «Seleccionar»: «Inicio › Seleccionar» offers Seleccionar todo, Seleccionar objetos (ocultos, apilados o detrás del texto), Seleccionar todo el texto con formato similar, Panel de selección | literal; garbled path; exam row | PASS | `ms-word-seleccionar-objetos.html`: «vaya aSeleccionarinicio> y siga uno de estos procedimientos: / Para seleccionar todo el texto del documento, elija Seleccionar todo. / Para seleccionar objetos que están ocultos, apilados o detrás del texto, elija Seleccionar objetos. / … elija Seleccionar todo el texto con formato similar. / … seleccione Panel de selección». **Path decode:** both labels are on the page («Seleccionar», «inicio»). The garble is the same shape as the accepted «Multitarea del sistema>» → «Sistema › Multitarea» (last label first). Other saved pages print the tab-first order with «Inicio» plainly: `ms-word-indice.html` «ve a Inicio>Mostrar u ocultar», `ms-word-transcribir.html` «Ir a Inicio>Dictar>Transcripción», `ms-word-ajustar-imagenes.html` «Inicio>Panel de selección». The en-us page, downloaded today and not saved, prints «go to Home > Select». The ledger's garbled-path rule is met. Exam row: 2020 extr. 52 (index line 131, `vigente`, «Inicio > Edición > Seleccionar»). The page does not print «Edición», so the lesson rightly leaves it out. The coordinator adds this path to the ledger's «Paths decoded from garbled strings». | — |
| R2 | Restoration: item «Opciones de impresión» (six options, Opciones de Word (Mostrar)) | literal; exam row | PASS | `ms-word-opciones-mostrar.html`: heading «Opciones de impresión», then «Imprimir dibujos creados en Word», «Imprimir imágenes y colores de fondo», «Imprimir propiedades del documento», «Imprimir texto oculto», «Actualizar campos antes de imprimir», «Actualizar los datos vinculados antes de imprimir». Exam row: 2020 ord. 53 (index line 126, `anulada`; annulled rows count under v1.5). The cut is on the ledger list. | — |
| R- | Restorations not made: cursiva (2025 A 51), note text on hover (2025 A 52), the other R2 cuts | rule change | PASS | Cursiva and hover are on the ledger's «Sin fuente oficial» list (lines 2933–2935). Macros' «Vista» tab was dropped as «label not confirmed», not for length, so it does not come back. I checked the other cuts in the writer notes («Cuts made for length») against the index's Word rows, and no row asks them. «Formato de imagen» pane tabs (2020 52) were never written (no page). | — |
| C | No cuts | diff | PASS | `git diff HEAD`: additions, the Ctrl+Alt+M move (3b) and the Fuentes reorder only | — |

## New sources

| File | sha256 vs fix notes | Official, Spanish | Final URL / title | PASS/FAIL |
|---|---|---|---|---|
| `ms-word-comentarios.html` | match (`5ef955f3…`) | support.microsoft.com, `lang="es-ES"` | canonical = recorded URL; `<title>` «Uso de comentarios modernos en Word» | PASS |
| `ms-word-coautoria-documentos.html` | match (`ebd5f179…`) | support.microsoft.com, `lang="es-ES"` | canonical = recorded URL; `<title>` «Coautoría de documentos» | PASS |
| `ms-word-seleccionar-objetos.html` | match (`dc03a3b9…`) | support.microsoft.com, `lang="es-ES"` | canonical = recorded URL; `<title>` «Seleccionar una forma u otro objeto de Word» | PASS |
| `ms-office-barra-acceso-rapido-teclado.html` | match (`deb29f06…`) | support.microsoft.com, `lang="es-ES"` | canonical = recorded URL; `<title>` «Usar un teclado para personalizar la barra de herramientas de acceso rápido» | PASS |
| Re-download | — | — | I re-fetched `ms-word-seleccionar-objetos.html` and `ms-office-barra-acceso-rapido-teclado.html` today. Both give **identical extracted text** (`pagetext.py` diff empty). The sha256 differs, which is the usual page-chrome churn on support.microsoft.com. | PASS |

None of the four new files is in `fuentes.yaml` yet. That is expected, because the coordinator merges.

## Covered rows re-checked against the lesson as it stands

All 17 rows marked `covered` in `m06-l04.md` still have their quoted text in the lesson: Transcribir, Imprimir
documento con revisiones, anclaje/«Mover con texto», Combinar correspondencia, .dotm (both rows), barra de estado,
QAT/«Agregar a la barra…», estilos/tabla de contenido, Insertar índice, Recorte de pantalla, «Mostrar u ocultar ¶»,
Sugerencias de teclas, Mayús+F7, Lectura en voz alta, Traducir and Mayús+F3. Three of the four partial rows are now
stated (2025 X 51 as far as a page allows, 2025 X 53, 2022 X 52). 2022 X 56 stays sin fuente oficial. Nothing asked in
2022–2025 was cut.

## Form

| Check | PASS/FAIL | Note |
|---|---|---|
| Words | PASS | `wc -w` 1,686, as claimed; there is no ceiling under the rule change |
| Lines ≤ 120 | PASS | Only line 1 (`#` title, unchanged) is longer |
| Fuentes | PASS | `fuentes_order.py`: nothing missing, nothing uncited, in order (`ms-word-opciones-mostrar.html` moved up to its new first citation). Titles match the pages' `<title>` |
| List-shape hygiene | PASS | No `-`, `*` or `1.` after sentence punctuation mid-line |
| LQMC | PASS | Exactly ten lines |
| Item shape | PASS | New items are 2–3 lines. «Opciones de impresión» lists six labels as printed. It is a list of UI labels, not a rhetorical triad |
| Voice | PASS | «tú» throughout («guarda … y compártelo», «usas»). No fillers, questions or closers. No invented terms |

## Counts

- Checks: 16 change rows, 5 source rows, 1 coverage re-check, 7 form rows = 29.
- PASS: 28. FAIL: 1 (5b QAT default position: the lesson says «encima» while the cited keyboard page says «debajo»,
  without saying so).
