# SPDX-License-Identifier: AGPL-3.0-only
"""The closing line of an explanation: the confirmed citation as inline code."""

from __future__ import annotations

from tradeschool.psicotecnico.backend.base import Citation, code


def source_line(citation: Citation) -> str:
    refs = (citation.confirmed or citation.suggested).split("; ")
    return f"Source: {'; '.join(code(ref) for ref in refs)}."
