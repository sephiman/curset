# SPDX-License-Identifier: AGPL-3.0-only
"""question reports: a learner's "this question is wrong", stored before it is mailed

Revision ID: d5e6f7a8b9c0
Revises: c3d4e5f6a7b8
Create Date: 2026-10-04
"""

from __future__ import annotations

import sqlalchemy as sa
from alembic import op
from fastapi_users_db_sqlalchemy.generics import GUID

revision: str = "d5e6f7a8b9c0"
down_revision: str | None = "c3d4e5f6a7b8"
branch_labels: str | None = None
depends_on: str | None = None


def upgrade() -> None:
    op.create_table(
        "question_reports",
        sa.Column("id", GUID(), nullable=False),
        sa.Column("user_id", GUID(), nullable=False),
        sa.Column("attempt_id", GUID(), nullable=False),
        sa.Column("message", sa.Text(), nullable=False),
        sa.Column("course_id", sa.String(), nullable=False),
        sa.Column("module_id", sa.String(), nullable=False),
        sa.Column("lesson_id", sa.String(), nullable=False),
        sa.Column("exercise_id", sa.String(), nullable=False),
        sa.Column("variant_id", sa.String(), nullable=False),
        sa.Column("seed", sa.BigInteger(), nullable=False),
        sa.Column("reading_locale", sa.String(length=2), nullable=False),
        sa.Column("prompt", sa.Text(), nullable=False),
        sa.Column("given_answer", sa.Text(), nullable=False),
        sa.Column("correct_answer", sa.Text(), nullable=False),
        sa.Column("username", sa.String(length=32), nullable=False),
        sa.Column("link", sa.Text(), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.text("now()"), nullable=False),
        sa.Column("emailed_at", sa.DateTime(timezone=True), nullable=True),
        sa.Column("email_attempts", sa.Integer(), server_default="0", nullable=False),
        sa.ForeignKeyConstraint(
            ["attempt_id"],
            ["attempts.id"],
            name="fk_question_reports_attempt_id_attempts",
            ondelete="cascade",
        ),
        sa.ForeignKeyConstraint(
            ["user_id"], ["user.id"], name="fk_question_reports_user_id_user", ondelete="cascade"
        ),
        sa.PrimaryKeyConstraint("id", name="pk_question_reports"),
        sa.UniqueConstraint("attempt_id", name="uq_question_reports_attempt_id"),
    )
    op.create_index("ix_question_reports_user_id", "question_reports", ["user_id"], unique=False)
    op.create_index("ix_question_reports_created_at", "question_reports", ["created_at"], unique=False)


def downgrade() -> None:
    op.drop_index("ix_question_reports_created_at", table_name="question_reports")
    op.drop_index("ix_question_reports_user_id", table_name="question_reports")
    op.drop_table("question_reports")
