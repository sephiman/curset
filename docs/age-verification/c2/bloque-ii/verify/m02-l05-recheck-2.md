# Verification — `m02-l05`, re-check 2 (blind)

Verifier: blind, 2026-11-06. Did not write the lesson; checked against the saved pages (HTML stripped to text), not the
proposer's wording. Input: `docs/age-verification/c2/bloque-ii/pending/m02-l05.md` (4 items), lesson
`content/age-auxiliar-c2/es/lessons/m02-l05.md`. Pages read in `content/age-auxiliar-c2/sources/otros/`:
`ms-win-configuracion-red.html` (Windows 11 panel), `python-tutorial-introduccion.html`, `moodle-codigo-abierto.html`.

New page `moodle-codigo-abierto.html` (`descarga nueva`, 2026-11-06): sha256 `56bcbc47…6c8ed5` matches `fuentes.yaml`;
`lang="es-ES"`; canonical URL `https://moodle.com/es/acerca-de/open-source/` as recorded; the project's own Spanish page
(title «Código abierto - Moodle - Aprendizaje en línea de código abierto», breadcrumb «Sobre nosotros / Código abierto»).

| id | verdict | precept checked | note | replacement |
|---|---|---|---|---|
| `879c9f7558` | PASS | ms-win-configuracion-red.html; Windows 11, «Navegar por la configuración de Bluetooth y dispositivos» | «La sección Bluetooth y dispositivos te permite administrar los dispositivos conectados al equipo, incluidos periféricos inalámbricos, como mouse, teclados, altavoces, auriculares y mucho más»; «como» keeps the list open | — |
| `95e1d66291` | PASS | python-tutorial-introduccion.html | «Los números enteros (ej. 2, 4, 20) tienen tipo int, los que tienen una parte fraccionaria (por ejemplo 5.0, 1.6) tiene el tipo float»; «El más versátil es la lista, la cual puede ser escrita como una lista de valores separados por coma (ítems) entre corchetes» (page `lang="es"`) | — |
| `91498dceab` | PASS | moodle-codigo-abierto.html | «una plataforma de aprendizaje de código abierto como Moodle LMS»; «el código fuente de Moodle LMS tiene una licencia que permite a cualquiera descargar gratuitamente todo el software y personalizar su funcionamiento» | — |
| `0ad2696be0` | PASS | Fuentes | title «Código abierto», site moodle.com and date 06-11-2026 match the page and `fuentes.yaml`; the file is cited in the prose | — |

PASS 4, FAIL 0.

Finding for the coordinator, outside the pending ids: the «Fuentes» section does not list exactly the files cited.
`ms-win-configuracion-red.html` is cited in the prose (line 29, «Periféricos») but has no «Fuentes» line (34 files cited,
33 listed). Missing line, per `fuentes.yaml`: `ms-win-configuracion-red.html`: Microsoft, «Comprender y explorar la
configuración de Windows» (support.microsoft.com, consultado el 06-11-2026).
