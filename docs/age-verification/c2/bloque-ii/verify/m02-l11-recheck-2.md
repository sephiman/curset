# Verification — `m02-l11`, re-check 2 (blind)

Verifier: blind, 2026-11-06. Did not write the lesson; checked against the saved pages in `content/age-auxiliar-c2/sources/otros/` (HTML stripped to text; Windows desktop sections, located by the pages' `data-tab` panels). Input: `docs/age-verification/c2/bloque-ii/pending/m02-l11.md` (4 items), lesson
`content/age-auxiliar-c2/es/lessons/m02-l11.md`. Pages read: `ms-outlook-atajos.html` (`classic-outlook` panel),
`ms-outlook-contactos-combinar.html`.

New page (`descarga nueva`, 2026-11-06): `ms-outlook-contactos-combinar.html` sha256 matches
`writer/m02-l11-fix-fuentes.yaml` and `sources/otros/fuentes.yaml`; `lang="es-ES"`, canonical URL equal to the recorded
one, Spanish article title as recorded. `ms-outlook-atajos.html` is an earlier copy; its sha256 matches `fuentes.yaml`.

| id | verdict | precept checked | note | replacement |
|---|---|---|---|---|
| `8eacb3a49f` | FAIL | ms-outlook-atajos.html; Outlook clásico, «Ir a la cinta de opciones» | the cited table gives «Abrir la pestaña Enviar y recibir. — Alt+J, S», not «Alt, J, S» (that form is in the classic «Métodos abreviados de teclado más usados» table: «Ir a la pestaña Enviar y recibir. — Alt, J, S»). ALT+H Inicio, Alt+F menú Archivo, Alt+O Carpeta, Alt+V Vista are literal. The page disagrees with itself; both forms stated | **Pestañas de la cinta de Outlook clásico**: la página de métodos abreviados da Alt+H para Inicio, Alt+J, S para Enviar y recibir (la tabla de métodos abreviados más usados da Alt, J, S), Alt+O para Carpeta y Alt+V para Vista; Alt+F abre el menú Archivo (fuente: `ms-outlook-atajos.html`; Ir a la cinta de opciones). |
| `1884ce97c0` | PASS | ms-outlook-contactos-combinar.html | «El comando Combinar correspondencia de Contactos solo está disponible en la versión clásica de Outlook para Windows»; «En Outlook clásico, vaya a People y seleccione los nombres … si desea incluir toda la libreta de direcciones, omita este paso» («People» is the page's own untranslated label) | — |
| `4ff795f04b` | PASS | ms-outlook-contactos-combinar.html | «En el nuevo Outlook para Windows, puede enviar a cada destinatario su propia copia del mensaje … seleccione la flecha situada junto a Enviar y, a continuación, seleccione Iniciar combinación de correspondencia. Esta opción no inserta campos personalizados desde los contactos.» | — |
| `4a6163e6f6` | PASS | Fuentes | title and date match the saved page; cited in the prose | — |

PASS 3, FAIL 1.

«Fuentes» section: 32 files cited in the prose, 32 listed, the same set.
