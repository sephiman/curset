<!-- SPDX-License-Identifier: AGPL-3.0-only -->
# DejaVu Sans — the fallback face for code characters outside the BMP

One unmodified TrueType file plus the upstream `LICENSE` (Bitstream Vera licence, DejaVu changes in the
public domain). Liberation Mono has no glyphs above U+FFFF, and a snippet prints a surrogate pair
(`"😀😁"` in m11-l05) to show a Java edge case. pdfmake has no per-glyph fallback, so `codeRuns` in
`frontend/src/lib/pdf/codeText.ts` sets those characters in this face. All four slots map to this file.
pdfkit embeds it only when a page uses it.
