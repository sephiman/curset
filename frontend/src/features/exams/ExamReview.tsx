import { Link, useParams } from "react-router-dom";
import { useQuery } from "@tanstack/react-query";
import { useTranslation } from "react-i18next";
import type { TFunction } from "i18next";
import type { ExerciseType } from "@/api/course";
import { reviewExam, type ExamQuestion, type ExamResult, type ExamSession, type NotGraded } from "@/api/exams";
import { Badge, Card, Spinner } from "@/components/ui/primitives";
import { ChartExercise } from "@/features/exercises/ChartExercise";
import { cn } from "@/lib/cn";
import { Prose } from "@/lib/markdown";
import { scopeKey, useCourse } from "@/features/courses/CourseContext";
import { ProseReferenceHost } from "@/features/references/ProseReferenceHost";
import { ByLessonTable } from "@/features/byLesson/ByLessonTable";
import { LessonLink } from "@/features/exercises/LessonLink";
import { SolutionPanel } from "@/features/exercises/SolutionPanel";
import { useCourseTree } from "@/features/course/queries";
import { clock, scoreNumber, sittingName } from "@/features/exams/format";

const CHART_TYPES: ReadonlySet<ExerciseType> = new Set(["synthetic_chart", "fixture_chart", "pattern_chart"]);

function pct(score: number | null): string {
  return score == null ? "—" : `${Math.round(score * 100)}%`;
}

/** Best-effort readable rendering of the learner's own answer, using the question payload. */
function answerText(q: ExamQuestion, t: TFunction, letters?: boolean): string {
  const a = q.givenAnswer;
  if (!a) return t("exam.unanswered");
  const opts = q.payload.options ?? [];
  const text = (id: string): string => {
    const idx = opts.findIndex((x) => x.id === id);
    if (idx < 0) return id;
    const o = opts[idx];
    const val = String(o.text ?? o.value ?? id);
    return letters ? `${String.fromCharCode(65 + idx)}) ${val}` : val;
  };
  if ("optionId" in a) return text(a.optionId);
  if ("optionIds" in a) return a.optionIds.map(text).join(", ");
  if ("value" in a) return a.value ? t("exercise.true") : t("exercise.false");
  if ("order" in a) {
    const items = q.payload.items ?? [];
    return a.order.map((id) => String(items.find((i) => i.id === id)?.text ?? id)).join(" → ");
  }
  if ("pairs" in a) {
    const lefts = q.payload.lefts ?? [];
    const rights = q.payload.rights ?? [];
    return Object.entries(a.pairs)
      .map(([l, r]) => `${lefts.find((x) => x.id === l)?.text ?? l} → ${rights.find((x) => x.id === r)?.text ?? r}`)
      .join("; ");
  }
  if ("divergence" in a) return t(`divergence.${a.divergence}`);
  if ("label" in a) return t(`chartLabel.${a.label}`);
  return "";
}

function StatusBadge({ q, t }: { q: ExamQuestion; t: TFunction }) {
  if (q.unanswered) return <Badge tone="neutral">{t("exam.unanswered")}</Badge>;
  return q.isCorrect ? (
    <Badge tone="green">{t("exercise.correct")}</Badge>
  ) : (
    <Badge tone="red">{t("exercise.incorrect")}</Badge>
  );
}

const NOT_GRADED: Record<NotGraded, string> = {
  "no-case-marked": "exam.notGradedNoCase",
  "several-cases-marked": "exam.notGradedSeveralCases",
  "previous-part-not-passed": "exam.notGradedPreviousPart",
};

/** Raw and transformed per part and in total — and nothing else about cut-offs. */
function PartScores({ exam, result }: { exam: ExamSession; result: ExamResult }) {
  const { t, i18n } = useTranslation();
  const lang = i18n.resolvedLanguage;
  const titles = new Map(exam.parts.map((part) => [part.id, part.title ?? part.id]));
  const caseTitles = new Map(exam.parts.flatMap((part) => part.cases.map((c) => [c.exerciseId, c.title])));
  const number = (value: number | undefined) => (value == null ? "—" : scoreNumber(value, lang));
  const hasTimes = (result.parts ?? []).some((p) => p.activeSeconds != null) || result.totalActiveSeconds != null;
  return (
    <div className="overflow-x-auto">
      <table className="w-full text-sm">
        <thead className="border-b border-gray-300 text-gray-500 dark:border-gray-700 dark:text-gray-400">
          <tr>
            <th className="py-2 pr-3 text-left" />
            <th className="py-2 pr-3 text-right">{t("exam.raw")}</th>
            <th className="py-2 pr-3 text-right">{t("exam.transformed")}</th>
            {hasTimes && <th className="py-2 text-right">{t("exam.activeTime")}</th>}
          </tr>
        </thead>
        <tbody className="divide-y divide-border dark:divide-gray-800">
          {(result.parts ?? []).map((part) => (
            <tr key={part.id}>
              <td className="py-2 pr-3">
                <p className="font-medium">{titles.get(part.id)}</p>
                {part.graded ? (
                  <p className="text-xs text-gray-500 dark:text-gray-400">
                    {t("exam.partTally", { correct: part.correct, wrong: part.wrong, blank: part.blank })}
                    {part.case && ` · ${t("exam.caseChosen", { title: caseTitles.get(part.case) ?? part.case })}`}
                  </p>
                ) : (
                  <p className="text-xs text-gray-500 dark:text-gray-400">
                    {t("exam.partNotGraded")}: {t(NOT_GRADED[part.reason ?? "no-case-marked"])}
                  </p>
                )}
              </td>
              <td className="py-2 pr-3 text-right tabular-nums">{part.graded ? number(part.raw) : "—"}</td>
              <td className="py-2 pr-3 text-right tabular-nums">
                {part.graded && part.transformed != null ? `${number(part.transformed)} / ${number(part.max)}` : "—"}
              </td>
              {hasTimes && (
                <td className="py-2 text-right font-mono text-xs text-gray-500 tabular-nums dark:text-gray-400">
                  {part.activeSeconds != null ? clock(part.activeSeconds * 1000) : "—"}
                </td>
              )}
            </tr>
          ))}
          <tr className="font-semibold">
            <td className="py-2 pr-3">{t("exam.total")}</td>
            <td className="py-2 pr-3 text-right tabular-nums">{number(result.raw)}</td>
            <td className="py-2 pr-3 text-right tabular-nums">
              {result.transformed != null ? `${number(result.transformed)} / ${number(result.max ?? undefined)}` : "—"}
            </td>
            {hasTimes && (
              <td className="py-2 text-right font-mono text-xs tabular-nums text-gray-900 dark:text-gray-100">
                {result.totalActiveSeconds != null ? clock(result.totalActiveSeconds * 1000) : "—"}
              </td>
            )}
          </tr>
        </tbody>
      </table>
    </div>
  );
}

export function ExamReview() {
  const { t, i18n } = useTranslation();
  const lang = i18n.resolvedLanguage;
  const { examId = "" } = useParams();
  const { scope, path } = useCourse();
  const { data: course } = useCourseTree();
  const noun = course?.course.lessonNoun;
  const letters = course?.course.optionLabels === "letters";

  const { data: exam, isLoading, isError } = useQuery({
    queryKey: ["exam", ...scopeKey(scope), examId, "review"],
    queryFn: () => reviewExam(scope, examId),
    retry: false,
  });

  if (isLoading) {
    return (
      <div className="flex justify-center py-16 text-gray-500">
        <Spinner />
      </div>
    );
  }
  if (isError || !exam || !exam.result) {
    return (
      <div className="py-16 text-center text-gray-500">
        <p>{t("exam.notFound")}</p>
        <Link to={path("/exams")} className="text-sm text-primary hover:underline">
          ← {t("nav.exams")}
        </Link>
      </div>
    );
  }

  const r = exam.result;
  const scored = r.parts !== undefined;
  const caseTitles = new Map(exam.parts.flatMap((part) => part.cases.map((c) => [c.exerciseId, c.title])));
  const graded = new Set((r.parts ?? []).filter((p) => p.graded).map((p) => p.case).filter(Boolean));

  return (
    <ProseReferenceHost>
    <div className="mx-auto max-w-2xl space-y-6">
      <div>
        <Link to={path("/exams")} className="text-sm text-primary hover:underline">
          ← {t("nav.exams")}
        </Link>
        <h1 className="mt-2 text-2xl font-bold">{sittingName(exam)}</h1>
        <p className="mt-1 text-sm text-gray-500 dark:text-gray-400">
          {exam.finishedAt ? new Date(exam.finishedAt).toLocaleDateString(lang) : ""}
        </p>
      </div>

      {r.autoSubmitted && (
        <p role="status" className="rounded-md bg-amber-50 p-3 text-sm text-amber-900 dark:bg-amber-950/50 dark:text-amber-100">
          {t("exam.autoSubmittedNotice")}
        </p>
      )}

      {/* Score — plain, honest numbers. No pass/fail, no badges/confetti. */}
      {scored && (
        <Card className="p-4">
          <PartScores exam={exam} result={r} />
        </Card>
      )}
      {!scored && (
      <Card className="p-4">
        <div className="flex items-baseline gap-3">
          <span className="text-3xl font-bold tabular-nums">{pct(r.score)}</span>
          <span className="text-sm text-gray-500 dark:text-gray-400">
            {t("exam.scoreLine", { correct: r.correct, total: r.total })}
          </span>
        </div>

        {r.blocks.length > 1 && (
          <div className="mt-4 space-y-1">
            <p className="text-xs font-semibold tracking-wide text-gray-500 uppercase dark:text-gray-400">
              {t("exam.byBlock")}
            </p>
            {r.blocks.map((b) => (
              <div key={b.blockId} className="flex items-center justify-between text-sm">
                <span className="text-gray-600 dark:text-gray-300">{b.title}</span>
                <span className="tabular-nums text-gray-500 dark:text-gray-400">
                  {pct(b.score)} <span className="text-xs">({b.correct}/{b.total})</span>
                </span>
              </div>
            ))}
          </div>
        )}

        <div className="mt-4 space-y-1">
          <p className="text-xs font-semibold tracking-wide text-gray-500 uppercase dark:text-gray-400">
            {t("exam.byModule")}
          </p>
          {r.modules.map((m) => (
            <div key={m.moduleId} className="flex items-center gap-2 text-sm">
              <span
                aria-hidden
                className={cn(
                  "inline-flex h-4 w-4 shrink-0 items-center justify-center rounded-full text-[10px] font-bold",
                  m.unanswered
                    ? "bg-gray-200 text-gray-500 dark:bg-gray-700 dark:text-gray-400"
                    : m.correct
                      ? "bg-emerald-100 text-emerald-700 dark:bg-emerald-950/50 dark:text-emerald-300"
                      : "bg-red-100 text-red-700 dark:bg-red-950/50 dark:text-red-300",
                )}
              >
                {m.unanswered ? "◦" : m.correct ? "✓" : "✗"}
              </span>
              <span className="text-gray-600 dark:text-gray-300">{m.title}</span>
            </div>
          ))}
        </div>
      </Card>
      )}

      {exam.byLesson && (
        <Card className="p-4">
          <ByLessonTable table={exam.byLesson} noun={noun} />
        </Card>
      )}

      {/* Per-question review — your answer, the correct answer, and the worked solution, in bulk. */}
      <div className="space-y-4">
        {exam.questions.map((q) => {
          const result = {
            attemptId: q.attemptId,
            correct: !!q.isCorrect,
            correctAnswer: q.correctAnswer,
            solutionSteps: q.solutionSteps,
            explanation: q.explanation,
          };
          return (
            <Card key={q.attemptId} className="p-4">
              <div className="flex items-center justify-between gap-2">
                <p className="text-xs text-gray-400">
                  <span className="font-mono">{q.moduleId.toUpperCase()}</span> · {q.moduleTitle}
                  {q.timeSeconds != null && (
                    <span className="ml-2 font-mono tabular-nums text-gray-500 dark:text-gray-400">
                      ({clock(q.timeSeconds * 1000)})
                    </span>
                  )}
                </p>
                <StatusBadge q={q} t={t} />
              </div>
              {(q.questionId || q.reserve) && (
                <p className="mt-1 text-xs text-gray-500 dark:text-gray-400">
                  {q.questionId &&
                    `${caseTitles.get(q.exerciseId) ?? q.exerciseId}${graded.has(q.exerciseId) ? "" : ` · ${t("exam.caseNotChosen")}`}`}
                  {q.reserve && t("exam.reserve")}
                </p>
              )}
              <div className="mt-2">
                <Prose markdown={q.prompt} />
              </div>
              {CHART_TYPES.has(q.type) && q.lessonId && (
                <div className="mt-2 flex flex-wrap items-start gap-3">
                  <LessonLink lessonId={q.lessonId} anchor={q.lessonAnchor} citation={q.citation} />
                </div>
              )}
              <p className="mt-2 text-sm text-gray-600 dark:text-gray-300">
                <span className="font-medium">{t("exam.yourAnswer")}:</span>{" "}
                <span className={cn(q.unanswered && "text-gray-400 italic dark:text-gray-500")}>
                  {answerText(q, t, letters)}
                </span>
              </p>
              {CHART_TYPES.has(q.type) ? (
                <ChartExercise type={q.type} payload={q.payload} result={result} hideVerdict={!!q.unanswered} />
              ) : (
                <SolutionPanel
                  attemptId={q.attemptId}
                  correct={result.correct}
                  correctAnswer={result.correctAnswer}
                  solutionSteps={result.solutionSteps}
                  explanation={result.explanation}
                  options={q.payload.options}
                  excerpt={q.excerpt}
                  noExcerpt={q.noExcerpt}
                  lessonLink={q.lessonId ? { lessonId: q.lessonId, anchor: q.lessonAnchor, citation: q.citation } : null}
                  reportable={q.type === "quiz" || q.type === "case"}
                  hideVerdict={!!q.unanswered}
                />
              )}
            </Card>
          );
        })}
      </div>
    </div>
    </ProseReferenceHost>
  );
}
