# Replacement brief, bloque VI (2026-10-30)

One replacement for `m06-l02-q350` (dropped: see its row in `bloque-vi/drops.tsv`). Read and follow
`bloque-vi/spec.md` (and what it tells you to read) and `s5-writer-brief.md` § «Replacements» and its rules; this page
says only what differs. Do not commit; do not edit lessons, content, tests, goldens, other drafts or `drops.tsv`.

- **File:** `bloque-vi/m06-l02.r1.draft.json` (a JSON list with one question, same fields as `m06-l02.draft.json`)
  plus `m06-l02.r1.writer-notes.md`. Id `m06-l02-q359`. Section «Copilot», tema VI.2, the same `covers` as q350.
- **Fact:** what Copilot in Excel for Microsoft 365 does, from `ms-excel-copilot.html` (the lesson cites it). Ask a new
  angle; do not reuse q350's stem or options. Every word of the keyed option must hold on the page as printed: the
  page lists «Generar datos y fórmulas» and «Crear gráficos, tablas dinámicas y formas» as separate items — do not
  merge them, and do not change «formas» into «fórmulas».
- **Citation:** `fuente: \`ms-excel-copilot.html\`; «<label>»`, where the label is the page's own sentence that holds
  the key, copied exactly from one paragraph or list item (six words or more, ending in «.», «:», «?» or «!»), so the
  solution panel shows that sentence.
- Run `tools/lint_drafts.py bloque-vi m06-l02.r1` and the anchor check (`_anchor` on your file) before hand-back;
  check `source_quote` against your text extraction of the page.

Final message: the stem with its keyed option and citation, anchor misses (0), lint result.
