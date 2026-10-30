import { useState } from "react";
import { useMutation } from "@tanstack/react-query";
import { useTranslation } from "react-i18next";
import { answerAttempt, openCase, type Answer, type CaseInstance, type GradeResponse } from "@/api/exercises";
import { Badge, Button, Card } from "@/components/ui/primitives";
import { CaseScenario } from "@/features/exercises/CaseScenario";
import { QuizExercise } from "@/features/exercises/QuizExercise";
import { SolutionPanel } from "@/features/exercises/SolutionPanel";
import { useCourse } from "@/features/courses/CourseContext";
import { useCourseTree } from "@/features/course/queries";
import { Prose } from "@/lib/markdown";
import { cn } from "@/lib/cn";
import { findTemaInfo } from "@/lib/tema";

/**
 * A case in practice: the scenario stays in view while its questions are answered in order, each one
 * submitted and graded on its own as any question is. The case is done when every question is.
 */
export function CaseExercise({ exerciseId, highlighted = false }: { exerciseId: string; highlighted?: boolean }) {
  const { t } = useTranslation();
  const { scope } = useCourse();
  const { data: courseTree } = useCourseTree();
  const [opened, setOpened] = useState<CaseInstance | null>(null);
  const [results, setResults] = useState<Record<string, GradeResponse>>({});

  const start = useMutation({
    mutationFn: () => openCase(scope, exerciseId),
    meta: { silentSuccess: true },
    onSuccess: (instance) => {
      setResults({});
      setOpened(instance);
    },
  });
  const answer = useMutation({
    mutationFn: ({ attemptId, value }: { attemptId: string; value: Answer }) => answerAttempt(scope, attemptId, value),
    meta: { silentSuccess: true },
    onSuccess: (graded) => setResults((before) => ({ ...before, [graded.attemptId]: graded })),
  });

  const total = opened?.questions.length ?? 0;
  const done = Object.keys(results).length;

  return (
    <Card id={`ex-${exerciseId}`} className={cn("my-4 scroll-mt-4 p-4", highlighted && "ring-2 ring-primary")}>
      <div className="flex items-center justify-between">
        <span className="font-mono text-xs text-gray-400">{exerciseId}</span>
        <Badge tone="indigo">{t("exerciseType.case")}</Badge>
      </div>
      {!opened ? (
        <div className="mt-3">
          <Button onClick={() => start.mutate()} disabled={start.isPending}>
            {t("exercise.startCase")}
          </Button>
        </div>
      ) : (
        <div className="mt-3 space-y-4">
          <CaseScenario title={opened.title} scenario={opened.scenario} />
          <p role="status" className="text-xs text-gray-500 dark:text-gray-400">
            {done === total ? t("exercise.caseDone") : t("exercise.caseProgress", { done, total })}
          </p>
          <ol className="space-y-4">
            {opened.questions.map((question, index) => {
              const result = results[question.attemptId];
              const qTema = findTemaInfo(courseTree, question.lessonId);
              return (
                <li key={question.attemptId} className="rounded-md border border-border p-3 dark:border-gray-800 oled:border-oled-line">
                  <p className="text-xs font-medium text-gray-500 dark:text-gray-400">
                    <span>{t("practice.progress", { number: index + 1, total })}</span>
                    {qTema && <span className="ml-2 font-normal text-gray-400">· {qTema.temaLabel}</span>}
                  </p>
                  <Prose markdown={question.prompt} />
                  {!result ? (
                    <QuizExercise
                      payload={question.payload}
                      pending={answer.isPending && answer.variables?.attemptId === question.attemptId}
                      onSubmit={(value) => answer.mutate({ attemptId: question.attemptId, value })}
                    />
                  ) : (
                    <SolutionPanel
                      attemptId={question.attemptId}
                      questionId={question.questionId}
                      lessonId={question.lessonId}
                      correct={result.correct}
                      correctAnswer={result.correctAnswer}
                      solutionSteps={result.solutionSteps}
                      explanation={result.explanation}
                      options={question.payload.options}
                      excerpt={result.excerpt}
                      noExcerpt={result.noExcerpt}
                      lessonLink={result.lessonLink}
                      reportable
                    />
                  )}
                </li>
              );
            })}
          </ol>
          {done === total && (
            <Button variant="secondary" onClick={() => start.mutate()} disabled={start.isPending}>
              {t("exercise.tryAgain")}
            </Button>
          )}
        </div>
      )}
    </Card>
  );
}
