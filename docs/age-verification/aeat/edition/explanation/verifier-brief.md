# Blind verifier brief — explanation layer (R4.11)

Input: `docs/age-verification/aeat/edition/explanation/<lesson>/verify-input.md`. It holds, per KEY, an explanation paragraph (or
the lesson overview) and the text of the articles it cites, extracted from the consolidated PDF (page headers and footers
may leak into the text; ignore them). You do NOT see the lesson. Do not open the lesson file or the draft.

For each KEY decide PASS or FAIL against the cited article text only:
- FAIL if the paragraph says anything the cited articles do not say (a condition, number, plazo, organ, percentage, exception,
  consequence, or a legal statement attributed to an article that does not contain it);
- FAIL if it drops or softens a condition, number, plazo or exception so that the statement becomes false or lets the reader
  draw a wrong rule (a partial list presented as complete; «puede» for «debe» or the reverse; a rule stated without the
  condition that limits it; a generalisation across cases the article distinguishes);
- FAIL if a citation names an article that does not support the sentence it ends;
- FAIL if the reader would be left with a wrong idea even though each clause is true (say what the wrong idea is).
A paragraph may paraphrase and may be incomplete (it explains; it is not the rule), but what it asserts must be true and
sufficiently conditioned. For the OVERVIEW, check every legal statement; structure statements need no article.
Write `docs/age-verification/aeat/edition/explanation/<lesson>/<output>.md`: a table, one row per KEY, exactly
`| <key copied exactly> | PASS or FAIL | reason (one or two sentences; for FAIL, the exact words at fault and what the article says) |`.
Do not edit anything else. Reply with counts and the list of FAIL keys with reasons.
