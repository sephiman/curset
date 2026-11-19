# Concept readers — brief (edition step 1, priority b)

You choose, for one lesson at a time, which already-verified sentences the shrunken lesson must keep so that every concept
the programme names is taught. You write no prose and change no file but your output JSON.

Input per lesson: `docs/age-verification/aeat/edition/outline/<lesson>.txt`. First line: the budget, the words already kept
by rule, the headroom. Then the programme sentences with their concepts. Then the lesson in reading order: headings, one
line per sentence (`id origin words | first 18 words`) and one line per esquema (`[esquema N] kind «title» rows`).
Origin letters: H pre-R2d text, C R2b restore / confirmed review item, N «No confundir», G gap fill, K range coverage,
W reworded; a trailing `A` means an official question rests on it. Sentences with `A` or `C` are kept anyway and count as
coverage. The full text of a sentence is in `docs/age-verification/aeat/pool/<lesson>.md` (grep the id's first words);
open it whenever the first 18 words do not tell you the role of the sentence.

For every concept of every programme sentence, pick the **fewest** sentences that together say: what it is, the rule, its
conditions, its exceptions, its plazos, the organ that acts or decides. Skip a role the concept does not have. If an
`A`/`C`/kept sentence already says it, pick nothing. Prefer the sentence that states the rule whole over three that
fragment it; prefer H sentences over K/G ones when both say the same. Do not pick background, history, transitional rules,
cross-references or examples. Never pick a sentence that depends on a neighbour you are not also picking («dicho plazo»,
«el apartado anterior», «en este caso»): pick the neighbour too. A list item needs its lead-in: pick the lead-in.

A complete legal enumeration of a concept in scope (exemptions, infractions, organs, requisites, motives) is an esquema:
list its index under `esquemas` and do not pick its prose. Do not list esquemas that only repeat one paragraph.

Aim to stay inside the headroom; the concepts' essentials come first even if that overruns it, and say so in `note`.
A concept the lesson cannot teach from verified sentences goes in `gaps` (do not invent).

Rank within a concept: 1 = indispensable, 2 = completes, 3 = nice to have. Roles: what, rule, condition, exception, plazo,
organ.

Output, one file per lesson, `docs/age-verification/aeat/edition/b/<lesson>.json`:

```json
{"picks": [{"concept": "...", "id": "0b377ad1b0", "role": "rule", "rank": 1}],
 "esquemas": [{"index": 3, "concept": "..."}],
 "gaps": ["concept: why"],
 "note": "words picked ≈ N; headroom H"}
```

Ids must exist in the outline. Process the lessons you were given in order; write each file as soon as the lesson is done.
Final reply: one line per lesson with picks, esquemas and gaps counts. Spanish content stays untouched; English output only.
