# S1 part B — platform deltas N1, N2, N3

**Existed:** react-markdown + remark-gfm + the directive dialect, `:::note`/`:::esquema` rendering (web and PDF), the excerpt/noExcerpt solution
panel, `EXTRA_CONTENT_DIR` for published e2e fixtures. No highlighter, no judgement block, no licence handling.

**Built**
- N1: highlight.js core with 8 grammars (`lib/highlight.ts`), `lib/CodeBlock.tsx` (focusable region, scrolls inside its box), token colours as CSS
  custom properties (light/dark) in `index.css`; `pre` mapped in `lib/markdown.tsx` so lessons and `Prose` (stems, explanations) share it;
  `OptionText` for options with backticks; `lib/comments.ts` drops `<!-- … -->`; info-string meta never shows.
- N2: `:::judgement{source ref}` as a labelled violet `aside` (web) and a callout with a "Judgement from <source>" line (PDF);
  `content/judgement.py` validates at load (source required, only source/ref, ref resolves against sources.yaml).
- N3: `QuizVariant.extract` and `.snippet` (excluded from payloads); `citations/tech_solution.py` decides the panel from the first citation's
  source (`TechSourceIndex`); `noExcerpt.detail` (omitted when unset); reasons `licence`, `no-extract`; loader rejects extract on a forbidden
  source and snippets that are not files. SolutionPanel labels web sources "Open the source".
- Fixture course `backend/tests/fixtures/content/fixture-tecnico` (Dockerfile bakes it into e2e-content), README section, en/es i18n keys.

**Files:** backend `content/judgement.py`, `citations/tech_solution.py`, edits in `content/registry.py`, `exercises/quiz.py`, `attempts/schemas.py`,
`citations/excerpt_store.py`, `Dockerfile`, tests `test_tech_platform.py`, `test_multi_course.py` (catalogue); frontend `lib/{highlight,CodeBlock,comments}`,
`lib/markdown.tsx`, `lib/pdf/{markdown,page,document,labels}.ts`, `features/exercises/{OptionText,SolutionPanel,QuizExercise}`, `api/exercises.ts`,
`i18n/{en,es}.json`, tests `markdown.code.test.tsx`, `OptionText.test.tsx`, `SolutionPanel.test.tsx`, `pdf/markdown.test.ts`, `e2e/technical.spec.ts`.

**Decisions:** D40–D49 in `decisions.tsv`. Open: PDF code stays in the sans face (no embedded mono font); the solution panel's correct-answer line is plain text.

**Results:** `e2e/ci-local.sh technical.spec.ts` (CI Playwright image): 6/6 (390 and 1280 px). Bundle re-export to scratch: identical to `dist/bundle`.
Backend, ruff, mypy, vitest, tsc: see the status line of the caller.
