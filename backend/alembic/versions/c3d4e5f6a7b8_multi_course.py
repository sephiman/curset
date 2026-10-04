# SPDX-License-Identifier: AGPL-3.0-only
"""Several courses: skeleton keys are unique per course, and users choose their active courses.

Module, lesson and exercise keys (`m01`, `m01-l1`, `m01-ex-1`) are unique only inside a course, so
every skeleton primary key becomes `(course_id, id)` and every row that points into the skeleton
(attempts, lesson completions) carries its course. Every existing row belongs to the one course
that existed, which the backfill reads off the parent rows rather than assuming.

`user_courses` records which courses each user has active, which one they are viewing and the
language they read it in. Existing users keep `crypto-futures` active and selected (R5.5).

Revision ID: c3d4e5f6a7b8
Revises: b1c2d3e4f5a6
Create Date: 2026-10-04
"""

from __future__ import annotations

import sqlalchemy as sa
from alembic import op
from fastapi_users_db_sqlalchemy.generics import GUID

revision: str = "c3d4e5f6a7b8"
down_revision: str | None = "b1c2d3e4f5a6"
branch_labels: str | None = None
depends_on: str | None = None

LEGACY_COURSE = "crypto-futures"

# (table, old single-column FK name) — replaced by composite FKs that include the course.
_SINGLE_FKS = [
    ("attempts", "fk_attempts_exercise_id_exercises"),
    ("lesson_completions", "fk_lesson_completions_lesson_id_lessons"),
    ("exercises", "fk_exercises_lesson_id_lessons"),
    ("exercises", "fk_exercises_module_id_modules"),
    ("lessons", "fk_lessons_module_id_modules"),
    ("modules", "fk_modules_block_id_blocks"),
]

# (table, the parent it inherits its course from, the join between them)
_BACKFILLS = [
    ("lessons", "modules", "modules.id = lessons.module_id"),
    ("exercises", "modules", "modules.id = exercises.module_id"),
    ("lesson_completions", "lessons", "lessons.id = lesson_completions.lesson_id"),
    ("attempts", "exercises", "exercises.id = attempts.exercise_id"),
]

# (name, table, columns, referred table, referred columns, ondelete)
_COMPOSITE_FKS = [
    (
        "fk_modules_course_id_blocks",
        "modules",
        ["course_id", "block_id"],
        "blocks",
        ["course_id", "id"],
        None,
    ),
    (
        "fk_lessons_course_id_modules",
        "lessons",
        ["course_id", "module_id"],
        "modules",
        ["course_id", "id"],
        None,
    ),
    (
        "fk_exercises_course_id_modules",
        "exercises",
        ["course_id", "module_id"],
        "modules",
        ["course_id", "id"],
        None,
    ),
    (
        "fk_exercises_course_id_lessons",
        "exercises",
        ["course_id", "lesson_id"],
        "lessons",
        ["course_id", "id"],
        None,
    ),
    (
        "fk_lesson_completions_course_id_lessons",
        "lesson_completions",
        ["course_id", "lesson_id"],
        "lessons",
        ["course_id", "id"],
        "cascade",
    ),
    (
        "fk_attempts_course_id_exercises",
        "attempts",
        ["course_id", "exercise_id"],
        "exercises",
        ["course_id", "id"],
        None,
    ),
]


def upgrade() -> None:
    for table, name in _SINGLE_FKS:
        op.drop_constraint(name, table, type_="foreignkey")

    for table, parent, join in _BACKFILLS:
        op.add_column(table, sa.Column("course_id", sa.String(), nullable=True))
        op.execute(f"UPDATE {table} SET course_id = {parent}.course_id FROM {parent} WHERE {join}")
        op.alter_column(table, "course_id", nullable=False)
        op.create_index(f"ix_{table}_course_id", table, ["course_id"], unique=False)
    for table in ("lessons", "exercises"):
        op.create_foreign_key(f"fk_{table}_course_id_courses", table, "courses", ["course_id"], ["id"])

    for table in ("blocks", "modules", "lessons", "exercises"):
        op.drop_constraint(f"pk_{table}", table, type_="primary")
        op.create_primary_key(f"pk_{table}", table, ["course_id", "id"])
    op.drop_constraint("pk_lesson_completions", "lesson_completions", type_="primary")
    op.create_primary_key(
        "pk_lesson_completions", "lesson_completions", ["user_id", "course_id", "lesson_id"]
    )

    for name, table, columns, referred, referred_columns, ondelete in _COMPOSITE_FKS:
        op.create_foreign_key(name, table, referred, columns, referred_columns, ondelete=ondelete)

    op.create_table(
        "user_courses",
        sa.Column("user_id", GUID(), nullable=False),
        sa.Column("course_id", sa.String(), nullable=False),
        sa.Column("active", sa.Boolean(), server_default="true", nullable=False),
        sa.Column("selected", sa.Boolean(), server_default="false", nullable=False),
        sa.Column("reading_locale", sa.String(length=2), nullable=True),
        sa.ForeignKeyConstraint(["course_id"], ["courses.id"], name="fk_user_courses_course_id_courses"),
        sa.ForeignKeyConstraint(
            ["user_id"], ["user.id"], name="fk_user_courses_user_id_user", ondelete="cascade"
        ),
        sa.PrimaryKeyConstraint("user_id", "course_id", name="pk_user_courses"),
    )
    op.create_index(
        "uq_user_courses_selected",
        "user_courses",
        ["user_id"],
        unique=True,
        postgresql_where=sa.text("selected"),
    )
    op.execute(
        sa.text(
            "INSERT INTO user_courses (user_id, course_id, active, selected) SELECT id, :course, true, true "
            'FROM "user" WHERE EXISTS (SELECT 1 FROM courses WHERE id = :course)'
        ).bindparams(course=LEGACY_COURSE)
    )


def downgrade() -> None:
    op.drop_index("uq_user_courses_selected", table_name="user_courses")
    op.drop_table("user_courses")

    for name, table, *_ in reversed(_COMPOSITE_FKS):
        op.drop_constraint(name, table, type_="foreignkey")
    # Only reversible while a single course exists: the old keys were global.
    op.drop_constraint("pk_lesson_completions", "lesson_completions", type_="primary")
    op.create_primary_key("pk_lesson_completions", "lesson_completions", ["user_id", "lesson_id"])
    for table in ("exercises", "lessons", "modules", "blocks"):
        op.drop_constraint(f"pk_{table}", table, type_="primary")
        op.create_primary_key(f"pk_{table}", table, ["id"])
    for table in ("exercises", "lessons"):
        op.drop_constraint(f"fk_{table}_course_id_courses", table, type_="foreignkey")
    for table, *_ in reversed(_BACKFILLS):
        op.drop_index(f"ix_{table}_course_id", table_name=table)
        op.drop_column(table, "course_id")

    op.create_foreign_key("fk_modules_block_id_blocks", "modules", "blocks", ["block_id"], ["id"])
    op.create_foreign_key("fk_lessons_module_id_modules", "lessons", "modules", ["module_id"], ["id"])
    op.create_foreign_key("fk_exercises_module_id_modules", "exercises", "modules", ["module_id"], ["id"])
    op.create_foreign_key("fk_exercises_lesson_id_lessons", "exercises", "lessons", ["lesson_id"], ["id"])
    op.create_foreign_key(
        "fk_lesson_completions_lesson_id_lessons",
        "lesson_completions",
        "lessons",
        ["lesson_id"],
        ["id"],
        ondelete="cascade",
    )
    op.create_foreign_key(
        "fk_attempts_exercise_id_exercises", "attempts", "exercises", ["exercise_id"], ["id"]
    )
