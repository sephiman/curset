# Currency check C1b, share «c»: Microsoft Word, Excel, Access and Outlook pages

Checked 2026-10-17 against `content/age-administrativo-c1/sources/otros/fuentes.yaml`: the 106 entries whose file
name starts with `ms-word`, `ms-excel`, `ms-access` or `ms-outlook`. Fetched with the spec's `curl` command into
`SP/currency/pages/` (SP = this session's scratchpad); text compared with `SP/pagetext.py`, `difflib` over the
extracted lines of the stored and live copies.

## Summary

| Status | Count |
|---|---|
| identical | 0 |
| text-identical | 106 |
| changed | 0 |
| gone | 0 |

- Every page answered HTTP 200 at the stored URL, with no redirect and no login wall.
- No sha256 matches, as expected: support.microsoft.com writes per-request tokens into the `<head>`
  (`awa-userFlightingId`, `awa-expid` experiment ids and similar). For `ms-outlook-buscar.html` the raw HTML differs
  in those two meta lines only. The extracted text of all 106 pages is identical line for line to the stored copy,
  so no boilerplate had to be set aside by hand.
- Fetch note: the first run sent 6 requests at a time, and Microsoft's edge answered 61 of them with a 403 «Access
  Denied» page. A sequential retry got 200 for all of them (two needed a third try). These were rate limits, not
  removed pages.

No page is **changed** or **gone**, so there are no affected citations to list.

## Pages

| File | Status | HTTP / final URL | Note |
|---|---|---|---|
| `ms-word-copilot.html` | text-identical | 200 / same URL | sha256 differs (session/experiment tokens); readable text identical |
| `ms-excel-copilot.html` | text-identical | 200 / same URL | sha256 differs (session/experiment tokens); readable text identical |
| `ms-outlook-copilot-resumir.html` | text-identical | 200 / same URL | sha256 differs (session/experiment tokens); readable text identical |
| `ms-word-atajos.html` | text-identical | 200 / same URL | sha256 differs (session/experiment tokens); readable text identical |
| `ms-word-lector-pantalla.html` | text-identical | 200 / same URL | sha256 differs (session/experiment tokens); readable text identical |
| `ms-word-opciones-mostrar.html` | text-identical | 200 / same URL | sha256 differs (session/experiment tokens); readable text identical |
| `ms-word-ajustar-imagenes.html` | text-identical | 200 / same URL | sha256 differs (session/experiment tokens); readable text identical |
| `ms-word-macros.html` | text-identical | 200 / same URL | sha256 differs (session/experiment tokens); readable text identical |
| `ms-word-lectura-voz-alta.html` | text-identical | 200 / same URL | sha256 differs (session/experiment tokens); readable text identical |
| `ms-word-transcribir.html` | text-identical | 200 / same URL | sha256 differs (session/experiment tokens); readable text identical |
| `ms-word-contar-palabras.html` | text-identical | 200 / same URL | sha256 differs (session/experiment tokens); readable text identical |
| `ms-word-coautoria.html` | text-identical | 200 / same URL | sha256 differs (session/experiment tokens); readable text identical |
| `ms-word-combinar-correspondencia.html` | text-identical | 200 / same URL | sha256 differs (session/experiment tokens); readable text identical |
| `ms-word-espaciado-caracteres.html` | text-identical | 200 / same URL | sha256 differs (session/experiment tokens); readable text identical |
| `ms-word-tabla-contenido.html` | text-identical | 200 / same URL | sha256 differs (session/experiment tokens); readable text identical |
| `ms-word-indice.html` | text-identical | 200 / same URL | sha256 differs (session/experiment tokens); readable text identical |
| `ms-word-notas.html` | text-identical | 200 / same URL | sha256 differs (session/experiment tokens); readable text identical |
| `ms-word-salto-seccion.html` | text-identical | 200 / same URL | sha256 differs (session/experiment tokens); readable text identical |
| `ms-word-numeros-pagina.html` | text-identical | 200 / same URL | sha256 differs (session/experiment tokens); readable text identical |
| `ms-word-opciones-guardar.html` | text-identical | 200 / same URL | sha256 differs (session/experiment tokens); readable text identical; 403 in the parallel run, 200 on sequential retry |
| `ms-word-imprimir.html` | text-identical | 200 / same URL | sha256 differs (session/experiment tokens); readable text identical |
| `ms-word-cinta.html` | text-identical | 200 / same URL | sha256 differs (session/experiment tokens); readable text identical |
| `ms-excel-atajos.html` | text-identical | 200 / same URL | sha256 differs (session/experiment tokens); readable text identical |
| `ms-excel-tabla-dinamica.html` | text-identical | 200 / same URL | sha256 differs (session/experiment tokens); readable text identical |
| `ms-excel-formulas.html` | text-identical | 200 / same URL | sha256 differs (session/experiment tokens); readable text identical |
| `ms-excel-insertar-hoja.html` | text-identical | 200 / same URL | sha256 differs (session/experiment tokens); readable text identical; 403 in the parallel run, 200 on sequential retry |
| `ms-excel-ocultar-hojas.html` | text-identical | 200 / same URL | sha256 differs (session/experiment tokens); readable text identical |
| `ms-excel-proteger-hoja.html` | text-identical | 200 / same URL | sha256 differs (session/experiment tokens); readable text identical |
| `ms-excel-proteger-libro.html` | text-identical | 200 / same URL | sha256 differs (session/experiment tokens); readable text identical |
| `ms-excel-inmovilizar-paneles.html` | text-identical | 200 / same URL | sha256 differs (session/experiment tokens); readable text identical; 403 twice (bot block), 200 on the third sequential try |
| `ms-excel-seleccionar-celdas.html` | text-identical | 200 / same URL | sha256 differs (session/experiment tokens); readable text identical |
| `ms-excel-combinar-celdas.html` | text-identical | 200 / same URL | sha256 differs (session/experiment tokens); readable text identical; 403 in the parallel run, 200 on sequential retry |
| `ms-excel-separadores.html` | text-identical | 200 / same URL | sha256 differs (session/experiment tokens); readable text identical |
| `ms-excel-formato-fecha.html` | text-identical | 200 / same URL | sha256 differs (session/experiment tokens); readable text identical |
| `ms-excel-funcion-dia.html` | text-identical | 200 / same URL | sha256 differs (session/experiment tokens); readable text identical; 403 in the parallel run, 200 on sequential retry |
| `ms-excel-referencias-estructuradas.html` | text-identical | 200 / same URL | sha256 differs (session/experiment tokens); readable text identical; 403 in the parallel run, 200 on sequential retry |
| `ms-excel-funciones-categoria.html` | text-identical | 200 / same URL | sha256 differs (session/experiment tokens); readable text identical; 403 in the parallel run, 200 on sequential retry |
| `ms-excel-funcion-no.html` | text-identical | 200 / same URL | sha256 differs (session/experiment tokens); readable text identical |
| `ms-excel-funcion-o.html` | text-identical | 200 / same URL | sha256 differs (session/experiment tokens); readable text identical |
| `ms-excel-funcion-sierror.html` | text-identical | 200 / same URL | sha256 differs (session/experiment tokens); readable text identical; 403 in the parallel run, 200 on sequential retry |
| `ms-excel-error-na.html` | text-identical | 200 / same URL | sha256 differs (session/experiment tokens); readable text identical; 403 in the parallel run, 200 on sequential retry |
| `ms-excel-funcion-contara.html` | text-identical | 200 / same URL | sha256 differs (session/experiment tokens); readable text identical; 403 in the parallel run, 200 on sequential retry |
| `ms-excel-graficos.html` | text-identical | 200 / same URL | sha256 differs (session/experiment tokens); readable text identical; 403 in the parallel run, 200 on sequential retry |
| `ms-excel-ordenar.html` | text-identical | 200 / same URL | sha256 differs (session/experiment tokens); readable text identical; 403 in the parallel run, 200 on sequential retry |
| `ms-excel-filtrar.html` | text-identical | 200 / same URL | sha256 differs (session/experiment tokens); readable text identical |
| `ms-excel-quitar-duplicados.html` | text-identical | 200 / same URL | sha256 differs (session/experiment tokens); readable text identical |
| `ms-excel-subtotales.html` | text-identical | 200 / same URL | sha256 differs (session/experiment tokens); readable text identical; 403 in the parallel run, 200 on sequential retry |
| `ms-excel-segmentacion.html` | text-identical | 200 / same URL | sha256 differs (session/experiment tokens); readable text identical; 403 in the parallel run, 200 on sequential retry |
| `ms-excel-anular-dinamizacion.html` | text-identical | 200 / same URL | sha256 differs (session/experiment tokens); readable text identical |
| `ms-excel-lista-desplegable.html` | text-identical | 200 / same URL | sha256 differs (session/experiment tokens); readable text identical; 403 in the parallel run, 200 on sequential retry |
| `ms-excel-imprimir.html` | text-identical | 200 / same URL | sha256 differs (session/experiment tokens); readable text identical; 403 twice (bot block), 200 on the third sequential try |
| `ms-excel-escalar.html` | text-identical | 200 / same URL | sha256 differs (session/experiment tokens); readable text identical; 403 in the parallel run, 200 on sequential retry |
| `ms-access-dividir.html` | text-identical | 200 / same URL | sha256 differs (session/experiment tokens); readable text identical; 403 in the parallel run, 200 on sequential retry |
| `ms-access-especificaciones.html` | text-identical | 200 / same URL | sha256 differs (session/experiment tokens); readable text identical |
| `ms-access-compactar.html` | text-identical | 200 / same URL | sha256 differs (session/experiment tokens); readable text identical; 403 in the parallel run, 200 on sequential retry |
| `ms-access-graficos.html` | text-identical | 200 / same URL | sha256 differs (session/experiment tokens); readable text identical; 403 in the parallel run, 200 on sequential retry |
| `ms-access-tipos-datos-escritorio.html` | text-identical | 200 / same URL | sha256 differs (session/experiment tokens); readable text identical; 403 in the parallel run, 200 on sequential retry |
| `ms-access-tipos-datos.html` | text-identical | 200 / same URL | sha256 differs (session/experiment tokens); readable text identical; 403 in the parallel run, 200 on sequential retry |
| `ms-access-clave-principal.html` | text-identical | 200 / same URL | sha256 differs (session/experiment tokens); readable text identical; 403 in the parallel run, 200 on sequential retry |
| `ms-access-reglas-validacion.html` | text-identical | 200 / same URL | sha256 differs (session/experiment tokens); readable text identical; 403 in the parallel run, 200 on sequential retry |
| `ms-access-consultas.html` | text-identical | 200 / same URL | sha256 differs (session/experiment tokens); readable text identical; 403 in the parallel run, 200 on sequential retry |
| `ms-access-criterios.html` | text-identical | 200 / same URL | sha256 differs (session/experiment tokens); readable text identical |
| `ms-access-where.html` | text-identical | 200 / same URL | sha256 differs (session/experiment tokens); readable text identical |
| `ms-access-formularios.html` | text-identical | 200 / same URL | sha256 differs (session/experiment tokens); readable text identical; 403 in the parallel run, 200 on sequential retry |
| `ms-access-subformulario.html` | text-identical | 200 / same URL | sha256 differs (session/experiment tokens); readable text identical |
| `ms-access-orden-tabulacion.html` | text-identical | 200 / same URL | sha256 differs (session/experiment tokens); readable text identical; 403 in the parallel run, 200 on sequential retry |
| `ms-access-informes.html` | text-identical | 200 / same URL | sha256 differs (session/experiment tokens); readable text identical; 403 in the parallel run, 200 on sequential retry |
| `ms-access-relaciones.html` | text-identical | 200 / same URL | sha256 differs (session/experiment tokens); readable text identical; 403 in the parallel run, 200 on sequential retry |
| `ms-access-importar-excel.html` | text-identical | 200 / same URL | sha256 differs (session/experiment tokens); readable text identical; 403 in the parallel run, 200 on sequential retry |
| `ms-access-exportar-excel.html` | text-identical | 200 / same URL | sha256 differs (session/experiment tokens); readable text identical; 403 in the parallel run, 200 on sequential retry |
| `ms-outlook-agregar-cuenta.html` | text-identical | 200 / same URL | sha256 differs (session/experiment tokens); readable text identical; 403 in the parallel run, 200 on sequential retry |
| `ms-outlook-imap-pop.html` | text-identical | 200 / same URL | sha256 differs (session/experiment tokens); readable text identical; 403 in the parallel run, 200 on sequential retry |
| `ms-outlook-smime.html` | text-identical | 200 / same URL | sha256 differs (session/experiment tokens); readable text identical |
| `ms-outlook-grupos.html` | text-identical | 200 / same URL | sha256 differs (session/experiment tokens); readable text identical; 403 in the parallel run, 200 on sequential retry |
| `ms-outlook-compartir-carpeta.html` | text-identical | 200 / same URL | sha256 differs (session/experiment tokens); readable text identical; 403 in the parallel run, 200 on sequential retry |
| `ms-outlook-delegados.html` | text-identical | 200 / same URL | sha256 differs (session/experiment tokens); readable text identical; 403 in the parallel run, 200 on sequential retry |
| `ms-outlook-atajos.html` | text-identical | 200 / same URL | sha256 differs (session/experiment tokens); readable text identical; 403 in the parallel run, 200 on sequential retry |
| `ms-outlook-vistas.html` | text-identical | 200 / same URL | sha256 differs (session/experiment tokens); readable text identical; 403 in the parallel run, 200 on sequential retry |
| `ms-outlook-categorias.html` | text-identical | 200 / same URL | sha256 differs (session/experiment tokens); readable text identical |
| `ms-outlook-buscar.html` | text-identical | 200 / same URL | sha256 differs (session/experiment tokens); readable text identical; 403 in the parallel run, 200 on sequential retry |
| `ms-outlook-procedimientos.html` | text-identical | 200 / same URL | sha256 differs (session/experiment tokens); readable text identical |
| `ms-outlook-limpieza-buzon.html` | text-identical | 200 / same URL | sha256 differs (session/experiment tokens); readable text identical; 403 in the parallel run, 200 on sequential retry |
| `ms-outlook-archivar.html` | text-identical | 200 / same URL | sha256 differs (session/experiment tokens); readable text identical; 403 in the parallel run, 200 on sequential retry |
| `ms-outlook-responder-reenviar.html` | text-identical | 200 / same URL | sha256 differs (session/experiment tokens); readable text identical; 403 in the parallel run, 200 on sequential retry |
| `ms-outlook-recuperar.html` | text-identical | 200 / same URL | sha256 differs (session/experiment tokens); readable text identical; 403 in the parallel run, 200 on sequential retry |
| `ms-outlook-programar-envio.html` | text-identical | 200 / same URL | sha256 differs (session/experiment tokens); readable text identical; 403 in the parallel run, 200 on sequential retry |
| `ms-outlook-importancia.html` | text-identical | 200 / same URL | sha256 differs (session/experiment tokens); readable text identical; 403 in the parallel run, 200 on sequential retry |
| `ms-outlook-firma.html` | text-identical | 200 / same URL | sha256 differs (session/experiment tokens); readable text identical; 403 in the parallel run, 200 on sequential retry |
| `ms-outlook-reglas.html` | text-identical | 200 / same URL | sha256 differs (session/experiment tokens); readable text identical; 403 in the parallel run, 200 on sequential retry |
| `ms-outlook-listas-contactos.html` | text-identical | 200 / same URL | sha256 differs (session/experiment tokens); readable text identical; 403 in the parallel run, 200 on sequential retry |
| `ms-access-consulta-seleccion.html` | text-identical | 200 / same URL | sha256 differs (session/experiment tokens); readable text identical; 403 in the parallel run, 200 on sequential retry |
| `ms-access-expresiones.html` | text-identical | 200 / same URL | sha256 differs (session/experiment tokens); readable text identical |
| `ms-access-funcion-ano.html` | text-identical | 200 / same URL | sha256 differs (session/experiment tokens); readable text identical; 403 in the parallel run, 200 on sequential retry |
| `ms-access-funcion-conmutador.html` | text-identical | 200 / same URL | sha256 differs (session/experiment tokens); readable text identical; 403 in the parallel run, 200 on sequential retry |
| `ms-excel-error-nombre.html` | text-identical | 200 / same URL | sha256 differs (session/experiment tokens); readable text identical; 403 in the parallel run, 200 on sequential retry |
| `ms-excel-funcion-dividirtexto.html` | text-identical | 200 / same URL | sha256 differs (session/experiment tokens); readable text identical; 403 in the parallel run, 200 on sequential retry |
| `ms-excel-funcion-extrae.html` | text-identical | 200 / same URL | sha256 differs (session/experiment tokens); readable text identical; 403 in the parallel run, 200 on sequential retry |
| `ms-outlook-carpetas-busqueda.html` | text-identical | 200 / same URL | sha256 differs (session/experiment tokens); readable text identical |
| `ms-outlook-correo-no-deseado.html` | text-identical | 200 / same URL | sha256 differs (session/experiment tokens); readable text identical; 403 in the parallel run, 200 on sequential retry |
| `ms-outlook-graficos.html` | text-identical | 200 / same URL | sha256 differs (session/experiment tokens); readable text identical; 403 in the parallel run, 200 on sequential retry |
| `ms-outlook-grupo-enviar.html` | text-identical | 200 / same URL | sha256 differs (session/experiment tokens); readable text identical; 403 in the parallel run, 200 on sequential retry |
| `ms-outlook-grupos-envio-recepcion.html` | text-identical | 200 / same URL | sha256 differs (session/experiment tokens); readable text identical |
| `ms-outlook-limpiar-conversacion.html` | text-identical | 200 / same URL | sha256 differs (session/experiment tokens); readable text identical; 403 in the parallel run, 200 on sequential retry |
| `ms-word-coautoria-documentos.html` | text-identical | 200 / same URL | sha256 differs (session/experiment tokens); readable text identical; 403 in the parallel run, 200 on sequential retry |
| `ms-word-comentarios.html` | text-identical | 200 / same URL | sha256 differs (session/experiment tokens); readable text identical; 403 in the parallel run, 200 on sequential retry |
| `ms-word-seleccionar-objetos.html` | text-identical | 200 / same URL | sha256 differs (session/experiment tokens); readable text identical; 403 in the parallel run, 200 on sequential retry |

## `ms-outlook-buscar.html`: the two disputed search keys

Both sentences behind the disputed keys read the same live as in the stored copy:

- 2024 X 65 («proyecto», key c): «Por ejemplo, si busca "proyect", con o sin comillas, Outlook devolverá todos los
  mensajes con la palabra proyecto, proyectos, proyector, proyectar, etc. en cualquier lugar del nombre del remitente,
  el asunto, el cuerpo del mensaje o los datos adjuntos.» The same page's table still says quotes give the exact phrase
  («“miguel” | Los elementos que contengan la frase exacta miguel y no las variaciones…»; «de:"miguel tórrez" | …
  Observe el uso de comillas dobles para que los resultados de la búsqueda coincidan con la frase exacta…»), so the
  internal inconsistency recorded in the ledger is still there.
- 2025 X 66 ("9876", key a): «Las cadenas de números de menos de cinco dígitos se omiten. Si desea buscar 98101, al
  introducir 9810 no obtendrá ningún resultado.»

The m06-l07 citations (lines 42–46, 114, 115: prefix matching «proyect» → proyecto, proyector; double quotes for the
exact phrase; cc:"miguel tórrez"; numbers under five digits omitted) all **hold**. The «Clave oficial discutida»
status of both items stands.

## Ledger table «Etiqueta del examen / Etiqueta oficial»: official labels in share «c», live

Every official label from the table that sits on a page in this share was searched in the stored and the live text.
Every one appears the same number of times in both.

| Official label (ledger) | Page | Live |
|---|---|---|
| «Ver» on the Macros page (Ver>macro grabar macros.>, Ver>macros>Detener grabación) | `ms-word-macros.html` | same |
| «grabar macros», garbled path | `ms-word-macros.html` | same |
| «Vista» / «Disposición» on the shortcut page | `ms-word-atajos.html` («Abrir la pestaña Disposición…», «Abrir la pestaña Vista…») | same |
| «Saltos de diseño>» | `ms-word-salto-seccion.html` (also «Saltos de> diseño») | same |
| «Mostrar u ocultar ¶» | `ms-word-opciones-mostrar.html` (printed lower case: «mostrar u ocultar ¶») | same |
| «Opciones de Word (Mostrar)» in the title, «Visualización» in the path | `ms-word-opciones-mostrar.html` | same |
| «Lectura en voz alta» | `ms-word-lectura-voz-alta.html` | same |
| «numeración de páginas» | `ms-word-numeros-pagina.html` | same |
| «Imprimir hojas activas» › «Imprimir tabla seleccionada» | `ms-excel-imprimir.html` | same |
| Ancho 1 página, Alto Automático; «Ajustar hoja en una página» | `ms-excel-escalar.html` | same |
| «pestaña Vista» and «Ver>Inmovilizar paneles» | `ms-excel-inmovilizar-paneles.html` | same |
| «SI.ERROR» | `ms-excel-funcion-sierror.html` | same |
| «#N/A»; «#N/D» on the DIVIDIRTEXTO page | `ms-excel-error-na.html`, `ms-excel-funcion-dividirtexto.html` | same |
| «Combinar y centrar» and «Combinar & centro» | `ms-excel-combinar-celdas.html` | same |
| «Indexado», «Obligatorio» | `ms-access-tipos-datos.html` | same |
| «Asistente para el separador de base de datos» | `ms-access-dividir.html` | same |
| «ControlSource» | `ms-access-expresiones.html` | same |
| «origen de control» of a text box (printed «Editar orígenes de control de cuadro de texto en los propios cuadros de texto, sin usar la hoja de propiedades») | `ms-access-formularios.html` | same |
| «Diseño» (Orden de tabulación); «Diseño de formulario» | `ms-access-orden-tabulacion.html`, `ms-access-formularios.html` | same |
| «Gráfico moderno» | `ms-access-graficos.html` | same |
| garbled «Información de>archivo>» | `ms-access-compactar.html` | same |
| «Agrupar &ordenar»; «Agrupación, orden y total» | `ms-access-informes.html` | same |
| «Importar & vínculo» / «Importar & vincular» | `ms-access-importar-excel.html` | same |
| «Opciones de mensaje», «Opciones de entrega», «No entregar antes» | `ms-outlook-programar-envio.html` | same |
| «Mensaje › Firma › Firmas» | `ms-outlook-firma.html` | same |
| «Delegar el acceso»; new Outlook delegation «solo está parcialmente disponible» | `ms-outlook-delegados.html` | same |
| «Vaya a Mail» | `ms-outlook-atajos.html` | same |
| «Uso compartido y permisos» (new Outlook folder permissions) | `ms-outlook-compartir-carpeta.html` | same |

The rows whose label sits on a page outside this share (`ms-win-*`, `incibe-glosario-ciberseguridad.pdf`) or on no
saved page («—», the junk-mail page that was read but not saved, «BUSCARV»/«CONSULTAV» with no file named) are not
covered here.
