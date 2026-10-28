# SPDX-License-Identifier: AGPL-3.0-only
"""attempts name their quiz question by its own id

Additive only. `attempts.variant_id` holds the id of the quiz question an attempt showed (m06-l02-q351),
so grading, review, reports and stats follow the question to whichever exercise holds it after a rebuild.
Existing rows are filled after this revision by `tradeschool backfill-question-ids` (also run at startup
with the content sync), which needs the course content and so cannot run inside a migration.

Revision ID: f8a9b0c1d2e3
Revises: e7f8a9b0c1d2
Create Date: 2026-10-28
"""

from __future__ import annotations

from collections.abc import Sequence

import sqlalchemy as sa
from alembic import op

revision: str = "f8a9b0c1d2e3"
down_revision: str | None = "e7f8a9b0c1d2"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    op.add_column(
        "attempts",
        sa.Column("variant_id", sa.String(), nullable=True, comment="the quiz question's own id"),
    )
    op.create_index("ix_attempts_course_variant", "attempts", ["course_id", "variant_id"])


def downgrade() -> None:
    op.drop_index("ix_attempts_course_variant", table_name="attempts")
    op.drop_column("attempts", "variant_id")
