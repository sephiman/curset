# Coverage check 2022–2025 (bloque VI) — auditor spec

Date 2026-10-17. Read-only audit: edit no lesson, no repo file other than your own report; commit nothing.

**Population.** Every row of `docs/age-ofimatica-index.md` (sections «Index by application») whose exam is 2025 ord.,
2025 extr., 2024 ord., 2024 extr., 2022 ord. or 2022 extr. Rows with status `función retirada` are listed but not
counted (retired features are not described by rule). `anulada` rows count (the feature was asked). The owner lesson
is the tema the exams ledger (`docs/age-official-exams-ledger.md`) gives that question (first tema when it says «X (o
Y)»); a row whose bracketed alternative lesson states the fact counts as covered there.

**The asked fact.** Open the questionnaire and its definitive key (`content/age-administrativo-c1/sources/examenes-oficiales/`,
`pdftotext -layout`) and write the fact the keyed option states, in one line (for annulled questions: what the stem
asks). Modelo B repeats modelo A: use modelo A.

**Covered** means the owner lesson (`content/age-administrativo-c1/es/lessons/m06-lNN.md`) has an item or a «Lo que más
cae» line that states that fact — not just the feature's name. «Partial»: the lesson states part of it (say which part is
missing). «Miss»: nothing states it. «Sin fuente oficial»: the ledger's «Sin fuente oficial» list
(`docs/age-theory-ledger.md`, bloque VI, Open items) names it — record as such, it is excluded from the denominator.
Labels: a lesson using the official label of the ledger table «Etiqueta del examen / Etiqueta oficial» for the exam's
label counts as stating the fact.

**Report** `docs/age-verification/bloque-vi/coverage/m06-lNN.md` per lesson: a table `| Exam | Nº | Feature | Asked fact
(key) | Status (covered / partial / miss / sin fuente / retirada) | Where in the lesson (quote) |`, then counts:
asked (excluding retirada and sin fuente), covered, partial, miss, and the share missed counting partial as half.
