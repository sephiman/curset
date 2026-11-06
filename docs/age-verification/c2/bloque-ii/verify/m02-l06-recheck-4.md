# Verification — `m02-l06`, re-check 4 (blind)

Verifier: blind, 2026-11-06. Did not write the lesson; checked against the saved pages (HTML stripped to text; the
`android` / `ios` tab panels separated by their `data-tab` sections), not the proposer's wording. Input:
`docs/age-verification/c2/bloque-ii/pending/m02-l06.md` (3 items), lesson `content/age-auxiliar-c2/es/lessons/m02-l06.md`.
Pages read: `ms-win-enlace-movil.html`, `ms-office-autoguardado.html` (both sha256 match `fuentes.yaml`).

| id | verdict | precept checked | note | replacement |
|---|---|---|---|---|
| `79b3e35cdc` | PASS | ms-win-enlace-movil.html; intro paragraph and «iOS» tab | iOS tab: «Lee y responde a mensajes de texto con facilidad, haz y recibe llamadas, y administra las notificaciones de tu iPhone® directamente en tu PC»; the word «foto» does not occur anywhere in the iOS panel; the intro paragraph before the tabs («conectar su Android o iPhone … ver fotos recientes desde tu dispositivo móvil») includes photos | — |
| `b2dc76265c` | PASS | ms-office-autoguardado.html | «Autoguardado es una nueva característica disponible en Excel, Word y PowerPoint para Microsoft 365 suscriptores que guarda el archivo automáticamente, cada pocos segundos»; «habilitado de forma predeterminada en Microsoft 365 cuando un archivo está almacenado en OneDrive, OneDrive para la Empresa o SharePoint Online» | — |
| `b93fae8fb8` | FAIL | ms-win-enlace-movil.html; «iOS» tab | the iOS half is right, but «que solo aparecen en el párrafo común a Android e iPhone» is false for the page: the «Android» tab names photos several times («mira fotos recientes de tu dispositivo Android», «ver fotos y mucho más») | Con iPhone, la pestaña «iOS» de la página de Microsoft describe mensajes, llamadas y notificaciones, sin nombrar las fotos, que aparecen en el párrafo común a Android e iPhone y en la pestaña «Android» (fuente: `ms-win-enlace-movil.html`; «iOS»). |

PASS 2, FAIL 1.

«Fuentes» section: 23 files cited in the prose, 23 listed, the same set.
