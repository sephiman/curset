# Verification — `m02-l11`, re-check 1 (blind)

Verifier: blind, 2026-11-06. Checked against the saved pages, not the proposer's wording. Files read:
`docs/age-verification/c2/bloque-ii/pending/m02-l11.md`, `content/age-auxiliar-c2/es/lessons/m02-l11.md`,
`docs/age-c2-exam-style.md` §9 (classic and new Outlook), and the saved pages (HTML stripped to text, tab panels read
separately where the page has them): `ms-outlook-limpieza-buzon.html`, `ms-outlook-leido.html`, `ms-outlook-atajos.html`,
`ms-outlook-asistente-programacion.html`, `ms-outlook-calendario.html`, `ms-outlook-cifrar-m365.html`,
`ms-outlook-menciones.html`. Client scoping is judged by each page's «Se aplica a» line and its tabs.

| id | verdict | precept checked | note | replacement |
|---|---|---|---|---|
| `094e17ff58` | PASS | ms-outlook-limpieza-buzon.html | «Archivo elementos mediante Autoarchivar»; «Vea el tamaño de la carpeta Conflictos y elimine esta carpeta»; label «Limpieza de buzón» literal. Classic scope: «Se aplica a Outlook 2024 Outlook 2021» and the path Archivo › Herramientas, with no new Outlook in the list | — |
| `ad5a455f1b` | PASS | ms-outlook-leido.html; ms-outlook-atajos.html | leído page: «Presione Ctrl+Q para marcar el mensaje como leído o Ctrl+U para marcarlo como no leído». Shortcuts page: «Los métodos abreviados de teclado de este tema hacen referencia a la distribución del teclado de España»; «Marcar la conversación o el mensaje seleccionados como no leídos — Ctrl+S» (new Outlook) and «Marcar un mensaje como no leído — Ctrl+S» under «Métodos abreviados de teclado de correo en la versión clásica de Outlook». The two pages disagree, and the item states both with their sources, as the spec requires | — |
| `60ce04a470` | PASS | ms-outlook-asistente-programacion.html; tabs Microsoft 365 and Windows | «Seleccione Asistente para programación en la cinta de opciones. Verá una fila para cada destinatario que especificó en el cuadro Para». Classic scope: the steps are the ribbon client, and «Se aplica a» lists Outlook para Microsoft 365, 2024, 2021, 2019, 2016 (plus Mac/mobile) and not «Nuevo Outlook para Windows» | — |
| `deefc04084` | PASS | ms-outlook-calendario.html; «Vincular a calendarios en sitios de Microsoft SharePoint» | «Si tiene acceso a un sitio de SharePoint, puede ver las listas de eventos de ese sitio en su Calendario de Outlook … puede ver los calendarios de SharePoint en paralelo con otros calendarios personales o compartidos». Classic scope: «Se aplica a Outlook para Microsoft 365 Outlook 2024 Outlook 2021 Outlook 2019 Outlook 2016» | — |
| `8a99f7b743` | PASS | ms-outlook-cifrar-m365.html | «Se aplica a Outlook.com Nuevo Outlook para Windows»; «redacte un mensaje nuevo, seleccione la cinta Opciones y, después, seleccione Cifrar»; «Como usuario Outlook.com con una suscripción Microsoft 365 Familia o Microsoft 365 Personal, verá…»; «Puede elegir Cifrar o No reenviar». The third entry on the page, «Ningún conjunto de permisos», is the default with no message encryption, so «ofrece Cifrar y No reenviar» is faithful | — |
| `12dff57a9b` | PASS | ms-outlook-menciones.html; Nota | «La característica de correo mencionado solo está disponible para destinatarios que usen Exchange Server 2016, Exchange Server 2019, Exchange Online o Outlook.com». Scope is the page's, and the item keeps it to the correo mencionado feature (it leaves out the separate @ indicator, which is limited to Exchange Online/Outlook.com) | — |
| `7243c21da8` | PASS | ms-outlook-calendario.html | as `deefc04084` | — |

PASS 7, FAIL 0.
