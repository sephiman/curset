# Coverage fix — m06-l02 (2026-10-17)

Lesson: `content/age-administrativo-c1/es/lessons/m06-l02.md`. Rows of `fixes.md`: 2025 A 47, 2024 X 48, 2024 X 51.
Applied under the rule change of `fix-spec.md` (requirements v1.5: no word ceiling; no cuts for length; earlier cuts an
exam asked are restored, plus the two items the coordinator named). Before: 1,500 words. After: 1,645 words (`wc -w`).
Lines ≤ 120 (except the `#` title, kept exactly). Fuentes in order of first citation (`fuentes_order.py`: in order,
nothing missing, nothing uncited).

## Fixes

### 1. 2025 A 47 — Windows Search covers apps, settings and files on the device (item «Búsqueda»)

Old:
```
- **Búsqueda**: Windows Search busca en el dispositivo, en OneDrive, Outlook y SharePoint de las cuentas
  conectadas y en la web con Bing (fuente: `ms-win-busqueda-privacidad.html`).
```
New:
```
- **Búsqueda**: Windows Search busca en el dispositivo (aplicaciones, configuraciones y archivos), en OneDrive, Outlook
  y SharePoint de las cuentas conectadas y en la web con Bing (fuente: `ms-win-busqueda-privacidad.html`).
```
Source passage (`ms-win-busqueda-privacidad.html`): «Búsqueda de Windows puede proporcionar resultados para elementos
de: / Tu dispositivo (incluyendo aplicaciones, configuraciones y archivos)». The page prints «configuraciones», not
«configuración» as `fixes.md` and `recheck-queue.md` wrote it; the lesson follows the page.

### 2. 2024 X 48 — several languages; display and keyboard languages can differ (new item «Idiomas», section «El entorno Windows. Fundamentos»)

New:
```
- **Idiomas**: «Configuración › Hora & idioma › Idioma & región»; Windows puede tener varios idiomas instalados. El
  idioma para mostrar determina el de la interfaz de usuario; la distribución del teclado puede ser de otro idioma
  (fuente: `ms-win-idioma.html`).
```
Source passages (`ms-win-idioma.html`, new; also the earlier «idiomas» cut of the ledger, now restored):
- Path: «Seleccione Inicio y elija Configuración .» / «Selecciona Hora & idioma y elige Idioma & región .» («&» as
  printed).
- Several languages: «Para comprobar qué idiomas están instalados actualmente en Windows…»; «el orden preferido actual
  de los idiomas instalados se muestra en Idiomas preferidos en la sección Idioma».
- Display language: «El idioma para mostrar de Windows determina el idioma que usa la interfaz de usuario de Windows.»
- Keyboard: «Todos los idiomas, incluido el idioma actual para mostrar de Windows, tienen distribuciones de teclado en
  varios idiomas diferentes. El idioma de visualización actual de Windows podría tener la distribución del teclado del
  teclado deseado en un idioma diferente.»; «Cambiar la distribución del teclado solo cambia el diseño y no cambia el
  idioma para mostrar de Windows.»

Sin fuente oficial: «the speech language can differ from the display language». The same page says the opposite for
speech features: «Asegúrese de que el idioma en el que se va a usar la voz está establecido como idioma para mostrar.»
Not written. (The earlier writer note said display, keyboard and voice «se configuran por separado»; the page does not
support the voice part.)

### 3. 2024 X 51 — the Registro holds system, hardware and installed-application configuration (new item «Registro», same section)

New:
```
- **Registro**: base de datos jerárquica central; contiene información que Windows consulta continuamente, como los
  perfiles de cada usuario, las aplicaciones instaladas y qué hardware existe en el sistema (fuente:
  `ms-win-registro.html`).
```
Source passages (`ms-win-registro.html`, new): «Una base de datos jerárquica central … sirve para almacenar información
necesaria para configurar el sistema para uno o varios usuarios, aplicaciones y dispositivos de hardware.» / «El
Registro contiene información que Windows consulta continuamente durante el funcionamiento, como perfiles para cada
usuario, las aplicaciones instaladas en el equipo … qué hardware existe en el sistema y los puertos que se usan.»
`ms-win-herramientas-sistema.html` (cited by m06-l03) says only «configuración de bajo nivel para Windows y para las
aplicaciones», no hardware, so a new page was needed.

## Restorations

### 4. Escala, resolución y orientación per screen (2024 ord. A 66; writer notes «Cuts») — item «Varias pantallas»

Old: `… La configuración de cada pantalla se ajusta por separado (fuente: `ms-win-varias-pantallas.html`).`
New:
```
  elementos entre pantallas) o Solo la segunda pantalla. La configuración de cada pantalla se ajusta por separado:
  resolución y diseño; la orientación, en «Escala y diseño» (fuente: `ms-win-varias-pantallas.html`).
```
Source passages (`ms-win-varias-pantallas.html`, already cited): «Después de conectarse a las pantallas externas, puede
cambiar la configuración, como la resolución, el diseño de pantalla y mucho más.» / «Para cambiarlo en Configuración
de presentación, vaya a Escala y diseño, a continuación elija suOrientación de Pantalla.» The earlier cut cited
«Cambiar la resolución de pantalla y el diseño en Windows»; not re-saved, the page already cited states it.

### 5. Dialog-box keys (coordinator decision; index: dialog boxes never asked) — item «Cuadros de diálogo»

Old: `… Ctrl+Tab cambia de pestaña. Windows+R abre …`
New:
```
- **Cuadros de diálogo**: Tab y Mayús+Tab recorren las opciones; Ctrl+Tab cambia de pestaña; Barra espaciadora marca una
  casilla; Esc descarta el cuadro. Windows+R abre el cuadro de diálogo Ejecutar (fuente: `ms-win-atajos.html`).
```
Source passages (`ms-win-atajos.html`, dialog-box table): «Barra espaciadora | Si la opción activa es una casilla,
activarla o desactivarla.»; «Esc o Escape | Detener o salir de la tarea actual, o descartar un cuadro de diálogo.»
Wording as before the cut (`recheck-queue.md` line 109).

### 6. Desktop icon sizes (coordinator decision; index: desktop icons never asked) — item «Iconos»

New (second sentence):
```
  Configuración del icono de escritorio». Clic derecho en un área vacía del escritorio › Ver: iconos grandes, medianos
  o pequeños; desactivar Mostrar iconos del escritorio los oculta (fuente: `ms-win-iconos-escritorio.html`).
```
Source passages (`ms-win-iconos-escritorio.html`): «Haga clic con el botón derecho en un área vacía del escritorio. /
Selecciona Ver y elige entre iconos grandes, medianos o pequeños para ajustar su tamaño.» / «Selecciona Ver y después
desactiva Mostrar iconos del escritorio. Esto ocultará temporalmente todos los iconos». Reworded from the cut text
(«tamaño grande, mediano o pequeño y Mostrar iconos del escritorio») to the page's own words.

Already back before this round: Narrador purpose (2024 A 46, 2020 50) and the two Impr Pant descriptions (decision 4).

Not restored: Otros usuarios / multiusuario (2024 X 49 is `función retirada`); Foco / Concentración (2020 X 46,
`función retirada`); Reconocimiento de voz replacement line (2020 50, the Reconocimiento de voz part is `función
retirada`; Acceso por voz keeps its item); Windows+L, Ctrl+Alt+Supr, Copilot Chat (Básico), Copilot data permissions,
Windows+X, Alt+arrastrar, carpetas junto al botón de encendido, «Resumir un archivo» (no exam row in the index).

## Cuts

None. A first pass of this fix cut six clauses for length (Ajustar ventanas path, «Enviar a › Escritorio», the Impr Pant
sentence with `ms-win-recortes.html`, Copilot install/location details, Copilot button/icon positions in Word and
Excel); all were undone under the rule change.

## New sources (fragment `SP/m06-l02/fuentes.yaml`, appended)

```yaml
- file: ms-win-idioma.html
  url: "https://support.microsoft.com/es-es/windows/hardware/input-devices/manage-the-language-and-keyboard-input-layout-settings-in-windows"
  title: "Microsoft, «Administrar la configuración de idioma y distribución del teclado/entrada en Windows»"
  consultado: "2026-10-17"
  sha256: e3b5934a2a24f169d3a273006ea6a4381c30f11841efc19ad252f07cbd105896
  lessons: [m06-l02]
- file: ms-win-registro.html
  url: "https://learn.microsoft.com/es-es/troubleshoot/windows-server/performance/windows-registry-advanced-users"
  title: "Microsoft, «Registro de Windows para usuarios avanzados»"
  consultado: "2026-10-17"
  sha256: 8e5c56b0f6f6f96f4391092c9d9ec62944c26a721cc02f42ce187f2baf8fa52a
  lessons: [m06-l02]
```
Both Spanish (`lang="es-ES"` / `lang="es-es"`); final URL = requested URL.

## Word count

1,645.
