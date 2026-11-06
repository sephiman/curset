# Verification — `m02-l06`, re-check 3

Verifier: blind verifier (opus), 2026-11-06. Did not write the lesson.

Files read: `docs/age-verification/c2/bloque-ii/pending/m02-l06.md`, `content/age-auxiliar-c2/es/lessons/m02-l06.md`,
`content/age-auxiliar-c2/sources/otros/fuentes.yaml`, and the text (HTML stripped) of `ms-win-enlace-movil.html`,
`ms-win-configuracion-red.html`, `ms-win-vpn.html`, `ms-office-autoguardado.html`. sha256 of all four equal to
fuentes.yaml; all Microsoft es-es pages, admissible.

Result: 5 PASS, 4 FAIL.

| id | verdict | precept checked | note | replacement |
|---|---|---|---|---|
| `48c4b40960` | FAIL | ms-win-enlace-movil.html, tab «iOS» | the iOS tab says «Lee y responde a mensajes de texto con facilidad, haz y recibe llamadas, y administra las notificaciones de tu iPhone®» and does not name photos; but the page itself does: its opening paragraph, for «Android o iPhone», includes «ver fotos recientes». «la página … no menciona las fotos» is false; the section is labelled «iOS», not «iPhone». State both | Con iPhone, la pestaña «iOS» de la página describe leer y responder mensajes de texto, hacer y recibir llamadas y administrar las notificaciones, sin nombrar las fotos; el párrafo inicial, común a Android e iPhone, sí incluye ver fotos recientes (fuente: `ms-win-enlace-movil.html`; «iOS»). |
| `bf9e660f85` | PASS | ms-win-configuracion-red.html, «Navegar por la configuración de Red e Internet» | «La sección Red e Internet le permite administrar la conectividad de su dispositivo, incluyendo la configuración de Wi-Fi, Ethernet, zonas con cobertura inalámbrica móvil y modo avión. Además, esta sección incluye opciones de configuración para las conexiones de acceso telefónico» | — |
| `09c924ddf0` | PASS | ms-win-vpn.html | the page prints «En la aplicación Configuración de tu dispositivo Windows, selecciona VPN de red & Internet>>Agregar VPN»: the labels are literal. Note for the coordinator: the string is the page's garbled rendering of Red & Internet › VPN › Agregar VPN; the lesson reproduces it faithfully | — |
| `318e200ac4` | FAIL | ms-office-autoguardado.html | «Autoguardado es una nueva característica disponible en Excel, Word y PowerPoint para Microsoft 365 suscriptores que guarda el archivo automáticamente, cada pocos segundos» and «está habilitado de forma predeterminada en Microsoft 365 cuando un archivo está almacenado en OneDrive, OneDrive para la Empresa o SharePoint Online» match; «no un ajuste de Windows» is not on the page | - **Autoguardado**: es una característica de Excel, Word y PowerPoint para suscriptores de Microsoft 365; guarda el archivo automáticamente, cada pocos segundos, y está habilitado de forma predeterminada cuando el archivo está en OneDrive, OneDrive para la Empresa o SharePoint Online (fuente: `ms-office-autoguardado.html`). |
| `3cac5c7e94` | FAIL | ms-win-enlace-movil.html, tab «iOS» | same defect as `48c4b40960`, and it contradicts the preceding «Lo que más cae» line (Android o iPhone … ver fotos recientes), which is the page's opening paragraph | Con iPhone, la pestaña «iOS» de la página de Microsoft describe mensajes, llamadas y notificaciones, sin nombrar las fotos, que solo aparecen en el párrafo común a Android e iPhone (fuente: `ms-win-enlace-movil.html`; «iOS»). |
| `027f0a6e2e` | PASS | Fuentes line | «Comprender y explorar la configuración de Windows», support.microsoft.com, 06-11-2026 | — |
| `2d00fd4996` | PASS | Fuentes line | «Conectarse a una VPN en Windows», support.microsoft.com, 06-11-2026 | — |
| `edc6193676` | PASS | Fuentes line | «¿Qué es el Autoguardado?» | — |
| `4c80c7afbc` | PASS | Fuentes line | support.microsoft.com, consultado 17-10-2026 as in fuentes.yaml | — |

Whole «Fuentes» section: lists exactly the files the lesson cites (checked by diff).
