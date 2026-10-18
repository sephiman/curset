# SPDX-License-Identifier: AGPL-3.0-only
"""Localized text, the one value type every piece of course content is written in."""

from __future__ import annotations

from typing import Literal, Self

from pydantic import BaseModel, ConfigDict, model_validator

#: Every language the platform can serve; a course declares the subset it is written in.
LOCALES = ("en", "es")
Locale = Literal["en", "es"]


class LocalizedText(BaseModel):
    """Text in the languages its course declares; which ones must be present is checked per course."""

    model_config = ConfigDict(extra="forbid")
    en: str | None = None
    es: str | None = None

    @model_validator(mode="after")
    def _not_empty(self) -> Self:
        if self.en is None and self.es is None:
            raise ValueError("localized text needs at least one language")
        return self

    def get(self, locale: str) -> str:
        value = self.es if locale == "es" else self.en
        if value is None:
            raise LookupError(f"no {locale!r} text in {self!r}")
        return value

    def languages(self) -> set[str]:
        return {locale for locale in LOCALES if getattr(self, locale) is not None}
