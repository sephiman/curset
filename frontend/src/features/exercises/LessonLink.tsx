import { Link } from "react-router-dom";
import { useTranslation } from "react-i18next";
import { useCourse } from "@/features/courses/CourseContext";

/**
 * «Ver en la lección»: the question's lesson, at the paragraph that first cites its article when it
 * cites one. Shown only where the answer is already on screen (after answering, or in a submitted
 * exam's review), like the report link beside it.
 */
export function LessonLink({
  lessonId,
  anchor,
  citation,
}: {
  lessonId: string;
  anchor: string | null;
  citation?: string | null;
}) {
  const { t } = useTranslation();
  const { path } = useCourse();
  return (
    <span className="inline-flex flex-wrap items-baseline gap-2 text-xs">
      <Link to={path(`/lessons/${lessonId}${anchor ? `#${anchor}` : ""}`)} className="font-medium text-primary hover:underline">
        {t("exercise.viewInLesson")}
      </Link>
      {citation && <span className="text-gray-500 dark:text-gray-400">({citation})</span>}
    </span>
  );
}
