// @vitest-environment jsdom
import { createHash } from "node:crypto";
import { existsSync, readFileSync, readdirSync, statSync } from "node:fs";
import { resolve } from "node:path";
import { load } from "js-yaml";
import { describe, expect, it } from "vitest";
import identity from "@/assets/identity/identity.json";
import sources from "@/assets/identity/png-sources.json";
import { CONTENT_ROOT } from "@/test/courseContent";

const DIR = resolve(__dirname);
const PIECES = ["mark", "wordmark", "lockup-horizontal", "lockup-stacked"];
const VARIANTS = ["light", "dark", "mono"];
const courses = readdirSync(CONTENT_ROOT).filter((slug) => existsSync(resolve(CONTENT_ROOT, slug, "course.yaml")));
const glyphFiles = courses.flatMap((slug) => {
  const dir = resolve(CONTENT_ROOT, slug, "identity");
  return existsSync(dir) ? readdirSync(dir).map((name) => resolve(dir, name)) : [];
});
const svgFiles = [...readdirSync(DIR).filter((name) => name.endsWith(".svg")).map((name) => resolve(DIR, name)), ...glyphFiles];

const read = (name: string) => readFileSync(resolve(DIR, name), "utf8");

describe("the identity artwork", () => {
  it.each(PIECES.flatMap((piece) => VARIANTS.map((variant) => `curset-${piece}-${variant}.svg`)))("has %s", (name) => {
    expect(existsSync(resolve(DIR, name))).toBe(true);
  });

  it.each(svgFiles)("%s is a valid SVG: a viewBox, no script, nothing fetched from elsewhere, under 20 KB", (path) => {
    const source = readFileSync(path, "utf8");
    const parsed = new DOMParser().parseFromString(source, "image/svg+xml");
    expect(parsed.getElementsByTagName("parsererror")).toHaveLength(0);
    expect(parsed.documentElement.tagName).toBe("svg");
    expect(parsed.documentElement.getAttribute("viewBox")).toMatch(/^-?[\d.]+ -?[\d.]+ [\d.]+ [\d.]+$/);
    expect(source).not.toMatch(/<script|\son\w+=/i);
    expect(source).not.toMatch(/(?:href|src)="(?!#)|url\(/);
    expect(statSync(path).size).toBeLessThan(20 * 1024);
  });

  it.each(PIECES)("draws the %s in currentColor, the light and dark files differing only in the colour they set", (piece) => {
    const mono = read(`curset-${piece}-mono.svg`);
    expect(mono).not.toMatch(/#[0-9a-f]{3,6}\b/i);
    const coloured = (fg: string) => mono.replace(/(<svg[^>]*)>/, `$1 color="${fg}">`);
    expect(read(`curset-${piece}-light.svg`)).toBe(coloured(identity.themes.light.fg));
    expect(read(`curset-${piece}-dark.svg`)).toBe(coloured(identity.themes.dark.fg));
  });

  it("generates the theme tokens from identity.json", () => {
    const css = read("tokens.css");
    for (const [selector, theme] of [
      [":root", identity.themes.light],
      [".dark", identity.themes.dark],
      [".oled", identity.themes.oled],
    ] as const) {
      expect(css).toContain(`${selector} {\n  --brand-fg: ${theme.fg};\n  --brand-bg: ${theme.bg};\n}`);
    }
  });
});

describe("the favicon PNGs", () => {
  const favicon = read("favicon.svg");

  it.each(Object.entries(sources))("%s was rasterized from the favicon.svg in the repo, at its size", (name, entry) => {
    expect(entry.source).toBe("favicon.svg");
    // A stale hash means the SVG changed and `npm run identity` was not run.
    expect(entry.sourceSha256).toBe(createHash("sha256").update(favicon).digest("hex"));
    const png = readFileSync(resolve(DIR, name));
    expect(png.subarray(1, 4).toString("ascii")).toBe("PNG");
    expect([png.readUInt32BE(16), png.readUInt32BE(20)]).toEqual([entry.size, entry.size]);
  });

  it("covers the four sizes", () => {
    expect(Object.values(sources).map((entry) => entry.size)).toEqual([16, 32, 180, 512]);
  });
});

describe("the course glyphs", () => {
  it.each(courses)("%s declares a glyph that exists", (slug) => {
    const manifest = load(readFileSync(resolve(CONTENT_ROOT, slug, "course.yaml"), "utf8")) as {
      course: { glyph?: string };
    };
    expect(manifest.course.glyph).toBeTruthy();
    expect(existsSync(resolve(CONTENT_ROOT, slug, "identity", `${manifest.course.glyph}.svg`))).toBe(true);
  });
});
