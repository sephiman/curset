# D2 verifier brief — blind check (Opus; you did not write the text)

Inputs: the lesson file, `docs/_work/backend-in-depth/d2/<lesson>.items.tsv` (the items new or changed this round: id, kind,
section, text), the lesson's new question candidates and refutation map if any, the diagram map if any. Load the cited anchors
one at a time from `backend/` with `uv run python scripts/tech_sources.py show --course backend-in-depth SOURCE#ANCHOR`.
Do NOT read the writer's gap list, notes or decisions. Never edit lessons. Write the verdict file
`docs/_work/backend-in-depth/d2/<lesson>.verdicts.tsv`, one line per listed item: `<id><TAB>pass` or
`<id><TAB>fail-fact<TAB>reason` / `fail-voice` / `fail-padding` (reason ≤ 15 words), ending with `checked/passed/failed` counts.

Per kind:
- `precise` (F): the cited anchors of the pinned version state exactly this claim (same sense, same numbers, same qualifiers);
  nothing added, nothing merged from two items. Version-specific facts name the version. `fail-fact` otherwise.
- `precise` sentence about a snippet (X): matches the snippet's `.run.json` stdout exactly.
- `plain` (amendment 14): introduces no fact that a precise sentence of the same section does not state; says what it is, why
  it matters or what goes wrong without it; promises nothing the section does not deliver. A plain sentence carrying an unstated
  fact is `fail-fact`.
- `row`: the cited anchor states the row's claim. `keypoint`: restates a fact present in the lesson. `judgement`: faithful to the
  attributed source (check the attribution, not the truth); text outside the judgement of the source is `fail-fact`.
- `diagram`: every node, edge, label and `when` restates a sentence of the lesson (use the map, but check against the
  sentences, not the map); anything the lesson does not say is `fail-fact`; a vague or misleading drawing is `fail-voice`.
- Voice (`fail-voice`): `docs/prose-voice.md` "never does" list and its blacklist: fillers, rhetorical questions, triads,
  "not only… but also", summary/uplift closers, announcing sentences, stacked hedges, repeated paragraph openers, explaining a
  metaphor, synonym rotation, coined vocabulary.
- `fail-padding` (amendment 15): the sentence repeats a fact already stated in the lesson in other words, or adds nothing.
- Questions: question-style sections 1–3 and 6; each wrong option contradicted by its own cited sentence; line format of
  `docs/backend-question-style.md` section 6 (`<qid> pass` / `<qid> fail <reason>`).
Return at most five lines: counts and any systemic problem.
