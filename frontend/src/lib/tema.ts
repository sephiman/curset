import type { Course } from "@/api/course";

/**
 * Converts a positive integer to Roman numerals (e.g. 1 -> "I", 3 -> "III", 6 -> "VI").
 * Returns empty string for numbers <= 0.
 */
export function toRoman(n: number): string {
  if (n <= 0) return "";
  const romanMap: [number, string][] = [
    [1000, "M"],
    [900, "CM"],
    [500, "D"],
    [400, "CD"],
    [100, "C"],
    [90, "XC"],
    [50, "L"],
    [40, "XL"],
    [10, "X"],
    [9, "IX"],
    [5, "V"],
    [4, "IV"],
    [1, "I"],
  ];
  let result = "";
  let current = n;
  for (const [val, roman] of romanMap) {
    while (current >= val) {
      result += roman;
      current -= val;
    }
  }
  return result;
}

/**
 * Formats short course identifier (e.g. "age-administrativo-c1" -> "age-c1").
 */
export function formatShortCourse(courseId: string): string {
  if (courseId === "age-administrativo-c1") return "age-c1";
  return courseId;
}

/**
 * Formats short question id (e.g. "m03-l03-q127" -> "q127", "q21" -> "q21").
 */
export function formatShortQuestionId(questionId: string): string {
  const match = questionId.match(/(q\d+)$/);
  return match ? match[1] : questionId;
}

export interface TemaInfo {
  moduleRoman: string;
  lessonOrder: number;
  temaCode: string;
  title: string;
  temaLabel: string;
}

/**
 * Locates the lesson within the course tree and extracts its Roman module numeral,
 * lesson order, and formatted tema label («Tema III.3 · <title>»).
 * Returns null if course has no lessonNoun or lesson is not found.
 */
export function findTemaInfo(
  course: Course | null | undefined,
  lessonId: string | null | undefined,
): TemaInfo | null {
  if (!course || !lessonId || !course.course.lessonNoun) return null;
  for (const block of course.blocks) {
    for (const module of block.modules) {
      const lesson = module.lessons.find((l) => l.id === lessonId);
      if (!lesson) continue;
      const numMatch = module.id ? module.id.match(/^m0*(\d+)/i) : null;
      const moduleNum = numMatch ? parseInt(numMatch[1], 10) : module.order;
      const moduleRoman = toRoman(moduleNum);
      const temaCode = moduleRoman ? `${moduleRoman}.${lesson.order}` : `${lesson.order}`;
      const noun = course.course.lessonNoun;
      const capitalizedNoun = noun ? noun.charAt(0).toUpperCase() + noun.slice(1) : "";
      const temaLabel = `${capitalizedNoun} ${temaCode} · ${lesson.title}`;
      return {
        moduleRoman,
        lessonOrder: lesson.order,
        temaCode,
        title: lesson.title,
        temaLabel,
      };
    }
  }
  return null;
}

/**
 * Builds the copyable stable question reference (e.g. "age-c1 · III.3 · q127").
 * Returns null if course has no lessonNoun, or if questionId/temaInfo are missing.
 */
export function buildQuestionReference(
  course: Course | null | undefined,
  lessonId: string | null | undefined,
  questionId: string | null | undefined,
): string | null {
  if (!course || !course.course.lessonNoun || !questionId) return null;
  const info = findTemaInfo(course, lessonId);
  if (!info) return null;
  const shortCourse = formatShortCourse(course.course.id);
  const shortQ = formatShortQuestionId(questionId);
  return `${shortCourse} · ${info.temaCode} · ${shortQ}`;
}
