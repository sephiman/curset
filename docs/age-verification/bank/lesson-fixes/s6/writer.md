# Lesson fixes, session 6 (writer A): record, 2026-10-24

Nothing committed. Checks: `uv run pytest tests/test_esquema.py -q` 10 passed; `uv run pytest tests/test_citations.py -q -k "not frozen"` 60 passed. Goldens not regenerated.

## 1. m04-l06, Procedimiento disciplinario / Principios, l. 291-293 (addition)

Sentence added after the art. 94.3 TREBEP one: «Por su parte, el RD 33/1986 dispone que el expediente continúe hasta su resolución, pero que se suspenda hasta que recaiga resolución judicial cuando los hechos pudieran ser constitutivos de alguno de los delitos de los funcionarios públicos tipificados en los títulos II y VII del libro segundo del Código Penal (art. 23 RD 33/1986).» Both rules are stated; the lesson does not say which prevails. Resolves to `boe-a-1986-1216-art-23`.

Norm (art. 23 RD 33/1986): «Ello no será obstáculo para que continúe la tramitación del expediente disciplinario hasta su resolución e imposición de la sanción si procediera. No obstante, cuándo se trate de hechos que pudieran ser constitutivos de algunos de los delitos cometidos por los funcionarios públicos, contra el ejercicio de los derechos de la persona reconocidos por las Leyes y de los delitos de los funcionarios públicos, en el ejercicio de sus cargos, tipificados en los títulos II y VII del Libro segundo del Código Penal, deberá suspenderse la tramitación del expediente disciplinario hasta tanto recaiga resolución judicial.»

## 2. m06-l01, «Aplicación de fuentes abiertas», l. 29-30 (citation form)

The prose already cited `boe-rd-4-2010-eni.pdf` and the Fuentes list already named it (l. 133), but the citation was «(fuente: `boe-rd-4-2010-eni.pdf`, anexo)»: the resolver's grammar takes only file names in a `fuente:` segment, so `_anchor` returned None. Now «(fuente: `boe-rd-4-2010-eni.pdf`)», which resolves to `fuente-boe-rd-4-2010-eni-pdf`. The word «anexo» is dropped; the fact is unchanged. The lesson's definition is a faithful reduction of the PDF's glossary (anexo): «Aplicación de fuentes abiertas: Aquella que se distribuye con una licencia que permite la libertad de ejecutarla, de conocer el código fuente, de modificarla o mejorarla y de redistribuir copias a otros usuarios.» No change to the Fuentes list (the entry exists). RD 4/2010 is not in `normativa.yaml`.

## 3. m06-l02, «Varias pantallas», l. 70-71 (correction)

Old text: «La configuración de cada pantalla se ajusta por separado: resolución y diseño; la orientación, en «Escala y diseño» (fuente: `ms-win-varias-pantallas.html`).» The page prints «Escala y diseño» and «Orientación de Pantalla» only in its Windows 10 tab («Cambiar la orientación … vaya a Escala y diseño, a continuación elija su Orientación de Pantalla»). The Windows 11 tab gives no orientation path; it lists only the links «Cambiar el brillo y el color de la pantalla», «Cambiar la resolución, la escala y el diseño de la pantalla» and «Cambiar la frecuencia de actualización de la pantalla».

New text (same lines): «La configuración de cada pantalla se ajusta por separado: brillo y color, resolución, escala y diseño, y frecuencia de actualización (fuente: `ms-win-varias-pantallas.html`).» The orientation clause and its path are removed; the Windows 11 tab states no orientation fact to keep. Citation unchanged and resolving. Note for the bank: m06-l02 questions on orientation (e.g. part-1 q «resolución, escala y orientación») rest on the Windows 10 tab and need a check. Checks: `test_esquema.py` 10 passed; `test_citations.py -k "not frozen"` 60 passed.
