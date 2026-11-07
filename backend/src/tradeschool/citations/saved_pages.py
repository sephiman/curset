# SPDX-License-Identifier: AGPL-3.0-only
"""Saved source pages (`content/*/sources/otros/`) without scripts, styles, frames or tracking attributes."""

from __future__ import annotations

import re

STRIPPED_ELEMENTS = ("script", "style", "iframe", "noscript")

_ATTRIBUTE = rb"""\s+[^\s"'>/=]+(?:\s*=\s*(?:"[^"]*"|'[^']*'|[^\s"'>]+))?"""
# Leftmost token wins, as in the HTML tokenizer: a `</script>` inside a comment or a `<!--` inside a script
# never ends the wrong token. An element left unclosed loses only its start tag. The rest stays byte for byte.
_TOKEN = re.compile(
    rb"(?P<comment><!--.*?-->)"
    rb"|(?P<element><(?P<name>" + "|".join(STRIPPED_ELEMENTS).encode() + rb")\b"
    rb"(?:" + _ATTRIBUTE + rb")*\s*/?>(?:.*?</(?P=name)\s*>)?)"
    rb"|(?P<tag><[a-zA-Z][^\s/>]*(?:" + _ATTRIBUTE + rb"|\s*/)*\s*>)",
    re.S | re.I,
)
_ATTRIBUTE_IN_TAG = re.compile(rb"""(\s+)([^\s"'>/=]+)(\s*=\s*(?:"[^"]*"|'[^']*'|[^\s"'>]+))?""")
# Event handlers, hyperlink auditing, and the analytics hooks the saved sites use (Microsoft JSLL/1DS, GTM).
TRACKING_ATTRIBUTE = re.compile(
    rb"on[a-z]+|ping|data-m|data-tel|data-bi-[-\w]*|data-mscc-[-\w]*|data-uhf-mscc|data-gtm-[-\w]*"
    rb"|data-ga(?:-[-\w]*)?|data-analytics(?:-[-\w]*)?|data-track(?:ing)?(?:-[-\w]*)?|data-telemetry(?:-[-\w]*)?",
    re.I,
)


def _clean_tag(tag: bytes) -> bytes:
    name_end = re.match(rb"<[a-zA-Z][^\s/>]*", tag)
    assert name_end is not None
    head, rest = tag[: name_end.end()], tag[name_end.end() :]
    return head + _ATTRIBUTE_IN_TAG.sub(lambda m: b"" if TRACKING_ATTRIBUTE.fullmatch(m[2]) else m[0], rest)


def _replace(match: re.Match[bytes]) -> bytes:
    if match["comment"] is not None:
        return match[0]
    if match["element"] is not None:
        return b""
    return _clean_tag(match[0])


# Bytes, not text: the pages come in UTF-8 or cp1252, and what is kept must stay byte for byte as saved.
def strip_page(html: bytes) -> bytes:
    """`html` without script, style, iframe and noscript elements and without tracking attributes."""
    return _TOKEN.sub(_replace, html)


def has_stripped_content(html: bytes) -> bool:
    """Whether `html` still holds an element or attribute that `strip_page` removes."""
    return strip_page(html) != html
