import { useState } from "react";
import { useMutation, useQuery, useQueryClient } from "@tanstack/react-query";
import { answerAttempt, createAttempt, type Answer, type GradeResponse } from "@/api/exercises";
import type { PracticeQuestion as Question } from "@/api/practice";
import { Spinner } from "@/components/ui/primitives";
import { scopeKey, useCourse } from "@/features/courses/CourseContext";
import { QuizExercise } from "@/features/exercises/QuizExercise";
import { SolutionPanel } from "@/features/exercises/SolutionPanel";
import { Prose } from "@/lib/markdown";

/** One question of a round: opened as a practice attempt on that question, graded on answer. */
export function PracticeQuestion({
  round,
  position,
  question,
  lessonId,
  onAnswered,
}: {
  /** Distinguishes two rounds that happen to serve the same question at the same position. */
  round: number;
  /** Where the question sits in the round: two generated questions share an empty question id. */
  position: number;
  question: Question;
  /** The lesson the round practises; absent in a round that crosses lessons. */
  lessonId?: string;
  onAnswered: () => void;
}) {
  const { scope } = useCourse();
  // A generated question has no stored id: the seed is the question, so there is nothing to report or link.
  const generated = question.questionId === "";
  const queryClient = useQueryClient();
  const [result, setResult] = useState<GradeResponse | null>(null);
  // A query, not an effect: opening is a write, and the query runs it once per question however often
  // the component mounts.
  const { data: attempt } = useQuery({
    queryKey: ["practice-attempt", ...scopeKey(scope), round, position, question.questionId],
    queryFn: () => createAttempt(scope, question.exerciseId, question.questionId || undefined),
    staleTime: Infinity,
    gcTime: 0,
    retry: false,
  });
  const answer = useMutation({
    mutationFn: (a: Answer) => answerAttempt(scope, attempt!.attemptId, a),
    meta: { silentSuccess: true },
    onSuccess: (graded) => {
      setResult(graded);
      onAnswered();
      void queryClient.invalidateQueries({ queryKey: ["attempts", scope.slug, question.exerciseId] });
    },
  });

  if (!attempt) {
    return (
      <div className="flex justify-center py-8 text-gray-500">
        <Spinner />
      </div>
    );
  }
  return (
    <div>
      <Prose markdown={attempt.prompt} />
      {!result ? (
        <QuizExercise payload={attempt.payload} pending={answer.isPending} onSubmit={(a) => answer.mutate(a)} />
      ) : (
        <SolutionPanel
          open
          attemptId={attempt.attemptId}
          questionId={result.questionId ?? attempt.questionId ?? question.questionId}
          lessonId={lessonId}
          correct={result.correct}
          correctAnswer={result.correctAnswer}
          solutionSteps={result.solutionSteps}
          explanation={result.explanation}
          options={attempt.payload.options}
          excerpt={result.excerpt}
          noExcerpt={result.noExcerpt}
          lessonLink={result.lessonLink && (result.lessonLink.anchor || result.lessonLink.lessonId !== lessonId) ? result.lessonLink : null}
          reference={generated ? attempt.questionId : undefined}
          reportable={!generated}
        />
      )}
    </div>
  );
}
