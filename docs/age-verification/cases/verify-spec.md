# Verifier spec — supuestos prácticos (R4, 2026-10-28)

You did not write the cases you check. Requirements R6.2 and R5.4; the test is `docs/age-exam-style.md` § 11–12.
Do not commit; do not edit drafts, lessons, content or tests. Do not read the writer's notes before your verdicts.

Read first (once per run): `docs/age-exam-style.md` whole, `docs/age-bank-plan.md` § 3, `docs/prose-voice.md`,
`docs/age-verification/bank/bloque-ii/verify-spec.md` (the bank's verifier spec: its five checks and its rulings
apply here unless this page says otherwise), `docs/age-verification/cases/spec.md` (what the writer was asked).

## 1. The scenario

Read the scenario and every stem. Check:

- **Complete.** Every fact a question needs is in the scenario or in its own stem (dates, amounts, organs, the
  person's corps and situation, the body's kind, the town for festivos).
- **Consistent.** No two facts contradict (a person renamed, a date after the act it precedes, an amount that does
  not add up, an organ that does not exist or is not the competent one, a post in the wrong body).
- **Calendar.** Every dated phrase has the true weekday for its year (check with Python `datetime`); every festivo
  in a counted window is named or excluded by the scenario's statement.
- **Fiction and voice.** No real person or company; AGE bodies with current names; the voice page's «never does»
  list holds.

A scenario fault is reported as `SCENARIO` with the sentence and what is wrong. The questions that rest on that
sentence fail check 1 or 2 if the fault changes their answer; otherwise they are judged on their own.

## 2. Per question

Open the cited article yourself (`pdftotext -layout`, the file named in `sources/normativa.yaml`, later version where
`cambios_pendientes` applies). Do not trust `source_quote`. The bank's five checks, with these additions:

1. **Key** — recompute every date and amount with Python. The count in the explanation must also be right.
2. **Unique** — read against the scenario: a distractor that becomes true under a reasonable reading of the scenario
   fails.
3. **Citation** — the cited article holds the answer; the question's `lesson` cites that article in its prose
   (search the lesson).
4. **Style** — checklist § 12 items 1–14, 16, 17, with case stems 20–50 words. **Dependence:** a question a candidate
   can answer without the scenario (no fact of it is needed) fails here. A question that needs the previous one must
   say so in its stem; if that previous one fails, this one fails too. Explanations name options by content, never by
   letter or position.
5. **Not official** — against `docs/age-verification/bank/official/<tema>.md`, supuesto questions included. A
   computation with an official case's shape and new figures, the official key and an official distractor, is a
   rewording and fails.

**Rulings of 2026-10-28 (user; they override anything above or in the bank spec that reads stricter):**

- **Dependence** is read as the style guide § 11 describes it: the scenario is context, and a stem may carry the
  facts, as the official cases do. Fail check 4 for dependence only when the question uses **no case fact at all**
  (none from the scenario and none from its own stem about the case's people, body, file, contract or budget), or
  when it **contradicts the scenario**. Distractors that are wrong whatever the facts, a key that states the deciding
  fact, an option that names its basis: none of these fails dependence.
- **Copies (check 5)** compare the stem and the options with the official question, not the kind of computation.
  Computing the same kind of plazo or amount as an official case, with the case's own dates and figures, is not a
  copy. The «lightly reworded» ruling still applies to stem and options: the same stem and the same option set, or
  the same options re-ordered, or the official key together with an official distractor in a near-identical stem.
- The scenario-consistency check and checks 1, 2, 3 and the rest of 4 are unchanged.

Any FAIL drops the question; you do not fix it. One line of reason, quoting the norm where it is about content.

## Report

`docs/age-verification/cases/sp-NN.verify-<k>.md` (`k` = 1 for the first pass, 2 for the replacements, …):

1. Scenario: OK, or each `SCENARIO` fault.
2. Table:

| id | tema | 1 key | 2 unique | 3 citation | 4 style | 5 not official | verdict | reason |
|---|---|---|---|---|---|---|---|---|

3. Summary: checked, PASS, FAIL by first failing check; computations recomputed (count) and how many disagreed.

Append one line per FAIL to `docs/age-verification/cases/drops.tsv` (columns `id	case	batch	check	reason`, id as
`sp-NN/qMM`, batch the report's stem; create with that header if missing; append with `>>` only). Final message:
per case, scenario OK or faults, checked, PASS, failing ids with their check. Keep it short.
