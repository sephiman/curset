# Writer brief — explanation layer v2 (R4.11 second design), course aeat-agentes-hacienda

You write ONLY `docs/age-verification/aeat/edition/explanation/<lesson>/layer.md`. Never edit a lesson file. Read first
`docs/prose-voice.md` (the «never does» list is a hard constraint), the lesson, its «Lo que más cae», its `asked` entry in
`docs/age-verification/aeat/edition/budget.json`. Peninsular Spanish, no invented vocabulary (a term the glossary defines is used
in the glossary's sense). The overview and «No confundir» blocks already exist (or are not your job); you write, per
section that STATES RULES that can be applied to facts:

- `PQ:` one line, two to four questions the section answers, in the order the text answers them. Questions only, no statement.
  Example: `PQ: ¿Cuándo vence el plazo de pago de una liquidación notificada el día 10? ¿Qué pasa si el último día es sábado?`
- `CASO:` ONE concrete case, 40–80 words, one line of text: fictional people (first names), every date and amount stated,
  the main rule of the section applied step by step to a result, EACH STEP with its own citation in parentheses
  (`(art. 62.2 LGT)`). Where the rule has a condition that changes the result, the case says what would happen without it,
  also cited. Use only rules the section's literal text states, nothing outside it (no extra law, no invented figures
  except the case's own facts). Check dates against a calendar (2026–2027: weekday!), do the arithmetic. Write the case so that
  the section's literal rule is easier to apply: facts first, then the steps, then the result. Plain statements, past or
  present tense; no «imagina que», no rhetorical questions.
- `PARA:` (rare) one sentence, ONLY when the norm's own preámbulo/exposición de motivos states the purpose of this rule:
  quote or follow it closely and cite it as `(preámbulo LGT)` or `(exposición de motivos LGT)`. Find it with `pdftotext` on the
  norm's PDF (path in `content/aeat-agentes-hacienda/normativa.yaml`/`source-index.json`). If you cannot find it in the text,
  write nothing. A purpose you know but the preámbulo does not say is NOT allowed.
- Sections that only define or list get nothing: `SKIP ## Heading :: reason`. Sections with no applicable rule (pure
  organisation, history) likewise. Prefer sections with the most exam weight; the budget is given in your task.

Format:
```
=== SECTION ## Exact heading line from the lesson
PQ: ¿…? ¿…?
CASO: …
PARA: …
=== SECTION ### Heading that occurs twice [#2]
...
=== SKIP ### Heading :: only a table of data
```
Every `##`/`###` heading appears exactly once (SECTION or SKIP). Headings character for character. One line per field.

Voice: one thing per sentence; simplest exact word; flat statements; no fillers («cabe destacar», «en definitiva»…); no
rhetorical questions in CASO/PARA; no triads; no «no solo… sino»; never start a sentence with «Es…», «Eso…», «Son…», «Por
eso…», «Así…», «Y…»; no summary closers. Facts in the case are your own invention but every rule is the text's.

Check: `uv run --project backend python docs/age-verification/aeat/edition/tools/layer.py lint <lesson>` until it prints nothing.
Then re-read each CASO against the cited text: result right? a condition missing? anything the articles do not say? Reply
with counts of sections written / skipped.
