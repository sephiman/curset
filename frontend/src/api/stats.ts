import { apiClient, courseUrl, inReadingLanguage, type CourseScope } from "@/api/client";

export interface Coverage {
  publishedModules: number;
  totalModules: number;
  publishedLessons: number;
}

export interface Reading {
  lessonsCompleted: number;
  lessonsTotal: number;
  courseCompletion: number | null;
}

export interface ExerciseOverall {
  answered: number;
  correct: number;
  accuracy: number | null;
  firstAttemptAccuracy: number | null;
  /** Distinct exercises with at least one answered attempt — the first-attempt denominator. */
  firstSeen: number;
  firstCorrect: number;
  avgAttemptsToSuccess: number | null;
}

/** An exercise the learner got wrong at least once, and where to go to try it again. */
export interface ReviewTarget {
  exerciseId: string;
  /** Set when the failure is one question of a case: the exercise is the case. */
  questionId?: string;
  lessonId: string | null;
  incorrect: number;
  /** Solved since — shown as solved rather than implying unfinished business. */
  passed: boolean;
}

export interface ModuleStat {
  id: string;
  title: string | null;
  blockId: string | null;
  lessonsTotal: number;
  lessonsCompleted: number;
  exercisesTotal: number;
  exercisesPassed: number;
  /** Answered attempts — the `accuracy` denominator. Distinct from `firstSeen`. */
  answered: number;
  correct: number;
  accuracy: number | null;
  firstAttemptAccuracy: number | null;
  firstSeen: number;
  firstCorrect: number;
  exercisesFailed: number;
  toReview: ReviewTarget[];
}

export interface CostliestSection {
  moduleId: string;
  title: string | null;
  incorrect: number;
  answered: number;
  correct: number;
  firstAttemptAccuracy: number | null;
  firstSeen: number;
  firstCorrect: number;
  exercisesFailed: number;
  toReview: ReviewTarget[];
}

export interface Thresholds {
  /** Distinct exercises a module needs answered before it may be ranked as "costliest". */
  minExercisesToRank: number;
}

export interface MeStats {
  coverage: Coverage;
  thresholds: Thresholds;
  reading: Reading;
  exercise: ExerciseOverall;
  modules: ModuleStat[];
  costliestSections: CostliestSection[];
}

export interface GlobalThresholds {
  /** Distinct learners a row needs before the global panel is allowed to show it at all. */
  minLearners: number;
}

/** `learners` and `firstSeen` are two populations: the rate goes over `firstSeen`, the headcount is `learners`. */
export interface GlobalModule {
  moduleId: string;
  title: string | null;
  learners: number;
  firstSeen: number;
  firstCorrect: number;
  firstAttemptAccuracy: number | null;
}

export interface GlobalExercise {
  exerciseId: string;
  questionId?: string;
  moduleId: string;
  learners: number;
  firstSeen: number;
  firstCorrect: number;
  firstAttemptAccuracy: number | null;
}

export interface GlobalStats {
  thresholds: GlobalThresholds;
  exercises: GlobalExercise[];
  modules: GlobalModule[];
}

export async function getMeStats(scope: CourseScope): Promise<MeStats> {
  const { data } = await apiClient.get<MeStats>(courseUrl(scope, "/stats/me"), inReadingLanguage(scope));
  return data;
}

export async function getGlobalStats(scope: CourseScope): Promise<GlobalStats> {
  const { data } = await apiClient.get<GlobalStats>(courseUrl(scope, "/stats/global"), inReadingLanguage(scope));
  return data;
}

/** One lesson's (or module's) row of «Por tema»: blanks apart, the percentage counting them as not correct. */
export interface LessonTableRow {
  questions: number;
  correct: number;
  wrong: number;
  blank: number;
  pct: number | null;
  title: string;
}

export interface LessonTableGroup extends LessonTableRow {
  moduleId: string;
  lessons: (LessonTableRow & { lessonId: string })[];
}

export interface LessonTableLists {
  /** `module` when fewer than three lessons had enough questions to rank, so modules were ranked. */
  level: "lesson" | "module";
  best: (LessonTableRow & { lessonId?: string; moduleId?: string })[];
  worst: (LessonTableRow & { lessonId?: string; moduleId?: string })[];
}

export interface LessonTable {
  /** Questions a lesson needs before it may be ranked in the lists. */
  threshold: number;
  groups: LessonTableGroup[];
  /** Absent when nothing qualifies: then only the table shows. */
  lists: LessonTableLists | null;
}

/** «Por tema» over every practice attempt and every submitted exam of the course. */
export async function getLessonProgress(scope: CourseScope): Promise<LessonTable> {
  const { data } = await apiClient.get<LessonTable>(courseUrl(scope, "/stats/me/by-lesson"), inReadingLanguage(scope));
  return data;
}
