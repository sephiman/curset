# Psicotécnico generators — blind review of round L (2026-11-07)

Task: check the word banks against the DLE (step 1); blind-read the 13 golden pages, 650 items (step 2); rerun the guards (step 3); report per generator (step 4). Not committed.

- **Blind reads.** Opus verifiers following [`verifier-brief.md`](verifier-brief.md): golden pages plus `docs/age-c2-psicotecnico-index.md` and the saved DLE pages. Never the generator code, its tests, the handoff, or an earlier pass.
- **Re-reads.** Every generator fix regenerated the goldens, and each page that moved was read again until its whole page passed. The latest read of each page is `<generator>.md`; earlier ones are `<generator>.passN.md`.
- **Word banks.** DLE work, removed and corrected entries, and every entry's citation: [`word-banks.md`](word-banks.md).

All 650 printed keys were right on every pass. Every FAIL was about wording, explanation, realism, a distractor that could also be defended or that gave the key away, a level label, or a bank entry.

## Per generator

| Generator | Items read (all passes) | FAILs by cause (pass where found) | Latest pass |
|---|---|---|---|
| tablas-lectura | 200 (4 passes) | generator 37 (p1), 28 (p2), 3 (p3) | 50/50 PASS (p4) |
| atencion-codificacion | 250 (5) | generator 11, bank 11 (p1); generator 4 (p3) | 50/50 (p5) |
| verbal-sinonimos | 200 (4) | generator 46 (p1), 2 (p2); bank 1 (p3) | 50/50 (p4) |
| verbal-antonimos | 50 (1) | none | 50/50 (p1) |
| calculo-ecuaciones | 100 (2) | none | 50/50 (p2) |
| verbal-definicion | 100 (2) | generator 6 (p1) | 50/50 (p2) |
| verbal-ortografia | 150 (3) | generator 7 (p1) | 50/50 (p3) |
| calculo-problemas | 200 (4) | generator 5 (p2), 1 (p3) | 50/50 (p4) |
| calculo-porcentajes | 100 (2) | generator 6, bank 6 (p1) | 50/50 (p2) |
| serie-numerica | 100 (2) | generator 50 (p1) | 50/50 (p2) |
| administrativo-clasificacion | 100 (2) | generator 25 (p1, 6 with a bank cause too) | 50/50 (p2) |
| calculo-fracciones-proporciones | 100 (2) | generator 7 (p1) | 50/50 (p2) |
| administrativo-ordenacion | 150 (3) | generator 40 (p1), 27 + bank 1 (p2) | 50/50 (p3) |

Problemas and ecuaciones passed in pass 1. They were re-read only because the contract fix (length tie-break, below) re-drew every golden page.

## Generator changes

Each change has a test in `backend/tests/test_psicotecnico_generators.py` (or `test_psicotecnico_lexicon.py` for the banks) that failed before the fix.

- **contract (all generators).** `generate` broke length ties by slot index, so accepting a redraw favoured some slots. verbal-antonimos failed the slot guard (z = 3.14) after the bank change. Ties are now broken by a seeded hash of the option text.
- **tablas-lectura:**
  - plural count columns read «más de 10 técnicos»;
  - text conditions are quoted after «cumple(n) estas condiciones:» («medio «Coche»»);
  - share questions read «corresponde a los alumnos con turno «Noche»»;
  - sum explanation: «la columna «X» suma…»;
  - explicit meaningful ratio pairs per theme; no sums of year, age or price per person;
  - thresholds within the column's spread, so no «inferior a 2253»;
  - ratio explanation shows 3 decimals below 1, so no «(0,00)»;
  - a nivel 3 filter sum takes 3–5 rows;
  - excursions go by bus, train or minibus, not boat;
  - trip time and cost follow from the distance and the means of transport.
- **atencion-codificacion:** the digit item asks for the coding of a given word. The old item decoded into a word against three non-words, so the key was the only real word. Words keep their tildes (Martínez, Gestión, Trámites); accent-bearing cipher words are replaced.
- **verbal-sinonimos:**
  - explanation names the synonym, the antonym(s) and the unrelated words;
  - distractors share the entry's part of speech;
  - no distractor whose cluster the DLE ties to the stem;
  - at most two antonyms, and other distractors from distinct clusters (no elimination by meaning).
- **verbal-antonimos:** no distractor may be a DLE antonym of the stem; stems without antonyms are skipped.
- **verbal-definicion:** each level draws words of exactly that level, with 5 rare words now level 3. Distractors share the defined sense's DLE category, and close definitions are never paired.
- **verbal-ortografia:**
  - word items deal from every other pair, which fixes the length-edge guard (z = −3.71 after the bank shrank);
  - the «correctamente escrita» explanation names each error and its correct form.
- **calculo-problemas:** in the stationery totals, the distractors are the slips a candidate makes (one unit more or less, prices swapped), so no option has impossible cents. In sum-and-ratio items, every option lies between half the sum and the sum.
- **calculo-porcentajes:** discount and increase items are nivel 1. A near miss on the wrong side of the original price is dropped, unless it is the named sign slip. «un mueble de oficina» replaces «un material de oficina».
- **serie-numerica:** the explanation names the simplest fitting rule with its constants («multiplicado por 2 más 3»; interleaved series give each subseries' rule). The product series is described by its odd places.
- **administrativo-clasificacion:** no «un bobina»; ropes come in rolls of noun materials (no «Trenzada», «Plano»…); every surname drawer spans 3+ surnames.
- **calculo-fracciones-proporciones:** «1 parte», and «Un sexto son 40 paquetes» for «Cada 6.º».
- **administrativo-ordenacion:** the explanation places every word by its deciding letter, with the shared prefix printed accent-free («com», not «cóm»). «consistorio» replaces «consiste».

## Follow-up: official error count and code length

Two open notes from the first review were applied, each with a test that failed first:

- **verbal-ortografia:** a sentence item carries 4–6 errors, as the official ones do (was 2–5). Re-read in pass 3: 50/50.
- **atencion-codificacion:** the «Clave de archivo» code has six positions with four values each, as in 2024X-P1-55 (was four). Pass 3 failed 4 items (G1) because the explanation did not decode the code. The explanation now reads every position («1 (departamento) = 1, Ventas; …») before naming the right statement. Re-read in pass 4: 50/50.

Pass 4 noted three things without failing any item: filing items asking for the CIERTA statement are nivel 2, though the index may put them at nivel 1; the digit words have 7 letters where the index gives 8; the binary tables draw shuffled letters from a–g, where the official example lists a–f in order.

## Open notes (not FAILs)

- serie-numerica gives nivel 1 to plain «+k» progressions, which the exams have not used.
- Count explanations don't name the rows that pass.
- The bank is small, so stems repeat within 50 items. A later round adds DLE-sourced entries (each cited through `dle_relations.py`) until no stem repeats within 50 items.
- verbal-antonimos accepts PROHIBIR → «Aprobar» via «vetar», a weak but defensible key.
- INCIPIENTE has no DLE antonym, so it appears only in synonym items.

## R3 calibration (2026-11-07)

Three points from pass 4, applied before the C2 bank round, each with a test in `test_psicotecnico_generators.py`:

- **Digit words** have eight letters, as 2020-P1-39 and 2020X-P1-31 (bank of 18 eight-letter office words; test failed first).
- **Binary tables** list the letters a–f in order, as 2024-P1-38 (test failed first).
- **Filing items** stay nivel 2, CIERTA and FALSA alike: the index's per-question levels put 2024X-P1-55, 58, 59 (FALSO)
  and P1-60 (CIERTO) at nivel 2 (its 10/6/0 count includes P1-60). The test pins that label; it passed before any
  change, since the generator already used it.

Goldens regenerated (only `atencion-codificacion` moved). Blind re-read pass 5: 50/50 PASS (`atencion-codificacion.md`;
pass 4 kept as `.pass4.md`).
