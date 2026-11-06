# Verification — `m02-l07`, re-check 1

Verifier: blind verifier (opus), 2026-11-06. Did not write the lesson.

Files read: `docs/age-verification/c2/bloque-ii/pending/m02-l07.md`, `content/age-auxiliar-c2/es/lessons/m02-l07.md`, and in
`content/age-auxiliar-c2/sources/otros/`: `ms-win-explorador.html` and `ms-win-liberar-espacio.html` (raw HTML for the tab
boundaries, `<section data-tab="windows-11">` / `<section data-tab="windows-10">`, and stripped text for the wording).

Tab positions: in `ms-win-explorador.html` the Windows 10 panel starts at byte 70037; «Las bibliotecas no se muestran…»
(72876, 75507), «Las carpetas usadas con frecuencia…» (72014) and «Si solo quieres ver las carpetas ancladas…» (73985)
are all in it, none in the Windows 11 panel. In `ms-win-liberar-espacio.html` the Windows 10 panel starts at byte 71611;
«Liberador de espacio» occurs only after it (72740+); «Recomendaciones de limpieza» (64137) is only in the Windows 11
panel; the Sensor de almacenamiento paragraph is in both.

Result: 6 PASS, 0 FAIL.

| id | verdict | precept checked | note | replacement |
|---|---|---|---|---|
| `c5df5605f1` | PASS | ms-win-explorador.html; Windows 10 tab | version claim right; «Las bibliotecas no se muestran en el Explorador de archivos a menos que usted quiera… pestaña Vista › Panel de navegación › Mostrar bibliotecas» (page text garbled, labels all present). «lo describe» refers to the topic (neuter «lo»); «las describe» would read better | — |
| `de86df3aa8` | PASS | ms-win-explorador.html; Windows 10 tab | version claim right; «Las carpetas usadas con frecuencia y los archivos usados recientemente se muestran allí»; «pestaña Vista… Opciones. En la sección Privacidad, desactive las casillas… solo mostrará las carpetas ancladas» | — |
| `a0e52173d0` | PASS | ms-win-liberar-espacio.html; Windows 10 tab | version claim right; «Si el sistema no tiene Sensor de almacenamiento… Liberador de espacio en disco para eliminar archivos temporales y archivos del sistema»; «En el cuadro de búsqueda de la barra de tareas, escribe liberador de espacio en disco»; «Selecciona la unidad». No citation of its own; governed by the next sentence's | — |
| `cd086e9008` | PASS | ms-win-liberar-espacio.html; Windows 11 tab | categories and «la cantidad de espacio que guardará al quitar esos elementos» verbatim; the page's path is garbled («Inicio>Configuración>Recomendaciones de limpieza delalmacenamiento> delsistema>»), the lesson's order Sistema › Almacenamiento › Recomendaciones de limpieza is the reconstruction of those labels | — |
| `d149e1a065` | PASS | ms-win-liberar-espacio.html; both tabs | verbatim: «puede liberar automáticamente espacio en el disco al deshacerse de los elementos que no necesitas, como archivos temporales y elementos en la Papelera de reciclaje» | — |
| `f156f1b8d9` | PASS | ms-win-liberar-espacio.html; Windows 11 tab | «incluidos los archivos temporales, los archivos grandes o sin usar, los archivos sincronizados con la nube y las aplicaciones sin usar» | — |
