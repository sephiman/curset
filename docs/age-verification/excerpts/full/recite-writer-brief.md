# Re-citation brief (writer, 2026-10-30)

Each item of `recite-writer-input.jsonl` is a question whose solution panel shows an excerpt of the page it cites
that does not hold the fact its key rests on. A verifier found where the fact is (`verifier_where`). Your job: give
the **label** that makes the panel show that fact. Do not change the question, the key or the file it cites.

A label is text copied **exactly** from the saved page `content/age-administrativo-c1/sources/otros/<file>` (the file
in `citation`), with these rules:

1. One sentence of one paragraph, of six words or more, ending in «.», «:», «?» or «!» — copied character for
   character as the page shows it (keep its odd spacing such as «Configuración , »), or
2. one table row, written as its cells joined by « — » («Ctrl+J — Abrir Descargas»), exactly as the cells read.
3. No «» characters in the label.

The panel will show the paragraph (or row, with the table's header row) that contains the label. If the fact the key
rests on is spread over two or more paragraphs, rows or list items so that no single paragraph or row holds it, or the
page holds it only in a heading, answer **none** with a one-line reason. Do not stretch: the shown paragraph must
contain the fact on its own.

Output (returned as text): one line per item, `n<TAB>label` or `n<TAB>none: reason`.
