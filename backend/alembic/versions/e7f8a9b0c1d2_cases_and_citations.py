# SPDX-License-Identifier: AGPL-3.0-only
"""case exercises and citations: the `case` exercise type, per-question attempts, richer reports

Additive only. `attempts.question_id` names the question inside a case (null for every other
exercise); the report columns carry the case title, the question's citation and its lesson anchor.

Revision ID: e7f8a9b0c1d2
Revises: d5e6f7a8b9c0
Create Date: 2026-10-18
"""

from __future__ import annotations

from collections.abc import Sequence

import sqlalchemy as sa
from alembic import op

revision: str = "e7f8a9b0c1d2"
down_revision: str | None = "d5e6f7a8b9c0"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    # The native enum stores member NAMES (see c7d9e1f3a5b7), so the new value is CASE.
    op.execute("ALTER TYPE exercise_type ADD VALUE IF NOT EXISTS 'CASE'")
    op.add_column("attempts", sa.Column("question_id", sa.String(), nullable=True))
    op.add_column("question_reports", sa.Column("case_title", sa.Text(), nullable=True))
    op.add_column("question_reports", sa.Column("citation", sa.Text(), nullable=True))
    op.add_column("question_reports", sa.Column("lesson_anchor", sa.String(), nullable=True))


def downgrade() -> None:
    op.drop_column("question_reports", "lesson_anchor")
    op.drop_column("question_reports", "citation")
    op.drop_column("question_reports", "case_title")
    op.drop_column("attempts", "question_id")
    # The enum value stays: PostgreSQL cannot drop it while rows may hold it (same as c7d9e1f3a5b7).
