# Writer brief — explanation layer (R4.11), course aeat-agentes-hacienda

You write ONLY `docs/age-verification/aeat/edition/explanation/<lesson>/draft.md`. You never edit a lesson file. Read
first: `docs/prose-voice.md` (the «never does» list is a hard constraint), the lesson itself, its «Lo que más cae» block, its
`asked` entry in `docs/age-verification/aeat/edition/budget.json`, and `content/aeat-agentes-hacienda/glossary.yaml`
(a term the glossary defines is used in that sense; invent no vocabulary: only terms that exist outside the course with the
same meaning). Spanish is Peninsular, addressing the reader as «tú» only where the voice calls for it (rules are stated flatly).

## What to write

1. `OVERVIEW` — 120–200 words, goes at the top of the lesson: what the tema covers, how its parts relate (the section order of
   the lesson), and what the exam has asked most, pointing at «Lo que más cae» by that name. Structure needs no citation;
   every legal statement in it carries its citation in parentheses, as the lesson does («art. 62.2 LGT»).
2. `AFTER <heading>` — for each `##`/`###` section that STATES RULES: one paragraph that opens «En pocas palabras.», 40–90
   words in total, plain Spanish: what the rule is for, when it applies, what changes if a condition fails, how it differs from
   its neighbour rule. It ends with, or carries, the citation of the rule it explains. It may paraphrase. It may not add, drop
   or soften a condition, a number, a plazo, an organ or an exception; every figure it mentions (digits or words: «seis meses»,
   «dos», «20 de noviembre») is exactly one the literal text of that section gives. Do not write «normalmente», «suele», «en
   general», «puede» where the text says «debe» or the reverse; do not generalise from one case to all.
   Sections that only list or define (a table of data, a list of documents, a definition) get NO paragraph: write
   `SKIP <heading> :: reason`. A `##` heading whose text is only subsections gets none either.
3. `NC <heading>` — a «No confundir» block (at most three per lesson INCLUDING those the lesson already has; count the
   `**No confundir.**` blocks in the file) only where two rules of this lesson are routinely confused (two plazos, two organs,
   two procedures, two recargos) and no block covers that pair. Two or three bullets, each bullet EXACTLY a sentence of the
   lesson (copy it verbatim, with its citation); no commentary. The block goes at the end of the section named.

## Format (the tool parses it)

```
=== OVERVIEW
text
=== AFTER ## Exact heading line from the lesson
En pocas palabras. text (art. 62.2 LGT).
=== AFTER ### Heading that occurs twice [#2]
...
=== NC ## Exact heading line
- sentence verbatim (art. X LGT).
- sentence verbatim (art. Y LGT).
=== SKIP ### Heading :: only a table of data
```
Every `##`/`###` heading of the lesson appears exactly once in the draft, as AFTER, NC (an NC may share a heading with an AFTER)
or SKIP — except those you leave out for the budget (then SKIP with reason «budget»). Headings are copied character for
character, including the `##`/`###`.

## Voice (the author, a trader-turned-teacher in Spanish; here a teacher of tax law)
One thing per sentence; the simplest exact word; state rules flatly; no fillers («cabe destacar», «es importante señalar»,
«en definitiva», «no obstante» as a tic, «a la hora de»); no rhetorical questions; no triads of adjectives; no «no solo… sino
también»; no closing line that sums up; no repeated openers across paragraphs (vary the second sentence's start; never start
a sentence with «Es…», «Eso…», «Son…», «Por eso…», «Así…», «Y…», «También es…»); no synonym rotation; no explaining a
metaphor (use none). No tax advice, no planning, no «te conviene».

## Check yourself
Run `uv run --project backend python docs/age-verification/aeat/edition/tools/explanation.py lint <lesson>` from the repository
root until it prints nothing. It checks lead-in, word range, a citation that resolves to a norm, figures present in the
section's literal text, fillers, split openers, NC bullets verbatim. It does not check meaning: you do. Before finishing, read
each paragraph against its section's literal sentences and ask: does it say anything they do not? did I drop a condition?

## Budget
Your lesson's headroom is given in your task. Fit the layer in it by choosing the sections with the most exam weight (the
`asked` articles and «Lo que más cae») and skipping the rest with reason «budget». Words of OVERVIEW and AFTER paragraphs count;
NC bullets are existing sentences and count as well when the block is new (their words are added).

## Report
Reply with: the number of paragraphs written, skipped (by reason), NC blocks, total layer words, and anything in the literal
text that looked wrong or unclear to you (do not fix it).
