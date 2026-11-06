# Verification — `m02-l08`, re-check 3

Verifier: blind verifier (opus), 2026-11-06. Did not write the lesson. Checked against the pages, not against the
proposer's wording.

Files read: `docs/age-verification/c2/bloque-ii/pending/m02-l08.md`, `content/age-auxiliar-c2/es/lessons/m02-l08.md`,
text (HTML stripped) of `content/age-auxiliar-c2/sources/otros/ms-word-origenes-datos.html`,
`ms-word-nuevos-usuarios.html`, `ms-word-ordenar-tabla.html` (sha256 of all three equal to fuentes.yaml; Microsoft
es-es, admissible).

Result: 2 PASS, 2 FAIL.

| id | verdict | precept checked | note | replacement |
|---|---|---|---|---|
| `1f07cb4644` | PASS | ms-word-origenes-datos.html, «Lista existente» | the page prints «Vaya a Correspondencia>Seleccione destinatarios>Usar una lista existente»; the sentence attributes the wording to the page, and the item's closing citation is this file | — |
| `fd5005df2a` | PASS | ms-word-nuevos-usuarios.html, «Usar estilos» | «Word le permite usar un conjunto de estilos para cambiar el aspecto de todo el documento a la vez. En la pestaña Diseño, en el grupo Formato del documento, elija uno de los conjuntos de estilos predefinidos, como Básicos o Casuales. Sitúe el puntero sobre cualquier conjunto de estilos para ver una vista previa dinámica directamente en el documento» | — |
| `28acaee7a3` | FAIL | ms-word-ordenar-tabla.html, tab «Windows» | «Seleccione la tabla. Después de seleccionarla, aparecerán las pestañas Diseño de tabla y Diseño» matches. The path is not literal: the Windows tab prints «Junto a Diseño de tabla, vaya a Ordenar diseño>.», then «En el cuadro de diálogo, elija cómo quiere ordenar la tabla». «Diseño › Ordenar» is a reading of that string, not the page's text. «Ordenar tabla ascendente / descendente» (sección Datos) appears only under «Cinta de opciones clásica» / «Cinta de opciones de una sola línea», after the Windows and macOS tabs; it is not a Windows-tab step | - **Ordenar tabla**: con la tabla seleccionada aparecen las pestañas Diseño de tabla y Diseño; la página continúa «Junto a Diseño de tabla, vaya a Ordenar diseño>», y en el cuadro de diálogo se elige cómo ordenar la tabla. |
| `5636e06e30` | FAIL | ms-word-ordenar-tabla.html, tab «Windows» | Ordenar por (nombre o número de columna), Tipo (Texto, Número o Una fecha), «Orden ascendente o descendente» and «Repita este procedimiento hasta tres niveles» match. The list reads as complete but leaves out the step before it, «Elija si los datos tienen encabezados o no» (Opciones also follows) | El cuadro de diálogo pide si los datos tienen encabezados, Ordenar por (nombre o número de columna), Tipo (Texto, Número o Una fecha) y orden ascendente o descendente, y el procedimiento se repite hasta tres niveles (fuente: `ms-word-ordenar-tabla.html`; Windows). |
