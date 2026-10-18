import { apiClient, courseUrl, inReadingLanguage, type CourseScope } from "@/api/client";
import type { ExerciseType } from "@/api/course";
import type { Answer, AttemptPayload } from "@/api/exercises";
import type { LessonTable } from "@/api/stats";

export type ExamStatus = "open" | "submitted" | "abandoned";

export interface ExamQuestion {
  index: number;
  attemptId: string;
  moduleId: string;
  moduleTitle: string;
  blockId: string;
  blockTitle: string;
  exerciseId: string;
  type: ExerciseType;
  prompt: string;
  payload: AttemptPayload;
  answered: boolean;
  givenAnswer: Answer | null;
  partId: string;
  /** The lesson the question counts under (a case question names its own). */
  lessonId: string | null;
  /** Set on a case question: `exerciseId` is the case, this is the question inside it. */
  questionId: string | null;
  /** Shown at the end of its part; counted only if a question before it is voided (never, here). */
  reserve: boolean;
  // Reveal-only (submitted review):
  lessonAnchor: string | null;
  citation: string | null;
  isCorrect: boolean | null;
  unanswered: boolean | null;
  correctAnswer: unknown;
  solutionSteps: string[];
  explanation: string | null;
}

export interface ExamCase {
  exerciseId: string;
  title: string;
  scenario: string;
}

export interface ExamPart {
  id: string;
  title: string | null;
  kind: "questions" | "cases";
  counted: number;
  reserve: number;
  /** Case parts: how many cases are offered; exactly one must be marked to be graded. */
  choose: number | null;
  penalty: string;
  cases: ExamCase[];
  marked: string[];
}

export type NotGraded = "no-case-marked" | "several-cases-marked" | "previous-part-not-passed";

export interface ExamResultPart {
  id: string;
  graded: boolean;
  reason: NotGraded | null;
  /** The marked case's exercise id, on a graded case part. */
  case: string | null;
  correct?: number;
  wrong?: number;
  blank?: number;
  questions?: number;
  raw?: number;
  transformed?: number;
  max?: number;
  passed?: boolean;
}

export interface ExamResultBlock {
  blockId: string;
  title: string;
  correct: number;
  total: number;
  score: number | null;
}

export interface ExamResultModule {
  moduleId: string;
  title: string;
  blockId: string;
  correct: boolean;
  unanswered: boolean;
}

export interface ExamResult {
  score: number | null;
  correct: number;
  total: number;
  blocks: ExamResultBlock[];
  modules: ExamResultModule[];
  // A scored preset only (penalties, transformed scores, cases or several parts):
  parts?: ExamResultPart[];
  raw?: number;
  transformed?: number | null;
  max?: number | null;
}

export interface ExamSession {
  id: string;
  presetId: string;
  presetVersion: number;
  presetTitle: string;
  target: string | null;
  targetTitle: string | null;
  status: ExamStatus;
  createdAt: string;
  finishedAt: string | null;
  /** When the clock runs out; null when the preset is untimed. */
  deadline: string | null;
  /** The server's clock at the response, so the countdown never trusts the device's. */
  serverNow: string;
  parts: ExamPart[];
  result: ExamResult | null;
  /** Revealed only: «Por tema». */
  byLesson: LessonTable | null;
  questions: ExamQuestion[];
}

export interface ExamHistoryItem {
  id: string;
  presetId: string;
  presetVersion: number;
  presetTitle: string;
  target: string | null;
  targetTitle: string | null;
  createdAt: string;
  finishedAt: string | null;
  score: number | null;
  correct: number;
  total: number;
  raw: number | null;
  transformed: number | null;
  max: number | null;
}

export interface PresetPart {
  id: string;
  title: string | null;
  kind: "questions" | "cases";
  questions: number;
  reserve: number;
  choose: number | null;
  penalty: string;
  max: number | null;
}

export interface PresetTarget {
  id: string;
  title: string;
  questions: number;
}

/** One exam of the course, as the Exams tab lists it. */
export interface ExamPreset {
  id: string;
  version: number;
  title: string;
  timeLimitMinutes: number | null;
  questions: number;
  parts: PresetPart[];
  /** A preset sat on one block, module or lesson at a time lists them here. */
  targets: PresetTarget[] | null;
}

export async function getExamPresets(course: CourseScope): Promise<ExamPreset[]> {
  const { data } = await apiClient.get<ExamPreset[]>(courseUrl(course, "/exams/presets"), inReadingLanguage(course));
  return data;
}

export async function startExam(course: CourseScope, presetId: string, target?: string): Promise<ExamSession> {
  const { data } = await apiClient.post<ExamSession>(
    courseUrl(course, "/exams"),
    { presetId, target: target ?? null },
    inReadingLanguage(course),
  );
  return data;
}

/**
 * EVERY open sitting, newest first.
 *
 * Starting an exam closes an open one of the same preset and target only, so two can be open at once,
 * and each needs a route in the UI to be resumed or abandoned.
 */
export async function getOpenExams(course: CourseScope): Promise<ExamSession[]> {
  const { data } = await apiClient.get<ExamSession[]>(courseUrl(course, "/exams/open"), inReadingLanguage(course));
  return data;
}

export async function getExam(course: CourseScope, examId: string): Promise<ExamSession> {
  const { data } = await apiClient.get<ExamSession>(courseUrl(course, `/exams/${examId}`), inReadingLanguage(course));
  return data;
}

export async function answerExamQuestion(
  course: CourseScope,
  examId: string,
  attemptId: string,
  answer: Answer,
): Promise<void> {
  await apiClient.post(courseUrl(course, `/exams/${examId}/questions/${attemptId}/answer`), { answer });
}

/** The cases of a part the learner marked; the part is graded only with exactly one. */
export async function markExamCases(
  course: CourseScope,
  examId: string,
  partId: string,
  exerciseIds: string[],
): Promise<void> {
  await apiClient.put(courseUrl(course, `/exams/${examId}/parts/${partId}/cases`), { exerciseIds });
}

export async function submitExam(course: CourseScope, examId: string): Promise<ExamSession> {
  const { data } = await apiClient.post<ExamSession>(
    courseUrl(course, `/exams/${examId}/submit`),
    {},
    inReadingLanguage(course),
  );
  return data;
}

export async function reviewExam(course: CourseScope, examId: string): Promise<ExamSession> {
  const { data } = await apiClient.get<ExamSession>(courseUrl(course, `/exams/${examId}/review`), inReadingLanguage(course));
  return data;
}

export async function abandonExam(course: CourseScope, examId: string): Promise<void> {
  await apiClient.post(courseUrl(course, `/exams/${examId}/abandon`), {});
}

export async function examHistory(course: CourseScope): Promise<ExamHistoryItem[]> {
  const { data } = await apiClient.get<ExamHistoryItem[]>(courseUrl(course, "/exams"), inReadingLanguage(course));
  return data;
}
