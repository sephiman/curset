# Blind verification of the coverage fix — m06-l03 (2026-10-17)

Spec: `fix-spec.md` («Verifier» and «Rule change»: no word ceiling; restorations allowed). Inputs: `fix-m06-l03.md`
(writer's claims), `m06-l03.md` (coverage report), `fixes.md` rows 2025 X 50, 2024 X 57, 2025 A 50. Lesson as it now
stands: `content/age-administrativo-c1/es/lessons/m06-l03.md` (compared with `git diff HEAD`). Pages read with
`pagetext.py`.

## Changes

| # | Change | Check | PASS/FAIL | Reason | Replacement |
|---|---|---|---|---|---|
| 1a | Papelera item: «los archivos de OneDrive eliminados de la nube no aparecen en la Papelera de reciclaje del equipo» (restoration R2) | literal on page | PASS | `ms-onedrive-restaurar.html`: «Los Files eliminados de la nube, incluidos los marcados como solo en línea ( ), no aparecen en la Papelera de reciclaje ni en la Papelera del equipo.» The lesson keeps the PC half of the sentence. That is a true subset. | — |
| 1b | Papelera item: «Con la directiva «No mover archivos eliminados a la papelera de reciclaje» habilitada, lo que eliminas en el Explorador de archivos no va a la Papelera y se elimina permanentemente» | literal on page | PASS | `ms-win-directivas-explorador.html` (NoRecycleFiles): «Si habilita esta configuración, los archivos y carpetas que se eliminan mediante Explorador de archivos no se colocarán en la Papelera de reciclaje y, por tanto, se eliminarán permanentemente.»; «Nombre descriptivo / No mover archivos eliminados a la papelera de reciclaje». «Se elimina permanentemente» is printed and limited to Explorer deletions, as the item says. The label is lower-case «papelera» as printed. The source is MDM/ADMX admin documentation, so it goes on the ledger's «Files resting on non-UI sources», as the writer notes. | — |
| 1c | 2025 X 50 now stated | fact asked | PASS | Key (a): not recoverable from a drive set not to use the Papelera, or after Mayús+Supr. The lesson now gives Mayús+Supr plus a documented setting that sends Explorer deletions past the Papelera for good. The per-drive property («Quitar los archivos inmediatamente al eliminarlos») has no official page. The writer recorded it as sin fuente oficial, and I did not search again. | — |
| 1d | LQMC: «…; con la directiva «No mover archivos eliminados a la papelera de reciclaje», lo eliminado tampoco va a la Papelera» | literal on page | **FAIL** | The policy covers only what is deleted «mediante Explorador de archivos», and only when it is enabled. «Lo eliminado» with no scope says more than the page does, and the line drops «habilitada». | «Mayús+Supr elimina sin pasar por la Papelera de reciclaje (fuente: `ms-win-atajos.html`); con la directiva «No mover archivos eliminados a la papelera de reciclaje» habilitada, lo que eliminas en el Explorador tampoco va a la Papelera (fuente: `ms-win-directivas-explorador.html`).» |
| 2a | Buscar en Windows: «Las ubicaciones de búsqueda incluyen o excluyen carpetas concretas; con la búsqueda de contenido en la nube activada, Windows Search muestra elementos de tu OneDrive personal» | literal on page | PASS | `ms-win-busqueda-privacidad.html`: «También puede personalizar las ubicaciones de búsqueda para incluir o excluir carpetas específicas.»; «Si activa la configuración de la cuenta de Microsoft para la búsqueda de contenido en la nube, Windows Search mostrará los resultados de los elementos de su OneDrive personal, Outlook y otros servicios Microsoft.» | — |
| 2b | «Desde Inicio del Explorador se busca en el PC y en la nube, con las cuentas en la nube iniciadas en «Configuración › Cuentas»» (restoration R3) | literal on page | PASS | `ms-win-explorador.html`: «Para buscar archivos relevantes desde el PC y la nube, busque desde Inicio del Explorador de archivos.»; «Inicie sesión en sus cuentas en la nube desde Inicio>Configuración>Cuentas para habilitar la búsqueda en la nube.» The lesson drops the Start-menu «Inicio» from the path. That avoids two senses of «Inicio» in one sentence, and «Configuración › Cuentas» is printed in that order. | — |
| 2c | LQMC: «…; con la búsqueda de contenido en la nube, Windows Search muestra elementos de OneDrive» | literal on page | PASS | Same passage as 2a. Two sources are cited, one per clause. | — |
| 2d | 2024 X 57 now stated | fact asked | PASS | Key (b): locations can be customised, OneDrive included. The lesson now states customisable locations (include or exclude) and OneDrive results through cloud search. No saved page says a OneDrive folder can be added as an indexed location, and the writer notes this. The lesson states no more than the pages. | — |
| 3a | Asistencia rápida: «Conexión remota: quien ayuda comparte un código de 6 dígitos y puede ver la pantalla del equipo o controlarlo, si lo permites; para el control total selecciona «Solicitar control»» | literal on page | PASS | `ms-win-asistencia-rapida.html`: «Asistencia rápida utiliza una conexión remota, […] ya que pueden ver la pantalla del equipo o controlar el equipo (si lo permites).»; «Selecciona Ayudar a alguien y comparte el código de 6 dígitos»; «Si quieres solicitar el control total del equipo, selecciona Solicitar control». The wording problem is under Form, «Voice». | — |
| 3b | 2025 A 50 now stated | fact asked | PASS | Key (c): another person can access and control your device remotely. «Conexión remota», «ver la pantalla … o controlarlo» is now explicit. | — |
| R1 | Restoration: «Acerca de» contents (name and model; «Especificaciones de Windows»: edition, version; «Especificaciones del dispositivo»: processor, RAM, 32 or 64 bits) | literal; exam row | PASS | `ms-win-info-dispositivo.html`: «El nombre del dispositivo aparece en la página, con el nombre del modelo justo debajo.»; «En Especificaciones de Windows, comprueba qué edición y versión de Windows utiliza el dispositivo.»; «En Especificaciones del dispositivo, comprueba los detalles sobre el dispositivo, incluyendo: Tipo de procesador. Cantidad de RAM instalada. Si el dispositivo ejecuta una versión de Windows de 32 o 64 bits.» The same page prints the path plainly: «seleccione Sistema y elija Acerca de». Exam row: 2020 ord. 44 (index line 93, `vigente`, «Configuración: Sistema > Acerca de»). This cut is on the ledger list («m06-l03 … Acerca de contents»). | — |
| R- | Restorations not made: «Enviar a» destinations (2024 X 56) and the other R2 cuts | rule change | PASS | «Enviar a» destinations are on the ledger's «Sin fuente oficial» list (line 2930), so they stay out. I checked the other cuts in the writer notes' «Cuts made for length» against the index's Windows rows. None asks window parts, Ctrl+Mayús+1…9, ZIP formats, \\localhost, index details, Recortes/Paint/Calculadora/Reloj extras or msinfo32/MSConfig/compmgmt. The 2020 ord. 51 winver row is `función retirada`. `recheck-queue.md` has no fix-round cut for m06-l03. | — |
| C | No cuts | diff | PASS | `git diff HEAD` shows only additions and replacements in place. Every old fact is still in the lesson (the Asistencia «control total» clause is reworded, not removed). | — |

## New sources

| File | sha256 vs fix notes | Official, Spanish | Final URL / title | PASS/FAIL |
|---|---|---|---|---|
| `ms-win-directivas-explorador.html` | match (`9fdba5ad…`) | learn.microsoft.com, `lang="es-es"` | canonical = recorded URL; `<title>` «CSP de directiva de ADMX_WindowsExplorer» | PASS |
| `ms-win-info-dispositivo.html` | match (`a7cf8519…`) | support.microsoft.com, `lang="es-ES"` | canonical = recorded URL; `<title>` «Encontrar información sobre el dispositivo Windows» | PASS |
| `ms-win-busqueda-privacidad.html` (reused) | already indexed | support.microsoft.com | `fuentes.yaml` `lessons: [m06-l02]`; the coordinator adds m06-l03 | PASS |
| Re-download | — | — | `ms-win-directivas-explorador.html` re-fetched from its URL today: **byte-identical** (same sha256). The other re-download, `ms-word-seleccionar-objetos.html`, is in `verify-fix-m06-l04.md`. | PASS |

Neither new file is in `fuentes.yaml` yet. That is expected, because the coordinator merges.

## Covered rows re-checked against the lesson as it stands

All 12 rows marked `covered` in `m06-l03.md` still have their quoted text in the lesson: Ver/diseños, Visor de
eventos, Compartir (Conceder acceso a; «Compartir y Eliminar»), Grabadora de pasos/Recortes, Windows+E, Administrador
de tareas, indexación, Unidad de recuperación, Alt+Entrar, Historial de archivos, rutas UNC and «Ver › Mostrar». The
Asistencia rápida row (2025 A 50) is reworded and still covered. Both partial rows (2025 X 50, 2024 X 57) are now
stated as far as a saved page allows. Nothing asked in 2022–2025 was cut.

## Form

| Check | PASS/FAIL | Note |
|---|---|---|
| Words | PASS | `wc -w` 1,715, as claimed; there is no ceiling under the rule change |
| Lines ≤ 120 | PASS | Only line 1 (`#` title, unchanged) is longer |
| Fuentes | PASS | `fuentes_order.py`: nothing missing, nothing uncited, in order. Titles match the pages' `<title>` |
| List-shape hygiene | PASS | No `-`, `*` or `1.` after sentence punctuation mid-line |
| LQMC | PASS | Exactly ten lines |
| Item shape | PASS | «Buscar en Windows» is now seven lines with three sources. That is long but holds one feature, and the length rule is lifted |
| Voice | **FAIL** | Asistencia rápida: «quien ayuda … puede ver la pantalla del equipo o controlarlo, si lo permites; para el control total selecciona «Solicitar control»». The «tú» changes person inside one sentence: «permites» is the person helped, «selecciona» is the helper, and «del equipo» has no owner. Replacement: «- **Asistencia rápida**: Ctrl+Windows+Q. Usa una conexión remota: quien ayuda comparte un código de 6 dígitos y, si la otra persona lo permite, ve su pantalla o controla su equipo; el control total se pide con «Solicitar control» (fuente: `ms-win-asistencia-rapida.html`).» Every clause stays on the page (see 3a). |

## Counts

- Checks: 13 change rows, 4 source rows, 1 coverage re-check, 7 form rows = 25.
- PASS: 23. FAIL: 2 (1d LQMC Papelera line overgeneralises the policy; Voice: Asistencia rápida switches addressee).
