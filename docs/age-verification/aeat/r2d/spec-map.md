# AEAT round R2d, step 1 — article map spec (no writing)

2026-11-14. Course `aeat-agentes-hacienda`. Requirements v1.2 (`docs/aeat-agentes-course-requirements.md`, R4.7–R4.9,
R3.5, R4.4). External review: `docs/aeat-external-review-2026-11.md` — a list of topics to check against the norms, never
a source. The academy material it names is never quoted, paraphrased or used as evidence.

You are a map auditor (blind to any later writer). You write **only** your map files
`docs/age-verification/aeat/r2d/<lesson>-map.md`. You never edit a lesson, a norm, `normativa.yaml` or anything else.

## Read once per run

- This file; `docs/aeat-agentes-course-requirements.md` §4 (R4.2–R4.9).
- The review sections for your temas (the review numbers temas «Tema 18» = III.18; «Lección 1» of part III = III.1;
  part II and part I sections by their own numbers).
- `docs/aeat-scope-audit.md`, «Sections removed» and «Sections kept by exam evidence» (R2b removed 13 sections + the art.
  167.3 list).
- `content/aeat-agentes-hacienda/sources/programa.md`, Anexo I (lines 208–360): your temas' programme text, verbatim.
- `content/aeat-agentes-hacienda/sources/normativa.yaml`: the entries of the norms your temas use (`short`, `aliases`,
  `file`, `note`, `cambios_pendientes`, `cifras_anuales`) and its header (unconvalidated RDLs).
- Per tema: the lesson `content/aeat-agentes-hacienda/es/lessons/<lesson>.md`; its question pack
  `docs/age-verification/aeat/r2/questions/<lesson>.md` (exam weight: coverage questions 2022–2025).

Norm texts: `pdftotext -layout content/aeat-agentes-hacienda/sources/normativa/<file> - | grep -n …`; for an `.html` file
strip tags with `python3 -I -c` and `html.parser`. The snapshot is the source of truth, never memory. If the governing
norm of a programme sentence is not in the snapshots (e.g. a tax the course never downloaded), say so under «Sources
missing» with the BOE id if you know it; do not fetch anything.

## Ranges

For each programme sentence (split the tema text at its full stops; «Recargos del período ejecutivo» is one sentence)
fix the governing article range:

- the articles of the governing law that regulate that matter, in the law's own grouping (capítulo/sección/article);
- the regulation articles that develop them **when they state a rule, plazo, amount, organ, list, document or effect**
  the law leaves to them (RGAT, RGR, RGRST, RGRVA, RIRPF, RIVA, RIS, CAU reglamentos). Purely internal procedure may be
  marked «out: organisational detail» with one line of reason;
- in doubt whether an article is inside a range: include it.

Legitimate reasons to leave an article of the range out: transitional (spent or of no current effect), organisational
detail, repealed / sin contenido, outside the epígrafe (say which epígrafe has it). Nothing else.

Exam weight decides depth, never presence: note per tema the number of coverage questions (pack) so the writer can
size each addition.

## Map file shape — `r2d/<lesson>-map.md`

```
# Article map — <tema> (`<lesson>`)

Programme: «<tema text verbatim>»
Exam weight: <n> coverage questions 2022–2025 (<depth: full ≥20 / standard 10–19 / focused <10>)
Lesson: <words> words (wc -w)

## 1. «<programme sentence>»
Governing: <norm short> arts. a–b; <reglamento> arts. c–d
| Article | Status | Lesson place (section / line) | Missing, or reason it stays out |
|---|---|---|---|
| art. 20.Uno LIVA | part | «Exenciones», l. 120–160 | 8.º–13.º, 23.º–27.º not given |
| art. 21 LIVA | not treated | — | exportaciones (viajeros 2.º) |
| art. 30 LIS | out: outside the epígrafe | — | III.17 has no «X»; … |
Status ∈ full · part · not treated · out: <reason>.
(one block per programme sentence)

## Enumerations
Every legal enumeration (lettered/numbered list, list of motives, requisites, organs, documents, exemptions,
infractions with sanctions) in the range's articles:
| Article | What it lists | Items in the norm | Items in the lesson | Whole? | Missing items (by number/letter) |

## «entre otros / entre otras / etc.» in the lesson
Every occurrence (grep the lesson):
| Line | Words around it | Stands for items of a legal list? (yes: which article / no: the norm's own words, or not a list) |

## Cross-references
Every reference to another lesson or tema («tema III.11», «(`m03-l11`)», «m01-l02», «se explica en…»):
| Line | Target | What the sentence promises | Target has it? (yes, line / NO: what is missing) |

## R2b removals inside this tema
For each section R2b removed from this lesson (scope audit): inside a programme sentence's range? yes/no and why.

## Review items
Every gap, alleged defect or doubt the review lists for this tema (and the general defects that apply to it: glossary
sense, numbered lists all «1.», mid-sentence titles, dense paragraphs, esquemas repeating one paragraph):
| # | Review says | Verdict | Evidence |
Verdict ∈ confirmed (against the norm and the lesson) · not confirmed (say why: the lesson has it at line N, or the norm
says otherwise) · outside every epígrafe. The review's unverified claims (2026 IS rates, 60 % Ceuta y Melilla,
250.000/125.000 and RDL 2/2026, RDL 29/2026) are checked against the snapshot or listed under «Sources missing».

## Readability
- Paragraphs over 120 words that string several rules (line, words, how many rules/citations).
- Esquemas (`:::esquema`) that only repeat one paragraph (an esquema must gather at least two paragraphs or articles).
- Markdown numbered lists with wrong numbering (all «1.» or skips).
- Ids `(m03-lNN)` / `` `m03-lNN` `` in running prose.

## Sources missing
Norms the ranges need that are not in `sources/normativa/` (title, BOE/CELEX id if known, for which sentence).

## Work list for step 2
Numbered, in the order a writer should do them, each tagged with the prompt letter:
(a) restore R2b removal · (b) complete enumeration · (c) treat article not treated / in part · (d) estimación objetiva
limits · (e) «No confundir» candidate (two neighbouring rules, both articles named; at most three per lesson) ·
(f) readability (split paragraph / remove esquema / remove id / numbering) · (g) fix cross-reference · (h) Normativa,
«Lo que más cae», course.yaml summary.
Each item: what, articles, depth (one line / paragraph / section / esquema), and why (map line).

## Counts
Articles in range: n · full n · part n · not treated n · out n. Enumerations: n, whole n, incomplete n.
«entre otros/otras/etc.» standing for a legal list: n. Cross-references: n, broken n. Review items: confirmed n · not
confirmed n · outside n. Work items: n.
```

Write the map file as you go (section by section) so a cut loses little. Finish with a one-paragraph summary in your
final message: per tema, the Counts line and the three biggest gaps.
