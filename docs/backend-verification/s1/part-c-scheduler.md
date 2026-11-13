# Part C1 (N4): the practice scheduler

- Opt-in: `practice_scheduler: spaced` in course.yaml (schema `ManifestCourse`); set in content/backend-in-depth/course.yaml. Other courses keep `practice_order`.
- Pure rule: `backend/src/tradeschool/practice/spaced.py` (`due_at`, `spaced_order`; intervals 1,3,7,15,30 days from the last answer, run of correct answers since the last failure, reset on failure). Decisions D80-D86.
- Selection: `practice/service.py` picks the scheduler per course for lesson rounds; new `POST /practice/review` is the mixed review (course-wide, same scheduler).
- Storage: existing `attempts` rows only; no migration. Options: already shuffled per attempt seed (quiz.py), reused.
- Tests: `backend/tests/test_practice_spaced.py` (unit rule + endpoint integration over a spaced copy of fixture-oposiciones via `spaced_client` in conftest; non-opted course refused/unchanged).
- Not done: frontend preset UI (mixed review button, by-module, code-reading, generators-only), no e2e spec; nothing exposes due counts.
- Frontend untouched, so vitest/tsc not run.

## Playwright

- `frontend/e2e/scheduler.spec.ts`, at 390 and 1280 px (via `e2e/ci-local.sh`, 4 tests green); a fresh English-locale learner per test, so history never leaks between runs.
- `fixture-tecnico` now opts in (`lesson_practice: true`, `practice_scheduler: spaced`) and has a third question (`lost-update-fix`); backend suite green (3554 passed), no test needed changing.
- (a) Options keep their order on reload: asserted through the API (`GET /attempts/{id}`) against the order on screen, because the UI drops an in-progress round on reload.
- (b)+(c) In the UI: after one question is answered wrong, a new round the same day serves the two unseen questions first and the failed one last (position 3 of 3).
- Not covered: return after the interval (needs a clock), `POST /practice/review` (no UI). Frontend production code unchanged; `tsc -b` clean, vitest not run.
