// @vitest-environment node
import { readFileSync, writeFileSync } from "node:fs";
import { resolve } from "node:path";
import { describe, expect, it } from "vitest";
import { buildRefReport, formatRefReport, type RefReport, type RefReportLesson } from "@/lib/refs/report";
import { GOLDEN_COURSES, type CourseContent, type Locale } from "@/test/courseContent";

/**
 * The golden reference report, per course and per language the course declares: frozen, reviewed by
 * hand, and loud when it moves — the same discipline as `glossary-links.<locale>.txt`, and kept beside
 * it in each course's directory.
 *
 * Regenerate with `UPDATE_LESSON_REFS=1 npx vitest run src/lib/refs/report.test.ts` and READ THE
 * DIFF. The zero-dangling test below is each course's permanent prose-integrity guard: every
 * id-shaped mention in every lesson must name a module or lesson of that same course.
 */

const UPDATE = process.env.UPDATE_LESSON_REFS === "1";
const SLOW = 120_000;

function courseLessons(course: CourseContent, locale: Locale): RefReportLesson[] {
  return course.lessons().map((lesson) => ({
    id: lesson.id,
    key: lesson.key ?? lesson.id,
    markdown: course.lessonMarkdown(locale, lesson.id),
  }));
}

function goldenPath(course: CourseContent, locale: Locale): string {
  return resolve(course.dir, `lesson-refs.${locale}.txt`);
}

function build(course: CourseContent, locale: Locale): RefReport {
  return buildRefReport(courseLessons(course, locale), course.refModules(locale), locale);
}

const reports = new Map<string, RefReport>();
function report(course: CourseContent, locale: Locale): RefReport {
  const key = `${course.slug}/${locale}`;
  const existing = reports.get(key);
  if (existing) return existing;
  const built = build(course, locale);
  reports.set(key, built);
  return built;
}

const CASES = GOLDEN_COURSES.flatMap((course) =>
  course.languages.map((locale) => [`${course.slug} ${locale}`, course, locale] as const),
);

describe.each(CASES)("the golden reference report (%s)", (_name, course, locale) => {
  it("matches the committed report", () => {
    const current = formatRefReport(report(course, locale));
    if (UPDATE) writeFileSync(goldenPath(course, locale), current, "utf8");
    const committed = readFileSync(goldenPath(course, locale), "utf8");
    expect(
      current,
      "the references the annotator would link have moved — review the diff, then regenerate with " +
        "UPDATE_LESSON_REFS=1",
    ).toBe(committed);
  }, SLOW);

  it("is deterministic: two runs are byte-identical", () => {
    expect(formatRefReport(build(course, locale))).toBe(formatRefReport(report(course, locale)));
  }, SLOW);

  it("leaves nothing dangling: every id-shaped mention names a module or lesson that exists", () => {
    expect(report(course, locale).dangling).toEqual([]);
  }, SLOW);

  it("never links a lesson to itself", () => {
    const loops = report(course, locale).rows.filter(
      (row) => row.kind === "lesson" && row.targetKey === row.lessonKey,
    );
    expect(loops).toEqual([]);
  }, SLOW);
});

const CRYPTO = GOLDEN_COURSES.find((course) => course.slug === "crypto-futures")!;

describe.each(CRYPTO.languages)("the crypto-futures reference report is not vacuous (%s)", (locale) => {
  it("links a real share of the course, so the guards above are not vacuous", () => {
    // A floor, not a fingerprint — the golden pins the exact set.
    const built = report(CRYPTO, locale);
    expect(built.rows.length).toBeGreaterThan(150);
    expect(new Set(built.rows.map((row) => row.lessonKey)).size).toBeGreaterThan(20);
  }, SLOW);
});

/** ES/EN parity binds two-language courses only; a one-language course has nothing to compare. */
const BILINGUAL = GOLDEN_COURSES.filter((course) => course.languages.length > 1);

describe.each(BILINGUAL.map((course) => [course.slug, course] as const))("the two locales of %s", (_name, course) => {
  it("carry the same references: the locales adapt together, mention for mention", () => {
    // Contexts differ (they are prose); the reference structure must not. A mention added to one
    // locale and not the other is a translation drifting, and this is where it gets caught.
    const shape = (locale: Locale) =>
      report(course, locale).rows.map((row) => `${row.lessonKey} ${row.mention} ${row.kind} ${row.targetKey}`);
    expect(shape("es")).toEqual(shape("en"));
  }, SLOW);
});
