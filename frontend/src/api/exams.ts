import { apiClient, courseUrl, inReadingLanguage, type CourseScope } from "@/api/client";
import type { ExerciseType } from "@/api/course";
import type { Answer, AttemptPayload } from "@/api/exercises";

export type ExamScope = "global" | "block";
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
  // Reveal-only (submitted review):
  isCorrect: boolean | null;
  unanswered: boolean | null;
  correctAnswer: unknown;
  solutionSteps: string[];
  explanation: string | null;
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
}

export interface ExamSession {
  id: string;
  scope: ExamScope;
  blockId: string | null;
  blockTitle: string | null;
  status: ExamStatus;
  createdAt: string;
  finishedAt: string | null;
  result: ExamResult | null;
  questions: ExamQuestion[];
}

export interface ExamHistoryItem {
  id: string;
  scope: ExamScope;
  blockId: string | null;
  blockTitle: string | null;
  createdAt: string;
  finishedAt: string | null;
  score: number | null;
  correct: number;
  total: number;
}

export async function startExam(course: CourseScope, scope: ExamScope, blockId?: string): Promise<ExamSession> {
  const { data } = await apiClient.post<ExamSession>(
    courseUrl(course, "/exams"),
    { scope, blockId: blockId ?? null },
    inReadingLanguage(course),
  );
  return data;
}

/**
 * EVERY open sitting, newest first.
 *
 * This replaced a `/current` that answered with the newest one alone. Starting an exam only closes an
 * open one of the same scope, so a global and a block exam can be open at once — and the older of the
 * two then had no route in the UI that could reach it, to resume or to abandon.
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
