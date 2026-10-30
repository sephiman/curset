import { describe, expect, it } from "vitest";
import type { Course } from "@/api/course";
import {
  buildQuestionReference,
  findTemaInfo,
  formatShortCourse,
  formatShortQuestionId,
  toRoman,
} from "@/lib/tema";

describe("toRoman", () => {
  it("converts numbers 1 through 10 to Roman numerals", () => {
    expect(toRoman(1)).toBe("I");
    expect(toRoman(2)).toBe("II");
    expect(toRoman(3)).toBe("III");
    expect(toRoman(4)).toBe("IV");
    expect(toRoman(5)).toBe("V");
    expect(toRoman(6)).toBe("VI");
    expect(toRoman(7)).toBe("VII");
    expect(toRoman(8)).toBe("VIII");
    expect(toRoman(9)).toBe("IX");
    expect(toRoman(10)).toBe("X");
  });

  it("handles non-positive values cleanly", () => {
    expect(toRoman(0)).toBe("");
    expect(toRoman(-1)).toBe("");
  });
});

describe("formatShortCourse and formatShortQuestionId", () => {
  it("shortens age-administrativo-c1 to age-c1", () => {
    expect(formatShortCourse("age-administrativo-c1")).toBe("age-c1");
    expect(formatShortCourse("other-course")).toBe("other-course");
  });

  it("extracts short question identifier", () => {
    expect(formatShortQuestionId("m03-l03-q127")).toBe("q127");
    expect(formatShortQuestionId("q21")).toBe("q21");
    expect(formatShortQuestionId("q01")).toBe("q01");
  });
});

const AGE_COURSE: Course = {
  locale: "es",
  started: true,
  course: {
    id: "age-administrativo-c1",
    title: "Administrativo del Estado (C1)",
    subtitle: "Ingreso libre",
    description: "Programa AGE",
    lessonNoun: "tema",
  },
  blocks: [
    {
      id: "block-b",
      order: 1,
      title: "Programa",
      modules: [
        {
          id: "m03",
          order: 3,
          title: "Derecho Administrativo General",
          summary: "Summary",
          assumes: [],
          unmetPrereqs: [],
          hasContent: true,
          lessonsTotal: 1,
          lessonsCompleted: 0,
          exercisesTotal: 1,
          exercisesPassed: 0,
          lessons: [
            {
              id: "m03-l03",
              order: 3,
              title: "El acto administrativo",
              summary: "Summary",
              completed: false,
              readingSeconds: 300,
              exercises: [],
            },
          ],
        },
      ],
    },
  ],
};

const CRYPTO_COURSE: Course = {
  locale: "en",
  started: true,
  course: {
    id: "crypto-futures",
    title: "Crypto Futures",
    subtitle: "Trading",
    description: "Futures",
  },
  blocks: [],
};

describe("findTemaInfo and buildQuestionReference", () => {
  it("computes tema label for AGE lessons", () => {
    const info = findTemaInfo(AGE_COURSE, "m03-l03");
    expect(info).not.toBeNull();
    expect(info?.moduleRoman).toBe("III");
    expect(info?.lessonOrder).toBe(3);
    expect(info?.temaCode).toBe("III.3");
    expect(info?.temaLabel).toBe("Tema III.3 · El acto administrativo");
  });

  it("builds copyable question reference for quiz and case questions", () => {
    expect(buildQuestionReference(AGE_COURSE, "m03-l03", "m03-l03-q127")).toBe(
      "age-c1 · III.3 · q127",
    );
    expect(buildQuestionReference(AGE_COURSE, "m03-l03", "q21")).toBe(
      "age-c1 · III.3 · q21",
    );
  });

  it("returns null for courses without lesson_noun (crypto-futures)", () => {
    expect(findTemaInfo(CRYPTO_COURSE, "m01-l01")).toBeNull();
    expect(buildQuestionReference(CRYPTO_COURSE, "m01-l01", "q1")).toBeNull();
  });
});
