# Verification — `m02-l08`, re-check 2 (blind)

Verifier: blind, 2026-11-06. Did not write the lesson; checked against the saved pages in `content/age-auxiliar-c2/sources/otros/` (HTML stripped to text; Windows desktop sections, located by the pages' `data-tab` panels). Input: `docs/age-verification/c2/bloque-ii/pending/m02-l08.md` (10 items), lesson
`content/age-auxiliar-c2/es/lessons/m02-l08.md`. Pages read: `ms-word-origenes-datos.html`, `ms-word-nuevos-usuarios.html`,
`ms-word-ordenar-tabla.html`, `ms-word-grafico.html`.

New pages (`descarga nueva`, 2026-11-06): the sha256 of each of the four files matches `writer/m02-l08-fix-fuentes.yaml`
and `sources/otros/fuentes.yaml`; each has `lang="es-ES"`, a canonical URL equal to the recorded one, and the Spanish
article title recorded.

| id | verdict | precept checked | note | replacement |
|---|---|---|---|---|
| `36bde3f552` | FAIL | ms-word-origenes-datos.html; Windows | the label «Seleccionar destinatarios» is not on the page (nor on any saved page); the page's path is «Vaya a Correspondencia>Seleccione destinatarios>Usar una lista existente» | **Seleccione destinatarios**: la página da la ruta «Correspondencia › Seleccione destinatarios › Usar una lista existente». |
| `4669931145` | PASS | ms-word-origenes-datos.html; Windows, «Lista existente», «Lista de contactos de Outlook», «Nueva lista» | «Las listas existentes podrían ser hojas de cálculo de Excel, bases de datos de Access o algún otro tipo de base de datos … elija usar una lista existente»; «elija elegir de los contactos de Outlook»; «Si aún no tiene una lista, puede escribir una en Word» | — |
| `2004fbfbe0` | FAIL | ms-word-nuevos-usuarios.html | path, «conjuntos de estilos predefinidos, como Básicos o Casuales» and «cambiar el aspecto de todo el documento a la vez» are literal; the page names the preview «vista previa dinámica» («Sitúe el puntero sobre cualquier conjunto de estilos para ver una vista previa dinámica directamente en el documento»), not «vista previa en vivo» | **Formato del documento**: «Diseño › Formato del documento» ofrece conjuntos de estilos predefinidos, como Básicos o Casuales, que cambian el aspecto de todo el documento a la vez; al situar el puntero sobre uno, una vista previa dinámica lo muestra en el documento (fuente: `ms-word-nuevos-usuarios.html`). |
| `b6bf530294` | FAIL | ms-word-ordenar-tabla.html; Windows | «Cinta de opciones clásica … Diseño de tabla … En la sección Datos, seleccione Ordenar tabla de forma ascendente u Ordenar tabla descendente» is in the Web panel (`tabpanel_2_web`), i.e. Word para la web, not desktop. The Windows panel says «aparecerán las pestañas Diseño de tabla y Diseño» and the garbled «Junto a Diseño de tabla, vaya a Ordenar diseño>.», whose single coherent reading is «Diseño › Ordenar» | **Ordenar tabla**: con la tabla seleccionada aparecen las pestañas Diseño de tabla y Diseño; junto a Diseño de tabla, «Diseño › Ordenar» abre el cuadro de diálogo de ordenación. |
| `cc1a22ed3f` | FAIL | ms-word-ordenar-tabla.html; Windows | Ordenar por, Tipo (Texto, Número o Una fecha) and three levels are in the Windows panel («Repita este procedimiento hasta tres niveles»); «Luego por» appears only in the macOS panel | El cuadro de diálogo pide Ordenar por (nombre o número de columna), Tipo (Texto, Número o Una fecha) y orden ascendente o descendente, y el procedimiento se repite hasta tres niveles (fuente: `ms-word-ordenar-tabla.html`; Windows). |
| `7345f20063` | PASS | ms-word-grafico.html | «Seleccione Insertar>gráfico.»; «Seleccione el tipo de gráfico y haga doble clic en el gráfico que desee.» | — |
| `a7139a82be` | PASS | Fuentes | title and date match the saved page; the file is cited in the prose | — |
| `f8afa5adcd` | PASS | Fuentes | title and date match the saved page; cited in the prose | — |
| `db5e40a796` | PASS | Fuentes | title and date match the saved page; cited in the prose | — |
| `eb7cfa0277` | PASS | Fuentes | title and date match the saved page; cited in the prose | — |

PASS 6, FAIL 4.

«Fuentes» section: 39 files cited in the prose, 39 listed, the same set.
