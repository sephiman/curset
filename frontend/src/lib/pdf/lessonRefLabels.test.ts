import { describe, expect, it } from "vitest";
import type { TDocumentDefinitions } from "pdfmake/interfaces";
import { buildCourseDocument, lessonSections, type DocumentPart } from "@/lib/pdf/document";
import { DEST } from "@/lib/pdf/pagination";
import { lessonReferenceLabel } from "@/lib/tema";
import {
  CONTENT_ROOT,
  courseContent,
  exportPart,
  figureDirectives,
  outlineFromManifest,
  stubFigures,
  type Locale,
} from "@/test/courseContent";
import { testPdfLabels } from "@/test/printLabels";

/**
 * N5: a reference to another lesson prints as that lesson's label — «tema IV.1 · <title>» in a course with
 * a lesson noun, the title in one without — never as the id the prose was written with. It links when the
 * document prints that lesson and is plain text otherwise. Read off the definition; the content is untouched.
 */

function build(slug: string, locale: Locale, part?: DocumentPart): TDocumentDefinitions {
  const course = courseContent(`${CONTENT_ROOT}/${slug}`);
  const whole = course.courseExport(locale);
  return buildCourseDocument({
    courseTitle: "T",
    courseSubtitle: "S",
    courseDescription: "D",
    export: part ? exportPart(whole, part) : whole,
    figures: stubFigures(slug === "crypto-futures" ? figureDirectives(locale) : []),
    exercises: { locale, lessons: [], excluded: [] },
    pdfExercises: false,
    exerciseCharts: new Map(),
    part,
    outline: outlineFromManifest(course.manifest(), locale),
    labels: testPdfLabels(locale),
  });
}

function values(node: unknown, key: string, found: unknown[] = []): unknown[] {
  if (Array.isArray(node)) node.forEach((child) => values(child, key, found));
  else if (typeof node === "object" && node !== null) {
    if (key in node) found.push((node as Record<string, unknown>)[key]);
    Object.values(node).forEach((child) => values(child, key, found));
  }
  return found;
}

function textOf(node: unknown): string {
  return values(node, "text")
    .flat(Infinity)
    .filter((value): value is string => typeof value === "string")
    .join("");
}

/** The runs that carry a link to a lesson's heading, with the text they print. */
function linkedText(node: unknown, lessonId: string): string[] {
  const runs: string[] = [];
  const walk = (n: unknown): void => {
    if (Array.isArray(n)) n.forEach(walk);
    else if (typeof n === "object" && n !== null) {
      const record = n as Record<string, unknown>;
      if (record.linkToDestination === DEST.outline(lessonId) && typeof record.text === "string") runs.push(record.text);
      Object.values(record).forEach(walk);
    }
  };
  walk(node);
  return runs;
}

function section(doc: TDocumentDefinitions, lessonId: string): unknown {
  const found = lessonSections(doc).find((s) => s.lessonId === lessonId);
  if (!found) throw new Error(`${lessonId} is not printed`);
  return found;
}

const label = (slug: string, locale: Locale, lessonId: string) =>
  lessonReferenceLabel(outlineFromManifest(courseContent(`${CONTENT_ROOT}/${slug}`).manifest(), locale), lessonId);

describe("age-administrativo-c1: m01-l03 cites m01-l05 (its bloque) and m03-l01 (another)", () => {
  const C1 = "age-administrativo-c1";

  it("labels with the course's noun and the tema number: «tema I.5 · <title>»", () => {
    expect(label(C1, "es", "m01-l05")).toMatch(/^tema I\.5 · \S/);
    expect(label(C1, "es", "m03-l01")).toMatch(/^tema III\.1 · \S/);
  });

  it("in the bloque, links the sibling under its label and prints the other bloque's tema as text", () => {
    const lesson = section(build(C1, "es", { kind: "module", id: "m01", title: "M01" }), "m01-l03");
    expect(linkedText(lesson, "m01-l05").join("")).toBe(label(C1, "es", "m01-l05"));
    expect(linkedText(lesson, "m03-l01")).toEqual([]);
    expect(textOf(lesson)).toContain(label(C1, "es", "m03-l01"));
  });

  it("in the tema alone, prints both as text", () => {
    const lesson = section(build(C1, "es", { kind: "lesson", id: "m01-l03", title: "M01-L03" }), "m01-l03");
    expect(linkedText(lesson, "m01-l05")).toEqual([]);
    expect(textOf(lesson)).toContain(label(C1, "es", "m01-l05"));
    expect(textOf(lesson)).toContain(label(C1, "es", "m03-l01"));
  });

  it("in the whole course, links both under their labels and prints no lesson id anywhere in the prose", () => {
    const doc = build(C1, "es");
    const lesson = section(doc, "m01-l03");
    expect(linkedText(lesson, "m03-l01").join("")).toBe(label(C1, "es", "m03-l01"));
    const prose = lessonSections(doc).map(textOf).join("\n");
    expect(prose.match(/\bm\d{2}-l\d{2}\b/g) ?? []).toEqual([]);
  });
});

describe("aeat-agentes-hacienda: m02-l02 cites m02-l01 (its bloque) and m01-l05 (another)", () => {
  const AEAT = "aeat-agentes-hacienda";

  it("links the sibling and prints the other bloque's tema as text, both by label", () => {
    const lesson = section(build(AEAT, "es", { kind: "module", id: "m02", title: "M02" }), "m02-l02");
    expect(label(AEAT, "es", "m02-l01")).toMatch(/^tema II\.1 · \S/);
    expect(linkedText(lesson, "m02-l01").join("")).toBe(label(AEAT, "es", "m02-l01"));
    expect(linkedText(lesson, "m01-l05")).toEqual([]);
    expect(textOf(lesson)).toContain(label(AEAT, "es", "m01-l05"));
  });
});

describe("crypto-futures (no lesson noun): m09-l1 cites m08-l2", () => {
  const CRYPTO = "crypto-futures";

  it.each(["en", "es"] as const)("prints the lesson's title, linked in the book and as text in its module (%s)", (locale) => {
    const title = label(CRYPTO, locale, "m08-l2");
    expect(title).not.toMatch(/m08-l2/);
    const inBook = section(build(CRYPTO, locale), "m09-l1");
    expect(linkedText(inBook, "m08-l2").join("")).toBe(title);
    const inModule = section(build(CRYPTO, locale, { kind: "module", id: "m09", title: "M09" }), "m09-l1");
    expect(linkedText(inModule, "m08-l2")).toEqual([]);
    expect(textOf(inModule)).toContain(title);
    expect(textOf(inModule)).not.toMatch(/\bm08-l2\b/);
  });
});
