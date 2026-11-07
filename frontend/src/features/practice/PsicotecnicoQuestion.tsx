import { useState } from "react";
import { useMutation, useQuery, useQueryClient } from "@tanstack/react-query";
import { answerAttempt, createAttempt, type Answer, type GradeResponse } from "@/api/exercises";
import { Spinner } from "@/components/ui/primitives";
import { scopeKey, useCourse } from "@/features/courses/CourseContext";
import { QuizExercise } from "@/features/exercises/QuizExercise";
import { SolutionPanel } from "@/features/exercises/SolutionPanel";
import { Prose } from "@/lib/markdown";

/** One generated item of a round: opened as a practice attempt (the server draws the seed), graded on answer. */
export function PsicotecnicoQuestion({
  round,
  position,
  exerciseId,
  onAnswered,
}: {
  round: number;
  position: number;
  exerciseId: string;
  onAnswered: (correct: boolean) => void;
}) {
  const { scope } = useCourse();
  const queryClient = useQueryClient();
  const [result, setResult] = useState<GradeResponse | null>(null);
  const { data: attempt } = useQuery({
    queryKey: ["psicotecnico-attempt", ...scopeKey(scope), round, position],
    queryFn: () => createAttempt(scope, exerciseId),
    staleTime: Infinity,
    gcTime: 0,
    retry: false,
  });
  const answer = useMutation({
    mutationFn: (a: Answer) => answerAttempt(scope, attempt!.attemptId, a),
    meta: { silentSuccess: true },
    onSuccess: (graded) => {
      setResult(graded);
      onAnswered(graded.correct);
      void queryClient.invalidateQueries({ queryKey: ["stats", scope.slug] });
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
          questionId={attempt.questionId}
          reference={attempt.questionId}
          correct={result.correct}
          correctAnswer={result.correctAnswer}
          solutionSteps={result.solutionSteps}
          explanation={result.explanation}
          options={attempt.payload.options}
          reportable={false}
        />
      )}
    </div>
  );
}
