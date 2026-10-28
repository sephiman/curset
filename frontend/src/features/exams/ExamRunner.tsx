import { useEffect, useMemo, useRef, useState } from "react";
import { useNavigate, useParams } from "react-router-dom";
import { useMutation, useQuery, useQueryClient } from "@tanstack/react-query";
import { useTranslation } from "react-i18next";
import type { ExerciseType } from "@/api/course";
import type { Answer } from "@/api/exercises";
import { abandonExam, answerExamQuestion, getExam, markExamCases, submitExam, type ExamCase } from "@/api/exams";
import { Button, Card, Spinner } from "@/components/ui/primitives";
import { CalculationExercise } from "@/features/exercises/CalculationExercise";
import { ChartExercise } from "@/features/exercises/ChartExercise";
import { QuizExercise } from "@/features/exercises/QuizExercise";
import { CaseScenario } from "@/features/exercises/CaseScenario";
import { cn } from "@/lib/cn";
import { Prose } from "@/lib/markdown";
import { scopeKey, useCourse } from "@/features/courses/CourseContext";
import { ProseReferenceHost } from "@/features/references/ProseReferenceHost";
import { clock, sittingName } from "@/features/exams/format";

const CHART_TYPES: ReadonlySet<ExerciseType> = new Set(["synthetic_chart", "fixture_chart", "pattern_chart"]);

/** Milliseconds left on the server's clock, ticking; null for an untimed sitting. */
function useTimeLeft(deadline: string | null | undefined, serverNow: string | undefined): number | null {
  // The device clock may be off; the server said what time it was when it answered, so count from that.
  const skew = useMemo(() => (serverNow ? Date.parse(serverNow) - Date.now() : 0), [serverNow]);
  const [now, setNow] = useState(() => Date.now());
  useEffect(() => {
    if (!deadline) return;
    const tick = window.setInterval(() => setNow(Date.now()), 1000);
    return () => window.clearInterval(tick);
  }, [deadline]);
  return deadline ? Date.parse(deadline) - (now + skew) : null;
}

export function ExamRunner() {
  const { t } = useTranslation();
  const { examId = "" } = useParams();
  const navigate = useNavigate();
  const qc = useQueryClient();
  const { scope, path } = useCourse();

  const { data: exam, isLoading, isError } = useQuery({
    queryKey: ["exam", ...scopeKey(scope), examId],
    queryFn: () => getExam(scope, examId),
    retry: false,
  });

  const [answers, setAnswers] = useState<Record<string, Answer>>({});
  const [marks, setMarks] = useState<Record<string, string[]>>({});
  const [current, setCurrent] = useState(0);
  const seeded = useRef(false);

  useEffect(() => {
    if (exam && !seeded.current) {
      seeded.current = true;
      const seed: Record<string, Answer> = {};
      for (const q of exam.questions) if (q.givenAnswer) seed[q.attemptId] = q.givenAnswer;
      setAnswers(seed);
      setMarks(Object.fromEntries(exam.parts.map((part) => [part.id, part.marked])));
    }
  }, [exam]);

  // A closed/unknown session can't be run — send the learner back to the landing.
  useEffect(() => {
    if (isError) navigate(path("/exams"), { replace: true });
  }, [isError, navigate]);

  const answerMut = useMutation({
    mutationFn: ({ attemptId, answer }: { attemptId: string; answer: Answer }) =>
      answerExamQuestion(scope, examId, attemptId, answer),
    meta: { silentSuccess: true },
  });
  const markMut = useMutation({
    mutationFn: ({ partId, exerciseIds }: { partId: string; exerciseIds: string[] }) =>
      markExamCases(scope, examId, partId, exerciseIds),
    meta: { silentSuccess: true },
  });
  // Every exam query but this runner's own: still mounted, it would refetch a sitting the server now
  // refuses as no longer in progress, and say so in a toast over the next page.
  const refreshOtherExamQueries = () =>
    void qc.invalidateQueries({ queryKey: ["exam", scope.slug], predicate: (query) => query.queryKey.at(-1) !== examId });
  // Answers and case marks still on their way to the server. Handing in waits for them: sent first, the
  // hand-in closed the sitting under them, the server refused the late save and the answer counted blank.
  const saving = useRef(new Set<Promise<unknown>>());
  const handingIn = useRef(false);
  const track = (save: Promise<unknown>) => {
    const settled = save.catch(() => undefined);
    saving.current.add(settled);
    void settled.finally(() => saving.current.delete(settled));
  };
  const submit = useMutation({
    mutationFn: async () => {
      await Promise.all(saving.current);
      return submitExam(scope, examId);
    },
    onError: () => {
      handingIn.current = false;
    },
    onSuccess: () => {
      refreshOtherExamQueries();
      navigate(path(`/exams/${examId}/review`), { replace: true });
    },
  });
  // Set before the hand-in is queued, so no answer chosen after the click is sent behind it.
  const handIn = () => {
    handingIn.current = true;
    submit.mutate();
  };
  const abandon = useMutation({
    mutationFn: () => abandonExam(scope, examId),
    onSuccess: () => {
      refreshOtherExamQueries();
      navigate(path("/exams"), { replace: true });
    },
  });

  const timeLeft = useTimeLeft(exam?.deadline, exam?.serverNow);
  const timeUp = timeLeft !== null && timeLeft <= 0;
  const submittedOnTime = useRef(false);
  useEffect(() => {
    // The clock ran out: the sitting is handed in with what was answered, once.
    if (timeUp && !submittedOnTime.current && !submit.isPending) {
      submittedOnTime.current = true;
      handIn();
    }
  }, [timeUp, submit]);

  if (isLoading || !exam) {
    return (
      <div className="flex justify-center py-16 text-gray-500">
        <Spinner />
      </div>
    );
  }

  const questions = exam.questions;
  const q = questions[current];
  const counted = questions.filter((x) => !x.reserve);
  const answeredCount = counted.filter((x) => answers[x.attemptId] !== undefined).length;
  const unanswered = counted.length - answeredCount;
  const casesById = new Map<string, ExamCase>(exam.parts.flatMap((part) => part.cases.map((c) => [c.exerciseId, c])));
  const caseOf = q.questionId ? casesById.get(q.exerciseId) : undefined;
  const part = exam.parts.find((p) => p.id === q.partId);
  const multiPart = exam.parts.length > 1;

  const setAnswer = (attemptId: string, a: Answer) => {
    if (handingIn.current) return;
    setAnswers((prev) => ({ ...prev, [attemptId]: a }));
    track(answerMut.mutateAsync({ attemptId, answer: a }));
  };
  const toggleMark = (partId: string, exerciseId: string, on: boolean) => {
    const before = marks[partId] ?? [];
    const next = on ? [...before, exerciseId] : before.filter((id) => id !== exerciseId);
    if (handingIn.current) return;
    setMarks((prev) => ({ ...prev, [partId]: next }));
    track(markMut.mutateAsync({ partId, exerciseIds: next }));
  };

  const onSubmit = () => {
    const msg = unanswered > 0 ? t("exam.submitConfirmUnanswered", { count: unanswered }) : t("exam.submitConfirm");
    if (window.confirm(msg)) handIn();
  };
  const onAbandon = () => {
    if (window.confirm(t("exam.abandonConfirm"))) abandon.mutate();
  };

  const deferred = { value: answers[q.attemptId] ?? null, onChange: (a: Answer) => setAnswer(q.attemptId, a) };

  return (
    <ProseReferenceHost>
      <div className="mx-auto max-w-2xl space-y-4">
        <div className="flex flex-wrap items-center justify-between gap-2">
          <h1 className="text-lg font-semibold">{sittingName(exam)}</h1>
          <div className="flex items-center gap-3 text-sm text-gray-500 dark:text-gray-400">
            {timeLeft !== null && (
              <span role="timer" aria-live="off" className={cn("font-mono tabular-nums", timeLeft < 5 * 60_000 && "text-red-600")}>
                {t("exam.timeLeft", { time: clock(timeLeft) })}
              </span>
            )}
            <span>{t("exam.answeredOf", { done: answeredCount, total: counted.length })}</span>
          </div>
        </div>
        {timeUp && (
          <p role="status" className="rounded-md bg-amber-50 p-3 text-sm text-amber-900 dark:bg-amber-950/50 dark:text-amber-100">
            {t("exam.timeUp")}
          </p>
        )}

        {/* Progress strip — tappable markers grouped by part; answered filled, current ringed, reserves marked. */}
        {exam.parts.map((p) => {
          const inPart = questions.filter((x) => x.partId === p.id);
          return (
            <div key={p.id} className="space-y-1">
              {multiPart && <p className="text-xs font-medium text-gray-500 dark:text-gray-400">{p.title ?? p.id}</p>}
              <div className="flex flex-wrap gap-1.5">
                {inPart.map((x) => {
                  const isAnswered = answers[x.attemptId] !== undefined;
                  const number = x.index + 1;
                  return (
                    <button
                      key={x.attemptId}
                      type="button"
                      aria-label={x.reserve ? `${number} · ${t("exam.reserve")}` : `${number}`}
                      aria-current={x.index === current}
                      onClick={() => setCurrent(x.index)}
                      className={cn(
                        "h-8 min-w-8 rounded-md border px-1 text-xs font-medium tabular-nums transition-colors",
                        x.index === current &&
                          "ring-2 ring-primary ring-offset-1 dark:ring-offset-gray-900 oled:ring-offset-oled-bg",
                        x.reserve && "border-dashed",
                        isAnswered
                          ? "border-primary bg-primary text-primary-foreground"
                          : "border-border text-gray-600 hover:border-primary/60 dark:border-gray-700 dark:text-gray-300",
                      )}
                    >
                      {x.reserve ? `R${number}` : number}
                    </button>
                  );
                })}
              </div>
            </div>
          );
        })}

        {caseOf && part && (
          <CaseScenario
            title={caseOf.title}
            scenario={caseOf.scenario}
            choice={{
              label: t("exam.markCase"),
              rule: t("exam.chooseCaseRule"),
              checked: (marks[part.id] ?? []).includes(caseOf.exerciseId),
              onChange: (on) => toggleMark(part.id, caseOf.exerciseId, on),
            }}
          />
        )}

        <Card className="p-4">
          <p className="text-xs text-gray-400">
            <span className="font-mono">{q.moduleId.toUpperCase()}</span> · {q.moduleTitle}
            {q.reserve && <span className="ml-2 font-medium text-amber-700 dark:text-amber-300">{t("exam.reserve")}</span>}
          </p>
          {q.reserve && <p className="mt-1 text-xs text-gray-500 dark:text-gray-400">{t("exam.reserveHint")}</p>}
          <div className="mt-2">
            <Prose markdown={q.prompt} />
          </div>
          {CHART_TYPES.has(q.type) ? (
            <ChartExercise key={q.attemptId} type={q.type} payload={q.payload} result={null} deferred={deferred} />
          ) : q.type === "quiz" || q.type === "case" ? (
            <QuizExercise key={q.attemptId} payload={q.payload} deferred={deferred} />
          ) : (
            <CalculationExercise
              key={q.attemptId}
              options={q.payload.options ?? []}
              unit={q.payload.unit}
              formula={q.payload.formula}
              deferred={deferred}
            />
          )}
        </Card>

        <div className="flex items-center justify-between gap-2">
          <Button variant="secondary" disabled={current === 0} onClick={() => setCurrent((i) => i - 1)}>
            ← {t("exam.prev")}
          </Button>
          {current < questions.length - 1 ? (
            <Button variant="secondary" onClick={() => setCurrent((i) => i + 1)}>
              {t("exam.next")} →
            </Button>
          ) : (
            <Button disabled={submit.isPending} onClick={onSubmit}>
              {t("exam.submit")}
            </Button>
          )}
        </div>

        <div className="flex items-center justify-between gap-2 border-t border-border pt-4 dark:border-gray-800 oled:border-oled-line">
          <button type="button" onClick={onAbandon} className="text-xs text-gray-400 hover:text-red-600 dark:text-gray-500">
            {t("exam.abandon")}
          </button>
          <Button variant="ghost" disabled={submit.isPending} onClick={onSubmit}>
            {t("exam.submit")}
          </Button>
        </div>
      </div>
    </ProseReferenceHost>
  );
}
