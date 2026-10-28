# Questions without an excerpt (platform delta F, closed 2026-10-30)

Bank change before commit (2026-10-30): **m06-l02-q350 dropped** (key «gráficos, tablas dinámicas y fórmulas» merged two
items of `ms-excel-copilot.html`, which says «formas»), replaced by **m06-l02-q359** (Copilot in Excel, «Búsqueda web»);
**m06-l03-q219 dropped** (distractor b, «La versión de Windows del equipo», arguably true: the page's Especificaciones del
dispositivo list holds «una versión de Windows de 32 o 64 bits»), replaced by **m06-l03-q276** (what Acerca de shows
right under the device name). Both replacements written by a sonnet writer and passed by a blind opus verifier on all
five checks (q276 after one explanation fix); reports `bank/bloque-vi/m06-l02.r1.verify-1.md`, `m06-l03.r1.verify-1.md`;
drops in `bank/bloque-vi/drops.tsv`. The rebuild moved m06-l02-q351 from exercise 10 to 9 (its text is unchanged).

88 questions show the solution panel without the norm's or page's text: explanation, «Tema N» and source links,
report button and «Sin extracto: …» with the reason. **extraction**: the build found no paragraph (21, unchanged since
2026-10-29). **verifier**: a blind check found that no single paragraph of the saved copy holds the fact the key rests
on, or the re-cited paragraph still fell short (67; `content/age-administrativo-c1/excerpt-exclusions.yaml`). No
question text or key was changed. **Open for a later round:** give each a citable sentence (a saved page that states the
fact in one paragraph, or a narrower annex unit for the code lists), then rebuild `excerpts.json`.

| question | exercise | citation | why |
|---|---|---|---|
| `m01-l01-q010` | `m01-l01-ex-1` | fuente: `boe-analisis-ce.xml` | extraction: no paragraph of the page holds what the explanation says |
| `m01-l06-q003` | `m01-l06-ex-1` | fuente: `oecd-recomendacion-gobierno-abierto-2017.pdf` | extraction: no paragraph of the page holds what the explanation says |
| `m01-l06-q008` | `m01-l06-ex-1` | fuente: `oecd-recomendacion-gobierno-abierto-2017.pdf` | extraction: no paragraph of the page holds what the explanation says |
| `m01-l06-q009` | `m01-l06-ex-1` | fuente: `oecd-recomendacion-gobierno-abierto-2017.pdf` | extraction: no paragraph of the page holds what the explanation says |
| `m01-l06-q025` | `m01-l06-ex-2` | fuente: `transparencia-planes-anteriores.html` | extraction: no paragraph of the page holds what the explanation says |
| `m01-l06-q026` | `m01-l06-ex-2` | fuente: `transparencia-planes-anteriores.html` | extraction: no paragraph of the page holds what the explanation says |
| `m01-l06-q027` | `m01-l06-ex-2` | fuente: `transparencia-planes-anteriores.html` | extraction: no paragraph of the page holds what the explanation says |
| `m01-l06-q032` | `m01-l06-ex-2` | fuente: `transparencia-iv-plan.pdf` | verifier: the blind check found the excerpt short of the fact (bloque I–II saved page) |
| `m01-l06-q041` | `m01-l06-ex-2` | fuente: `transparencia-v-plan.pdf` | verifier: the blind check found the excerpt short of the fact (bloque I–II saved page) |
| `m01-l06-q043` | `m01-l06-ex-3` | fuente: `un-res-70-1-agenda-2030.pdf` | extraction: no paragraph of the page holds what the explanation says |
| `m01-l06-q049` | `m01-l06-ex-3` | fuente: `un-res-70-1-agenda-2030.pdf`; «Los Objetivos y las metas estimularán durante los próximos 15 años la acción en las siguientes esferas de importancia crítica pa ra la humanidad y el planeta.» | verifier: re-cited; the list the cited sentence opens is a run of sub-headings, which no paragraph holds |
| `m01-l06-q054` | `m01-l06-ex-3` | fuente: `un-ods-objetivos.html` | extraction: no paragraph of the page holds what the explanation says |
| `m01-l06-q055` | `m01-l06-ex-3` | fuente: `un-res-70-1-agenda-2030.pdf` | extraction: no paragraph of the page holds what the explanation says |
| `m01-l06-q057` | `m01-l06-ex-3` | fuente: `un-ods-objetivos.html` | extraction: no paragraph of the page holds what the explanation says |
| `m02-l02-q064` | `m02-l02-ex-4` | fuente: `cultura-dta-diccionario.html` | verifier: the blind check found the excerpt short of the fact (bloque I–II saved page) |
| `m02-l02-q066` | `m02-l02-ex-4` | fuente: `cultura-dta-diccionario.html` | verifier: the blind check found the excerpt short of the fact (bloque I–II saved page) |
| `m05-l02-q020` | `m05-l02-ex-1` | anexo II Orden HAC/557/2026 | verifier: annex code list: the fact is a neighbouring code line |
| `m05-l02-q039` | `m05-l02-ex-1` | arts. 43.2 y 44.2 LGP | verifier: the key needs arts. 43.2 and 44.2 together |
| `m05-l02-q064` | `m05-l02-ex-3` | art. 44.1 LGP | verifier: re-cited, but the blind re-check found the cited paragraph short of the fact |
| `m05-l02-q066` | `m05-l02-ex-3` | anexo II Orden HAC/557/2026 | verifier: annex code list: the fact is a neighbouring code line |
| `m05-l02-q067` | `m05-l02-ex-3` | anexo II Orden HAC/557/2026 | verifier: annex code list: the fact spans two capítulos |
| `m05-l02-q070` | `m05-l02-ex-3` | anexo IV, art. 22, Resolución de 20-01-2014 | verifier: annex: the subconcepto sentence is beyond the excerpt |
| `m05-l02-q278` | `m05-l02-ex-9` | art. 44.1 LGP | verifier: re-cited, but the blind re-check found the cited paragraph short of the fact |
| `m05-l02-q282` | `m05-l02-ex-9` | anexo II Orden HAC/557/2026 | verifier: annex code list: the subconcepto is below the cited line |
| `m05-l02-q309` | `m05-l02-ex-11` | anexo II Orden HAC/557/2026 | verifier: annex code list: the fact spans two capítulos |
| `m05-l02-q310` | `m05-l02-ex-11` | anexo II Orden HAC/557/2026 | verifier: annex code list: the cited capítulos are far into the annex |
| `m05-l03-q041` | `m05-l03-ex-2` | anexo I Orden de documentos contables | verifier: annex note beyond the excerpt |
| `m05-l04-q058` | `m05-l04-ex-2` | anexo IV, art. 23, concepto 233, Resolución de 20-01-2014 | verifier: annex concepto text beyond the heading |
| `m05-l04-q059` | `m05-l04-ex-2` | anexo II Orden HAC/557/2026 | verifier: annex code list: the subconcepto is far from the cited line |
| `m05-l05-q007` | `m05-l05-ex-1` | anexo IV, introducción, Resolución de 20-01-2014 | verifier: annex introduction paragraph beyond the excerpt |
| `m05-l06-q049` | `m05-l06-ex-2` | anexo I, nota 34.II.a.1, Orden de documentos contables | verifier: annex note sub-item beyond the excerpt |
| `m05-l06-q050` | `m05-l06-ex-2` | anexo I, nota 34.II.a.1, Orden de documentos contables | verifier: annex note sub-item beyond the excerpt |
| `m06-l01-q012` | `m06-l01-ex-1` | fuente: `ms-win32-processor-cache.html`; «Una caché de nivel 2 es un área de memoria externa que tiene un tiempo de acceso más rápido que la memoria RAM principal.» | verifier: re-cited, but the blind re-check found the cited paragraph short of the fact |
| `m06-l01-q031` | `m06-l01-ex-1` | fuente: `nist-prefijos-binarios.html`; «Examples and comparisons with SI prefixes» | extraction: no paragraph of the page holds what the explanation says |
| `m06-l01-q032` | `m06-l01-ex-1` | fuente: `nist-prefijos-binarios.html`; «Examples and comparisons with SI prefixes» | extraction: no paragraph of the page holds what the explanation says |
| `m06-l01-q033` | `m06-l01-ex-1` | fuente: `nist-prefijos-binarios.html`; «Prefixes for binary multiples» | extraction: no paragraph of the page holds what the explanation says |
| `m06-l01-q034` | `m06-l01-ex-2` | fuente: `nist-prefijos-binarios.html`; «Prefixes for binary multiples» | extraction: no paragraph of the page holds what the explanation says |
| `m06-l01-q035` | `m06-l01-ex-2` | fuente: `nist-prefijos-binarios.html`; «Prefixes for binary multiples» | extraction: no paragraph of the page holds what the explanation says |
| `m06-l01-q036` | `m06-l01-ex-2` | fuente: `nist-prefijos-binarios.html`; «Prefixes for binary multiples» | extraction: no paragraph of the page holds what the explanation says |
| `m06-l01-q037` | `m06-l01-ex-2` | fuente: `nist-prefijos-binarios.html`; «Examples and comparisons with SI prefixes» | extraction: no paragraph of the page holds what the explanation says |
| `m06-l01-q038` | `m06-l01-ex-2` | fuente: `nist-prefijos-binarios.html`; «Examples and comparisons with SI prefixes» | extraction: no paragraph of the page holds what the explanation says |
| `m06-l01-q040` | `m06-l01-ex-2` | fuente: `nist-prefijos-binarios.html`; «Prefixes for binary multiples» | extraction: no paragraph of the page holds what the explanation says |
| `m06-l01-q148` | `m06-l01-ex-5` | fuente: `ms-learn-equipos-almacenamiento.html`; «Tanto las unidades de disco duro como las unidades de estado sólido pueden contener mucha información.» | verifier: re-cited, but the blind re-check found the cited paragraph short of the fact |
| `m06-l01-q174` | `m06-l01-ex-6` | fuente: `azure-vdi.html`; «Seis componentes clave de VDI» | verifier: writer: only the heading states the number six |
| `m06-l01-q207` | `m06-l01-ex-7` | fuente: `ms-win-sistemas-archivos.html`; «Comparación de la funcionalidad del sistema de archivos» | verifier: writer: the key needs two separate table rows |
| `m06-l01-q211` | `m06-l01-ex-7` | fuente: `ms-win-sistemas-archivos.html`; «Enlaces simbólicos — Sí — No — No — No» | verifier: re-cited, but the blind re-check found the cited paragraph short of the fact |
| `m06-l01-q320` | `m06-l01-ex-10` | fuente: `incibe-glosario-ciberseguridad.pdf`; «Phishing» | verifier: writer: the synonym line is under six words and has no end punctuation |
| `m06-l01-q344` | `m06-l01-ex-10` | fuente: `ms-cuenta-mfa.html`; «Algo que tiene: como un smartphone o una memoria USB segura.» | verifier: re-cited, but the blind re-check found the cited paragraph short of the fact |
| `m06-l02-q004` | `m06-l02-ex-1` | fuente: `ms-win-atajos.html`; «Métodos abreviados de teclado con las teclas de Windows» | verifier: the sentence holding the fact is not one paragraph of the saved copy (split by markup or a PDF line break) |
| `m06-l02-q005` | `m06-l02-ex-1` | fuente: `ms-win-opciones-inicio-sesion.html`; «Formas de iniciar sesión en Windows 11» | verifier: the sentence holding the fact is not one paragraph of the saved copy (split by markup or a PDF line break) |
| `m06-l02-q206` | `m06-l02-ex-5` | fuente: `ms-win-barra-tareas.html`; «Widgets» | verifier: writer: the key is a short list item, apart from its intro |
| `m06-l02-q211` | `m06-l02-ex-6` | fuente: `ms-win-barra-tareas.html`; «La configuración rápida proporciona una manera cómoda de acceder a la configuración usada con frecuencia y modificarla sin tener que navegar por los menús. Por ejemplo, puedes ajustar rápidamente el volumen, cambiar el brillo de la pantalla, cambiar Wi-Fi redes o activar las herramientas de accesibilidad.» | verifier: re-cited, but the blind re-check found the cited paragraph short of the fact |
| `m06-l02-q217` | `m06-l02-ex-6` | fuente: `ms-win-notificaciones.html`; «Cómo funcionan las notificaciones» | verifier: writer: the key is a short list item, apart from its intro |
| `m06-l02-q241` | `m06-l02-ex-7` | fuente: `ms-win-escritorios.html`; «En todos los escritorios: esta configuración mostrará todas las ventanas abiertas de todos los escritorios de la barra de tareas, independientemente del escritorio que esté usando actualmente. Esto puede ser útil si desea obtener acceso rápido a todas las aplicaciones abiertas sin cambiar de escritorio.» | verifier: re-cited, but the blind re-check found the cited paragraph short of the fact |
| `m06-l02-q302` | `m06-l02-ex-8` | fuente: `ms-win-atajos.html`; «Escritorio y otros métodos abreviados generales» | extraction: no paragraph of the page holds what the explanation says |
| `m06-l02-q304` | `m06-l02-ex-8` | fuente: `ms-win-menu-inicio.html`; «Mover Inicio a un lado» | verifier: writer: split between two list items |
| `m06-l02-q335` | `m06-l02-ex-9` | fuente: `ms-copilot-introduccion.html`; «Introducción a Microsoft Copilot» | verifier: writer: three separate list items |
| `m06-l02-q337` | `m06-l02-ex-9` | fuente: `ms-copilot-introduccion.html`; «Introducción a Microsoft Copilot» | verifier: the sentence holding the fact is not one paragraph of the saved copy (split by markup or a PDF line break) |
| `m06-l03-q215` | `m06-l03-ex-6` | fuente: `ms-win-atajos.html`; «Métodos abreviados de teclado con las teclas de Windows» | verifier: the sentence holding the fact is not one paragraph of the saved copy (split by markup or a PDF line break) |
| `m06-l03-q393` | `m06-l03-ex-11` | fuente: `ms-win-unidad-recuperacion.html`; «Crear una unidad de recuperación» | verifier: writer: a four-word list item apart from its intro |
| `m06-l04-q131` | `m06-l04-ex-4` | fuente: `ms-word-coautoria-documentos.html`; «Si la coautoría no funciona» | verifier: writer: NOT question resting on five checks under five subheadings |
| `m06-l04-q243` | `m06-l04-ex-6` | fuente: `ms-office-formatos-archivo.html`; «.dotm — Plantilla habilitada para macros de Word — Plantilla para crear nuevos archivos Word» | verifier: re-cited, but the blind re-check found the cited paragraph short of the fact |
| `m06-l04-q343` | `m06-l04-ex-8` | fuente: `ms-word-cinta.html`; «Personalizar la cinta de opciones en Word» | verifier: the sentence holding the fact is not one paragraph of the saved copy (split by markup or a PDF line break) |
| `m06-l04-q352` | `m06-l04-ex-8` | fuente: `ms-word-cinta.html`; «En la ventana Personalizar la cinta de opciones, seleccione Importar o exportar.» | verifier: re-cited, but the blind re-check found the cited paragraph short of the fact |
| `m06-l05-q113` | `m06-l05-ex-4` | fuente: `ms-excel-formato-fecha.html`; «En Tipo, elija un formato de fecha. Se verá una vista previa de su formato en el cuadro Muestra, con la primera fecha de sus datos.» | verifier: re-cited, but the blind re-check found the cited paragraph short of the fact |
| `m06-l06-q004` | `m06-l06-ex-1` | fuente: `ms-access-especificaciones.html`; «Número de caracteres de un nombre de campo — 64» | verifier: re-cited, but the blind re-check found the cited paragraph short of the fact |
| `m06-l06-q405` | `m06-l06-ex-10` | fuente: `ms-access-funcion-conmutador.html`; «Función Conmutador» | verifier: writer: split between the intro and a short list item |
| `m06-l06-q406` | `m06-l06-ex-10` | fuente: `ms-access-funcion-conmutador.html`; «La primera expresión verdadera tiene un valor correspondiente que es nulo.» | verifier: re-cited, but the blind re-check found the cited paragraph short of the fact |
| `m06-l07-q003` | `m06-l07-ex-1` | fuente: `ms-outlook-agregar-cuenta.html`; «Agregar una cuenta de correo electrónico» | verifier: the sentence holding the fact is not one paragraph of the saved copy (split by markup or a PDF line break) |
| `m06-l07-q008` | `m06-l07-ex-1` | fuente: `rfc5322-formato-mensaje.txt`; «3.4. Address Specification» | verifier: writer: the sentence is cut by an RFC page footer |
| `m06-l07-q023` | `m06-l07-ex-1` | fuente: `ms-outlook-smime.html`; «Cifrar todos los mensajes con S/MIME en el nuevo Outlook» | verifier: the sentence holding the fact is not one paragraph of the saved copy (split by markup or a PDF line break) |
| `m06-l07-q044` | `m06-l07-ex-2` | fuente: `ms-outlook-grupo-enviar.html`; «Enviar un correo electrónico a un grupo en el nuevo Outlook» | verifier: writer: split between two list items |
| `m06-l07-q046` | `m06-l07-ex-2` | fuente: `ms-outlook-compartir-carpeta.html`; «En la sección Permisos , seleccione la lista desplegable Nivel de permisos y seleccione los permisos que desea conceder a este usuario. Si no está seguro del nivel de permisos que debe seleccionar, consulte la siguiente sección Comprender los permisos de uso compartido.» | verifier: re-cited, but the blind re-check found the cited paragraph short of the fact |
| `m06-l07-q048` | `m06-l07-ex-2` | fuente: `ms-outlook-compartir-carpeta.html`; «En la sección Permisos , seleccione la lista desplegable Nivel de permisos y seleccione los permisos que desea conceder a este usuario. Si no está seguro del nivel de permisos que debe seleccionar, consulte la siguiente sección Comprender los permisos de uso compartido.» | verifier: re-cited, but the blind re-check found the cited paragraph short of the fact |
| `m06-l07-q068` | `m06-l07-ex-3` | fuente: `ms-outlook-delegados.html`; «Opciones para delegar una carpeta» | verifier: writer: split between the intro and two list items |
| `m06-l07-q159` | `m06-l07-ex-6` | fuente: `ms-outlook-procedimientos.html`; «Encontrar ese mensaje: búsqueda eficaz» | verifier: writer: route spread over three list items |
| `m06-l07-q171` | `m06-l07-ex-6` | fuente: `ms-outlook-limpiar-conversacion.html`; «Cambiar las opciones de limpieza de la conversación» | verifier: writer: route spread over three list items |
| `m06-l07-q311` | `m06-l07-ex-9` | fuente: `ms-outlook-graficos.html`; «Para insertar gráficos en mensajes en Outlook para PC, siga estos pasos.» | verifier: re-cited, but the blind re-check found the cited paragraph short of the fact |
| `m06-l07-q332` | `m06-l07-ex-10` | fuente: `ms-outlook-reglas.html`; «Ejecutar reglas de bandeja de entrada en mensajes existentes en el nuevo Outlook para Windows» | verifier: writer: route spread over two list items |
| `m06-l07-q349` | `m06-l07-ex-11` | fuente: `ms-outlook-listas-contactos.html`; «Seleccione Nuevo grupo de contactos en la cinta de opciones .» | verifier: re-cited, but the blind re-check found the cited paragraph short of the fact |
| `m06-l08-q057` | `m06-l08-ex-3` | fuente: `rfc1122-capas-tcp-ip.txt`; «1.1.3 Internet Protocol Suite» | verifier: writer: the protocols are a bulleted list apart from the intro |
| `m06-l08-q115` | `m06-l08-ex-4` | fuente: `ms-win-ping.html`; «/R — Especifica que se realiza un seguimiento de la ruta de acceso de ida y vuelta (disponible solo en IPv6).» | verifier: re-cited, but the blind re-check found the cited paragraph short of the fact |
| `m06-l08-q205` | `m06-l08-ex-7` | fuente: `aepd-guia-cookies.pdf`; «2.1.3. Tipos de cookies según el plazo de tiempo que permanecen activadas» | verifier: the sentence holding the fact is not one paragraph of the saved copy (split by markup or a PDF line break) |
| `m06-l08-q207` | `m06-l08-ex-7` | fuente: `aepd-guia-cookies.pdf`; «2.1.3. Tipos de cookies según el plazo de tiempo que permanecen activadas» | verifier: the sentence holding the fact is not one paragraph of the saved copy (split by markup or a PDF line break) |
| `m06-l08-q210` | `m06-l08-ex-7` | fuente: `aepd-guia-cookies.pdf`; «2.1.3. Tipos de cookies según el plazo de tiempo que permanecen activadas» | verifier: the sentence holding the fact is not one paragraph of the saved copy (split by markup or a PDF line break) |
| `m06-l08-q237` | `m06-l08-ex-8` | fuente: `ms-edge-inprivate.html`; «¿Qué hace Microsoft Edge con tus datos mientras te encuentras en InPrivate?» | verifier: writer: the negation lives only in the list's heading |
| `m06-l08-q249` | `m06-l08-ex-8` | fuente: `ms-edge-extensiones.html`; «A la derecha de la ventana que se abre, seleccione Notificar abuso.» | verifier: re-cited, but the blind re-check found the cited paragraph short of the fact |
| `m06-l08-q257` | `m06-l08-ex-9` | fuente: `aepd-guia-cookies.pdf`; «2.1.3. Tipos de cookies según el plazo de tiempo que permanecen activadas» | verifier: writer: the two types are in separate paragraphs |

# R3 closing steps (2026-10-27 → 28)

User's four closing items. Nothing committed.

1. **conv2022_X·P1·29.** Art. 62 LPAC added to m03-l03 (62.1–62.5, one citation per apartado; the 62.4 paragraph
   replaced with the checker's wording; blind check 3/3 PASS, `bank/lesson-fixes/r3-close/`). Two questions on art.
   63.1: q326 (passes, but «siempre de oficio» is a shared premise, so it claims no cover) and q327 («¿Cuál … es
   correcta?», key «se inicia siempre de oficio, por acuerdo del órgano competente», distractors from arts. 62.4,
   62.5 and 63.1; PASS; covers the official fact **partly** — the confusion the official question tests, a petición
   de parte or por denuncia, cannot be offered as a distractor under the user's constraint).
2. **Live pages.** The six saved Microsoft pages on the R2b list fetched live (es-es): visible text identical, saved
   sha256 match `fuentes.yaml`; no question re-verified, no new snapshot (`bank/bloque-vi/live-check-r3-close.md`).
   The es-es Word index page still says «punto y coma»; the Excel validation page still prints «225 caracteres».
3. **Explanations.** Scan of all 5,223 kept questions for (a) a distractor dismissed by the source's silence and
   (b) one sentence reused for several distractors: **289 flagged** (silence 255, repeated 34; bloque VI 136,
   I–V 153; q211 and q122 among them). Explanations rewritten (options untouched), each blind-checked, up to three
   passes (`bank/style-rewrites-*.json` and `*.check.md`). Outcome: **264 explanations rewritten and applied**;
   **25 questions dropped**, because no source sentence rules a distractor out (the explanation could not be fixed
   without inventing one): bloque VI 20, I–V 5 (m01-l02-q056, m03-l02-q038, m03-l04-q106, m04-l09-q060,
   m05-l03-q280). A rescan finds the phrases in 15 kept explanations, all rewrites a checker passed because each
   distractor also has a positive source sentence.
4. **Build.** All six bloques rebuilt: **5,200 kept** — I 675, II 264, III 775, IV 988, V 645, VI 1,853 (35.6 %);
   every bloque VI tema ≥ quota (VI.4 218/217). Goldens regenerated and read: citations 3,533 / 1,532 anchors (art.
   62 rows added); glossary 323 marks; lesson-refs unchanged in substance. Android and crypto-futures untouched.
   Suites: see the progress log (the Docker daemon was down, so the Testcontainers tests could not run).

# R3 close (2026-10-27): bloques I–V closed, bloque VI authored

Nothing committed. Session 5 to 7 work, run under `CLAUDE.md` «Subagent models and concurrency» from 2026-10-24
(writers sonnet, verifiers opus, at most four agents). The per-part log is «Session 6 progress» at the end of this file.

**Bank:** 5,223 kept questions. I 676 · II 264 · III 775 · IV 989 · V 646 · VI 1,873 (35.9 %; R5.1 asks ≥ 35 %).

**1. Re-verification of the Haiku-verified batches.** 718 questions (all of bloque V, IV.6 q101+, IV.5 q261), 25 blind
batches: 71 FAIL (9.9 %): style 41, citation 13, unique 8, official 7, key 2. Verifiers before the switch: 186/2,005
(9.3 %). Haiku verifiers had failed 186/919 (20 %), so they over-dropped and still passed about one in ten that a blind
check fails. All 71 replaced; replacements verified (several rounds; the last failures re-replaced).

**2. Decisions applied.**
- a. Parser: table cells that hold only citations anchor (test first); «fuente: `file`; «label»» resolves (test first).
  The held m05-l01 questions were rewritten and verified; about 50 table-fact questions written and verified
  (comisión de servicios and the provisión forms, RD 364/1995 plazos, IOC reglas, Tribunal de Cuentas, anexo II RD
  462/2002, the art. 48 TREBEP rows).
- b./c. Lesson additions and corrections in m02–m06, each blind-checked (failures fixed with the checker's wording and
  re-checked); listed in the theory ledger «R3 session 5–7 lesson fixes» as coverage-audit misses. Questions on the
  additions written and verified (.s5b–.s5d).
- d. Art. 35.2 LGP does say «de carácter plurianual» (m05-l01 unchanged); art. 24.5 LRJSP (3/3) and programas
  finalistas (4/4) authored with new stem forms and distractors and verified. Ruling recorded: check 5 compares stem
  and options, not the fact.
- Coverage: 25 official codes lost in earlier sessions recovered with new angles; **one is unreachable** (below).

**3. Bloque VI.** Spec `bank/bloque-vi/spec.md`, verifier spec `bloque-vi/verify-spec.md` (2026-10-24 ruling: every
distractor must be shown wrong by a page sentence; all saved pages grepped). Every recurring family ≥ 5, every listed
programme feature asked, every «Lo que más cae» line covered, 190 official codes covered, none copied.

| Tema | Quota | Authored | Kept | Stem forms (dir/cual/enun/señ) | Key longest | z edge / longest |
|---|---|---|---|---|---|---|
| VI.1 | 241 | 283 | 244 | 40/45/9/5 | 20 % | +1.40 / −0.24 |
| VI.2 | 202 | 235 | 228 | 44/42/7/6 | 24 % | +1.53 / +0.73 |
| VI.3 | 221 | 314 | 240 | 41/45/10/3 | 19 % | +0.42 / −0.69 |
| VI.4 | 217 | 292 | 223 | 40/48/8/4 | 18 % | −0.16 / −0.93 |
| VI.5 | 202 | 257 | 215 | 40/46/6/7 | 19 % | +0.31 / −0.61 |
| VI.6 | 253 | 300 | 276 | 39/47/7/7 | 21 % | +0.68 / +0.04 |
| VI.7 | 246 | 280 | 253 | 43/42/8/7 | 21 % | +0.98 / −0.35 |
| VI.8 | 168 | 203 | 194 | 41/45/8/7 | 24 % | +0.38 / +0.67 |
| **VI** | **1,750** | **2,164** | **1,873** | | | |

Drops: 291 (13 %), mostly stems without the version («Windows 11») and explanations that did not name each distractor;
both rules were made explicit in the spec mid-round and the failures rewritten. Difficulty about 30/50/20 in every tema.

**4. Build and checks.** Built II–VI (`build_exercises.py`; fixed to read only each lesson's main draft). Goldens
regenerated and read: citations 3,528 prose citations / 1,531 anchors (removed rows are moved anchors or intended
rewrites); glossary 324 web marks (a false-friend mark `g-oposicion` in m03-l03 given `link_except`); lesson-refs two
context shifts. Backend: ruff, format, mypy clean; pytest 1,497 passed, 20 skipped; `export_bundle.py --verify-only`
OK; `verify_golden_stability.py` exit 0. Frontend: build and `tsc -b` clean; vitest first run 2 failed (a Normativa
line read as a list marker in m02-l01 — fixed; the lesson-refs golden — regenerated); rerun after the fixes: 594 passed, 51 skipped, 0 failed.
crypto-futures and Android untouched.

**Open, for Juanjo**
- Unreachable cover: conv2022_X·P1·29 (art. 63.1 LPAC, sancionador «siempre de oficio»). Every honest option set pairs
  the official key with an official distractor, and art. 62 LPAC is not in m03-l03. Accept the gap, allow one question
  with that key and new non-official distractors, or add art. 62 to the lesson.
- For R2b (live-page currency): Word index separator (es «punto y coma» vs en «colon»); `ms-excel` data-validation
  «225 caracteres» (q370 dropped); `ms-win-update.html` update frequency; `ms-outlook-buscar.html` quotes;
  `ms-outlook-procedimientos.html` and `ms-outlook-limpieza-buzon.html` «Se aplica a».
- Theory ledger: label clash `ms-access-tipos-datos-escritorio.html` «Texto breve» vs «Texto corto» (not in the label
  table).

**Ten random bloque VI questions** (seed 20261027, from the kept set). Two weaknesses passed verification: q211's
explanation repeats one sentence for three distractors; q122 dismisses one distractor on the page's silence.

1. **m06-l02-q112** (VI.2, Ventanas, iconos, menús contextuales, cuadros de diálogo) — En el Explorador de archivos de Windows 11, ¿qué ocurre al mantener pulsada Mayús y hacer clic con el botón derecho del ratón en un elemento?
   - a) Se crea un acceso directo al elemento en la carpeta actual
   - b) Se abre otra instancia de la aplicación asociada al elemento
   - c) Se muestra el menú contextual Mostrar más opciones del elemento seleccionado  ✓
   - d) Se elimina el elemento sin moverlo a la Papelera de reciclaje
   Cita: fuente: `ms-win-atajos.html`; «Métodos abreviados de teclado del Explorador de archivos». Explicación: La tabla del Explorador de archivos dice que Mayús+clic con el botón derecho muestra «el menú contextual Mostrar más opciones para el elemento seleccionado». Un acceso directo se crea arrastrando el archivo con Alt pulsada. Abrir otra instancia es lo que hace Mayús al seleccionar un icono de la barra de tareas. Eliminar sin pasar por la Papelera es Mayús+Supr.

2. **m06-l01-q145** (VI.1, Sistemas de almacenamiento de datos) — ¿Cómo lee y escribe la información una unidad de disco duro (HDD), uno de los tipos de almacenamiento a largo plazo?
   - a) Con circuitos pequeños, sin ninguna parte móvil en la unidad.
   - b) Con una cinta magnética que debe rebobinarse o avanzarse.
   - c) Con memoria de acceso aleatorio, que se borra al apagar el equipo.
   - d) Con discos que giran rápido y un brazo con una cabeza.  ✓
   Cita: fuente: `ms-learn-equipos-almacenamiento.html`; «Unidades de disco duro». Explicación: La página describe el HDD como discos que giran rápido y usan un brazo y una cabeza para leer y escribir información, «algo así como un tocadiscos». Los circuitos sin partes móviles son la SSD, la cinta que se rebobina es el soporte anterior y la RAM es memoria a corto plazo, no almacenamiento.

3. **m06-l07-q342** (VI.7, Libreta de direcciones) — En Outlook 365 clásico, el método abreviado de teclado que abre la Libreta de direcciones es:
   - a) Ctrl+Mayús+B  ✓
   - b) Ctrl+Mayús+C
   - c) Ctrl+Mayús+L
   - d) Ctrl+Mayús+F
   Cita: fuente: `ms-outlook-atajos.html`; «Métodos abreviados de teclado de correo en la versión clásica de Outlook». Explicación: Ctrl+Mayús+B abre la Libreta de direcciones. Ctrl+Mayús+C crea un contacto. Ctrl+Mayús+L crea un grupo de contactos. Ctrl+Mayús+F abre la Búsqueda avanzada.

4. **m06-l02-q024** (VI.2, El entorno Windows. Fundamentos) — En Windows 11, ¿cómo se consigue que el Narrador se inicie automáticamente antes del inicio de sesión para todos los usuarios?
   - a) Marcando «Iniciar el Narrador después de iniciar sesión» en su configuración.
   - b) Marcando «Iniciar Lupa antes de iniciar sesión» en la configuración de la Lupa.
   - c) Marcando «Iniciar el Narrador antes del inicio de sesión» en su configuración.  ✓
   - d) Desmarcando la casilla de la Página principal del Narrador en su configuración.
   Cita: fuente: `ms-win-narrador.html`; «Inicia el Narrador automáticamente antes o después de que inicies sesión en el equipo». Explicación: Para iniciar el Narrador antes del inicio de sesión para todos los usuarios se marca la casilla «Iniciar el Narrador antes del inicio de sesión», en la configuración que abre Windows+Ctrl+N. La casilla de después de iniciar sesión lo arranca tras entrar; la opción de la Lupa arranca la Lupa, no el Narrador; y la casilla de la Página principal solo decide si esa página se abre al iniciar el Narrador.

5. **m06-l02-q231** (VI.2, El escritorio y sus elementos) — En Windows 11, ¿cuál de los siguientes botones permite elegir las aplicaciones que pueden enviar notificaciones mientras No molestar está activado?
   - a) Desactivar todas las notificaciones
   - b) Agregar aplicaciones  ✓
   - c) Borrar todo
   - d) Mostrar banners de notificación
   Cita: fuente: `ms-win-notificaciones.html`; «No molestar». Explicación: La página dice que, en Aplicaciones, se elige qué aplicaciones pueden enviar notificaciones con No molestar activado seleccionando el botón Agregar aplicaciones. Desactivar todas las notificaciones se aplica a una aplicación, Borrar todo limpia el centro y Mostrar banners es una opción por aplicación.

6. **m06-l06-q122** (VI.6, Tablas) — En Access 365, ¿qué ocurre si se intenta quitar una clave principal que forma parte de una relación de tabla?
   - a) Access elimina la relación automáticamente y quita la clave
   - b) Access quita la clave y deja la relación sin efecto
   - c) Access convierte la clave en una clave externa
   - d) Access advierte de que hay que eliminar primero la relación  ✓
   Cita: fuente: `ms-access-clave-principal.html`; «Quitar la clave principal en Access». Explicación: La ayuda dice que si se intenta quitar una clave principal que forma parte de una o más relaciones, «Access le advertirá de que debe eliminar primero la relación». Por eso no elimina la relación por su cuenta ni quita la clave dejándola sin efecto, y la página no habla de convertirla en clave externa.

7. **m06-l02-q225** (VI.2, El escritorio y sus elementos) — ¿Cuántas aplicaciones puede haber en Windows 11 con la prioridad de notificaciones más alta, Superior?
   - a) Hasta tres
   - b) Una por escritorio
   - c) Solo una aplicación  ✓
   - d) Todas ellas
   Cita: fuente: `ms-win-notificaciones.html`; «Configurar notificaciones». Explicación: La página dice que solo se puede establecer una aplicación como de máxima prioridad. Por tanto, hasta tres, una por escritorio o todas las aplicaciones contradicen esa limitación.

8. **m06-l04-q211** (VI.4, Creación y estructuración del documento) — En Word 365, ¿cuál de los siguientes ajustes de texto hace que una imagen no tenga anclaje visible en el documento?
   - a) Cuadrado
   - b) Detrás del texto
   - c) En línea con el texto  ✓
   - d) Arriba y abajo
   Cita: fuente: `ms-word-ajustar-imagenes.html`; «Información sobre los anclajes». Explicación: La página dice: «Los anclajes no aparecen para las imágenes incorporadas», las que están «en línea con el texto». Cuadrado se ancla a una ubicación específica del documento. Detrás del texto se ancla a una ubicación específica del documento. Arriba y abajo se ancla a una ubicación específica del documento.

9. **m06-l01-q321** (VI.1, Nociones básicas de seguridad informática) — Según el glosario de ciberseguridad del INCIBE, ¿cuál de las siguientes definiciones corresponde al spear phishing?
   - a) Una modalidad de phishing dirigida contra un usuario u organización en concreto.  ✓
   - b) Una modalidad de phishing que se envía de forma masiva a cualquier usuario.
   - c) Un ataque que modifica el archivo del servidor DNS para redirigir al usuario.
   - d) Una estafa por medios electrónicos que ofrece productos o servicios falsos a las víctimas.
   Cita: fuente: `incibe-glosario-ciberseguridad.pdf`; «Spear phishing». Explicación: El glosario define el spear phishing como una «modalidad de phishing dirigido contra un usuario u organización en concreto», con un correo que aparenta ser de un amigo o de una empresa conocida. Modificar el archivo del servidor de nombres de dominio para redirigir al usuario es el pharming, y la estafa por medios electrónicos con productos o servicios falsos es el scam.

10. **m06-l02-q352** (VI.2, Copilot) — En Outlook clásico o en el nuevo Outlook, ¿dónde aparece el resumen que genera Copilot de una conversación de correo?
   - a) Debajo del correo electrónico
   - b) En la parte superior del correo electrónico  ✓
   - c) En un panel lateral junto a la lista de mensajes
   - d) En una ventana emergente que oculta la conversación
   Cita: fuente: `ms-outlook-copilot-resumir.html`; «Resumen por Copilot». Explicación: La página dice que el resumen aparecerá en la parte superior del correo electrónico, y que puede incluir citas numeradas que llevan al correo correspondiente. Debajo del correo es donde se ve el resumen en Outlook para iOS y Android, y la página sitúa el resumen en la parte superior, no en un panel lateral ni en una ventana emergente.


# Session 6 (2026-10-24): resumed under `CLAUDE.md` «Subagent models and concurrency»

Writers sonnet, verifiers and re-checks opus, at most 4 agents (2 writers, 2 verifiers). Each agent appends one line
per finished part to «Session 6 progress (append-only)» at the end of this file. The Session 5 state below was
checked against the files on 2026-10-24: bloque VI drafts without a `writer-notes.md` (m06-l01 p1–p2, m06-l02 p2,
m06-l03 p2, m06-l05 p1, m06-l07 p1) are from interrupted runs and are completed before verification; m05-l02 s5 (29,
q278–q306) has no notes either.

Agent plan: writer A, bloques II–V (finish m05-l02 s5, then s5b new-fact questions for m03, m04, m02), then bloque VI
temas; writer B, bloque VI one tema per run (VI.1 first); verifier 1, re-checks (two m04 edits, m05-l02 l. 220) and
the unverified II–V files; verifier 2, bloque VI parts with notes, one part per batch.

# Session 5 (2026-10-22 → 23): paused by the user. Resume here

Nothing committed. Subagents run on the session model (`CLAUDE.md` has no «Subagent models» section).

**1. Re-verification: done.** 718 Haiku-passed questions (all of bloque V, IV.6 q101+, IV.5 q261) were re-checked
blind in 25 batches (`bloque-iv|v/<lesson>.reverify-N.md`; drops batch `<lesson>.reverify-N`). **71 FAIL / 718 =
9.9 %**: style 41, citation 13, unique 8, official 7, key 2. Before the switch, Opus verifiers failed 186/2,005 (9.3 %).
The Haiku verifiers had failed 186/919 (20 %), 90 on style and 49 official, so they over-dropped yet still let about
10 % through that a blind check fails. Questions Haiku dropped stay dropped. Fails per lesson: m05-l01 2, m05-l02 24,
m05-l03 12, m05-l04 9, m05-l05 6, m05-l06 6, m04-l06 12.

**Replacements and table facts** (brief `s5-writer-brief.md`; files `<lesson>.s5.draft.json`, each to be appended to
the lesson's draft, or its last part, once verified):

| Lesson | Written | Verified | Still to do |
|---|---|---|---|
| m04-l02 | 5 table facts (q067–q071) | 5/5 PASS | — |
| m04-l05 | 18 table facts (q262–q279; comisión de servicios, provisión forms, art. 48 rows) | **not yet** (verifier stopped) | verify |
| m04-l06 | 12 replacements + q280 (restores conv2020·P1·5) | **not yet** (stopped) | verify |
| m05-l01 | 2 replacements + 5 ex-held (q074–q080) | 6/7; q079 FAIL (plural cue) | replace q079 |
| m05-l04 | 9 replacements + 3 table facts (q079–q090) | **not yet** (stopped) | verify |
| m05-l05 | 6 replacements + 4 table facts (q087–q096) | **not yet** (stopped) | verify |
| m05-l06 | 6 replacements (q087–q092) | 6/6 PASS | — |
| m05-l02 | — (writer stopped before writing) | — | relaunch: 24 replacements (ids in `drops.tsv`, batch `m05-l02.reverify-*`), anexo I and other table facts, first id q278 |
| m05-l03 | — (writer stopped before writing) | — | relaunch: 12 replacements, IOC reglas and Tribunal de Cuentas table facts, first id q273 |

Covers still lost from earlier sessions (after the s5 files merge, rerun `lost_coverage.py`): V.4
conv2020_X·P1·38, conv2020·P1·27, conv2025_X·S2·3; V.5 conv2020_X·S2·10, conv2022_X·P1·24, conv2022_X·S2·11 (art. 79.1
LGP, dropped three times as rewordings), conv2025_A·S2R·3; V.6 conv2020_X·S1·1, conv2020_X·S2·13, conv2022·S2·7.

**2a. Platform: done.** Table cells that hold only citations anchor (`citations/lesson.py`, test first; golden +106).
A question citation «fuente: `file`; «label»» resolves to the file (`citations/course.py` `_labelled_source`, test
first). Both are in content/README.md. Goldens must be regenerated again after the lesson fixes.

**2b–2d. Lesson fixes: written, blind check partly done** (brief `lesson-fixes-brief.md`, checker brief
`lesson-fixes-check-brief.md`; records `lesson-fixes/<module>/writer.md`):
- m02: 4 items. **Checked, 4/4 PASS** (`lesson-fixes/m02/check.md`). Not done for want of a source: «Gobiernos
  Civiles» successor; TRLSC DA 3.ª (DUE cese).
- m03: 13 additions (art. 128.2 LJCA; month rule via art. 185.1 LOPJ and art. 5.1 CC; arts. 13, 30.2–3 LRJSP;
  arts. 95.3, 96.5, 106.3, 68.1, 89.1, 25.1.b) LPAC; art. 29.7 LCSP), 2 citation forms (art. 6 LJCA, art. 93.2 hoy),
  1 correction (m03-l07 Observatorio). Not done: RGLCAP absent; arts. 47–51, 123 LRJSP already stated. **Blind check
  not done** (checker stopped).
- m04: 5 hunks kept from the stopped run (m04-l07), 8 additions (arts. 207.1, 208.1 and DT 26.ª LGSS; art. 6 RD
  33/1986; arts. 25.3 and 30.2 LRJSP; art. 30.4 LPAC; art. 61.s) LRJSP; art. 29.3 Ley 30/1984; art. 98.3 TREBEP).
  **Blind check not done.**
- m05: 3 additions (arts. 62/63 criterion, anexo IV Res. 20-01-2014; art. 47.2 10 % and 47.4–6 LGP; art. 13.2 RD
  2188/1995), 4 corrections (esquema 40.1 letters, «Ministro de Economía» hoy, m05-l05 art. 63 vs 630, m05-l06 DA
  12.ª), 4 citation forms (incl. art. 34.1 LGP). Decision 2d: art. 35.2 LGP does say «de carácter plurianual», so it
  stays; the lesson already states the programas finalistas definition word for word. **Blind check not done.**
- Then: questions on the checked additions (a writer for m02 was started and stopped before writing; same s5 brief,
  but «write only on the added sentences»), decision 2d questions (art. 24.5 LRJSP, III.3; programas finalistas,
  V.1 lmc-7; new stem forms and distractors), the theory-ledger «coverage-audit miss» notes, verification.

Verify-spec rulings added (`bloque-ii/verify-spec.md`): check 5 compares stem and options, not the fact; a key half
resting on an uncited norm fails check 3; a norm named by number alone or by acronym fails checklist 2.

**3. Bloque VI: spec ready, no questions yet.** `bloque-vi/spec.md` (writers) and `bloque-vi/verify-spec.md`.
Sources: any fact on a saved page the lesson cites (R4.3: the bank carries the bloque), applying to Windows 11 /
Microsoft 365 desktop. Citation «fuente: `file`; «label»». Quotas from the index's per-application shares: VI.1 241,
VI.2 202, VI.3 221, VI.4 217, VI.5 202, VI.6 253, VI.7 246, VI.8 168 (1,750), in 32 parts of about 50–62 by line
range (table in the spec; ids part k from q(k−1)01). Ten part writers were launched and stopped before writing
anything; `bloque-vi/` holds only the specs. Relaunch prompt: «You are a question writer … Read and follow
`docs/age-verification/bank/bloque-vi/spec.md` exactly. Your part: tema VI.N, lesson m06-lNN, part-k. Ids from
m06-lNN-q(k−1)01.»

**4. Not run:** build, goldens, full suites.

**State at the 2026-10-23 usage limit (resets 12:10).**
- Passed blind verification since the pause: m04-l05 s5 18/18, m04-l06 s5 13/13, m05-l04 s5 12/12, m05-l05 s5 10/10,
  m05-l01 s5b 4/4 (q079 replacement + lmc-7 finalistas), m03-l03 s5 3/3 (art. 24.5 LRJSP), m02-l03 s5 2/2 (STC
  100/2019). Decision 2d closed.
- Lesson-fix checks: m03 15/16 and m04 13/15 and m05 14/15 PASS. The FAIL items were fixed with the checkers' wording
  (m03-l07 two sentences cut; m04-l09 art. 207.1 indemnización condition; m04-l06 «como el del pliego…»; m05-l04
  noveno.1 cheque conditions) plus m05-l02 l. 220 and l. 309 «(hoy: titular del Ministerio de Hacienda) (art. 5.1 RD
  829/2023)». Re-check `lesson-fixes/coordinator-recheck.md` passed m05-l04, m05-l02 l. 309 and m03-l07. **Still to
  re-check:** the two m04 edits and m05-l02 l. 220.
- Written, not verified: m05-l03 s5 (21: q273–q293), m05-l02 s5b and m05-l03 s5b (8 new-fact questions); bloque VI
  m06-l02 part-1 (60), m06-l04 part-1 (63), m06-l06 part-1 (59).
- Interrupted by the limit (resume each by SendMessage, or relaunch): m05-l02 s5 writer; m03 and m04 new-fact writers
  (s5b); verifiers of m05-l03 s5 and of m06-l02 part-1 q001–q030; bloque VI writers VI.1 p1–p2, VI.2 p2, VI.3 p1–p2,
  VI.4 p2, VI.5 p1–p2, VI.7 p1, VI.8 p1. Check each target file before relaunching; a partial draft may exist.
- Spec ruling added: pages on the «non-UI sources» list back concept questions only (bloque-vi/spec.md).
- Lesson gap noted by a verifier: m04-l06 l. ~290 gives the art. 94.3 TREBEP suspension rule only; art. 23 RD 33/1986
  (the expediente goes on; it is suspended only for delitos of títulos II and VII of libro II CP) is missing.

**Resume order:** (1) blind checks m03, m04, m05; (2) verify the m04-l05, m04-l06, m05-l04, m05-l05 s5 files;
relaunch the m05-l02 and m05-l03 writers; replace m05-l01 q079; (3) questions on the checked additions and 2d;
(4) bloque VI parts, at most 20 agents at once; (5) merge the s5 files, rebuild IV–V, build VI, goldens, suites,
ledger, ten bloque VI questions for Juanjo.

# Question bank ledger — age-administrativo-c1

Round R3 (requirements § 5). Plan and quotas: `docs/age-bank-plan.md`. Working files:
`docs/age-verification/bank/` (official questions per tema in `official/`, bloque I in `bloque-i/`). Nothing committed.

## Session 4 (2026-10-20 → 2026-10-22) — summary and where to resume

**Bloques II–V are closed and built.** Nothing committed. The course bank now holds **3,212 questions** for bloques
I–V (I 676, II 262, III 745, IV 937, V 592) against the plan's 2,850; every tema is above its quota.

| Bloque | Quota | Authored | Dropped | Kept | «Lo que más cae» tested |
|---|---|---|---|---|---|
| II | 222 | 288 | 26 | 262 | 40/40 |
| III | 668 | 848 | 103 | 745 | 68/68 |
| IV | 807 | 1,018 | 81 | 937 | 81/81 |
| V | 548 | 770 | 178 | 592 | 53/54 |

Per-tema tables, drop reasons, unaskable facts, lesson gaps and the ten questions for the reader are in each bloque's
section below (II.4, III.3, IV.5, V.2 samples).

- **Build:** `tools/build_exercises.py <bloque> <module>` per bloque (it now skips part drafts; engine temas merged with
  `tools/merge_parts.py`). Every citation resolves to an anchor.
- **Goldens:** `citations.es.txt` regenerated (the moved rows are the bloque II prose-gap rows only, read);
  `glossary-links.es.txt` one row moves (g-unidades-administrativas in m02-l02, onto the new art. 16.2 sentence);
  `lesson-refs.es.txt` unchanged.
- **Suites on the final tree:** backend `ruff check`, `ruff format --check`, `mypy src` clean, `pytest` 1,495 passed,
  20 skipped; frontend `npm run build`, `tsc -b` clean, `vitest` 593 passed, 51 skipped; `export_bundle.py
  --verify-only` OK (crypto-futures bundle and label catalogs unchanged); `verify_golden_stability.py` exit 0. The
  answer-bias guards over the whole AGE bank pass.
- **Method:** writers and verifiers per tema, two verify batches each, replacements under new ids through the same
  check. From 2026-10-22 `CLAUDE.md` sets writers to sonnet and verifiers to haiku. Tools added: `lint_drafts.py`
  (mechanical style faults verifiers fail), `lost_coverage.py`, `normalise_covers.py`, `ledger_rows.py`. The
  verifier spec gained two rulings (norms named by number and date when the title would pass 40 words; stems that name
  no norm are allowed). Coordinator drops are logged in each `drops.tsv` with batch `coordinator` and a reason.
- **Theory ledger:** «Bloque II prose gaps (R3, 2026-10-19)» records the m02 fixes.

**For the user to decide** (no question can be written until then):
1. Two «Lo que más cae»-level facts whose only sentence is an official exam key, so every question reads as a
   rewording: art. 24.5 LRJSP (III.3, three tries) and V.1 lmc-7 (programas finalistas, three tries; also blocked by
   m05-l01 l. 136 «de carácter plurianual»). Either a different lmc fact or a lesson change.
2. **Plain markdown tables** whose citations the resolver does not read (m04-l02, m04-l05, m05-l01, m05-l02, m05-l03):
   about 30 facts are blocked, among them comisión de servicios, adscripción provisional, the Tribunal de Cuentas
   Pleno and the IOC reglas. A parser change (read citations in a table's citation column) or a prose sentence per
   lesson unblocks them; m05-l01's five held questions (`bloque-v/m05-l01.held.json`) are ready to verify then.
3. Lesson facts official exams ask that no lesson states: art. 128.2 LJCA (August inhábil in the contencioso), the
   art. 62/63 nueva inversión vs reposición criterion (V.2 supuestos), art. 13.2 RD 2188/1995, arts. 207–208 LGSS,
   and the others listed per bloque.
4. Lesson errors found by verifiers (listed per bloque), notably the m05-l02 esquema tagging art. 40.1 letters wrongly
   and several old ministry names without «(hoy: …)».

**Resume (session 5): bloque VI.** Read this ledger, `docs/age-bank-plan.md` § 1–2 (bloque VI provisional quotas, 1,750
total), the requirements R5.1b, `docs/age-ofimatica-index.md` (recurring features → at least five questions each;
every programme feature → at least one; spread the 1,750 by the index's per-application shares; retired features not
asked), `docs/age-theory-ledger.md` «# Bloque VI» (saved sources, the «sin fuente oficial» list, the «Etiqueta del
examen / Etiqueta oficial» table) and `sources/otros/fuentes.yaml`. Write a bloque VI writer spec from
`bloque-ii/spec.md`: sources are the saved official pages, cited «(fuente: `file`; label)» as the lessons cite them;
the official Spanish label in stems (the exam's label may appear in the explanation); no question on a point two
official pages dispute (Impr Pant, the quick access toolbar position); stems never name an article (profile G-like
mix: mostly direct and «¿Cuál…?»). First fix the per-tema VI quotas from the index (the total stays 1,750), then
author VI.1–VI.8 in parts of about 60, verify in batches, replace, build `bloque-vi m06`, regenerate and read goldens,
run every suite. Writers sonnet, verifiers haiku; run `lint_drafts.py` before each hand-back.

## Session 3 (2026-10-19) — summary and where to resume

Paused by the user mid-round. **Bloques II–V are in progress; nothing is built** (no exercise YAML, `course.yaml`,
goldens or suites changed for them yet). Nothing committed.

**Method changes this session.**
- The writer and verifier specs for bloques II–V are `bank/bloque-ii/spec.md` and `verify-spec.md` (bloque I's, plus:
  options named by content in explanations; a stem that names no norm is read against every norm in force; length
  guard per tema, length-edge z and longest-is-correct z within ±1.5 at hand-back; date-computation rules, calendar
  checked with Python; TREBEP-vs-earlier-rule stems name the norm; old organ names only quoted). `bloque-iii/`,
  `-iv/`, `-v/` hold a pointer `spec.md`.
- Agents get a short prompt plus `bank/writer-brief.md` / `bank/verifier-brief.md`, which carry the lessons learned
  (lowercase «no» in a negative stem fails; options under five words that are not an organ, quantity or figure name
  fail; supuesto questions are the commonest «lightly reworded» drop; generator scripts in their own scratchpad
  subfolder; `covers` codes `P1`, `P1R`, `S1`, `S2`, `S1R`, `S2R`).
- Engine temas are written in three parts by lesson line range (`mBB-lTT.part-<k>.draft.json`, id ranges q001–,
  q101–, q201–), verified per part, and merged with `tools/merge_parts.py <bloque> <lesson>` before the build.
- New tools: `tools/lost_coverage.py` (a «Lo que más cae» line or official question claimed by some draft question but
  by no kept one: owes a replacement), `bank_stats.py` now prints key-shortest share and the two z-scores per tema.
  `bank_stats.py` and `check_anchors.py` take the bloque folder as their first argument.

**Bloque II prose gaps: closed.** All of «Esquemas bloque II» open item 1, in m02-l01 … m02-l04, plus 11 bare
`sources/otros/` citations rewritten to «(fuente: `file`; label)» (13 was the grep count with two index lines).
17 esquema rows restored and 2 cells extended (peticiones plazos; Patrimonio Documental table; registro `pasos`;
accesibilidad plazos; supresión-de-portal row; four rights rows; AEPD cese row; 65.5 cell). Blind check 65 items,
61 PASS; the 5 FAIL items (art. 9.2 LO 4/2001 order; art. 22.4 RGPD scope in prose and cell; «conforme al artículo
64.4» in art. 65.5 prose and cell) were fixed and re-checked by a new reviewer, 5/5 PASS. Records:
`bank/bloque-ii/prose-gaps/writer.md`, `verify.md`, `recheck.md`. Bloques III–V had no open prose gaps (their esquema
rounds closed them). The theory ledger still needs its note (to do at the bloque II build).
`test_esquema.py` passes; `citations.es.txt` has moved (53 rows added, 2 removed in m02) and is not regenerated.

**State per tema at the pause** (authored / dropped / kept; files in `bank/<bloque>/`):

| Tema | Quota | State |
|---|---|---|
| III.1 | 53 | done: 61 / 4 / 57, every lmc covered, z +0.82 / +0.32 |
| III.2 | 57 | verified: 74 / 4 / 70; replacements q075 (art. 41.5, conv2022·P1·20, lmc-6) and q076 (art. 98.1.b, conv2020_X·S2·5) written, **not yet verified** (`m03-l02.replacements.verify-1`) |
| III.3 part 1 | 60 | verified: 71 / 10 / 61 |
| III.3 part 2 | 75 | drafted 91 (q101–q191); not verified (verify-1 q101–q145, verify-2 q146–q191) |
| III.3 part 3 | 65 | drafted 76 (q201–q276); not verified (verify-1 q201–q238, verify-2 q239–q276) |
| III.4 part 1 | 65 | verified: 81 / 17 / 64 (verify-2: 10 of its 11 FAILs were official computation cases reworded, e.g. garantía definitiva, valor estimado); one short of the part target, so check `lost_coverage.py` and add replacements from new angles |
| III.4 part 2 | 65 | verified: 75 / 7 / 68 |
| III.4 part 3 | 65 | drafted 78 (q201–q278); not verified (verify-1 q201–q239, verify-2 q240–q278) |
| III.5 | 51 | done: 62 / 4 / 58 |
| III.6 | 58 | done: 72 / 5 / 67 (replacements q070–q072, 3/3 PASS) |
| III.7 | 54 | done: 64 / 6 / 58 |
| II.1–II.4 | 222 | not started (writers stopped before writing; relaunch) |
| IV.1–IV.9 | 807 | not started (writers stopped; their partial drafts deleted) |
| bloque V, bloque VI | | not started |

**Resume (session 4):** done (see «Session 4» above).

~~**Resume (session 4).**~~
1. All agents were stopped at the pause; their partial drafts were deleted and they left no reports or drop lines.
   Every file now under `bank/bloque-*/` is complete.
2. Finish bloque III: the six open verify batches (III.3 parts 2–3, III.4 part 3), III.2's replacement check, then `lost_coverage.py` on every
   tema and replacements where a cover is lost, `merge_parts.py` for m03-l03 and m03-l04, the build.
3. Then bloque II (write, verify), IV (write in parts as the table's engine split: IV.4 l. 16–101 / 102–238 / 239–338;
   IV.5 l. 15–139 / 140–237 / 238–317; IV.6 l. 13–117 / 118–255 / 256–352), V, VI, each built in order II, III, IV, V with its suites; the build steps are
   in the round prompt and in «Session 2» below.

**Lesson gaps found (no question asks them; for the user to decide):**
- m03-l03 does not state art. 128.2 LJCA (August inhábil in the contencioso) or the date-to-date month rule for the
  contencioso; contencioso date questions avoid August. `art. 6 LJCA` resolves to no anchor (two questions cite DA 1.ª
  LO 1/2025 instead).
- m03-l03 does not state art. 16.1, 16.2, 16.4–16.7 LPAC (registro), art. 13 LRJSP suplencia, art. 30.2 LRJSP (start of
  prescription), art. 95.3 párr. 2, 96.5, 106.3 LPAC — all asked in official exams (2020 mostly; conv2025_A·P1·13 for
  16.1). The registro facts may be covered by II.2.
- m03-l05: arts. 47–49, 51, 123 LRJSP, art. 10 LGS, arts. 25.1.b, 89.1 LPAC (official questions filed «III.3 (o
  III.5)» / «V.6 (o III.5)»). m03-l06: art. 68 LPAC subsanación; the recurso against the resolution (in III.3).
- m03-l04: art. 29.7 LCSP (exception to the one-year contrato menor) is not stated; Orden HAC/1517/2025 citations
  resolve to no anchor, so threshold questions cite the LCSP articles.

**Smaller notes for the theory ledger:** m03-l04 «Procedimiento restringido» paragraph drops «como mínimo» / «no será inferior a» from arts. 161.3, 164.1–2 plazos (its table is right); m03-l03 art. 93.2 LRJSP names «Ministerio de Hacienda y Administraciones
Públicas» without «(hoy: …)»; m03-l07 cites art. 20 RD 829/2023 for the Observatorio's adscripción, which that article
does not state; RD 1112/2018 plazos are not basic after STC 100/2019 (m02-l03 does not say so); art. 3.2 RD 208/1996
now names repealed LO 5/1992 and art. 37 Ley 30/1992 without «(hoy: …)».

## Bloque V (session 4, built 2026-10-22)

**592 questions** (33 quiz exercises, `m05-lTT-ex-N`), listed in `course.yaml`. V.2 and V.3 were written in three parts
each and merged. Writers ran on sonnet and verifiers on haiku (`CLAUDE.md`, from 2026-10-22). Working files and
reports in `docs/age-verification/bank/bloque-v/`. Every tema is above its quota.

| Tema | Quota | Authored | Dropped (key / unique / citation / style / official) | Kept | LMC covered |
|---|---|---|---|---|---|
| V.1 | 55 | 68 | 9 (0 / 5 / 0 / 3 / 1) | 59 | 7/8 |
| V.2 | 165 | 244 | 70 (1 / 6 / 5 / 47 / 11) | 174 | 7/7 |
| V.3 | 155 | 208 | 42 (1 / 5 / 11 / 17 / 8) | 166 | 10/10 |
| V.4 | 59 | 78 | 15 (2 / 3 / 0 / 3 / 7) | 63 | 9/9 |
| V.5 | 60 | 86 | 15 (0 / 4 / 1 / 2 / 8) | 71 | 10/10 |
| V.6 | 54 | 86 | 27 (6 / 4 / 0 / 13 / 4) | 59 | 10/10 |
| **Bloque V** | **548** | **770** | **178 (10 / 27 / 17 / 85 / 39)** | **592** | **53/54** |

| Tema | art-compl. / art-preg. / directa / cuál / enunc. / señale / norma | Names article | Negative | Key longest | Diff 1/2/3 | Key a/b/c/d |
|---|---|---|---|---|---|---|
| V.1 | 39 / 10 / 24 / 20 / 3 / 2 / 2 % | 53 % | 1 | 20 % | 19/28/12 | 16/15/13/15 |
| V.2 | 37 / 21 / 18 / 16 / 4 / 2 / 3 % | 61 % | 2 | 24 % | 41/96/37 | 46/43/41/44 |
| V.3 | 39 / 15 / 15 / 19 / 10 / 1 / 1 % | 69 % | 0 | 25 % | 45/92/29 | 39/43/43/41 |
| V.4 | 38 / 22 / 17 / 11 / 3 / 3 / 5 % | 62 % | 0 | 21 % | 15/35/13 | 15/15/17/16 |
| V.5 | 31 / 23 / 25 / 10 / 10 / 0 / 1 % | 61 % | 1 | 24 % | 18/36/17 | 18/18/19/16 |
| V.6 | 41 / 14 / 20 / 10 / 5 / 2 / 8 % | 59 % | 1 | 22 % | 20/29/10 | 14/15/15/15 |

Course-wide over bloque V: length edge z −0.04, longest-is-correct z +0.78. V.3 names the article in 69 % of stems.

**Drops.** 178 of 770 (23 %), far above bloques II–IV. Most were slips the sonnet writers made and the lint now
catches (`tools/lint_drafts.py`: option references by position, stems under 15 or over 40 words, article numbers as
options, short norm names such as «la Ley General Presupuestaria»), plus one batch of six keys on the wrong option
(V.6; the writer brief now requires the script to set `correct` from the key text). A haiku verifier misread checklist
item 2 as forbidding stems that name no norm; its 16 verdicts were withdrawn and the questions re-checked blind under an
explicit ruling now in `verify-spec.md` («Stems that name no norm are allowed»), 10 of 16 passing. Coordinator drops:
V.3 q242–q250 (LO 2/1982 articles cited only in a lesson table, no anchor), V.4 q045 (two readings of «tres veces»),
V.5 q062 (art. 79.4 LGP vs art. 10.2 RD 640/1987), V.5 q069 (regla 30 IOC changed by Orden HAC/965/2024, not in
sources), V.6 q080 (near-duplicate of q084).

**«Lo que más cae» line not tested — for the user to decide:** V.1 lmc-7 (programas finalistas, art. 6 apartado 1.1
Orden HAC/557/2026): three tries (q052, q072, q073) dropped; the definition is the official key of conv2022_X·P1·17,
and m05-l01 l. 136 calls programas presupuestarios «de carácter plurianual», which makes plurianual distractors
defensible. A different «Lo que más cae» fact, or that lesson sentence reworded, unblocks it.

**2022–2025 official facts no kept question tests** (each tried at least twice; the rule's sentence is the official
key): conv2022_X·S1R·2, conv2022·S1R·1, conv2024_A·P1·36, conv2025_A·S2·12 (V.2); conv2022_X·P1·27, conv2024_A·S1·18,
conv2024_X·P1R·5 (V.3); conv2025_X·S2·3 (V.4); conv2022_X·P1·24, conv2022_X·S2·11, conv2025_A·S2R·3 (V.5);
conv2022·S2·7 (V.6).

**Lesson gaps found** (no question asks them):
- Plain markdown tables whose citations the resolver does not read: m05-l01 «Terminología y desarrollo» (arts. 4.2, 5,
  7.1 Orden HAC/557/2026; five questions written and held in `bloque-v/m05-l01.held.json`), m05-l02 anexo I Orden
  HAC/557/2026, m05-l03 Tribunal de Cuentas table (arts. 21, 29, 30.Uno LO 2/1982) and the IOC reglas rows.
- m05-l02 gives no criterion between nueva inversión (art. 62) and reposición (art. 63), so the official supuestos that
  classify an expense are unaskable; its esquema «Estructura de los estados de gastos» (l. 73–74) tags orgánica 40.1.b
  and programas 40.1.c where the LGP and its own prose say 40.1.a and 40.1.b; l. 180 and 345 use «Ministro de
  Economía» unmarked; l. 304 calls the 9.Dos.2–5 transfers «del Ministro de Hacienda» though 9.Dos.5 belongs to
  department heads.
- m05-l03: art. 13.2 RD 2188/1995 (fiscalización in ten / five days) not stated; `art. 15.A).1.º RD 1009/2023` split
  across lines resolves to no anchor and its «(hoy: …)» parenthesis is unbalanced.
- m05-l04: «Formas de pago» cites apartado noveno.1 Orden PRE/1576/2002 outside parentheses (no anchor); anexo II RD
  462/2002 resolves to no anchor.
- m05-l05 l. 440 merges art. 63 «inútiles por uso normal» with concepto 630. m05-l06 l. 70–71 says no due date falls
  on a weekend under DA 12.ª LCSP (it only moves an inhábil last day).
- Sources: Orden HAC/965/2024 (regla 30 IOC from 2025-01-01) is not in `sources/normativa`.

### Ten V.2 questions for the reader

Ten kept V.2 questions drawn with `random.Random(20261022).sample(kept, 10)` over the 174 kept, shown as authored.

**1. `m05-l02-q001`** · art. 33.2 LGP · dificultad 2

> De acuerdo con el artículo 33.2 de la Ley 47/2003, de 26 de noviembre, General Presupuestaria, los Presupuestos Generales del Estado determinarán las obligaciones económicas que:
>
> a) Como mínimo, deben reconocer los sujetos que el artículo 33.1.a) incluye en los presupuestos de carácter limitativo.
>
> b) Como máximo, pueden reconocer los sujetos que el artículo 33.1.a) incluye en los presupuestos de carácter limitativo. **(clave)**
>
> c) Como máximo, pueden reconocer las entidades de los sectores empresarial y fundacional, de presupuesto estimativo.
>
> d) Como máximo, pueden reconocer los consorcios y las universidades no transferidas, con presupuesto de carácter estimativo.
>

*Explicación.* El artículo 33.2.a) habla de las obligaciones que, «como máximo», pueden reconocer los sujetos del artículo 33.1.a): el presupuesto limita, no obliga a gastar. La opción del mínimo cambia ese límite en un suelo. Las dos opciones de las entidades empresariales, fundacionales, consorcios y universidades describen a los sujetos del artículo 33.1.b), de presupuesto estimativo, que no reconocen obligaciones con ese límite.

**2. `m05-l02-q031`** · art. 43.1 LGP · dificultad 2

> Según el artículo 43.1 de la Ley 47/2003, de 26 de noviembre, General Presupuestaria, en el presupuesto del Estado los créditos se especificarán:
>
> a) A nivel de artículo, salvo personal y bienes y servicios, a nivel de concepto, e inversiones reales, a nivel de capítulo.
>
> b) A nivel de concepto, salvo personal e inversiones reales, a nivel de artículo, y bienes y servicios, a nivel de capítulo.
>
> c) A nivel de concepto, salvo personal y bienes y servicios, a nivel de artículo, e inversiones reales, a nivel de capítulo. **(clave)**
>
> d) A nivel de capítulo, salvo personal y bienes y servicios, a nivel de artículo, e inversiones reales, a nivel de concepto.
>

*Explicación.* En el Estado la regla general es el concepto. Los gastos de personal y los gastos corrientes en bienes y servicios se especifican a nivel de artículo, y las inversiones reales a nivel de capítulo. Las otras tres opciones permutan los niveles: regla general de artículo, bienes y servicios a nivel de capítulo, o regla general de capítulo con inversiones a nivel de concepto.

**3. `m05-l02-q073`** · art. 40.1.b) LGP · dificultad 2

> Según el artículo 40.1.b) de la Ley 47/2003, de 26 de noviembre, General Presupuestaria, la clasificación por programas permite a los centros gestores establecer los objetivos a conseguir de acuerdo con:
>
> a) La Intervención General de la Administración del Estado.
>
> b) El Consejo de Ministros.
>
> c) El Tribunal de Cuentas.
>
> d) El Ministerio de Hacienda. **(clave)**
>

*Explicación.* El artículo 40.1.b) dice que los centros gestores establecen los objetivos «de acuerdo con el Ministerio de Hacienda». Ni la Intervención General ni el Consejo de Ministros ni el Tribunal de Cuentas intervienen en esa fijación según el artículo.

**4. `m05-l02-q101`** · art. 51 LGP · dificultad 1

> Según el artículo 51 de la Ley 47/2003, de 26 de noviembre, General Presupuestaria, ¿qué enumeración recoge todas las modificaciones con las que durante el ejercicio puede variar la cuantía y finalidad de los créditos?
>
> a) Transferencias, generaciones, ampliaciones, créditos extraordinarios y suplementos de crédito, y anticipos de tesorería.
>
> b) Transferencias, ampliaciones, créditos extraordinarios y suplementos de crédito, incorporaciones y prórrogas de crédito.
>
> c) Transferencias, generaciones, ampliaciones, créditos extraordinarios y suplementos de crédito.
>
> d) Transferencias, generaciones, ampliaciones, créditos extraordinarios y suplementos de crédito, e incorporaciones. **(clave)**
>

*Explicación.* El artículo 51 enumera cinco clases: transferencias, generaciones, ampliaciones, créditos extraordinarios y suplementos, e incorporaciones. La opción con anticipos de tesorería cambia las incorporaciones por una figura que el artículo 60 regula aparte y que no modifica créditos. La opción con prórrogas de crédito añade una figura ajena al artículo y omite las generaciones. La que termina en suplementos de crédito deja fuera las incorporaciones.

**5. `m05-l02-q104`** · art. 50.1 LGP · dificultad 1

> Según el artículo 50.1 de la Ley 47/2003, de 26 de noviembre, General Presupuestaria, el presupuesto del Estado incluye el Fondo de Contingencia de ejecución presupuestaria para hacer frente durante el ejercicio a:
>
> a) Necesidades aplazables al ejercicio siguiente y de carácter discrecional, para las que se hizo una dotación insuficiente de crédito.
>
> b) Gastos de la Administración decididos libremente durante el ejercicio, aunque carezcan de cobertura presupuestaria y de crédito.
>
> c) Necesidades inaplazables y no discrecionales para las que no hubo, en todo o en parte, dotación adecuada de crédito. **(clave)**
>
> d) Desviaciones de tesorería del ejercicio, siempre que las apruebe el Ministro de Hacienda mediante orden ministerial.
>

*Explicación.* La finalidad del Fondo son las necesidades inaplazables y no discrecionales sin dotación adecuada de crédito. La opción de las necesidades aplazables y discrecionales invierte ambos requisitos. La de los gastos decididos libremente contradice la prohibición final del artículo 50.1. La de las desviaciones de tesorería mezcla el Fondo con los anticipos de tesorería, que son otra figura.

**6. `m05-l02-q105`** · art. 50.1 LGP · dificultad 1

> ¿Cuál de las siguientes modificaciones de crédito puede financiar el Fondo de Contingencia, cuando proceda, conforme al artículo 50.1 de la Ley 47/2003, de 26 de noviembre, General Presupuestaria?
>
> a) Las incorporaciones de crédito. **(clave)**
>
> b) Las generaciones de crédito por ingresos.
>
> c) Las transferencias de crédito.
>
> d) Los anticipos de tesorería.
>

*Explicación.* El Fondo únicamente financia ampliaciones, créditos extraordinarios y suplementos, e incorporaciones. Las generaciones se financian con los ingresos que las originan, las transferencias con el traspaso de dotaciones entre créditos, y los anticipos de tesorería no son una modificación del artículo 51.

**7. `m05-l02-q120`** · art. 55.1 LGP · dificultad 1

> Un departamento necesita atender un gasto inaplazable para el que no existe ninguna aplicación presupuestaria adecuada. No hay crédito ampliable ni otra figura que lo dote. ¿Qué modificación procede?
>
> a) Una ampliación de crédito.
>
> b) Una generación de crédito.
>
> c) Una incorporación de crédito.
>
> d) Un crédito extraordinario. **(clave)**
>

*Explicación.* Cuando el gasto no puede demorarse, no existe crédito adecuado y las demás figuras no sirven, el artículo 55.1 manda tramitar un crédito extraordinario, o un suplemento si el crédito existe pero es insuficiente. La ampliación exige un crédito declarado ampliable, la generación unos ingresos que la justifiquen y la incorporación un remanente del ejercicio anterior.

**8. `m05-l02-q139`** · art. 62.1.d) LGP · dificultad 1

> Los intereses de la Deuda del Estado agotan antes de fin de ejercicio el crédito consignado. ¿Qué modificación permite incrementarlo hasta el importe de las obligaciones, sin tramitar un suplemento?
>
> a) Una generación de crédito.
>
> b) Una incorporación de crédito.
>
> c) Una ampliación de crédito. **(clave)**
>
> d) Una transferencia de crédito.
>

*Explicación.* Los créditos de la Deuda del Estado son ampliables (art. 54.1) y, por serlo, se atienden con ampliación y no con suplemento. La generación exige unos ingresos nuevos, la incorporación un remanente del ejercicio anterior y la transferencia traspasa dotaciones de otro crédito.

**9. `m05-l02-q231`** · art. 9.Dos.1 Ley 31/2022 · dificultad 2

> Según el artículo 9.Dos.1 de la Ley 31/2022, de 23 de diciembre, de Presupuestos Generales del Estado para el año 2023, ¿quién autoriza las transferencias que minoren los créditos consignados para atender obligaciones de ejercicios anteriores?
>
> a) El titular del ministerio afectado, previo informe favorable de la Intervención Delegada.
>
> b) El Presidente o Director del organismo autónomo afectado.
>
> c) El Gobierno, a propuesta del Ministro de Hacienda.
>
> d) La persona titular del Ministerio de Hacienda. **(clave)**
>

*Explicación.* El artículo 9.Dos.1 atribuye a la persona titular del Ministerio de Hacienda autorizar las transferencias que minoren los créditos consignados para obligaciones de ejercicios anteriores (art. 8.Uno.1). El titular del ministerio, el director del organismo y el Gobierno no tienen esa competencia en ese artículo.

**10. `m05-l02-q244`** · art. 62.1.a) LGP · dificultad 1

> Según el artículo 62.1.a) de la Ley 47/2003, de 26 de noviembre, General Presupuestaria, el Ministro de Hacienda autoriza las transferencias:
>
> a) entre distintas secciones presupuestarias como consecuencia de reorganizaciones administrativas de los departamentos.
>
> b) no reservadas al Consejo de Ministros que, conforme al artículo 63, no puedan acordar los titulares de los departamentos. **(clave)**
>
> c) entre créditos de un mismo programa, aunque puedan acordarlas directamente los titulares de los departamentos.
>
> d) de todos los organismos autónomos, sin que estos puedan acordar ninguna de ellas por sí mismos en su presupuesto.
>

*Explicación.* El artículo 62.1.a) es residual: el Ministro de Hacienda autoriza las transferencias no reservadas al Consejo de Ministros que los titulares de los departamentos no pueden acordar por el artículo 63. Las reorganizaciones entre secciones las autoriza el Gobierno (art. 61.a)), las de un mismo programa las acuerda el titular del ministerio y los organismos autónomos autorizan las del artículo 63.2 en su presupuesto.


## Bloque II (session 4, built 2026-10-22)

**262 questions** in `content/age-administrativo-c1/exercises/` (16 quiz exercises, `m02-lTT-ex-N`), listed in
`course.yaml`. Working files and verification reports in `docs/age-verification/bank/bloque-ii/`; drop log
`bloque-ii/drops.tsv`. Prose gaps closed first (see «Session 3»: 65 items, 5 fixed and re-checked, records in
`bloque-ii/prose-gaps/`). Every tema is above its quota, every «Lo que más cae» line is tested, no official cover is
lost.

| Tema | Quota | Authored | Dropped (key / unique / citation / style / official) | Kept | LMC covered |
|---|---|---|---|---|---|
| II.1 | 55 | 64 | 0 (0 / 0 / 0 / 0 / 0) | 64 | 10/10 |
| II.2 | 54 | 71 | 3 (0 / 0 / 0 / 3 / 0) | 68 | 10/10 |
| II.3 | 56 | 85 | 18 (0 / 2 / 1 / 14 / 1) | 67 | 10/10 |
| II.4 | 57 | 68 | 5 (0 / 1 / 0 / 3 / 1) | 63 | 10/10 |
| **Bloque II** | **222** | **288** | **26 (0 / 3 / 1 / 20 / 2)** | **262** | **40/40** |

| Tema | art-compl. / art-preg. / directa / cuál / enunc. / señale / norma | Names article | Negative | Key longest | Diff 1/2/3 | Key a/b/c/d |
|---|---|---|---|---|---|---|
| II.1 | 38 / 16 / 22 / 14 / 6 / 3 / 2 % | 53 % | 0 | 25 % | 19/32/13 | 16/16/16/16 |
| II.2 | 38 / 12 / 16 / 19 / 7 / 3 / 4 % | 56 % | 2 | 24 % | 21/33/14 | 17/16/18/17 |
| II.3 | 36 / 19 / 21 / 13 / 6 / 3 / 1 % | 55 % | 0 | 24 % | 21/34/12 | 16/17/17/17 |
| II.4 | 35 / 21 / 25 / 10 / 3 / 2 / 5 % | 56 % | 1 | 22 % | 16/32/15 | 17/16/15/15 |

Course-wide over bloque II: length edge z +1.69, longest-is-correct z +0.49 (inside the ±2 guard; the platform test over
the whole AGE bank passes). Most drops were one generator slip in II.3 («de el Real Decreto», 13 questions), replaced
under new ids and re-verified; the lint tool (`tools/lint_drafts.py`) now catches it.

**Notes for the theory ledger:** m02-l01 l. 283–285 gives the old ministry name of art. 17.2 RD 951/2005 without
«(hoy: …)», and art. 9.1 LO 4/2001 «Gobiernos Civiles» likewise; art. 3.2 RD 208/1996 names repealed LO 5/1992 and
art. 37 Ley 30/1992; RD 1112/2018 arts. 12–13 are not basic after STC 100/2019 (stems name the RD); art. 18.1 RD
1112/2018 «Ministerio de Política Territorial y Función Pública» without «(hoy: …)»; m02-l03 does not say the DUE
also carries the cese trámites (disp. adic. 3.ª.1.d TRLSC).

### Ten II.4 questions for the reader

Ten kept II.4 questions drawn with `random.Random(20261022).sample(kept, 10)` over the 63 kept, shown as authored.

**1. `m02-l04-q004`** · art. 3.1 LOPDGDD · dificultad 2

> Según la Ley Orgánica 3/2018, de Protección de Datos Personales y garantía de los derechos digitales, ¿quiénes pueden dirigirse al responsable del tratamiento para solicitar el acceso a los datos de una persona fallecida?
>
> a) Las personas vinculadas al fallecido por razones familiares o de hecho y sus herederos. **(clave)**
>
> b) Únicamente sus herederos, sean testamentarios o abintestato.
>
> c) Las personas vinculadas al fallecido por razones familiares, con exclusión de las de hecho.
>
> d) Únicamente sus parientes por consanguinidad hasta el segundo grado.
>

*Explicación.* El artículo 3.1 dice que «las personas vinculadas al fallecido por razones familiares o de hecho así como sus herederos» pueden dirigirse al responsable o encargado para pedir el acceso. No se limita a los herederos. Incluye expresamente a las personas vinculadas por razones de hecho. No fija ningún grado de parentesco.

**2. `m02-l04-q013`** · art. 22.3 LOPDGDD · dificultad 2

> Unas cámaras de seguridad captan imágenes el martes 9 de febrero de 2027 que no han de conservarse para acreditar actos contra la integridad de personas, bienes o instalaciones. Según la Ley Orgánica 3/2018, de Protección de Datos Personales y garantía de los derechos digitales, ¿hasta qué fecha pueden conservarse?
>
> a) Hasta el martes 9 de marzo de 2027. **(clave)**
>
> b) Hasta el viernes 12 de febrero de 2027.
>
> c) Hasta el martes 23 de febrero de 2027.
>
> d) Hasta el viernes 9 de abril de 2027.
>

*Explicación.* El artículo 22.3 dice que los datos «serán suprimidos en el plazo máximo de un mes desde su captación». El mes se cuenta de fecha a fecha: desde el martes 9 de febrero de 2027 vence el martes 9 de marzo de 2027, un día laborable sin festivo en el intervalo. El viernes 12 de febrero resulta de aplicar setenta y dos horas, que es el plazo para poner las imágenes a disposición de la autoridad. El martes 23 de febrero son diez días hábiles. El viernes 9 de abril son dos meses.

**3. `m02-l04-q016`** · art. 12.3 RGPD · dificultad 1

> De acuerdo con el artículo 12.3 del Reglamento (UE) 2016/679, de 27 de abril de 2016, el plazo de un mes del responsable para informar al interesado de sus actuaciones podrá prorrogarse en caso necesario:
>
> a) Otro mes, teniendo en cuenta la complejidad y el número de solicitudes.
>
> b) Otros dos meses, previa autorización de la autoridad de control competente.
>
> c) Otros tres meses, teniendo en cuenta la complejidad y el número de solicitudes.
>
> d) Otros dos meses, teniendo en cuenta la complejidad y el número de solicitudes. **(clave)**
>

*Explicación.* El artículo 12.3 dice que el plazo «podrá prorrogarse otros dos meses en caso necesario, teniendo en cuenta la complejidad y el número de solicitudes». La prórroga no es de un mes ni de tres. Tampoco necesita autorización de la autoridad de control: la decide el responsable y la comunica al interesado.

**4. `m02-l04-q017`** · art. 12.3 RGPD · dificultad 2

> Si el responsable del tratamiento decide prorrogar el plazo para atender una solicitud de ejercicio de derechos, ¿cuándo debe informar de la prórroga al interesado según el Reglamento general de protección de datos?
>
> a) En el plazo de un mes desde la recepción de la solicitud, indicando los motivos de la dilación. **(clave)**
>
> b) En el plazo de diez días desde la recepción de la solicitud, indicando los motivos de la dilación.
>
> c) Antes de que venza el plazo ya prorrogado, indicando los motivos de la dilación.
>
> d) En el plazo de un mes desde la recepción de la solicitud, sin necesidad de indicar motivos.
>

*Explicación.* El artículo 12.3 dice que el responsable informará de la prórroga «en el plazo de un mes a partir de la recepción de la solicitud, indicando los motivos de la dilación». No es un plazo de diez días. El aviso no puede esperar al final del plazo prorrogado. Los motivos de la dilación sí hay que indicarlos.

**5. `m02-l04-q020`** · art. 14 LOPDGDD · dificultad 2

> Según el artículo 14 de la Ley Orgánica 3/2018, de 5 de diciembre, de Protección de Datos Personales y garantía de los derechos digitales, quien ejerce el derecho de rectificación aportará la documentación justificativa de la inexactitud de los datos:
>
> a) Acompañándola a la solicitud cuando sea preciso. **(clave)**
>
> b) Dentro de los diez días siguientes a la solicitud.
>
> c) Solo cuando se lo requiera la autoridad de control.
>
> d) Solo cuando los datos procedan de un registro público.
>

*Explicación.* El artículo 14 dice que el afectado «deberá acompañar, cuando sea preciso, la documentación justificativa de la inexactitud o carácter incompleto de los datos». Se acompaña a la solicitud, sin un plazo posterior de diez días. No depende de un requerimiento de la autoridad de control. Tampoco de que los datos procedan de un registro público.

**6. `m02-l04-q024`** · art. 20.1 RGPD · dificultad 2

> Según el artículo 20.1 del Reglamento (UE) 2016/679, de 27 de abril de 2016, el derecho a la portabilidad existe cuando el tratamiento se efectúa por medios automatizados y está basado:
>
> a) En el consentimiento o en un contrato. **(clave)**
>
> b) En una obligación legal o en un contrato.
>
> c) En el consentimiento o en el interés público.
>
> d) En intereses legítimos o en un contrato.
>

*Explicación.* El artículo 20.1 exige que el tratamiento «esté basado en el consentimiento […] o en un contrato» y que se efectúe por medios automatizados. La obligación legal, el interés público y los intereses legítimos son otras bases de licitud del artículo 6.1 que no dan derecho a la portabilidad.

**7. `m02-l04-q040`** · art. 34.1 LOPDGDD · dificultad 1

> Una entidad aseguradora tiene treinta empleados. Según el artículo 34.1 de la Ley Orgánica 3/2018, de Protección de Datos Personales y garantía de los derechos digitales, ¿debe designar un delegado de protección de datos?
>
> a) Solo si trata a gran escala categorías especiales de datos.
>
> b) No, porque la designación es voluntaria para las entidades privadas.
>
> c) Sí, en todo caso, por ser una entidad aseguradora. **(clave)**
>
> d) Solo si se lo requiere la Agencia Española de Protección de Datos.
>

*Explicación.* El artículo 34.1.g) obliga a designar delegado «en todo caso» a «las entidades aseguradoras y reaseguradoras», sin atender al número de empleados. La obligación no depende de tratar categorías especiales a gran escala ni de un requerimiento de la Agencia. Para estas entidades la designación no es voluntaria.

**8. `m02-l04-q046`** · art. 39.1 RGPD · dificultad 1

> ¿Cuál de las siguientes es una de las funciones mínimas del delegado de protección de datos según el Reglamento (UE) 2016/679?
>
> a) Imponer multas administrativas al responsable.
>
> b) Cooperar con la autoridad de control. **(clave)**
>
> c) Autorizar la contratación de otros encargados.
>
> d) Determinar los fines y medios del tratamiento.
>

*Explicación.* El artículo 39.1.d) incluye entre las funciones mínimas del delegado «cooperar con la autoridad de control». Imponer multas es un poder de la autoridad de control. Autorizar a otros encargados corresponde al responsable (artículo 28.2). Determinar los fines y medios es lo que define al responsable.

**9. `m02-l04-q057`** · art. 65.5 LOPDGDD · dificultad 1

> Según el artículo 65.5 de la Ley Orgánica 3/2018, de Protección de Datos Personales y garantía de los derechos digitales, la decisión sobre la admisión o inadmisión de una reclamación deberá notificarse al reclamante en el plazo de:
>
> a) Un mes.
>
> b) Tres meses. **(clave)**
>
> c) Dos meses.
>
> d) Seis meses.
>

*Explicación.* El artículo 65.5 dice que la decisión sobre la admisión o inadmisión «deberá notificarse al reclamante en el plazo de tres meses». Un mes es el plazo del delegado del artículo 37.2. Dos meses es el del artículo 37.1. Seis meses no es el plazo de esta notificación.

**10. `m02-l04-q060`** · art. 73 LOPDGDD · dificultad 2

> Según la Ley Orgánica 3/2018, de Protección de Datos Personales y garantía de los derechos digitales, la contratación por un encargado del tratamiento de otros encargados sin contar con la autorización previa del responsable constituye una infracción:
>
> a) Leve, que prescribe al año.
>
> b) Grave, que prescribe a los dos años. **(clave)**
>
> c) Muy grave, que prescribe a los tres años.
>
> d) Grave, que prescribe al año.
>

*Explicación.* El artículo 73.l) califica como grave «la contratación por un encargado del tratamiento de otros encargados sin contar con la autorización previa del responsable», y el artículo 73 dice que las graves «prescribirán a los dos años». No es leve ni muy grave. Un año es la prescripción de las leves.

## Bloque IV (session 4, built 2026-10-22)

**937 questions** (46 quiz exercises, `m04-lTT-ex-N`), listed in `course.yaml`. IV.4, IV.5 and IV.6 were written in
three parts each and merged. Working files and reports in `docs/age-verification/bank/bloque-iv/`. Every tema is above
its quota and every «Lo que más cae» line is tested.

| Tema | Quota | Authored | Dropped (key / unique / citation / style / official) | Kept | LMC covered |
|---|---|---|---|---|---|
| IV.1 | 55 | 67 | 7 (1 / 1 / 0 / 4 / 1) | 60 | 9/9 |
| IV.2 | 55 | 66 | 4 (0 / 0 / 0 / 4 / 0) | 62 | 8/8 |
| IV.3 | 55 | 70 | 7 (0 / 1 / 0 / 6 / 0) | 63 | 8/8 |
| IV.4 | 155 | 185 | 5 (0 / 3 / 0 / 2 / 0) | 180 | 10/10 |
| IV.5 | 170 | 213 | 18 (1 / 2 / 2 / 7 / 6) | 195 | 10/10 |
| IV.6 | 150 | 208 | 26 (0 / 3 / 3 / 10 / 10) | 182 | 10/10 |
| IV.7 | 53 | 68 | 8 (0 / 0 / 1 / 6 / 1) | 60 | 8/8 |
| IV.8 | 60 | 74 | 3 (0 / 2 / 0 / 1 / 0) | 71 | 10/10 |
| IV.9 | 54 | 67 | 3 (0 / 2 / 0 / 1 / 0) | 64 | 8/8 |
| **Bloque IV** | **807** | **1018** | **81 (2 / 14 / 6 / 41 / 18)** | **937** | **81/81** |

| Tema | art-compl. / art-preg. / directa / cuál / enunc. / señale / norma | Names article | Negative | Key longest | Diff 1/2/3 | Key a/b/c/d |
|---|---|---|---|---|---|---|
| IV.1 | 38 / 17 / 23 / 10 / 7 / 2 / 3 % | 62 % | 0 | 18 % | 17/33/10 | 14/15/15/16 |
| IV.2 | 34 / 16 / 24 / 11 / 10 / 2 / 3 % | 60 % | 1 | 24 % | 17/33/12 | 16/15/15/16 |
| IV.3 | 37 / 22 / 24 / 11 / 3 / 0 / 3 % | 59 % | 0 | 24 % | 20/33/10 | 16/16/15/16 |
| IV.4 | 40 / 17 / 19 / 9 / 6 / 3 / 5 % | 61 % | 2 | 22 % | 49/96/35 | 46/46/43/45 |
| IV.5 | 42 / 14 / 25 / 10 / 5 / 1 / 4 % | 62 % | 1 | 22 % | 55/105/35 | 48/49/48/50 |
| IV.6 | 38 / 23 / 13 / 12 / 4 / 3 / 6 % | 67 % | 1 | 24 % | 50/90/42 | 48/45/43/46 |
| IV.7 | 43 / 13 / 23 / 12 / 7 / 0 / 2 % | 60 % | 0 | 27 % | 20/30/10 | 15/15/15/15 |
| IV.8 | 39 / 18 / 24 / 10 / 4 / 3 / 1 % | 65 % | 0 | 21 % | 20/38/13 | 17/20/17/17 |
| IV.9 | 39 / 16 / 22 / 11 / 8 / 3 / 2 % | 59 % | 0 | 22 % | 18/32/14 | 15/15/17/17 |

Course-wide over bloque IV: length edge z +0.07, longest-is-correct z +1.06. IV.1 key-longest is 18 % (target 20–28);
IV.6 names the article in 67 % of stems (the TREBEP-vs-RD 33/1986 rule makes its stems name the norm). From
2026-10-22 the project runs writers on sonnet and verifiers on haiku (`CLAUDE.md`); the haiku verifiers of IV.6 read
check 5 more strictly than the ruling (the official key alone, without an official distractor) and the coordinator
left those drops standing; replacements restored every «Lo que más cae» line.

**Official facts no kept question tests:** conv2020·P1·5 (IV.6); conv2020_X·S2R·1 (IV.4 and IV.7, jubilación
voluntaria organ, not in the lessons). **Coordinator drops:** IV.6 q264, q265 (duplicates of kept questions).

**Lesson gaps found** (no question asks them): m04-l02 cites arts. 20.1, 16.j), 23.1 RD 364/1995 only in a plain
markdown table, and m04-l05 cites arts. 59–60, 63, 64, 66 bis, 66 ter RD 364/1995 and 82.1 TREBEP only in the
«Otras formas de provisión» table: the resolver reads no citation in a plain table, so comisión de servicios,
adscripción provisional, redistribución, reasignación and the movilidades have no question (conv2022·S1·6, ·S1·17,
conv2020_X·S1·19 uncovered). m04-l07 cites Ley 29/1975 arts. tercero.uno and diez.uno in a form the resolver cannot
anchor, and states two old ministry names as plain fact (art. 4.1 RDL 4/2000, art. 5.1 RD 577/1997). m04-l09 lacks
jubilación anticipada (arts. 207–208 LGSS) and DT 26.ª LGSS. m04-l06: art. 6 RD 33/1986 (faltas muy graves) and
art. 30.4 LPAC are not cited; art. 61.s LRJSP is not in the Resolución section (open item 9 stands: q255 keys the
Consejo de Ministros with a stem confined to art. 47.1 RD 33/1986). Theory-ledger «Which rule applies» does not record
art. 14.1 RD 365/1995 (three years from birth even for adoption) against art. 89.4 TREBEP, nor art. 17.1 RD 365/1995's
narrower spouse-employer list against art. 89.3 TREBEP.

### Ten IV.5 questions for the reader

Ten kept IV.5 questions drawn with `random.Random(20261022).sample(kept, 10)` over the 195 kept, shown as authored.

**1. `m04-l05-q001`** · disposición final cuarta.1 TREBEP · dificultad 2

> Según la disposición final cuarta.1 del texto refundido de la Ley del Estatuto Básico del Empleado Público, aprobado por el Real Decreto Legislativo 5/2015, de 30 de octubre, lo establecido en el capítulo III de su título V producirá efectos:
>
> a) a partir de la entrada en vigor de las leyes de Función Pública que se dicten en desarrollo del Estatuto. **(clave)**
>
> b) a partir de la entrada en vigor del propio Estatuto, sin necesidad de ningún desarrollo legal o reglamentario posterior.
>
> c) a partir de la aprobación de los reglamentos de provisión de puestos de cada Administración Pública.
>
> d) a partir de la aprobación de las relaciones de puestos de trabajo de cada Departamento ministerial.
>

*Explicación.* La disposición final cuarta.1 TREBEP dice que lo establecido en el capítulo III del título V «producirá efectos a partir de la entrada en vigor de las leyes de Función Pública que se dicten en desarrollo de este Estatuto». No surte efectos con el Estatuto mismo: queda diferido. La disposición no habla de reglamentos de provisión ni de relaciones de puestos de trabajo: lo que exige es una ley de Función Pública.

**2. `m04-l05-q014`** · art. 41.2 RD 364/1995 · dificultad 1

> Según el artículo 41.2 del Real Decreto 364/1995, de 10 de marzo, ¿en qué puestos deben permanecer los funcionarios un mínimo de dos años para poder participar en los concursos de provisión?
>
> a) En cualquier puesto, incluido el desempeñado en comisión de servicios.
>
> b) En el Cuerpo o Escala de pertenencia, con independencia del puesto.
>
> c) Solo en los puestos obtenidos por el sistema de libre designación.
>
> d) En cada puesto de trabajo de destino definitivo. **(clave)**
>

*Explicación.* El artículo 41.2 RD 364/1995 dice que los funcionarios «deberán permanecer en cada puesto de trabajo de destino definitivo un mínimo de dos años». El destino provisional, como la comisión de servicios, no entra en la regla. La permanencia se mide en el puesto, no en el Cuerpo o Escala. Tampoco se limita a los puestos de libre designación: el artículo habla de cada puesto de destino definitivo.

**3. `m04-l05-q046`** · art. 48.2 RD 364/1995 · dificultad 3

> Según el artículo 48.2 del Real Decreto 364/1995, de 10 de marzo, cuando el Subsecretario difiere el cese del funcionario por necesidades del servicio, ¿a quién debe comunicarse?
>
> a) A la Junta de Personal del centro de origen del funcionario.
>
> b) A la Comisión de Valoración que resolvió el concurso.
>
> c) Al titular de la Secretaría de Estado de Función Pública.
>
> d) A la unidad a la que haya sido destinado el funcionario. **(clave)**
>

*Explicación.* El artículo 48.2 RD 364/1995 permite diferir el cese hasta veinte días hábiles, «comunicándose a la unidad a que haya sido destinado el funcionario». Es la unidad de destino la que ha de saber que el funcionario llegará más tarde. El artículo no prevé comunicarlo a la Junta de Personal, a la Comisión de Valoración ni a la Secretaría de Estado de Función Pública.

**4. `m04-l05-q061`** · art. 48.1 RD 364/1995 · dificultad 2

> Una funcionaria cesa el viernes, 23 de octubre de 2026, en su puesto para incorporarse al obtenido por concurso en la misma localidad, y toma posesión el jueves, 29 de octubre. Sin festivos en el periodo, ¿lo hace en plazo?
>
> a) Sí, porque el plazo de tres días hábiles termina el jueves, 29 de octubre de 2026.
>
> b) Sí, porque el plazo es de un mes y termina el lunes, 23 de noviembre de 2026.
>
> c) No, porque el plazo de tres días hábiles terminó el miércoles, 28 de octubre de 2026. **(clave)**
>
> d) No, porque el plazo de tres días naturales terminó el lunes, 26 de octubre de 2026.
>

*Explicación.* Sin cambio de residencia, el artículo 48.1 RD 364/1995 da tres días hábiles, contados «a partir del día siguiente al del cese». Excluidos sábado y domingo, son el lunes 26, el martes 27 y el miércoles 28 de octubre de 2026. El jueves 29 está fuera de plazo. Llegar al jueves supone contar un cuarto día hábil. El mes es para el cambio de residencia o el reingreso. Los días no son naturales sino hábiles.

**5. `m04-l05-q063`** · art. 48.1 RD 364/1995 · dificultad 2

> Una funcionaria en excedencia obtiene por concurso un puesto que comporta su reingreso al servicio activo. La resolución se publica en el BOE el martes, 14 de abril de 2026. ¿Cuál es el último día para tomar posesión?
>
> a) El viernes, 17 de abril de 2026.
>
> b) El miércoles, 29 de abril de 2026.
>
> c) El miércoles, 13 de mayo de 2026.
>
> d) El jueves, 14 de mayo de 2026. **(clave)**
>

*Explicación.* El artículo 48.1 RD 364/1995 da un mes cuando el destino comporta el reingreso al servicio activo, y en ese caso el plazo «deberá computarse desde dicha publicación». Con el artículo 30.4 LPAC, el mes empieza el día siguiente, miércoles 15 de abril, y termina el mismo día de la publicación en el mes de vencimiento: el jueves 14 de mayo de 2026. El viernes 17 de abril aplica tres días hábiles, plazo del destino sin cambio de residencia ni reingreso. El miércoles 29 de abril sale de contar quince días naturales, un plazo que el artículo no da. El miércoles 13 de mayo deja el plazo un día corto.

**6. `m04-l05-q065`** · art. 48.2 RD 364/1995 · dificultad 2

> Según el artículo 48.2 del Real Decreto 364/1995, de 10 de marzo, si el nuevo destino implica cambio de residencia y el interesado lo solicita por razones justificadas, la prórroga de incorporación podrá alcanzar:
>
> a) un máximo de veinte días hábiles. **(clave)**
>
> b) un máximo de veinte días naturales.
>
> c) un máximo de diez días hábiles.
>
> d) un máximo de un mes adicional.
>

*Explicación.* El artículo 48.2 RD 364/1995 permite al Subsecretario del Departamento de nuevo destino conceder «una prórroga de incorporación hasta un máximo de veinte días hábiles». Los días son hábiles, no naturales. El artículo no prevé diez días ni un mes adicional para la incorporación.

**7. `m04-l05-q107`** · art. 15 TREBEP · dificultad 1

> Según el artículo 15 del texto refundido de la Ley del Estatuto Básico del Empleado Público, los empleados públicos tienen derecho al ejercicio de la huelga:
>
> a) Con la garantía del mantenimiento de los servicios esenciales de la comunidad. **(clave)**
>
> b) Solo cuando la convoque la Junta de Personal del centro de trabajo.
>
> c) Con la garantía de los servicios mínimos que fijen los sindicatos convocantes.
>
> d) Previa autorización del órgano competente en materia de personal.
>

*Explicación.* La letra c) del artículo 15 dice «al ejercicio de la huelga, con la garantía del mantenimiento de los servicios esenciales de la comunidad». La garantía no la fijan los sindicatos convocantes. El artículo no exige autorización del órgano de personal ni reserva la convocatoria a la Junta de Personal.

**8. `m04-l05-q127`** · art. 48.f) TREBEP · dificultad 2

> Una funcionaria da a luz el martes 16 de febrero de 2027 y opta por la hora diaria de ausencia por lactancia. ¿Hasta cuándo puede ejercer ese derecho?
>
> a) Mientras el hijo sea menor de seis meses, es decir, hasta agosto de 2027.
>
> b) Mientras el hijo sea menor de nueve meses, es decir, hasta noviembre de 2027.
>
> c) Mientras el hijo sea menor de doce meses, es decir, hasta febrero de 2028. **(clave)**
>
> d) Mientras el hijo sea menor de quince meses, es decir, hasta mayo de 2028.
>

*Explicación.* La letra f) da el permiso «por lactancia de un hijo menor de doce meses». Nacido el martes 16 de febrero de 2027, el hijo cumple doce meses el miércoles 16 de febrero de 2028, así que el derecho dura hasta febrero de 2028. Seis, nueve o quince meses no son la edad que fija el artículo.

**9. `m04-l05-q211`** · art. 54.8 TREBEP · dificultad 1

> De acuerdo con el artículo 54.8 del texto refundido de la Ley del Estatuto Básico del Empleado Público, en cuanto a su formación, los empleados públicos:
>
> a) Realizarán cada año las acciones formativas que fije su Departamento.
>
> b) Seguirán la formación que la Administración les ofrezca en horario de trabajo.
>
> c) Mantendrán actualizada su formación y cualificación. **(clave)**
>
> d) Mantendrán actualizada su formación cuando lo exija el puesto que desempeñen.
>

*Explicación.* El artículo 54.8 dice: «Mantendrán actualizada su formación y cualificación». El deber es permanente y propio del empleado. No depende de que el Departamento fije acciones anuales, de que la formación se ofrezca en horario de trabajo ni de que la exija el puesto.

**10. `m04-l05-q238`** · disposición transitoria sexta RDL 6/2023 · dificultad 1

> De acuerdo con la disposición transitoria sexta del Real Decreto-ley 6/2023, de 19 de diciembre, hasta que se apruebe la normativa reglamentaria, el intervalo de niveles del Subgrupo C1 es:
>
> a) Del nivel 18 al nivel 24.
>
> b) Del nivel 14 al nivel 18.
>
> c) Del nivel 20 al nivel 26.
>
> d) Del nivel 16 al nivel 22. **(clave)**
>

*Explicación.* La disposición transitoria sexta fija para el Grupo C1 el nivel mínimo 16 y el máximo 22. Del 18 al 24 es el Grupo B. Del 14 al 18 es el C2. Del 20 al 26 es el A2.

## Bloque III (sessions 3–4, built 2026-10-22)

**745 questions** in `content/age-administrativo-c1/exercises/` (37 quiz exercises, `m03-lTT-ex-N`), listed in
`course.yaml`. Working files and every verification report in `docs/age-verification/bank/bloque-iii/`; drop log
`bloque-iii/drops.tsv`. III.3 and III.4 were written in three parts each (`.part-<k>.draft.json`, merged with
`tools/merge_parts.py`). Every tema is above its quota and every «Lo que más cae» line is tested.

| Tema | Quota | Authored | Dropped (key / unique / citation / style / official) | Kept | LMC covered |
|---|---|---|---|---|---|
| III.1 | 53 | 61 | 4 (0 / 0 / 0 / 4 / 0) | 57 | 10/10 |
| III.2 | 57 | 76 | 4 (0 / 1 / 0 / 2 / 1) | 72 | 10/10 |
| III.3 | 200 | 260 | 43 (1 / 5 / 0 / 5 / 32) | 217 | 10/10 |
| III.4 | 195 | 253 | 37 (1 / 5 / 0 / 7 / 24) | 216 | 9/9 |
| III.5 | 51 | 62 | 4 (0 / 2 / 0 / 2 / 0) | 58 | 9/9 |
| III.6 | 58 | 72 | 5 (0 / 1 / 0 / 1 / 3) | 67 | 10/10 |
| III.7 | 54 | 64 | 6 (0 / 1 / 0 / 3 / 2) | 58 | 10/10 |
| **Bloque III** | **668** | **848** | **103 (2 / 15 / 0 / 24 / 62)** | **745** | **68/68** |

| Tema | art-compl. / art-preg. / directa / cuál / enunc. / señale / norma | Names article | Negative | Key longest | Diff 1/2/3 | Key a/b/c/d |
|---|---|---|---|---|---|---|
| III.1 | 46 / 18 / 21 / 7 / 5 / 2 / 2 % | 63 % | 0 | 25 % | 18/27/12 | 14/15/14/14 |
| III.2 | 42 / 19 / 18 / 11 / 6 / 3 / 1 % | 61 % | 0 | 26 % | 22/35/15 | 17/18/19/18 |
| III.3 | 31 / 20 / 24 / 13 / 7 / 2 / 3 % | 57 % | 1 | 24 % | 56/119/42 | 53/55/54/55 |
| III.4 | 36 / 19 / 22 / 11 / 6 / 2 / 3 % | 57 % | 2 | 22 % | 57/113/46 | 56/53/55/52 |
| III.5 | 36 / 17 / 26 / 14 / 3 / 2 / 2 % | 53 % | 1 | 22 % | 22/27/9 | 15/15/16/12 |
| III.6 | 39 / 16 / 22 / 7 / 10 / 3 / 1 % | 58 % | 1 | 22 % | 18/35/14 | 16/16/17/18 |
| III.7 | 41 / 12 / 26 / 10 / 7 / 2 / 2 % | 57 % | 0 | 22 % | 22/25/11 | 16/16/13/13 |

Every form is within ±10 points of profile N (III.3 art-completar 31 %, the lowest). Course-wide over bloque III: length
edge z +1.05, longest-is-correct z +0.65; the platform guard over the whole AGE bank passes.

**Drops.** 62 of 103 were check 5 (official): a light rewording of an official question — mostly supuesto computation
cases rebuilt with the official case's shape and new figures, or the official key with one official distractor
reworded. Replacements took another element of the rule or inverted the angle; each was verified like the rest
(`*.replacements.verify-*.md`). One coordinator drop: III.3 q262 (a contencioso count across 24-12 / 6-01, days art. 183
LOPJ as LO 1/2025 words it makes inhábiles, so the keyed date was not safe).

**Official facts no kept question tests** (2022–2025 unless stated; each tried at least twice where an angle existed):
- art. 24.5 LRJSP (conv2022·S2·3, conv2020_X·S2R·2): the article's sentence is the official key, so every question on it
  read as a rewording (q047, q074, q077 dropped). For the user to decide.
- conv2022_X·P1·29 (the sanctioning procedure always starts de oficio) and conv2024_X·S2·9 (a plazo in hours): the
  writer found no angle that does not need the official key or the official natural-hours distractor.
- conv2024_X·S2·6, conv2025_A·S1·10 (the garantía definitiva computation): two computation questions dropped as
  rewordings; the rule (5 % of the price offered, IVA excluded) stays tested by the lmc-3 questions (q091 and others).
- 2020 only: conv2020_X·P1·28 (art. 193.3 LCSP, three tries), conv2020·S2·3.

**Lesson gaps found** (no question asks them): m03-l03 does not state art. 128.2 LJCA (August inhábil in the
contencioso) or the date-to-date month rule there, nor arts. 16.1–16.7 LPAC (registro, covered in II.2), art. 13
LRJSP, art. 30.2 LRJSP, arts. 95.3 párr. 2, 96.5, 106.3 LPAC; `art. 6 LJCA` resolves to no anchor. m03-l04 does not
state art. 29.7 LCSP (services complementing a contrato menor de obras) or art. 98 RGLCAP; Orden HAC/1517/2025
citations resolve to no anchor (threshold questions cite the LCSP articles, which print the 2026 figures). m03-l05:
arts. 47–49, 51, 123 LRJSP, art. 10 LGS, arts. 25.1.b), 89.1 LPAC. m03-l06: art. 68 LPAC; art. 33.1 second sentence
LRJSP. m03-l07 cites art. 20 RD 829/2023 for the Observatorio, which that article does not state. m03-l03 art. 93.2
LRJSP keeps an old ministry name without «(hoy: …)».

**Build and checks.** `build_exercises.py bloque-iii m03` (now skips part drafts). Anchors: every citation resolves.
`citations.es.txt` regenerated (its moved rows are the bloque II prose-gap rows, read: 53 added, 2 replaced, all m02).
Backend `ruff check`, `ruff format --check`, `mypy src` clean; `pytest` 1,495 passed, 20 skipped.

### Ten III.3 questions for the reader

Ten kept III.3 questions drawn with `random.Random(20261022).sample(kept, 10)` over the 217 kept, shown as authored
(the platform shuffles the options per learner). The key is marked **(clave)**.

**1. `m03-l03-q015`** · art. 9.1 LRJSP · dificultad 2

> Según el artículo 9.1 de la Ley 40/2015, de 1 de octubre, de Régimen Jurídico del Sector Público, cuando dos órganos de un mismo Ministerio no están relacionados jerárquicamente, ¿quién aprueba previamente la delegación de competencias entre ellos?
>
> a) El superior común de ambos órganos. **(clave)**
>
> b) El órgano superior del que dependa el órgano delegado.
>
> c) El Subsecretario del Ministerio al que pertenecen.
>
> d) El Consejo de Ministros, a propuesta del Ministro.
>

*Explicación.* Para órganos no relacionados jerárquicamente, el artículo 9.1 LRJSP exige «la aprobación previa del superior común si ambos pertenecen al mismo Ministerio». El órgano superior del que dependa el órgano delegado es la regla para órganos de diferentes Ministerios. El Subsecretario y el Consejo de Ministros no aparecen en esta regla.

**2. `m03-l03-q052`** · art. 30.1 LRJSP · dificultad 3

> De acuerdo con el artículo 30.1 de la Ley 40/2015, de 1 de octubre, de Régimen Jurídico del Sector Público, las infracciones y sanciones prescribirán:
>
> a) en los plazos de ese artículo, que prevalecen siempre sobre los que fijen las leyes sectoriales.
>
> b) según disponga el reglamento que tipifique la infracción, sin que existan plazos supletorios.
>
> c) en el plazo que fije en cada caso la resolución que imponga la sanción correspondiente.
>
> d) según dispongan las leyes que las establezcan y, en su defecto, en los plazos de ese artículo. **(clave)**
>

*Explicación.* El artículo 30.1 LRJSP empieza: «Las infracciones y sanciones prescribirán según lo dispuesto en las leyes que las establezcan. Si éstas no fijan plazos de prescripción», se aplican los del propio artículo. Los plazos de la LRJSP son supletorios, no prevalecen sobre los de la ley sectorial. Remiten a las leyes, no a un reglamento, y sí hay plazos supletorios. La resolución sancionadora no fija el plazo de prescripción.

**3. `m03-l03-q068`** · art. 123.2.b) LRJSP · dificultad 2

> Según el artículo 123.2.b) de la Ley 40/2015, de 1 de octubre, de Régimen Jurídico del Sector Público, ¿qué precisa el convenio de creación de un consorcio en el que participe la Administración General del Estado?
>
> a) La autorización previa del Consejo de Ministros. **(clave)**
>
> b) La autorización previa de las Cortes Generales.
>
> c) La autorización previa del Ministerio de Hacienda.
>
> d) La autorización previa del Presidente del Gobierno.
>

*Explicación.* El artículo 123.2.b) LRJSP dice: «El convenio de creación precisará de autorización previa del Consejo de Ministros». Las Cortes Generales intervienen por otra vía, la ley que autoriza la creación. El Ministerio de Hacienda y el Presidente del Gobierno no son el órgano que autoriza el convenio.

**4. `m03-l03-q070`** · art. 123.2.b) LRJSP · dificultad 3

> Según el artículo 123.2.b) de la Ley 40/2015, de 1 de octubre, de Régimen Jurídico del Sector Público, en el ámbito de los organismos autónomos, la competencia para suscribir el convenio de creación de un consorcio corresponde:
>
> a) al titular del departamento ministerial de adscripción, que podrá delegarla en el organismo.
>
> b) al titular del máximo órgano de dirección del organismo, previo informe del Ministerio de dependencia. **(clave)**
>
> c) al titular del máximo órgano de dirección, previo informe vinculante de la Intervención General.
>
> d) al órgano colegiado de gobierno del organismo, sin necesidad de informe ministerial previo.
>

*Explicación.* El artículo 123.2.b) LRJSP atribuye esa competencia, en los organismos autónomos, «al titular del máximo órgano de dirección del organismo, previo informe del Ministerio del que dependa o al que esté vinculado». No es del Ministro, y en ningún caso puede delegarse. El informe es del Ministerio de dependencia, no de la Intervención General. No suscribe un órgano colegiado sin informe.

**5. `m03-l03-q072`** · art. 5.6 LPAC · dificultad 2

> Según el artículo 5.6 de la Ley 39/2015, de 1 de octubre, del Procedimiento Administrativo Común de las Administraciones Públicas, ¿quién concede el plazo para subsanar la falta de acreditación de la representación, y de cuántos días es como regla?
>
> a) La oficina de registro, que debe conceder diez días al efecto.
>
> b) El órgano administrativo, que debe conceder un mes al efecto.
>
> c) El superior jerárquico del instructor, que debe conceder tres días.
>
> d) El órgano administrativo, que debe conceder diez días al efecto. **(clave)**
>

*Explicación.* El artículo 5.6 LPAC habla del «plazo de diez días que deberá conceder al efecto el órgano administrativo». Lo concede el órgano que tramita, no la oficina de registro ni el superior jerárquico del instructor. El plazo de la regla es de diez días, no de un mes ni de tres días.

**6. `m03-l03-q109`** · art. 30.4 LPAC · dificultad 2

> De acuerdo con el artículo 30.4 de la Ley 39/2015, de 1 de octubre, del Procedimiento Administrativo Común de las Administraciones Públicas, si un plazo en meses vence en un mes sin día equivalente al de inicio del cómputo:
>
> a) Se entenderá que el plazo expira el último día del mes. **(clave)**
>
> b) Se entenderá que el plazo expira el primer día del mes siguiente.
>
> c) Se entenderá que el plazo expira el primer día hábil del mes siguiente.
>
> d) Se contará el plazo por días naturales, a razón de treinta días por mes.
>

*Explicación.* El artículo 30.4 dice que, si en el mes de vencimiento no hay día equivalente, «se entenderá que el plazo expira el último día del mes». El plazo no pasa al mes siguiente, ni a su primer día ni a su primer día hábil. Los meses se cuentan de fecha a fecha, no como treinta días naturales.

**7. `m03-l03-q130`** · art. 21.3 LPAC · dificultad 3

> Una solicitud entra el martes 31 de marzo de 2026 en el registro electrónico del órgano competente para tramitarla. Si su norma reguladora no fija plazo máximo, el último día para notificar la resolución es:
>
> a) El lunes 29 de junio de 2026.
>
> b) El martes 30 de junio de 2026. **(clave)**
>
> c) El miércoles 1 de julio de 2026.
>
> d) El miércoles 30 de septiembre de 2026.
>

*Explicación.* El plazo supletorio es de tres meses, contados desde la entrada en el registro del órgano competente (art. 21.3). Los meses van de fecha a fecha, y junio no tiene día 31: el plazo expira el último día del mes (art. 30.4), el martes 30 de junio de 2026, que es hábil. El lunes 29 de junio termina un día antes. El miércoles 1 de julio pasa al mes siguiente, que la ley no prevé. El miércoles 30 de septiembre aplica seis meses.

**8. `m03-l03-q204`** · art. 106.5 LPAC · dificultad 2

> Conforme al artículo 106.5 de la Ley 39/2015, de 1 de octubre, del Procedimiento Administrativo Común de las Administraciones Públicas, si la revisión de oficio se inició a solicitud de interesado y pasan seis meses sin resolver:
>
> a) Se podrá entender estimada la solicitud por silencio administrativo.
>
> b) Se podrá entender desestimada la solicitud por silencio administrativo. **(clave)**
>
> c) Se producirá la caducidad del procedimiento de revisión de oficio iniciado.
>
> d) El órgano deberá recabar un nuevo dictamen del Consejo de Estado.
>

*Explicación.* El artículo 106.5 distingue según cómo empezó el procedimiento: «Si el procedimiento se hubiera iniciado a solicitud de interesado, se podrá entender la misma desestimada por silencio administrativo». El silencio es negativo, no estimatorio. La caducidad es la consecuencia del procedimiento iniciado de oficio. El precepto no ordena pedir un nuevo dictamen al Consejo de Estado.

**9. `m03-l03-q234`** · art. 122.1 LPAC · dificultad 2

> Una resolución que no pone fin a la vía administrativa se notifica el martes, 3 de febrero de 2026. ¿Cuál es el último día para interponer contra ella recurso de alzada?
>
> a) El martes, 17 de febrero de 2026.
>
> b) El miércoles, 4 de marzo de 2026.
>
> c) El martes, 3 de marzo de 2026. **(clave)**
>
> d) El lunes, 4 de mayo de 2026.
>

*Explicación.* La alzada contra un acto expreso se interpone en un mes (art. 122.1 de la Ley 39/2015). El plazo empieza el día siguiente a la notificación, miércoles 4 de febrero, y concluye el mismo día del mes siguiente en que se notificó: el martes 3 de marzo de 2026, día hábil (art. 30.4). En un plazo por meses los festivos intermedios no cuentan; solo importa que el último día sea hábil. El 17 de febrero resulta de contar diez días hábiles. El 4 de marzo añade un día de más al cómputo. El 4 de mayo corresponde a tres meses: el 3 de mayo es domingo.

**10. `m03-l03-q273`** · art. 19.1.h) LJCA · dificultad 1

> Conforme al artículo 19.1.h) de la Ley 29/1998, de 13 de julio, reguladora de la Jurisdicción Contencioso-administrativa, cualquier ciudadano está legitimado en ejercicio de la acción popular:
>
> a) En todo caso, frente a cualquier acto.
>
> b) Cuando acredite un interés legítimo en el asunto.
>
> c) En los casos expresamente previstos por las Leyes. **(clave)**
>
> d) Solo frente a disposiciones de carácter general.
>

*Explicación.* El artículo 19.1.h) legitima a «cualquier ciudadano, en ejercicio de la acción popular, en los casos expresamente previstos por las Leyes». No es una legitimación general. Quien acredita un interés legítimo ya está legitimado por el artículo 19.1.a), sin acción popular. La acción popular no se limita a las disposiciones generales: depende de lo que prevea cada ley.

## Session 2 (2026-10-18) — summary

Bloque I is closed: **676 questions** in `content/age-administrativo-c1/exercises/` (40 quiz exercises, `m01-lTT-ex-N`),
listed under their lessons in `course.yaml`, loader and cross-reference check green. Stop here; bloque II is next.

- **Platform:** a question may cite a saved source page («fuente: `file`») its lesson cites
  (`citations/course.py`, `_source_anchor`); tests `test_a_question_citing_a_source_file_its_lesson_cites_opens_at_that_citation`
  (failed before the fix) and `…_never_cites_fails_the_load`. `content/README.md` documents it. The answer-bias guards
  (`test_quiz_answer_bias.py`) now run the single-choice checks and the generator deal over age-administrativo-c1 too.
- **Lessons** (blind-checked, `bloque-i/lesson-fixes/`: writer, verify 4/5 PASS, recheck PASS):
  - m01-l01 «Lo que más cae» line 6 is now art. 13.2 CE (asked in conv2020_X P1 1); «Las reformas» gives only date and
    article, as `boe-analisis-ce.xml` does.
  - m01-l02: the «Nombramientos en otros poderes» table cites in parentheses (six citations, no fact changed); the tutela
    sentence limits «español de nacimiento» to the testamentary tutor (art. 60.1 CE); art. 151.2 CE is stated as rules
    4.º and 5.º.
  - Markup: a source citation is read only when its parenthetical starts with «fuente:», so m01-l01, m01-l06 and m01-l11
    now write «(fuente: `file`; label)» (39 citations).
  - No kept question rested on the old wide readings (I.2 q052–q053 test the testamentary tutor; I.1 q010 tests «four
    reforms, one article each»; the I.9 art. 151.2 questions were verified against the CE).
- **Explanations:** the platform shuffles options per learner and the PDF prints the shuffled letters, so 66 kept
  explanations that named options by letter or position were rewritten to name them by content
  (`explanation-refs.json`, blind check `explanation-refs.verify.md`, 66/66 PASS). No other word changed. Verify-spec now
  checks this.
- **New questions** (verified as usual; `additions.verify-1` … `-5`): 36 authored, 7 dropped, 29 kept. I.1 q065 (new
  lmc-6; q013 re-tagged to it); I.2 q065, q067–q071 (the six appointment rows); I.4 q069–q073 (article share 49 → 53 %);
  I.11 q063–q072 (article share 49 → 54 %, and the industria half of lmc-10); I.7 q062–q064 and I.9 q063–q066 (short
  keys, see below). Dropped: I.4 q065–q068 (explanations named options by letter), I.2 q066 (official copy), I.1 q066
  and I.7 q065 (no norm named in the stem, and another norm in force makes a distractor true).
- **Length edge.** Built as it stood, the bank failed the course-wide length-edge guard (z = +3.07: keys about 1.6
  characters longer than distractors on average, I.11 and I.7 the heaviest). Verified options were not rewritten; the
  new questions carry keys shorter than their distractors instead. Final: length edge z = +0.60, longest-is-correct
  z = +0.44, authored position a/b/c/d 170/170/170/166 (z ≤ 0.27). Verifiers noted that in the new questions the key is
  often the shortest option; the aggregate guard is the authority, and each tema's key-shortest share is for the
  bloque II writers to keep in mind.
- **Goldens:** `citations.es.txt` 3,271 → 3,334 prose citations (427 → 466 source files), 1,464 → 1,482 anchors,
  496 → 510 esquema rows, every moved row in m01 (prose-gap citations, the 39 source citations now read, restored
  rows, the six table citations, art. 151.2.4.º/5.º, art. 13.2). `glossary-links.es.txt` 319 → 320 web marks:
  g-estatuto-de-autonomia new in m01-l07 (Ciudades con Estatuto de Autonomía, same sense); g-provincia's first mark moves
  to m01-l02 (art. 151.2 sentence); g-personas-con-discapacidad moves within m01-l01; g-estabilidad-presupuestaria loses
  its m01-l01 mark (the reform topics were removed; its origin m05-l01 still states it). `lesson-refs.es.txt` unchanged.
- **Suites:** backend `ruff check`, `ruff format --check`, `mypy src` (strict) clean; `pytest` 1,495 passed, 20 skipped
  (+6: two citation tests, four AGE bias cases). Frontend `npm run build` clean; `vitest` 593 passed, 51 skipped.
- **Unchanged:** crypto-futures content and goldens; Android bundle re-exported to scratch, byte-identical to
  `dist/bundle`, label catalogs identical to `dist/i18n`; `verify_golden_stability.py` exit 0, digest `f0ae701b…bcaea`.

## Session 1 (2026-10-18) — summary and where to resume

- Plan written: `docs/age-bank-plan.md` (quotas, target mixes, repository shape, verification).
- Bloque I prose gaps closed (theory ledger «Esquemas bloque I», open item 1) and blocked esquema rows restored; see
  «Bloque I prose gaps» below.
- Official questions split by tema into `docs/age-verification/bank/official/<tema>.md` (generated from the
  questionnaires and the exams ledger's tema column; cover pages excluded).
- **Bloque I authored and verified:** 690 questions written by 11 writers, every one checked blind in two batches
  (plus a check of each replacement): 43 dropped (key 0, unique 7, citation 3, style 23, official 10), **647 kept**
  against a quota of 605. Every tema is at or above its quota; every «Lo que más cae» line is tested except I.1 lmc-6
  (open item 8).
- **Paused by the user:** code changes, test runs and golden regeneration (another task is changing the test suite).
  Pending until released: answer-bias guards over AGE, the YAML build into `content/age-administrativo-c1/exercises/`
  and `course.yaml`, loader, cross-reference check, `citations.es.txt` and the other goldens (they also move for the
  prose-gap citations, e.g. the new art. 76 LOTC anchor).

**Resume (session 2):** done (see «Session 2» above).

**Resume (session 3): bloque II.** Read this ledger, `docs/age-bank-plan.md` and the theory ledger «Esquemas bloque II»
open item 1 (prose gaps). Before authoring: close those gaps blind-checked, restore the rows they block, and rewrite
the 13 bare `sources/otros/` citations in m02-l02 / m02-l03 to «(fuente: `file`; label)». Copy `bloque-i/spec.md` and
`verify-spec.md` to `bloque-ii/` with these lessons learned: explanations name options by content, never by letter;
a stem that names no norm is checked against every norm in force; keep the key-longest share near a quarter and the key
not systematically shorter either (watch `bank_stats.py` and the course-wide length-edge guard after each build).
Build with `uv run python ../docs/age-verification/bank/tools/build_exercises.py bloque-ii m02` from `backend/`.

## Bloque I prose gaps

Writer record `docs/age-verification/bank/bloque-i/prose-gaps/writer.md`; blind check `verify.md` (39 items, 37 PASS,
2 FAIL: two m01-l11 esquema rows, art. 235.1 TFUE condition cut and art. 238.3 TFUE blocking minority placed after the
72 % case); the reviewer's replacements applied and re-checked by a new reviewer, `recheck.md` (6 items, 6 PASS).

- Sentences added or completed: m01-l01 (arts. 76, 33.2, 35.2 LOTC; art. 7.2 LO 3/1981), m01-l03 (art. 93.1 RS; arts.
  41.1, 46.2 RC), m01-l04 (arts. 595.1, 630.1 LOPJ, the CNI Magistrate), m01-l07 (art. 19.3, DA 4.ª.3 Ley 19/2013),
  m01-l09 (medio ambiente and ferrocarriles pairs), m01-l11 (arts. 235.1, 238.2, 238.3 TFUE).
- Rows restored: 14 (m01-l01 4, m01-l03 1, m01-l04 3, m01-l09 2, m01-l11 4 including the split 235.1 row), plus the
  m01-l07 19.3 cell and the 16.4 TUE label. Not restored: a 41.1 RC row (a Mesa's composition, not a majority).
- Tests and goldens not run (pause above).

## Per tema

| Tema | Quota | Authored | Dropped (key / unique / citation / style / official) | Kept | LMC covered | Verification files |
|---|---|---|---|---|---|---|
| I.1 | 57 | 66 | 7 (0 / 1 / 3 / 1 / 2) | 59 | 10/10 | `m01-l01.verify-1.md`, `-2`, `additions.verify-2.md` |
| I.2 | 55 | 71 | 7 (0 / 2 / 0 / 4 / 1) | 64 | 10/10 | `m01-l02.verify-1.md`, `-2`, `-3`, `additions.verify-2.md`, `-5` |
| I.3 | 56 | 64 | 4 (0 / 2 / 0 / 1 / 1) | 60 | 10/10 | `m01-l03.verify-1.md`, `-2`, `replacements.verify-1.md` |
| I.4 | 54 | 73 | 9 (0 / 0 / 0 / 6 / 3) | 64 | 10/10 | `m01-l04.verify-1.md`, `-2`, `-3`, `additions.verify-1.md`, `-2`, `-4` |
| I.5 | 54 | 61 | 4 (0 / 1 / 0 / 3 / 0) | 57 | 10/10 | `m01-l05.verify-1.md`, `-2` |
| I.6 | 54 | 61 | 0 | 61 | 9/9 | `m01-l06.verify-1.md`, `-2` |
| I.7 | 54 | 65 | 5 (0 / 1 / 0 / 4 / 0) | 60 | 10/10 | `m01-l07.verify-1.md`, `-2`, `additions.verify-3.md` |
| I.8 | 58 | 66 | 2 (0 / 0 / 0 / 2 / 0) | 64 | 10/10 | `m01-l08.verify-1.md`, `-2`, `replacements.verify-1.md` |
| I.9 | 54 | 66 | 4 (0 / 1 / 0 / 2 / 1) | 62 | 10/10 | `m01-l09.verify-1.md`, `-2`, `replacements.verify-1.md`, `additions.verify-3.md` |
| I.10 | 54 | 61 | 3 (0 / 1 / 0 / 1 / 1) | 58 | 10/10 | `m01-l10.verify-1.md`, `-2` |
| I.11 | 55 | 72 | 5 (0 / 0 / 0 / 3 / 2) | 67 | 10/10 | `m01-l11.verify-1.md`, `-2`, `additions.verify-1.md`, `-3` |
| **Bloque I** | **605** | **726** | **50 (0 / 9 / 3 / 27 / 11)** | **676** | **108/108** | |

Drop log with reasons: `docs/age-verification/bank/bloque-i/drops.tsv`. Working tools in `docs/age-verification/bank/tools/`:
`official_by_tema.py` (needs the questionnaires as `pdftotext -layout` text), `bank_stats.py` (kept-set mix per tema),
`check_anchors.py` (resolves every draft citation with the platform's resolver; run with `uv run` from `backend/`).

### Mix of kept questions

| Tema | art-compl. / art-preg. / directa / cuál / enunc. / señale / norma | Names article | Negative | Key longest | Diff 1/2/3 | Key a/b/c/d (authored) |
|---|---|---|---|---|---|---|
| I.1 | 42 / 15 / 20 / 10 / 7 / 3 / 2 % | 58 % | 1 | 25 % | 18/28/13 | 15/15/14/15 |
| I.2 | 42 / 12 / 23 / 16 / 5 / 2 / 0 % | 55 % | 1 | 22 % | 19/33/12 | 16/16/18/14 |
| I.3 | 38 / 15 / 23 / 13 / 5 / 3 / 2 % | 53 % | 0 | 25 % | 19/28/13 | 14/15/16/15 |
| I.4 | 31 / 22 / 20 / 16 / 6 / 3 / 2 % | 53 % | 0 | 20 % | 18/33/13 | 16/16/16/16 |
| I.5 | 37 / 14 / 21 / 16 / 7 / 4 / 2 % | 51 % | 0 | 21 % | 18/28/11 | 14/14/14/15 |
| I.6 (profile G) | 21 / 5 / 38 / 21 / 7 / 3 / 5 % | 26 % | 0 | 26 % | 20/29/12 | 16/15/15/15 |
| I.7 | 38 / 13 / 22 / 17 / 7 / 2 / 2 % | 52 % | 1 | 27 % | 17/32/11 | 14/16/15/15 |
| I.8 | 39 / 16 / 22 / 14 / 5 / 3 / 2 % | 55 % | 1 | 22 % | 20/31/13 | 17/16/16/15 |
| I.9 | 37 / 16 / 21 / 16 / 5 / 3 / 2 % | 53 % | 0 | 23 % | 19/29/14 | 16/15/15/16 |
| I.10 | 36 / 16 / 22 / 14 / 7 / 3 / 2 % | 52 % | 0 | 26 % | 18/28/12 | 15/16/12/15 |
| I.11 | 36 / 18 / 24 / 10 / 7 / 3 / 1 % | 54 % | 0 | 22 % | 19/36/12 | 17/16/19/15 |

Every form is within ±10 points of its profile (N, or G for I.6). The article share is 51–58 % in profile-N temas. Key-longest is counted by characters, as the platform guard counts it. Difficulty 1 runs 17–20 per tema (about 30 %). Authored key positions are kept as written (balanced per tema; 170/170/170/166 over the bloque); the platform shuffles per learner.

### Coverage of official questions

Each writer mapped every official question filed under its tema (`official/I.TT.md`) to kept questions in its
`writer-notes.md`. Official facts no lesson states (so no question is possible) are in open item 3; the rest are covered
from a new angle. Ten drafts were dropped as light rewordings of an official question; each lost fact got a replacement
from another angle where it carried a «Lo que más cae» line (I.3 q064, I.4 q062–q064, I.9 q062).

### Rulings recorded in `verify-spec.md`

Short organ or quantity options of the kind the style guide's § 3 shows do not fail checklist 10 on length; «lightly
reworded» includes same fact and angle with the official key and an official distractor carried over; a descriptive
norm name counts as the «no norm named» form. The two I.11 short-option drops (q053, q059) predate the first ruling and
stand.

## Open items

1. **Closed (session 2).** ~~m01-l02 table without parenthesised citations.~~ Six citations in parentheses; six appointment questions kept. «Nombramientos en otros poderes» cites arts. 122.3, 123.2,
   124.4, 152.1, 159.1 and 160 CE in bare cells; the resolver does not read them, so no question can test those six
   appointments. A prose fix (parenthesised citations) unblocks them.
2. **Closed (session 2).** ~~m01-l02 sentences wider than the norm~~ — rewritten and blind-checked. (verifier notes, `m01-l02.verify-2.md`): the tutela sentence asks
   «español de nacimiento» of every tutor (art. 60.1 CE asks it of the testamentary tutor); the art. 151.2 sentence
   gives sanción after ratification, true only under rule 4.º (rule 5.º puts a provincial referendum first). One-sentence
   R2 fixes with their own blind check.
3. **Official facts the lessons do not state** (no question possible): I.1 — arts. 107, 103.1, 103.3, 117.1 CE; I.3 —
   art. 134.3 CE (conv2024_A P1 35), art. 82.3 CE (an option of conv2022_X P1 8); I.4 — art. 120.2 CE (conv2020 P1 3);
   I.5 — art. 94.1 CE, art. 26 Ley 50/1997, art. 124 CE, art. 86 CE; I.7 — art. 29.2.d Ley 19/2013 (sigilo, conv2020
   P1 5); I.8 — arts. 20.1, 89, 93 LRJSP, arts. 8, 9 Ley 50/1997 (filed under other temas first); I.10 — arts. 133, 147,
   152, 153 CE (conv2020_X P1 11). Writer notes list each. For the scope audit to weigh.
4. **Reading of checklist item 2:** I.10 stems that say «la legislación básica estatal de régimen local» without the
   BOE title were passed as the «no norm named» form (style guide § 2). Kept as the round's reading.
5. **`covers` code for reserve questions:** `official:<code>·P1R·<n>` (writers' convention, now standard).
6. **Closed (session 2).** ~~Platform: question citations to source files.~~ `CourseCitations._anchor` resolves only norm segments, so a question
   citing «fuente: `file`» fails the load even when its lesson cites the file (48 in I.6, 4 in I.11, 1 in I.1; bloque VI
   will need it throughout). Fix when code is released: resolve a `files` segment to `fuente-<file>` when the lesson's
   prose cites it, plus a test that fails before.
7. **Lesson citation forms fixed this session (markup only, no fact changed):** m01-l01, m01-l06, m01-l11 cited saved
   pages as bare `sources/otros/<file>` inside the parenthesis, which the grammar does not read; now «fuente: `<file>`»
   as in the m06 lessons (38 citations). m01-l09 «(disp. trans. 2.ª / 5.ª CE)» → «(disposición transitoria segunda /
   quinta CE)», and I.9 q019 and q022 normalised to the same form. m02-l02 and m02-l03 still carry 13 bare paths
   (bloque II round). Goldens not regenerated (pause).
8. **Closed (session 2):** line replaced by art. 13.2 CE. ~~I.1 lmc-6 («La Constitución tiene un título preliminar y diez títulos (CE)»)** has no citable unit: «(CE)» is not a
   citation and no article states it. Its two questions (q002, q003) were dropped at the resolver. Needs a lesson
   decision: a different «Lo que más cae» fact, or a citable unit for the structure.
9. **RD 33/1986 art. 47.1 vs art. 61.s LRJSP** (separación del servicio: Consejo de Ministros vs Ministro). The
   consolidated RD 33/1986 file (1991) predates the LRJSP; I.8 asks it only as a distractor wrong under both. Matters
   for IV.6.
10. **Closed (session 2).** ~~I.1 «Las reformas» paragraph~~ — now date and article only. cites `boe-analisis-ce.xml` for what each reform was about; the page gives only
    article and date (verifier note, `m01-l01.verify-1.md`). Wider than the source; R2 fix.
12. **Smaller lesson notes from verifiers** (no verdict changed): m01-l07 art. 2.1 qualifier read as covering the whole
    list, mutuas left out; art. 15.2 condition left out; m01-l08 art. 69.2 «sin perjuicio…» left out; m01-l11 opening
    sentence says 2016 DOUE versions while «Normativa» says 15-03-2025; m01-l01 «Antes de plantearla» (art. 35.2 LOTC
    says «Antes de adoptar mediante auto su decisión definitiva»); m01-l10 art. 21.1 «salvo los supuestos…» left out.
11. **m01-l07 l. 72** names «Ministerio de la Presidencia» (art. 10.1 Ley 19/2013) without «(hoy: …)» (convention 1).

## Ten I.5 questions for the reader

Ten kept I.5 questions drawn with `random.Random(20261018).sample(kept, 10)` over the 57 kept, shown as authored (the
platform shuffles the options per learner). The key is marked **(clave)**.

**1. `m01-l05-q005`** · art. 107 CE · dificultad 1

> Según la Constitución Española de 1978, ¿qué órgano es el supremo órgano consultivo del Gobierno?
>
> a) El Consejo Económico y Social, cuya composición regula una ley ordinaria.
>
> b) La Comisión General de Secretarios de Estado y Subsecretarios, que preside un Vicepresidente.
>
> c) El Secretariado del Gobierno, como órgano de apoyo del Consejo de Ministros.
>
> d) El Consejo de Estado, cuya composición y competencia regula una ley orgánica. **(clave)**

*Explicación.* El artículo 107 dice: «El Consejo de Estado es el supremo órgano consultivo del Gobierno. Una ley orgánica regulará su composición y competencia». El Consejo Económico y Social es un órgano consultivo en materia socioeconómica, no el supremo órgano consultivo del Gobierno. La Comisión General de Secretarios de Estado y Subsecretarios es un órgano de colaboración del Gobierno y el Secretariado del Gobierno es un órgano de apoyo (arts. 8 y 9 Ley 50/1997); ninguno es consultivo.

**2. `m01-l05-q008`** · art. 2.2 Ley 50/1997 · dificultad 3

> De acuerdo con el artículo 2.2 de la Ley 50/1997, de 27 de noviembre, del Gobierno, corresponde al Presidente del Gobierno crear, modificar y suprimir, por Real Decreto:
>
> a) Los órganos directivos de los Departamentos Ministeriales.
>
> b) Los Departamentos Ministeriales y las Subsecretarías de cada uno de ellos.
>
> c) Los Departamentos Ministeriales, así como las Secretarías de Estado. **(clave)**
>
> d) Las Comisiones Delegadas del Gobierno y sus respectivas Secretarías.

*Explicación.* El artículo 2.2.j) atribuye al Presidente crear, modificar y suprimir, por Real Decreto, «los Departamentos Ministeriales, así como las Secretarías de Estado». Los órganos directivos de los Departamentos los crea el Consejo de Ministros (art. 5.1.i). Las Subsecretarías no figuran en esta letra. Las Comisiones Delegadas las crea el Consejo de Ministros mediante Real Decreto, a propuesta del Presidente (art. 6.1).

**3. `m01-l05-q013`** · art. 18.1 Ley 50/1997 · dificultad 1

> De acuerdo con el artículo 18.1 de la Ley 50/1997, de 27 de noviembre, del Gobierno, en las reuniones del Consejo de Ministros:
>
> a) El Presidente del Gobierno las convoca y preside, y actúa como Secretario el Director del Secretariado del Gobierno.
>
> b) El Presidente del Gobierno las convoca y preside, y actúa como Secretario el Ministro de la Presidencia. **(clave)**
>
> c) El Presidente del Gobierno las convoca y preside, y actúa como Secretario el Subsecretario de la Presidencia.
>
> d) El Vicepresidente primero las convoca y preside, y actúa como Secretario el Ministro de la Presidencia.

*Explicación.* El artículo 18.1 dice: «El Presidente del Gobierno convoca y preside las reuniones del Consejo de Ministros, actuando como Secretario el Ministro de la Presidencia». El Director del Secretariado del Gobierno suple al Secretario de la Comisión General de Secretarios de Estado y Subsecretarios (art. 8.3). El Subsecretario de la Presidencia es el Secretario de esa Comisión, no del Consejo. El Consejo lo convoca y preside el Presidente, no un Vicepresidente.

**4. `m01-l05-q023`** · art. 8.2 Ley 50/1997 · dificultad 2

> De acuerdo con el artículo 8.2 de la Ley 50/1997, de 27 de noviembre, del Gobierno, la Presidencia de la Comisión General de Secretarios de Estado y Subsecretarios corresponde:
>
> a) Al Presidente del Gobierno o, en su defecto, a un Vicepresidente del Gobierno.
>
> b) A un Vicepresidente del Gobierno o, en su defecto, al Ministro de la Presidencia. **(clave)**
>
> c) Al Ministro de la Presidencia o, en su defecto, al Subsecretario de la Presidencia.
>
> d) Al Subsecretario de la Presidencia o, en su defecto, al Director del Secretariado del Gobierno.

*Explicación.* El artículo 8.2 dice que la Presidencia «corresponde a un Vicepresidente del Gobierno o, en su defecto, al Ministro de la Presidencia». El Presidente del Gobierno no preside esta Comisión. El Subsecretario de la Presidencia ejerce la Secretaría, no la Presidencia, y el Director del Secretariado del Gobierno lo suple como Secretario (art. 8.3).

**5. `m01-l05-q032`** · art. 99.3 CE · dificultad 1

> Según el artículo 99.3 de la Constitución Española de 1978, ¿qué mayoría necesita el candidato a la Presidencia del Gobierno en la primera votación de investidura?
>
> a) La mayoría simple de los miembros del Congreso de los Diputados.
>
> b) La mayoría absoluta de los miembros del Congreso de los Diputados. **(clave)**
>
> c) La mayoría de tres quintos de los miembros del Congreso de los Diputados.
>
> d) La mayoría absoluta de los miembros de cada una de las Cámaras.

*Explicación.* El artículo 99.3 dice que el Rey nombrará Presidente al candidato si el Congreso, «por el voto de la mayoría absoluta de sus miembros», le otorga su confianza. La mayoría simple basta solo en la segunda votación, cuarenta y ocho horas después. Los tres quintos no se exigen en la investidura. El Senado no vota la investidura.

**6. `m01-l05-q035`** · art. 100 CE · dificultad 2

> ¿Cuál de las siguientes afirmaciones sobre el nombramiento de los miembros del Gobierno se ajusta a la Constitución Española de 1978?
>
> a) Los Ministros son nombrados por el Rey, a propuesta del Presidente, y separados por el Congreso de los Diputados.
>
> b) Los Vicepresidentes son nombrados por el Rey, previa votación de investidura en el Congreso de los Diputados.
>
> c) Los demás miembros del Gobierno son nombrados y separados por el Rey, a propuesta de su Presidente. **(clave)**
>
> d) Los Ministros son nombrados por el Presidente del Gobierno, previa deliberación del Consejo de Ministros.

*Explicación.* El artículo 100 dice: «Los demás miembros del Gobierno serán nombrados y separados por el Rey, a propuesta de su Presidente». El Congreso no separa a los Ministros; exige la responsabilidad política del Gobierno en su conjunto (art. 113.1). Solo el candidato a Presidente se somete a investidura (art. 99). Los Ministros los nombra el Rey, no el Presidente, y la ley no exige deliberación del Consejo.

**7. `m01-l05-q037`** · art. 101.2 CE · dificultad 2

> Tras la celebración de elecciones generales el Gobierno cesa, pero el Gobierno cesante continuará en funciones:
>
> a) Hasta la votación de investidura del nuevo Presidente en el Congreso.
>
> b) Hasta la constitución de las nuevas Cortes Generales tras las elecciones.
>
> c) Hasta la toma de posesión del nuevo Gobierno. **(clave)**
>
> d) Durante un plazo máximo de dos meses desde las elecciones.

*Explicación.* El artículo 101.2 dice que el Gobierno cesante «continuará en funciones hasta la toma de posesión del nuevo Gobierno». La investidura y la constitución de las Cortes son pasos anteriores, y no ponen fin a las funciones. La Constitución no fija un plazo máximo de dos meses; los dos meses del artículo 99.5 se cuentan desde la primera votación de investidura.

**8. `m01-l05-q053`** · art. 113.4 CE · dificultad 3

> Según el artículo 113.4 de la Constitución Española de 1978, ¿qué consecuencia tiene para sus signatarios que la moción de censura no sea aprobada por el Congreso?
>
> a) No podrán presentar otra durante el resto de la legislatura.
>
> b) No podrán presentar otra durante el mismo período de sesiones. **(clave)**
>
> c) No podrán presentar otra hasta que transcurra un año desde la votación.
>
> d) No podrán presentar otra hasta que transcurran dos meses desde la votación.

*Explicación.* El artículo 113.4 dice que, si la moción no fuere aprobada, «sus signatarios no podrán presentar otra durante el mismo período de sesiones». La limitación no dura toda la legislatura. El año es el plazo entre disoluciones (art. 115.3) y los dos meses son los de la investidura (art. 99.5).

**9. `m01-l05-q055`** · art. 115.2 CE · dificultad 2

> La propuesta de disolución del Congreso, del Senado o de las Cortes Generales queda vedada al Presidente del Gobierno cuando:
>
> a) Esté en trámite una cuestión de confianza ante el Congreso.
>
> b) Esté en trámite el Proyecto de Ley de Presupuestos Generales del Estado.
>
> c) Falten menos de seis meses para el término de la legislatura.
>
> d) Esté en trámite una moción de censura. **(clave)**

*Explicación.* El artículo 115.2 dice: «La propuesta de disolución no podrá presentarse cuando esté en trámite una moción de censura». La Constitución no impide la disolución durante una cuestión de confianza ni durante la tramitación de los Presupuestos. Tampoco fija un límite por la proximidad del fin de la legislatura.

**10. `m01-l05-q059`** · art. 116.3 CE · dificultad 2

> ¿Cuál de las siguientes afirmaciones sobre la declaración de los estados de alarma, de excepción y de sitio es correcta según la Constitución Española de 1978?
>
> a) El estado de alarma lo declara el Gobierno mediante decreto acordado en Consejo de Ministros, previa autorización del Congreso.
>
> b) El estado de excepción lo declara el Gobierno mediante decreto acordado en Consejo de Ministros, previa autorización del Congreso. **(clave)**
>
> c) El estado de sitio lo declara el Gobierno mediante decreto acordado en Consejo de Ministros, dando cuenta al Congreso.
>
> d) El estado de excepción lo declara el Congreso por mayoría absoluta, a propuesta exclusiva del Gobierno.

*Explicación.* El artículo 116.3 dice que el estado de excepción «será declarado por el Gobierno mediante decreto acordado en Consejo de Ministros, previa autorización del Congreso de los Diputados». El estado de alarma no exige autorización previa: el Gobierno lo declara dando cuenta al Congreso (art. 116.2). El estado de sitio lo declara la mayoría absoluta del Congreso, a propuesta exclusiva del Gobierno (art. 116.4), y esa no es la regla del estado de excepción.


# Session 6 progress (append-only)

One line per finished part: date-time, agent, file, result.

- 2026-10-24 08:58 · verifier-1 · lesson-fixes/recheck-s6.md · 3 checked, PASS 3, FAIL 0
- 2026-10-24 09:00 · verifier-2 · bloque-vi/m06-l02.part-1.draft.json · checked 60, PASS 60, FAIL 0 (key 0, unique 0, citation 0, style 0, official 0)
- 2026-10-24 09:02 · verifier-1 · bloque-v/m05-l03.s5.verify-1.md · 21 checked, PASS 21, FAIL 0
- 2026-10-24 09:02 · verifier-2 · bloque-vi/m06-l04.part-1.draft.json · checked 63, PASS 63, FAIL 0 (key 0, unique 0, citation 0, style 0, official 0)
- 2026-10-24 09:04 · verifier-1 · bloque-v/m05-l02.s5b.verify-1.md + m05-l03.s5b.verify-1.md · 8 checked, PASS 8, FAIL 0
- 2026-10-24 09:04 · verifier-2 · bloque-vi/m06-l06.part-1.draft.json · checked 59, PASS 59, FAIL 0 (key 0, unique 0, citation 0, style 0, official 0)
- 2026-10-24 09:06 · writer-A · bloque-v/m05-l02.s5.draft.json · 33 written (24 replacements, 9 table facts), 0 anchor misses, stats z +1.19/-0.12
- 2026-10-24 09:06 · writer-B · bloque-vi/m06-l01.part-1 · 69 kept (63 inherited re-checked + 6 new, 9 inherited removed), lint 16 flags (short label/quantity options only), stats z +0.97/+1.01, 0 anchor misses
- 2026-10-24 09:06 · verifier-2 · bloque-vi/m06-l03.part-1.draft.json · checked 70, PASS 70, FAIL 0 (key 0, unique 0, citation 0, style 0, official 0)
- 2026-10-24 09:10 · writer-B · bloque-vi/m06-l01.part-2 · 69 kept (57 inherited re-checked + 12 new, 12 inherited removed), lint 13 flags (short label/quantity options only), stats z +0.62/+0.60, 0 anchor misses; blocker: ENI pdf not in lesson Fuentes (item uncovered)
- 2026-10-24 09:12 · recheck-opus · bloque-vi part-1 sample (32) · PASS 30, FAIL 2 (unique 2: m06-l04-q056, m06-l03-q023)
- 2026-10-24 09:14 · coordinator · bloque-vi part-1 ×4 · sample missed 2/32 on check 2; both dropped; full strict second pass ordered on the other 220
- 2026-10-24 09:16 · coordinator · bloque-vi/verify-spec.md · ruling added: check 2 names the sentence that makes each distractor wrong, grep all saved pages
- 2026-10-24 09:15 · coordinator · session resumed under CLAUDE.md «Subagent models and concurrency» (no .claude/agents files exist); writer-A (sonnet): s5b m03-l04/l05/l06 then m04; writer-B (sonnet): finish m06-l02 p2, m06-l03 p2, m06-l05 p1, m06-l07 p1; verifier-1 (opus): strict verify-2 of VI part-1 ×4 (220, sample excluded); verifier-2 (opus): m05-l02 s5 + m03-l03 s5b, then m06-l01 p1, p2
- 2026-10-24 09:18 · writer-A · bloque-iii/m03-l04.s5b.draft.json · 2 written, anchor misses 0, stats z +0.10/-0.58
- 2026-10-24 09:19 · verifier-1 · m06-l02.part-1.draft.json verify-2 · checked 52, PASS 51, FAIL 1 (key 0, unique 1, citation 0, style 0, official 0)
- 2026-10-24 09:20 · writer-B · bloque-vi/m06-l02.part-2.draft.json · 61 kept (61 inherited re-checked + 0 new, 0 removed; 9 edited), lint clean (short-option flags only), stats z +1.39/+0.79, anchor misses 0
- 2026-10-24 09:20 · writer-A · bloque-iii/m03-l05.s5b.draft.json · 4 written, anchor misses 0, stats z +0.21/+0.00
- 2026-10-24 09:21 · writer-A · bloque-iii/m03-l06.s5b.draft.json · 2 written, anchor misses 0, stats z +0.99/+0.82
- 2026-10-24 09:21 · verifier-2 · bloque-v/m05-l02.s5.draft.json + bloque-iii/m03-l03.s5b.draft.json · checked 48, PASS 46, FAIL 2 (key 0, unique 0, citation 1, style 1, official 0)
- 2026-10-24 09:22 · verifier-1 · m06-l03.part-1.draft.json verify-2 · checked 62, PASS 61, FAIL 1 (key 0, unique 1, citation 0, style 0, official 0)
- 2026-10-24 09:23 · writer-A · bloque-iv/m04-l04.s5b.draft.json · 4 written, anchor misses 0, stats z +0.71/+0.00
- 2026-10-24 09:25 · verifier-2 · bloque-vi/m06-l01.part-1.draft.json · checked 69, PASS 67, FAIL 2 (key 0, unique 1, citation 0, style 1, official 0)
- 2026-10-24 09:25 · writer-B · bloque-vi/m06-l03.part-2.draft.json · 64 kept (59 inherited re-checked + 5 new, 4 removed), lint clean (short-option flags only), stats z +1.28/-0.40, anchor misses 0
- 2026-10-24 09:26 · verifier-1 · m06-l04.part-1.draft.json verify-2 · checked 55, PASS 51, FAIL 4 (key 0, unique 4, citation 0, style 0, official 0)
- 2026-10-24 09:27 · writer-A · bloque-iv/m04-l06.s5b.draft.json · 11 written, anchor misses 0, stats z +0.32/+0.37
- 2026-10-24 09:28 · writer-B · bloque-vi/m06-l05.part-1.draft.json · 61 kept (61 inherited re-checked + 0 new, 0 removed; 8 edited), lint clean (short-option flags only), stats z +0.32/-0.40, anchor misses 0
- 2026-10-24 09:29 · writer-A · bloque-iv/m04-l07.s5b.draft.json · 4 written, anchor misses 0, stats z +0.61/+0.00
- 2026-10-24 09:29 · verifier-2 · bloque-vi/m06-l01.part-2.draft.json · checked 69, PASS 68, FAIL 1 (key 0, unique 1, citation 0, style 0, official 0)
- 2026-10-24 09:29 · verifier-1 · m06-l06.part-1.draft.json verify-2 · checked 51, PASS 48, FAIL 3 (key 0, unique 2, citation 0, style 1, official 0)
- 2026-10-24 09:30 · coordinator · strict verify-2 of VI part-1 ×4: 219 checked, 9 FAIL (4.1 %, all but one unique); label clash noted: ms-access-tipos-datos-escritorio.html «Texto breve» vs lesson/specs «Texto corto» (not in the label table). Ruling added to bloque-vi/spec.md: a retired product's page may back a general concept (ms-mineria-datos.html). Open: VI.1 p2 item resting on boe-rd-4-2010-eni.pdf uncovered (file not cited in m06-l01 prose). Launched verifier-1b (VI.2 p2, VI.3 p2, s5b II–V) and verifier-2b (VI.5 p1, VI.7 p1).
- 2026-10-24 09:31 · writer-A · bloque-iv/m04-l09.s5b.draft.json · 9 written, anchor misses 0, stats z +1.00/-0.82
- 2026-10-24 09:31 · writer-B · bloque-vi/m06-l07.part-1.draft.json · 74 kept (73 inherited re-checked + 1 new, 1 removed), lint clean (short-option flags only), stats z +0.76/+0.14, anchor misses 0
- 2026-10-24 09:33 · writer-A · bloque-v/m05-l02.s5c.draft.json · 2 written (q326 for q285, q327 for q307), anchor misses 0, lint clean, stats z +0.50/-0.82
- 2026-10-24 09:34 · verifier-2 · bloque-vi/m06-l05.part-1.draft.json · checked 61, PASS 59, FAIL 2 (key 0, unique 0, citation 0, style 2, official 0)
- 2026-10-24 09:34 · writer-A · lesson-fixes/s6 (m04-l06 art. 23 RD 33/1986 sentence added; m06-l01 ENI citation form fixed, now resolves) · tests esquema 10 passed, citations 60 passed
- 2026-10-24 09:36 · verifier-1 · bloque-vi/m06-l02.part-2.draft.json · checked 61, PASS 58, FAIL 3 (key 0, unique 1, citation 0, style 2, official 0)
- 2026-10-24 09:38 · verifier-2 · bloque-vi/m06-l07.part-1.draft.json · checked 74, PASS 72, FAIL 2 (key 0, unique 0, citation 0, style 2, official 0)
- 2026-10-24 09:38 · verifier-2 · bloque-vi/m06-l05.part-1.draft.json · correction: q020 PASS (explanation names the option by content); now checked 61, PASS 60, FAIL 1 (style 1); its drops.tsv line needs removing
- 2026-10-24 09:39 · coordinator · bloque-vi/drops.tsv · removed the m06-l05-q020 row the verifier reversed to PASS in its report
- 2026-10-24 09:39 · verifier-1 · bloque-vi/m06-l03.part-2.draft.json · checked 64, PASS 61, FAIL 3 (key 0, unique 0, citation 0, style 3, official 0)
- 2026-10-24 09:46 · verifier-1 · bloque-iii/m03-l04.s5b.draft.json · checked 2, PASS 2, FAIL 0 (key 0, unique 0, citation 0, style 0, official 0)
- 2026-10-24 09:46 · verifier-1 · bloque-iii/m03-l05.s5b.draft.json · checked 4, PASS 3, FAIL 1 (key 0, unique 0, citation 0, style 0, official 1)
- 2026-10-24 09:46 · verifier-1 · bloque-iii/m03-l06.s5b.draft.json · checked 2, PASS 0, FAIL 2 (key 0, unique 0, citation 0, style 0, official 2)
- 2026-10-24 09:46 · verifier-1 · bloque-iv/m04-l04.s5b.draft.json · checked 4, PASS 4, FAIL 0 (key 0, unique 0, citation 0, style 0, official 0)
- 2026-10-24 09:46 · verifier-1 · bloque-iv/m04-l06.s5b.draft.json · checked 11, PASS 10, FAIL 1 (key 0, unique 0, citation 0, style 1, official 0)
- 2026-10-24 09:46 · verifier-1 · bloque-iv/m04-l07.s5b.draft.json · checked 4, PASS 3, FAIL 1 (key 0, unique 0, citation 0, style 1, official 0)
- 2026-10-24 09:46 · verifier-1 · bloque-iv/m04-l09.s5b.draft.json · checked 9, PASS 9, FAIL 0 (key 0, unique 0, citation 0, style 0, official 0)
- 2026-10-24 09:47 · coordinator · pending II–V replacements for the next writer-A run: m03-l05-q066 (official, conv2020·S2·4), m03-l06-q073 (official, conv2022_X·S1·1: ask art. 68.1 from an angle other than the plazo — who requires, the consequence's form «previa resolución», the art. 21 link), m03-l06-q074 (official, conv2025_A·S1·1), m04-l06-q290 (stem 41 words), m04-l07-q069 (gender agreement). Verifiers idle until a writer finishes a part.
- 2026-10-24 09:48 · writer-B · bloque-vi/m06-l02.part-3.draft.json · 56 written, lint clean (short-option flags only), stats z +0.45/+0.40, anchor misses 0
- 2026-10-24 09:52 · writer-A · bloque-vi/m06-l01.part-3.draft.json · 75 written (q201-q275), anchor misses 0, stats z +0.65/-1.03, lint clean (short-option flags only), every distractor shown wrong by a page sentence and grepped over sources/otros
- 2026-10-24 09:57 · writer-B · bloque-vi/m06-l02.part-4.draft.json · 58 written, lint clean (short-option flags only), stats z +1.26/+0.24, anchor misses 0
- 2026-10-24 10:04 · writer-B · bloque-vi/m06-l03.part-3.draft.json · 64 written, lint clean (short-option flags only), stats z +0.21/-0.24, anchor misses 0
- 2026-10-24 10:05 · writer-A · bloque-vi/m06-l01.part-4.draft.json · 70 written (q301-q370), anchor misses 0, stats z +0.96/-0.07, lint clean (short-option flags only), every distractor shown wrong by a page sentence and grepped over sources/otros
- 2026-10-24 10:07 · verifier-2 · lesson-fixes/s6/check.md · 2 checked, 1 PASS, 1 FAIL (m04-l06 art. 23 RD 33/1986, faithful)
- 2026-10-24 10:08 · verifier-2 · bloque-v/m05-l02.s5c.verify-1.md · 2 checked, 1 PASS, 1 FAIL (citation: q327)
- 2026-10-24 10:09 · writer-A · m03-l05.s5c.draft.json · 1 replacement (q067 for q066), lint 0, anchors 0
- 2026-10-24 10:09 · writer-A · m03-l06.s5c.draft.json · 2 replacements (q075 for q073, q076 for q074), lint 0, anchors 0
- 2026-10-24 10:09 · writer-A · m04-l06.s5c.draft.json · 1 replacement (q292 for q290), lint 0, anchors 0
- 2026-10-24 10:09 · writer-A · m04-l07.s5c.draft.json · 1 replacement (q073 for q069), lint 0, anchors 0
- 2026-10-24 10:09 · coordinator · m04-l06 art. 23 RD 33/1986 sentence replaced with the s6 checker's wording (plus the norm's «o falta penal»), art. 23 added to Normativa; to re-check. m05-l02-q327 dropped on citation: no replacement unless lost_coverage shows its cover lost after the merge.
- 2026-10-24 10:12 · writer-B · bloque-vi/m06-l03.part-4.draft.json · 66 written, lint clean (short-option flags only), stats z +0.59/-0.73, anchor misses 0
- 2026-10-24 10:12 · verifier-1 · m06-l01.part-3.draft.json · checked 75, PASS 58, FAIL 17 (key 0, unique 1, citation 0, style 16, official 0)
- 2026-10-24 10:13 · verifier-2 · lesson-fixes/s6/check.md (re-check m04-l06 art. 23 RD 33/1986) · checked 2, PASS 2, FAIL 0
- 2026-10-24 10:17 · verifier-1 · m06-l01.part-4.draft.json · checked 70, PASS 51, FAIL 19 (key 0, unique 1, citation 0, style 17, official 1)
- 2026-10-24 10:17 · coordinator · VI.1 complete: kept p1 67, p2 68, p3 58, p4 51 = 244 ≥ quota 241 (no replacements unless a cover is lost). 29 of the 36 p3–p4 fails were stems without «Windows 11»: rule made explicit in bloque-vi/spec.md, plus «feature-update frequency not asked» (ms-win-update.html contradicts itself).
- 2026-10-24 10:18 · verifier-2 · m06-l02.part-3.draft.json · checked 56, PASS 56, FAIL 0 (key 0, unique 0, citation 0, style 0, official 0)
- 2026-10-24 10:21 · verifier-2 · m06-l02.part-4.draft.json · checked 58, PASS 56, FAIL 2 (key 0, unique 0, citation 0, style 2, official 0)
- 2026-10-24 10:22 · writer-A · bloque-vi/m06-l04.part-2.draft.json · 68 written (q101-q168), anchor misses 0, stats z +0.88/-0.86, lint clean (short-option flags only), every distractor shown wrong by a saved-page sentence, stems name Word 365
- 2026-10-24 10:24 · writer-B · m06-l05.part-2.draft.json · 58 written, lint clean (short shortcut/code options only), stats z -0.61/+0.27, anchor misses 0
- 2026-10-24 10:25 · verifier-2 · m06-l03.part-3.draft.json · checked 64, PASS 47, FAIL 17 (key 0, unique 0, citation 0, style 16, official 1)
- 2026-10-24 10:28 · verifier-2 · m06-l03.part-4.draft.json · checked 66, PASS 21, FAIL 45 (key 0, unique 0, citation 0, style 45, official 0; 39 for stems without «Windows 11»)
- 2026-10-24 10:29 · coordinator · rulings: «Copilot para Windows» needs no version (official exams name it so); the Asistencia rápida web app needs no Windows version. VI.3 short of quota after p3–p4 version fails: rewrite version-only fails (m06-l03 p3 q221, q225–q234; p4 the 39 listed in part-4.verify-1) under new ids with «en Windows 11». Lesson note: m06-l02 l. 70–71 gives the orientation path «Escala y diseño» that the page shows only in its Windows 10 tab — to fix.
- 2026-10-24 10:30 · writer-A · bloque-vi/m06-l04.part-3.draft.json · 62 written (q201-q262), anchor misses 0, stats z +1.00/-0.32, lint clean (short-option flags only), every distractor shown wrong by a saved-page sentence, stems name Word 365
- 2026-10-24 10:31 · verifier-1 · bloque-iii/m03-l05.s5c.draft.json · checked 1, PASS 1, FAIL 0 (key 0, unique 0, citation 0, style 0, official 0)
- 2026-10-24 10:31 · verifier-1 · bloque-iii/m03-l06.s5c.draft.json · checked 2, PASS 1, FAIL 1 (key 0, unique 0, citation 1, style 0, official 0)
- 2026-10-24 10:31 · verifier-1 · bloque-iv/m04-l06.s5c.draft.json · checked 1, PASS 1, FAIL 0 (key 0, unique 0, citation 0, style 0, official 0)
- 2026-10-24 10:31 · verifier-1 · bloque-iv/m04-l07.s5c.draft.json · checked 1, PASS 0, FAIL 1 (key 0, unique 0, citation 0, style 0, official 1)
- 2026-10-24 10:32 · writer-B · m06-l05.part-3.draft.json · 56 written, lint clean (short function/figure options only), stats z +0.12/-0.35, anchor misses 0
- 2026-10-24 10:34 · verifier-2 · m06-l05.part-2.draft.json · checked 58, PASS 55, FAIL 3 (key 1, unique 1, citation 0, style 1, official 0)
- 2026-10-24 10:37 · writer-A · bloque-vi/m06-l04.part-4.draft.json · 62 written (q301-q362), anchor misses 0, stats z -0.65/-0.96, lint clean (short-option flags only), every distractor shown wrong by a saved-page sentence, stems name Word 365
- 2026-10-24 10:37 · verifier-2 · m06-l05.part-3.draft.json · checked 56, PASS 50, FAIL 6 (key 0, unique 1, citation 1, style 2, official 2)
- 2026-10-24 10:37 · verifier-1 · bloque-vi/m06-l04.part-2.draft.json · checked 68, PASS 61, FAIL 7 (key 0, unique 1, citation 0, style 6, official 0)
- 2026-10-24 10:38 · verifier-1 · bloque-vi/m06-l04.part-2.draft.json (revised, replaces the 10:37 line) · checked 68, PASS 59, FAIL 9 (key 0, unique 1, citation 0, style 8, official 0)
- 2026-10-24 10:40 · writer-B · m06-l05.part-4.draft.json · 56 written, lint clean (short shortcut/figure options only), stats z +1.06/-0.59, anchor misses 0
- 2026-10-24 10:40 · writer-A · bloque-vi/m06-l03.part-3b.draft.json · authored 11, lint clean (short-option flags only), stats ok, anchors 0 misses, quotes 0 misses
- 2026-10-24 10:40 · writer-A · bloque-vi/m06-l03.part-4b.draft.json · authored 39, lint clean (short-option flags only), stats ok, anchors 0 misses, quotes 0 misses
- 2026-10-24 10:40 · verifier-1 · bloque-vi/m06-l04.part-3.draft.json · checked 62, PASS 53, FAIL 9 (key 0, unique 2, citation 0, style 7, official 0)
- 2026-10-24 10:41 · coordinator · PAUSE ordered by the user (resume another day after the limit reset). No new agents; the four running agents finish their current part and stop, each logging here. Resume: read this log from the top of «Session 6 progress»; then (1) VI.3 version rewrites and the m06-l02 l. 70–71 lesson fix if not logged done, (2) verify VI.4 p3–p4, VI.5 p4, the m03/m04 s5c files if not logged, the VI.3 rewrite files, (3) write VI.6 p2–p5, VI.7 p2–p4, VI.8 p1–p3, verify them, (4) coverage check II–V (lost_coverage after merging s5/s5b/s5c), theory-ledger coverage-audit-miss notes, (5) merge, rebuild II–V, build VI, goldens, suites, ledger close, ten VI questions.
- 2026-10-24 10:41 · coordinator · verifier-1 paused: m06-l04 p4 and verifier-2's m06-l05 p4 not verified. New II–V replacements needed: m03-l06-q075 (citation: key is art. 21's heading), m04-l07-q073 (official, conv2025_A·P1·31). Kept the m06-l04-q160 drop (verdict rested on the live en-us page saying «colon» against the saved es-es «punto y coma»); flag the Word index page for an R2b currency check. Ledger note: the 10:37 verifier-1 line for m06-l04 p2 is superseded by the 10:38 line.
- 2026-10-24 10:41 · writer-A · content/.../m06-l02.md + lesson-fixes/s6/writer.md §3 · orientation path removed (Windows 10 tab only); esquema 10 passed, citations 60 passed
- 2026-10-24 10:41 · coordinator · all agents stopped; PAUSED until the limit reset. Next-session queue: (1) verify: VI.3 part-3b (11) and part-4b (39), VI.4 p4 (62), VI.5 p4 (56); blind-check the m06-l02 l. 70–71 lesson fix (lesson-fixes/s6/writer.md §3) and re-verify the m06-l02 questions on screen orientation that may rest on the Windows 10 tab; (2) II–V replacements m03-l06-q075, m04-l07-q073; (3) write VI.6 p2–p5, VI.7 p2–p4, VI.8 p1–p3 and verify them; (4) per-tema quota and coverage check (families ≥5, programme features ≥1, lost_coverage after merges); theory-ledger coverage-audit-miss notes; (5) merge, rebuild II–V, build VI, goldens, suites, ledger close, ten VI questions.
- 2026-10-27 18:33 · coordinator · resumed after the reset. verifier-1 (opus): VI.3 part-3b+4b, VI.4 p4; verifier-2 (opus): VI.5 p4, m06-l02 lesson-fix check, orientation re-check (q013, q242, q250); writer-A (sonnet): m03-l06-q075 and m04-l07-q073 replacements (.s5d), VI.6 p2–p3; writer-B (sonnet): VI.7 p2–p4.
- 2026-10-27 18:35 · writer-A · bloque-iii/m03-l06.s5d.draft.json · 1 replacement (q077 for q075), lint 0, anchors 0, quotes ok
- 2026-10-27 18:35 · writer-A · bloque-iv/m04-l07.s5d.draft.json · 1 replacement (q074 for q073), lint 0, anchors 0, quotes ok
- 2026-10-27 18:37 · verifier-1 · m06-l03.part-3b.draft.json + m06-l03.part-4b.draft.json · checked 50, PASS 43, FAIL 7 (key 0, unique 1, citation 0, style 6, official 0)
- 2026-10-27 18:39 · verifier-1 · m06-l04.part-4.draft.json · checked 62, PASS 21, FAIL 41 (key 1, unique 1, citation 0, style 38, official 1)
- 2026-10-27 18:40 · verifier-2 · bloque-vi/m06-l05.part-4.verify-1.md · 56 checked, 26 PASS, 30 FAIL (unique 2, style 26, official 2)
- 2026-10-27 18:40 · verifier-2 · lesson-fixes/s6/check.md «m06-l02 (§3)» · 1 checked, 1 PASS
- 2026-10-27 18:41 · coordinator · VI.3 done (~240 kept ≥ 221). VI.4 short (~191 of 217): 38 style-only fails in part-4 (explanations not naming distractors) queued for rewrite into m06-l04.part-4b (new ids from q363) by the next free writer; explanation pattern made explicit in bloque-vi/spec.md and sent to both running writers.
- 2026-10-27 18:41 · verifier-2 · bloque-vi/m06-l02.orientation-recheck.md · 3 checked, 2 PASS, 1 FAIL (q013 style)
- 2026-10-27 18:42 · coordinator · VI.5 short (~191 of 202): part-4 fails that are style-only (unnamed distractors; «Señale» stems ending in «.») queued for rewrite into m06-l05.part-4b (ids from q357) with the VI.4 part-4b rewrite. m06-l02 §3 lesson fix PASS; m06-l02-q013 dropped (rests on the Windows 10 panel).
- 2026-10-27 18:44 · writer-A · bloque-vi/m06-l06.part-2.draft.json · 59 authored (q101-q159), lint ok, anchors 0, quotes ok
- 2026-10-27 18:46 · writer-B · m06-l07.part-2.draft.json · 74 written, lint 0 real flags (31 short-option), stats z -0.56/-1.03, anchor misses 0
- 2026-10-27 18:52 · writer-A · bloque-vi/m06-l06.part-3.draft.json · 58 authored (q201-q258), lint ok, anchors 0, quotes ok
- 2026-10-27 18:52 · writer-A · bloque-vi/m06-l06.part-2.draft.json · final 62 authored (q101-q162) after lmc top-up, lint ok, anchors 0, quotes ok
- 2026-10-27 18:54 · verifier-1 · bloque-iii/m03-l06.s5d.draft.json · checked 1, PASS 1, FAIL 0 (key 0, unique 0, citation 0, style 0, official 0)
- 2026-10-27 18:54 · verifier-1 · bloque-iv/m04-l07.s5d.draft.json · checked 1, PASS 1, FAIL 0 (key 0, unique 0, citation 0, style 0, official 0)
- 2026-10-27 18:54 · writer-B · m06-l07.part-3.draft.json · 67 written, lint 0 real flags (25 short-option), stats z +0.77/-0.23, anchor misses 0
- 2026-10-27 18:55 · writer-A · bloque-vi/m06-l04.part-4b.draft.json · 37 rewrites authored (q363-q399), lint ok (short labels only), anchors 0, quotes ok; stats z -2.36/-1.97 on the failure subset
- 2026-10-27 18:57 · verifier-2 · bloque-vi/m06-l06.part-3.draft.json · checked 58, PASS 51, FAIL 7 (key 0, unique 2, citation 0, style 5, official 0)
- 2026-10-27 18:57 · writer-A · bloque-vi/m06-l05.part-4b.draft.json · 26 rewrites authored (q357-q382), lint ok (short labels only), anchors 0, quotes ok, stats z +1.14/-0.74
- 2026-10-27 18:58 · verifier-1 · bloque-vi/m06-l06.part-2.draft.json · checked 62, PASS 53, FAIL 9 (key 0, unique 0, citation 0, style 8, official 1)
- 2026-10-27 18:59 · coordinator · bloques II–V: all s5/s5b/s5c/s5d files verified and merged into the lesson drafts (last part where parts exist, then merge_parts; 202 questions; backup of the pre-merge folders in the scratchpad coord-merge/). The .s5* files stay as records, already merged — do not merge them again. lost_coverage after the merge: 25 official codes lost (m03-l03 3, m03-l04 3, m05-l02 3, m05-l03 6, m05-l04 3, m05-l05 4, m05-l06 3), all from earlier sessions; queued as one coverage top-up run (one question per code, new stem form and distractors under the check-5 ruling) for the next free writer.
- 2026-10-27 19:00 · writer-B · m06-l07.part-4.draft.json · 65 written, lint 0 real flags (28 short-option), stats z +0.32/+0.30, anchor misses 0
- 2026-10-27 19:05 · verifier-1 · bloque-vi/m06-l07.part-2.draft.json · checked 74, PASS 64, FAIL 10 (unique 3: q127, q138, q149; style 7: q101, q102, q104, q110, q111, q139, q165)
- 2026-10-27 19:06 · coordinator · for R2b: ms-outlook-procedimientos.html and ms-outlook-limpieza-buzon.html list only Outlook 2024/2021 under «Se aplica a»; ms-outlook-buscar.html contradicts itself on quotes (lesson m06-l07 l. 44 rests on it); ms-win-update.html contradicts itself on feature-update frequency; the Word index page (es-es «punto y coma» vs en-us «colon»).
- 2026-10-27 19:06 · verifier-2 · m06-l07.part-3.draft.json · checked 67, PASS 55, FAIL 12 (key 1, unique 3, citation 3, style 5, official 0)
- 2026-10-27 19:08 · verifier-2 · m06-l07.part-4.draft.json · checked 65, PASS 62, FAIL 3 (key 0, unique 3, citation 0, style 0, official 0)
- 2026-10-27 19:08 · coordinator · VI.7 done: kept p1 72, p2 64, p3 55, p4 62 = 253 ≥ quota 246. Done temas: VI.1, VI.2, VI.3, VI.7. Pending: VI.4/VI.5 part-4b rewrites and VI.6 p4–p5 (writer-A), VI.8 p1–p3 (writer-B), II–V coverage top-up (25 codes), close-out.
- 2026-10-27 19:13 · writer-A · bloque-vi/m06-l06.part-4.draft.json · 61 authored (q301-q361), lint ok (short labels only), anchors 0, quotes ok, stats z +0.54/+0.64
- 2026-10-27 19:13 · writer-A · bloque-vi/m06-l06.part-5.draft.json · 60 authored (q401-q460), lint ok (short labels only), anchors 0, quotes ok, stats z -0.31/-0.32; programme feature Importación/vinculación/exportación 36 questions
- 2026-10-27 19:14 · coordinator · theory ledger: section «R3 session 5–7 lesson fixes» added (coverage-audit misses, errors corrected, not done).
- 2026-10-27 19:15 · writer-B · bloque-vi/m06-l08.part-1.draft.json · 71 written, lint 6 flags (short names/years only), stats z -0.05/+1.20, anchor misses 0
- 2026-10-27 19:16 · writer-A · bloque-iii/m03-l03.s7.draft.json · 3 written (q323-q325), codes covered conv2020·S2·3, conv2022_X·P1·29, conv2024_X·S2·9, skipped none
- 2026-10-27 19:17 · verifier-1 · bloque-vi/m06-l04.part-4b.draft.json · checked 37, PASS 32, FAIL 5 (unique q390; style q374 q385 q391 q399)
- 2026-10-27 19:18 · verifier-2 · m06-l06.part-4.draft.json · checked 61, PASS 57, FAIL 4 (unique 1: q342; style 3: q322, q339, q344)
- 2026-10-27 19:20 · verifier-2 · m06-l06.part-5.draft.json · checked 60, PASS 59, FAIL 1 (unique 1: q403)
- 2026-10-27 19:20 · verifier-1 · bloque-vi/m06-l05.part-4b.draft.json · checked 26, PASS 25, FAIL 1 (style q378)
- 2026-10-27 19:20 · coordinator · VI.6 done (all five parts verified; kept ≥ quota 253).
- 2026-10-27 19:20 · coordinator · VI.4 done (218 ≥ 217) and VI.5 done (214 ≥ 202) after part-4b verification; m06-l05-q370 dropped by the coordinator (probable typo «225» on the saved validation page; R2b to check the live page). Done: VI.1–VI.7; VI.8 being written.
- 2026-10-27 19:24 · writer-B · bloque-vi/m06-l08.part-2.draft.json · 67 written, lint 3 flags (labels/shortcuts only), stats z +1.24/+0.23, anchor misses 0
- 2026-10-27 19:25 · coordinator · bloque VI coverage (VI.1–VI.7): 55 recurring families, all ≥ 5 kept questions («Plantillas» tagged 2 but 16 by content); every listed programme feature asked (AQS/search filters 12, RAID 2, Copilot open/in apps 3/6, Paint 8, Reloj 10, Inmovilizar 5, MFA 7…); every «Lo que más cae» line covered (m06-l06 lmc-9 by q329, tag added — metadata only); 190 official codes covered. VI.8 pending.
- 2026-10-27 19:31 · verifier-1 · II–V coverage top-up (.s7) · checked 19, PASS 16, FAIL 3 (official 1: m03-l03-q324; style 2: m03-l04-q286, m03-l04-q287 stem over 40 words on an amount computation); covers yes/partly/no 17/8/0
- 2026-10-27 19:32 · coordinator · II–V coverage top-up (.s7) 16/19 PASS; covers 17 yes, 8 partly, 0 no. Retries for q286, q287 (stem length) and q324 (official) given to writer-A (.s7b). A verifier's scratch folder had landed in the repo root (verifier-1j-s7/, untracked extracts and a script); moved to the scratchpad.
- 2026-10-27 19:33 · writer-A · m03-l04.s7b.draft.json (q288-q289), m03-l03.s7b skipped (q324) · 2 replacements authored, lint/stats/anchors/quotes clean; q324 skipped: fact already in q150, other angles in q151/art. 58 or not in the lesson
- 2026-10-27 19:33 · writer-B · bloque-vi/m06-l08.part-3.draft.json · 65 written, lint 20 flags (shortcuts/labels under five words only), stats z -0.01/+0.24, anchor misses 0
- 2026-10-27 19:33 · coordinator · UNREACHABLE cover, for the user: official:conv2022_X·P1·29 (III.3, art. 63.1 LPAC: the procedimiento sancionador «siempre de oficio»). Four tries fell as rewordings (q150, q324 …); any option set on how it starts pairs the official key with a reworded official distractor (a petición de parte, por denuncia), and art. 62 LPAC is not in the lesson. Needs a decision: accept the gap, or allow one question with that key and new non-official distractors, or add art. 62 to m03-l03.
- 2026-10-27 19:34 · verifier-1 · m03-l04.s7b · checked 2, PASS 2, FAIL 0 (none)
- 2026-10-27 19:37 · verifier-2 · bloque-vi/m06-l08.part-1.draft.json · checked 71, PASS 69, FAIL 2 (key q067; style q021)
- 2026-10-27 19:39 · verifier-1 · m06-l08.part-3 · checked 65, PASS 61, FAIL 4 (unique 1: q233; style 3: q227, q236, q245)
- 2026-10-27 19:40 · coordinator · II–V closed: .s7/.s7b merged (21); lost_coverage leaves only the unreachable conv2022_X·P1·29. Rebuilt bloques II–V: II 264, III 775, IV 989, V 646 kept. build_exercises.py fixed to read only the lesson's main draft (the glob was also visiting the merged .s5/.s7 record files, double-counting the total; output files were unaffected).
- 2026-10-27 19:40 · verifier-2 · bloque-vi/m06-l08.part-2.draft.json · checked 67, PASS 64, FAIL 3 (official q129; style q135, q154)
- 2026-10-27 19:17 · writer-A · bloque-iii/m03-l04.s7.draft.json · 2 written (q286-q287), codes covered conv2020_X·P1·28, conv2024_X·S2·6, conv2025_A·S1·10, skipped none
- 2026-10-27 19:19 · writer-A · bloque-v/m05-l02.s7.draft.json · 3 written (q328-q330), codes covered conv2022_X·S1R·2, conv2022·S1R·1, conv2024_A·P1·36, skipped none
- 2026-10-27 19:20 · writer-A · bloque-v/m05-l03.s7.draft.json · 3 written (q312-q314), codes covered conv2020_X·S1·10, conv2020_X·S1·13, conv2022_X·P1·27, conv2024_A·S1·18, conv2020·S1·10, conv2024_X·P1R·5, skipped none
- 2026-10-27 19:22 · writer-A · bloque-v/m05-l04.s7.draft.json · 3 written (q091-q093), codes covered conv2020_X·P1·38, conv2020·P1·27, conv2025_X·S2·3, skipped none
- 2026-10-27 19:23 · writer-A · bloque-v/m05-l05.s7.draft.json · 2 written (q097-q098), codes covered conv2020_X·S2·10 (partial), conv2022_X·P1·24, conv2022_X·S2·11, conv2025_A·S2R·3, skipped none
- 2026-10-27 19:24 · writer-A · bloque-v/m05-l06.s7.draft.json · 3 written (q093-q095), codes covered conv2020_X·S1·1, conv2020_X·S2·13 (partial), conv2022·S2·7, skipped none
- 2026-10-27 19:43 · coordinator · the six writer-A lines above (19:17–19:24) had been appended to a stray docs/age-verification/age-bank-ledger.md; moved here, stray file removed. Also moved a second verifier scratch folder (verifier-1g-s7/) out of the repo root.
- 2026-10-27 19:59 · coordinator · README updated (bank counts, all six bloques); ledger «R3 close» section written at the top.
- 2026-10-27 20:05 · coordinator · frontend full rerun: 594 passed, 51 skipped, 0 failed. R3 closed.
- 2026-10-27 20:13 · coordinator · R3 close (user): (1) art. 62 LPAC into m03-l03 → writer-A; (2) live check of the saved Microsoft pages (six files on the R2b list) → verifier-1; (3) explanation scan over the whole bank (5,223 kept): 289 flagged — silence 255, repeated sentence 34 (bloque VI 136, I–V 153; q211 and q122 among them). Rewrites as id→explanation maps (style-fix-brief.md), blind-checked, then applied by the coordinator; options untouched. VI set → writer-B.
- 2026-10-27 20:13 · writer-A · m03-l03 art. 62 LPAC · done (62.1-62.5 added, Normativa updated, tests pass, anchors resolve)
- 2026-10-27 20:13 · verifier-1 · live check (6 pages) · changed: none (es-es visible text identical on ms-word-indice, ms-excel-lista-desplegable, ms-win-update, ms-outlook-buscar, ms-outlook-procedimientos, ms-outlook-limpieza-buzon; report bloque-vi/live-check-r3-close.md); questions affected: none
- 2026-10-27 20:14 · coordinator · live check (report bloque-vi/live-check-r3-close.md): all six pages unchanged in visible text, saved sha256 match fuentes.yaml; no question re-verified, fuentes.yaml unchanged. Notes: es-es Word index still «punto y coma» (q160's drop rested on the en-us page; kept dropped); live Excel page still prints «225 caracteres» (q370 stays dropped).
- 2026-10-27 20:15 · verifier-2 · m03-l03 art. 62 check · 2 PASS (62.1-62.3/62.5 paragraph, Normativa line), 1 FAIL (62.4 paragraph: dropped «de esta naturaleza», «repare»→«se repare», subject of «facilite»)
- 2026-10-27 20:15 · coordinator · m03-l03 art. 62.4 paragraph replaced with the r3-close checker's wording (verified against the LPAC text); to re-check.
- 2026-10-27 20:16 · verifier-2 · m03-l03 art. 62.4 re-check · PASS
- 2026-10-27 20:24 · writer-B · style rewrites VI · 50/136 ids done
- 2026-10-27 20:24 · writer-B · style rewrites VI · 100/136 ids done
- 2026-10-27 20:24 · writer-B · style rewrites VI · 136/136 ids done
- 2026-10-27 20:25 · writer-A · style rewrites I–V · 50/153 ids done
- 2026-10-27 20:25 · writer-A · style rewrites I–V · 100/153 ids done
- 2026-10-27 20:25 · writer-A · style rewrites I–V · 153/153 ids done
- 2026-10-27 20:26 · writer-A · m03-l03 r3c · q326 (art. 63.1 LPAC, official:conv2022_X·P1·29) written; lint 0, anchors 0 misses, quote ok
- 2026-10-28 11:54 · verifier-2 · style rewrites I–V batch 1 (ids 1–60) · PASS 56, FAIL 4
- 2026-10-28 11:54 · verifier-2 · style rewrites I–V batch 2 (ids 61–120) · PASS 54, FAIL 6
- 2026-10-28 11:54 · verifier-2 · style rewrites I–V batch 3 (ids 121–153, incl. unsupported m05-l03-q280) · PASS 29, FAIL 4
- 2026-10-28 11:54 · verifier-2 · m03-l03 r3c q326 · PASS 1, FAIL 0 (cover of conv2022_X·P1·29: no)
- 2026-10-28 11:55 · coordinator · I–V rewrites: 139/153 PASS; m05-l03-q280 dropped (open list, art. 107 LGP); 13 failed rewrites to a second pass. q326 passes but does not test the official fact (de oficio is a shared premise): its official:conv2022_X·P1·29 claim removed (metadata only); writer-A to write a «¿Cuál … afirmaciones es correcta?» question with «siempre de oficio» as the true statement and arts. 62–63 falsehoods as distractors.
- 2026-10-28 11:57 · verifier-1 · style rewrites VI batch 1 · PASS 51, FAIL 9
- 2026-10-28 11:57 · verifier-1 · style rewrites VI batch 2 · PASS 53, FAIL 9
- 2026-10-28 11:58 · coordinator · VI rewrites: 104/122 PASS; unsupported 14 → 4 PASS on check 2 (sentence found), 10 dropped (style-recheck). Pass 2 to writer-B: 18 failed + 4 to write from the checker's sentences + 2 quote slips.
- 2026-10-28 11:58 · writer-A · second pass on 13 failed explanation rewrites (style-rewrites-i-v-2.json) · 11 rewrite, 2 unsupported (m01-l02-q056, m04-l09-q060)
- 2026-10-28 11:58 · writer-A · m03-l03.r3d, 1 question on art. 63.1 LPAC (q327, covers conv2022_X·P1·29) · lint 0, anchor ok, quote ok
- 2026-10-28 11:59 · coordinator · applied the round-1 PASS explanation rewrites (explanation field only, every draft file holding the id): I–V 139, VI 104. Pass-2 I–V (11 rewrite, 2 unsupported) and q327 to verifier-2.
- 2026-10-28 12:03 · writer-B · style rewrites VI pass 2 · 24 ids: 15 rewrite, 9 unsupported (m06-l01-q351, m06-l02-q129, m06-l02-q135, m06-l02-q139, m06-l04-q060, m06-l04-q104, m06-l04-q147, m06-l06-q058, m06-l06-q421)
- 2026-10-28 12:05 · verifier-2 · style rewrites I–V pass 2 (style-rewrites-i-v-2.check.md): 11 rewrite + 2 unsupported; FAIL m03-l02-q038 (also dropped, check 2), m03-l04-q106, m05-l03-q002, m05-l01-q036; m01-l02-q056 dropped (check 2); m04-l09-q060 kept (art. 224.3 LGSS), explanation still open · PASS 8, FAIL 5
- 2026-10-28 12:05 · verifier-2 · m03-l03.r3d verify-1, q327 (art. 63.1 LPAC); cover of conv2022_X·P1·29: partly · PASS 1, FAIL 0
- 2026-10-28 12:05 · coordinator · I–V pass 2: 7 PASS applied; m03-l02-q038 and m01-l02-q056 dropped (check 2); pass 3 for m03-l04-q106, m05-l03-q002, m05-l01-q036, m04-l09-q060 → writer-A. q326 and q327 (art. 63.1 LPAC) PASS and merged into m03-l03; q327 covers conv2022_X·P1·29 «partly» (the official confusion — petición de parte, denuncia — cannot be offered under the user's constraint).
- 2026-10-28 · writer-A · style rewrites I–V pass 3 (style-rewrites-i-v-3.json) · 4 ids: 4 rewrite (m03-l04-q106, m05-l03-q002, m05-l01-q036, m04-l09-q060)
- 2026-10-28 12:08 · verifier-1 · style rewrites VI pass 2 · PASS 13, FAIL 11; unsupported dropped 8
- 2026-10-28 12:09 · coordinator · VI pass 2: 12 PASS applied; 8 unsupported dropped by verifier-1; m06-l05-q367 and m06-l06-q014 dropped by the coordinator (check 2, per the checker's reasons); m06-l08-q143 and m06-l01-q351 to a last rewrite from the sentences the checker found.
- 2026-10-28 12:09 · verifier-2 · style rewrites I–V pass 3 (style-rewrites-i-v-3.check.md): 4 rewrite; m03-l04-q106 and m04-l09-q060 dropped (check 2, style-recheck-3); m05-l03-q002 and m05-l01-q036 FAIL style only (explanation wording; question stands) · PASS 0, FAIL 4
- 2026-10-28 · writer-B · style rewrites VI pass 3 (style-rewrites-vi-3.json): m06-l08-q143 and m06-l01-q351 rewritten, 0 unsupported
- 2026-10-28 · verifier-1 · style rewrites final pass (style-rewrites-final.check.md): m05-l03-q002, m05-l01-q036 (i-v-4), m06-l08-q143, m06-l01-q351 (vi-3) · PASS 4, FAIL 0; no drops
- 2026-10-28 12:40 · coordinator · R3 closing steps done. Suites: frontend build and tsc -b clean, vitest 594 passed / 51 skipped / 0 failed; backend ruff, format, mypy clean; pytest 1,337 passed, 20 skipped, 160 errors — every error is a Testcontainers fixture failing at setup because the Docker daemon is not running (unix:///var/run/docker.sock missing), so the database-backed tests were NOT run this time (they passed on 2026-10-27 with Docker up; only content changed since); export_bundle --verify-only OK; verify_golden_stability exit 0. Android and crypto-futures untouched. README counts updated (5,200). Stop.
- 2026-10-28 13:33 · coordinator · Docker back up: full backend pytest 1,497 passed, 20 skipped, 0 errors — confirms the 160 setup errors were only the missing daemon.
