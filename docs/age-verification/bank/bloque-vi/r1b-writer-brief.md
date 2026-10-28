# Replacement brief, bloque VI (2026-10-30, second)

One replacement for `m06-l03-q219` (dropped: see its row in `bloque-vi/drops.tsv`). Read and follow
`bloque-vi/spec.md` (and what it tells you to read) and `s5-writer-brief.md` § «Replacements» and its rules; this page
says only what differs. Do not commit; do not edit lessons, content, tests, goldens, other drafts or `drops.tsv`.

- **File:** `bloque-vi/m06-l03.r1.draft.json` (a JSON list with one question, same fields as `m06-l03.draft.json`)
  plus `m06-l03.r1.writer-notes.md`. Id `m06-l03-q276`. Section «"Este equipo" y "Acceso rápido"» as q219 has it
  (copy the exact `section` string from q219), tema VI.3, `covers` as q219.
- **Fact:** what the Acerca de page of Windows 11 shows, from `ms-win-info-dispositivo.html`. New angle; do not reuse
  q219's stem or options. The fault to avoid: the page's «Especificaciones del dispositivo» list includes «Si el
  dispositivo ejecuta una versión de Windows de 32 o 64 bits», so no distractor may mention the version, the bitness
  or anything that list holds unless the stem asks about a different section that excludes it. Every distractor needs a
  page sentence that makes it wrong.
- **Citation:** `fuente: \`ms-win-info-dispositivo.html\`; «<label>»`, where the label is the page's own sentence
  that holds the key, copied exactly from one paragraph or list item (six words or more, ending in «.», «:», «?» or
  «!»), so the solution panel shows that sentence (a «…:» lead-in brings its list).
- Run `tools/lint_drafts.py bloque-vi m06-l03.r1` and the anchor check (`_anchor` on your file) before hand-back;
  check `source_quote` against your text extraction of the page.

Final message: the stem with its keyed option and citation, anchor misses (0), lint result.
