# Blind verification of the coverage fix — m06-l02 (2026-10-17)

Spec: `fix-spec.md` («Verifier» and «Rule change»: no word ceiling; restorations allowed, plus the coordinator's two
named items). Inputs: `fix-m06-l02.md` (writer's claims), `m06-l02.md` (coverage report), `fixes.md` rows 2025 A 47,
2024 X 48, 2024 X 51. Lesson as it now stands: `content/age-administrativo-c1/es/lessons/m06-l02.md` (compared with
`git diff HEAD`). Pages read with `pagetext.py`. Exam texts read from `sources/examenes-oficiales/`.

## Changes

| # | Change | Check | PASS/FAIL | Reason | Replacement |
|---|---|---|---|---|---|
| 1 | Búsqueda: «busca en el dispositivo (aplicaciones, configuraciones y archivos)» | literal on page | PASS | `ms-win-busqueda-privacidad.html`: «Tu dispositivo (incluyendo aplicaciones, configuraciones y archivos)»; «configuraciones» as printed | — |
| 1 | 2025 A 47 now stated | fact asked | PASS | Key c: web, apps, settings, files, plus OneDrive, SharePoint, Outlook, Bing; the item now names all of them, which rules out a, b and d | — |
| 2 | New item «Idiomas»: path «Configuración › Hora & idioma › Idioma & región» | literal on page | PASS | «Seleccione Inicio y elija Configuración .» / «Selecciona Hora & idioma y elige Idioma & región .» («&» as printed; Windows 11 section) | — |
| 2 | «Windows puede tener varios idiomas instalados» | literal on page | PASS | «el orden preferido actual de los idiomas instalados se muestra en Idiomas preferidos»; «qué idiomas están instalados actualmente» | — |
| 2 | «El idioma para mostrar determina el de la interfaz de usuario» | literal on page | PASS | «El idioma para mostrar de Windows determina el idioma que usa la interfaz de usuario de Windows.» | — |
| 2 | «la distribución del teclado puede ser de otro idioma» | literal on page | PASS | «El idioma de visualización actual de Windows podría tener la distribución del teclado del teclado deseado en un idioma diferente.» | — |
| 2 | 2024 X 48 now stated | fact asked | PASS | Key d (several languages; display, voice and keyboard may differ). Several languages rules out b; keyboard in another language rules out a and c. The voice part is correctly left out: the page says «Asegúrese de que el idioma en el que se va a usar la voz está establecido como idioma para mostrar» | — |
| 3 | New item «Registro»: «base de datos jerárquica central; contiene información que Windows consulta continuamente, como los perfiles de cada usuario, las aplicaciones instaladas y qué hardware existe en el sistema» | literal on page | PASS | `ms-win-registro.html`: «Una base de datos jerárquica central…»; «El Registro contiene información que Windows consulta continuamente durante el funcionamiento, como perfiles para cada usuario, las aplicaciones instaladas en el equipo … qué hardware existe en el sistema» | — |
| 3 | 2024 X 51 now stated | fact asked | PASS | Key a: «configuración del sistema, el hardware y las aplicaciones instaladas». Hardware and installed apps are named, which rules out b, c and d. Optional, not required: the page's own clause «sirve para almacenar información necesaria para configurar el sistema» would echo the key's «configuración» | — |
| 4 | Restoration: Varias pantallas «resolución y diseño; la orientación, en «Escala y diseño»» | literal; exam row | PASS | «puede cambiar la configuración, como la resolución, el diseño de pantalla y mucho más» / «vaya a Escala y diseño, a continuación elija suOrientación de Pantalla»; per screen: «puede ajustar la configuración de cada una de ellas». Exam row 2024 A 66 (index line 106) | — |
| 5 | Restoration (coordinator): «Barra espaciadora marca una casilla; Esc descarta el cuadro» | literal on page | PASS | `ms-win-atajos.html` dialog table: «Barra espaciadora — Si la opción activa es una casilla, activarla o desactivarla.»; «Esc o Escape — … o descartar un cuadro de diálogo.» | — |
| 6 | Restoration (coordinator): «Clic derecho en un área vacía del escritorio › Ver: iconos grandes, medianos o pequeños; desactivar Mostrar iconos del escritorio los oculta» | literal on page | PASS | `ms-win-iconos-escritorio.html`: «Haga clic con el botón derecho en un área vacía del escritorio. / Selecciona Ver y elige entre iconos grandes, medianos o pequeños»; «Selecciona Ver y después desactiva Mostrar iconos del escritorio. Esto ocultará temporalmente todos los iconos» | — |
| 7 | Restorations not made (Otros usuarios, Foco/Concentración, Reconocimiento de voz line, Windows+L, Ctrl+Alt+Supr, Copilot Chat, Copilot permissions, Windows+X, Alt+arrastrar, carpetas junto al botón de encendido, «Resumir un archivo», Cambiar de ventana parenthetical) | rule change | PASS | 2024 X 49, 2020 X 46 and the 2020 50 voice part are `función retirada`; the rest have no index row (Alt+Tab is in the VI.2 «never asked» list). Narrador and the Impr Pant descriptions are already in the lesson | — |
| 8 | First-pass cuts undone | no cut remains | PASS | `git diff HEAD` shows only additions; Ajustar ventanas path, «Enviar a › Escritorio», the `ms-win-recortes.html` Impr Pant sentence and the Copilot install/button details are in place | — |

## New sources

| File | sha256 vs fix notes | Official, Spanish | Final URL | Re-download | PASS/FAIL |
|---|---|---|---|---|---|
| `ms-win-idioma.html` | match (`e3b5934a…`) | support.microsoft.com, `lang="es-ES"` | canonical = recorded URL | fetched 2026-10-17: HTTP 200, same final URL; bytes differ (page chrome), extracted text identical (492 lines, empty diff) | PASS |
| `ms-win-registro.html` | match (`8e5c56b0…`) | learn.microsoft.com, `lang="es-es"` | canonical = recorded URL | fetched 2026-10-17: HTTP 200, same final URL, byte-identical (same sha256) | PASS |

Neither file is in `fuentes.yaml` yet (expected; coordinator merges). Note for the ledger: `ms-win-registro.html` is a
Windows Server troubleshooting page quoting the Microsoft Computer Dictionary definition (Windows 98–2000); the item
uses only the general «El Registro contiene información…» sentence, so it fits the «Files resting on non-UI sources»
list rather than a Windows 11 UI page.

## Covered rows re-checked against the lesson as it stands

All 16 rows marked `covered` in `m06-l02.md` still have their text in the lesson (centro de notificaciones, Copilot LLM,
Inicio centrado, Copilot frente a buscador, Windows+Impr Pant, Narrador, Extender, cada pantalla por separado, Anclados,
Windows Hello, Windows+D, Restaurar, «En todos los escritorios», Ctrl+Esc, Lupa Windows+signo más, acceso directo). The
partial row (2025 A 47) and the two misses (2024 X 48, 2024 X 51) are now covered. Nothing asked 2022–2025 was cut.

## Form

| Check | PASS/FAIL | Note |
|---|---|---|
| Words | PASS | `wc -w` 1,645, as claimed; no ceiling under the rule change |
| Lines ≤ 120 | PASS | only line 1 (`#` title, unchanged from HEAD) is longer |
| Fuentes | PASS | `fuentes_order.py`: nothing missing, nothing uncited, in order; titles match the pages' `<title>` |
| List-shape hygiene | PASS | no `-`, `*` or `1.` after sentence punctuation mid-line |
| Item shape | PASS | new items three lines; longest items (four lines) predate this fix |
| Voice | PASS | no fillers, triads, rhetorical questions or closers; labels as printed («Hora & idioma», «Idioma & región», «Escala y diseño») |
| LQMC | PASS | exactly ten lines, unchanged |

## Counts

- Checks: 14 change rows, 2 source rows, 1 coverage re-check, 7 form rows = 24.
- PASS: 24. FAIL: 0.
