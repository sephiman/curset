# S1 review: uncommitted working tree (correctness)

Scope: `git diff` plus untracked backend/, frontend/, docs/backend-verification/s1/ and content/backend-in-depth/
files. Nothing was edited or committed apart from this file.

## Other four courses and the Android bundle: no change found

- No other course has `sources/sources.yaml`, so `TechSourceIndex.load` returns None and the tech branches in
  `citations/course.py`, `content/registry.py` and `question_excerpt` never run for them.
- No other course has fenced code or HTML comments in its markdown, and no option text with backticks, in either
  its exercise YAML or 300 seeds × all levels of every existing psicotécnico generator. So the frontend `pre`,
  `remarkHideComments` and `OptionText` changes render nothing differently for them.
- `NoExcerptOut.detail` is left out when unset (checked with pydantic 2.14.1). The new `QuizVariant` fields are
  `exclude=True`. No generator id is in both `GENERATORS` and `BACKEND_GENERATORS`. Hrefs in the existing
  solution panel are all `/api/...`, so `useSourceLabel` labels them as before.
- Suites run, all passing: test_multi_course, test_practice_spaced (integration), test_psicotecnico_generators,
  test_psicotecnico_platform, test_export_bundle, test_export_contracts_to_android, test_generation_goldens,
  test_backend_generators, test_tech_course_scripts, test_tech_course_citations, test_tech_platform.

## Generator keys checked by hand

All correct: capacity (seeds 3676…, 1255…, 8300…), circuit breaker (1548…, 2024…), isolation anomaly (3649…, 2997…),
quorum (5279…), Lamport clocks (1533…), Kafka lag (8793…), consistent hashing (2826…), LRU (4185…), token bucket
(3512…), composite index (2952…), binary heap (4216…), retry backoff (1418…, and seed 8 at level 2), loop
complexity (1395…).

## Findings, most severe first

1. **`psicotecnico/backend/capacity.py:52`, `retry_backoff.py:39`: the "equivalent wording" hedges
   (`about {}`, `approximately {}`) make two options defensible when a distractor is close to the key.**
   Retry seed 8, level 2 asks for an exact bound (1,500 ms) and shows "about 1,500 ms" next to "about 1,550 ms".
   Capacity seed 1, level 2 has the key "about 2,963.0 Mbit/s" next to "about 2,893.5 Mbit/s". A scan of seeds
   0–2999 at both levels found a distractor within 5 % of the key in 925/6000 capacity items and 173/6000 retry
   items (script in the session scratchpad). The hedge also misstates exact answers: the largest wait is exactly
   3,200 ms, not "about" it. The forms are drawn independently of the key slot, so they do not leak the key's
   position. The problem is equivalence, not leakage. A related case: `isolation_anomaly.py:42-46` appends
   "which is what PostgreSQL 18 does at this isolation level", which also turns a distractor into a false claim
   of correctness.
2. **`practice/service.py:305-321, 358-363`: the mixed review and `_history` key questions by `variant_id` alone,
   but variant ids are only unique within one exercise (`exercises/quiz.py:161`).** Scenario: two exercises in
   different lessons each have a variant `q1`. `by_id` keeps only one of them, so the other is never reviewed, and
   the answers to both are merged into one history, so failing one makes the other due. Verified by reading. The
   per-lesson `_mastered` already made this assumption, but the course-wide review widens it to every lesson.
3. **`citations/tech_solution.py:18-42` vs `scripts/tech_course/check_extracts.py:36-46`: the panel attributes an
   extract to the first cited source, but the check accepts it as a substring of any cited anchor.** Scenario:
   a question cites `a#x; b#y` and its extract is copied from `b`. The extract passes the check, and the panel
   then shows it under `a`'s title, anchor, licence and link. Verified by reading.
4. **`scripts/tech_course/check_extracts.py:42-43`: `return []` on the first anchor whose local copy cannot be
   read skips every remaining ref of that question, and the summary line never reports skips.** The only trace
   is the one-time stderr warning. Scenario: with the citation `local-src#a; pg-iso#b`, an extract with a typo
   passes whenever the local folder is absent, even though `pg-iso` is in the repo and could be checked.
   "Warn, not fail" should skip only the local ref. Verified by reading.
5. **`scripts/tech_course/lessons.py:132-139` (`prose_citations`): a malformed prose citation is silently dropped
   (`refs or []`), so `check_citations` cannot fail on it.** Verified: a lesson containing
   ``(`pg-iso XACT-READ-COMMITTED`)`` gives `citations() == []` and `fact_sentences() == 0`, and no FAIL is
   printed. A typo therefore makes an F fact uncited without any report. `lesson_quota` also under-counts it.
6. **`scripts/tech_course/run_snippets.py:180-188` (`--check`): it compares only the snippet sha.** It does not
   compare the record's `java`/`kotlin` with `pinned()`, and does not check its `isolation`. Scenario: after the
   pin moves to a new JDK, every record made on the old JDK still passes `--check`, so "runs on the pinned
   toolchain" is not enforced. Verified by reading.
7. **`psicotecnico/backend/base.py:96-101`: `solve()` recomputes the key with the same `correct()` that `build()`
   used, so the property tests cannot detect a wrong rule.** They only catch duplicate options. Key correctness
   rests entirely on the blind golden review. This is informational; verified by reading.
8. **`frontend/src/features/exercises/AttemptResult.tsx:138` and `frontend/src/lib/pdf/exercises.ts:160` still
   print `opt.text` raw, while `QuizExercise` now renders code via `OptionText`.** For backend-in-depth, the
   result review and the PDF show literal backticks. Verified by grep.
9. **`content/registry.py:240`: `tech_solution` is passed `manifest.course.languages[0]`, not the reader's
   locale.** The extract language would be wrong once the course gains a second language. This is latent: the
   course is `[en]` today.

No XSS found. Judgement `source`/`ref` are rendered as React text. `CodeBlock` injects only highlight.js output,
which escapes the source. Option markdown goes through react-markdown's default URL transform.

## Fixes

1. Fixed: `min_separation` of 20% (D100) between key and distractors and among distractors for capacity and retry; test over seeds 0-2999, both levels; goldens re-exported. Other families have no hedged wording (exact discrete answers), so no margin.
2. Fixed: the mixed review, `_history`, `_mastered` and the round are keyed by (exercise id, variant id); integration test with two exercises sharing a variant id.
3. Fixed: `check_extracts` accepts an extract only from the first citation; a missing local copy skips that question only.
4. Fixed: a prose parenthetical with `#` in inline code that does not parse is reported by `check_citations` (`Lesson.malformed_citations`).
5. Fixed: `run_snippets --check` compares the recorded Java (and Kotlin for `.kt`) with the pins; `isolation` is still not compared.
6. Open: 7 (informational: `solve()` reuses `correct()`), 8 (raw `opt.text` in AttemptResult and the PDF), 9 (latent: `languages[0]`).
Isolation anomaly's "what PostgreSQL 18 does" wording (part of 1) is open.
Suite: pytest 3563 passed, ruff, mypy clean; tech_course scripts exit 0.
