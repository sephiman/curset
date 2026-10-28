# Blind re-check — bloque VI part-1 sample (32), recheck-opus, 2026-10-24

Spec: `bloque-vi/verify-spec.md` with `bloque-ii/verify-spec.md` and its rulings. Every cited page re-extracted
(Python HTML-to-text) into the scratchpad folder `recheck-m06-sample/txt/`; the whole `sources/otros/` folder was
extracted, so check 2 was also searched across every saved page. Anchors: `check_anchors.py bloque-vi m06`, 0 misses on
the sample (every citation resolves to the lesson's `fuente-<file>` anchor). Existing verify reports and writer notes
not read.

| id | 1 key | 2 unique | 3 citation | 4 style | 5 not official | verdict | reason |
|---|---|---|---|---|---|---|---|
| m06-l02-q002 | ok | ok | ok | ok | ok | PASS | `ms-win-atajos.html` (Windows 11 table): «Tecla Windows + U · Abra la aplicación Configuración en la sección Accesibilidad»; Pausa, V and N rows give the three distractors. |
| m06-l02-q005 | ok | ok | ok | ok | ok | PASS | Garbled «Opcionesde inicio de sesión decuentas>» read with the ledger's decode «Configuración › Cuentas › Opciones de inicio de sesión». Same fact as conv2020 P1 45 (key Cuentas), but no official distractor carried over (Aplicaciones / Red e Internet / Sistema), so not «lightly reworded». |
| m06-l02-q012 | ok | ok | ok | ok | ok | PASS | «Mostrar detalles de la cuenta en la pantalla de inicio de sesión. Si está activada, esta opción muestra la dirección de correo electrónico de tu cuenta»; Alt+F8 row confirms the explanation's «Mostrar la contraseña en la pantalla de inicio de sesión». |
| m06-l02-q013 | ok | ok | ok | ok | ok | PASS | `ms-win-version.html`: «Iniciar>configuración>Sistema y luego Acerca de… información sobre la edición, la versión y la compilación». conv2020 P1 44 asks the path from the opposite angle; options new. |
| m06-l02-q020 | ok | ok | ok | ok | ok | PASS | Windows 11 tab: «Para iniciar el Narrador, presiona … Ctrl + Entrar. Para detener el narrador, vuelve a presionar estas teclas»; Ctrl+N (Narrador settings), Ctrl+M (`ms-win-lupa.html`), Ctrl+C (filtros de color) all elsewhere. |
| m06-l02-q038 | ok | ok | ok | ok | ok | PASS | Windows 11 tab: «Seleccione la hora & el idioma>Idioma & región … Los idiomas instalados actualmente se muestran en la sección Idioma». |
| m06-l02-q042 | ok | ok | ok | ok | ok | PASS | «El primer idioma admitido en la lista de idiomas preferidos determina el idioma que usan las aplicaciones y los sitios web de Microsoft Store». |
| m06-l02-q047 | ok | ok | ok | ok | ok | PASS | «Tecla Windows + Flecha arriba · Maximizar la ventana activa»; Alt+Flecha arriba «mitad superior», M «Minimizar todas», Flecha izquierda «Acoplar … lado izquierdo». |
| m06-l04-q004 | ok | ok | ok | ok | ok | PASS | `ms-word-atajos.html` (Windows tab): «presione Alt y, luego … E (Editar) … Aparece una notificación que le indica que está usando una tecla de acceso de una versión anterior». Different angle from conv2024_X 61. |
| m06-l04-q006 | ok | ok | ok | ok | ok | PASS | «Abrir la pestaña Referencias para agregar una tabla de contenido, notas al pie, o una tabla de citas. · Alt, S»; M, R, W rows for the distractors. |
| m06-l04-q034 | ok | ok | ok | ok | ok | PASS | Windows tab: «La revisión gramatical automática solo está disponible en Outlook, Word y PowerPoint». Note: the macOS tab of the same page says PowerPoint «no puede revisar la gramática»; the stem says only «aplicaciones de Microsoft 365». No option becomes true under the Mac reading, so it passes, but the stem would be safer naming Windows. |
| m06-l04-q036 | ok | ok | ok | ok | ok | PASS | «Desactive las casillas Marcar errores gramaticales mientras escribe y Revisar gramática con ortografía». |
| m06-l04-q042 | ok | ok | ok | ok | ok | PASS | «Insertar un comentario. · Ctrl+Alt+M»; Ctrl+Alt+I «vista previa de impresión», Alt+Mayús+C «Cerrar el Panel de revisión», Ctrl+Alt+Z «cuatro cambios anteriores». conv2022_X 52 (annulled) asked a ribbon path. |
| m06-l04-q048 | ok | ok | ok | ok | ok | PASS | `ms-word-comentarios.html`: «Para eliminar, obtener un vínculo o resolver un hilo de comentarios, seleccione Más acciones de subproceso (...)». Note: the ribbon's Revisar › Resolver exists in the product but is not «en la tarjeta» and is on no saved page. |
| m06-l04-q050 | ok | ok | ok | ok | ok | PASS | «puede agregar texto e imágenes (solo Windows). En el cuadro de comentarios no se admiten otros objetos, como tablas, ecuaciones, formas o campos»; the stem says Windows. |
| m06-l04-q056 | ok | **FAIL** | ok | FAIL | ok | FAIL | Distractor «Usar el modelo de comentarios anterior, con los comentarios clásicos» is not wrong by the page: the @mention sentence follows «Los comentarios modernos siguen funcionando como los comentarios anteriores» and does not tie @mention to modern comments. The explanation's «La @mención forma parte de la experiencia moderna, no del modelo anterior» is on no page (and classic comments did support @mentions). |
| m06-l06-q022 | ok | ok | ok | ok | ok | PASS | `ms-access-dividir.html`: «En la pestaña Herramientas de base de datos, en el grupo Mover datos, haga clic en Base de datos de Access. Se inicia el Asistente para el separador de base de datos». conv2022_X 63 gives the path and asks the effect; reversed angle, new options. |
| m06-l06-q023 | ok | ok | ok | ok | ok | PASS | «insertando _be en el nombre, justo antes de la extensión del nombre de archivo». |
| m06-l06-q033 | ok | ok | ok | ok | ok | PASS | `ms-access-graficos.html`: «En los campos numéricos y de moneda, la agregación predeterminada es Suma. En el resto de campos, la agregación predeterminada es Cuenta». |
| m06-l06-q040 | ok | ok | ok | ok | ok | PASS | «transmite rápidamente qué palabras tienen la mayor frecuencia en el origen de datos»; cascada, cajas y bigotes, radar descriptions from the same page. conv2025_X P1R 2 asks which chart is in the gallery; different angle. |
| m06-l06-q042 | ok | ok | ok | ok | ok | PASS | «Si se selecciona también un campo Leyenda (serie), Access convierte el origen de la fila en una consulta de tabla de referencias cruzadas (usando para ello la instrucción de consulta SQL TRANSFORM)». |
| m06-l06-q055 | ok | ok | ok | ok | ok | PASS | `ms-access-tipos-datos.html`, Nuevos valores: «Incrementar … Aleatorio»; Tamaño del campo and Indexado values for the distractors. |
| m06-l06-q057 | ok | ok | ok | ok | ok | PASS | «El uso más común de un campo Autonumeración es como clave principal»; «No se debe usar un campo Autonumeración para mantener un recuento de los registros». |
| m06-l06-q058 | ok | ok | ok | ok | ok | PASS | «El cálculo debe referirse a otros campos en la misma tabla». |
| m06-l03-q021 | ok | ok | ok | ok | ok | PASS | `ms-win-extensiones.html`: «accdb · Archivo de base de datos de Microsoft Access»; accde, accdt, accdr rows for the distractors. Note: the stem says «de Windows» with no version (conv2022 52 does the same for Word). |
| m06-l03-q023 | ok | **FAIL** | ok | ok | ok | FAIL | Distractor «Archivo de texto sin formato» is true of a csv on saved pages: `ms-office-formatos-archivo.html` «Guarda un libro como un archivo de texto delimitado por comas» and the Excel pages' «Importar o exportar archivos de texto (.txt o .csv)». Saying «según la lista» does not remove a reading a candidate could reasonably take. |
| m06-l03-q038 | ok | ok | ok | ok | ok | PASS | Explorer table: «F6 · Desplazarse por los elementos de la ventana»; F5, F3, F11 rows; F6/Mayús+F6 confirmed on `ms-win-explorador-lector.html`. |
| m06-l03-q052 | ok | ok | ok | ok | ok | PASS | «Ctrl+Mayús+N · Cree una carpeta nueva»; Ctrl+U, Ctrl+T, Ctrl+Mayús+E rows. |
| m06-l03-q056 | ok | ok | ok | ok | ok | PASS | «Ctrl+D / Suprimir · Eliminar el elemento seleccionado y moverlo a la papelera de reciclaje»; Mayús+Supr row for the permanent delete. Different from conv2025_X 50. |
| m06-l03-q061 | ok | ok | ok | ok | ok | PASS | «Ctrl+mouse arrastrar un archivo · Cuando suelte el archivo, cree una copia en esa ubicación»; Mayús+arrastrar moves it. conv2025_X 48 (Ctrl+Mayús, shortcut) has a different stem and key. |
| m06-l03-q063 | ok | ok | ok | ok | ok | PASS | `ms-win-comprimir.html`: «Se crea una nueva carpeta comprimida con el mismo nombre en la misma ubicación». |
| m06-l03-q065 | ok | ok | ok | ok | ok | PASS | «Para descomprimir un solo archivo o carpeta, abre la carpeta comprimida y después arrastra el archivo o carpeta … a una nueva ubicación». Note: copy and paste out of the zip also works in the product, but it is not an option and is on no saved page. |

## Summary

- Checked: 32. PASS: 30. FAIL: 2.
- FAIL by first failing check: key 0, unique 2 (m06-l04-q056, m06-l03-q023), citation 0, style 0, official 0.
- Notes that do not change a verdict: m06-l04-q034 (the page's Mac tab contradicts the key for PowerPoint; the stem
  names no platform); m06-l03-q021 and q023 name «Windows» without a version; m06-l04-q048 and m06-l03-q065 have real
  product alternatives that are on no saved page and are not among the options.
- No lesson sentence found at odds with its page in the items sampled.
