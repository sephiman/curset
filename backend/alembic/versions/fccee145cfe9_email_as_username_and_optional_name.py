# SPDX-License-Identifier: AGPL-3.0-only
"""email as username and optional name

Transitions primary identity to email, adds optional display name (backfilled with username),
and adjusts question reports to store reporter email and name.

Revision ID: fccee145cfe9
Revises: a1b2c3d4e5f6
Create Date: 2026-11-01 13:00:35.507870
"""

from __future__ import annotations

from collections.abc import Sequence

import sqlalchemy as sa
from alembic import op

revision: str = "fccee145cfe9"
down_revision: str | None = "a1b2c3d4e5f6"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    bind = op.get_bind()

    # 1. Update user table: add name, backfill from username, ensure email is not null and unique.
    op.add_column("user", sa.Column("name", sa.String(length=100), nullable=True))
    bind.execute(sa.text('UPDATE "user" SET name = username WHERE name IS NULL'))
    bind.execute(
        sa.text("UPDATE \"user\" SET email = lower(username) || '@curset.invalid' WHERE email IS NULL")
    )
    op.alter_column("user", "email", nullable=False, existing_type=sa.String(length=254))

    op.drop_index("ix_user_email_lower_verified", table_name="user")
    op.create_index("ix_user_email_lower", "user", [sa.text("lower(email)")], unique=True)

    op.drop_index("ix_user_username_lower", table_name="user")
    op.drop_column("user", "username")

    # 2. Update question_reports: store reporter email and optional name instead of username.
    op.add_column("question_reports", sa.Column("email", sa.String(length=254), nullable=True))
    op.add_column("question_reports", sa.Column("name", sa.String(length=100), nullable=True))
    bind.execute(sa.text("UPDATE question_reports SET name = username WHERE name IS NULL"))
    bind.execute(
        sa.text(
            "UPDATE question_reports q SET email = u.email, name = COALESCE(u.name, q.username) "
            'FROM "user" u WHERE q.user_id = u.id'
        )
    )
    bind.execute(
        sa.text(
            "UPDATE question_reports SET email = lower(username) || '@curset.invalid' WHERE email IS NULL"
        )
    )
    op.alter_column("question_reports", "email", nullable=False, existing_type=sa.String(length=254))
    op.drop_column("question_reports", "username")


def downgrade() -> None:
    bind = op.get_bind()

    # 1. Revert question_reports
    op.add_column("question_reports", sa.Column("username", sa.String(length=32), nullable=True))
    bind.execute(
        sa.text(
            "UPDATE question_reports SET username = SUBSTRING(COALESCE(name, split_part(email, '@', 1)), 1, 32)"
        )
    )
    op.alter_column("question_reports", "username", nullable=False, existing_type=sa.String(length=32))
    op.drop_column("question_reports", "name")
    op.drop_column("question_reports", "email")

    # 2. Revert user
    op.add_column("user", sa.Column("username", sa.String(length=32), nullable=True))
    bind.execute(
        sa.text("UPDATE \"user\" SET username = SUBSTRING(COALESCE(name, split_part(email, '@', 1)), 1, 32)")
    )
    op.alter_column("user", "username", nullable=False, existing_type=sa.String(length=32))
    op.create_index("ix_user_username_lower", "user", [sa.text("lower(username)")], unique=True)

    op.drop_index("ix_user_email_lower", table_name="user")
    op.alter_column("user", "email", nullable=True, existing_type=sa.String(length=254))
    op.create_index(
        "ix_user_email_lower_verified",
        "user",
        [sa.text("lower(email)")],
        unique=True,
        postgresql_where=sa.text("is_verified"),
    )
    op.drop_column("user", "name")
