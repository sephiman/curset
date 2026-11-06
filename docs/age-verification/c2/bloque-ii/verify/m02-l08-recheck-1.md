# Verification — `m02-l08`, re-check 1 (blind)

Verifier: blind, 2026-11-06. Did not write the lesson; checked against the pages, not the proposer's wording. Files read:
`docs/age-verification/c2/bloque-ii/pending/m02-l08.md`, `content/age-auxiliar-c2/es/lessons/m02-l08.md`, and in
`content/age-auxiliar-c2/sources/otros/` (HTML stripped to text, Windows sections): `ms-office-ortografia.html`,
`ms-word-control-cambios.html`, `ms-word-combinar-reglas.html`, `ms-word-subrayar.html`, `ms-word-lector-pantalla.html`.

The pending splitter cut two sentences at the ellipsis in «Si...»: `570cfa7719` and `1be7acd40c` are fragments; the
whole sentence (lesson lines 46 and 126) was checked.

| id | verdict | precept checked | note | replacement |
|---|---|---|---|---|
| `36debd3ec1` | PASS | ms-office-ortografia.html | «¿Usa Microsoft 365? Es posible que le interese echar un vistazo a la nueva y potente característica Editor en Word. Para obtener más información, consulte Editor: su asistente para la redacción.» | — |
| `05652b1dea` | PASS | ms-word-control-cambios.html; «Activar y desactivar el control de cambios» | the activation step is garbled («seleccione **Seguimiento de**>**cambios**»); the same page gives the clean path «Revisar … Seguimiento>Control de cambios>Bloquear seguimiento», so «Revisar › Seguimiento › Control de cambios» is literal; heading «Activar y desactivar el control de cambios» | — |
| `570cfa7719` | PASS | ms-word-combinar-reglas.html; «Si... Entonces... En caso contrario» | path «Reglas>de correspondencia>si... Entonces... De lo contrario»; «mostrar texto diferente según la información del origen de datos … un mensaje … cuando el campo País o región está en blanco y otro cuando no lo está»; heading «Si... Entonces... En caso contrario»; label «Siguiente registro si» («Reglas>de correspondencia>Siguiente registro si»), «controlar cuándo Word pasa al registro siguiente en función de una condición» | — |
| `26afa28f2b` | PASS | ms-word-subrayar.html | «Ir a Inicio>Subrayado»; «Vaya a Inicio y seleccione Fuente» + dialog launcher; «Estilo de subrayado» with «Solo palabras» and «el subrayado doble»; «Color de subrayado». The page's Ctrl+U and Ctrl+D are US-keyboard shortcuts and are rightly left out | — |
| `1be7acd40c` | PASS | ms-word-combinar-reglas.html | whole line: «Correspondencia › Reglas» incluye «Si... Entonces... De lo contrario», que muestra un texto según el origen de datos. Path: the page's «Reglas>de correspondencia>» is the garbled form of Correspondencia › Reglas («En la pestaña Correspondencia, vaya a … reglas»); rule label and behaviour as in `570cfa7719` | — |
| `9094129192` | PASS | ms-word-lector-pantalla.html; Windows, «Usar el panel de navegación» | «Puede usar el panel de navegación para desplazarse rápidamente entre partes del documento, como títulos o gráficos.» | — |

PASS 6, FAIL 0.

Note for the coordinator (not a verdict): lesson lines 27, 46, 71 and 128 are not wrapped to the file's width.
