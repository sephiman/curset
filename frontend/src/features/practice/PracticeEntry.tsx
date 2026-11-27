import { useNavigate } from "react-router-dom";
import { useTranslation } from "react-i18next";
import type { GeneratedFamily } from "@/api/course";
import { Button, Card } from "@/components/ui/primitives";
import { useCourse } from "@/features/courses/CourseContext";

/** The way into a lesson's or a module's practice, below its content; nothing when it has no questions. */
export function PracticeEntry({
  to,
  questions,
  families = [],
  title,
}: {
  /** The practice page, relative to the course. */
  to: string;
  questions: number | undefined;
  /** Generated families that practise this lesson, named below the hint. */
  families?: GeneratedFamily[];
  title?: string;
}) {
  const { t } = useTranslation();
  const navigate = useNavigate();
  const { path } = useCourse();
  if (!questions && families.length === 0) return null;
  return (
    <Card className="mt-8 flex flex-col gap-3 p-4 sm:flex-row sm:items-center sm:justify-between">
      <div>
        <h2 className="font-semibold">{title ?? t("practice.entry")}</h2>
        {questions ? (
          <p className="text-sm text-gray-500 dark:text-gray-400">{t("practice.entryHint", { count: questions })}</p>
        ) : null}
        {families.length > 0 && (
          <p className="text-sm text-gray-500 dark:text-gray-400">
            {t("practice.generatedFamilies", { families: families.map((family) => family.title).join(", ") })}
          </p>
        )}
      </div>
      <Button className="shrink-0" onClick={() => navigate(path(to))}>
        {t("practice.entry")}
      </Button>
    </Card>
  );
}
