import { useState } from "react";
import { Link } from "react-router-dom";
import { useTranslation } from "react-i18next";
import type { LessonLink as LessonTarget, NoExcerpt, OptionView, SolutionExcerpt } from "@/api/exercises";
import { CopyableReference } from "@/components/ui/CopyableReference";
import { useCourse } from "@/features/courses/CourseContext";
import { useCourseTree } from "@/features/course/queries";
import { SolutionBody, Verdict } from "@/features/exercises/AttemptResult";
import { ReportQuestion } from "@/features/reports/ReportQuestion";
import { buildQuestionReference } from "@/lib/tema";

/** «Tema 3: Las fuentes del Derecho»: the course's noun for a lesson, its place in its module, its title. */
function useLessonLabel(lessonId: string): string | null {
  const { t } = useTranslation();
  const { data: course } = useCourseTree();
  if (!course) return null;
  for (const block of course.blocks) {
    for (const module of block.modules) {
      const lesson = module.lessons.find((l) => l.id === lessonId);
      if (!lesson) continue;
      const noun = course.course.lessonNoun ?? t("byLesson.lesson");
      return t("solution.lessonLabel", {
        noun: noun.charAt(0).toUpperCase() + noun.slice(1),
        number: lesson.order,
        title: lesson.title,
      });
    }
  }
  return null;
}

function Paragraphs({ text }: { text: string }) {
  return (
    <>
      {text.split(/\n{2,}/).map((paragraph, i) => (
        <p key={i} className="break-words">
          {paragraph}
        </p>
      ))}
    </>
  );
}

// The lesson and source links: inline text above 768 px, a row of two buttons on a phone (J7).
const LINK =
  "font-medium text-primary hover:underline max-md:flex max-md:min-h-11 max-md:items-center max-md:justify-center max-md:rounded-md max-md:border max-md:border-border max-md:px-3 max-md:text-center max-md:leading-tight max-md:hover:no-underline dark:max-md:border-gray-700 oled:max-md:border-oled-line-strong";

/** The norm's own words, under «Art. 30.4 LPAC»; the whole article one tap away when it fits. */
function ExcerptBlock({ excerpt }: { excerpt: SolutionExcerpt }) {
  const { t } = useTranslation();
  const [whole, setWhole] = useState(false);
  return (
    <figure className="rounded-md border-l-4 border-primary/60 bg-gray-50 p-3 max-md:ring-1 max-md:ring-border dark:bg-gray-900 dark:max-md:ring-gray-800 oled:bg-oled-bg oled:ring-1 oled:ring-oled-line">
      <figcaption className="mb-2 text-sm font-semibold text-gray-800 dark:text-gray-100">{excerpt.heading}</figcaption>
      <blockquote className="space-y-2 text-sm leading-relaxed text-gray-700 dark:text-gray-300">
        <Paragraphs text={whole && excerpt.full ? excerpt.full : excerpt.text} />
      </blockquote>
      {excerpt.attribution && (
        <p className="mt-2 text-xs text-gray-500 dark:text-gray-400">{excerpt.attribution}</p>
      )}
      {excerpt.full && (
        <button
          type="button"
          className="mt-2 text-xs font-medium text-primary hover:underline"
          aria-expanded={whole}
          onClick={() => setWhole((open) => !open)}
        >
          {whole ? t("solution.showExcerpt") : t("solution.showFull")}
        </button>
      )}
      {excerpt.fullTooLong && (
        <a
          href={excerpt.href}
          target="_blank"
          rel="noreferrer"
          className="mt-2 inline-block text-xs font-medium text-primary hover:underline"
        >
          {t("solution.showFull")}
        </a>
      )}
    </figure>
  );
}

/**
 * «Ver solución» (delta F1): collapsed under the verdict once a question is answered, or in a submitted
 * exam's review. In order: the correct option, the explanation, the cited text of the norm, the links to
 * the lesson and to the source, and the report button, so a reader who has seen the norm and still
 * disagrees reports from here. Never rendered before the answer is known.
 */
export function SolutionPanel({
  attemptId,
  questionId,
  lessonId,
  reference: explicitReference,
  correct,
  correctAnswer,
  solutionSteps,
  explanation,
  options,
  excerpt,
  noExcerpt,
  lessonLink,
  reportable,
  hideVerdict = false,
  open = false,
}: {
  attemptId: string;
  questionId?: string | null;
  lessonId?: string | null;
  reference?: string | null;
  correct: boolean;
  correctAnswer: unknown;
  solutionSteps: string[];
  explanation: string | null;
  options?: OptionView[];
  excerpt?: SolutionExcerpt | null;
  noExcerpt?: NoExcerpt | null;
  lessonLink?: LessonTarget | null;
  reportable: boolean;
  hideVerdict?: boolean;
  /** Unfolded from the start (lesson practice: the solution is the point of answering). */
  open?: boolean;
}) {
  const { t } = useTranslation();
  const { path } = useCourse();
  const { data: course } = useCourseTree();
  const targetLessonId = lessonId ?? lessonLink?.lessonId;
  const lessonLabel = useLessonLabel(targetLessonId ?? "");
  const reference =
    explicitReference ??
    (course && questionId ? buildQuestionReference(course, targetLessonId, questionId) : null);
  return (
    <div className="mt-4 space-y-3">
      {!hideVerdict && <Verdict correct={correct} />}
      <details open={open} className="group rounded-md border border-border dark:border-gray-800 oled:border-oled-line">
        <summary className="cursor-pointer px-3 py-2 max-md:py-3 text-sm font-medium text-primary select-none">
          {t("solution.show")}
        </summary>
        <div className="space-y-3 border-t border-border px-3 py-3 dark:border-gray-800 oled:border-oled-line">
          <SolutionBody
            correctAnswer={correctAnswer}
            solutionSteps={solutionSteps}
            explanation={explanation}
            options={options}
          />
          {excerpt && <ExcerptBlock excerpt={excerpt} />}
          {!excerpt && noExcerpt && (
            <p className="text-xs text-gray-500 dark:text-gray-400">
              {t("solution.noExcerpt", { reason: t(`noExcerptReason.${noExcerpt.reason}`) })}
            </p>
          )}
          {(lessonLink || excerpt || noExcerpt?.href) && (
            <nav className="flex flex-wrap gap-x-4 gap-y-1 text-sm max-md:grid max-md:grid-cols-2 max-md:gap-2">
              {lessonLink && (
                <Link
                  to={path(`/lessons/${lessonLink.lessonId}${lessonLink.anchor ? `#${lessonLink.anchor}` : ""}`)}
                  className={LINK}
                >
                  <span className="max-md:line-clamp-2">{lessonLabel ?? t("exercise.viewInLesson")}</span>
                </Link>
              )}
              {!excerpt && lessonLink?.citation && (
                <span className="text-gray-500 max-md:order-last max-md:col-span-2 dark:text-gray-400">({lessonLink.citation})</span>
              )}
              {!excerpt && noExcerpt?.href && (
                <a href={noExcerpt.href} target="_blank" rel="noreferrer" className={LINK}>
                  {noExcerpt.href.includes("/sources/otros/") ? t("solution.savedPage") : t("solution.source")}
                </a>
              )}
              {excerpt && (
                <a href={excerpt.href} target="_blank" rel="noreferrer" className={LINK}>
                  {excerpt.attribution ? t("solution.savedPage") : t("solution.source")}
                </a>
              )}
            </nav>
          )}
          {(reference || reportable) && (
            <div className="flex flex-wrap items-center justify-between gap-3 pt-1 max-md:flex-col max-md:items-start">
              {reference && <CopyableReference reference={reference} />}
              {reportable && <ReportQuestion attemptId={attemptId} />}
            </div>
          )}
        </div>
      </details>
    </div>
  );
}
