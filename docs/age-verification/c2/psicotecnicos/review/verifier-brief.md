# Blind review of the psicotécnico goldens — verifier brief (round L review, 2026-11-07)

You are a blind verifier. You read generated exam items as a candidate and an examiner would. You do **not**
read the generator code (`backend/src/tradeschool/psicotecnico/`), its tests, or `docs/platform-delta-handoff.md`.

## Inputs

- The golden page(s) you are assigned: `docs/age-verification/c2/psicotecnicos/<generator>.md` (50 items each:
  seed, level, stem, options a–d, the key the solver computed, the explanation shown after answering).
- The official reference: `docs/age-c2-psicotecnico-index.md` — section 3 has, per type, what is asked, the
  parameters, the difficulty levels and one official question verbatim; section 4 the format rules (Spanish
  decimal comma, «41,40 €», «25,83 %», options short, stems 17–23 words, no calculator).

## For every item, decide

1. **Key.** Solve the item yourself from what is printed, before looking at the key. Recompute every number
   (use `python3 -c` freely; exact fractions where it matters). Is the printed key the *only defensible*
   answer? A FAIL if: the key is wrong; another option is also right under a reasonable reading; the stem
   admits two readings that give different answers; a series is continued just as well by another simple rule
   that leads to a different option; rounding/truncation makes two options defensible.
2. **Realism.** Against the official example(s) and parameters of the type: stem form and wording, length,
   option form (punctuation, units, decimals), magnitudes doable without a calculator in ~50 s, difficulty
   level plausible for the stated `nivel`. A FAIL only for a real departure a candidate would notice
   (an implausible situation, an impossible-looking number, an option format the official exams never use,
   a distractor so absurd the item is trivial, Spanish that is wrong or unnatural). Not for taste.
3. **Explanation.** Is it correct, and is it the rule the official exams use (the solving route a candidate
   would be taught), stated concretely? A FAIL if it is wrong, misleading (e.g. names a rule other than the
   evident one), or too vague to teach (e.g. «multiplicado por una constante» without saying which).

## Cause of each FAIL

- `generator`: comes from how the type is built — an ambiguous rule family, a distractor that can also be
  right, an unrealistic form, a wrong or vague explanation template, a level label that does not fit.
- `bank`: comes from one word-bank entry (a word, a synonym/antonym, a definition, a spelling pair).
- `other`: say what.

Group repeated FAILs: when the same defect recurs, give it one short id (e.g. `G1`) and reference it.

## Output

Write `docs/age-verification/c2/psicotecnicos/review/<generator>.md` per page:

```
# <generator> — blind review, pass <n> (2026-11-07)

Items read: 50. PASS: x. FAIL: y (generator: a, bank: b, other: c).

## Defects
- G1 (generator): <one sentence: what, why it matters, which items>. Suggested fix: <one sentence>.

## Items
| # | seed | verdict | cause | reason |
|---|---|---|---|---|
| 1 | 3604… | PASS | | key 445 (×2+3) only fit |
| 2 | … | FAIL | generator (G1) | … |
```

Every row has a reason, also for PASS (the computed answer or the deciding fact, a few words).
Write the file after each page so a cut loses at most one page. Use Spanish quotes and wording as printed.
Your final message: per page, counts and the defect list (ids, one line each). Nothing else.

## Verbal pages (sinónimos, antónimos, definiciones, ortografía)

The DLE is the authority, as in the official exams. Saved DLE pages (24.ª edición, consulted 2026-11-07) are in
`content/age-auxiliar-c2/sources/otros/dle/<palabra>.html`; `backend/src/tradeschool/psicotecnico/dle_relations.json`
is those pages parsed (per word: senses with number, text, «Sinónimos y afines» and «Antónimos y opuestos»; `absent`
when the DLE answers «no está en el Diccionario»). Use them, and your own knowledge of Spanish, to decide:

- sinónimos/antónimos: the key is a synonym/antonym in a current sense, and no distractor is one too (a distractor
  that the DLE lists as synonym/antonym of the stem, or whose definition coincides, is a FAIL);
- definiciones: the definition is the DLE's, and no other option fits it as well;
- ortografía: the misspelt form is not a DLE word or form (a conjugated form counts: «medico» is «medicar»), it breaks
  a rule of the Ortografía (b/v, h, g/j, x/s, ll/y, r/rr, m/n, tildes, diéresis), and the right forms are right; in
  a sentence, count every error yourself, including any not in the explanation.

Do not read `backend/src/tradeschool/psicotecnico/lexicon.py` or any generator: they are what you are checking.
On a re-read (pass 2) write the new review file; the pass-1 file is `<generator>.pass1.md`, don't read it first.
