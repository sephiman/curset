# R2c esquemas, C2 bloque I (`m01-l01` … `m01-l16`) — spec, 2026-11-06

Course `content/age-auxiliar-c2` (C2). Requirements: `docs/age-auxiliar-course-requirements.md` R2.3 (provenance) and
R4.1, which takes C1's section 4a (`docs/age-administrativo-course-requirements.md`). Nothing is committed.

## Rule

C1's esquema rule applies unchanged: read `docs/age-verification/bloque-i/esquemas/spec.md`, sections «Rule» and
«Platform limits». In short: every cell, node or step is a verbatim fragment of the norm or of the lesson's own
wording, with its citation; no new fact; no citation the lesson's prose does not carry inline; one norm per row; no
false order (`plazos`, `pasos`), no false dependency (`arbol`); a title never makes a selective list read as
complete; an esquema follows the paragraphs it summarises; one to four per lesson, none where the prose is narrative or
already a list or table of its own. The prose is not touched.

## Derive from C1 first (R2.3)

Each C2 lesson was written from the C1 lessons in the mapping table of `docs/age-verification/c2/bloque-i/spec.md`.
The esquemas of those C1 lessons (`:::esquema` blocks in `content/age-administrativo-c1/es/lessons/`) come first:

1. For each C1 esquema whose subject the C2 lesson covers, take its rows one by one. A row is **inherited** when it is
   copied **byte-identical** (the whole line, every cell, the citation as written) and (a) every fact of the row is
   stated in the C2 lesson's prose, and (b) the row's norm and article appear in a citation of the C2 prose. Provenance
   (`backend/scripts/provenance.py`) then finds it in C1 with the same text, citation and cited-file sha256 and records
   «verificado en C1». Header rows of tables are copied the same way.
2. A row whose fact C2 cut is dropped. Never edit a kept row to fit: a row whose text must change is a **new** row.
3. **New** rows (and whole new esquemas, where the C2 lesson lists plazos, organs, kinds or phases that no C1 esquema
   lays out) are allowed under the same rule; they go to the blind verifier. Prefer inherited rows; add new ones only
   where they earn their place.
4. The title (the `title=` of the fence) is not a sentence for provenance: keep C1's when the kept rows still make it
   accurate; otherwise write one that names exactly what the rows show. Every title, inherited or not, is checked by
   the verifier.
5. Place each esquema after the C2 paragraphs it summarises (not where it sat in C1).

Exam weight: bloque I questions are mostly organs, majorities and plazos (`docs/age-c2-exam-style.md`): those first.

## What the writer does, per lesson

- Edit only the esquema blocks of your lessons (`content/age-auxiliar-c2/es/lessons/<lesson>.md`); no prose, no
  «Lo que más cae», no Normativa.
- After each lesson, from `backend/`: `uv run pytest tests/test_esquema.py -q` (must pass), and
  `../docs/age-verification/c2/bloque-i/tools/prov.sh plan <c2 lesson> <c1 lessons of the mapping>`; the pending file
  `docs/age-verification/c2/bloque-i/pending/<lesson>.md` must list only your new rows (an inherited row that shows up
  there is not byte-identical, or its citation differs: fix the copy). Other pending sentences already listed there
  before you started are not yours (`m01-l05`, `m01-l06`, `m01-l13`, `m01-l15` have R2b notes and Normativa lines
  pending): leave them.
- `tests/test_citations.py` will fail on the citations golden (new esquema rows): expected, the coordinator
  regenerates it. Any other failure is yours.
- Notes per lesson in `docs/age-verification/c2/bloque-i/esquemas/writer-<your range>.md`: each esquema (title,
  kind, placement line), its C1 origin, rows inherited / dropped (why) / new, and esquemas considered and not made
  (why; «narrative» is a reason). Write after each lesson.

## Verification (coordinator launches it)

A blind reviewer (opus) checks every **new** row and every title against the cited article exactly as a sentence,
as C1's spec «Verification» says, and writes `docs/age-verification/c2/bloque-i/verify/esquemas-<range>.md` with the
table shape `| \`<10-hex id>\` | PASS|FAIL | …` (titles as `| title <lesson> «…» | PASS|FAIL | …`). Fixes are re-checked
by another reviewer. Then `provenance.py record` for every lesson; `test_provenance.py` must pass.
