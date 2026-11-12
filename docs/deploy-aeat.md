# Deploying aeat-agentes-hacienda (stage 1, theory only)

Written 2026-11-12. Nothing here has been run against the deploy host. Run it there, in order; stop at the first
check that does not hold.

What ships: the course `aeat-agentes-hacienda` published (Spanish only) with 33 lessons (the process lesson, 12 common
temas, 20 tax temas), its glossary, 81 esquemas, a calculator glyph and an ochre accent, and platform delta M: a course
with no exercises and no exams shows default pages (`theoryOnly`). Stage 2 (question bank) is not part of this deploy.

## 1. Migrations

None. Delta M and this round add no Alembic revision. Check `SELECT version_num FROM alembic_version;` equals the
head of `backend/alembic/versions/` before and after.

## 2. Environment

Nothing new. `SYNC_CONTENT_ON_STARTUP=true` inserts the course skeleton (blocks, modules, lessons; no exercises).
`EXTRA_CONTENT_DIR` is for the e2e stack only: do not set it on the host.

## 3. Before and after

```sql
SELECT version_num FROM alembic_version;
SELECT course_id, count(*) FROM exercises WHERE active GROUP BY 1 ORDER BY 1;   -- no row for aeat-agentes-hacienda
SELECT course_id, count(*) FROM lessons GROUP BY 1 ORDER BY 1;                  -- aeat-agentes-hacienda: 33
SELECT course_id, count(*) FROM attempts GROUP BY 1;                            -- unchanged by the deploy
```

Take a `pg_dump` first, as in `docs/deploy-age-1.0.md`. Rollback is the same: restore the dump and the previous image.

## 4. Browser checks (test account)

- Sign-up and Cuenta › Cursos list «Agentes de la Hacienda Pública (C1)» with «Solo en español»; the selector offers
  four courses.
- The course page lists «Proceso selectivo» and the three parts of the programme, shows no «ejercicios» count and has
  «Exportar PDF».
- A tax lesson (`m03-l03`) shows its esquemas and the worked examples; no «Practicar».
- Exámenes: «Este curso todavía no tiene exámenes» and «La teoría está completa.», no button.
- Progreso: «Lecciones marcadas como leídas» only.
- «Exportar PDF» downloads the course (about 135,000 words of tax theory: allow several minutes).
- C1, C2 and crypto-futures behave as before.

## 5. After deploy

- **RDL 29/2026** (BOE-A-2026-20823): convalidation deadline 19-11-2026. From 18-11-2026 check the BOE. If it was
  convalidated, move its `normativa.yaml` entries to «convalidado» and drop the «cambio pendiente» marks. If it was
  derogated or lapsed, apply `docs/age-verification/aeat/r1/rdl-29-2026-revert-list.md` (III.1, III.15, III.16, III.18)
  with blind checks. RDL 31/2026 (about 04-12-2026), 33, 35 and 36/2026 likewise.
- The monthly currency audit covers this course from publication (`check_pages.py`, the norm check
  `docs/age-verification/aeat/r2b/tools/check_norms.py`). Annual figures are re-found in their norms before the
  OEP 2026 convocatoria.
- Two dated sentences copied from C2 (m01-l03 «Estructura vigente a 16-10-2026», m01-l04 Commission count) may change
  with the elections of 29-11-2026.
