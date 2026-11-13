# S2 writer brief — one lesson of backend-in-depth

You write one lesson at a time; the coordinator may send you the next lesson of the same module afterwards.
Load once per run: `CLAUDE.md`, `docs/backend-verification/s1/contracts.md` (follow it exactly),
`docs/backend-question-style.md`, `docs/prose-voice.md`, requirements sections 4 and 5
(`docs/backend-in-depth-course-requirements.md`, lines 72–94) and the module's bullets in
`content/backend-in-depth/programme.md`. Read nothing else beyond the anchors below.

## Inputs per lesson

- The stub `content/backend-in-depth/en/lessons/<lesson>.md`: its «Sources» block lists, per bullet, the class
  (F, F+X, X, J) and the anchors. Load **only** those anchors, one at a time, from `backend/`:
  `uv run python scripts/tech_sources.py show SOURCE#ANCHOR` (local-only copies resolve through
  `CURSET_SOURCES_LOCAL`). Never open a whole source file.
- If a bullet needs an anchor that is missing, add the source with the S0 rules (`tech_sources.py fetch`/`anchors`,
  licence in `sources/licences.yaml`) and log it in `docs/backend-verification/s2/<module>/decisions.tsv`
  (`id<TAB>lesson<TAB>decision<TAB>rule`). When unsure, the conservative default: leave the claim out.

## What you write

1. **The lesson**, replacing the stub file (keep the `# Title`). Sections `## …`, each followed on the next line
   by `<!-- bullets: 6.2.a … -->` with the bullets it covers (only this subsection's bullets; together the
   sections cover every bullet of the stub not marked dropped). English only. Voice: `docs/prose-voice.md`
   (its "never does" list is a hard constraint; no coined vocabulary).
   - Each F sentence ends with a parenthetical holding only inline-code citations: ``(`pg-x#ANCHOR`)``. One
     fact per sentence; the fact must be stated by the cited anchor of the pinned version, not by memory.
   - J content (trade-offs, advice) only inside `:::judgement{source="…" ref="…"}` … `:::`, worded "According
     to …", attributed faithfully.
   - Schemas: `:::esquema{kind=tabla title="…"}` (or decision tree / steps, per the m00-l01 example); every row
     is an F fact with a `source_id#anchor` citation column.
   - Code: fenced with a language. SQL, YAML and config are illustrative and need a citation for any claim
     about their effect. Java/Kotlin snippets that run with the JDK alone go in
     `content/backend-in-depth/snippets/<lesson>/<File>.java` and are shown as ```` ```java snippet=<lesson>/<File>.java ````
     with the block body equal to the file; then run, from `backend/`,
     `uv run python -m scripts.tech_course.run_snippets --lesson <lesson>`. Anything needing a database or
     broker is not X: cite documentation or leave it out.
   - End with `## Key points` (bullets restating only F/X facts already in the lesson, no new facts, no
     metadata line) and keep the stub's `## Sources` section as it is.
2. **Glossary candidates** (do not edit `glossary.yaml`): `docs/backend-verification/s2/<module>/<lesson>.glossary.yaml`,
   a YAML list of `{id: g-<slug>, term: {en: …}, definition: {en: …}, origin: <lesson>, citation: "src#anchor"}`.
   Only terms that exist outside the course, defined in the wording of the cited source, and used verbatim
   in your lesson prose. One or two sentences each.
3. **Summary** for the course manifest: one sentence in `docs/backend-verification/s2/<module>/<lesson>.summary.txt`.
4. **Question candidates**: run `uv run python -m scripts.tech_course.lesson_quota` from `backend/` after the
   lesson is written; write between the lesson's quota and quota + 3 candidates (extra ones absorb discards) to
   `docs/backend-verification/s2/<module>/<lesson>.questions.json`: a list of
   `{"id": "<lesson>-qNN", "stem", "key", "distractors": [3], "explanation", "citation", "extract", "snippet"}`.
   - Follow `docs/backend-question-style.md` in full: one fact per key, version named in the stem when it
     matters ("in PostgreSQL 18"), every distractor contradicted by a cited sentence, explanation names each
     distractor by content (never by letter), key not systematically longest (aim ~1 in 4), no near-duplicates.
   - `citation`: first citation supports the key. `extract`: a literal substring of the first cited anchor,
     only when that source's licence allows extracts (`show` prints it); otherwise `null`.
   - Code-reading questions only on a snippet of this lesson that ran; put the snippet path in `snippet` and
     the recorded stdout as the key.
   - Then build the exercise file: `python3 docs/backend-verification/s2/tools/build_quiz.py
     docs/backend-verification/s2/<module>/<lesson>.questions.json content/backend-in-depth/exercises/<lesson>-ex-1.yaml`
     and read its report: if the key is longest in more than ~40 % or the mean gap is above +8 chars, rebalance.
5. **Script checks** from `backend/`: `check_citations`, `check_extracts`, `check_scope`, `run_snippets --check`
   (each `uv run python -m scripts.tech_course.<name>`). Fix what is yours until they are clean for your lesson.

## Return

At most five lines: lesson id, F sentences / esquema rows / snippets / questions written, quota, script-check
status, any decision logged. Do not paste content.

## Fix rounds

When the coordinator sends failed sentence ids from a verdict file: rewrite each failed sentence **once**,
from its source, and list the rewritten ids in `docs/backend-verification/s2/<module>/<lesson>.rewrites.tsv`
(`id<TAB>new sentence`). On a second failure, delete the sentence (and any key point restating it) and keep
the lesson grammatical. Never repair a failed question; the coordinator drops it.
