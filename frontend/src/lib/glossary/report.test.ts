// @vitest-environment node
import { readFileSync, writeFileSync } from "node:fs";
import { resolve } from "node:path";
import { describe, expect, it } from "vitest";
import {
  buildLinkReport,
  formatLinkReport,
  type LinkReport,
  type ReportLesson,
} from "@/lib/glossary/report";
import { GOLDEN_COURSES, type CourseContent, type Locale } from "@/test/courseContent";

/**
 * The golden link report, per course and per language the course declares: frozen, reviewed by
 * hand, and loud when it moves. Each course keeps its own `glossary-links.<locale>.txt` beside its
 * manifest, so a change in one course can never move another's golden.
 *
 * Regenerate with `UPDATE_GLOSSARY_LINKS=1 npx vitest run src/lib/glossary/report.test.ts` and READ
 * THE DIFF — it is the only place a false positive is caught before a reader meets it.
 */

const UPDATE = process.env.UPDATE_GLOSSARY_LINKS === "1";
/** Building the report walks every lesson twice; under a full parallel run that outlasts the 5s default. */
const SLOW = 120_000;

/**
 * Course reading order, which is what the PDF's "first occurrence in the book" means.
 *
 * The report's lesson axis is the permanent KEY (matching the yaml's `origin`/`link_except`), so a
 * display renumbering leaves every line's lesson column untouched; only genuine order changes diff.
 */
function courseLessons(course: CourseContent, locale: Locale): ReportLesson[] {
  return course.lessons().map((lesson) => ({
    id: lesson.key ?? lesson.id,
    markdown: course.lessonMarkdown(locale, lesson.id),
  }));
}

function goldenPath(course: CourseContent, locale: Locale): string {
  return resolve(course.dir, `glossary-links.${locale}.txt`);
}

/** The whole course, twice per locale, is the expensive part — build it once and read it many times. */
const reports = new Map<string, LinkReport>();
function report(course: CourseContent, locale: Locale): LinkReport {
  const key = `${course.slug}/${locale}`;
  const existing = reports.get(key);
  if (existing) return existing;
  const built = generateReport(course, locale);
  reports.set(key, built);
  return built;
}

function generateReport(course: CourseContent, locale: Locale): LinkReport {
  return buildLinkReport(courseLessons(course, locale), course.glossary(locale, "key"), locale);
}

const CASES = GOLDEN_COURSES.flatMap((course) =>
  course.languages.map((locale) => [`${course.slug} ${locale}`, course, locale] as const),
);

describe.each(CASES)("the golden link report (%s)", (_name, course, locale) => {
  it("matches the committed report", () => {
    const current = formatLinkReport(generateReport(course, locale));
    if (UPDATE) writeFileSync(goldenPath(course, locale), current, "utf8");
    const committed = readFileSync(goldenPath(course, locale), "utf8");
    expect(
      current,
      "the links the annotator would draw have moved — review the diff, then regenerate with " +
        "UPDATE_GLOSSARY_LINKS=1",
    ).toBe(committed);
  }, SLOW);

  it("is deterministic: two runs are byte-identical", () => {
    expect(formatLinkReport(generateReport(course, locale))).toBe(formatLinkReport(generateReport(course, locale)));
  }, SLOW);

  it("never links a term in a lesson that term points back at", () => {
    const origins = new Map(
      course.glossary(locale, "key").map((entry) => [
        entry.id,
        new Set([entry.origin, ...(entry.senses ?? []).map((sense) => sense.origin)].filter(Boolean)),
      ]),
    );
    const loops = report(course, locale).rows.filter((row) => origins.get(row.termId)?.has(row.lessonId));
    expect(loops).toEqual([]);
  }, SLOW);

  it("links each term at most once in the whole book", () => {
    // Every `WP` row is a web row by construction; what this pins is that one term never claims two
    // places in the book, which is what the global policy means.
    const linked = report(course, locale).rows.filter((row) => row.flag === "WP").map((row) => row.termId);
    expect(new Set(linked).size).toBe(linked.length);
  }, SLOW);
});

const CRYPTO = GOLDEN_COURSES.find((course) => course.slug === "crypto-futures")!;

describe.each(CRYPTO.languages)("the crypto-futures report is not vacuous (%s)", (locale) => {
  it("marks something in most lessons, and links a real share of the glossary", () => {
    // A floor, not a fingerprint: if a refactor quietly stopped matching, the report above would
    // still "match" nothing against nothing on the day it is regenerated without being read. Pinned
    // to the large course; a two-term fixture course has no floor to speak of.
    const built = report(CRYPTO, locale);
    expect(new Set(built.rows.map((row) => row.lessonId)).size).toBeGreaterThan(25);
    expect(built.rows.filter((row) => row.flag === "WP").length).toBeGreaterThan(30);
  }, SLOW);

  it("shows a moved link as a diff when the prose changes", () => {
    const lessons = courseLessons(CRYPTO, locale);
    const entries = CRYPTO.glossary(locale, "key");
    // A synthetic edit: the same prose with its first two lessons swapped moves every term whose
    // first occurrence lived in either of them.
    const swapped = [lessons[1], lessons[0], ...lessons.slice(2)];
    expect(formatLinkReport(buildLinkReport(swapped, entries, locale))).not.toBe(
      formatLinkReport(report(CRYPTO, locale)),
    );
  }, SLOW);
});
