import type { CourseMeta } from "@/api/course";

/** What a PDF prints besides the theory: nothing, crypto's in-lesson exercises, or a question-bank questionnaire. */
export type PdfExerciseMode = "none" | "inline" | "questionnaire";

/**
 * The account's switch decides; the course's `pdf_exercises` only says whether it can print exercises at
 * all, and whether it has a question bank (`lessonPractice`) says which kind.
 */
export function pdfExerciseMode(
  course: Pick<CourseMeta, "pdfExercises" | "lessonPractice" | "theoryOnly">,
  include: boolean,
): PdfExerciseMode {
  if (!include || course.pdfExercises === false || course.theoryOnly) return "none";
  return course.lessonPractice ? "questionnaire" : "inline";
}
