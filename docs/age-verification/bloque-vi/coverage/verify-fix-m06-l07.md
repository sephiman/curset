# Coverage fix — m06-l07: blind verification (2026-10-17)

Inputs: `fix-m06-l07.md` (writer's claims), `m06-l07.md` (coverage report), `fix-spec.md` incl. «Rule change»
(no word ceiling; restorations). Lesson `content/age-administrativo-c1/es/lessons/m06-l07.md` as it now stands (not
edited). Page text with `SP/tools/pagetext.py` on the files in `C/sources/otros/`.

Client attribution yardstick: the lesson already labels «(Outlook clásico)» the items whose page's «Se aplica a» lists
Outlook para Microsoft 365 / 2024 / 2021 but not «Nuevo Outlook para Windows» (Vistas, Buzón actual, Limpieza de buzón).
The restored items are held to the same rule (spec: «state which one an item describes when they differ»).

## Changes, restorations, sources

| # | item (first words) | field(s) | PASS/FAIL | reason | replacement |
|---|---|---|---|---|---|
| 1 | IMAP y POP: «El proveedor da los nombres del servidor de correo entrante (IMAP o POP) y del saliente (SMTP)» | behaviour | PASS | Page: «debe ir a su proveedor de correo electrónico y averiguar el nombre de su servidor POP y SMTP» followed by «Servidor de correo entrante (IMAP)… (POP)… saliente (SMTP)». With the address item, 2025 A 63 (server, «@», protocol) is now covered. | — |
| 2 | **Dirección de correo**: una cadena que se interpreta localmente, el signo «@»… | definition | PASS | RFC 5322 §3.4.1: «a locally interpreted string followed by the at-sign character ("@" …) followed by an Internet domain». IETF is on the spec's list for correo items; English fallback documented (no Spanish official page found); no UI label involved. | — |
| 3 | Grupos de Microsoft 365: «Todos los miembros reciben el correo enviado al grupo.» | behaviour, client | FAIL | Printed only in the «Outlook clásico» tab of `ms-outlook-grupo-enviar.html` («Enviar un correo electrónico a un grupo en Outlook clásico … Todos los miembros del grupo recibirán el correo electrónico»); the general part says only that members who follow the group also get conversations in their personal inbox. The lesson states it for every client. | «Cualquier persona de la organización puede iniciar una conversación de grupo. En Outlook clásico, todos los miembros reciben el correo enviado al grupo.» (both printed; the first is the general list and is the closer fact for 2025 A 66) |
| 4 | Grupos de Microsoft 365: «En un grupo público, cualquier persona de la organización lee y responde…; en uno privado, solo los miembros» | behaviour | PASS | General list, all clients: «Para un grupo público, cualquier persona de su organización puede leer y responder a las conversaciones del grupo. / Para un grupo privado, solo los miembros del grupo pueden participar». 2025 A 66 now covered (address, public/private; members' receipt once #3 is fixed). | — |
| 5 | Outlook: «si nunca abriste Outlook, sale la pantalla principal, donde escribes tu dirección de correo y seleccionas Conectar» | behaviour | PASS | Page (applies to Outlook para Microsoft 365 and Nuevo Outlook para Windows, no tabs): «Si nunca abrió Outlook, se mostrará la pantalla principal. / Escriba su dirección de correo electrónico y seleccione Conectar.» 2022 62: judged covered — the first-run screen asks for the account; «el primer paso» as literal wording stays sin fuente oficial, as the writer notes. | — |
| 6 | Restored **Gráficos**: «Insertar › Ilustraciones › Gráfico»; hoja de cálculo de Excel | path, behaviour, client | FAIL | Path and Excel sheet literal («en el menú Insertar, en el grupo Ilustraciones … Gráfico … En la hoja de cálculo de Excel que aparece, escriba los datos»). But «Se aplica a: Outlook para Microsoft 365, Outlook 2024, Outlook 2021» (no new Outlook) and the item names no client. 2020 X 64 restoration otherwise correct. | «- **Gráficos** (Outlook clásico): en el cuerpo del mensaje, «Insertar › Ilustraciones › Gráfico»; …» (rest unchanged) |
| 7 | Restored **Limpiar**: «con la cinta clásica, «Inicio › Eliminar › Limpiar»…» | path, behaviour, default, client | FAIL | Path, three options, redundant messages and default Elementos eliminados literal. «Se aplica a» has no new Outlook and the item names no client; «cinta clásica» is the ribbon layout, not the client, and invites that misreading. 2020 X 66 restoration otherwise correct. | «- **Limpiar** (Outlook clásico): con la cinta clásica, «Inicio › Eliminar › Limpiar»; …» (rest unchanged) |
| 8 | Restored **Correo no deseado**: «Inicio › Eliminar › Bloquear › Opciones de correo electrónico no deseado» | path, default, levels, client | FAIL | Path, default «Sin filtrado automático», Bajo, Alto, «Solo listas seguras … la opción más restrictiva» literal; label as printed («Bloquear», not the exam's «Correo no deseado»). «Se aplica a» has no new Outlook and the page itself frames it as classic («Explícame el FILTRO de correo no deseado en Outlook clásico»); the item names no client. | «- **Correo no deseado** (Outlook clásico): «Inicio › Eliminar › Bloquear › Opciones de correo electrónico no deseado». …» (rest unchanged) |
| 9 | Restored **Carpetas de búsqueda** | definition, path, client | PASS | «carpetas virtuales que muestran los mensajes que coinciden con criterios específicos, sin mover ni duplicar»; classic tab: «pestaña Carpeta. En el grupo Nuevo, haga clic en Nueva carpeta de búsqueda»; «Las carpetas de búsqueda personalizadas avanzadas solo se admiten en Outlook clásico». Client attributed. 2020 X 63. | — |
| 10 | Restored: «Un grupo de envío y recepción contiene una colección de cuentas y carpetas; se programa cada n minutos o al salir» | behaviour, client | PASS (note) | Literal: «contiene una colección de cuentas y carpetas de Outlook», «Programar un envío o recepción automáticos cada n minutos», «Realizar un envío/recepción automático al salir». Item sits under «Enviar y recibir (Outlook clásico)». Note: the page is OCT 2016 admin help («Se aplica a: Office Profesional Plus 2016, Office Standard 2016»; settings for Exchange accounts and folders), not Microsoft 365 UI help — list it under «Files resting on non-UI sources». 2020 X P1R 1. | — |
| 11 | Búsqueda: «F4 busca un texto en un elemento abierto» | shortcut, client | PASS (note) | `ms-outlook-atajos.html`, section «Usar la búsqueda en la versión clásica de Outlook»: «Buscar un texto en un elemento abierto. / F4». Item says «en Outlook clásico». 2020 X 68. Note: lines 41–43 wrap badly («(fuente:» then a short line); rewrap the item. | — |
| 12 | Source `ms-outlook-grupo-enviar.html` | sha256, URL, lang, title, re-download | PASS | sha256 a76ab1f5… matches; canonical …/es-es/outlook/people/send-an-email-to-a-group-in-outlook; `lang="es-ES"`; title matches. Re-downloaded 2026-10-17 (200, same URL): extracted text identical. | — |
| 13 | Source `rfc5322-formato-mensaje.txt` | sha256, URL, re-download | PASS | sha256 cb459acc… matches; re-downloaded from https://www.rfc-editor.org/rfc/rfc5322.txt: byte-identical (same sha256). Documented English fallback. | — |
| 14 | Source `ms-outlook-carpetas-busqueda.html` | sha256, URL, lang, title | PASS | 6769bb58… matches; canonical …/es-es/outlook/mail/use-search-folders-…; `es-ES`; title matches. | — |
| 15 | Source `ms-outlook-limpiar-conversacion.html` | sha256, URL, lang, title | PASS | 49d9f333… matches; canonical …/es-es/outlook/use-conversation-clean-up-…; `es-ES`; title matches. | — |
| 16 | Source `ms-outlook-correo-no-deseado.html` | sha256, URL, lang, title | PASS | a33f6d23… matches; canonical …/es-es/outlook/change-the-level-of-protection-…; `es-ES`; title matches («Filtro de Email no deseado», as printed). | — |
| 17 | Source `ms-outlook-grupos-envio-recepcion.html` | sha256, URL, lang, title | PASS | b36f9aa2… matches; canonical/og:url learn.microsoft.com/es-es/office/customization-tool/oct-2016-help-specify-send-receive-groups; Spanish; title matches. Scope note in #10. | — |
| 18 | Source `ms-outlook-graficos.html` | sha256, URL, lang, title | PASS | dbec89d3… matches; canonical …/es-es/outlook/add-graphics-to-messages-in-outlook; `es-ES`; title matches. | — |
| 19 | Fuentes block | titles, order | PASS | Seven new lines with titles as printed (rfc-editor.org and learn.microsoft.com domains given). `fuentes_order.py` (read-only): none missing, none uncited, in order. | — |
| 20 | «Not restored» (Dirigir respuestas a, Incluir › Firma, within-item cuts) | restoration scope | PASS | 2020 X 65 and 2020 X 62 were never cut for space (no page / label not confirmed), so outside the restore rule. Index Outlook rows (31) checked: none asks the R2 within-item cuts (vistas path, S/MIME option labels, 24-hour recall retry, delay up to 120 min, Ctrl+Mayús+L, Alt+S, Todos los elementos de Outlook…) beyond what the lesson states. All six cut 2020 X rows of the ledger list are restored. | — |

## Coverage re-check (lesson as it now stands)

Every row of `m06-l07.md` marked covered (20) still has its quoted text in the lesson (string check after unwrapping):
Colaborador, cc:, rules after activation, Programar envío/IMAP-POP, S/MIME, Buzón actual, Regla, acceso delegado and
Editor, Limpieza de buzón, categorías, five-digit numbers, Recuperar, Responder shortcuts, Qué es Outlook, exclamación
roja, Vistas, frase exacta, IMAP/POP, Archivar. No cut was made.

After the fix: 2025 A 63, 2025 A 66 (stays covered with the #3 replacement) and 2022 62 → covered. Unchanged (not in
`fixes.md`; discussed keys): 2024 X 65 partial, 2025 X 66 miss. Asked 25; covered 23; partial 1; miss 1; share missed
(partial as half) 1.5 / 25 = 6%.

## Form

- Words: 1,859 (`wc -w`), allowed under the rule change. Lines ≤120 except line 1 (the `#` title, unchanged).
- List-shape hygiene: clean. Spanish quotes. Voice: terse items, no fillers or closers; no invented vocabulary.
- Cosmetic: Búsqueda item, lines 41–43, uneven wrap (see #11).

## Counts

Checked 20: PASS 16 (2 with notes), FAIL 4 (#3, #6, #7, #8 — all client attribution). Coverage re-check: 20/20 covered
rows intact; 3 partial → covered.
