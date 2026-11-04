import { Link, useParams } from "react-router-dom";
import { useQuery } from "@tanstack/react-query";
import { useTranslation } from "react-i18next";
import { getModule } from "@/api/course";
import { formatReadingTime, remainingSeconds } from "@/features/course/readingTime";
import { Badge, Card, Spinner } from "@/components/ui/primitives";
import { scopeKey, useCourse } from "@/features/courses/CourseContext";
import { OneLineSummary } from "@/features/course/OneLineSummary";
import { useCourseTree } from "@/features/course/queries";

export function ModulePage() {
  const { t } = useTranslation();
  const { moduleId = "" } = useParams();
  const { scope, path } = useCourse();
  const { data: module, isLoading } = useQuery({
    queryKey: ["module", ...scopeKey(scope), moduleId],
    queryFn: () => getModule(scope, moduleId),
  });
  // The module endpoint carries no lesson summaries; the course tree (already cached) does.
  const { data: tree } = useCourseTree();
  const lessonSummaries = new Map(
    (tree?.blocks ?? []).flatMap((block) => block.modules.flatMap((m) => m.lessons.map((l) => [l.id, l.summary] as const))),
  );

  if (isLoading || !module) {
    return (
      <div className="flex justify-center py-16 text-gray-500">
        <Spinner />
      </div>
    );
  }

  // The same number the module's card on the course page shows: time left, from the same per-lesson
  // seconds, hidden entirely once the module is read.
  const timeLeft = formatReadingTime(remainingSeconds(module.lessons), t);

  return (
    <div className="space-y-6">
      <div>
        <Link to={path()} className="text-sm text-primary hover:underline">
          ← {t("nav.course")}
        </Link>
        <h1 className="mt-2 text-2xl font-bold">{module.title}</h1>
        <p className="mt-1 text-gray-500 dark:text-gray-400">{module.summary}</p>
        {timeLeft !== null && (
          <p className="mt-2 text-xs text-gray-500 dark:text-gray-400">{timeLeft}</p>
        )}
      </div>

      {module.unmetPrereqs.length > 0 && module.lessons.some((l) => !l.completed) && (
        <p className="text-sm text-gray-400 dark:text-gray-500">
          {t("course.prereqNoticeLong")} {module.unmetPrereqs.map((p) => p.title ?? p.id).join(", ")}.
        </p>
      )}

      <div className="space-y-2">
        {module.lessons.map((lesson) => {
          const summary = lessonSummaries.get(lesson.id);
          // K6: title and one-line summary, then reading time and «Practicar». The title's link stretches
          // over the row; «Practicar» and the summary's «más» sit above it. On a phone the time stays
          // beside the title and «Practicar» drops below.
          return (
            <Card
              key={lesson.id}
              className="relative grid grid-cols-[minmax(0,1fr)_auto] items-baseline gap-x-3 p-4 hover:border-primary md:grid-cols-[minmax(0,1fr)_auto_auto] md:items-center md:gap-x-6"
            >
              <Link
                to={path(`/lessons/${lesson.id}`)}
                className="col-start-1 row-start-1 font-medium after:absolute after:inset-0 after:rounded-lg focus:outline-none focus-visible:after:ring-2 focus-visible:after:ring-primary"
              >
                {lesson.title}
              </Link>
              {/* Each row carries the lesson's OWN full estimate — the same number its page shows, and
                  the reason the header's remaining total can be smaller: a read lesson still costs what
                  it costs, it just no longer counts as time left. */}
              <span className="col-start-2 row-start-1 flex shrink-0 items-center gap-2 md:row-span-2">
                <span className="text-xs text-gray-500 dark:text-gray-400">
                  {formatReadingTime(lesson.readingSeconds, t)}
                </span>
                {lesson.completed && <Badge tone="green">{t("course.completed")}</Badge>}
              </span>
              {summary && (
                <OneLineSummary
                  text={summary}
                  everywhere
                  className="col-span-2 row-start-2 mt-0.5 text-sm text-gray-500 md:col-span-1 dark:text-gray-400"
                />
              )}
              {(lesson.practiceQuestions ?? 0) > 0 && (
                <Link
                  to={path(`/lessons/${lesson.id}/practice`)}
                  className="relative z-10 col-span-2 row-start-3 -mb-2 inline-flex min-h-11 items-center justify-self-start text-sm font-medium text-primary hover:underline md:col-span-1 md:col-start-3 md:row-span-2 md:row-start-1 md:mb-0 md:min-h-0"
                >
                  {t("practice.entry")}
                </Link>
              )}
            </Card>
          );
        })}
      </div>
    </div>
  );
}
