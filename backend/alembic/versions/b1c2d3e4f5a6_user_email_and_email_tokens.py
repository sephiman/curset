# SPDX-License-Identifier: AGPL-3.0-only
"""Optional user email (unique once verified) and the table of mailed single-use links.

Revision ID: b1c2d3e4f5a6
Revises: a9b0c1d2e3f4
Create Date: 2026-10-04
"""

from __future__ import annotations

import sqlalchemy as sa
from alembic import op
from fastapi_users_db_sqlalchemy.generics import GUID

revision: str = "b1c2d3e4f5a6"
down_revision: str | None = "a9b0c1d2e3f4"
branch_labels: str | None = None
depends_on: str | None = None


def upgrade() -> None:
    op.add_column("user", sa.Column("email", sa.String(length=254), nullable=True))
    # No account has had an address to verify yet; whatever is_verified held meant nothing.
    op.execute('UPDATE "user" SET is_verified = false')
    op.create_index(
        "ix_user_email_lower_verified",
        "user",
        [sa.text("lower(email)")],
        unique=True,
        postgresql_where=sa.text("is_verified"),
    )

    op.create_table(
        "email_token",
        sa.Column("id", GUID(), nullable=False),
        sa.Column("user_id", GUID(), nullable=False),
        sa.Column("purpose", sa.String(length=32), nullable=False),
        sa.Column("email", sa.String(length=254), nullable=False),
        sa.Column("token_hash", sa.String(length=64), nullable=False),
        sa.Column("expires_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("used_at", sa.DateTime(timezone=True), nullable=True),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
        sa.ForeignKeyConstraint(
            ["user_id"], ["user.id"], name="fk_email_token_user_id_user", ondelete="CASCADE"
        ),
        sa.PrimaryKeyConstraint("id", name="pk_email_token"),
        sa.UniqueConstraint("token_hash", name="uq_email_token_token_hash"),
    )
    op.create_index("ix_email_token_user_id", "email_token", ["user_id"])


def downgrade() -> None:
    op.drop_index("ix_email_token_user_id", table_name="email_token")
    op.drop_table("email_token")
    op.drop_index("ix_user_email_lower_verified", table_name="user")
    op.drop_column("user", "email")
