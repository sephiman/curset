import { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import { useMutation } from "@tanstack/react-query";
import { useTranslation } from "react-i18next";
import { drawPsicotecnicoRound } from "@/api/practice";
import { Button, Card } from "@/components/ui/primitives";
import { useCourse } from "@/features/courses/CourseContext";
import { useCourseTree } from "@/features/course/queries";
import { PsicotecnicoQuestion } from "@/features/practice/PsicotecnicoQuestion";
import { clock } from "@/features/exams/format";
import { cn } from "@/lib/cn";

const COUNTS = [10, 20, 40] as const;
/** Seconds a timed round allows per item: the official exam gives about 49 for a question. */
const SECONDS_PER_ITEM = 50;
const ALL = "all";

interface Round {
  number: number;
  exerciseIds: string[];
  timed: boolean;
}

/**
 * Generated psicotécnicos, one at a time: every type in the exam's weights or one type, with or without a clock.
 * Every answer is an ordinary practice attempt, so Progress counts it per type.
 */
export function PsicotecnicoPracticePage() {
  const { t } = useTranslation();
  const { scope, path } = useCourse();
  const { data: course } = useCourseTree();
  const types = course?.course.psicotecnicos ?? [];
  const [kind, setKind] = useState<string>(ALL);
  const [count, setCount] = useState<number>(20);
  const [timed, setTimed] = useState(false);
  const [round, setRound] = useState<Round | null>(null);
  const [index, setIndex] = useState(0);
  const [answered, setAnswered] = useState(false);
  const [correct, setCorrect] = useState(0);
  const [done, setDone] = useState(false);
  const [elapsed, setElapsed] = useState(0);

  const draw = useMutation({
    mutationFn: () => drawPsicotecnicoRound(scope, count, kind === ALL ? undefined : kind),
    meta: { silentSuccess: true },
    onSuccess: (drawn) => {
      setRound((previous) => ({ number: (previous?.number ?? 0) + 1, exerciseIds: drawn.exerciseIds, timed }));
      setIndex(0);
      setAnswered(false);
      setCorrect(0);
      setElapsed(0);
      setDone(false);
    },
  });

  const limit = round?.timed ? round.exerciseIds.length * SECONDS_PER_ITEM : null;
  const running = round !== null && !done;
  useEffect(() => {
    if (!running) return;
    const timer = window.setInterval(() => setElapsed((seconds) => seconds + 1), 1000);
    return () => window.clearInterval(timer);
  }, [running, round?.number]);
  useEffect(() => {
    if (limit !== null && elapsed >= limit) setDone(true);
  }, [elapsed, limit]);

  const last = round !== null && index === round.exerciseIds.length - 1;
  const next = () => {
    if (last) setDone(true);
    else {
      setIndex((i) => i + 1);
      setAnswered(false);
    }
  };

  return (
    <div className="mx-auto max-w-3xl space-y-4">
      <div>
        <Link to={path("")} className="text-sm text-primary hover:underline">
          ← {t("psicotecnicos.back")}
        </Link>
        <h1 className="mt-2 text-xl font-bold">{t("psicotecnicos.title")}</h1>
      </div>

      {(round === null || done) && (
        <Card className="space-y-4 p-4">
          {done && round && (
            <p className="font-medium" role="status">
              {t("psicotecnicos.result", { correct, total: round.exerciseIds.length })}
              {" · "}
              {clock(elapsed * 1000)}
            </p>
          )}
          <p className="text-sm text-gray-600 dark:text-gray-300">{t("psicotecnicos.intro")}</p>
          <label className="block text-sm">
            <span className="mb-1 block text-xs text-gray-500 dark:text-gray-400">{t("psicotecnicos.type")}</span>
            <select
              value={kind}
              onChange={(event) => setKind(event.target.value)}
              className="min-h-11 w-full rounded-md border border-border bg-transparent px-3 dark:border-gray-700"
            >
              <option value={ALL}>{t("psicotecnicos.allTypes")}</option>
              {types.map((type) => (
                <option key={type.generator} value={type.generator}>
                  {type.title}
                </option>
              ))}
            </select>
          </label>
          <fieldset>
            <legend className="mb-2 text-xs text-gray-500 dark:text-gray-400">{t("psicotecnicos.count")}</legend>
            <div role="radiogroup" className="grid grid-cols-3 gap-2">
              {COUNTS.map((choice) => (
                <label
                  key={choice}
                  className={cn(
                    "flex min-h-11 cursor-pointer items-center justify-center rounded-md border px-3 py-2 text-sm font-medium",
                    count === choice
                      ? "border-primary bg-primary/10 text-primary"
                      : "border-border text-gray-700 dark:border-gray-700 dark:text-gray-200",
                  )}
                >
                  <input
                    type="radio"
                    name="psicotecnico-count"
                    className="sr-only"
                    checked={count === choice}
                    onChange={() => setCount(choice)}
                  />
                  {choice}
                </label>
              ))}
            </div>
          </fieldset>
          <label className="flex min-h-11 items-center gap-2 text-sm">
            <input type="checkbox" checked={timed} onChange={(event) => setTimed(event.target.checked)} />
            {t("psicotecnicos.timed", { seconds: SECONDS_PER_ITEM })}
          </label>
          <Button className="w-full sm:w-auto" disabled={draw.isPending || types.length === 0} onClick={() => draw.mutate()}>
            {done ? t("practice.again") : t("practice.begin")}
          </Button>
        </Card>
      )}

      {round !== null && !done && (
        <Card className="p-4">
          <p className="mb-3 flex flex-wrap items-center justify-between gap-2 text-xs text-gray-500 dark:text-gray-400">
            <span className="font-medium text-gray-700 dark:text-gray-300">
              {t("practice.progress", { number: index + 1, total: round.exerciseIds.length })}
            </span>
            <span className="font-mono tabular-nums" aria-label={t("psicotecnicos.clock")}>
              {limit !== null ? `${clock(Math.max(0, limit - elapsed) * 1000)} / ${clock(limit * 1000)}` : clock(elapsed * 1000)}
            </span>
          </p>
          <PsicotecnicoQuestion
            key={`${round.number}-${index}`}
            round={round.number}
            position={index}
            exerciseId={round.exerciseIds[index]}
            onAnswered={(wasCorrect) => {
              setAnswered(true);
              if (wasCorrect) setCorrect((n) => n + 1);
            }}
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
