# Blind verification — audit 2026-11 replacements, batch A (2026-11-05)

Specs: `bank/bloque-vi/verify-spec.md` with its rulings (bloque VI); `bank/bloque-ii/verify-spec.md` (bloque I re-cites).
Pages extracted from `content/age-administrativo-c1/sources/otros/` (HTML to text, PDFs with `pdftotext -layout`); every
saved page grepped for distractor-making text. Anchors: `check_anchors.py bloque-vi m06` and `_anchor` on the new
m01-l06 citation, 0 misses. `fuentes.yaml`: all cited pages have no `comprobacion` except `ms-outlook-grupo-enviar.html`
(«Los demás hechos citados se mantienen»; q366's fact is not the changed label), and the new
`transparencia-planes-accion_2026-11-05.html` has none. Duplicate test against kept questions (not in `drops.tsv`) of
`m06-l04.draft.json` / `m06-l07.draft.json`.

| id | 1 | 2 | 3 | 4 | 5 | verdict | reason |
|---|---|---|---|---|---|---|---|
| m06-l04-q400 | PASS | PASS | PASS | PASS | FAIL | FAIL | Duplicates the angle of kept m06-l04-q142 («¿en cuál de las siguientes plantillas se guarda una macro para que esté disponible en todos los documentos futuros?», key Normal.dotm): same fact, same key, same question. Only the distractor set differs |
| m06-l04-q401 | PASS | PASS | PASS | PASS | PASS | PASS | «Las notas al pie aparecen en la parte inferior de la página y las notas al final se muestran al final del documento»; no saved page puts notes in a side pane |
| m06-l04-q402 | PASS | PASS | PASS | PASS | PASS | PASS | Windows table «Desplazarse por una tabla»: Mayús+TAB anterior, Tecla TAB siguiente, Alt+Inicio primera, Alt+Fin última celda de la fila. Kept q237 asks the next cell (Tab), a different fact |
| m06-l04-q403 | PASS | PASS | PASS | PASS | PASS | PASS | Each type's row on `ms-word-salto-seccion.html`; no kept question asks Página impar |
| m06-l04-q404 | PASS | PASS | PASS | PASS | PASS | PASS | Definition sentence of `ms-word-indice.html`; TOC distractor ruled out by `ms-word-tabla-contenido.html` «se basa en los títulos del documento» (cited by m06-l04). The kept set has no index-definition question (q157 dropped); conv2024_A P1 55 is the reverse angle with no official distractor carried |
| m06-l04-q405 | PASS | PASS | PASS | PASS | PASS | PASS | «Al seleccionar Expandido o Condensado, se modifica el espaciado entre todas las letras seleccionadas en la misma cantidad. Interletraje modifica el espaciado entre pares de letras concretos»; line spacing is ruled out by «Cambiar el interlineado». Kept q202 asks which option widens evenly (Expandido); this question asks the contrast, a different angle |
| m06-l04-q406 | PASS | PASS | PASS | PASS | PASS | PASS | «Página siguiente … inicia la nueva sección en la página siguiente»; siblings from their own rows. Its near-twin q229 is dropped, not kept |
| m06-l07-q366 | PASS | FAIL | PASS | FAIL | PASS | FAIL | The stem does not say whether the group is public or private. The same page says «Para un grupo privado, solo los miembros del grupo pueden participar en la conversación», so «Solo los miembros del grupo» is defensible for a private group (kept q037 teaches exactly that). The explanation's «limita … la participación …, pero no el inicio» is stated on no page |
| m01-l06-q025 | PASS | PASS | PASS | PASS | — | PASS (re-cite) | New page: «I Plan de Gobierno Abierto 2012-2014», «II … 2014-2016», «III … 2017-2019». The explanation's 2011 OGP entry is on `transparencia-v-plan.pdf` (cited by m01-l06): «Desde nuestra incorporación en 2011 a la Alianza…» |
| m01-l06-q026 | PASS | PASS | PASS | PASS | — | PASS (re-cite) | «III Plan de Gobierno Abierto 2017-2019»; the page lists every plan period (I–V), so 2016-2018 and 2018-2020 match none |
| m01-l06-q027 | PASS | PASS | PASS | PASS | — | PASS (re-cite) | «IV Plan de Gobierno Abierto 2020-2024»; «V Plan de Gobierno Abierto 2025-2029» on the same page. The stem's «29 de octubre de 2020» is not on the new page but is on `transparencia-iv-plan.pdf` (no `comprobacion`; m01-l06 cites it), so the key does not depend on it |

## Summary

- Checked: 8 new questions + 3 re-cites.
- New questions: 6 PASS, 2 FAIL. First failing check: m06-l04-q400 on not official (duplicate angle, by analogy); m06-l07-q366 on unique.
- Re-cites: 3 PASS (q025, q026, q027 rest on `transparencia-planes-accion_2026-11-05.html`).
- Drops appended to `bank/bloque-vi/drops.tsv` (batch `audit-2026-11.replacements`): q400, q366.

## Notes (no verdict change)

- q400, q401, q402 and q403 put a body sentence in the citation label, not the page heading the writer spec asks for. The anchors resolve, so check 3 passes.
- q400 is tagged `stem_form: cual`, but its stem is a direct «¿qué…?» question.
- q401 rules out «panel lateral» and q404 rules out «comentarios…» and «notas…» with «la página solo habla de…». That reads like silence, but the reason underneath is the positive sentence (footnotes «aparecen en la parte inferior de la página»; the index definition). I passed them on that basis.
- q366: its option set repeats three options of kept q038 («Cualquier persona de la organización», «Solo los propietarios del grupo», «Solo los miembros del grupo») for a different fact. That would not have failed check 5 by itself.
