# Style rewrites VI, pass 2: verifier-1 check (2026-10-28)

Input: `style-rewrites-vi-2.json` (15 rewrite, 9 unsupported). I used the same rule as `style-rewrites-vi.check.md`. A distractor passes when the explanation gives a page sentence that contradicts it, or when the quoted key sentence fixes a single value (a figure, a tab, a step or a closed list) that excludes it. Silence fails. So does one general sentence shared by several distractors. I matched every «…» quote accent-insensitively against all 234 saved pages in `sources/otros/`. Every quote is verbatim. The only differences are spaces that the HTML tags add before punctuation, and the `"href"` that is split by `<code>` on the WHATWG page.

Unsupported items get strict check 2: is there any saved-page sentence that makes the named distractor wrong? A FAIL here is appended to `bloque-vi/drops.tsv` (batch `style-recheck-2`, check `unique`).

## Rewrites (15)

| id | decision | verdict | reason |
|---|---|---|---|
| m06-l01-q025 | rewrite | PASS | the tape quotes are now verbatim on ms-learn-equipos-almacenamiento.html; «lo que esté en RAM desaparece» covers the switched-off case; the key's single «porque» excludes the random-position reason |
| m06-l04-q258 | rewrite | PASS | «puede desactivar Autoguardado. Cuando esté listo, haga clic en Guardar» describes editing with it off, which contradicts «pide activarlo antes de permitir la edición»; «un archivo individual» fixes the scope against the OneDrive-wide distractor |
| m06-l04-q260 | rewrite | PASS | Restaurar is another button; delete is answered by the follow-on Restaurar step; copy is answered by «se muestra el comando Guardar una copia en el menú Archivo» (another command); each has its own sentence |
| m06-l05-q367 | rewrite | FAIL | the «solo» sentence states a necessary condition (same source), not a sufficient one. «una tabla de otra hoja con el mismo origen cumple la frase» does not show it can be connected. «Solo con las de la misma hoja» adds a further restriction that «solo» does not exclude, and no saved page says anything about sheets. b and c are fine |
| m06-l06-q012 | rewrite | PASS | a: «no comprime los datos» + «mejorar el rendimiento»; c: compacting removes only «el espacio no utilizado» (the one thing it eliminates), not others' work; d: dividing is a separate measure on the same page |
| m06-l06-q014 | rewrite | FAIL | d (.accdb to .mdb): «queda fuera de lo que la página atribuye al comando» is silence. The list of «problemas siguientes» is a list of problems the command addresses, not a closed list of its effects. b and c pass |
| m06-l06-q425 | rewrite | PASS | a: the Access 2016 sentence; b and d: the key fixes one tab (Datos externos) and one group (Importar & vínculo) |
| m06-l06-q432 | rewrite | PASS | the sheet, file and range names each get their own sentence from ms-access-importar-excel.html with a different role; the key fixes the one thing that must match (column headers) |
| m06-l08-q143 | rewrite | FAIL | c (replace with an XML tree the browser does not process): «DOM trees are used as the way to represent HTML documents when they are processed…» speaks of HTML documents and does not exclude replacement or an unprocessed XML tree. A sentence that would work: «When a document is transmitted with an XML MIME type, such as application/xhtml+xml, then it is treated as an XML document by web browsers, to be parsed by an XML processor.» a and b pass |
| m06-l01-q175 | rewrite | PASS | the closed pair (magnético/digital) excludes local/nube; corto/largo plazo and cinta/disco each have a verbatim sentence |
| m06-l04-q148 | rewrite | PASS | the key fixes the tab (Programador); each wrong tab gets its own purpose from ms-word-atajos.html |
| m06-l06-q210 | rewrite | PASS | the key fixes one separator (dos puntos), which excludes = and ;; «Anteponga» excludes the name placed after the expression |
| m06-l08-q229 | rewrite | PASS | the key fixes the path, with no Más herramientas step; b and d each have a verbatim sentence from ms-edge-inprivate.html |
| m06-l04-q142 | rewrite | PASS | quote fix only: «que no contienen macros» is now verbatim (ms-office-formatos-archivo.html) |
| m06-l04-q221 | rewrite | PASS | quote fix only: the guillemet paraphrase is gone, and the remaining quote is verbatim on ms-office-recorte-pantalla.html |

## Unsupported (9): strict check 2

| id | decision | verdict | reason |
|---|---|---|---|
| m06-l01-q351 | unsupported | PASS | incibe-glosario-ciberseguridad.pdf (HTTPS): «En HTTPS el tráfico HTTP es cifrado mediante un algoritmo de cifrado simétrico cuya clave ha sido previamente intercambiada entre el navegador y el servidor. Es utilizado por cualquier tipo de servicio que requiera el envío de datos personales o contraseñas, entidades bancarias, tiendas en línea, pago seguro, etc.» This makes d («se envía sin cifrar a todos los servicios en línea») wrong. The explanation should use this sentence |
| m06-l02-q129 | unsupported | FAIL, dropped | no sentence rules out a default Explorador de archivos desktop icon; the default sentence is not a closed list, and ms-win-explorador.html gives only taskbar, Start and Win+E as ways to open it |
| m06-l02-q135 | unsupported | FAIL, dropped | no sentence gives or denies an effect of Mayús with the wheel on the desktop. The ms-excel-atajos.html line («Mayús y, a continuación, desplázate…») is for Excel (in the Mac table, next to Cmd+F) and the page does not extend it to the Windows desktop |
| m06-l02-q139 | unsupported | FAIL, dropped | no saved page says whether desktop shortcuts open at sign-in |
| m06-l04-q060 | unsupported | FAIL, dropped | ms-office-traducir.html gives Internet plus experiencias conectadas; nothing excludes an accessory pack or saving to OneDrive or SharePoint first |
| m06-l04-q104 | unsupported | FAIL, dropped | the Navigation pane is not mentioned with Lectura en voz alta on any page (ms-word-lectura-voz-alta.html or ms-word-lector-pantalla.html) |
| m06-l04-q147 | unsupported | FAIL, dropped | the steps in ms-word-macros.html run Asignar, record, stop, run, with no restart, but no sentence excludes one (same standard as q104) |
| m06-l06-q058 | unsupported | FAIL, dropped | ms-access-tipos-datos(-escritorio).html: «puede crear una expresión que use datos de uno o varios campos» and result types including Texto corto; nothing limits or frees the input field types |
| m06-l06-q421 | unsupported | FAIL, dropped | «Access rechazará todas las operaciones…» does not exclude logging them as well; the only error-log table on the saved pages belongs to Excel import |

## Totals

- Rewrites: PASS 12, FAIL 3 (m06-l05-q367, m06-l06-q014, m06-l08-q143).
- Unsupported: PASS 1 (m06-l01-q351, with the INCIBE sentence), FAIL 8, all appended to `bloque-vi/drops.tsv`.
- Overall: PASS 13, FAIL 11; unsupported dropped 8.
