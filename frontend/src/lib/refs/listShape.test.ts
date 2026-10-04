// @vitest-environment node
import { describe, expect, it } from "vitest";
import { listShape, parseLesson, strayMarkers } from "@/lib/refs/listShape";
import { lessonMarkdown, manifestLessons, LOCALES } from "@/test/courseContent";

// Both shapes are the real damage a re-wrap did to m23-l1 and m22-l1 (EN), trimmed.
const MERGED_ITEM = `1. **Weight a signal by the session it printed in.** It often deserves
confirmation from an active session before you act on it. 2. **Know which session you actually
trade.** A scalper needs hours where the book is deep.
`;
const FLATTENED_SUBLIST = `- **Where liquidation sits relative to your stop.** Using m06's formula, \`liq = entry ×
  (1 − 1/leverage + mmr)\`: - At 5×: \`60,000 × 0.805 = 48,300\`. It is irrelevant to this
  trade. - At 20×: \`60,000 × 0.955 = 57,300\`. Still below the stop.
`;

describe("list shape", () => {
  it("counts items, nested items and numbered items", () => {
    const tree = parseLesson("1. one\n2. two\n   - a\n   - b\n\n- three\n");
    expect(listShape(tree)).toEqual({ items: 5, nestedItems: 2, numberedItems: 2 });
  });

  it("finds a numbered marker pulled into the previous item", () => {
    const tree = parseLesson(MERGED_ITEM);
    expect(listShape(tree).numberedItems).toBe(1);
    expect(strayMarkers(tree)).toMatchObject([{ line: 2, marker: "2." }]);
  });

  it("finds nested markers flattened into their parent item", () => {
    const tree = parseLesson(FLATTENED_SUBLIST);
    expect(listShape(tree).nestedItems).toBe(0);
    expect(strayMarkers(tree).map((m) => [m.line, m.marker])).toEqual([[2, "-"], [3, "-"]]);
  });

  it("ignores hyphens inside code spans and numbers that end a sentence", () => {
    const tree = parseLesson("The spread is `a - b`. The fee came to 2. Then it rose.\n");
    expect(strayMarkers(tree)).toEqual([]);
  });
});

describe("every lesson's lists", () => {
  const lessons = manifestLessons().map((lesson) => lesson.id);

  it.each(lessons)("%s has the same list structure in both locales", (lessonId) => {
    const [en, es] = LOCALES.map((locale) => listShape(parseLesson(lessonMarkdown(locale, lessonId))));
    expect(es, "a list item exists in one locale and not the other").toEqual(en);
  });

  it.each(LOCALES)("carry no list marker in the middle of a sentence (%s)", (locale) => {
    const hits = lessons.flatMap((lessonId) =>
      strayMarkers(parseLesson(lessonMarkdown(locale, lessonId))).map(
        (m) => `${lessonId}:${m.line} «${m.marker}» …${m.context}…`,
      ),
    );
    expect(hits, "a list marker that no longer starts its line renders as literal text").toEqual([]);
  });
});
