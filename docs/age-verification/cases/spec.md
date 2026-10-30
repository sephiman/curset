# Writer spec — supuestos prácticos (R4, 2026-10-28)

You write one or more cases of the course `content/age-administrativo-c1`: a scenario and 20 questions each. Do not
commit. Do not edit lessons, content, exercises, tests or goldens; write only `docs/age-verification/cases/sp-NN.draft.json`
and `sp-NN.writer-notes.md`, and your generator scripts in your own scratchpad subfolder (`<scratchpad>/sp-NN/`).

## Read first (once per run)

`CLAUDE.md`; `docs/prose-voice.md` (the «never does» list is a hard constraint on the scenario and the
explanations); `docs/age-exam-style.md` whole (§ 11 supuestos, § 12 checklist); `docs/age-bank-plan.md` § 3;
`docs/age-verification/bank/bloque-ii/spec.md` (the bank's writer spec: every question rule there applies here
unless this page says otherwise); `docs/age-verification/cases/plan.md` (your case's brief) and `slots.tsv` (its
tema slots). Read one official supuesto for the shape: `pdftotext -layout` of
`content/age-administrativo-c1/sources/examenes-oficiales/2026-05-23_conv2025_modeloA_cuestionario.pdf`, from
«SUPUESTO I» to the end. For each question: the tema's lesson (`es/lessons/mBB-lTT.md`, grep the section you need)
and the cited article in `sources/normativa/` read with `pdftotext -layout` (the file named in
`sources/normativa.yaml`, the later version where `cambios_pendientes` applies). Facts come from the norm the
lesson cites, never from memory or an official key.

Tema → lesson: II.1 `m02-l01` … II.4 `m02-l04`; III.1 `m03-l01` … III.7 `m03-l07`; IV.1 `m04-l01` … IV.9 `m04-l09`;
V.1 `m05-l01` … V.6 `m05-l06`.

## The scenario

- 300–550 words of plain narrative in the present or past tense, as § 11 describes. Fictional people (first name +
  two surnames, never a known public figure; one name each, kept through the case), a real AGE body with its current
  name, and several threads (a citizen's request or a file, a contract, a budget shortage, a staff situation) as the
  brief lists. It ends with «Se plantean las siguientes cuestiones:».
- It states every fact the questions need: dates with weekday and year («el lunes, 8 de febrero de 2027»), amounts
  in euros, budget items, corps, posts, levels, organs, the town where the office is. It says which festivos fall in
  the periods the questions count, or that there are none besides the national ones listed in the plan. No fact a
  question needs may be missing; none may contradict another.
- A question may add a fact in its stem («El jueves, 4 de marzo de 2027, la empresa…»), as the official cases do.
- No real person, no real company (invent companies with «S.L.»/«S.A.»), no real private address.

## The questions

Twenty per case, `q01` … `q20` in the order shown. The order follows the scenario's threads (procedure first, then
contract, staff, budget, as the official cases do), not the slot list. Each question follows every rule of the bank
spec (four options; one correct under the cited text and every other norm in force; citation as the lesson writes
it and cited in that lesson's prose; options 5–20 words, statements to 40; distractor patterns; no article-number
option; no «ninguna/todas»; current organ names; explanation names options by content, never by letter or position;
negative stems at most one per case, in capitals), with these differences:

- **Depends on the scenario.** Every question needs at least one fact of the scenario (a date, an amount, the kind
  of body, the person's situation, the contract's type or value) to be answered. A question a candidate could answer
  without reading the scenario fails. Record the scenario sentence(s) it needs in `depends_on`. A question may also
  depend on the previous one («dicho suplemento»); it then says so in the stem and names it in `follows`.
- **Stem** 20–50 words. Forms, over the case: mostly direct questions (`directa`, about 55 %), «Señale la respuesta
  correcta» (`senale`, about 10 %), statements to complete (`enunciado`, about 10 %), the article named
  (`art-pregunta`/`art-completar`, about 20 %), `cual` the rest. A stem that names a norm uses its BOE title, or
  number and date when the title would push past 50 words.
- **Computations.** At least 10 of the 20 compute a date or an amount (`computes`: `date` or `amount`; tag `cómputo`
  for dates, `cantidad` for amounts). Dates: the scenario or stem gives every date the count needs; the kind of day
  is the norm's (hábiles: no sábados, domingos or festivos; naturales; months date to date, last day of the month if
  that day does not exist; a last day inhábil moves to the next hábil; August hábil in administrative procedure,
  inhábil for the contencioso, art. 128.2 LJCA; the norm's special rule where it has one, e.g. LCSP disposición
  adicional duodécima). Check every weekday and every count with Python `datetime`, never by hand. The four options
  are dates of the same form («El lunes, 22 de marzo de 2027.») built from the plausible miscounts (naturales for
  hábiles, the first day counted, the month counted as 30 days, the festivo ignored). Amounts: the scenario gives
  every figure; the options are amounts from the plausible slips (IVA included or not, prórrogas left out, the wrong
  percentage). The explanation shows the count step by step.
- **Spread over the case:** difficulty about 30/50/20 % (computations with a trap are 3); key position a/b/c/d 3–7
  each; the key strictly the longest option in at most 6 of 20, strictly the shortest in at most 6.
- **Not official.** Compare each question with the tema's official questions in
  `docs/age-verification/bank/official/<tema>.md` (supuesto questions included). A computation with an official
  case's shape and new figures is still a rewording: change the angle (another plazo, another starting fact,
  another figure) and never carry over the official key with an official distractor.
- **Lesson anchor.** `lesson` is the lesson whose prose cites your citation (normally the tema's). Check it resolves:
  from `backend/`, `uv run python ../docs/age-verification/cases/tools/case_check.py sp-NN --anchors`. Zero misses.

## Rulings of 2026-10-28 (user) — these override the two sections below where they read stricter

- **Dependence** as the style guide § 11 describes it: the scenario is context; a stem may carry the facts, as the
  official cases do. A question fails only when it uses no case fact at all (scenario or stem) or contradicts the
  scenario. Still write questions that use the case: the person, the body, the file, the dates, the figures.
- **Copies** are judged on the stem and options against the official question, not on the kind of computation. The
  same kind of plazo or amount with the case's own dates and figures is not a copy; an official stem with the same
  option set, or the official key with an official distractor in a near-identical stem, still is.
- **Sectoral law.** A scenario fact governed by a norm outside the course (water, traffic, the body's statute:
  infraction classes and fine ceilings, who ends the vía administrativa) must agree with that norm; when unsure,
  leave the figure out. Never let a figure break the LGP (obligations above the credit) or the LCSP's own conditions
  (a DA 15.ª count needs the publication fact).
- **Taken twice already:** the global amount of anticipos de caja fija (7 % of capítulo 2, with 5 % as a distractor) is official 2024 extr. P1 q39 — do not ask it. State the contract procedure (abierto, restringido…) and whether electronic offers are accepted whenever a licitación plazo is asked.
- **Repeat faults (sp-07, sp-10):** art. 158.1 LCSP's fifteen days are naturales (DA 12.ª) — in an explanation too; a reintegro de subvención ends the vía administrativa (art. 42.5 Ley 38/2003): reposición, not alzada; a ministerial act that confirms an organismo's act goes to the Juzgados Centrales (art. 9.1.c LJCA), not the Audiencia Nacional — keep the contencioso court out of the case unless the lesson states the rule; name RD 2188/1995, RD 725/1989 and RD 462/2002 by their full BOE titles when the stem stays within 50 words.
- **Official shapes taken (verifiers, cases sp-05, sp-14, sp-16):** which artículo (62/63/22) an equipment purchase is imputed to (conv2025_X·S1·6); «sin modificación, ¿a qué nivel vincula?» with capítulo/concepto options (conv2024_X·S2·R4). Do not ask them.
- **Saturated:** the plurianual limit of art. 47.2 LGP is asked in nine cases already; do not ask it again.
- **What is taken:** before choosing each question, grep `kept-index.tsv` (regenerate it first: `python3 docs/age-verification/cases/tools/kept_index.py`) for its citation; if another case asks the same fact from the same angle, choose another fact or angle.
- **No reuse across cases.** Never copy another case's question, dates or option set (sp-07 q07 was dropped for
  repeating sp-05 q07 with another company's name). `case_check.py` prints `DUPLICATE` for a shared option set.
- **Replace, don't rewrite.** A case with more than five drops gets replacements in batches; passed questions stay.
  Replacement ids continue from the case's highest id.

## Lessons from sp-01 (verifier, 2026-10-28: 7 of 20 dropped, case rewritten)

- **Do not restate the scenario in the stem.** A stem that repeats every figure the answer needs, or whose options
  name the facts, stands alone and fails dependence. Leave the deciding fact (the date, the amount, the body's
  kind, the person's situation) in the scenario and refer to it («el contrato de obras», «la solicitud de la
  empresa»). A stem may add one new fact, not re-tell the old ones.
- **Official computation shapes are taken.** These are reworded copies even with new dates or figures: the last day
  to correct a request under art. 68 LPAC; the last day for an alzada of one month; the garantía definitiva or a
  modification amount from a base with IVA; how a suplemento de crédito is financed («dicho suplemento»); the last
  day of toma de posesión with change of residence. Read the official supuestos of your temas
  (`bank/official/<tema>.md`) before choosing your computations, and pick other plazos, other starting facts,
  other figures (e.g. the date the silence arises, the date a caducidad is declared, the date the recurso especial
  closes, a penalidad accumulated to a date, the dieta for a trip with given times).
- **Festivos statement.** Say exactly which days are inhábiles in the windows you count. Mind Jueves Santo and
  Viernes Santo (25–26 March 2027) and any month-counted window that crosses them; do not write «no more inhábiles
  than weekends» unless it is true for every window.
- **Citation of the rule that decides.** If the key rests on a second rule (another regla, another article), cite
  that one or change the question; and check the norm applies to the body (the IOC covers the AGE's own services,
  not an organismo autónomo's accounting).
- Punctuation in dated phrases: «el viernes, 2 de julio de 2027, a …». Every full date carries its weekday.

## Self-test before hand-back (after sp-03 and sp-04, 2026-10-28: 8 and 5 drops)

Most drops are the same two faults. Before hand-back, for **each** question write in the notes one line:

1. **Stem only.** Cover the scenario and read the stem and options: can the cited article alone pick the key? If
   yes, the question fails. Typical failures: the stem names the procedure or figure that decides («procedimiento
   sancionador», «declara urgente», «ingresos por matrícula»); the plazo is fixed by the norm whatever the facts
   («dentro del mes siguiente»); the competent organ is the same for every body. Make the deciding fact one that
   only the scenario gives (which body it is — department or organismo autónomo —, which contract type and value,
   which date the act was notified, which situation the person is in), and keep it out of the stem.
2. **Official twin.** Name the closest official question in `bank/official/<tema>.md` (supuesto questions
   included) and say what differs. If the key rule and any one distractor are the same, change the angle. Taken
   shapes so far, besides those above: when the decision must be notified when the norm fixes no plazo (three
   months); what the valor estimado includes (IVA, prórrogas), in words or in figures; who approves, recognises and
   pays in an organismo autónomo; last day of a one-year claim from the alta.
3. **Grammar of the completed stem.** A stem ending in «el:» with options starting «El …» reads «el El»; end the
   stem without the article.
4. **Norm named in full** at its first mention in a stem: «el Reglamento (UE) 2016/679 del Parlamento Europeo y del
   Consejo, de 27 de abril de 2016, …» (or describe it without naming it).
5. **Body names** in the stem match the scenario's body.

**Festivos sentence (use this form).** Name the place, then list every festivo inside every window you count, by
date, both national and the place's own (Madrid 2027: 2 May falls on Sunday and moves per the Comunidad's calendar
— avoid windows in early May; 15 May San Isidro; 9 Nov Almudena), or say «ningún festivo cae dentro de los plazos
por días; los plazos por meses o años terminan en día hábil». Check it by script over every window of every question.

## Draft file

`docs/age-verification/cases/sp-NN.draft.json`, written with `json.dump(..., ensure_ascii=False, indent=1)`:

```json
{
 "case": "sp-01",
 "title": "La autorización de vertido",
 "scenario": "Doña … \n\nSe plantean las siguientes cuestiones:",
 "festivos": "Madrid, 2027: ninguno en los periodos que cuentan las cuestiones salvo …",
 "questions": [
  {"id": "q01", "bloque": "III", "tema": "III.3", "lesson": "m03-l03", "section": "…",
   "citation": "art. 68.1 LPAC", "stem_form": "directa", "names_article": false, "negative": false,
   "prompt": "…", "options": {"a": "…", "b": "…", "c": "…", "d": "…"}, "correct": "b",
   "difficulty": 2, "tags": ["plazo", "cómputo"], "distractor_pattern": "otro-plazo",
   "computes": "date", "depends_on": ["…scenario sentence…"], "follows": null,
   "explanation": "…", "source_quote": "…", "covers": []}
 ]
}
```

Title: a short noun phrase naming the case's main matter (2–6 words, Spanish sentence case). Scenario paragraphs are
separated by a blank line (`\n\n`). `section`, `stem_form`, `tags`, `distractor_pattern`, `source_quote`, `covers`
as in the bank spec. Set `correct` in your script from the key's text, never by hand, and print each stem with its
keyed option before hand-back.

## Before hand-back

Run, from `backend/`: `uv run python ../docs/age-verification/cases/tools/case_check.py sp-NN --anchors`. It checks
the fields, the weekday of every dated phrase, festivos named, stem and option lengths, the lint patterns of the
bank, the explanation letters, the computations count, key position and length spread, and the anchors. Fix every
flag that is a real fault. Check by script that every `source_quote` is an exact substring of the pdftotext output
(whitespace normalised).

`sp-NN.writer-notes.md`: lesson/norm disagreements found, slots moved, facts you wanted but the lesson lacks, the
check output. After each case, append one line to `docs/age-cases-ledger.md` under «Progress» (`sp-NN written:
<title>, 20 questions, <k> computations`) so a cut run loses at most one case.

## Replacements

When a verifier drops questions, you write replacements under new ids (`q21`, `q22` … never reusing a dropped id),
each with `"replaces": "<dropped id>"` so the build puts it in the dropped question's place. A replacement must keep
the case's slots and computation count. A scenario fault the verifier reports is fixed in the scenario itself (it is
not a question); list the sentences you changed in the notes so the affected questions are re-checked.

Final message to the coordinator: per case, title, 20 written, computations, the check's summary line, any blocker.
Keep it short.
