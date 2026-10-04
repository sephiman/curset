# SPDX-License-Identifier: AGPL-3.0-only
"""Auth request/response schemas — username identity, optional email for password reset."""

from __future__ import annotations

import re
import uuid
from typing import Literal

from pydantic import BaseModel, ConfigDict, Field, field_validator

Locale = Literal["en", "es"]

USERNAME_MIN = 3
USERNAME_MAX = 32
# Letters, digits, hyphen and underscore. Normalized to lowercase for case-insensitive identity.
USERNAME_RE = re.compile(r"^[a-z0-9_-]+$")
EMAIL_MAX = 254
EMAIL_RE = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")


def normalize_username(raw: str) -> str:
    """Lowercase, trim, and validate a username. Raises ``ValueError`` if it breaks the policy."""
    value = raw.strip().lower()
    if not (USERNAME_MIN <= len(value) <= USERNAME_MAX):
        raise ValueError(f"Username must be {USERNAME_MIN}-{USERNAME_MAX} characters.")
    if not USERNAME_RE.match(value):
        raise ValueError("Username may contain only letters, numbers, hyphen and underscore.")
    return value


def normalize_email(raw: str) -> str:
    """Lowercase, trim, and shape-check an address. Raises ``ValueError`` if it is not one."""
    value = raw.strip().lower()
    if len(value) > EMAIL_MAX or not EMAIL_RE.match(value):
        raise ValueError("That is not an email address.")
    return value


class UserRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: uuid.UUID
    username: str
    locale: str
    email: str | None
    email_verified: bool = Field(validation_alias="is_verified")


class UserCreate(BaseModel):
    model_config = ConfigDict(extra="forbid")
    username: str
    password: str
    locale: Locale = "en"
    email: str | None = None
    #: The courses ticked on the sign-up screen; none is a valid answer.
    courses: list[str] = Field(default_factory=list)

    @field_validator("username")
    @classmethod
    def _normalize(cls, v: str) -> str:
        return normalize_username(v)

    @field_validator("email")
    @classmethod
    def _normalize_email(cls, v: str | None) -> str | None:
        return normalize_email(v) if v else None


class UserUpdate(BaseModel):
    """Absent fields stay as they are; ``email: null`` removes the address."""

    model_config = ConfigDict(extra="forbid")
    locale: Locale | None = None
    email: str | None = None

    @field_validator("email")
    @classmethod
    def _normalize_email(cls, v: str | None) -> str | None:
        return normalize_email(v) if v else None


class LoginRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")
    username: str
    password: str


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
