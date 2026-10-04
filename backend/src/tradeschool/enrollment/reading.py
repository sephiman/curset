# SPDX-License-Identifier: AGPL-3.0-only
"""The reading-language rule (R4.2), shared by every surface that serves course content."""

from __future__ import annotations


def reading_language(course_languages: list[str], chosen: str | None, account_locale: str) -> str:
    """The user's choice if the course has it, else the account language, else the course's first."""
    for candidate in (chosen, account_locale):
        if candidate in course_languages:
            return str(candidate)
    return course_languages[0]
