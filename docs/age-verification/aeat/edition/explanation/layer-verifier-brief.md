# Blind verifier brief — cases (R4.11 second design)

Input: `docs/age-verification/aeat/edition/explanation/<lesson>/layer-verify-input.md`: per KEY a CASO (a fictional case with facts and
steps, each step citing an article) and the text of the cited articles (page headers/footers may leak in; ignore them). You do
NOT see the lesson; do not open it or any draft.

For each KEY recompute the case yourself from the stated facts and the cited article text, then decide PASS or FAIL:
- FAIL if the result or any intermediate date/amount/plazo is wrong (check weekdays with a calendar: compute them);
- FAIL if a step's citation does not support the step;
- FAIL if a condition that changes the result is missing, or the «without the condition» branch is wrong;
- FAIL if the case says something the articles do not support (a rule, organ, figure, consequence not in them);
- FAIL if the case, though each clause is true, would leave the reader with a wrong rule (say which).
A PARA key: PASS only if its sentence quotes or closely follows the norm's own preámbulo/exposición de motivos (find it in the
PDF yourself if the input includes it; if the input has no such text, FAIL).
Write `<out>` (path given in your task): a table, one row per KEY, exactly `| <key copied exactly> | PASS or FAIL | reason |`
(for FAIL: the exact words at fault and what the article says). Reply with counts and the FAIL keys with reasons.
