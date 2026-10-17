# Coverage check 2022–2025 (R2b, Part B, bloques I–V) — auditor spec

Date 2026-10-17. Read-only: edit no lesson and no repo file other than your own report; commit nothing. Method reused
from `docs/age-verification/bloque-vi/coverage/spec.md`.

**Population.** Every row of `docs/age-official-exams-ledger.md` in the questionnaires conv2025_A, conv2025_X,
conv2024_A, conv2024_X, conv2022 and conv2022_X (modelo B repeats modelo A: use modelo A; conv2020 is «programa
anterior» and is left out, as in bloque VI), in all six tables of each (Primera parte, Supuesto I, Supuesto II and
their reserve tables), whose Tema is in your bloque (first tema when it says «X (o Y)») and whose Estado is `vigente`
or `vigente-con-nota`. Left out: `anulada`, `dudosa`, `norma modificada…`, `función retirada`, `fuera de temario`.
The owner lesson is that tema's lesson (I.3 → m01-l03); a row whose bracketed alternative lesson states the fact
counts as covered there (say so).

**The asked fact.** Open the questionnaire and its definitive key (text in `SP/exams/`, given in your prompt; the
file names match `content/age-administrativo-c1/sources/examenes-oficiales/`) and write, in one line, the fact the
keyed option states, with the article that states it when you can find it in `content/age-administrativo-c1/sources/
normativa/` (`pdftotext -layout`). For a supuesto, the fact is the legal rule the keyed answer applies to the
scenario (plazo, órgano, cuantía, procedure step), not the scenario's data.

**Disputed keys.** When the ledger's «Nota de clave» says «Clave oficial discutida», the asked fact is what the norm
says on the point, not the key: write the norm's fact, mark the row «disputed» in the Note column, and judge coverage
against the norm's fact.

**Status.** «Covered»: the owner lesson has a sentence, list item or «Lo que más cae» line that states the fact (not
just names the subject). «Partial»: it states part of it (say which part is missing). «Miss»: nothing states it.
Add «needs source: <norm, article>» when the article is not in `sources/normativa/` or `sources/otros/`.

**Report** `docs/age-verification/audit-2026-10/coverage/mBB-lTT.md` per lesson: a table `| Exam | Part | Nº |
Asked fact (key) | Article | Status | Where in the lesson (quote) | Note |`, then counts: asked, covered, partial,
miss, and the share missed counting partial as half. Then `docs/age-verification/audit-2026-10/coverage/mBB.md`: one
row per lesson with those counts, and a list of every partial and miss: lesson, exam, nº, the missing fact stated
precisely, and the article (with paragraph) that states it.
