# Blind excerpt check — age-auxiliar-c2 (round R3, 2026-11-10)

After a question is answered, the solution panel shows an excerpt of the source the question cites, extracted by a
program from the course's saved copy (`content/age-auxiliar-c2/sources/otros/` or `sources/normativa/`). The check
measures whether that excerpt shows the fact the key rests on. It is C1's full pass
(`docs/age-verification/excerpts/full/spec.md`) and re-citation brief (`full/recite-writer-brief.md`) in one step.

## Input

`<bloque>/batch-NN.jsonl`, one JSON object per line: `n`, `key` (question id), `prompt`, `options` (`correct: true`
marks the key), `explanation`, `citation`, `excerpt_heading`, `excerpt_text` (what the panel shows), `excerpt_full`,
`flag` (`fallback`: the extractor found no paragraph matching the citation's label and fell back to the best match
for the explanation), `none` (the build found no excerpt at all; then `excerpt_text` is null), `source_file`.

## Per item

1. **Verdict.** Does `excerpt_text` contain the fact the key rests on, i.e. the text a reader needs to see that the
   marked option is right? **yes** / **no** (no excerpt counts as no). Garbled spacing copied from the page does not
   matter.
2. **For no:** open `source_file` (HTML: read the text; `.pdf`: `pdftotext -layout`; `.txt`: as is) and give
   - **label**: text copied **exactly** from the saved file that, used as the citation's label, makes the panel show
     the fact. Either one sentence of one paragraph, six words or more, ending in «.», «:», «?» or «!», character for
     character as the file shows it (keep odd spacing), or one table row written as its cells joined by « — »
     exactly as they read. No «» characters inside. The paragraph (or row) that holds the label must contain the
     fact **on its own**: do not stretch;
   - or **none: <reason>**, when the fact is spread over two or more paragraphs, rows or list items so that no single
     one holds it, sits only in a heading, or is **not on the page** at all. Say which, in one line.
3. **Flags**, whatever the verdict: excerpt text that is garbled (words run together, page furniture inside), or an
   excerpt that is not the unit its heading names.

Judge the question as written: you do not decide whether the key is right, only whether the excerpt (or a label)
shows the fact the explanation gives for it. If the page does not state the fact at all, that is **none: not on
page**, and say so plainly: the coordinator records it.

Work from the item and the cited file only. Do not read code, other reports, the ledger or anything else.

## Output

`<bloque>/report-NN.md` (same number as the batch): a table

`n | key | verdict | label or none: reason | flags`

then the counts: items, yes, no with a label, no with none (by reason). Final message: the counts only.

## Norm citations (bloque I, 2026-11-10)

When the item cites a norm (`art. …`, `disposición …`, `anexo …`), the panel shows that unit of the norm (`excerpt_text`,
with the whole unit in `excerpt_full`). Judge `excerpt_text` as above. For a **no**, instead of a label give:

- **cite: <citation>**: the citation, written as the item's own citation is written (same norm name), that makes
  the panel show the fact: a narrower paragraph or letter of the same article («art. 23.2 Ley 19/2013»), or another
  article of the same norm when the fact is there and the explanation already rests on it. Only when that unit
  alone holds what the key rests on; or
- **none: <reason>** as above (the fact needs two articles, sits only in `excerpt_full` beyond the excerpt's cut, or
  is not in the norm).
