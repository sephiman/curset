import { apiClient, courseUrl, inReadingLanguage, type CourseScope } from "@/api/client";

/** One question of a practice round: opened with `createAttempt(scope, exerciseId, questionId)`. */
export interface PracticeQuestion {
  exerciseId: string;
  questionId: string;
}

/** The questions of a round, in the order to serve them. */
export interface DrawnRound {
  questions: PracticeQuestion[];
}

export interface PracticeRound extends DrawnRound {
  lessonId: string;
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

/** A round of a module's questions, in the order to serve them: twenty, or `all` of them. */
export async function drawModuleRound(scope: CourseScope, moduleId: string, all: boolean): Promise<DrawnRound> {
  const { data } = await apiClient.post<DrawnRound>(
    courseUrl(scope, `/modules/${moduleId}/practice`),
    { all },
    inReadingLanguage(scope),
  );
  return data;
}

/** The course-wide presets that draw a fixed count: the scheduler's mixed review, or code reading only. */
export type CourseRoundPreset = "review" | "code-reading";

export async function drawCourseRound(scope: CourseScope, preset: CourseRoundPreset, count: number): Promise<DrawnRound> {
  const { data } = await apiClient.post<DrawnRound>(
    courseUrl(scope, `/practice/${preset}`),
    { count },
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
