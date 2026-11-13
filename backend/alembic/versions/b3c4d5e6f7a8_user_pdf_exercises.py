# SPDX-License-Identifier: AGPL-3.0-only
"""user.pdf_exercises: the account's «Incluir ejercicios al exportar PDF» switch, off for everyone

Additive. Existing rows take the server default, so every account starts with theory-only exports.

Revision ID: b3c4d5e6f7a8
Revises: a2b3c4d5e6f7
Create Date: 2026-11-13
"""

from __future__ import annotations

from collections.abc import Sequence

import sqlalchemy as sa
from alembic import op

revision: str = "b3c4d5e6f7a8"
down_revision: str | None = "a2b3c4d5e6f7"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    op.add_column("user", sa.Column("pdf_exercises", sa.Boolean(), nullable=False, server_default=sa.false()))


def downgrade() -> None:
    op.drop_column("user", "pdf_exercises")
