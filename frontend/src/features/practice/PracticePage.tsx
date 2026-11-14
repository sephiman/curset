import { Link, useParams } from "react-router-dom";
import { useQuery } from "@tanstack/react-query";
import { useTranslation } from "react-i18next";
import { getLesson } from "@/api/course";
import { drawPracticeRound } from "@/api/practice";
import { Spinner } from "@/components/ui/primitives";
import { scopeKey, useCourse } from "@/features/courses/CourseContext";
import { useCourseTree } from "@/features/course/queries";
import { PracticeRound } from "@/features/practice/PracticeRound";
import { cn } from "@/lib/cn";
import { useLessonWidth } from "@/lib/lessonWidth";
import { findTemaInfo } from "@/lib/tema";

/** The «by lesson» preset: a round of one lesson's questions. */
export function PracticePage() {
  const { t } = useTranslation();
  const { lessonId = "" } = useParams();
  const { scope, path } = useCourse();
  const { lessonWidthClass } = useLessonWidth();
  const { data: courseTree } = useCourseTree();
  const { data: lesson } = useQuery({
    queryKey: ["lesson", ...scopeKey(scope), lessonId],
    queryFn: () => getLesson(scope, lessonId),
  });
  const temaInfo = findTemaInfo(courseTree, lessonId);

  if (!lesson) {
    return (
      <div className="flex justify-center py-16 text-gray-500">
        <Spinner />
      </div>
    );
  }

  return (
    <div className={cn("mx-auto space-y-4", lessonWidthClass)}>
      <div>
        <Link to={path(`/lessons/${lessonId}`)} className="text-sm text-primary hover:underline">
          ← {t("practice.back")}
        </Link>
        <h1 className="mt-2 text-xl font-bold">{t("practice.title", { title: lesson.title })}</h1>
      </div>

      <PracticeRound
        draw={(all) => drawPracticeRound(scope, lessonId, all)}
        total={lesson.practiceQuestions ?? 0}
        lessonId={lessonId}
        note={temaInfo?.temaLabel}
      />
    </div>
  );
}
