# Currency check C1b, share b: Microsoft pages (`ms-*`, excluding Word, Excel, Access, Outlook)

Date 2026-10-17. Entries: 76 (every `ms-*` entry of `content/age-administrativo-c1/sources/otros/fuentes.yaml`
except `ms-word*`, `ms-excel*`, `ms-access*`, `ms-outlook*`). Live copies: `SP/currency/pages/<file>`.

Method: `curl -sL --compressed` with the spec's User-Agent and `Accept-Language: es-ES,es;q=0.9`; sha256 of the live
download compared with the stored `sha256` (every stored file still matches its recorded sha256); when different, the
`SP/pagetext.py` text of stored and live copies compared with a line diff.

Summary: identical 0, text-identical 76, changed 0, gone 0. Every page answered HTTP 200 at its own URL (no
redirect, no login wall). In 75 pages the extracted text is equal line for line; in `ms-win-paint.html` the
only differing line is the footer trace id. The sha256 differences come from per-request tokens in the HTML head.

| File | Status | HTTP / final URL | Note |
|---|---|---|---|
| `ms-learn-equipos-procesador.html` | text-identical | 200 / same URL | sha256 differs only in page tokens (awa-userFlightingId, awa-expid, request ids) |
| `ms-learn-equipos-ram.html` | text-identical | 200 / same URL | sha256 differs only in page tokens (awa-userFlightingId, awa-expid, request ids) |
| `ms-learn-equipos-almacenamiento.html` | text-identical | 200 / same URL | sha256 differs only in page tokens (awa-userFlightingId, awa-expid, request ids) |
| `ms-win32-processor-cache.html` | text-identical | 200 / same URL | sha256 differs only in page tokens (awa-userFlightingId, awa-expid, request ids) |
| `ms-sql-bits.html` | text-identical | 200 / same URL | sha256 differs only in page tokens (awa-userFlightingId, awa-expid, request ids) |
| `ms-win11-requisitos.html` | text-identical | 200 / same URL | sha256 differs only in page tokens (awa-userFlightingId, awa-expid, request ids) |
| `ms-win-uefi.html` | text-identical | 200 / same URL | sha256 differs only in page tokens (awa-userFlightingId, awa-expid, request ids) |
| `ms-win-plug-and-play.html` | text-identical | 200 / same URL | sha256 differs only in page tokens (awa-userFlightingId, awa-expid, request ids) |
| `ms-win-dispositivos-entrada.html` | text-identical | 200 / same URL | sha256 differs only in page tokens (awa-userFlightingId, awa-expid, request ids) |
| `ms-sql-server.html` | text-identical | 200 / same URL | sha256 differs only in page tokens (awa-userFlightingId, awa-expid, request ids) |
| `ms-win-ntfs.html` | text-identical | 200 / same URL | sha256 differs only in page tokens (awa-userFlightingId, awa-expid, request ids) |
| `ms-win-sistemas-archivos.html` | text-identical | 200 / same URL | sha256 differs only in page tokens (awa-userFlightingId, awa-expid, request ids) |
| `ms-win-tolerancia-errores.html` | text-identical | 200 / same URL | sha256 differs only in page tokens (awa-userFlightingId, awa-expid, request ids) |
| `ms-win-copias-seguridad.html` | text-identical | 200 / same URL | sha256 differs only in page tokens (awa-userFlightingId, awa-expid, request ids) |
| `ms-win-componentes-kernel.html` | text-identical | 200 / same URL | sha256 differs only in page tokens (awa-userFlightingId, awa-expid, request ids) |
| `ms-win-antivirus.html` | text-identical | 200 / same URL | sha256 differs only in page tokens (awa-userFlightingId, awa-expid, request ids) |
| `ms-win-firewall.html` | text-identical | 200 / same URL | sha256 differs only in page tokens (awa-userFlightingId, awa-expid, request ids) |
| `ms-cuenta-mfa.html` | text-identical | 200 / same URL | sha256 differs only in page tokens (awa-userFlightingId, awa-expid, request ids) |
| `ms-win-update.html` | text-identical | 200 / same URL | sha256 differs only in page tokens (awa-userFlightingId, awa-expid, request ids) |
| `ms-win-atajos.html` | text-identical | 200 / same URL | sha256 differs only in page tokens (awa-userFlightingId, awa-expid, request ids) |
| `ms-win-opciones-inicio-sesion.html` | text-identical | 200 / same URL | sha256 differs only in page tokens (awa-userFlightingId, awa-expid, request ids) |
| `ms-win-version.html` | text-identical | 200 / same URL | sha256 differs only in page tokens (awa-userFlightingId, awa-expid, request ids) |
| `ms-win-narrador.html` | text-identical | 200 / same URL | sha256 differs only in page tokens (awa-userFlightingId, awa-expid, request ids) |
| `ms-win-lupa.html` | text-identical | 200 / same URL | sha256 differs only in page tokens (awa-userFlightingId, awa-expid, request ids) |
| `ms-cortana-fin-soporte.html` | text-identical | 200 / same URL | sha256 differs only in page tokens (awa-userFlightingId, awa-expid, request ids) |
| `ms-win-acoplar.html` | text-identical | 200 / same URL | sha256 differs only in page tokens (awa-userFlightingId, awa-expid, request ids) |
| `ms-win-iconos-escritorio.html` | text-identical | 200 / same URL | sha256 differs only in page tokens (awa-userFlightingId, awa-expid, request ids) |
| `ms-onedrive-restaurar.html` | text-identical | 200 / same URL | sha256 differs only in page tokens (awa-userFlightingId, awa-expid, request ids) |
| `ms-win-barra-tareas.html` | text-identical | 200 / same URL | sha256 differs only in page tokens (awa-userFlightingId, awa-expid, request ids) |
| `ms-win-notificaciones.html` | text-identical | 200 / same URL | sha256 differs only in page tokens (awa-userFlightingId, awa-expid, request ids) |
| `ms-win-escritorios.html` | text-identical | 200 / same URL | sha256 differs only in page tokens (awa-userFlightingId, awa-expid, request ids) |
| `ms-win-varias-pantallas.html` | text-identical | 200 / same URL | sha256 differs only in page tokens (awa-userFlightingId, awa-expid, request ids) |
| `ms-win-menu-inicio.html` | text-identical | 200 / same URL | sha256 differs only in page tokens (awa-userFlightingId, awa-expid, request ids) |
| `ms-win-busqueda-privacidad.html` | text-identical | 200 / same URL | sha256 differs only in page tokens (awa-userFlightingId, awa-expid, request ids) |
| `ms-copilot-windows.html` | text-identical | 200 / same URL | sha256 differs only in page tokens (awa-userFlightingId, awa-expid, request ids) |
| `ms-copilot-introduccion.html` | text-identical | 200 / same URL | sha256 differs only in page tokens (awa-userFlightingId, awa-expid, request ids) |
| `ms-win-explorador.html` | text-identical | 200 / same URL | sha256 differs only in page tokens (awa-userFlightingId, awa-expid, request ids) |
| `ms-win-explorador-lector.html` | text-identical | 200 / same URL | sha256 differs only in page tokens (awa-userFlightingId, awa-expid, request ids) |
| `ms-win-extensiones.html` | text-identical | 200 / same URL | sha256 differs only in page tokens (awa-userFlightingId, awa-expid, request ids) |
| `ms-dotnet-rutas-unc.html` | text-identical | 200 / same URL | sha256 differs only in page tokens (awa-userFlightingId, awa-expid, request ids) |
| `ms-win-comprimir.html` | text-identical | 200 / same URL | sha256 differs only in page tokens (awa-userFlightingId, awa-expid, request ids) |
| `ms-win-compartir-red.html` | text-identical | 200 / same URL | sha256 differs only in page tokens (awa-userFlightingId, awa-expid, request ids) |
| `ms-win-indexacion.html` | text-identical | 200 / same URL | sha256 differs only in page tokens (awa-userFlightingId, awa-expid, request ids) |
| `ms-win-aqs.html` | text-identical | 200 / same URL | sha256 differs only in page tokens (awa-userFlightingId, awa-expid, request ids) |
| `ms-win-desuso.html` | text-identical | 200 / same URL | sha256 differs only in page tokens (awa-userFlightingId, awa-expid, request ids) |
| `ms-win-bloc-notas.html` | text-identical | 200 / same URL | sha256 differs only in page tokens (awa-userFlightingId, awa-expid, request ids) |
| `ms-win-recortes.html` | text-identical | 200 / same URL | sha256 differs only in page tokens (awa-userFlightingId, awa-expid, request ids) |
| `ms-win-paint.html` | text-identical | 200 / same URL | page tokens; extracted text differs only in the footer «This is the Trace Id: …» line |
| `ms-win-calculadora.html` | text-identical | 200 / same URL | sha256 differs only in page tokens (awa-userFlightingId, awa-expid, request ids) |
| `ms-win-reloj.html` | text-identical | 200 / same URL | sha256 differs only in page tokens (awa-userFlightingId, awa-expid, request ids) |
| `ms-win-asistencia-rapida.html` | text-identical | 200 / same URL | sha256 differs only in page tokens (awa-userFlightingId, awa-expid, request ids) |
| `ms-win-herramientas-windows.html` | text-identical | 200 / same URL | sha256 differs only in page tokens (awa-userFlightingId, awa-expid, request ids) |
| `ms-win-herramientas-sistema.html` | text-identical | 200 / same URL | sha256 differs only in page tokens (awa-userFlightingId, awa-expid, request ids) |
| `ms-win-unidad-recuperacion.html` | text-identical | 200 / same URL | sha256 differs only in page tokens (awa-userFlightingId, awa-expid, request ids) |
| `ms-win-historial-archivos.html` | text-identical | 200 / same URL | sha256 differs only in page tokens (awa-userFlightingId, awa-expid, request ids) |
| `ms-office-ortografia.html` | text-identical | 200 / same URL | sha256 differs only in page tokens (awa-userFlightingId, awa-expid, request ids) |
| `ms-office-traducir.html` | text-identical | 200 / same URL | sha256 differs only in page tokens (awa-userFlightingId, awa-expid, request ids) |
| `ms-office-recorte-pantalla.html` | text-identical | 200 / same URL | sha256 differs only in page tokens (awa-userFlightingId, awa-expid, request ids) |
| `ms-office-formatos-archivo.html` | text-identical | 200 / same URL | sha256 differs only in page tokens (awa-userFlightingId, awa-expid, request ids) |
| `ms-office-autoguardado.html` | text-identical | 200 / same URL | sha256 differs only in page tokens (awa-userFlightingId, awa-expid, request ids) |
| `ms-office-pdf.html` | text-identical | 200 / same URL | sha256 differs only in page tokens (awa-userFlightingId, awa-expid, request ids) |
| `ms-office-barra-acceso-rapido.html` | text-identical | 200 / same URL | sha256 differs only in page tokens (awa-userFlightingId, awa-expid, request ids) |
| `ms-office-cinta.html` | text-identical | 200 / same URL | sha256 differs only in page tokens (awa-userFlightingId, awa-expid, request ids) |
| `ms-win-ping.html` | text-identical | 200 / same URL | sha256 differs only in page tokens (awa-userFlightingId, awa-expid, request ids) |
| `ms-edge-consola-javascript.html` | text-identical | 200 / same URL | sha256 differs only in page tokens (awa-userFlightingId, awa-expid, request ids) |
| `ms-edge-atajos.html` | text-identical | 200 / same URL | sha256 differs only in page tokens (awa-userFlightingId, awa-expid, request ids) |
| `ms-edge-inprivate.html` | text-identical | 200 / same URL | sha256 differs only in page tokens (awa-userFlightingId, awa-expid, request ids) |
| `ms-edge-extensiones.html` | text-identical | 200 / same URL | sha256 differs only in page tokens (awa-userFlightingId, awa-expid, request ids) |
| `ms-azure-mysql.html` | text-identical | 200 / same URL | sha256 differs only in page tokens (awa-userFlightingId, awa-expid, request ids) |
| `ms-mineria-datos.html` | text-identical | 200 / same URL | sha256 differs only in page tokens (awa-userFlightingId, awa-expid, request ids) |
| `ms-office-barra-acceso-rapido-teclado.html` | text-identical | 200 / same URL | sha256 differs only in page tokens (awa-userFlightingId, awa-expid, request ids) |
| `ms-win-analisis-cpu.html` | text-identical | 200 / same URL | sha256 differs only in page tokens (awa-userFlightingId, awa-expid, request ids) |
| `ms-win-directivas-explorador.html` | text-identical | 200 / same URL | sha256 differs only in page tokens (awa-userFlightingId, awa-expid, request ids) |
| `ms-win-idioma.html` | text-identical | 200 / same URL | sha256 differs only in page tokens (awa-userFlightingId, awa-expid, request ids) |
| `ms-win-info-dispositivo.html` | text-identical | 200 / same URL | sha256 differs only in page tokens (awa-userFlightingId, awa-expid, request ids) |
| `ms-win-registro.html` | text-identical | 200 / same URL | sha256 differs only in page tokens (awa-userFlightingId, awa-expid, request ids) |

## Changed or gone pages

None. No citation is affected.

## Points checked by request

The three pages below are text-identical to the stored copies; the live text on the asked points:

### `ms-win-atajos.html` (Impr Pant)

Cited in `es/lessons/m06-l02.md` (l. 71-73 and 116): «Windows+Impr Pant guarda la pantalla completa en Imágenes ›
Capturas de pantalla» and «Impr Pant … deja seleccionar una zona y la copia al portapapeles». Verdict: holds.

- Windows 11 table: «Impr Scn o Impr Pant | Seleccione una zona de la pantalla para hacer una captura de pantalla en
  el portapapeles. A continuación, puedes abrir la herramienta Recortes para compartir o aumentar la imagen.» with the
  note «Puede desactivar este comportamiento predeterminado. Selecciona Inicio>,configuración>,Accesibilidad>,Teclado y
  establece Usar el botón Imprimir pantalla para abrir el recorte de pantalla en Desactivado.»
- Windows 11 table: «Tecla Windows + PrtScn | Capture una captura de pantalla completa y guárdela en un archivo en la
  subcarpeta Capturas de pantalla de la carpeta Imágenes.»
- Windows 11 table: «Alt+Impr Pant | Capture una captura de pantalla de la ventana activa y cópiela en el
  Portapapeles.»
- Windows 10 table (same page): «PrtScn | Tomar una captura de pantalla de la pantalla completa y copiarla en el
  Portapapeles.» So the page itself carries both behaviours, split by version.

### `ms-win-recortes.html` (Impr Pant)

Cited in `es/lessons/m06-l02.md` (l. 73-74): Impr Pant «copia la pantalla completa al portapapeles». Verdict: holds.

- Windows 11 section: «Presione Imprimir pantalla (PrtSc) para obtener una instantánea de imagen estática de toda la
  pantalla y colóquela en el portapapeles.»
- Windows 10 section: «Presione Imprimir pantalla (PrtSc).» (as a way to open the snipping overlay) and «Presione las
  teclas Ctrl + PrtSc. Toda la pantalla adquirirá un color gris, incluido el menú abierto.»

The two Microsoft pages still disagree for Windows 11 (zone selection vs whole screen to clipboard), which is what the
lesson already says.

### `ms-win-idioma.html` (speech language vs display language)

Cited in `es/lessons/m06-l02.md` (l. 19-21): «Configuración › Hora & idioma › Idioma & región»; varios idiomas; el
idioma para mostrar determina el de la interfaz; la distribución del teclado puede ser de otro idioma. Verdict: holds
(text unchanged).

- «Con la aplicación Configuración, puedes: Instalar y quitar idiomas. Cambiar el idioma de visualización de Windows.
  Cambiar el idioma que usan las aplicaciones y los sitios web de Microsoft Store. Agregar características de voz a un
  idioma. Agregar y quitar diseños de teclado/entrada.»
- Menu path (Windows 11): «Seleccione la hora & el idioma>Idioma & región .»
- Speech vs display (Windows 11 and Windows 10 sections, same wording): «Instalar la voz de un idioma … Asegúrese de
  que el idioma en el que se va a usar la voz está establecido como idioma para mostrar.» Then (Windows 11) «seleccione
  el botón Descargar junto a cada característica de voz deseada … Texto a voz. Reconocimiento de voz básico.
  Reconocimiento de voz mejorado.» and «No todos los idiomas tienen características de voz.»
  So the page ties the speech features to the language set as display language; it does not describe a separate speech
  language setting.
