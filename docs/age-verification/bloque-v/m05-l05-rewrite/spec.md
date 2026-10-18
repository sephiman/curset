# m05-l05 rewrite (tema V.5) and the move from m05-l03 (tema V.3) — spec, 2026-10-18

Course `content/age-administrativo-c1` (C below). Nothing is committed. Session scratchpad: given in each prompt (SP);
norm texts already extracted with `pdftotext -layout` in `SP/txt/`, exam texts in `SP/exams/`.

## Why

R2b coverage audit (`docs/age-scope-audit.md`, Part B; `docs/age-verification/audit-2026-10/coverage/m05-l05.md`):
m05-l05 missed 64.7 % of the 2022–2025 facts asked of it. The regime of pagos a justificar and anticipos de caja fija
sat in m05-l03; the programme (`C/sources/programa.md`, V.5) assigns «Anticipos de caja fija», «Pagos "a justificar"»
and «Justificación de libramientos» to V.5.

## What was done (writer)

- m05-l05 holds, in full, what the V.5 sentence names. Sections 1–4 (clasificación económica, pagos: concepto y tipos)
  are unchanged. Sections 5–8 are rebuilt from the governing norms in their article order: «Pagos por obligaciones
  presupuestarias» (apartados séptimo.1.3, séptimo.5, décimo Orden PRE/1576/2002); «Anticipos de caja fija» (art. 78
  LGP; RD 725/1989 arts. 1–7 and 9; reglas 34–36 IOC; apartado décimo.2 Orden de documentos contables) with a worked
  example; «Pagos "a justificar"» (art. 79.1–3, 79.5 LGP; RD 640/1987 arts. 1, 3–7, 9; reglas 28, 29, 33 IOC);
  «Justificación de libramientos» (arts. 73.4, 79.3–4, 79.6 LGP; RD 640/1987 arts. 10 and 12; reglas 30–32, 61.1 IOC;
  apartado décimo.1 Orden de documentos contables; apartado noveno.2.5 Orden PRE/1576/2002). New «Lo que más cae».
- m05-l03 keeps the fases del gasto and everything else; it loses the two `###` sections «Pagos a justificar» and
  «Anticipos de caja fija» (with the worked plazo example), and gets one line under «Perceptores»: «El régimen de los
  pagos a justificar y de los anticipos de caja fija está en m05-l05.» Its intro, «Lo que más cae» and «Normativa» are
  adjusted. The perceptores list (apartado séptimo.2, which names ACF and pagos a justificar among the agentes
  mediadores) and art. 151 LGP (gastos menores de 5.000 euros pagados por ACF, not subject to fiscalización previa)
  stay in m05-l03: the programme gives perceptores and control to V.3.
- Glossary: g-anticipo-de-caja-fija and g-pago-a-justificar move origin m05-l03 → m05-l05 (definitions unchanged; they
  cite art. 78.1 and 79.1–2 LGP, both cited in m05-l05). g-servicios-comunes gets `link_except` m05-l05 (Seguridad
  Social sense, as in m05-l03).
- course.yaml: new summaries for m05-l03 and m05-l05.

## R2 rules

- Every fact copied from the article, verbatim or a faithful shortening that keeps every number, plazo, organ,
  majority, condition and exception; cited inline. Sources: `C/sources/normativa/` only (texts in `SP/txt/`).
- No duplication: a fact lives in the lesson the programme assigns it to.
- «(desde 28-10-2026)» marks the RD 813/2026 wording (art. 6 RD 640/1987, art. 6.3 RD 725/1989).
- Voice: `docs/prose-voice.md` «never does» list is a hard constraint; `CLAUDE.md` (no invented vocabulary; Peninsular
  Spanish).

## Blind review (reviewer did not write the text)

For **every** sentence, table row/cell, list item, worked-example step and «Lo que más cae» line of m05-l05 sections
5–8 and of the whole of m05-l03 that carries a number, plazo, amount, percentage, organ, date, exception, condition or
list: open the cited article and write PASS or FAIL, with the article passage for a FAIL and a replacement in the
lesson's style. Also check: every citation points to the article that says it; the Normativa blocks match the citations
in the text (no article cited and missing, none listed and not cited); the worked examples recomputed; the course.yaml
summaries (three sentences at most, nothing the lesson does not say); the glossary origin changes; voice and Spanish.
Sections 1–4 of m05-l05 are unchanged from the verified R2 text: check only that nothing there now contradicts or
duplicates sections 5–8.

Report: `docs/age-verification/bloque-v/m05-l05-rewrite/verify-m05-l05.md` and `verify-m05-l03.md`, a table
`| # | quote (short) | citation | PASS/FAIL | passage / reason | replacement |`, then counts.

## Coverage re-check

Method of `docs/age-verification/audit-2026-10/coverage/spec.md`, on both lessons, population 2022–2025 (conv2025_A,
conv2025_X, conv2024_A, conv2024_X, conv2022, conv2022_X; all six tables), rows whose first tema is V.3 or V.5:
asked, covered, partial, miss. Reports `coverage-m05-l05.md`, `coverage-m05-l03.md` in this folder.
