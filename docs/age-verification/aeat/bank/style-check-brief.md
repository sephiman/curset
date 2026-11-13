# AEAT style check of derived candidates — checker brief (round R3, step 2)

You check questions copied verbatim from the C1 and C2 banks of this repo into the course `aeat-agentes-hacienda`
against **this course's reviewer checklist only**. Their facts, keys and citations were verified in their origin course
against the same source files (same sha256), and you do **not** re-check them: no key, uniqueness or citation work,
no source reading. A candidate that fails is **dropped**, never rewritten: do not propose fixes. Work in
`/home/juanjo/PycharmProjects/curset`. Do not commit. Write only your output files.

## Read first, once per run

- `docs/aeat-exam-style.md` sections 1–10 and 12 (skip the statistics tables).
- For each lesson you check, its official pack `docs/age-verification/aeat/r2/questions/<lesson>.md` (item 7).

## Input and output

Input: `docs/age-verification/aeat/bank/style/input/<lesson>.b<k>.md` (up to 60 candidates). Output, one file per batch,
written as soon as the batch is done: `docs/age-verification/aeat/bank/style/<lesson>.b<k>.md`:

```
# Style check — <lesson>, batch <k>

Checked: n. PASS: x. FAIL: y.

| id | verdict | items | reason |
|---|---|---|---|
| m01-l01-q0001 | PASS | | |
| m01-l01-q0002 | FAIL | 8 | typo «recurso» → «recuros» |
```

Every candidate gets one row; `items` lists the checklist numbers failed; `reason` is one short line for a FAIL,
empty for a PASS.

## What fails (checklist § 12, as applied to a candidate)

- **2.** The stem does not name the norm by its BOE title (number and date alone, «Ley 39/2015, de 1 de octubre»,
  passes; a short name or acronym fails) where the question rests on a norm, or does not name the article where the
  question rests on one article. A stem that quotes a constitutional or institutional rule with no article and asks a
  general question passes if it reads like the 2025 «pregunta directa» form.
- **3.** The stem is not a sentence to complete ending in «:», a question «¿…?», or a «señale la respuesta CORRECTA»
  instruction.
- **5.** A negative stem (asks for the option that is NOT, or the INCORRECTA one) whose negative word is not in capitals.
  A «no» inside a premise is not a negative stem.
- **7.** The candidate copies or lightly rewords an official question of the lesson's pack: same fact, angle and key
  with an official distractor carried over. The same fact with new options passes.
- **8.** The four options do not share grammatical form and register, one is absurd, or wrong on spelling alone;
  also a typo, a missing accent, or Spanish that is not Peninsular.
- **11.** An organ name that is not current (AEAT departments, ministries, Government structure) and the stem does not
  date it.
- **12.** A figure set by a yearly norm (interés de demora, IPREM, módulos, límite de garantía de aplazamiento) with no
  year in the stem.
- **14.** The fact is outside the 2025 programme (IRNR, Impuestos Especiales, contrabando, impuestos medioambientales,
  tipos del IVA, retenciones, declaraciones informativas, consulta tributaria) with no 2025 tema phrase covering it.
- **16.** An official erratum copied («Ley 58/2023», «Ley 27/2004», «Ley 29/1988», «Ley Orgánica 3/2017», «Ley 58/2003,
  de 28 de diciembre»).
- **17 (part).** The explanation does not say why the key is right **and** why each distractor is wrong, or names an
  option by letter or position («la opción b», «la primera»). Ruling (as C1 and C2): when the cited text gives a single
  value, a single holder of the function or a closed list, and the explanation states that rule, it may dismiss the
  distractors as absent from the precept.
- **Standalone.** The stem needs a case scenario it does not contain.
- **Dated copy.** The stem or explanation depends on a person or fact that changes with an election or appointment
  (names of office-holders) with no date.

Do not fail on anything else: not on length (a script checked it), not on the fact, not on taste. When unsure whether a
defect is real, PASS with a short note in `reason`.

## Final message

Per batch: checked, PASS, FAIL, FAIL count per item. Nothing else.
