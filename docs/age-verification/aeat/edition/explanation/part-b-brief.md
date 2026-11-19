# Part B writer brief — explanation layer v2 (R4.11), course aeat-agentes-hacienda

You write, per lesson assigned, in `docs/age-verification/aeat/edition/explanation/<lesson>/`:
1. `draft.md` (only if the lesson has no OVERVIEW yet; the pilot lessons m03-l09, m03-l13, m02-l03 already have theirs and their
   «No confundir» blocks — leave those): an `=== OVERVIEW` (120–200 words, points at «Lo que más cae» by that name, every legal
   statement cited) and up to three `=== NC ## Heading` blocks (count those the lesson already has; only where two rules of the
   lesson are routinely confused and no block exists; each bullet EXACTLY a lesson sentence, verbatim with citation). Format and
   rules: `docs/age-verification/aeat/edition/explanation/writer-brief.md` items 1 and 3 and its Format and Voice sections (ignore
   its AFTER/«En pocas palabras» part: that design is dropped). Lint: `uv run --project backend python
   docs/age-verification/aeat/edition/tools/explanation.py lint <lesson>` (it will not complain about missing AFTER entries).
2. `layer.md` (format and field rules in `layer-writer-brief.md`: PQ, CASO, PARA, SKIP), with the TIGHTENED case rules below.
   Lint: `uv run --project backend python docs/age-verification/aeat/edition/tools/layer.py lint <lesson>`.
Read first: `docs/prose-voice.md` (hard constraint), the lesson, its «Lo que más cae», `budget.json` `asked`, and the lesson's
budget in `explanation/budget-v2.json` (`cases_words` = the most words all your PQ + CASO + PARA lines (lead words included) and NC
blocks together may add; 0 = write only what the lesson still lacks: overview). Put cases first on the sections with the most
exam weight (the `asked` articles). Every `##`/`###` heading appears exactly once in layer.md (SECTION or SKIP, reason «budget»
when the words run out). A section that only defines or lists, or has no rule to apply, is SKIP.

## Tightened case rules
- A case rests on the text of ONE article (or one article and the cómputo rule it needs, e.g. art. 30 LPAC for días hábiles). It
  applies what that text states and nothing else. No contrast step («qué pasaría sin…») unless the article itself states the contrary case.
- Modal verbs are the article's own: «podrá» stays a possibility, «deberá» an obligation; nothing is called automatic unless the
  text says so.
- Every source of a rule that the article names is named («ley», «Derecho de la Unión Europea», «tratado»…); never shorten to one.
- Plazos are computed with the rule for their unit (días hábiles — no sábados, domingos ni festivos —, naturales, meses de fecha
  a fecha) and the calendar is stated: say the weekday of every date that matters, and compute it (2026–2027 calendar).
- The situation must be one the article's wording covers LITERALLY; if in doubt, pick the plainest case.
- 40–80 words, one line, fictional first names, every date and amount stated, each step with its own citation `(art. N NORM)`.
  Lint checks length and citations, not meaning: re-read each case against the cited text for (a) result, (b) a condition missing, (c) anything the
  articles do not say.

## PARA (Para qué sirve) — only where the norm's own preámbulo / exposición de motivos states the purpose
Find the preámbulo with `pdftotext -layout <norm pdf> -` (pdf paths in `content/aeat-agentes-hacienda/source-index.json`/`normativa.yaml`);
read the text before «Artículo 1». If it states the purpose of this rule, write one sentence that quotes or closely follows it,
ending `(preámbulo LGT)` or `(exposición de motivos LGT)`; if not, no PARA. At most one or two per lesson; never a purpose from memory.

Reply with: sections / PQ lines / cases / PARA lines, words added, and anything doubtful.
