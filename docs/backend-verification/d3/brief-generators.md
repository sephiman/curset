# Round D3, Part A — runtime generator writer brief

Read: `CLAUDE.md`, `docs/prose-voice.md`, `docs/backend-question-style.md` (sections 1, 4, 7), `docs/backend-verification/s1/contracts.md`,
`docs/backend-verification/s1/part-c-generators.md`, `docs/backend-verification/s1/generator-goldens/*.md` (one for the shape), and
`backend/src/tradeschool/psicotecnico/backend/{base.py,quorum.py,lru_cache.py}` plus `backend/tests/test_backend_generators.py`.
Then your modules' written lessons in `content/backend-in-depth/en/lessons/`.

Task: for each candidate family of your modules, add a generator in `backend/src/tradeschool/psicotecnico/backend/<name>.py`, same shape as the existing 13.

Hard rules
1. A family exists only if a lesson ALREADY states its rule in a verified sentence. The citation is that sentence's `source_id#anchor` (the trailing parenthetical of the sentence); the explanation cites the anchor. If no lesson sentence states the rule, write NOTHING for the family: append a line to your `decisions.tsv` (id, lesson, "skipped: <rule missing>", "round D3 part A"). This round writes no theory; never edit a lesson.
2. Seeded and deterministic; key computed by code; never by hand. Explanation: inputs, formula once, each numbered step, result. One-line doc comments only (CLAUDE.md global).
3. Four distinct options. Wrong options come from NAMED typical mistakes computed by code; numeric wrong options differ from the key by a clear margin (use `separated`/`min_separation`), distinct after rounding. Numbers mentally tractable. Stems 15–40 words, code as inline code, version named only when it changes the answer.
4. Tests: property tests (key distinct from distractors, four options, determinism per seed, explanation mentions every step) and golden seeds, in `backend/tests/test_backend_generators_<writer>.py`, which instantiates YOUR classes directly. Write the test first and watch it fail. `ruff check`, `ruff format`, `mypy` clean.
5. DO NOT edit `catalogue.py`, `course.yaml`, any fingerprints json, README, or another writer's files; the coordinator registers every generator afterwards. Put in `docs/_work/backend-in-depth/d3/<writer>/registration.md` per family: id, class, module path, title, lesson, citation, and one sentence for the lesson page "practises this lesson".
6. Run only your own tests with `cd backend && uv run pytest tests/test_backend_generators_<writer>.py -q`. No git command that rewrites the working tree; never commit.
7. Log decisions (ids like `D3-A-<writer>-n`) to `docs/_work/backend-in-depth/d3/<writer>/decisions.tsv` (columns id, lesson, decision, rule) and tokens per family to `.../cost.tsv`.
8. A family you cannot make correct is dropped and logged; carry on with the next. Work the families in sequence in one run; progress notes after every family in `.../progress.md`.
9. Report at the end: families added (id, lesson, anchor), skipped with the missing rule, dropped and why, each with the module's test result. Under 25 lines.
