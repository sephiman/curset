# D4 Part D writer brief — attributed questions on judgement content (amendment 17)

You are a Sonnet writer. You take the lessons the coordinator names, one after another, reusing your loaded context.
Never commit; never run git stash, checkout, reset or restore. Never edit lessons, exercises or `course.yaml`.

Load once: `CLAUDE.md`, `docs/prose-voice.md` (its "never does" list is a hard constraint), `docs/backend-question-style.md`,
`docs/backend-verification/s1/contracts.md`, and in `docs/backend-in-depth-course-requirements.md` section 4 and
amendment 17 (the last one; it overrides "J is never the key"). Read nothing else except the lesson's `:::judgement`
blocks and the anchors you fetch.

Work files go to `docs/_work/backend-in-depth/d4/attr/` (git-ignored). Run tools from `backend/`:
`uv run python scripts/tech_sources.py list --course backend-in-depth SOURCE` (anchors with sizes) and
`... show --course backend-in-depth SOURCE#ANCHOR` (one anchor's text; it also says whether extracts are allowed).

## Per lesson

1. `grep -n -A8 ':::judgement' content/backend-in-depth/en/lessons/<lesson>.md`: the judgement blocks and their `ref`
   sources. Only those sources may back a question. A block with no `ref` backs none.
2. For each such source, `list` it. Use it only if it is stored in full: the anchors hold the body of the work (not a
   cookie wall, a teaser, a table of contents or a page cut short). Read the anchors the judgement block draws on, then
   the others you need for refutations.
3. Write candidates (at most 8 per lesson, fewer is normal, zero is acceptable). A candidate exists only when:
   - **Key** (amendment 17 c): restates one stored sentence of the source, in its sense, nothing added, two sentences
     never merged. It is a point the lesson's judgement block attributes to that source, or one beside it in the same
     anchor and on the same topic.
   - **Three wrong options** (17 d): each contradicted by its own stored sentence of the **same source** (any anchor of
     it). Contradicted means the source states the opposite or something incompatible. An option the source merely does
     not mention is forbidden. An option the source supports elsewhere, or that a reader of the source could defend, is
     forbidden. One sentence never refutes two options; `exclusive` is not used in this round. If you cannot find three,
     do not write the question.
   - **Stem** (17 b): `According to AUTHOR in WORK, …?` — AUTHOR is the person (or, when the work names no person, the
     organisation) the stored page credits; WORK is the title of the article, chapter or handbook page as the page gives
     it. 15 to 40 words in all. The question asks what the source states or recommends; it never asks what is true.
   - **Options** (round rule): same grammatical shape, similar length (the shortest at least 60 % of the longest, in
     characters), and the key is the longest option in at most 40 % of the lesson's questions. Plan the four lengths
     while choosing the options, before writing the explanation. No filler words to reach a length ("in general",
     "typically", "as needed", restated context). A candidate that cannot be balanced without filler is not written.
   - **Explanation** (17 e): one sentence for the key, then one sentence per wrong option naming it by its content and
     giving the source's sentence that contradicts it. Every sentence reports the source ("Nygard writes that …",
     "The page recommends …"); none states the judgement as a fact of the field. Never refers to an option by letter.
   - **Citation**: `"src#anchor"` of the key's sentence first, then the anchors of the refuting sentences, `; ` between.
     **Extract**: a literal substring of the key's anchor when `show` says extracts are allowed, else `null`.
   - Identifiers, headers, annotations, commands and the like are inline code (question-style section 7). No
     near-duplicates within the lesson or with its published questions (`content/backend-in-depth/exercises/<lesson>-ex-*.yaml`).
4. Files: `d4/attr/<lesson>.questions.json` — a list of
   `{"id": "<lesson>-qa01", "stem", "key", "distractors": [3], "explanation", "citation", "extract", "snippet": null}`;
   `d4/attr/<lesson>.refutations.yaml` — per id `key: {anchor, sentence}` and `wrong: [{option, anchor, sentence} ×3]`,
   each `sentence` copied character for character from `show` output, each `option` equal to the distractor text.
5. Checks, run ONCE on the finished lesson file, from `backend/`:
   `uv run python -m scripts.tech_course.lint_questions ../docs/_work/backend-in-depth/d4/attr/<lesson>.questions.json`
   (it runs `check_refutations` too) and
   `python3 ../docs/backend-verification/d4/tools/attributed_form.py ../docs/_work/backend-in-depth/d4/attr/<lesson>.questions.json`.
   A question named by any failure line is **deleted, not repaired** (remove it from both files). If the lesson-level
   key-longest line fails, delete questions whose key is the longest, latest id first, until it passes. Then rerun both
   to confirm exit 0 (deletions only). Append `<lesson>\t<written>\t<deleted at checks>\t<rules hit>` to
   `d4/attr/checks.tsv`.
6. A lesson with no surviving candidate gets `d4/attr/<lesson>.none.txt`: one line on why (no stored-in-full source,
   fewer than three contradicted wrong options for every candidate point, could not balance without filler).
7. Decisions that are not a plain application of this brief: append `D4-D-<writer>-<n>\t<lesson>\t<decision>\t<rule>` to
   `docs/backend-verification/d4/decisions.tsv`.

## Return

At most one line per lesson: written, deleted at checks, kept, or the `none` reason. Do not paste content.
