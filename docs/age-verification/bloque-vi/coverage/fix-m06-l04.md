# Fix — m06-l04 (2026-10-17)

Rows of `fixes.md` for m06-l04, applied under the v1.5 rule change (no word ceiling): nothing was cut. Lesson:
`content/age-administrativo-c1/es/lessons/m06-l04.md`. Word count (`wc -w`): 1485 → **1686**. Lines ≤ 120 except the
`#` title line (unchanged). Fuentes reordered by first citation (`fuentes_order.py`: in order, none missing, none
uncited).

## Changes

### 1. 2025 X 51 — red wavy underline (item «Ortografía y gramática»; LQMC line 5)

- Old: «F7 inicia la revisión. Línea ondulada roja, posible error ortográfico; azul, gramatical (fuente:
  `ms-office-ortografia.html`).»
- New: «… azul, gramatical. Si marca como incorrecta una palabra escrita como quieres, «Agregar al diccionario» hace que
  no vuelva a marcarla (fuente: `ms-office-ortografia.html`).»
- LQMC old: «La línea ondulada roja marca un posible error ortográfico (fuente: `ms-office-ortografia.html`).» New:
  «…; «Agregar al diccionario» evita que vuelva a marcar una palabra bien escrita (fuente: `ms-office-ortografia.html`).»
- Source (Windows tab): «Office marca los posibles errores ortográficos con una línea ondulada de color rojo»; «Si Office
  marca como incorrectas palabras que están escritas de la manera que usted quiere, seleccione Agregar al diccionario
  para que Office no las vuelva a marcar como incorrectas.»
- Not used: «Cuando no se reconoce una palabra, la aplicación la marca como incorrecta subrayando la palabra con una
  línea roja ondulada» is printed on «Agregar o editar palabras en un diccionario de corrección ortográfica»
  (support.microsoft.com/es-es/word/add-or-edit-words-in-a-spell-check-dictionary) only in its **Web** tab; not saved.
  The literal «palabra que no está en el diccionario» for Word desktop: **sin fuente oficial**.

### 2. 2025 X 53 — co-authoring in OneDrive/SharePoint (item «Coautoría»)

- Old: «- **Coautoría**: en un documento compartido ves la presencia y los cambios de quien lo edita, en tiempo real
  (fuente: `ms-word-coautoria.html`).»
- New: «- **Coautoría**: guarda el documento en OneDrive o SharePoint y compártelo para trabajar en él a la vez (fuente:
  `ms-word-coautoria-documentos.html`); ves la presencia y los cambios de quien lo edita, en tiempo real (fuente:
  `ms-word-coautoria.html`).»
- Source (`ms-word-coautoria-documentos.html`, «Se aplica a» Word para Microsoft 365, 2024, 2021): «Guarde el documento
  en OneDrive o SharePoint y compártalo con otros usuarios para que pueda trabajar en él al mismo tiempo.»
- Version history in the disputed key: not added (not on this page; the existing «Historial de versiones» item covers
  the feature).

### 3. 2022 X 52 — ribbon path for a new comment (new item «Nuevo comentario»)

- Old: «… Mayús+F3 cambia el texto entre mayúsculas, minúsculas y tipo título. Ctrl+Alt+M inserta un comentario (fuente:
  `ms-word-atajos.html`).»
- New: «… tipo título (fuente: `ms-word-atajos.html`).» and a new item «- **Nuevo comentario**: «Revisar › Nuevo
  comentario», Ctrl+Alt+M o clic derecho en el texto › Nuevo comentario (fuente: `ms-word-comentarios.html`).»
- Source («Uso de comentarios modernos en Word», «Para agregar un comentario»): «En la pestaña Revisar , seleccione Nuevo
  comentario.»; «Presiona Ctrl + Alt + M.»; «Haga clic con el botón derecho en cualquier texto y seleccione Nuevo
  comentario en el menú contextual.»

### 4. 2022 X 56 — Contar palabras, characters with and without spaces

- **Sin fuente oficial.** `ms-word-contar-palabras.html` gives «caracteres, párrafos y líneas» only. Checked: Outlook
  «Contar el número de palabras de un mensaje de correo» («recuento de caracteres y párrafos», no spaces split); the VBA
  `WdStatistic` reference (learn.microsoft.com/es-es/office/vba/api/word.wdstatistic: «Número de caracteres incluidos
  los espacios») names the statistic but not the Contar palabras box; the rest are Q&A threads. No change.

### 5. 2024 A 53 — Barra de herramientas de acceso rápido (item; LQMC line 2)

- Old: «comandos que no dependen de la pestaña activa; por defecto encima de la cinta. …»
- New: «accesos directos a los comandos que usas con frecuencia (fuente: `ms-office-barra-acceso-rapido-teclado.html`),
  independientes de la pestaña activa; por defecto encima de la cinta. …»
- LQMC old: «… reúne comandos independientes de la pestaña activa (fuente: `ms-office-barra-acceso-rapido.html`).» New:
  «… reúne los comandos que usas con frecuencia, independientes de la pestaña activa (fuente:
  `ms-office-barra-acceso-rapido-teclado.html`, `ms-office-barra-acceso-rapido.html`).»
- Source (`ms-office-barra-acceso-rapido-teclado.html`): «La barra de herramientas de acceso rápido es una colección de
  accesos directos a las características, opciones, comandos o grupos de opciones que usa con frecuencia.»;
  (`ms-office-barra-acceso-rapido.html`): «un conjunto de comandos que son independientes de la pestaña que se muestra
  actualmente en la cinta de opciones». Caution: the keyboard page also says the bar is «oculta debajo de la cinta» by
  default; the lesson keeps the main page's «Encima de la cinta de opciones, en la barra de título (ubicación
  predeterminada)» and does not cite the keyboard page for the position.

## Restorations (v1.5: earlier cuts an exam asked)

| # | Restored | Exam row that asked it | Source passage |
|---|---|---|---|
| R1 | New item «Seleccionar»: «Inicio › Seleccionar» ofrece Seleccionar todo, Seleccionar objetos (ocultos, apilados o detrás del texto), Seleccionar todo el texto con formato similar y Panel de selección | 2020 extr. 52 (index: Inicio › Edición › Seleccionar, vigente) | `ms-word-seleccionar-objetos.html` (re-saved; downloaded and not saved in R2): «Para seleccionar todo el texto del documento, elija Seleccionar todo.»; «Para seleccionar objetos que están ocultos, apilados o detrás del texto, elija Seleccionar objetos.»; «Para seleccionar texto con formato similar, elija Seleccionar todo el texto con formato similar.»; «Para abrir el panel de tareas […] seleccione Panel de selección». Path: the HTML prints `vaya a<strong>Seleccionar</strong><strong>inicio</strong>&gt;` (a garbled «Inicio > Seleccionar»); verifier to judge. |
| R2 | New item «Opciones de impresión» in Opciones de Word (Mostrar), with the six options | 2020 ord. 53 (annulled; index: Opciones de Word: opciones de impresión) | `ms-word-opciones-mostrar.html` (already saved and cited): heading «Opciones de impresión», then «Imprimir dibujos creados en Word», «Imprimir imágenes y colores de fondo», «Imprimir propiedades del documento», «Imprimir texto oculto», «Actualizar campos antes de imprimir», «Actualizar los datos vinculados antes de imprimir». |

Not restored: cursiva (2025 A 51) and a note's text on hover (2025 A 52) — ledger «Sin fuente oficial». The other R2
cuts of this lesson (Alt tab sequences, Ctrl+F1, Autoguardado/control de cambios/notas/índice shortcuts, Interletraje,
Bloquear anclaje, PDF/A, Historial de versiones interval, QAT below the ribbon, ribbon export, combinar correspondencia
output types, Transcribir formats…) match no index row as the fact asked.

## Cuts

None.

## New sources (fuentes.yaml entries for the coordinator)

```yaml
- file: ms-word-comentarios.html
  url: "https://support.microsoft.com/es-es/word/using-modern-comments-in-word"
  title: "Microsoft, «Uso de comentarios modernos en Word»"
  consultado: "2026-10-17"
  sha256: 5ef955f30776079498b6087ef2894f7da623c0b2f6349088c9a0f1e681e6e0c3
  lessons: [m06-l04]
- file: ms-word-coautoria-documentos.html
  url: "https://support.microsoft.com/es-es/word/coauthor-documents-anywhere"
  title: "Microsoft, «Coautoría de documentos»"
  consultado: "2026-10-17"
  sha256: ebd5f17964bd7feafaff2e62377c307d7ea8dcf9ef6f19f13556a74fdcbdb258
  lessons: [m06-l04]
- file: ms-word-seleccionar-objetos.html
  url: "https://support.microsoft.com/es-es/word/select-a-shape-or-other-object-in-word"
  title: "Microsoft, «Seleccionar una forma u otro objeto de Word»"
  consultado: "2026-10-17"
  sha256: dc03a3b994040817169a24cdca2b92c20bcd6b91c6bd850d556afe13f7dc07f6
  lessons: [m06-l04]
- file: ms-office-barra-acceso-rapido-teclado.html
  url: "https://support.microsoft.com/es-es/accessibility/office-accessibility/use-a-keyboard-to-customize-the-quick-access-toolbar"
  title: "Microsoft, «Usar un teclado para personalizar la barra de herramientas de acceso rápido»"
  consultado: "2026-10-17"
  sha256: deb29f06ca0ef941a375728b39caf0242a9348b5366427ecc46da63ccab6ffcc
  lessons: [m06-l04]
```
