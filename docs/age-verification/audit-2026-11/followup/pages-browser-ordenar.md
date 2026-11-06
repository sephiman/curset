# Part P follow-up — `ms-excel-ordenar.html` (browser fetch, 2026-11-06)

Blind verifier, `spec.md` Part P, five checks of `bank/bloque-vi/verify-spec.md` against the live page.
Live copy: Playwright Chromium rendered DOM, 2026-11-06 (scratchpad `pages-browser-live/ms-excel-ordenar.html`).
Text extracted from both copies and diffed in full (not only `<main>`): the only content change is the added block
«Más información sobre los criterios de ordenación» (table Números / Fechas / Texto / Valores lógicos / Valores de error /
Celdas en blanco, plus «Nota: Los criterios de ordenación varían según la configuración regional.»). Every other
sentence of the stored page is on the live page unchanged (chrome only: «Iniciar sesión» → «Iniciar sesión en tu
cuenta», a «Más» menu item moved).

Places found: `grep -rn ms-excel-ordenar` in `es/lessons/`, `glossary.yaml` and the bank/cases drafts. Glossary: no
entry cites the page. Cases: none. Lesson: one esquema row (`m06-l05.md:82`) plus the source list entry (`:166`).
Questions in `bloque-vi/m06-l05.draft.json` citing it: 7; dropped already (in `drops.tsv`): q302, q303, q304; kept:
q301, q305, q357, q358 (also shipped in `exercises/m06-l05-ex-8.yaml` / `ex-9.yaml`, same text).

| place | fact | stored text | live text | verdict | replacement / check |
|---|---|---|---|---|---|
| `m06-l05.md:81–82` esquema row **Ordenar** | «Datos › Ordenar y filtrar» | «En la ficha Datos, en el grupo Ordenar y filtrar, siga uno de estos procedimientos.» | same sentence, «Ordenar texto» | holds | — |
| `m06-l05.md:81–82` esquema row **Ordenar** | numbers stored as numbers sort before numbers stored as text | «Si no lo hace, los números almacenados como números se ordenarán antes que los números almacenados como texto.» | same sentence, «Posibles problemas»; new table adds «El texto, incluidos los números guardados como texto, se ordena en el siguiente orden: 0 1 2 … A … Z» and «Una ordenación descendente utiliza el orden inverso a este orden, excepto donde se indique lo contrario.» | holds | Not contradicted: the table gives the order within each kind of value, never states one kind before another, and the cited sentence is still printed unqualified. Note (non-blocking): read as a type order, the table would put text before numbers in a descending sort. If the coordinator wants the row tightened: «En orden ascendente, los números guardados como números van antes que los guardados como texto.» |
| `m06-l05.md:166` source list | title «Ordenar datos de una tabla o un rango en Excel» | page title | same title | holds | — (consultation date is the coordinator's call) |
| q301 (kept) | A–Z / Z–A in Datos › Ordenar y filtrar; distractors Datos › Esquema, Datos › Herramientas de datos, Inicio › Estilos | «En la ficha Datos, en el grupo Ordenar y filtrar…» «(Ordenar de la A a la Z)» «(Ordenar de la Z a la A)» | same | holds | 1 key PASS · 2 unique PASS (live page also has «pestaña Inicio, grupo Edición, Ordenar & filtrar», already in the stored copy; Edición is not an option, Estilos stays wrong; added table names no group) · 3 citation PASS · 4 style PASS (unchanged) · 5 official PASS (unchanged) → **PASS** |
| q305 (kept) | tables do not sort left to right; convert to range first | «Las tablas no admiten la ordenación de izquierda a derecha. Para ello, primero debe convertir la tabla en un rango…» | same | holds | 1 PASS · 2 PASS (added «El texto alfanumérico se ordena de izquierda a derecha, carácter por carácter» is about character order inside a string, not sort orientation; makes no distractor true) · 3 PASS · 4 PASS · 5 PASS → **PASS** |
| q357 (kept) | at most 64 columns | «Puede ordenar por un máximo de 64 columnas.» | same | holds | 1 PASS · 2 PASS (added text gives no other limit) · 3 PASS · 4 PASS · 5 PASS → **PASS** |
| q358 (kept) | Ordenar según › Color de celda for manual or conditional cell colour | «Para ordenar por formato, seleccione Color de celda, Color de fuente o Icono de celda.»; «Si ha aplicado formato manual o condicionalmente… por color de celda o color de fuente…» | same | holds | 1 PASS · 2 PASS (added table is about value order, says nothing of colour) · 3 PASS · 4 PASS · 5 PASS → **PASS** |

Added sentences checked against every kept key, distractor and lesson sentence: blank cells always last; error values
equal; FALSE before TRUE; text order incl. space/symbols and case-insensitive default; «varían según la configuración
regional». None of the kept questions or lesson rows states anything about blanks, errors, logical values, character
order or locale in sorting, so nothing is made true, contradicted or incomplete. The only lesson mention of
«configuración regional» (`m06-l05.md:31`, separators) cites another page and is unaffected.

## Counts

- Places: 3 lesson (2 facts on the esquema row + source entry), 0 glossary, 0 cases, 4 kept questions.
- Verdicts: 7 holds, 0 changed, 0 removed.
- Questions: 4 PASS, 0 FAIL. Drops added to `bloque-vi/drops.tsv`: none.
- Lesson replacements required: none (one optional tightening above).
