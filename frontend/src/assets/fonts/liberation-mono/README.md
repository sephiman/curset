<!-- SPDX-License-Identifier: AGPL-3.0-only -->
# Liberation Mono — the print face for code in the course PDF

Two unmodified TrueType files (Regular, Bold) from the same Liberation 2.x release as
`../liberation-sans/`, plus the upstream `LICENSE` (SIL Open Font License 1.1). pdfmake's italic slots
map to the upright files: code never prints in italics. Not used on screen.

Code blocks and the code spans of printed questions set in it (`CODE_FONT` in
`frontend/src/lib/pdf/page.ts`). pdfkit embeds a font only when a page uses it, so a course without code
prints exactly what it printed before this face was added. `frontend/src/lib/pdf/fonts.test.ts` checks
its coverage the same way as the text face's.
