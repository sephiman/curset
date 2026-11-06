# m02-l08 — coverage fixes (2026-11-06)

Pages saved: `ms-word-nuevos-usuarios.html`, `ms-word-origenes-datos.html`, `ms-word-ordenar-tabla.html`,
`ms-word-grafico.html` (fragment `m02-l08-fix-fuentes.yaml`). Pending after `plan m02-l08 m06-l04`: 10, all new.

| Row | Result | Item / what was searched |
|---|---|---|
| 2024-P2-27 (Ctrl+< reduce font) | sin fuente | `ms-word-atajos.html` is the US layout (Ctrl+[); no Microsoft es-es page found that is the Spanish-keyboard layout. |
| 2024X-P2-11 (3D model: corrections, background) | sin fuente | Searched es-es 3D-model and shape-format pages; `ms-office-modelos-3d.html` has no corrections or background text; results were shapes and WordArt only. |
| 2024X-P2-12 (Tab in last cell adds a row) | sin fuente | The sentence appears on `ms-word-atajos.html` only in the macOS/web part (line 1221 of the text dump, after the Cmd rows), not the Windows section; the other pages found are PowerPoint, Publisher, and a screen-reader page whose row-adding line is the Mac section. |
| 2024X-P2-13 (Ctrl+G save) | sin fuente | Same as 2024-P2-27: only the US-layout page; Ctrl+G is «Ir a» there. |
| 2024X-P2-14 (Diseño › Formato del documento) | fixed | Item «Formato del documento» (`ms-word-nuevos-usuarios.html`). |
| 2022-P2-35 (footnote shortcut) | sin fuente | The page gives Ctrl+Alt+F (US layout); no Spanish-layout page found. |
| Family: Insertar › Gráfico | fixed | Item «Gráfico» (`ms-word-grafico.html`). |
| Family: Ordenar tabla | fixed | Item «Ordenar tabla» (`ms-word-ordenar-tabla.html`); the page's path is garbled in the one-line ribbon, so the item gives the classic ribbon route «Diseño de tabla › Datos». |
| Family: Seleccionar destinatarios | fixed | Item «Seleccionar destinatarios» (`ms-word-origenes-datos.html`); the page prints «elegir de los contactos de Outlook» in lower case and no «Escribir una nueva lista» label, so the item says so. |

Counts, MISS rows: fixed 1, sin fuente 5. Family gaps: fixed 3.
