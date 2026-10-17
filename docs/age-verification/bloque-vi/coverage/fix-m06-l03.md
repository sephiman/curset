# Fix — m06-l03 (2026-10-17)

Rows of `fixes.md` for m06-l03, applied under the v1.5 rule change (no word ceiling): nothing was cut. Lesson:
`content/age-administrativo-c1/es/lessons/m06-l03.md`. Word count (`wc -w`): 1494 → **1715**. Lines ≤ 120 except the
`#` title line (unchanged). Fuentes reordered by first citation (`fuentes_order.py`: in order, none missing, none
uncited).

## Changes

### 1. 2025 X 50 — Papelera not used (item «Papelera de reciclaje»; LQMC line 10)

- Old: «- **Papelera de reciclaje**: Restaurar devuelve el archivo a su carpeta original (fuente:
  `ms-onedrive-restaurar.html`).»
- New: «… Restaurar devuelve el archivo a su carpeta original; los archivos de OneDrive eliminados de la nube no aparecen
  en la Papelera de reciclaje del equipo (fuente: `ms-onedrive-restaurar.html`). Con la directiva «No mover archivos
  eliminados a la papelera de reciclaje» habilitada, lo que eliminas en el Explorador de archivos no va a la Papelera y
  se elimina permanentemente (fuente: `ms-win-directivas-explorador.html`).»
- LQMC old: «Mayús+Supr elimina sin pasar por la Papelera de reciclaje (fuente: `ms-win-atajos.html`).» New: same, plus
  «; con la directiva «No mover archivos eliminados a la papelera de reciclaje», lo eliminado tampoco va a la Papelera
  (fuente: `ms-win-directivas-explorador.html`).»
- Source (`ms-win-directivas-explorador.html`, NoRecycleFiles): «Cuando se elimina un archivo o carpeta en Explorador de
  archivos, se coloca una copia del archivo o carpeta en la Papelera de reciclaje. […] Si habilita esta configuración,
  los archivos y carpetas que se eliminan mediante Explorador de archivos no se colocarán en la Papelera de reciclaje y,
  por tanto, se eliminarán permanentemente.»; «Nombre descriptivo | No mover archivos eliminados a la papelera de
  reciclaje».
- OneDrive clause = restoration R2 below.
- **Sin fuente oficial**: the *per-drive* Recycle Bin property («No mover archivos a la Papelera de reciclaje. Quitar
  los archivos inmediatamente al eliminarlos», set per unit in Propiedades de la Papelera). Searched support.microsoft.com
  and learn.microsoft.com (es-es, en-us): Q&A threads and third-party blogs only. The lesson states the policy form
  (same effect: deleted from the Explorer, not in the Papelera, permanent) and not the per-drive setting.

### 2. 2024 X 57 — search locations, OneDrive (item «Buscar en Windows»; LQMC line 9)

- Old: «… Mejorado indexa todo el equipo y puede usar más recursos (fuente: `ms-win-indexacion.html`).»
- New: same, then «Las ubicaciones de búsqueda incluyen o excluyen carpetas concretas; con la búsqueda de contenido en
  la nube activada, Windows Search muestra elementos de tu OneDrive personal (fuente:
  `ms-win-busqueda-privacidad.html`). Desde Inicio del Explorador se busca en el PC y en la nube, con las cuentas en la
  nube iniciadas en «Configuración › Cuentas» (fuente: `ms-win-explorador.html`).»
- LQMC old: «Las ubicaciones de búsqueda se personalizan en «Buscar en Windows» (fuente: `ms-win-indexacion.html`).»
  New: «…; con la búsqueda de contenido en la nube, Windows Search muestra elementos de OneDrive (fuente:
  `ms-win-indexacion.html`, `ms-win-busqueda-privacidad.html`).»
- Source (`ms-win-busqueda-privacidad.html`, reused from m06-l02): «También puede personalizar las ubicaciones de
  búsqueda para incluir o excluir carpetas específicas.»; «Si activa la configuración de la cuenta de Microsoft para la
  búsqueda de contenido en la nube, Windows Search mostrará los resultados de los elementos de su OneDrive personal,
  Outlook y otros servicios Microsoft.»
- Source (`ms-win-explorador.html`): «Para buscar archivos relevantes desde el PC y la nube, busque desde Inicio del
  Explorador de archivos.»; «Inicie sesión en sus cuentas en la nube desde Inicio>Configuración>Cuentas para habilitar
  la búsqueda en la nube.» (this sentence = restoration R3).
- Note: no official page says literally that a OneDrive folder can be *added as an indexed location*; the pages say
  locations include/exclude folders and that cloud content search brings OneDrive results. The lesson states exactly
  that.

### 3. 2025 A 50 — Asistencia rápida (item «Asistencia rápida»)

- Old: «Ctrl+Windows+Q. Quien ayuda comparte un código de 6 dígitos, ve la pantalla del otro y puede pedir el control
  total si este lo permite (fuente: `ms-win-asistencia-rapida.html`).»
- New: «Ctrl+Windows+Q. Conexión remota: quien ayuda comparte un código de 6 dígitos y puede ver la pantalla del equipo
  o controlarlo, si lo permites; para el control total selecciona «Solicitar control» (fuente:
  `ms-win-asistencia-rapida.html`).»
- Source: «Asistencia rápida utiliza una conexión remota, […] ya que pueden ver la pantalla del equipo o controlar el
  equipo (si lo permites).»; «Selecciona Ayudar a alguien y comparte el código de 6 dígitos»; «Si quieres solicitar el
  control total del equipo, selecciona Solicitar control».

## Restorations (v1.5: earlier cuts an exam asked)

| # | Restored | Exam row that asked it | Source passage |
|---|---|---|---|
| R1 | «Acerca de»: nombre y modelo; «Especificaciones de Windows» (edición, versión); «Especificaciones del dispositivo» (procesador, RAM, 32 o 64 bits) | 2020 ord. 44 (index: Configuración › Sistema › Acerca de, vigente; asks where to see «las especificaciones de Windows 10 y del equipo») | `ms-win-info-dispositivo.html` (re-saved; cut in R2 and not saved then): «El nombre del dispositivo aparece en la página, con el nombre del modelo justo debajo.»; «En Especificaciones de Windows, comprueba qué edición y versión de Windows utiliza el dispositivo.»; «En Especificaciones del dispositivo, comprueba los detalles sobre el dispositivo, incluyendo: Tipo de procesador. Cantidad de RAM instalada. Si el dispositivo ejecuta una versión de Windows de 32 o 64 bits.» |
| R2 | OneDrive files deleted from the cloud do not reach the PC's Papelera | 2025 X 50 (what cannot be recovered from the Papelera) | `ms-onedrive-restaurar.html`: «Los Files eliminados de la nube, incluidos los marcados como solo en línea ( ), no aparecen en la Papelera de reciclaje ni en la Papelera del equipo.» |
| R3 | Cloud search from Inicio del Explorador, accounts in Configuración › Cuentas | 2024 X 57 (OneDrive in search) | `ms-win-explorador.html`, quoted in change 2 |

Not restored: «Enviar a» destinations (2024 X 56) — on the ledger's «Sin fuente oficial» list. The other R2 cuts of this
lesson (window parts, Ctrl+Mayús+1…9, ZIP formats, \\localhost, index details, Recortes/Paint/Calculadora/Reloj extras,
msinfo32/MSConfig/compmgmt) match no index row.

## Cuts

None.

## New sources (fuentes.yaml entries for the coordinator)

```yaml
- file: ms-win-directivas-explorador.html
  url: "https://learn.microsoft.com/es-es/windows/client-management/mdm/policy-csp-admx-windowsexplorer"
  title: "Microsoft, «CSP de directiva de ADMX_WindowsExplorer»"
  consultado: "2026-10-17"
  sha256: 9fdba5ad5ceabbfb74ba8a727da8acce4e1e5a916410daf7bbc0f6840a09b431
  lessons: [m06-l03]
- file: ms-win-info-dispositivo.html
  url: "https://support.microsoft.com/es-es/windows/experience/find-information-about-your-windows-device"
  title: "Microsoft, «Encontrar información sobre el dispositivo Windows»"
  consultado: "2026-10-17"
  sha256: a7cf85194db6e6820c7d01793ecf4528dfdda4d6341e4d1e9298217c8528f058
  lessons: [m06-l03]
```

`ms-win-directivas-explorador.html` is an MDM/Group Policy reference (admin documentation, not a UI help page); add it to
the ledger's «Files resting on non-UI sources».

reused: [ms-win-busqueda-privacidad.html]
