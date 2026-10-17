# Bloque VI coverage fixes — confirmation (2026-10-17)

Read-only check of the coverage fixes made earlier today for bloque VI. I did not redo the audit. Inputs are in
`docs/age-verification/bloque-vi/coverage/`: `fixes.md`, `fix-m06-lNN.md`, `verify-fix-m06-lNN.md`,
`recheck-queue.md` and `recheck.md`. The lessons were read as they stand in
`content/age-administrativo-c1/es/lessons/` (committed in HEAD 9cf1a22, with no working-tree diff under `content/`).
Each quote was matched verbatim after joining the wrapped lines.

For each source, I checked that the cited file exists in `content/age-administrativo-c1/sources/otros/` and that it
has an entry in `fuentes.yaml`. I compared that entry's sha256 with `sha256sum` of the file and checked that its
`lessons` list names the lesson. Every cited file passed all four checks, so the column below gives only the file
names. For short filenames, «VF» stands for `verify-fix-m06-lNN.md` and «RC» for `recheck.md`.

## m06-l08: no verify file

There is no `verify-fix-m06-l08.md`, and that is correct. `verify-fix-m06-l06.md` is titled «… m06-l06 …, with the
m06-l08 check». Its section «m06-l08 (claims of `fix-m06-l08.md`)» has 2 PASS rows: «No restorable cut an exam asked»
and «Lesson unchanged by this pass». This matches the ledger's «m06-l06 22/24 (with the m06-l08 check)». m06-l08 has
no row in `fixes.md`, and `fix-m06-l08.md` lists no additions or restorations.

## Table

| Lesson | Fix | In lesson (quote) | Verified (file, row) | Source ok | Status |
|---|---|---|---|---|---|
| m06-l01 | 2025 A 41: the processor interprets and executes instructions | «Puede interpretar una secuencia de instrucciones (fuente: `ms-win32-processor-cache.html`) y el sistema operativo lo usa para ejecutar instrucciones de programa»; LQMC «El procesador interpreta instrucciones y con él se ejecutan las de los programas» | VF-l01 rows 1, 1, 1, 1b: PASS | `ms-win32-processor-cache.html`, `ms-win-analisis-cpu.html` | confirmed (the «obtiene» part is on the sin fuente oficial list) |
| m06-l01 | 2024 A 43: Excel is an Office app (also a restoration) | «**Aplicaciones de Office**: PowerPoint y Excel, entre otras» | VF-l01 rows 2, 2: PASS | `ms-office-autoguardado.html` (lessons include m06-l01) | confirmed |
| m06-l01 | Restoration: MySQL (2020 ord. 41) | «MySQL es un motor de base de datos (fuente: `ms-azure-mysql.html`)» | VF-l01 row 3: PASS | `ms-azure-mysql.html` | confirmed |
| m06-l01 | Restoration: Minería de datos (2020 extr. 43) | «**Minería de datos**: proceso de detectar información accionable de grandes conjuntos de datos; usa análisis matemáticos para derivar patrones y tendencias» | VF-l01 row 4: PASS | `ms-mineria-datos.html` | confirmed |
| m06-l02 | 2025 A 47: Windows Search covers apps, settings and files | «Windows Search busca en el dispositivo (aplicaciones, configuraciones y archivos), en OneDrive, Outlook y SharePoint…» | VF-l02 rows 1, 1: PASS | `ms-win-busqueda-privacidad.html` | confirmed |
| m06-l02 | 2024 X 48: several languages, keyboard can differ (also a restoration) | «**Idiomas**: «Configuración › Hora & idioma › Idioma & región»; Windows puede tener varios idiomas instalados. El idioma para mostrar determina el de la interfaz de usuario; la distribución del teclado puede ser de otro idioma» | VF-l02 rows 2 (×5): PASS | `ms-win-idioma.html` | confirmed (the speech part is on the sin fuente oficial list) |
| m06-l02 | 2024 X 51: the Registro | «**Registro**: base de datos jerárquica central; contiene información que Windows consulta continuamente, como los perfiles de cada usuario, las aplicaciones instaladas y qué hardware existe en el sistema» | VF-l02 rows 3, 3: PASS | `ms-win-registro.html` | confirmed |
| m06-l02 | Restoration: settings for each screen (2024 A 66) | «La configuración de cada pantalla se ajusta por separado: resolución y diseño; la orientación, en «Escala y diseño»» | VF-l02 row 4: PASS | `ms-win-varias-pantallas.html` | confirmed |
| m06-l02 | Restoration (coordinator): dialog-box keys | «Barra espaciadora marca una casilla; Esc descarta el cuadro.» | VF-l02 row 5: PASS | `ms-win-atajos.html` | confirmed |
| m06-l02 | Restoration (coordinator): desktop icon sizes | «Clic derecho en un área vacía del escritorio › Ver: iconos grandes, medianos o pequeños; desactivar Mostrar iconos del escritorio los oculta» | VF-l02 row 6: PASS | `ms-win-iconos-escritorio.html` | confirmed |
| m06-l03 | 2025 X 50: deleted files that do not go to the Papelera | Item: «Con la directiva «No mover archivos eliminados a la papelera de reciclaje» habilitada, lo que eliminas en el Explorador de archivos no va a la Papelera y se elimina permanentemente»; LQMC: «con la directiva … habilitada, lo que eliminas en el Explorador tampoco va a la Papelera (fuente: `ms-win-directivas-explorador.html`)» | VF-l03 rows 1b, 1c: PASS. Row 1d (LQMC): FAIL, then RC row 6: PASS. Wrap RC F1: FAIL; the lesson's line 124 is now joined | `ms-win-directivas-explorador.html`, `ms-win-atajos.html` | confirmed (the per-drive setting is on the sin fuente oficial list) |
| m06-l03 | Restoration R2: OneDrive Papelera | «los archivos de OneDrive eliminados de la nube no aparecen en la Papelera de reciclaje del equipo» | VF-l03 row 1a: PASS | `ms-onedrive-restaurar.html` | confirmed |
| m06-l03 | 2024 X 57: search locations, OneDrive | «Las ubicaciones de búsqueda incluyen o excluyen carpetas concretas; con la búsqueda de contenido en la nube activada, Windows Search muestra elementos de tu OneDrive personal»; LQMC «…Windows Search muestra elementos de OneDrive» | VF-l03 rows 2a, 2c, 2d: PASS | `ms-win-busqueda-privacidad.html` (lessons include m06-l03), `ms-win-indexacion.html` | confirmed |
| m06-l03 | Restoration R3: cloud search from Inicio del Explorador | «Desde Inicio del Explorador se busca en el PC y en la nube, con las cuentas en la nube iniciadas en «Configuración › Cuentas»» | VF-l03 row 2b: PASS | `ms-win-explorador.html` | confirmed |
| m06-l03 | 2025 A 50: Asistencia rápida | «Usa una conexión remota: quien ayuda comparte un código de 6 dígitos y, si la otra persona lo permite, ve su pantalla o controla su equipo; el control total se pide con «Solicitar control»» | VF-l03 rows 3a, 3b: PASS. Form «Voice»: FAIL, then RC row 7: PASS | `ms-win-asistencia-rapida.html` | confirmed |
| m06-l03 | Restoration R1: contents of Acerca de (2020 ord. 44) | «Muestra el nombre y el modelo del dispositivo; en «Especificaciones de Windows», la edición y la versión; en «Especificaciones del dispositivo», el tipo de procesador, la RAM instalada y si Windows es de 32 o 64 bits» | VF-l03 row R1: PASS | `ms-win-info-dispositivo.html` | confirmed |
| m06-l04 | 2025 X 51: red wavy underline, dictionary | «Línea ondulada roja, posible error ortográfico; azul, gramatical. Si marca como incorrecta una palabra escrita como quieres, «Agregar al diccionario» hace que no vuelva a marcarla»; LQMC «…«Agregar al diccionario» evita que vuelva a marcar una palabra bien escrita» | VF-l04 rows 1a, 1b, 1c: PASS | `ms-office-ortografia.html` | confirmed («no está en el diccionario» is on the sin fuente oficial list) |
| m06-l04 | 2025 X 53: co-authoring in OneDrive/SharePoint | «**Coautoría**: guarda el documento en OneDrive o SharePoint y compártelo para trabajar en él a la vez» | VF-l04 rows 2a, 2b: PASS | `ms-word-coautoria-documentos.html`, `ms-word-coautoria.html` | confirmed |
| m06-l04 | 2022 X 52: ribbon path for a new comment | «**Nuevo comentario**: «Revisar › Nuevo comentario», Ctrl+Alt+M o clic derecho en el texto › Nuevo comentario» | VF-l04 rows 3a, 3b, 3c: PASS | `ms-word-comentarios.html`, `ms-word-atajos.html` | confirmed |
| m06-l04 | 2022 X 56: Contar palabras, characters with and without spaces | Not stated. The item says only «da también caracteres, párrafos y líneas» | VF-l04 row 4: PASS (the «no change» is correct: sin fuente oficial) | `ms-word-contar-palabras.html` (unchanged) | **missing** (no fix was applied: sin fuente oficial, as recorded) |
| m06-l04 | 2024 A 53: QAT holds frequently used commands | «accesos directos a los comandos que usas con frecuencia (fuente: `ms-office-barra-acceso-rapido-teclado.html`), independientes de la pestaña activa»; «Las páginas de Microsoft dan dos ubicaciones predeterminadas: encima de la cinta, en la barra de título (…), y oculta debajo de la cinta (…)»; LQMC «reúne los comandos que usas con frecuencia, independientes de la pestaña activa» | VF-l04 rows 5a, 5c: PASS. Row 5b: FAIL, then RC row 8: PASS | `ms-office-barra-acceso-rapido-teclado.html`, `ms-office-barra-acceso-rapido.html` | confirmed |
| m06-l04 | Restoration R1: Seleccionar (2020 extr. 52) | «**Seleccionar**: «Inicio › Seleccionar» ofrece Seleccionar todo, Seleccionar objetos (ocultos, apilados o detrás del texto), Seleccionar todo el texto con formato similar y Panel de selección» | VF-l04 row R1: PASS | `ms-word-seleccionar-objetos.html` | confirmed |
| m06-l04 | Restoration R2: Opciones de impresión (2020 ord. 53) | «**Opciones de impresión**: en Opciones de Word (Mostrar): Imprimir dibujos creados en Word, … y Actualizar los datos vinculados antes de imprimir» | VF-l04 row R2: PASS | `ms-word-opciones-mostrar.html` | confirmed |
| m06-l05 | 2024 X 63: DIVIDIRTEXTO spills its output | «DIVIDIRTEXTO desborda el texto entre columnas o hacia abajo por filas» | VF-l05 row 1: PASS | `ms-excel-funcion-dividirtexto.html` | confirmed |
| m06-l05 | 2022 54: #¿NOMBRE? | «**#¿NOMBRE?**: sale por un error ortográfico en el nombre de la fórmula, un nombre no definido o un texto sin comillas dobles» | VF-l05 row 2: PASS | `ms-excel-error-nombre.html` | confirmed |
| m06-l05 | Restoration: EXTRAE syntax (2020 ord. 60) | «EXTRAE(texto; posición_inicial; núm_de_caracteres): el primer carácter del texto es la posición 1» | VF-l05 row 3: PASS | `ms-excel-funcion-extrae.html` | confirmed |
| m06-l06 | Restoration: SiInm (2020 ord. 61) | «**SiInm**: recibe tres argumentos: una expresión, el valor que devuelve si es verdadera y el que devuelve si es falsa» | VF-l06 rows 1, 1: PASS | `ms-access-expresiones.html` | confirmed |
| m06-l06 | Restoration: Campo calculado (2020 ord. 62) | «columna de la consulta con el resultado de una expresión (…). La expresión va precedida del nombre que quieres para el campo de salida, seguido de dos puntos (fuente: `ms-access-consulta-seleccion.html`)». The old «lo que va delante de los dos puntos…» is gone | VF-l06 row 2 (definition): PASS. Row 2 (dos puntos): FAIL, then RC row 9: PASS | `ms-access-expresiones.html`, `ms-access-consulta-seleccion.html` (sha b766e20d…, as in RC), `ms-access-consultas.html` | confirmed |
| m06-l06 | Restoration: Año (2020 ord. 62) | «**Año**: devuelve un número entero que representa el año de una fecha» | VF-l06 row 2 (Año): PASS. Row 2 (2020 ord. 62 stated) was conditional, and RC row 9 met the condition | `ms-access-funcion-ano.html` | confirmed |
| m06-l06 | Restoration: Control calculado (2020 ord. 64) | «la expresión se escribe en la propiedad ControlSource del control, no en un campo de tabla o consulta (…). En la vista Diseño de un formulario, el origen de control de un cuadro de texto se edita en el propio cuadro, sin la hoja de propiedades» | VF-l06 row 3 (ControlSource): PASS. Row 3 (vista Diseño): FAIL, then RC row 10: PASS | `ms-access-expresiones.html`, `ms-access-formularios.html` | confirmed |
| m06-l06 | Restoration: Conmutador (2020 ord. 64) | «**Conmutador**: recibe pares de expresión y valor; evalúa las expresiones de izquierda a derecha y devuelve el valor de la primera verdadera» | VF-l06 rows 3 (Conmutador), 3 (2020 ord. 64): PASS | `ms-access-funcion-conmutador.html` | confirmed |
| m06-l06 | Restoration: Texto largo 65.535 (2022 ord. 57, anulada) | «en un campo Texto largo, 65.535 caracteres al introducir los datos en la interfaz de usuario» | VF-l06 row 4: PASS | `ms-access-especificaciones.html` | confirmed |
| m06-l07 | 2025 A 63: server, «@», SMTP | «El correo saliente va por SMTP. El proveedor da los nombres del servidor de correo entrante (IMAP o POP) y del saliente (SMTP)»; «**Dirección de correo**: una cadena que se interpreta localmente, el signo «@» y un dominio de Internet» | VF-l07 rows 1, 2: PASS | `ms-outlook-imap-pop.html`, `rfc5322-formato-mensaje.txt` | confirmed |
| m06-l07 | 2025 A 66: group address, members, public/private | «una dirección de correo del grupo…»; «Cualquier persona de la organización puede iniciar una conversación de grupo. En Outlook clásico, todos los miembros reciben el correo enviado al grupo. En un grupo público, cualquier persona de la organización lee y responde sus conversaciones; en uno privado, solo los miembros» | VF-l07 row 4: PASS. Row 3: FAIL, then RC rows 1, 5: PASS | `ms-outlook-grupos.html`, `ms-outlook-grupo-enviar.html` | confirmed |
| m06-l07 | 2022 62: first step, add an account | «Una cuenta se agrega en «Archivo › Agregar cuenta»; si nunca abriste Outlook, sale la pantalla principal, donde escribes tu dirección de correo y seleccionas Conectar» | VF-l07 row 5: PASS | `ms-outlook-agregar-cuenta.html` | confirmed («primer paso» as wording is on the sin fuente oficial list) |
| m06-l07 | Restoration: Gráficos (2020 X 64) | «**Gráficos** (Outlook clásico): en el cuerpo del mensaje, «Insertar › Ilustraciones › Gráfico»; los datos se escriben en la hoja de cálculo de Excel que aparece» | VF-l07 row 6: FAIL, then RC row 2: PASS | `ms-outlook-graficos.html` | confirmed |
| m06-l07 | Restoration: Limpiar (2020 X 66) | «**Limpiar** (Outlook clásico): con la cinta clásica, «Inicio › Eliminar › Limpiar»; … eliminan los mensajes redundantes, que van por defecto a Elementos eliminados» | VF-l07 row 7: FAIL, then RC row 3: PASS | `ms-outlook-limpiar-conversacion.html` | confirmed |
| m06-l07 | Restoration: Correo no deseado (2020 X 61) | «**Correo no deseado** (Outlook clásico): «Inicio › Eliminar › Bloquear › Opciones de correo electrónico no deseado». El nivel predeterminado es Sin filtrado automático; … Solo listas seguras, el más restrictivo» | VF-l07 row 8: FAIL, then RC row 4: PASS | `ms-outlook-correo-no-deseado.html` | confirmed |
| m06-l07 | Restoration: Carpetas de búsqueda (2020 X 63) | «**Carpetas de búsqueda**: carpetas virtuales con los mensajes que cumplen unos criterios, sin moverlos ni duplicarlos. En Outlook clásico, «Carpeta › Nuevo › Nueva carpeta de búsqueda»» | VF-l07 row 9: PASS | `ms-outlook-carpetas-busqueda.html` | confirmed |
| m06-l07 | Restoration: grupos de envío y recepción (2020 X P1R 1) | «Un grupo de envío y recepción contiene una colección de cuentas y carpetas; se programa cada n minutos o al salir de Outlook» | VF-l07 row 10: PASS (note) | `ms-outlook-grupos-envio-recepcion.html` | confirmed |
| m06-l07 | Restoration: F4 (2020 X 68) | «en Outlook clásico, Ctrl+E o F3 busca, F4 busca un texto en un elemento abierto» | VF-l07 row 11: PASS (note: wrap). The item was re-wrapped, RC row 5: PASS | `ms-outlook-atajos.html` | confirmed |

## Counts

- Fixes checked: 41. That is 18 rows of `fixes.md` plus 23 additions or restorations from the `fix-m06-lNN.md` files.
  Two restorations, «Aplicaciones de Office» (m06-l01) and «Idiomas» (m06-l02), are the same text as a `fixes.md`
  row, so each is counted once.
- Confirmed: 40. Missing: 1. Unverified: 0.
- Verification FAILs on these fixes: 10, all fixed in the lessons. 9 were content FAILs and passed in `recheck.md`
  rows 1–4 and 6–10. The 10th was the m06-l03 Voice FAIL for Asistencia rápida, which passed in RC row 7. Separately,
  RC form row F1 (a line wrap in m06-l03) is fixed in the lesson.
- Sources: 51 cited (file, lesson) pairs checked. All exist, all are indexed, every sha256 matches, and every entry
  lists its lesson. `sources/otros/` has 233 files besides `fuentes.yaml`, and `fuentes.yaml` has 233 entries.
- m06-l08: confirmed. It was checked in `verify-fix-m06-l06.md`, section «m06-l08», 2 PASS.

## Problems found

1. **m06-l04, 2022 X 56 (Contar palabras, characters with and without spaces): no text in the lesson.** This was a
   documented choice, not a lapse. `fix-m06-l04.md` §4 records the fact as «Sin fuente oficial». `verify-fix-m06-l04.md`
   row 4 passes that «no change», and the ledger's sin fuente oficial list names it. The audit's partial on that row is
   still open.
2. Some fixes are confirmed for only part of the asked fact. The missing parts are on the ledger's sin fuente oficial
   list, so the lessons are not wrong, but those rows are not fully covered:
   - 2025 A 41: «obtiene».
   - 2024 X 48: the speech language.
   - 2025 X 50: the per-drive Papelera setting.
   - 2025 X 51: «no está en el diccionario».
   - 2022 62: «primer paso».
3. Minor: the m06-l03 wrap fix (RC form row F1) has no blind re-check recorded after it was made. `recheck.md` ends
   with F1 as FAIL. I confirmed the result directly: the lesson's line 124 now reads
   `  (fuente: \`ms-win-directivas-explorador.html\`).`
