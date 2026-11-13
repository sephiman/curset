# Handoff — aeat-agentes-hacienda, R5 (2026-11-13)

Nothing committed. Record: `docs/aeat-bank-ledger.md` «R5».

1. **Presets** in `course.yaml` `exams:` (16): «Primer ejercicio», «Bloque», «Tema», 13 official sets.
2. **Primer ejercicio:** 80 q (8 I + 10 II + 62 III, the 2025 paper's part counts), 90 min, no pause, −1/4, blank 0, tema hidden, shuffled (the paper mixes parts).
3. **Decision to confirm:** the Tribunal fixes the pass raw score each year, so the mark uses the criteria's 50 % floor: 40 raw = 5, 80 = 10. 41,00 (2025) is in the description as information only. The m00-l01 lesson's worked example uses 41.
4. **Bloque / Tema:** 40 q / 45 min and 10 q / 11 min, described as course estimates (1,125 min per question).
5. **Official sets:** `backend/scripts/build_aeat_official_exams.py` → 13 exercises `ofi-*` under m00-l01 (`official: true`); 1,180 questions in; printed order and letters, no shuffle; raw score only; the 28 dropped-topic questions out and counted in each header.
6. **Blind check:** two opus verifiers, every included question against the PDFs. One defect class (hyphen at line end, 24 places), fixed and test-guarded; second verifier re-ran clean. Reports: `docs/age-verification/aeat/official/verify/`. The 2025–2023 sets were re-read on the corrected files at review (0 FAIL, 0 UNREAD); `verify/` holds those reports.
7. **Source finding:** the OEP 2022 answer sheets say «PROVISIONAL» in their header but carry the annulments; treated as definitive; confirmed at review against the Tribunal's resolution of 9-05-2023 (ledger R5, finding 1).
8. **Platform change:** `ExamRunner` hides the tema label when `pause === "never"` (was preset-id prefixes). Same behaviour for C1, C2, crypto-futures.
9. **Results, review, «Por tema», solution panel, PDF with key sheet** work as in C1/C2 with no further change; official sets count under the intro lesson, as in C1/C2.
10. **Tests:** `test_aeat_first_exercise_presets.py` (draw, hand-computed marks, auto-submit), `test_aeat_official_exams.py` (PDF and sheet checks), `aeat_client` fixture, e2e `aeat-agentes.spec.ts` (theory-only default stays on the fixture course), AEAT added to the excerpt test in `age-c2.spec.ts`.
11. **Close:** backend 3,377 passed / 34 skipped; frontend 753; `tsc -b` clean; e2e 110; goldens unchanged; C1, C2, crypto-futures, Android untouched.
12. **Open:** variant rounds (gap 912); official sets show no per-year cut-off mark (raw only); RDL 29/2026 and 31/2026 watch; check `.husky/pre-push` and `backend/raw.json` before committing.
