# SPDX-License-Identifier: AGPL-3.0-only
"""Auth request/response schemas — email identity, optional display name."""

from __future__ import annotations

import re
import uuid
from typing import Literal

from pydantic import BaseModel, ConfigDict, Field, field_validator

Locale = Literal["en", "es"]

EMAIL_MAX = 254
EMAIL_RE = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")
NAME_MAX = 100


def normalize_email(raw: str) -> str:
    """Lowercase, trim, and shape-check an address. Raises ``ValueError`` if it is not one."""
    value = raw.strip().lower()
    if len(value) > EMAIL_MAX or not EMAIL_RE.match(value):
        raise ValueError("That is not an email address.")
    return value


def derive_name_from_email(email: str) -> str:
    """Local-part of the address as the initial display name."""
    local = email.split("@", 1)[0].strip()
    return local[:NAME_MAX] or "learner"


def normalize_name(raw: str | None) -> str | None:
    if raw is None:
        return None
    value = raw.strip()
    return value[:NAME_MAX] if value else None


class UserRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: uuid.UUID
    email: str
    name: str | None
    locale: str
    email_verified: bool = Field(validation_alias="is_verified")


class UserCreate(BaseModel):
    model_config = ConfigDict(extra="forbid")
    email: str
    password: str
    name: str | None = None
    locale: Locale = "en"
    courses: list[str] = Field(default_factory=list)

    @field_validator("email")
    @classmethod
    def _normalize_email(cls, v: str) -> str:
        return normalize_email(v)

    @field_validator("name")
    @classmethod
    def _normalize_name(cls, v: str | None) -> str | None:
        return normalize_name(v)


class UserUpdate(BaseModel):
    """Absent fields stay as they are."""

    model_config = ConfigDict(extra="forbid")
    name: str | None = None
    locale: Locale | None = None
    email: str | None = None

    @field_validator("email")
    @classmethod
    def _normalize_email(cls, v: str | None) -> str | None:
        return normalize_email(v) if v else None

    @field_validator("name")
    @classmethod
    def _normalize_name(cls, v: str | None) -> str | None:
        return normalize_name(v)


class LoginRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")
    email: str
    password: str

    @field_validator("email")
    @classmethod
    def _normalize_email(cls, v: str) -> str:
        return normalize_email(v)


class Features(BaseModel):
    mail: bool


class PasswordResetRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")
    email: str

    @field_validator("email")
    @classmethod
    def _normalize_email(cls, v: str) -> str:
        return normalize_email(v)


class EmailTokenBody(BaseModel):
    model_config = ConfigDict(extra="forbid")
    token: str


class PasswordResetConfirm(BaseModel):
    model_config = ConfigDict(extra="forbid")
    token: str
    new_password: str
