# Lesson fixes s6: blind check (verifier 2, 2026-10-24)

Checked against `lesson-fixes/s6/writer.md`, judged from `git diff HEAD -- <lesson>` and from the sources read with
`pdftotext -layout`: `sources/normativa/BOE-A-1986-1216_rd-33-1986-regimen-disciplinario_1991-12-31.pdf` (the file
`normativa.yaml` names; no `cambios_pendientes`) and `sources/otros/boe-rd-4-2010-eni.pdf`. Resolver:
`CourseCitations.build(...)._anchor(lesson, citation, 'es')` from `backend/`. In m04-l06 only the s6 hunk (l. 293–295)
was judged; the other hunks are session 5 items, checked in `lesson-fixes/m04/check.md`.

| # | Item | Lesson, lines | Faithful | Cited | Placed and scoped | Voice | Verdict | Reason |
|---|------|---------------|----------|-------|-------------------|-------|---------|--------|
| 1 | art. 23 RD 33/1986 beside art. 94.3 TREBEP (addition) | m04-l06, 293–295 | ✗ | ✓ | ✓ (note) | ✓ | FAIL | Art. 23 limits the suspension to «algunos de los delitos cometidos por los funcionarios públicos, contra el ejercicio de los derechos de la persona reconocidos por las Leyes y de los delitos de los funcionarios públicos, en el ejercicio de sus cargos, tipificados en los títulos II y VII del Libro segundo del Código Penal». The lesson shortens this to «alguno de los delitos de los funcionarios públicos tipificados en los títulos II y VII», dropping both qualifiers (the brief: keep the norm's words where shortening drops a condition; exam items quote these words). The sentence also drops the premise of the first rule: the expediente continues «hasta su resolución e imposición de la sanción si procediera» when the falta «puede ser constitutiva de delito o falta penal»; it now reads as an unconditional rule. Placement after art. 94.3 TREBEP is right, and both rules are stated without resolving the conflict. `art. 23 RD 33/1986` → `boe-a-1986-1216-art-23`. Note: the Fuentes line «RD 33/1986 …: arts. 1, 6, 7.1, …» does not list art. 23. «Por su parte» is not a blacklisted opener. |
| 2 | `boe-rd-4-2010-eni.pdf` citation form (citation form) | m06-l01, 29–30 | ✓ | ✓ | ✓ | ✓ | PASS | Only «, anexo» is removed from the parenthesis; the definition is unchanged. The PDF's glossary (anexo) reads: «Aplicación de fuentes abiertas: Aquella que se distribuye con una licencia que permite la libertad de ejecutarla, de conocer el código fuente, de modificarla o mejorarla y de redistribuir copias a otros usuarios.» The lesson keeps all four freedoms; nothing is wider. `fuente: \`boe-rd-4-2010-eni.pdf\`` → `fuente-boe-rd-4-2010-eni-pdf` (the form without backticks gives None, so the backticks are needed and present). The Fuentes list already names the file (l. 133). |

**Fix for item 1** (replace l. 293–295 with one line):

«Por su parte, el RD 33/1986 dispone que, si la falta puede ser constitutiva de delito, el expediente continúe hasta su resolución e imposición de la sanción si procediera, pero que se suspenda hasta que recaiga resolución judicial cuando los hechos pudieran ser constitutivos de alguno de los delitos cometidos por los funcionarios públicos contra el ejercicio de los derechos de la persona reconocidos por las Leyes y de los delitos de los funcionarios públicos en el ejercicio de sus cargos, tipificados en los títulos II y VII del libro segundo del Código Penal (art. 23 RD 33/1986).»

and add «23» to the RD 33/1986 line of the Fuentes list («… 20–21, 23, 29.1, …»).

**Not-done items:** the record lists none.

Counts: 2 items checked, 1 PASS, 1 FAIL (item 1, Faithful). Citations: 2 new or changed, both resolve.

## Re-check (coordinator edit)

Re-checked 2026-10-24 by verifier 2 against art. 23 RD 33/1986, opened in
`sources/normativa/BOE-A-1986-1216_rd-33-1986-regimen-disciplinario_1991-12-31.pdf` (`pdftotext -layout`, p. 8–9).

| # | Item | Lesson, lines | Faithful | Cited | Placed and scoped | Voice | Verdict | Reason |
|---|------|---------------|----------|-------|-------------------|-------|---------|--------|
| 1r | «Por su parte, el RD 33/1986 dispone…» (coordinator edit of item 1) | m04-l06, 293–298 | ✓ | ✓ | ✓ | ✓ | PASS | Both premises are now kept. Norm, first paragraph: «la presunta falta puede ser constitutiva de delito o falta penal … Ello no será obstáculo para que continúe la tramitación del expediente disciplinario hasta su resolución e imposición de la sanción si procediera»; second: «hechos que pudieran ser constitutivos de algunos de los delitos cometidos por los funcionarios públicos, contra el ejercicio de los derechos de la persona reconocidos por las Leyes y de los delitos de los funcionarios públicos, en el ejercicio de sus cargos, tipificados en los títulos II y VII del Libro segundo del Código Penal, deberá suspenderse la tramitación … hasta tanto recaiga resolución judicial». Both qualifiers and the títulos/libro are kept word for word (only commas and «algunos»→«alguno» change, no change of meaning). The instructor's duty to inform the authority for the Ministerio Fiscal is left out, which the TREBEP sentence just above covers in its own terms; nothing stated is wider than the norm. `art. 23 RD 33/1986` → `boe-a-1986-1216-art-23`. Placement right after art. 94.3 TREBEP, no conflict resolved. The sentence is long but carries one idea and keeps the norm's words, which the brief asks for where shortening drops a condition. |
| 1n | Normativa line, RD 33/1986 | m04-l06, 412–413 | ✓ | — | ✓ | ✓ | PASS | Now «arts. 1, 6, 7.1, 8, 14–17, 20–21, 23, 29.1, …»: art. 23 listed in numeric order; the lesson cites it (l. 298). |

Counts: 2 checked, 2 PASS, 0 FAIL. Item 1 of the first check is closed.

## m06-l02 (§3)

Blind check by verifier 2, 2026-10-27. Judged from `git diff HEAD -- content/age-administrativo-c1/es/lessons/m06-l02.md`
(one hunk, l. 69–71) and from `sources/otros/ms-win-varias-pantallas.html` itself (HTML tab panels read directly).
Resolver: `CourseCitations.build(...)._anchor('m06-l02', 'fuente: `ms-win-varias-pantallas.html`', 'es')` →
`fuente-ms-win-varias-pantallas-html`.

| # | Item | Lesson, lines | Faithful | Cited | Placed and scoped | Voice | Verdict | Reason |
|---|------|---------------|----------|-------|-------------------|-------|---------|--------|
| 3 | «Escala y diseño» orientation path removed; Windows 11 display options listed (correction) | m06-l02, 70–71 | ✓ (note) | ✓ | ✓ | ✓ | PASS | The removal is right: «Cambiar la orientación … vaya a Escala y diseño, a continuación elija su Orientación de Pantalla» sits in `<section id="tabpanel_1_windows-10">` (`hidden`), and the Windows 11 panel has no orientation text. The new list is the Windows 11 panel's «Cambiar las opciones de pantalla» links: «Cambiar el brillo y el color de la pantalla», «Cambiar la resolución, la escala y el diseño de la pantalla», «Cambiar la frecuencia de actualización de la pantalla», after «puede ajustar la configuración de cada una de ellas». Only the second clause of the sentence changed; the Windows+P list is untouched. |

Note (no verdict change): the page lists those links as general display options; it does not say that brightness in
particular is set per screen. «La configuración de cada pantalla se ajusta por separado: brillo y color, …» stays
within the page's «ajustar la configuración de cada una de ellas» followed by that list, so it passes. A stricter
wording, if the coordinator wants one: «La configuración de cada pantalla se ajusta por separado; las opciones de
pantalla son brillo y color, resolución, escala y diseño, y frecuencia de actualización (fuente:
`ms-win-varias-pantallas.html`).»

Counts (§3): 1 checked, 1 PASS, 0 FAIL.
