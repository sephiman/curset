# Fixer brief — rewrite once (R4.11 second design)

Per lesson, `explanation/<lesson>/fix-brief.md` lists the keys to rewrite, each with its current text, a blind verifier's reason (it
checked the text against the cited articles) and/or a student reader's reason. Rewrite each listed key ONCE, in the file where it lives:
- `caso:…`, `pq:…`, `para:…` keys: the one-line field in `explanation/<lesson>/layer.md` (CASO:/PARA:);
- `overview`: the OVERVIEW block in `explanation/<lesson>/draft.md` (120–200 words, every legal statement cited; fix exactly the fault named).
Rules: the tightened case rules in `part-b-brief.md` (one article + cómputo rule; the article's own modal verbs; every source named;
plazos by their unit's rule with weekdays; literal coverage; 40–80 words; each step cited). Fix the fault the verifier names by reading the
article text yourself (`uv run --project backend python docs/age-verification/aeat/edition/tools/article_text.py <lesson>` gives the lesson's
cited articles; for another article use its PDF). If the reader's reason asks for something the article cannot back (purpose, extra context),
ignore that part. If a case cannot be made faithful within 80 words, keep the key but write in `explanation/<lesson>/cut-keys.txt` one more
line with the key (the case is then dropped). Do not edit lesson files. Run `layer.py lint <lesson>` (and `explanation.py lint` for an overview).
Reply with, per lesson, how many keys rewritten and how many cut.
