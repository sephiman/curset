# Round D4, Part B — rule text verifier brief (Opus, blind; you did not write the text)

Inputs: the lesson `content/backend-in-depth/en/lessons/<lesson>.md` and `docs/_work/backend-in-depth/d4/<lesson>.items.tsv`
(the items new or changed this round: id, kind, section, text). Load the cited anchors one at a time from `backend/` with
`uv run python scripts/tech_sources.py show --course backend-in-depth SOURCE#ANCHOR`; a snippet's record is
`content/backend-in-depth/snippets/<lesson>/<File>.run.json`. Do NOT read the writer's notes, decisions or work files.
Never edit anything outside your verdict file `docs/_work/backend-in-depth/d4/<lesson>.verdicts.tsv`: one line per listed item,
`<id><TAB>pass` or `<id><TAB>fail-fact|fail-voice|fail-padding<TAB>reason` (≤ 15 words), ending with `checked/passed/failed`.

The kinds and their tests are those of `docs/backend-verification/d2/brief-verifier.md` (precise, X sentence, plain, row,
keypoint, judgement; voice; padding). In addition, for D4:
- The rule each added block states must be complete enough to compute an answer from: if a later generator would need a
  condition the sentences omit (a tie-break, a boundary, a default), say so in the reason of the precise item (`fail-fact`
  only when the sentence as written is wrong or misleading without that condition).
- A plain sentence that is a generalisation beyond the anchor ("always", "every", "never") the anchor does not make is `fail-fact`.
- Each block stays at about 150 words or fewer; a block well over that is `fail-padding` on the items that repeat.
Return at most five lines: counts and any systemic problem.
