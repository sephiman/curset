# Verification — reinstated questions on doubtful official keys (reinstated2.v1)

Verifier: blind (opus), 2026-11-12, under `verify-spec.md` including the Amendment of 2026-11-12. Writer notes not read.
Source: LIS `BOE-A-2014-12328_lis_2026-09-02.pdf` (`pdftotext -layout`), arts. 26.5 (p. 50) and 31.7; no
`cambios_pendientes`, not on the RDL 29/2026 revert list. Cross-check: art. 66 bis.2 LGT gives the same ten-year term
and dies a quo, so no other norm in force makes a distractor defensible. `check_draft.py` on
`m03-l17.authored-p1.draft.json`: 107 questions, 0 anchor misses; lesson m03-l17 cites (art. 26.5 LIS) at l. 202 and
(art. 31.7 LIS) at l. 279. Official comparison: all 680 questions in `r0a/parsed/` (conv*_A + 2022_X), searched for
bases imponibles negativas, doble imposición, prescripción, 10 años / diez años, 66 bis; relevant items 2024-43 (art.
66 bis LGT, combined plazo + procedural-scope señale, key «finalice el periodo impositivo») and 2025-18 (art. 26 LIS,
plazo de compensación, a different fact). Both explanations end with the Amendment sentence (examen 2024, pregunta 43).

| id | 1 key | 2 unique | 3 citation | 4 style | 5 not official | verdict | reason |
|---|---|---|---|---|---|---|---|
| m03-l17-q0062 | PASS | PASS | PASS | PASS | PASS | PASS | Key d = art. 26.5 LIS word for word (10 años desde el día siguiente al fin del plazo de declaración del período en que se generó el derecho a compensar). a, b: 5 and 15 años contradict «prescribirá a los 10 años»; c: dies a quo «presentación de la declaración del período en que se compense» contradicts «finalice el plazo establecido para presentar la declaración … del período impositivo en que se generó el derecho». Stem names the LIS by BOE title and article; options parallel, key not longest; explanation covers every distractor without letters. Not official: 2024-43 asks art. 66 bis LGT with a combined angle; no official option carried over (its 4 años / «no tiene plazo» / «finalice el periodo impositivo» are absent); 2025-18 is a different fact. |
| m03-l17-q0081 | PASS | PASS | PASS | PASS | PASS | PASS | Key c = art. 31.7 LIS word for word (same wording in art. 32.8). a, b: 5 and 15 años contradict «prescribirá a los 10 años»; d: dies a quo «día siguiente a aquel en que se aplique la deducción» contradicts «finalice el plazo establecido para presentar la declaración … del período impositivo en que se generó el derecho a su aplicación». Style items as q0062; key same length as a and b, d shorter. Not official: same reasoning as q0062 (2024-43 is a different norm, angle and option set). Twin of q0062 on a different article; fine as a bank pair. |

Summary: checked 2, PASS 2, FAIL 0. No lines added to `drops.tsv`.
