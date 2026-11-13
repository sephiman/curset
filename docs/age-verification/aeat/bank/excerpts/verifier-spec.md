# Excerpt verification — AEAT bank (blind)

Each question of `aeat-agentes-hacienda` shows, after it is answered, an excerpt of the norm it cites (extracted by a program from the course's
own copies of the sources). You measure the extractor, not the question. Read `docs/age-verification/excerpts/verifier-spec.md` for the
verdicts (yes / full-only / no, plus the flags for garbled text and for an excerpt that is not the unit its heading names): it applies as written
(there, «C1» paths read as `content/aeat-agentes-hacienda/sources/…`).

## Input and output

Batches: `docs/age-verification/aeat/bank/excerpts/batches/batch-NN.jsonl`, one JSON object per line (fields as the platform spec, plus `none`: the
extractor's reason when it found no excerpt, and `source_file`). Output per batch, written as soon as the batch is done:
`docs/age-verification/aeat/bank/excerpts/reports/report-NN.md`:

```
# Excerpt check — batch NN

| n | key | verdict | note |
|---|---|---|---|
| 1 | m01-l01-q0001 | yes | |
| 2 | m03-l02-q0042 | none-ok | the Orden's apartado primero.2 is not a heading the extractor can find; no excerpt possible |
```

Verdicts: `yes`, `full-only`, `no` (say what the excerpt shows instead and, if you can, the paragraph label or «cite: <citation>» that would
hold the fact), `none-ok` (the extractor found no excerpt and you agree none can be shown: say why), `none-miss` (it found none but the source
has the fact: give the file and the paragraph). Judge from the item and the source file, never from the extractor's code. At the end of each
report, a short list of misses and flags by cause. Do not edit any content file. Do not commit.
