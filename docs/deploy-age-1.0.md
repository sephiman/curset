# First production deployment of Curset with two courses (AGE 1.0)

Written 2026-10-28. Nothing in this file has been run against production; the SQL and the startup
sequence were rehearsed on a copy of the local testing database (section 6). Run every step on the deploy
host, in order. Stop at the first check that does not hold.

What ships: the web as Curset with `crypto-futures` and `age-administrativo-c1` both published, the AGE
exam presets «Tema» and «Bloque», lesson practice («Practicar») for AGE, question reports by mail, and
attempts that name their quiz question by its own id. The Android app and its bundle do not change. Lesson
practice needs no migration and no setting: its attempts are ordinary practice attempts, stored with the
columns of section 1.

## 1. Migrations, in order

The backend runs `alembic upgrade head` at startup (`RUN_MIGRATIONS_ON_STARTUP`, default `true`), then
reconciles every course into the skeleton tables (`SYNC_CONTENT_ON_STARTUP`), then fills the question ids
of existing attempts. The chain, oldest first; production applies the ones after its current revision:

| revision | what it does to existing rows |
|---|---|
| `a9b0c1d2e3f4` content keys | column comments only |
| `b1c2d3e4f5a6` user email and email tokens | adds columns and a table |
| `c3d4e5f6a7b8` **course structure** | skeleton primary keys become `(course_id, id)`; `attempts` and `lesson_completions` get `course_id`, backfilled from their parent rows; `user_courses` created, every existing user gets `crypto-futures` active and selected |
| `d5e6f7a8b9c0` question reports | new table `question_reports` |
| `e7f8a9b0c1d2` **cases and attempts** | adds `attempts.question_id` (null on every existing row), report columns, enum value `CASE` |
| `f8a9b0c1d2e3` **stable question id** (step 0) | adds `attempts.variant_id` (null) and index `ix_attempts_course_variant` |
| startup backfill (not a revision) | fills `attempts.variant_id` on every existing quiz attempt; needs the course content, so it runs after the content sync, not inside Alembic |

The backfill identifies each attempt's question from the instance it stored (prompt and laid-out options),
then by prompt alone, then by option texts alone, inside the attempt's exercise; only an attempt none of
those identifies is pinned to what its seed draws, which is how it was graded until now. It logs one line:
`Question ids: N by the exact instance shown, … by seed …, N left unnamed (exercise gone).` It can be
re-run by hand at any time: `docker exec curset-backend tradeschool backfill-question-ids`; a second run
names nothing.

## 2. Environment

Set in the backend's `.env` before starting the new image (secrets stay in `env_file`, never in
`docker-compose.yml`):

| variable | value |
|---|---|
| `REPORT_EMAIL_TO` | the address that receives «Informar de un error» mails; empty stores reports without mailing |
| `SMTP_HOST` | the mail server, e.g. `smtp.gmail.com` |
| `SMTP_PORT` | `587` (STARTTLS) unless the server says otherwise |
| `SMTP_USERNAME` | the sending account |
| `SMTP_PASSWORD` | its app password |
| `MAIL_FROM` | the sender address shown in the mail |
| `APP_PUBLIC_URL` | the public origin, e.g. `https://curset.example` — the report mail's exercise and lesson links are built from it |

The four `SMTP_HOST`/`SMTP_USERNAME`/`SMTP_PASSWORD`/`MAIL_FROM` go together or not at all. Unchanged:
`DB_*`, `COOKIE_SECURE=true`, `RUN_MIGRATIONS_ON_STARTUP=true`, `SYNC_CONTENT_ON_STARTUP=true`.

## 3. Before: backup and counts

```sh
docker exec <postgres container> pg_dump -U <DB_USERNAME> -Fc <DB_NAME> > curset-before-age-1.0.dump
```

Then, in `psql` on the production database, save the output of:

```sql
SELECT version_num FROM alembic_version;
SELECT 'user' AS t, count(*) FROM "user"
UNION ALL SELECT 'attempts', count(*) FROM attempts
UNION ALL SELECT 'attempts answered', count(*) FROM attempts WHERE state = 'ANSWERED'
UNION ALL SELECT 'lesson_completions', count(*) FROM lesson_completions
UNION ALL SELECT 'exam_sessions', count(*) FROM exam_sessions
UNION ALL SELECT 'exercises', count(*) FROM exercises;
SELECT e.type, count(*) FROM attempts a JOIN exercises e ON e.id = a.exercise_id GROUP BY 1 ORDER BY 1;
```

The last query joins on `id` only, which is right before `c3d4e5f6a7b8` (one course) and still right after
it while only `crypto-futures` has attempts. If `version_num` is `f8a9b0c1d2e3` already, this deployment
was done; stop.

## 4. Deploy

```sh
docker compose pull && docker compose up -d
docker logs -f curset-backend   # until the health check passes
```

The log must show, in this order: `Running database migrations…`, the course sync line
(`Course sync: … inserted, … updated, … deactivated.`; inserted includes every AGE block, module, lesson and
exercise), and the `Question ids:` line with `0 left unnamed`. A failure in a migration leaves the container
restarting; restore the dump (section 7).

## 5. After: counts

```sql
SELECT version_num FROM alembic_version;                       -- f8a9b0c1d2e3
-- every count from section 3 unchanged:
SELECT 'user' AS t, count(*) FROM "user"
UNION ALL SELECT 'attempts', count(*) FROM attempts
UNION ALL SELECT 'attempts answered', count(*) FROM attempts WHERE state = 'ANSWERED'
UNION ALL SELECT 'lesson_completions', count(*) FROM lesson_completions
UNION ALL SELECT 'exam_sessions', count(*) FROM exam_sessions;
-- all of it still belongs to crypto-futures:
SELECT course_id, count(*) FROM attempts GROUP BY 1;            -- one row: crypto-futures
SELECT course_id, count(*) FROM lesson_completions GROUP BY 1;  -- one row: crypto-futures
SELECT course_id, count(*) FROM exam_sessions GROUP BY 1;       -- one row: crypto-futures
-- every user kept crypto-futures (R5.5):
SELECT (SELECT count(*) FROM "user") AS users,
       (SELECT count(*) FROM user_courses WHERE course_id = 'crypto-futures' AND active) AS crypto_active;
-- every quiz attempt names its question; other kinds keep the seed as their question:
SELECT e.type, count(*) AS attempts, count(a.variant_id) AS named
FROM attempts a JOIN exercises e ON e.course_id = a.course_id AND e.id = a.exercise_id
GROUP BY 1 ORDER BY 1;                                          -- QUIZ: attempts = named; others: named = 0
-- the per-type counts equal section 3's
-- both courses in the skeleton, AGE with its whole bank:
SELECT course_id, count(*) FROM exercises WHERE active GROUP BY 1 ORDER BY 1;
                                                                -- age-administrativo-c1 266
```

Then in a browser, with a test account: sign-up lists both courses, «Administrativo del Estado (C1)» with
«Solo en español»; Cuenta › Cursos shows the same; with both enabled the course dropdown offers both;
Exámenes in AGE offers «Tema» (45 temas) and «Bloque» (6 bloques); a submitted «Tema» shows «Ver
solución» under every question and no error toast; the end of an AGE tema, and its row on the module page,
offer «Practicar», whose round opens the solution after each answer; a crypto-futures lesson still embeds
its quizzes and offers no «Practicar». Then, for the practice round just answered:

```sql
SELECT count(*) FROM attempts a JOIN "user" u ON u.id = a.user_id
WHERE u.username = '<test account>' AND a.exam_session_id IS NULL AND a.variant_id IS NOT NULL;
                                                                -- one row per practice answer
```

## 6. One test report through the real mail server

With the test account from section 5:

1. Sit a «Tema» in AGE, submit it, open «Ver solución» on any question and use «Informar de un error en
   esta pregunta» with the text `Prueba de despliegue AGE 1.0: ignorar.`
2. The mail reaches `REPORT_EMAIL_TO` within a minute (it is sent right after the report is stored).
   Check it carries the course slug, module, lesson, exercise, the question id (`Variant`), the seed, the
   reading language, both answers, the username, the date and the two links, and that the links open on
   `APP_PUBLIC_URL`.
3. In `psql`:
   ```sql
   SELECT id, variant_id, emailed_at, email_attempts FROM question_reports
   ORDER BY created_at DESC LIMIT 1;                           -- emailed_at set, email_attempts >= 1
   ```
   If `emailed_at` stays null, the SMTP settings are wrong: the report is kept and retried every 15
   minutes; fix `.env`, `docker compose up -d`, and watch it go out.
4. Delete the test report and the test account once checked.

## 7. Rollback

The previous image does not know revision `f8a9b0c1d2e3` and will not start against a migrated database.
Roll back by restoring the dump, then the previous image:

```sh
docker compose stop backend
docker exec -i <postgres container> pg_restore -U <DB_USERNAME> -d <DB_NAME> --clean --if-exists \
  < curset-before-age-1.0.dump
# pin the previous image tag in docker-compose.yml, then
docker compose up -d
```

## Rehearsal (local testing database, 2026-10-28)

On a copy of the local testing database (at `e7f8a9b0c1d2`, crypto only: 368 attempts, 2 reports, 11
exams): `migrate` → `f8a9b0c1d2e3`; backfill: 159 by the exact instance shown, 55 by prompt, 2 by option
texts, 9 by seed, 0 unnamed; a second run named nothing; quiz attempts 225 of 225 named, the 143 attempts
of generated exercises untouched; report and exam counts unchanged. The browser checks of section 5 passed
against that copy. A second rehearsal (2026-10-28, after lesson practice and the hand-in fixes) on a fresh
copy: migrate, then at 360×640 the module page's «Practicar», the tema's end card («63 preguntas…»), a round
of 20 with the solution open after each answer and the report link inside; a «Tema» handed in while every
answer save was slowed to 1.5 s stored all 20 answers, with no 409 and no toast.
