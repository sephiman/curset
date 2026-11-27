# SPDX-License-Identifier: AGPL-3.0-only
"""The closing line of a generator explanation: the anchors its rule was implemented from."""

from __future__ import annotations

from tradeschool.psicotecnico.backend.base import Citation


def source_line(citation: Citation) -> str:
    anchors = (citation.confirmed or citation.suggested).split(";")
    return "Source: " + "; ".join(f"`{anchor.strip()}`" for anchor in anchors) + "."
