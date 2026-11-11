# R2c esquemas, AEAT (`aeat-agentes-hacienda`) — spec, 2026-11-11

Requirements `docs/aeat-agentes-course-requirements.md` R2.3 (provenance) and R4.5 (esquemas as C1 4a). Nothing is
committed. Read once per agent run: this file; `docs/age-verification/bloque-i/esquemas/spec.md` sections «Rule» and
«Platform limits» (C1's rule, which applies unchanged); `CLAUDE.md` (writing rule) and `docs/prose-voice.md` (titles and
labels follow it); `docs/age-verification/aeat/r2-tax/spec.md` only for how to read the norm files.

## Rule (C1's, in short)

Every cell, node or step is a verbatim fragment of the norm or of the lesson's own wording, with its citation; no new
fact; **no citation the lesson's prose does not carry inline** (the load fails otherwise); one norm per row; no order the
text does not support (`plazos`, `pasos`), no false dependency (`arbol`); a title never makes a selective list read as
complete («Algunos…» where it is selective); every row keeps the article's conditions and exceptions, or carries the
condition in its label so it never reads wider than the article; an esquema follows the paragraphs it summarises
(placed right after them); **one to four per lesson**, none where the prose is narrative or already a list or table of
its own. Annual figures keep the year and the norm that sets them, as the prose has them.

**Where the prose has the same gap as a row** (a condition, exception or fact the row needs and the prose leaves out):
do not write the row and do not touch the prose; list the gap in your notes (lesson, article, what is missing). The
coordinator fixes the prose first under the R2 rules and then the row can be written.

## Syntax

```
:::esquema{kind=tabla title="…"}
| Header | Header | Cita |
|---|---|---|
| … | … | art. 62.2.a) LGT |
:::
```

`kind=plazos`: `1. Label — plazo (art. N Norma)` (2 fields); `kind=pasos`: `1. Label — what — who (art. N Norma)` (3
fields); `kind=arbol`: `- Node — text (art. N Norma)` nested by two spaces (1–2 fields). Field separator « — »; no other
spaced em dash inside a field. A list row's citation cannot end in a letter «f)»: cite the apartado without the letter;
tables may cite letters. Look at existing esquemas in `content/aeat-agentes-hacienda/es/lessons/m02-l05.md` and
`m02-l02.md`.

## What R4.5 asks for (tax part, all new)

- III.9: plazos de pago in período voluntario (art. 62.1–2 LGT and what else the lesson states). III.11: plazos de pago
  of the providencia de apremio (art. 62.5 LGT) and the recargos del período ejecutivo (art. 28 LGT).
- Recargos por declaración extemporánea of art. 27 LGT, in the lesson that states them.
- III.13: types of infractions (leve, grave, muy grave), sanctions and the reductions (art. 188 LGT).
- III.7, III.8, III.11–III.12: the procedures of gestión, inspección and recaudación with their plazos and effects
  (iniciación, plazos de resolución, effects of the lapse of the plazo).
- III.14: recursos and reclamaciones with plazo, organ and effects.
- III.2: órganos of the AEAT (an `arbol` only where the text says what belongs to what).
- III.15–III.20: for each tax its structure, one esquema each where the lesson states them: hecho imponible, sujeto
  pasivo / contribuyente, base, tipo, devengo, and the exenciones the programme names. III.20: deuda aduanera de
  importación y de exportación (nacimiento, deudor).
- Other temas (III.1, III.3–III.6, III.10): only where the prose lays out plazos, organs, kinds or phases (e.g.
  prescripción, plazos de resolución, clases de tributos).

Exam weight (`docs/age-verification/aeat/r2/questions/<lesson>.md`, coverage questions): plazos, percentages, organs and
kinds first.

## Writer

- Edit only esquema blocks of your lessons (`content/aeat-agentes-hacienda/es/lessons/<lesson>.md`); no prose, no «Lo
  que más cae», no «Normativa». Do not touch the `:::note` blocks.
- After each lesson, from `backend/`: `uv run pytest tests/test_esquema.py -q` (must pass) and
  `uv run python ../docs/age-verification/aeat/r2-tax/tools/taxprov.py plan <lesson>`: the lesson's
  `docs/age-verification/aeat/r2-tax/<lesson>/pending.md` must list only your new rows (titles are not listed; table
  header rows are). `tests/test_citations.py` will fail on the citations golden: expected, the coordinator regenerates
  it. Any other failure is yours.
- Notes per lesson in `docs/age-verification/aeat/r2c/writer-<your range>.md`, written after each lesson: each esquema
  (title, kind, placement: the line it follows), the paragraphs and articles it summarises, esquemas considered and not
  made (why; «narrative» or «the prose is already a table» are reasons), and prose gaps found (see Rule).

## Verifier (coordinator launches it; Opus, blind)

Checks every new row and every title against the cited article exactly as a sentence, as C1's spec «Verification»
says: verbatim fragment or faithful shortening keeping every number, plazo, organ, condition and exception; no wider
reading; right citation; fact already in the lesson's prose with that citation; no false order or dependency; title not
reading a selective list as complete; placement after the paragraphs summarised; one to four per lesson. Report per
lesson `docs/age-verification/aeat/r2-tax/<lesson>/verify-esquemas.md` (common part:
`docs/age-verification/aeat/r2/verify/r2c-esquemas.md`) with rows `| \`<10-hex id>\` | PASS|FAIL | reason | replacement |`
(ids from the pending file) and titles as `| title <lesson> «…» | PASS|FAIL | reason | replacement |`. Put only the
replacement text in the last column, no instructions. Fixes are re-checked by a different verifier
(`verify-esquemas-recheck-N.md`).
