# Verifier spec — C2 question bank, authored questions (round R3, 2026-11-07)

You verify questions written for `content/age-auxiliar-c2` (repo `/home/juanjo/PycharmProjects/curset`). You are
blind: you did not write them, and you do not read the writer's notes before your verdicts. Do not commit. Write only
your report and your lines in `drops.tsv`.

C1's verifier specs apply with every path read as `content/age-auxiliar-c2/…`, and their rulings stand:
`docs/age-verification/bank/bloque-ii/verify-spec.md` (norm temas: bloque I, II.1–II.4) and
`docs/age-verification/bank/bloque-vi/verify-spec.md` (ofimática, II.5–II.12, including the 2026-10-24 ruling: for
each distractor, name the page sentence that makes it wrong, and grep every saved page in `sources/otros/`). Where
they differ from this page, this page rules:

- **Check 4 (style) is the C2 checklist**, `docs/age-c2-exam-style.md` § 12, items 1–21 as they apply to the set.
  The C1 checklist does not apply. The C2 lengths are: bloque I stem 20–40 words; II.1–II.4 stem 20–55;
  ofimática 15–35, or up to 50 with a path or formula; options per items 14 and 21. Ofimática stems name the
  application with its version. «Excel 365» and «Microsoft Excel 365» both pass (ruling of this round).
- **Check 5 (not official)** compares against the C2 official pack of the tema,
  `docs/age-verification/c2/<bloque>/questions/<lesson>.md`, and the repeated questions of the guide § 10, with C1's
  «lightly reworded» ruling. Spelled out (coordinator, 2026-11-07): check 5 **fails** a question with the same stem
  and option set, or the same options re-ordered, or the same fact, angle and key **with an official distractor
  carried over** (even reworded). It **passes** a question with the same fact, angle and key whose distractors are
  all new: the writers were told to cover the official facts, and check 5 compares stem and options, not the fact.
- **Check 3** uses the C2 lesson: the lesson must cite the norm and article, or the page. Check it with
  `uv run python ../docs/age-verification/c2/bank/tools/check_draft.py <draft>` from `backend/`.
- Sources: `content/age-auxiliar-c2/sources/normativa/` (`pdftotext -layout`; the file `normativa.yaml` names, with
  its «Cambio pendiente» rule) and `content/age-auxiliar-c2/sources/otros/`. Open the text yourself. Do not trust
  `source_quote`.

Any FAIL drops the question. You do not fix it and do not propose a corrected one.

## Batches and report

A batch is up to 60 questions with the same cited unit or neighbouring ones, as the coordinator assigns. Report:
`docs/age-verification/c2/bank/<bloque>/verify/<lesson>.<batch>.md`, with C1's table:

| id | 1 key | 2 unique | 3 citation | 4 style | 5 not official | verdict | reason |
|---|---|---|---|---|---|---|---|

Then the summary: checked, PASS, and FAIL by first failing check. Append one line per FAIL to
`docs/age-verification/c2/bank/<bloque>/drops.tsv` (`id	tema	batch	check	reason`, tab-separated, append with `>>`,
never rewrite). Write the report after each batch. Final message: counts and the failing ids with their check.
