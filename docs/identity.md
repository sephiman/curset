# Curset — visual identity

Direction C, «Reading»: a scale with three ticks and a pointer stopped between two of them. Review page:
`/dev/identity` (needs `DEV_MODE=true`). Screens: `docs/screens/identity/`.

## Decisions

1. The mark is the scale and pointer in a 24-unit box with a 2-unit round stroke. Course glyphs share that box and stroke and a 1-unit corner radius.
2. The wordmark is «curset» in DM Mono Medium (OFL), outlined to paths. It stands on the same scale, with the tall tick at the joint of «cur» and «set». No SVG loads a font.
3. Ink `#24211b`, paper `#efeadf`. Light draws ink on paper, dark draws paper on ink, and OLED draws paper on black.
4. `frontend/src/assets/identity/identity.json` holds the name, typeface and tokens. `npm run identity` (`frontend/scripts/identity/build.mjs`) writes every SVG, `tokens.css`, the glyphs and the favicon PNGs from it.
5. Pieces: mark, wordmark, horizontal lockup and stacked lockup, each in light, dark and mono. The mono files use `currentColor`; light and dark are the mono file plus a `color` attribute.
6. The header uses the horizontal lockup, the phone header the mark, and the auth card the stacked lockup.
7. The favicon is the paper mark on an ink tile, so it shows on light and dark tab strips. Chromium rasterizes the 16, 32, 180 and 512 PNGs from it, and `png-sources.json` records the SVG's hash. On a tab strip as dark as the ink, only the mark shows.
8. Glyphs live in `content/<slug>/identity/` and are drawn in `currentColor`: a candlestick for `crypto-futures`, a columned public building for `age-administrativo-c1` and a sheet with a folded corner and two lines of text for `age-auxiliar-c2` (no flag, crest or seal). The backend serves each at `/api/courses/<slug>/glyph.svg`, and the app uses it as a mask filled with the accent.
9. Accents come in two shades per course, because no single colour reaches 4.5:1 against both this ink and this paper (the best is 3.66:1). The `light` shade passes 4.5:1 on paper, and the `dark` shade passes on ink and on black. Courses stay within 15 % of each other's luminance. Crypto is teal `#0f6b68`/`#19afaa`, AGE C1 is plum `#a3366c`/`#d685ad` and AGE C2 is blue `#3a5aa6`/`#7ea0dc` (5.5:1 on paper, 6.1:1 on ink).
10. The PDF cover prints the ink mark above the title and the glyph in its paper shade beside it. The footer is unchanged.

## Rejected

- A · Tally (a five-bar gate; «cur» regular, «set» bold in Space Grotesk): turned to a blot at 16 px.
- B · Interval (three narrowing intervals; «Cur set» in Fraunces): read as a publishing house, and the gap made two words.
