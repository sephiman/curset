# Deploying the tema/bloque PDF export and the exercises switch (delta N)

Written 2026-11-13. Nothing here has been run against the deploy host. Run it there, in order; stop at the first
check that does not hold.

What ships: `GET /courses/<slug>/export?scope=<module|lesson>`, `GET /courses/<slug>/print/questionnaire`, the
«Exportar PDF» / «Exportar PDF del bloque» buttons and dialog, and the account switch «Incluir ejercicios al exportar
PDF» in Cuenta. Content: `pdf_exercises: true` in the `course.yaml` of crypto-futures (explicit; it was the default),
age-administrativo-c1, age-auxiliar-c2 and aeat-agentes-hacienda, and nothing else. The flag only lets a course print
exercises; with every account's switch off after the migration, no PDF changes until a reader turns it on. No
lesson, question, golden or Android bundle file changes.

## 1. Migration

One additive migration, `b3c4d5e6f7a8_user_pdf_exercises` (revises `a2b3c4d5e6f7`): adds
`"user".pdf_exercises boolean NOT NULL DEFAULT false`. Every existing account gets `false` from the server default,
so every export is theory only until the reader switches exercises on. Adding a column with a constant default is a
metadata-only change in PostgreSQL 11 and later: no table rewrite, no long lock.

It runs at startup with `RUN_MIGRATIONS_ON_STARTUP=true`. Check the head first:

```sql
SELECT version_num FROM alembic_version;                      -- a2b3c4d5e6f7 before, b3c4d5e6f7a8 after
SELECT pdf_exercises, count(*) FROM "user" GROUP BY 1;        -- after: one row, false, every account
```

Rollback: `alembic downgrade a2b3c4d5e6f7` drops the column (the switch's values are lost, nothing else), then the
previous image. Take a `pg_dump` first, as in `docs/deploy-age-1.0.md`.

## 2. Environment

Nothing new.

## 3. Browser checks (test account)

- Cuenta shows «Incluir ejercicios al exportar PDF», off.
- A C1 lesson page shows «Exportar PDF»; its dialog says «Solo teoría»; the file is
  `curset-age-administrativo-c1-m01-l01-es-<date>.pdf` with one tema, no contents page, «N de M» in the footer.
- A C1 module page shows «Exportar PDF del bloque»; the file has a contents page and a glossary of that bloque's terms.
- On a phone (390 px) the lesson's, module's and course's export sit in the avatar menu; the course page's module
  cards have «⋯» › «Exportar PDF del bloque».
- Switch on, export a crypto-futures module: «Con ejercicios», its exercises and answer key print. Export a C1 tema:
  «Con ejercicios», 20 questions lettered A–D after the tema, «Plantilla de respuestas» at the back with each
  answer's article, «Semilla N» in the footer. Switch off again: theory only.
- The whole-course export still produces `curset-<course>-<locale>-<date>.pdf`.
