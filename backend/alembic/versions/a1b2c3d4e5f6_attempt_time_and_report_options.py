# SPDX-License-Identifier: AGPL-3.0-only
"""attempt time_seconds and question_reports options

Additive: per-question active time on attempts; lettered options on reports.

Revision ID: a1b2c3d4e5f6
Revises: f8a9b0c1d2e3
Create Date: 2026-10-30
"""

from __future__ import annotations

from collections.abc import Sequence

import sqlalchemy as sa
from alembic import op

revision: str = "a1b2c3d4e5f6"
down_revision: str | None = "f8a9b0c1d2e3"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    op.add_column("attempts", sa.Column("time_seconds", sa.Float(), nullable=True))
    op.add_column("question_reports", sa.Column("options", sa.Text(), nullable=True))


def downgrade() -> None:
    op.drop_column("question_reports", "options")
    op.drop_column("attempts", "time_seconds")
