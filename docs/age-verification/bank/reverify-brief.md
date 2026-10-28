# Re-verification brief (session 5, 2026-10-23)

You re-verify questions that a Haiku verifier passed. You are blind: do **not** open any `*.verify*.md` report and do
not read `drops.tsv` or the writer notes; you may only append to `drops.tsv`. Your spec is
`docs/age-verification/bank/bloque-ii/verify-spec.md` (read it whole, rulings included) and the style guide it names.
Apply its five checks to each id of your batch, against the cited text you open yourself:
(1) key correct by the cited text; (2) exactly one option correct, under every norm in force; (3) the citation contains
the answer and the lesson cites it; (4) style checklist; (5) not an official question copied or lightly reworded.

Your batch is in `docs/age-verification/bank/reverify-plan.json` (find your lesson and batch name). The draft for a
bloque IV lesson is `bloque-iv/<lesson>.draft.json`; for bloque V `bloque-v/<lesson>.draft.json`. Write the report as
`<bloque-folder>/<lesson>.<batch>.md` (table: id | 1 | 2 | 3 | 4 | 5 | verdict | reason; then counts) and append one
line per FAIL to `<bloque-folder>/drops.tsv` (`id	tema	batch	check	reason`, batch `<lesson>.<batch>`, `>>` only).
Final message: checked, PASS, FAIL by check, failing ids.

Keep any extracted text or script in your own scratchpad subfolder named after your batch (e.g. `<scratchpad>/m04-l06-reverify-4/`); other agents share the scratchpad.
