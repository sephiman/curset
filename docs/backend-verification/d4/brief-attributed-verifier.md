# D4 Part D verifier brief — blind check of attributed questions (Opus; you did not write them)

Load once: `docs/prose-voice.md`, `docs/backend-question-style.md`, and amendment 17 (the last amendment of
`docs/backend-in-depth-course-requirements.md`, which allows a question keyed to what a named, stored source states).
Do NOT read the writer brief, `checks.tsv`, `decisions.tsv` or any writer notes. Never edit questions or lessons.

Inputs per lesson in `docs/_work/backend-in-depth/d4/attr/`: `<lesson>.questions.json` and `<lesson>.refutations.yaml`
(the map only tells you where to look). Load anchors from `backend/` with
`uv run python scripts/tech_sources.py show --course backend-in-depth SOURCE#ANCHOR` (`list … SOURCE` lists them).
Read the lesson's `:::judgement` blocks (`grep -n -A8 ':::judgement' content/backend-in-depth/en/lessons/<lesson>.md`).

A question passes only when every point holds:

1. Stem: `According to AUTHOR in WORK, …`; AUTHOR and WORK match what the stored page credits; 15–40 words; it asks
   what the source states, not what is true.
2. Key: restates a stored sentence of that source in the same sense; nothing added, no two sentences merged, no
   qualifier dropped. It does not contradict what the lesson's judgement block attributes to the source.
3. Each wrong option: contradicted by its own stored sentence of the same source (read the whole relevant anchor, not
   only the quoted sentence). Fails if the source is merely silent, if another sentence of the source supports the option,
   if a reader of the source could defend it, or if one sentence carries two options.
4. Explanation: one sentence for the key and one per wrong option, naming it by content; every sentence reports what the
   source states (attribution verb); nothing presents the judgement as a fact of the field; no option letters. Extract,
   if present, is literal text of the first cited anchor.
5. Options: same shape, similar length, no filler words added to reach a length; the key not given away by wording.
6. Voice: `docs/prose-voice.md` "never does" list and blacklist; code-like tokens in inline code.

Write `docs/_work/backend-in-depth/d4/attr/<lesson>.verdicts.tsv`: one line per question, `<qid>\tpass` or
`<qid>\tfail\t<reason of at most fifteen words naming the point>`, then a last line `checked N passed P failed F`.
Return at most one line per lesson with the counts, plus one line on any systemic problem.
