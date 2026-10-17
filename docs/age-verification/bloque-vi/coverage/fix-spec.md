# Coverage fixes — writer and verifier spec (2026-10-17)

R2 rules apply: `docs/age-verification/bloque-vi/spec.md` (sources, item shape, labels as printed, «&» as printed,
Fuentes in order of first citation, voice). Helper scripts: `/tmp/claude-1000/-home-juanjo-PycharmProjects-curset/3bfdbef1-0a20-46f7-a34d-245ff55c6923/scratchpad/tools/`
(`pagetext.py FILE [REGEX]`, `fuentes_order.py LESSON [--write]`, `rewrap.py LESSON`; run with `python3 -I`).

**Writer.** For each row of `fixes.md` for your lessons: state the fact in the lesson, in the existing item for that
feature where there is one, or as a new item in the right section, cited to a saved page that states it literally.
Prefer a page already saved in `content/age-administrativo-c1/sources/otros/`; if none states it, save a new official
page there (curl, final URL, Spanish) and record it in your notes as a fuentes.yaml entry (file, url, title, consultado
"2026-10-17", sha256, lessons) — do not edit `fuentes.yaml` yourself; the coordinator merges. If no official page states
the fact, do not write it: record it as «sin fuente oficial». Each lesson stays ≤ 1,500 words (`wc -w`). Pay for
additions by cutting, in this order: wording inside items; detail asked only in 2020 or never asked that is not the
only item for a programme-named feature. Never cut a fact a 2022–2025 exam asked (see this folder's coverage reports,
column «Where in the lesson») or a feature's only item. Lines ≤ 120 chars; Fuentes complete and in order. Write
`fix-m06-lNN.md` in this folder per lesson: each change as old → new with its source passage quoted, each cut, new
sources, word count.

**Verifier (blind).** For each change in `fix-m06-lNN.md`: the claim is literally on the cited page; the fact asked
(coverage report row) is now stated; no cut removed a 2022–2025 asked fact (re-check every covered row of the lesson's
coverage report against the lesson as it now stands); form (words, lines, Fuentes order, list-shape hygiene, voice).
Write `verify-fix-m06-lNN.md`: PASS/FAIL table with reason and replacement, counts.

## Rule change (2026-10-17, requirements v1.5): no word ceilings

Do not cut anything for length; lessons may grow past 1,500 words. Undo any cut you already made for these fixes.
Also **restore** what earlier passes cut for space when `docs/age-ofimatica-index.md` shows an exam (any year, 2020
included; annulled questions included; not `función retirada`) asked it. The cut lists: the ledger
(`docs/age-theory-ledger.md`, bloque VI, «Cut for length» under Open items, and «Decisions after bloque VI» item 4), the
«Cuts» sections of the writer notes in `docs/age-verification/bloque-vi/m06-lNN.md`, and `recheck-queue.md` (cuts made
during fixes). Coordinator decision: the two m06-l02 dialog-box keys («Barra espaciadora marca una casilla; Esc descarta
el cuadro») and the desktop icon sizes («Clic derecho en el escritorio › Ver: tamaño grande, mediano o pequeño y Mostrar
iconos del escritorio») are restored too, although the index lists dialog boxes and desktop icons as never asked; the
m06-l02 Narrador fact is already back. Each restored item follows the R2 rules (its page saved and indexed — re-save a
page that was deleted when the item was cut — and stated as the page states it). List restorations in
`fix-m06-lNN.md` with the exam rows that asked them. Facts on the «Sin fuente oficial» list stay out.
