import { useState } from "react";
import { Link, useParams } from "react-router-dom";
import { useMutation, useQuery } from "@tanstack/react-query";
import { useTranslation } from "react-i18next";
import { getLesson } from "@/api/course";
import { drawPracticeRound, type PracticeRound } from "@/api/practice";
import { Button, Card, Spinner } from "@/components/ui/primitives";
import { scopeKey, useCourse } from "@/features/courses/CourseContext";
import { useCourseTree } from "@/features/course/queries";
import { PracticeQuestion } from "@/features/practice/PracticeQuestion";
import { cn } from "@/lib/cn";
import { findTemaInfo } from "@/lib/tema";

type Size = "twenty" | "all";

/**
 * A lesson's questions one at a time: no clock, no penalty, no score at the end. Each answer opens
 * its solution; every answer is an ordinary practice attempt, so Progress counts it.
 */
export function PracticePage() {
  const { t } = useTranslation();
  const { lessonId = "" } = useParams();
  const { scope, path } = useCourse();
  const { data: courseTree } = useCourseTree();
  const { data: lesson } = useQuery({
    queryKey: ["lesson", ...scopeKey(scope), lessonId],
    queryFn: () => getLesson(scope, lessonId),
  });
  const temaInfo = findTemaInfo(courseTree, lessonId);
  const [size, setSize] = useState<Size>("twenty");
  const [round, setRound] = useState<{ number: number; questions: PracticeRound["questions"] } | null>(null);
  const [index, setIndex] = useState(0);
  const [answered, setAnswered] = useState(false);
  const [done, setDone] = useState(false);

  const draw = useMutation({
    mutationFn: () => drawPracticeRound(scope, lessonId, size === "all"),
    meta: { silentSuccess: true },
    onSuccess: (drawn) => {
      setRound((previous) => ({ number: (previous?.number ?? 0) + 1, questions: drawn.questions }));
      setIndex(0);
      setAnswered(false);
      setDone(false);
    },
  });

  if (!lesson) {
    return (
      <div className="flex justify-center py-16 text-gray-500">
        <Spinner />
      </div>
    );
  }

  const total = lesson.practiceQuestions ?? 0;
  const last = round !== null && index === round.questions.length - 1;
  const next = () => {
    if (last) setDone(true);
    else {
      setIndex((i) => i + 1);
      setAnswered(false);
    }
  };

  return (
    <div className="mx-auto max-w-2xl space-y-4">
      <div>
        <Link to={path(`/lessons/${lessonId}`)} className="text-sm text-primary hover:underline">
          ← {t("practice.back")}
        </Link>
        <h1 className="mt-2 text-xl font-bold">{t("practice.title", { title: lesson.title })}</h1>
      </div>

      {(round === null || done) && (
        <Card className="space-y-4 p-4">
          {done && <p className="font-medium">{t("practice.done")}</p>}
          <p className="text-sm text-gray-600 dark:text-gray-300">{t("practice.intro")}</p>
          <fieldset>
            <legend className="mb-2 text-xs text-gray-500 dark:text-gray-400">{t("practice.size")}</legend>
            <div role="radiogroup" className="grid grid-cols-2 gap-2">
              {(["twenty", "all"] as const).map((choice) => (
                <label
                  key={choice}
                  className={cn(
                    "flex cursor-pointer items-center justify-center rounded-md border px-3 py-2 text-sm font-medium",
                    size === choice
                      ? "border-primary bg-primary/10 text-primary"
                      : "border-border text-gray-700 dark:border-gray-700 dark:text-gray-200",
                  )}
                >
                  <input
                    type="radio"
                    name="practice-size"
                    className="sr-only"
                    checked={size === choice}
                    onChange={() => setSize(choice)}
                  />
                  {choice === "twenty" ? t("practice.twenty") : t("practice.all", { count: total })}
                </label>
              ))}
            </div>
          </fieldset>
          <Button className="w-full sm:w-auto" disabled={draw.isPending || total === 0} onClick={() => draw.mutate()}>
            {done ? t("practice.again") : t("practice.begin")}
          </Button>
        </Card>
      )}

      {round !== null && !done && (
        <Card className="p-4">
          <p className="mb-3 text-xs text-gray-500 dark:text-gray-400">
            <span className="font-medium text-gray-700 dark:text-gray-300">
              {t("practice.progress", { number: index + 1, total: round.questions.length })}
            </span>
            {temaInfo && <span className="ml-2">· {temaInfo.temaLabel}</span>}
          </p>
          <PracticeQuestion
            key={`${round.number}-${index}`}
            round={round.number}
            question={round.questions[index]}
            lessonId={lessonId}
            onAnswered={() => setAnswered(true)}
          />
          {answered && (
            <div className="mt-4 flex justify-end">
              <Button onClick={next}>{last ? t("practice.finish") : `${t("practice.next")} →`}</Button>
            </div>
          )}
        </Card>
      )}
    </div>
  );
}
