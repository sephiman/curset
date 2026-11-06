# Excerpt verification — follow-up sample (2026-11-06)

Blind check of `excerpts-sample.jsonl` (29 items) under `../../excerpts/verifier-spec.md`, with the November
future-wording rule: for LGSS arts. 144, 169, 171, 172, 173, 309, art. 19 RDL 4/2000 and art. 23 Reglamento del
Congreso, the fact must be in the wording from 01-12-2026 / the XVI legislatura. Every cited unit was compared with
the course copy (`pdftotext -layout`):

- `BOE-A-1982-5196_reglamento-congreso_2026-07-28.pdf` (art. 23, XVI legislatura wording + «Redacción anterior»)
- `BOE-A-1997-25336_ley-gobierno_2025-01-03.pdf` (art. 26.6)
- `BOE-A-2017-12902_lcsp_2026-04-09.pdf` (art. 159)
- `BOE-A-1985-151_ley-incompatibilidades_2024-06-08.pdf` (art. 16, conditional TREBEP wording + «Redacción anterior»)
- `BOE-A-2000-12140_trlssfce_2026-10-21.pdf` (art. 19, wording from 01-12-2026 + «Redacción anterior»)
- `BOE-A-2015-11724_lgss_2026-10-21.pdf` (arts. 169, 171, 172, 173, wording from 01-12-2026 + «Redacción anterior»)

Columns: **verdict** (yes / full-only / no); **old** = superseded wording in `excerpt_text` / `excerpt_full`;
**apartado** = the excerpt shows the apartado the citation names.

| n | key | citation | verdict | old wording | right apartado | note |
|---|---|---|---|---|---|---|
| 1 | m01-l03-q042 | 23.1 Regl. Congreso | yes | none (XVI wording only; «15 por 100 / 5 por 100» old text absent) | yes | «no inferior a quince» |
| 2 | m01-l03-q043 | 23.1 Regl. Congreso | yes | none | yes | «no inferior a cinco … media del 10 por 100 … circunscripciones en que hubieren obtenido representación» (XVI wording) |
| 3 | m03-l01-q056 | 26.6 Ley 50/1997 | yes | none | yes | Shown paragraph is the 2nd paragraph of apartado 6 in the source; the excerpt omits the «6.» lead paragraph, so the number is not visible (flag, minor) |
| 4 | m03-l01-q057 | 26.6 Ley 50/1997 | yes | none | yes | Same as 3 |
| 5 | m03-l04-q129 | 159.4.f) LCSP | yes | none | yes, with gap | Shows «4.» lead then «4.º Requerir … siete días hábiles»; the «f) … la mesa procederá a:» lead-in that 4.º hangs from is dropped, so the reader cannot see the 4.º is in letter f) (flag) |
| 6 | m03-l04-q132 | 159.6 LCSP | yes | none | yes | 159.6 lead + a) «el plazo será de 5 días hábiles» |
| 7 | m03-l04-q136 | 159.6 LCSP | yes | none | yes | 159.6 lead + f) «No se requerirá la constitución de garantía definitiva» |
| 8 | m04-l06-q044 | 16.1 Ley 53/1984 | yes | yes, both; labelled «Redacción anterior:» and after the new wording — OK under the conditional note | yes | «incluyan el factor de incompatibilidad» |
| 9 | m04-l06-q045 | 16.1 Ley 53/1984 | yes | yes, both; labelled and after the new — OK (and the key rests on it: question asks for the redacción anterior) | yes | «complementos específicos o concepto equiparable» |
| 10 | m04-l06-q046 | 16.1 Ley 53/1984 | yes | yes, both; labelled and after — OK | yes | «al personal directivo, incluido … alta dirección» |
| 11 | m04-l06-q047 | 16.4 Ley 53/1984 | yes | text: none; full: 16.1 old wording, labelled and after the new — OK | yes | «30 por 100 … excluidos … antigüedad» |
| 12 | m04-l06-q048 | 16.4 Ley 53/1984 | yes | as 11 — OK | yes | same fact |
| 13 | m04-l06-q049 | 16.4 Ley 53/1984 | yes | as 11 — OK | yes | «para el ejercicio de actividades privadas» |
| 14 | m04-l07-q031 | 19.1 RDL 4/2000 | yes | none (01-12-2026 wording: «169.1.a), 1.ª, 2.ª, 4.ª y 5.ª»; old «párrafos segundo y tercero» absent) | yes | «asistencia sanitaria … Mutualidad … licencia por enfermedad» |
| 15 | m04-l07-q032 | 19.3 RDL 4/2000 | yes | none | yes | «órganos administrativos con competencia en materias de gestión de personal» |
| 16 | m04-l09-q018 | 169.1.a) LGSS | yes | none (new wording «otros 180 días»; old «ciento ochenta días» absent) | yes | Same figure; key spells it out |
| 17 | m04-l09-q019 | 169.1.a) LGSS | yes | none | yes | «cuando se presuma … alta médica por curación» |
| 18 | m04-l09-q020 | 169.1.a) LGSS | yes | none | yes | «reciba asistencia sanitaria … y esté impedido para el trabajo» |
| 19 | m04-l09-q021 | 169.1.b) LGSS | yes | none | yes | «1.» lead + b) «ciento ochenta días, prorrogables por otros ciento ochenta» |
| 20 | m04-l09-q022 | 172 LGSS | yes | none (new «180 días … 169.1.a).1.ª, 3.ª, 4.ª y 5.ª») | yes | full = null (whole unit shown) |
| 21 | m04-l09-q023 | 172 LGSS | yes | none | yes | b) «no se exigirá ningún período previo» |
| 22 | m04-l09-q024 | 171 LGSS | yes | none (new «169.1.a).3.ª»; old «No obstante … párrafo cuarto» absent) | yes | «cien por ciento de la base reguladora … contingencias comunes» |
| 23 | m04-l09-q026 | 173.1 LGSS | yes | none | yes | «a partir del cuarto día … del cuarto al decimoquinto … a cargo del empresario» |
| 24 | m04-l09-q027 | 173.1 LGSS | yes | none | yes | same paragraph |
| 25 | m04-l09-q028 | 173.1 LGSS | yes | none | yes | AT: «desde el día siguiente al de la baja» |
| 26 | m04-l09-q077 | 173.1 LGSS | yes | none (new 3rd paragraph; old «desde el mismo día de baja» paragraphs absent) | yes | «a cargo de la entidad gestora o colaboradora … desde el día siguiente … salario íntegro … día de la baja» |
| 27 | sp-04/q12 | 173.1 LGSS | yes | none | yes | «del cuarto al decimoquinto … a cargo del empresario» |
| 28 | sp-04/q13 | 172 LGSS | yes | none | yes | b) accidente, sea o no de trabajo |
| 29 | sp-05/q23 | 16.4 Ley 53/1984 | yes | as 11 — OK | yes | «30 por 100 … excluidos … antigüedad» |

## Summary

- yes: 29 · full-only: 0 · no: 0.
- Future wording: every LGSS / RDL 4/2000 / Reglamento del Congreso excerpt carries the 01-12-2026 / XVI
  legislatura text; no «Redacción anterior» of those norms appears in any `excerpt_text` or `excerpt_full`.
- Old wording present only in art. 16 Ley 53/1984 (items 8–13, 29), always labelled «Redacción anterior:» and after
  the new wording, as the conditional note allows. The BOE «Téngase en cuenta…» note itself is not reproduced.
- No garbled text, page headers, or «►M» markers. Every excerpt is the unit its heading names.

## Flags (fact present, context incomplete)

- **Missing intermediate lead-in** — item 5 (159.4.f LCSP): «4.» is followed directly by «4.º», dropping the
  letter f) paragraph that the numbered steps belong to.
- **Missing apartado number** — items 3, 4 (26.6 Ley 50/1997): the excerpt shows only apartado 6's second paragraph,
  with no «6.» lead; content is correct but unlabelled.
