import { apiClient, courseUrl, inReadingLanguage, type CourseScope } from "@/api/client";
import type { ExerciseType } from "@/api/course";

export type AttemptState = "open" | "answered" | "abandoned";

export type QuizKind =
  | "single_choice"
  | "true_false"
  | "multi_select"
  | "ordering"
  | "matching";

/** A selectable item: quiz/ordering/matching carry `text`, calculation carries `value`. */
export interface OptionView {
  id: string;
  text?: string;
  value?: string | number;
}

export interface ChartSeriesPayload {
  time: number[];
  open: number[];
  high: number[];
  low: number[];
  close: number[];
  volume: number[];
}

export interface PriceLevelPayload {
  price: number;
  label: string;
  kind: string;
}

/** A sloped line (m15). Public on the question, unlike a band — see `PriceDiagonal`. */
export interface PriceDiagonalPayload {
  start: number;
  end: number;
  start_price: number;
  end_price: number;
  label: string;
  kind: string;
}

/**
 * The second candle panel (m23-l2): the same stretch of price at a coarser resolution.
 *
 * `position` is where it draws, not what it is — the two panels are the same size on purpose, so
 * "which of these contains the other" is answered off the candles and never off the layout.
 */
export interface TimeframeContext {
  series: ChartSeriesPayload;
  position: "above" | "below";
}

/** «Ver en la lección»: the question's lesson, at the anchor of what it cites (null: the top). */
export interface LessonLink {
  lessonId: string;
  anchor: string | null;
  citation: string | null;
}

/** The cited text of the norm (or of a saved page) a solution panel shows; built with the course. */
export interface SolutionExcerpt {
  /** «Art. 30.4 LPAC», or the cited label of a saved page. */
  heading: string;
  /** Paragraphs separated by a blank line; at most 200 words, «[…]» marks a cut. */
  text: string;
  /** The whole article behind «Ver artículo completo»; null when `text` is all of it or it is too long. */
  full: string | null;
  /** The article is too long to show: «Ver artículo completo» opens the source instead. */
  fullTooLong: boolean;
  /** «Texto consolidado»: the source at the article or page. */
  href: string;
  /** A saved page's title and consultation date; null for a norm. */
  attribution: string | null;
}

export type NoExcerptReason =
  | "no-citation"
  | "no-norm"
  | "no-file"
  | "not-text"
  | "no-heading"
  | "no-label"
  | "no-match"
  | "no-parse"
  | "no-fact";

/** «Sin extracto»: why, and the source the question cites when the course keeps it. */
export interface NoExcerpt {
  reason: NoExcerptReason;
  href: string | null;
}

export interface AttemptPayload {
  // quiz — every quiz payload carries `kind`; calculation carries "multiple_choice".
  kind?: QuizKind | "multiple_choice";
  options?: OptionView[]; // single_choice, multi_select, calculation
  items?: OptionView[]; // ordering (already shuffled)
  lefts?: OptionView[]; // matching — left column (shuffled)
  rights?: OptionView[]; // matching — right column (shuffled)
  // calculation
  unit?: string | null;
  formula?: string;
  // case (print only): the scenario and its questions in order
  scenario?: string;
  questions?: { id: string; number: string; prompt: string; payload: AttemptPayload }[];
  // chart
  series?: ChartSeriesPayload;
  rsi?: number[];
  macd?: { line: number[]; signal: number[]; hist: number[] };
  oi?: number[];
  cvd?: number[];
  // The zero-centred pane (m16): a signed series and its optional per-bar state row.
  momentum?: number[];
  momentum_state?: number[];
  indicator?: "rsi" | "macd" | "oi" | "cvd" | "momentum" | "none";
  choices?: string[];
  // pattern_chart: price-pane overlays (name -> values aligned 1:1 with the series), levels and the
  // sloped lines m15 asks its questions against.
  overlays?: Record<string, number[]>;
  levels?: PriceLevelPayload[];
  diagonals?: PriceDiagonalPayload[];
  /** A second panel of the SAME price at a coarser frame (m23-l2). Public, like `diagonals`. */
  context?: TimeframeContext;
}

export interface AttemptInstance {
  attemptId: string;
  exerciseId: string;
  questionId?: string | null;
  type: ExerciseType;
  prompt: string;
  payload: AttemptPayload;
  state: AttemptState;
}

export interface GradeResponse {
  attemptId: string;
  questionId?: string | null;
  correct: boolean;
  correctAnswer: unknown;
  solutionSteps: string[];
  explanation: string | null;
  lessonLink?: LessonLink | null;
  excerpt?: SolutionExcerpt | null;
  /** Set instead of `excerpt` when the course keeps norms but found no text for the question: why. */
  noExcerpt?: NoExcerpt | null;
}

export interface AttemptReview extends AttemptInstance {
  questionId: string | null;
  lessonLink: LessonLink | null;
  excerpt?: SolutionExcerpt | null;
  noExcerpt?: NoExcerpt | null;
  givenAnswer: Record<string, unknown> | null;
  isCorrect: boolean | null;
  correctAnswer: unknown;
  solutionSteps: string[];
  explanation: string | null;
  createdAt: string;
  answeredAt: string | null;
}

export interface AttemptSummary {
  attemptId: string;
  exerciseId: string;
  state: AttemptState;
  isCorrect: boolean | null;
  createdAt: string;
  answeredAt: string | null;
}

export type Answer =
  | { optionId: string } // single_choice, calculation
  | { optionIds: string[] } // multi_select
  | { value: boolean } // true_false
  | { order: string[] } // ordering
  | { pairs: Record<string, string> } // matching
  | { divergence: string } // divergence chart
  | { label: string }; // pattern chart

/** Deferred-grading mode (exams): answer-capture only, no submit button or feedback. */
export type Deferred = { value: Answer | null; onChange: (answer: Answer) => void };

/** A fresh attempt: the question its seed draws, or the one `variantId` names (lesson practice). */
export async function createAttempt(scope: CourseScope, exerciseId: string, variantId?: string): Promise<AttemptInstance> {
  const { data } = await apiClient.post<AttemptInstance>(
    courseUrl(scope, `/exercises/${exerciseId}/attempts`),
    variantId ? { variantId } : undefined,
    inReadingLanguage(scope),
  );
  return data;
}

/** One question of an opened case: its own attempt, answered through `answerAttempt`. */
export interface CaseQuestionInstance {
  attemptId: string;
  questionId: string;
  lessonId: string | null;
  prompt: string;
  payload: AttemptPayload;
}

export interface CaseInstance {
  exerciseId: string;
  title: string;
  scenario: string;
  questions: CaseQuestionInstance[];
}

export async function openCase(scope: CourseScope, exerciseId: string): Promise<CaseInstance> {
  const { data } = await apiClient.post<CaseInstance>(
    courseUrl(scope, `/exercises/${exerciseId}/case-attempts`),
    undefined,
    inReadingLanguage(scope),
  );
  return data;
}

export async function answerAttempt(scope: CourseScope, attemptId: string, answer: Answer): Promise<GradeResponse> {
  const { data } = await apiClient.post<GradeResponse>(
    courseUrl(scope, `/attempts/${attemptId}/answer`),
    { answer },
    inReadingLanguage(scope),
  );
  return data;
}

export async function getAttempt(scope: CourseScope, attemptId: string): Promise<AttemptReview> {
  const { data } = await apiClient.get<AttemptReview>(courseUrl(scope, `/attempts/${attemptId}`), inReadingLanguage(scope));
  return data;
}

export async function listAttempts(scope: CourseScope, exerciseId: string): Promise<AttemptSummary[]> {
  const { data } = await apiClient.get<AttemptSummary[]>(
    courseUrl(scope, "/attempts"),
    inReadingLanguage(scope, { exercise_id: exerciseId }),
  );
  return data;
}
