# Coverage fix — m06-l07 (writer, 2026-10-17)

Lesson: `content/age-administrativo-c1/es/lessons/m06-l07.md`. Applies the rule change (requirements v1.5, no word
ceiling): nothing cut. Words (`wc -w`): 1489 before, **1859** after. Lines ≤ 120 (only the `#` title line is longer,
unchanged). Fuentes reordered with `fuentes_order.py` (in order, none missing or uncited).

## Changes

### 1. 2025 A 63 — mail server, address with «@», protocol (SMTP)

a) Old (IMAP y POP): «… POP los descarga y los elimina del servicio. El correo saliente va por SMTP (fuente:
`ms-outlook-imap-pop.html`).»
New: «… El correo saliente va por SMTP. El proveedor da los nombres del servidor de correo entrante (IMAP o POP) y del
saliente (SMTP) (fuente: `ms-outlook-imap-pop.html`).»
Source: «debe ir a su proveedor de correo electrónico y averiguar el nombre de su servidor POP y SMTP para que pueda
escribir la información en la aplicación de correo electrónico. […] Servidor de correo entrante (IMAP): imap.<nombre del
servicio>. com / Servidor entrante (POP): pop.<nombre del servicio>. com / Servidor de correo saliente (SMTP):
smtp.<nombre del servicio>. com»

b) New item after Outlook:
`- **Dirección de correo**: una cadena que se interpreta localmente, el signo «@» y un dominio de Internet (fuente:`
`  `rfc5322-formato-mensaje.txt`).`
Source `rfc5322-formato-mensaje.txt` (new), §3.4.1: «An addr-spec is a specific Internet identifier that contains a
locally interpreted string followed by the at-sign character ("@", ASCII value 64) followed by an Internet domain.»
(IETF standards page, English; no Spanish official page found stating the address form.)

### 2. 2025 A 66 — group address reaches every member; public / private

Old (Grupos de Microsoft 365) ended: «La bandeja puede aceptar mensajes de fuera del grupo y de la organización (fuente:
`ms-outlook-grupos.html`).»
Appended: «Todos los miembros reciben el correo enviado al grupo. En un grupo público, cualquier persona de la
organización lee y responde sus conversaciones; en uno privado, solo los miembros (fuente: `ms-outlook-grupo-enviar.html`).»
Source `ms-outlook-grupo-enviar.html` (new): «Escriba el mensaje y seleccione Enviar. Todos los miembros del grupo
recibirán el correo electrónico.» / «Para un grupo público, cualquier persona de su organización puede leer y responder a
las conversaciones del grupo. Para un grupo privado, solo los miembros del grupo pueden participar en la conversación.»
The group address is already stated (`ms-outlook-grupos.html`). The page does not say that anyone can *send* to a public
group; the lesson states only what it prints.

### 3. 2022 62 — the first step in Outlook is adding an account

Old: «Una cuenta se agrega en «Archivo › Agregar cuenta» (fuente: `ms-outlook-agregar-cuenta.html`).»
New: «Una cuenta se agrega en «Archivo › Agregar cuenta»; si nunca abriste Outlook, sale la pantalla principal, donde
escribes tu dirección de correo y seleccionas Conectar (fuente: `ms-outlook-agregar-cuenta.html`).»
Source («Inicio rápido: Agregar una cuenta de correo electrónico a Outlook»): «Abra Outlook y seleccione Agregar cuenta a
archivo>. / Si nunca abrió Outlook, se mostrará la pantalla principal. / Escriba su dirección de correo electrónico y
seleccione Conectar.» No saved or found page says literally «el primer paso» / «lo primero»; also checked «Introducción
al nuevo Outlook para Windows» (support.microsoft.com/es-es/outlook/getting-started-with-the-new-outlook-for-windows),
not saved. The verifier may judge the row still partial; the «first step» wording itself is **sin fuente oficial**.

## Restored (earlier cut for length, asked by an exam; all 2020 extr., programa anterior)

| Restored item | Exam row | Text (source) | Passage |
|---|---|---|---|
| Gráficos | 2020 X 64 (Insertar › Ilustraciones › Gráfico) | «en el cuerpo del mensaje, «Insertar › Ilustraciones › Gráfico»; los datos se escriben en la hoja de cálculo de Excel que aparece» (`ms-outlook-graficos.html`) | «en el menú Insertar, en el grupo Ilustraciones, elija una de las opciones. […] Gráfico Elija un tipo de gráfico […] En la hoja de cálculo de Excel que aparece, escriba los datos del gráfico.» |
| Limpiar | 2020 X 66 (Limpiar carpeta quita mensajes redundantes) | «con la cinta clásica, «Inicio › Eliminar › Limpiar»; Limpiar conversación, Limpiar carpeta y Limpiar carpeta y subcarpetas eliminan los mensajes redundantes, que van por defecto a Elementos eliminados» (`ms-outlook-limpiar-conversacion.html`) | «(Cinta clásica) En la pestaña Inicio, en el grupo Eliminar, seleccione Limpiar.» / «Limpiar carpeta Se revisan todas las conversaciones en la carpeta seleccionada y se eliminan los mensajes redundantes.» / «De manera predeterminada, los mensajes se colocan en la carpeta Elementos eliminados.» |
| Correo no deseado | 2020 X 61 (Inicio › Correo no deseado › Opciones) | «Inicio › Eliminar › Bloquear › Opciones de correo electrónico no deseado». Predeterminado Sin filtrado automático; Bajo, Alto, Solo listas seguras, el más restrictivo (`ms-outlook-correo-no-deseado.html`) | «Seleccione Inicio y, a continuación, en el grupo Eliminar, seleccione Bloquear y, después, Opciones de correo electrónico no deseado.» / «De forma predeterminada, el nivel de protección […] está establecido en Sin filtrado automático.» / «Solo listas seguras Esta es la opción más restrictiva.» The exam's label «Correo no deseado» is not the printed one («Bloquear»). |
| Carpetas de búsqueda | 2020 X 63 (Ctrl+Mayús+P: Nueva carpeta de búsqueda; shortcut kept in Búsqueda) | «carpetas virtuales con los mensajes que cumplen unos criterios, sin moverlos ni duplicarlos. En Outlook clásico, «Carpeta › Nuevo › Nueva carpeta de búsqueda»; las personalizadas avanzadas solo existen en el clásico» (`ms-outlook-carpetas-busqueda.html`) | «Las carpetas de búsqueda son carpetas virtuales que muestran los mensajes que coinciden con criterios específicos, sin mover ni duplicar los elementos originales.» / «Las carpetas de búsqueda personalizadas avanzadas solo se admiten en Outlook clásico.» / (Outlook clásico) «seleccione la pestaña Carpeta. En el grupo Nuevo, haga clic en Nueva carpeta de búsqueda.» |
| Grupos de envío y recepción | 2020 X P1R 1 | «Un grupo de envío y recepción contiene una colección de cuentas y carpetas; se programa cada n minutos o al salir de Outlook» (`ms-outlook-grupos-envio-recepcion.html`, Office Customization Tool 2016 help on learn.microsoft.com) | «Un grupo de envío y recepción contiene una colección de cuentas y carpetas de Outlook.» / «Programar un envío o recepción automáticos cada n minutos» / «Realizar un envío/recepción automático al salir» |
| F4 | 2020 X 68 (Buscar texto en el mensaje) | Búsqueda item: «F4 busca un texto en un elemento abierto» (`ms-outlook-atajos.html`, classic section «Usar la búsqueda en la versión clásica de Outlook») | «Buscar un texto en un elemento abierto. / F4» |

Not restored: «Opciones › Dirigir respuestas a» (2020 X 65; no Spanish Microsoft page found in R2); «Mensaje › Incluir ›
Firma» (2020 X 62; «Incluir» not confirmed, the Firmas item keeps the printed path). The within-item cuts of R2
(vistas path, S/MIME option labels, recall retry, etc.) and the queue's earlier m06-l07 edits: no index row asks them
beyond what the lesson states.

## Cuts

None. (A first draft of this fix cut nine clauses for the 1,500 ceiling; all undone under the rule change.)

Re-checked: every covered row of `m06-l07.md` (coverage report) still has its quoted text in the lesson.

## New sources (for `fuentes.yaml`; not edited)

```yaml
- file: ms-outlook-grupo-enviar.html
  url: "https://support.microsoft.com/es-es/outlook/people/send-an-email-to-a-group-in-outlook"
  title: "Microsoft, «Enviar un correo electrónico a un grupo en Outlook»"
  consultado: "2026-10-17"
  sha256: a76ab1f5f2707845354b6ce143c2ed339c90b2ad220b326355c4f5602e71743c
  lessons: [m06-l07]
- file: rfc5322-formato-mensaje.txt
  url: "https://www.rfc-editor.org/rfc/rfc5322.txt"
  title: "IETF, RFC 5322, «Internet Message Format»"
  consultado: "2026-10-17"
  sha256: cb459acca15a2aa895863eaeff6f1d5b9c4ca15578ae3e3706f757787a385969
  lessons: [m06-l07]
- file: ms-outlook-carpetas-busqueda.html
  url: "https://support.microsoft.com/es-es/outlook/mail/use-search-folders-to-find-messages-or-other-outlook-items"
  title: "Microsoft, «Usar carpetas de búsqueda para buscar mensajes u otros elementos de Outlook»"
  consultado: "2026-10-17"
  sha256: 6769bb58639055ec7495c1a51ec7df9a136ea29b1fd63a5cbd927021e07ad1be
  lessons: [m06-l07]
- file: ms-outlook-limpiar-conversacion.html
  url: "https://support.microsoft.com/es-es/outlook/use-conversation-clean-up-to-delete-redundant-messages-in-outlook"
  title: "Microsoft, «Usar Limpieza de conversación para eliminar mensajes redundantes en Outlook»"
  consultado: "2026-10-17"
  sha256: 49d9f33363034b055d995f8f8f9adf1263084e1cf0547deb0caf25b5b1296ac1
  lessons: [m06-l07]
- file: ms-outlook-correo-no-deseado.html
  url: "https://support.microsoft.com/es-es/outlook/change-the-level-of-protection-in-the-junk-email-filter-in-outlook"
  title: "Microsoft, «Cambiar el nivel de protección en el Filtro de Email no deseado en Outlook»"
  consultado: "2026-10-17"
  sha256: a33f6d2349fa1aeacdcff5dc6013e50360d0a4b9eaeaccce135e4460e286550e
  lessons: [m06-l07]
- file: ms-outlook-grupos-envio-recepcion.html
  url: "https://learn.microsoft.com/es-es/office/customization-tool/oct-2016-help-specify-send-receive-groups"
  title: "Microsoft, «Herramienta de personalización de Office (OCT) 2016 Ayuda para especificar envío y recepción Grupos»"
  consultado: "2026-10-17"
  sha256: b36f9aa27ef8d55ae5211add73344641518a4f278268c6b11fcf0674152c8570
  lessons: [m06-l07]
- file: ms-outlook-graficos.html
  url: "https://support.microsoft.com/es-es/outlook/add-graphics-to-messages-in-outlook"
  title: "Microsoft, «Agregar gráficos a mensajes en Outlook»"
  consultado: "2026-10-17"
  sha256: dbec89d366cddd2b472a2cb2a913aeb3ded97ad96b462409a20bb1d003964a2d
  lessons: [m06-l07]
```

`ms-outlook-grupos-envio-recepcion.html` is an admin-tool page (Office Customization Tool 2016), not a UI help page; the
coordinator may list it under «Files resting on non-UI sources».

Sin fuente oficial: «adding an account is the *first* step in Outlook» (2022 62), as literal wording.
