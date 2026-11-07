# SPDX-License-Identifier: AGPL-3.0-only
"""psicotécnico exercises: the `psicotecnico` exercise type, and exercises that belong to no module

Additive. A generated exercise (one per declared generator) has no lesson and no module; its attempts keep the
foreign key to `exercises`, so `module_id` becomes nullable.

Revision ID: a2b3c4d5e6f7
Revises: fccee145cfe9
Create Date: 2026-11-07
"""

from __future__ import annotations

from collections.abc import Sequence

from alembic import op

revision: str = "a2b3c4d5e6f7"
down_revision: str | None = "fccee145cfe9"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    # The native enum stores member NAMES (see c7d9e1f3a5b7).
    op.execute("ALTER TYPE exercise_type ADD VALUE IF NOT EXISTS 'PSICOTECNICO'")
    op.alter_column("exercises", "module_id", nullable=True)


def downgrade() -> None:
    op.execute("DELETE FROM exercises WHERE module_id IS NULL")
    op.alter_column("exercises", "module_id", nullable=False)
    # The enum value stays: PostgreSQL cannot drop it while rows may hold it (same as c7d9e1f3a5b7).
