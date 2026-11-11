# Deploying age-auxiliar-c2 (round R5)

Written 2026-11-11. Nothing here has been run against the deploy host. Run it there, in order; stop at the first
check that does not hold.

What ships: the course `age-auxiliar-c2` published (Spanish only), its presets (simulacro, partes, psicotécnicos,
bloque, tema, the eight official sets), the 34 calibration items, a new accent and glyph, and two small platform
changes: a stored quiz question may carry a `table`, and the exam review now draws it.

## 1. Migrations

**R5 adds none.** The chain after the AGE 1.0 head `f8a9b0c1d2e3` is `a1b2c3d4e5f6` (attempt time and report
options), `fccee145cfe9` (email as username) and `a2b3c4d5e6f7` (round L: enum value `PSICOTECNICO`,
`exercises.module_id` nullable; additive). If the host is still at `f8a9b0c1d2e3`, those three run at startup;
check `SELECT version_num FROM alembic_version;` first and read each file under `backend/alembic/versions/`.

## 2. Environment

Nothing new. `SYNC_CONTENT_ON_STARTUP=true` inserts the course skeleton (blocks, modules, lessons, exercises,
including the generated `gen:<generator>` exercises and the nine official/calibration ones).

## 3. Before and after

```sql
SELECT version_num FROM alembic_version;
SELECT course_id, count(*) FROM exercises WHERE active GROUP BY 1 ORDER BY 1;   -- add age-auxiliar-c2 after
SELECT course_id, count(*) FROM attempts GROUP BY 1;                            -- unchanged by the deploy
```

Take a `pg_dump` first, as in `docs/deploy-age-1.0.md`. Rollback is the same: restore the dump and the previous image.

## 4. Browser checks (test account)

Sign-up and Cuenta › Cursos list «Auxiliar Administrativo del Estado (C2)» with «Solo en español»; the course selector
offers three courses; a tema's «Practicar» opens the solution with its excerpt; «Psicotécnicos» practice shows the rule
after each answer; Exámenes offers the simulacro (90 minutes, no pause, options A–D, no tema label during the
sitting), «Parte 1», «Parte 2», «Psicotécnicos», «Bloque», «Tema» and the eight official sets; after a submitted
simulacro, «Por tema» lists the psicotécnico types and the review shows each question's table.
