# C2 style check of derived candidates — checker brief (round R3, step 2)

You check C1 questions copied verbatim into the C2 course (`age-auxiliar-c2`) against the **C2 style checklist only**.
Their facts, keys and citations were verified in C1 against the same source files, and you do **not** re-check them:
no key, uniqueness or citation work, no source reading. A candidate that fails is **dropped**, never rewritten, so
do not propose fixes. Work in the repo `/home/juanjo/PycharmProjects/curset`. Do not commit. Write only your output
files.

## Read first, once per run

- `docs/age-c2-exam-style.md`, sections 1–9 and 12 (checklist). Skip the statistics tables.
- For each lesson you check: its official pack `docs/age-verification/c2/<bloque>/questions/<lesson>.md` (C2 official
  questions, for item 7).

## Input and output

Input batches: `docs/age-verification/c2/bank/<bloque>/style/input/<lesson>.b<k>.md`, with up to 60 candidates each
(stem, options with the key marked ✓, citation, explanation). Output, one file per batch, written as soon as the batch
is done: `docs/age-verification/c2/bank/<bloque>/style/<lesson>.b<k>.md`:

```
# Style check — <lesson>, batch <k> (2026-11-07)

Checked: n. PASS: x. FAIL: y.

| id | verdict | items | reason |
|---|---|---|---|
| m02-l09-q001 | PASS | | |
| m02-l09-q002 | FAIL | 16 | stem says «En Excel» with no version |
```

Every candidate gets one row. `items` lists the checklist numbers failed. `reason` is one short line for a FAIL and
empty for a PASS.

## What fails (checklist § 12, as applied to these candidates)

- **2.** The stem is not a sentence to complete ending in «:» or a question «¿…?» in one of the forms of § 2 for its
  set.
- **4.** The options do not share grammatical form and register, or one is absurd, a joke, or wrong on spelling alone.
- **6.** A negative stem (it asks for the option that is NOT, or for the INCORRECTA one) whose negative word is not in
  capitals. A «no» inside a premise («si no se guarda…») is not a negative stem. The script flags candidates. You
  decide.
- **7.** The candidate copies or lightly rewords a question of the lesson's official pack: same fact, same angle and
  key, plus an official option carried over even when reworded. The same topic with new options and another angle
  passes.
- **8.** A typo, a missing accent, a stray character, or Spanish that is not Peninsular.
- **9.** The explanation does not say why the key is right **and** why each distractor is wrong, or it names an
  option by letter or position («la opción b», «la primera»). A distractor left unexplained, or dismissed only
  because the source is silent about it, fails. **Norm temas (bloque I, II.1–II.4), ruling of this round as in C1's
  R3 close:** when the cited text gives a single value («superior a 100.000 euros»), a single holder of the function
  («a las inspecciones generales de servicios») or a closed list, and the explanation quotes or states that rule, the
  rule itself excludes the distractors, so the explanation may then say they «no aparecen» in the precept. That
  passes. Ofimática stays strict: a help page that does not mention a feature does not show that it does not
  exist, so each distractor needs a page fact.
- **10.** (bloque I and II.1–II.4) The stem names a norm by an acronym or a short name instead of its BOE title (in
  the stem only: the explanation and citation may use acronyms). Number and date alone («Ley 39/2015, de 1 de
  octubre») pass. A stem that names no norm passes.
- **13.** An organ or ministry name that is not current, unless the stem dates the fact.
- **15.** A fact that expires without a change in the law («el plan vigente», «la última versión») and the stem does
  not date it.
- **16.** (ofimática, II.6–II.11) The stem does not name the application with its version. «Windows 11», «Word 365» or
  «Microsoft Word 365», «Excel 365», «Access 365», «Outlook 365» or «Outlook clásico/nuevo Outlook» with 365 all pass:
  the point is that the application and version are named. «configurado en español» is needed only when the key is a
  shortcut, key tip or format code whose characters differ by locale (Ctrl+B, Alt+H, `aa`) **and** the stem gives
  none. A translated UI label or menu path («Pausar actualizaciones») does not need it: the question is in Spanish
  (ruling of this round, 2026-11-07). II.5 and II.12 concept questions name no
  application and pass without one. (Ruling of this round: the «Microsoft» prefix is not required.)
- **17 (part).** A label or behaviour the stem presents as Windows 11 / Microsoft 365 but the explanation shows to be
  Windows 10 only, or a feature that differs between classic and new Outlook when the stem does not say which.
- **Standalone.** The stem needs a case scenario it does not contain («la empresa», «el funcionario del supuesto», a
  date or figure only the scenario gives). Candidates from a case are marked `[from case …]`.

Do not fail on anything else: not on length (the script checked it), not on the fact, not on taste. When unsure
whether a defect is real, PASS with a short note in `reason`.

## Final message

Per batch: checked, PASS, FAIL, and the FAIL count per item. Nothing else.
