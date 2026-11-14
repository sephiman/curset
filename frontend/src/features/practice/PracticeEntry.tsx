import { useNavigate } from "react-router-dom";
import { useTranslation } from "react-i18next";
import { Button, Card } from "@/components/ui/primitives";
import { useCourse } from "@/features/courses/CourseContext";

/** The way into a lesson's or a module's practice, below its content; nothing when it has no questions. */
export function PracticeEntry({
  to,
  questions,
  title,
}: {
  /** The practice page, relative to the course. */
  to: string;
  questions: number | undefined;
  title?: string;
}) {
  const { t } = useTranslation();
  const navigate = useNavigate();
  const { path } = useCourse();
  if (!questions) return null;
  return (
    <Card className="mt-8 flex flex-col gap-3 p-4 sm:flex-row sm:items-center sm:justify-between">
      <div>
        <h2 className="font-semibold">{title ?? t("practice.entry")}</h2>
        <p className="text-sm text-gray-500 dark:text-gray-400">{t("practice.entryHint", { count: questions })}</p>
      </div>
      <Button className="shrink-0" onClick={() => navigate(path(to))}>
        {t("practice.entry")}
      </Button>
    </Card>
  );
}
