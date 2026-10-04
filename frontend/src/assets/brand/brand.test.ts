// @vitest-environment node
import { existsSync, readFileSync, readdirSync, statSync } from "node:fs";
import { resolve } from "node:path";
import { describe, expect, it } from "vitest";

/** The Curset artwork: every theme has its logo, the tab has its icons, and the SVG sources stay clean. */

const DIR = resolve(__dirname);
const svgs = readdirSync(DIR).filter((name) => name.endsWith(".svg"));

describe("the brand artwork", () => {
  it.each(["light", "dark", "oled"])("has a logo for the %s theme, rendered from its source", (theme) => {
    expect(existsSync(resolve(DIR, `curset-logo-${theme}.svg`))).toBe(true);
    expect(existsSync(resolve(DIR, `curset-logo-${theme}.png`))).toBe(true);
  });

  it.each(["light", "dark"])("has a %s tab icon", (theme) => {
    expect(existsSync(resolve(DIR, `curset-icon-${theme}.png`))).toBe(true);
  });

  it.each(svgs)("%s is a clean SVG: a viewBox, no script, nothing fetched from elsewhere, under 20 KB", (name) => {
    const source = readFileSync(resolve(DIR, name), "utf8");
    expect(source).toMatch(/<svg[^>]*\sviewBox="[^"]+"/);
    expect(source).not.toMatch(/<script|\son\w+=/i);
    expect(source).not.toMatch(/(?:href|src)="(?!#)/);
    expect(statSync(resolve(DIR, name)).size).toBeLessThan(20 * 1024);
  });

  it("says who made it, in small type under the name", () => {
    for (const theme of ["light", "dark", "oled"]) {
      expect(readFileSync(resolve(DIR, `curset-logo-${theme}.svg`), "utf8")).toContain(">a Sephimandev app<");
    }
  });
});
