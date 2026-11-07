import { apiClient, courseUrl, inReadingLanguage, type CourseScope } from "@/api/client";

/** One question of a practice round: opened with `createAttempt(scope, exerciseId, questionId)`. */
export interface PracticeQuestion {
  exerciseId: string;
  questionId: string;
}

export interface PracticeRound {
  lessonId: string;
  questions: PracticeQuestion[];
}

/** A round of a lesson's questions in the order to serve them: twenty, or `all` of them. */
export async function drawPracticeRound(scope: CourseScope, lessonId: string, all: boolean): Promise<PracticeRound> {
  const { data } = await apiClient.post<PracticeRound>(
    courseUrl(scope, `/lessons/${lessonId}/practice`),
    { all },
    inReadingLanguage(scope),
  );
  return data;
}

/** A «Psicotécnicos» round: generated exercise ids in the order to serve them, each opened as its own attempt. */
export interface GeneratedRound {
  exerciseIds: string[];
}

/** One type (`generator`) or every type in the course's weights (absent), `count` items. */
export async function drawPsicotecnicoRound(
  scope: CourseScope,
  count: number,
  generator?: string,
): Promise<GeneratedRound> {
  const { data } = await apiClient.post<GeneratedRound>(
    courseUrl(scope, "/practice/psicotecnicos"),
    { count, generator: generator ?? null },
    inReadingLanguage(scope),
  );
  return data;
}
