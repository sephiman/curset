// SPDX-License-Identifier: AGPL-3.0-only
// Builds every identity file from identity.json and the drawing below: `npm run identity`.
// PNGs are rasterized from favicon.svg by Chromium (Playwright) and never edited by hand.
import { createHash } from "node:crypto";
import { mkdirSync, readFileSync, writeFileSync } from "node:fs";
import { dirname, resolve } from "node:path";
import { fileURLToPath } from "node:url";
import { chromium } from "@playwright/test";

const ROOT = resolve(dirname(fileURLToPath(import.meta.url)), "../..");
const OUT = resolve(ROOT, "src/assets/identity");
const CONTENT = resolve(ROOT, "../content");
const identity = JSON.parse(readFileSync(resolve(OUT, "identity.json"), "utf8"));

// The family's shared geometry: a 24-unit box, a 2-unit round stroke, 1-unit corner radius.
const BOX = 24;
const STROKE = 2;
const RADIUS = 1;
const LINE = `fill="none" stroke="currentColor" stroke-width="${STROKE}" stroke-linecap="round" stroke-linejoin="round"`;

// A scale with three ticks and a pointer stopped between two of them.
const MARK =
  `<path ${LINE} d="M3 19h18M6 19v-4M12 19v-4M18 19v-4"/>` +
  `<path fill="currentColor" stroke="currentColor" stroke-width="${STROKE}" stroke-linejoin="round" d="M11.5 4h7L15 10.5z"/>`;

// «curset» in DM Mono Medium (OFL) at 40 units, outlined once so no SVG depends on the font.
const WORD = {
  d: "M12.3 0.5Q9.5 0.5 7.3 -0.8Q5.2 -2.1 3.9 -4.4Q2.7 -6.8 2.7 -9.9Q2.7 -13.1 3.9 -15.4Q5.2 -17.7 7.4 -19Q9.5 -20.3 12.3 -20.3Q16.1 -20.3 18.4 -18.4Q20.8 -16.5 21.4 -13.2H17Q16.6 -14.6 15.3 -15.5Q14.1 -16.3 12.2 -16.3Q10.9 -16.3 9.7 -15.6Q8.4 -14.9 7.7 -13.5Q7 -12 7 -9.9Q7 -7.8 7.7 -6.4Q8.4 -5 9.7 -4.2Q10.9 -3.5 12.2 -3.5Q14.2 -3.5 15.3 -4.3Q16.5 -5.2 17 -6.6H21.4Q20.6 -3.4 18.3 -1.4Q16 0.5 12.3 0.5Z M34.2 0.5Q30.6 0.5 28.8 -1.7Q26.9 -4 26.9 -8.2V-19.8H31.2V-8.7Q31.2 -6.3 32.2 -4.9Q33.3 -3.5 35.5 -3.5Q37.7 -3.5 39.2 -5Q40.6 -6.5 40.6 -9.3V-19.8H44.9V0H41.2L40.8 -3H40.6Q39.8 -1.5 38.2 -0.5Q36.5 0.5 34.2 0.5Z M51.1 0V-3.7H55.9V-14.8Q55.9 -16.2 54.6 -16.2H51.5V-19.8H56.2Q57.9 -19.8 58.9 -18.9Q60 -18 60 -16.3V-15.8H60.2Q60.6 -18 62.1 -19.2Q63.5 -20.3 66.3 -20.3H69.4V-15.8H65.1Q62.7 -15.8 61.4 -14.2Q60.2 -12.6 60.2 -10.3V-3.7H66.3V0Z M84.2 0.5Q80.2 0.5 77.9 -1.4Q75.6 -3.2 75.3 -6.2H79.6Q79.9 -4.8 81.1 -4Q82.2 -3.1 84.2 -3.1Q86.1 -3.1 87.1 -3.9Q88.1 -4.6 88.1 -5.7Q88.1 -7.2 86.9 -7.8Q85.7 -8.3 83.3 -8.6Q81.3 -8.8 79.6 -9.5Q78 -10.2 77 -11.5Q76 -12.7 76 -14.5Q76 -17.1 78.1 -18.7Q80.1 -20.3 83.8 -20.3Q87.4 -20.3 89.4 -18.7Q91.4 -17 91.7 -14.2H87.6Q87.5 -15.4 86.4 -16.1Q85.3 -16.8 83.7 -16.8Q82.1 -16.8 81.1 -16.2Q80.2 -15.6 80.2 -14.6Q80.2 -12.4 84.8 -11.9Q87 -11.7 88.7 -11.1Q90.4 -10.5 91.4 -9.3Q92.4 -8.1 92.4 -5.9Q92.5 -4.1 91.4 -2.6Q90.4 -1.2 88.5 -0.4Q86.6 0.5 84.2 0.5Z M108.2 0.5Q105.4 0.5 103.2 -0.8Q101 -2.1 99.7 -4.4Q98.5 -6.8 98.5 -9.8Q98.5 -13 99.7 -15.3Q100.9 -17.7 103.1 -19Q105.4 -20.3 108.3 -20.3Q111.2 -20.3 113.2 -19Q115.3 -17.7 116.5 -15.6Q117.6 -13.4 117.6 -10.8Q117.6 -10.4 117.6 -9.9Q117.6 -9.5 117.6 -8.9H102.6Q102.8 -6.2 104.4 -4.7Q106 -3.3 108.2 -3.3Q110.1 -3.3 111.2 -4.1Q112.3 -4.9 112.8 -6.2H117.1Q116.4 -3.4 114.1 -1.5Q111.8 0.5 108.2 0.5ZM108.2 -16.6Q106.3 -16.6 104.8 -15.5Q103.2 -14.3 102.8 -12.2H113.4Q113.2 -14.2 111.8 -15.4Q110.4 -16.6 108.2 -16.6Z M134.2 0Q131.2 0 129.5 -1.4Q127.8 -2.8 127.8 -6.5V-16.2H122.8V-19.8H125.8Q127.8 -19.8 128.2 -21.8L128.8 -25H132V-19.8H139.9V-16.2H132V-6.6Q132 -5 132.7 -4.4Q133.4 -3.8 135.2 -3.8H139.8V0Z",
  left: 2.7,
  right: 139.9,
  top: -25.1,
  joint: 72, // the advance after «cur»: the tall tick of the scale sits here
};
const RULE_Y = 9;
const RULE_WIDTH = 2.4;
const WORDMARK =
  `<path fill="currentColor" d="${WORD.d}"/>` +
  `<path fill="none" stroke="currentColor" stroke-width="${RULE_WIDTH}" stroke-linecap="round" ` +
  `d="M${WORD.left} ${RULE_Y}H${WORD.right}M${WORD.left} ${RULE_Y}v-3.5M${WORD.joint} ${RULE_Y}v-7M${WORD.right} ${RULE_Y}v-3.5"/>`;
const WORD_BOX = {
  x: WORD.left - RULE_WIDTH / 2,
  y: WORD.top,
  w: WORD.right - WORD.left + RULE_WIDTH,
  h: RULE_Y + RULE_WIDTH / 2 - WORD.top,
};

// Course glyphs: same box, stroke and radius as the mark, drawn in currentColor for the course accent.
const GLYPHS = {
  candlestick:
    `<path ${LINE} d="M7.5 3v4M7.5 16v5M16.5 3v6M16.5 17v4"/>` +
    `<rect x="4.5" y="7" width="6" height="9" rx="${RADIUS}" ${LINE}/>` +
    `<rect x="13.5" y="9" width="6" height="8" rx="${RADIUS}" fill="currentColor" stroke="currentColor" stroke-width="${STROKE}" stroke-linejoin="round"/>`,
  // A columned public building: the institution, with no flag, crest or seal.
  "public-building": `<path ${LINE} d="M3 9.5 12 4l9 5.5zM6 12.5v5M10 12.5v5M14 12.5v5M18 12.5v5M3 20.5h18"/>`,
  // A sheet with a folded corner and two lines of text: the filed form of the administrative auxiliary's desk.
  "document-sheet": `<path ${LINE} d="M7 3h7l5 5v12a1 1 0 0 1-1 1H7a1 1 0 0 1-1-1V4a1 1 0 0 1 1-1zM14 3v5h5M9.5 13h5M9.5 17h3.5"/>`,
};
const COURSE_GLYPHS = {
  "crypto-futures": "candlestick",
  "age-administrativo-c1": "public-building",
  "age-auxiliar-c2": "document-sheet",
};

const HEADER = "<!-- SPDX-License-Identifier: AGPL-3.0-only -->\n";
const num = (n) => String(Math.round(n * 100) / 100);

function svg(box, body, color, pad = 0) {
  const fill = color ? ` color="${color}"` : "";
  const viewBox = [box.x - pad, box.y - pad, box.w + 2 * pad, box.h + 2 * pad].map(num).join(" ");
  return `${HEADER}<svg xmlns="http://www.w3.org/2000/svg" viewBox="${viewBox}"${fill}>${body}</svg>\n`;
}

const at = (x, y, scale, body) => `<g transform="translate(${num(x)} ${num(y)}) scale(${num(scale)})">${body}</g>`;

function lockupHorizontal() {
  const scale = (1.25 * WORD_BOX.h) / BOX;
  const size = BOX * scale;
  const gap = 0.45 * WORD_BOX.h;
  const top = WORD_BOX.y - (size - WORD_BOX.h) / 2;
  const x = WORD_BOX.x - size - gap;
  return {
    box: { x, y: top, w: size + gap + WORD_BOX.w, h: size },
    body: at(x, top, scale, MARK) + WORDMARK,
  };
}

function lockupStacked() {
  const scale = (2 * WORD_BOX.h) / BOX;
  const size = BOX * scale;
  const gap = 0.35 * WORD_BOX.h;
  const x = WORD_BOX.x + (WORD_BOX.w - size) / 2;
  const y = WORD_BOX.y - gap - size;
  return { box: { x: WORD_BOX.x, y, w: WORD_BOX.w, h: size + gap + WORD_BOX.h }, body: at(x, y, scale, MARK) + WORDMARK };
}

const PIECES = {
  mark: { box: { x: 0, y: 0, w: BOX, h: BOX }, body: MARK },
  wordmark: { box: WORD_BOX, body: WORDMARK },
  "lockup-horizontal": lockupHorizontal(),
  "lockup-stacked": lockupStacked(),
};

// The tab icon: the mark in paper on an ink tile, readable on light and dark tab strips alike.
const FAVICON = svg(
  { x: 0, y: 0, w: 32, h: 32 },
  `<rect width="32" height="32" rx="7" fill="${identity.colors.ink}"/>` + at(1.9, 2.2, 1.2, MARK),
  identity.colors.paper,
);

function tokensCss() {
  const block = (selector, theme) =>
    `${selector} {\n  --brand-fg: ${theme.fg};\n  --brand-bg: ${theme.bg};\n}\n`;
  const { light, dark, oled } = identity.themes;
  return (
    "/* Generated by scripts/identity/build.mjs from identity.json; edit that file, not this one. */\n" +
    block(":root", light) +
    block(".dark", dark) +
    block(".oled", oled)
  );
}

async function rasterize(source, sizes) {
  const browser = await chromium.launch();
  const page = await browser.newPage();
  const data = `data:image/svg+xml;base64,${Buffer.from(source).toString("base64")}`;
  const files = {};
  for (const size of sizes) {
    await page.setViewportSize({ width: size, height: size });
    await page.setContent(
      `<html><body style="margin:0;background:transparent"><img src="${data}" width="${size}" height="${size}"></body></html>`,
    );
    await page.locator("img").evaluate((img) => img.decode());
    files[size] = await page.screenshot({ omitBackground: true });
  }
  await browser.close();
  return files;
}

const sha256 = (text) => createHash("sha256").update(text).digest("hex");

function write(path, text) {
  mkdirSync(dirname(path), { recursive: true });
  writeFileSync(path, text);
}

for (const [name, piece] of Object.entries(PIECES)) {
  // Text pieces get a hair of margin so the scale's round caps are never clipped.
  const pad = name === "mark" ? 0 : 1;
  write(resolve(OUT, `curset-${name}-light.svg`), svg(piece.box, piece.body, identity.themes.light.fg, pad));
  write(resolve(OUT, `curset-${name}-dark.svg`), svg(piece.box, piece.body, identity.themes.dark.fg, pad));
  write(resolve(OUT, `curset-${name}-mono.svg`), svg(piece.box, piece.body, undefined, pad));
}
for (const [slug, glyph] of Object.entries(COURSE_GLYPHS)) {
  write(resolve(CONTENT, slug, "identity", `${glyph}.svg`), svg({ x: 0, y: 0, w: BOX, h: BOX }, GLYPHS[glyph]));
}
write(resolve(OUT, "favicon.svg"), FAVICON);
write(resolve(OUT, "tokens.css"), tokensCss());

const SIZES = [16, 32, 180, 512];
const pngs = await rasterize(FAVICON, SIZES);
const sources = {};
for (const size of SIZES) {
  writeFileSync(resolve(OUT, `favicon-${size}.png`), pngs[size]);
  sources[`favicon-${size}.png`] = { source: "favicon.svg", sourceSha256: sha256(FAVICON), size };
}
write(resolve(OUT, "png-sources.json"), `${JSON.stringify(sources, null, 2)}\n`);
console.log(`identity: ${Object.keys(PIECES).length * 3} pieces, favicon + ${SIZES.length} PNGs, ${Object.keys(COURSE_GLYPHS).length} glyphs`);
