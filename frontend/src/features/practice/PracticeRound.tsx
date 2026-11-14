import { useState } from "react";
import { useMutation } from "@tanstack/react-query";
import { useTranslation } from "react-i18next";
import type { DrawnRound } from "@/api/practice";
import { Button, Card } from "@/components/ui/primitives";
import { useCourseTree } from "@/features/course/queries";
import { PracticeQuestion } from "@/features/practice/PracticeQuestion";
import { cn } from "@/lib/cn";

type Size = "twenty" | "all";

/**
 * One practice round, whatever it draws from: no clock, no penalty, no score at the end. Each answer
 * opens its solution; every answer is an ordinary practice attempt, so Progress counts it.
 */
export function PracticeRound({
  draw,
  total,
  lead,
  lessonId,
  note,
}: {
  draw: (all: boolean) => Promise<DrawnRound>;
  /** How many questions «All» draws; absent: every round is the default twenty, with no size to choose. */
  total?: number;
  /** What this preset draws, said before how the round orders it. */
  lead?: string;
  /** The lesson every question belongs to; absent in a round that crosses lessons. */
  lessonId?: string;
  /** Shown beside the question counter (the lesson's «tema» label). */
  note?: string | null;
}) {
  const { t } = useTranslation();
  const { data: courseTree } = useCourseTree();
  const [size, setSize] = useState<Size>("twenty");
  const [round, setRound] = useState<{ number: number; questions: DrawnRound["questions"] } | null>(null);
  const [index, setIndex] = useState(0);
  const [answered, setAnswered] = useState(false);
  const [done, setDone] = useState(false);

  const drawRound = useMutation({
    mutationFn: () => draw(total !== undefined && size === "all"),
    meta: { silentSuccess: true },
    onSuccess: (drawn) => {
      setRound((previous) => ({ number: (previous?.number ?? 0) + 1, questions: drawn.questions }));
      setIndex(0);
      setAnswered(false);
      setDone(false);
    },
  });

  const intro = courseTree?.course.practiceScheduler === "spaced" ? t("practice.introSpaced") : t("practice.intro");
  const last = round !== null && index === round.questions.length - 1;
  const next = () => {
    if (last) setDone(true);
    else {
      setIndex((i) => i + 1);
      setAnswered(false);
    }
  };

  return (
    <>
      {(round === null || done) && (
        <Card className="space-y-4 p-4">
          {done && <p className="font-medium">{t("practice.done")}</p>}
          <p className="text-sm text-gray-600 dark:text-gray-300">{lead ? `${lead} ${intro}` : intro}</p>
          {total !== undefined && (
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
          )}
          <Button
            className="w-full sm:w-auto"
            disabled={drawRound.isPending || total === 0}
            onClick={() => drawRound.mutate()}
          >
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
            {note && <span className="ml-2">· {note}</span>}
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
    </>
  );
}
