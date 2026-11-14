import { Link, useParams } from "react-router-dom";
import { useQuery } from "@tanstack/react-query";
import { useTranslation } from "react-i18next";
import { getModule } from "@/api/course";
import { drawModuleRound } from "@/api/practice";
import { Spinner } from "@/components/ui/primitives";
import { scopeKey, useCourse } from "@/features/courses/CourseContext";
import { PracticeRound } from "@/features/practice/PracticeRound";
import { cn } from "@/lib/cn";
import { useLessonWidth } from "@/lib/lessonWidth";

/** The «by module» preset: a round of every lesson's questions in one module. */
export function ModulePracticePage() {
  const { t } = useTranslation();
  const { moduleId = "" } = useParams();
  const { scope, path } = useCourse();
  const { lessonWidthClass } = useLessonWidth();
  const { data: module } = useQuery({
    queryKey: ["module", ...scopeKey(scope), moduleId],
    queryFn: () => getModule(scope, moduleId),
  });

  if (!module) {
    return (
      <div className="flex justify-center py-16 text-gray-500">
        <Spinner />
      </div>
    );
  }

  const total = module.lessons.reduce((sum, lesson) => sum + (lesson.practiceQuestions ?? 0), 0);
  return (
    <div className={cn("mx-auto space-y-4", lessonWidthClass)}>
      <div>
        <Link to={path(`/modules/${moduleId}`)} className="text-sm text-primary hover:underline">
          ← {t("practice.moduleBack")}
        </Link>
        <h1 className="mt-2 text-xl font-bold">{t("practice.title", { title: module.title })}</h1>
      </div>
      <PracticeRound draw={(all) => drawModuleRound(scope, moduleId, all)} total={total} />
    </div>
  );
}
