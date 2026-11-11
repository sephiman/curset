# Handoff — age-auxiliar-c2, R5 (2026-11-11)

Nothing committed. Record: `docs/age-c2-bank-ledger.md` «R5»; deploy: `docs/deploy-age-c2.md`.

**Calibration items.** 34 frozen generated items (`ps-calibracion`, `official: true`), one per generator level.
**Presets.** `exams:` in `course.yaml`: simulacro, parte-1, parte-2, psicotecnicos, bloque, tema, and `conv2025-a` …
`conv2020-x`. Scoring with the 2025 cut-offs as exact fractions (29; 64/3); part 2 graded only if part 1 reaches its
minimum (Anexo I 2.3.1 a)).
**Decisions to confirm.** Parts alone get 49 / 41 minutes (share of 90 over 110 questions); psicotécnicos 25 minutes;
bloque 50 q / 41 min; tema 20 q / 16 min. The mixed part's reserve is five bloque I questions. Part 1 prints bloque I first, then the
psicotécnicos (`order: by-source`, added in the R5 review).
**Official sets.** 934 questions in, 26 out, tables as printed; blind-verified against the PDFs (0 errors).
**Platform.** Stored quiz `table`; the review now shows tables; the review's reference no longer overflows at 390 px.
**Identity.** `document-sheet`, blue `#3a5aa6` / `#7ea0dc`.
**Publication.** `status: published`; e2e extended (`e2e/age-c2.spec.ts`, three courses in `session.ts`).
**Results.** Backend 3,085 passed / 21 skipped; frontend 726 / 81; e2e 72; tsc, ruff, mypy clean; Android bundle
byte-identical; goldens unchanged; C1 and crypto-futures untouched. No migration in R5 (the chain since AGE 1.0 is in
the deploy doc).
**Open.** Variant rounds for bloque I; three psicotécnico types; word-bank growth; OEP 2026 diff round.
