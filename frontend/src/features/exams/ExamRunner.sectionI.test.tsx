import { act } from "react";
import { createRoot } from "react-dom/client";
import { MemoryRouter, Route, Routes } from "react-router-dom";
import { QueryClient, QueryClientProvider } from "@tanstack/react-query";
import { afterEach, beforeEach, describe, expect, it, vi } from "vitest";
import en from "@/i18n/en.json";
import type { ExamSession } from "@/api/exams";
import type { Course } from "@/api/course";
import { InCourse } from "@/test/course";

(globalThis as { IS_REACT_ACT_ENVIRONMENT?: boolean }).IS_REACT_ACT_ENVIRONMENT = true;

/**
 * Delta Section I tests:
 * I1 Every question shows «Pregunta N de M» in practice and in every exam and review.
 * I2 The tema label («Tema III.3 · <lesson title>») is shown in practice, in «Tema» and «Bloque» exams and in every review.
 *    It is not shown during a «Simulacro oficial», «Parte 1» or «Parte 2» sitting; it appears in that exam's review.
 * I3 The solution panel and the review show the question's stable id as a copyable reference («age-c1 · III.3 · q127»).
 * I4 Courses without lesson_noun (crypto-futures) show the number only, as today.
 */

const AGE_COURSE: Course = {
  locale: "es",
  started: true,
  course: {
    id: "age-administrativo-c1",
    title: "Administrativo del Estado (C1)",
    subtitle: "Ingreso libre",
    description: "Programa AGE",
    lessonNoun: "tema",
  },
  blocks: [
    {
      id: "block-b",
      order: 1,
      title: "Programa",
      modules: [
        {
          id: "m03",
          order: 3,
          title: "Derecho Administrativo General",
          summary: "Summary",
          assumes: [],
          unmetPrereqs: [],
          hasContent: true,
          lessonsTotal: 1,
          lessonsCompleted: 0,
          exercisesTotal: 1,
          exercisesPassed: 0,
          lessons: [
            {
              id: "m03-l03",
              order: 3,
              title: "El acto administrativo",
              summary: "Summary",
              completed: false,
              readingSeconds: 300,
              exercises: [],
            },
          ],
        },
      ],
    },
  ],
};

const CRYPTO_COURSE: Course = {
  locale: "en",
  started: true,
  course: {
    id: "crypto-futures",
    title: "Crypto Futures",
    subtitle: "Trading",
    description: "Futures",
  },
  blocks: [
    {
      id: "block-a",
      order: 1,
      title: "Basics",
      modules: [
        {
          id: "m01",
          order: 1,
          title: "Orders",
          summary: "Summary",
          assumes: [],
          unmetPrereqs: [],
          hasContent: true,
          lessonsTotal: 1,
          lessonsCompleted: 0,
          exercisesTotal: 1,
          exercisesPassed: 0,
          lessons: [
            {
              id: "m01-l01",
              order: 1,
              title: "Limit orders",
              summary: "Summary",
              completed: false,
              readingSeconds: 300,
              exercises: [],
            },
          ],
        },
      ],
    },
  ],
};

let currentCourseTree: Course = AGE_COURSE;
let currentExamSession: ExamSession | null = null;

vi.mock("@/api/exams", async (importOriginal) => {
  const actual = await importOriginal<typeof import("@/api/exams")>();
  return {
    ...actual,
    getExam: async () => currentExamSession,
    reviewExam: async () => currentExamSession,
    answerExamQuestion: vi.fn(async () => ({ activeSeconds: 10 })),
  };
});

vi.mock("@/api/course", async (importOriginal) => {
  const actual = await importOriginal<typeof import("@/api/course")>();
  return {
    ...actual,
    getCourse: async () => currentCourseTree,
  };
});

function translate(key: string, params?: Record<string, unknown>): string {
  const lookup = (path: string): unknown =>
    path.split(".").reduce<unknown>((node, part) => (node as Record<string, unknown>)?.[part], en);
  const count = params?.count;
  const plural = typeof count === "number" ? lookup(`${key}_${count === 1 ? "one" : "other"}`) : undefined;
  const template = plural ?? lookup(key);
  if (typeof template !== "string") return key;
  return template.replace(/\{\{(\w+)\}\}/g, (_, name: string) => String(params?.[name]));
}

vi.mock("react-i18next", () => ({
  useTranslation: () => ({ t: translate, i18n: { resolvedLanguage: "es", language: "es" } }),
  initReactI18next: { type: "3rdParty", init: () => {} },
}));

const { ExamRunner } = await import("@/features/exams/ExamRunner");
const { ExamReview } = await import("@/features/exams/ExamReview");

function makeExamSession(
  presetId: string,
  status: "open" | "submitted" = "open",
): ExamSession {
  return {
    id: "exam-test-1",
    presetId,
    presetVersion: 1,
    presetTitle: presetId === "simulacro" ? "Simulacro oficial" : "Tema",
    target: null,
    targetTitle: null,
    status,
    createdAt: "2026-10-30T10:00:00Z",
    finishedAt: status === "submitted" ? "2026-10-30T11:00:00Z" : null,
    deadline: null,
    pause: "between-questions",
    paused: false,
    activeSeconds: 120,
    serverNow: "2026-10-30T10:00:00Z",
    byLesson: null,
    parts: [
      {
        id: "parte-1",
        title: "Primera parte",
        kind: "questions",
        counted: 2,
        reserve: 0,
        choose: null,
        penalty: "0",
        cases: [],
        marked: [],
      },
    ],
    questions: [
      {
        index: 0,
        attemptId: "att-1",
        moduleId: "m03",
        moduleTitle: "Derecho Administrativo",
        blockId: "block-b",
        blockTitle: "Programa",
        exerciseId: "m03-l03-ex-1",
        type: "quiz",
        prompt: "Pregunta sobre el acto administrativo.",
        payload: { kind: "single_choice", options: [{ id: "a", text: "Opción A" }] },
        answered: false,
        givenAnswer: null,
        partId: "parte-1",
        lessonId: "m03-l03",
        questionId: "m03-l03-q127",
        reserve: false,
        lessonAnchor: null,
        citation: null,
        isCorrect: true,
        unanswered: false,
        correctAnswer: { optionId: "a", text: "Opción A" },
        solutionSteps: [],
        explanation: "Explicación del tema.",
      },
      {
        index: 1,
        attemptId: "att-2",
        moduleId: "m03",
        moduleTitle: "Derecho Administrativo",
        blockId: "block-b",
        blockTitle: "Programa",
        exerciseId: "m03-l03-ex-1",
        type: "quiz",
        prompt: "Segunda pregunta sobre el acto administrativo.",
        payload: { kind: "single_choice", options: [{ id: "a", text: "Opción A" }] },
        answered: false,
        givenAnswer: null,
        partId: "parte-1",
        lessonId: "m03-l03",
        questionId: "m03-l03-q128",
        reserve: false,
        lessonAnchor: null,
        citation: null,
        isCorrect: true,
        unanswered: false,
        correctAnswer: { optionId: "a", text: "Opción A" },
        solutionSteps: [],
        explanation: "Explicación 2.",
      },
    ],
    result:
      status === "submitted"
        ? {
            raw: 2,
            score: 1.0,
            correct: 2,
            total: 2,
            totalActiveSeconds: 120,
            blocks: [],
            modules: [],
            parts: [],
          }
        : null,
  };
}

let host: HTMLDivElement;
let qc: QueryClient;

beforeEach(() => {
  host = document.createElement("div");
  document.body.appendChild(host);
  qc = new QueryClient({ defaultOptions: { queries: { retry: false } } });
  currentCourseTree = AGE_COURSE;
});

afterEach(() => {
  host.remove();
  qc.clear();
});

async function settle(): Promise<void> {
  for (let i = 0; i < 5; i += 1) {
    await act(async () => {
      await new Promise((resolve) => setTimeout(resolve, 0));
    });
  }
}

async function render(node: React.ReactNode, path = "/courses/age-administrativo-c1/exams/exam-test-1") {
  act(() => {
    createRoot(host).render(
      <QueryClientProvider client={qc}>
        <MemoryRouter initialEntries={[path]}>
          <InCourse>
            <Routes>
              <Route path="/courses/:courseId/exams/:examId" element={node} />
              <Route path="/courses/:courseId/exams/:examId/review" element={node} />
            </Routes>
          </InCourse>
        </MemoryRouter>
      </QueryClientProvider>,
    );
  });
  await settle();
}

describe("Delta Section I — question number, tema label and shareable reference", () => {
  it("I1 & I2: shows question number and tema label during a «Tema» or «Bloque» sitting", async () => {
    currentExamSession = makeExamSession("tema", "open");
    await render(<ExamRunner />);

    // Question number: "Question 1 of 2"
    expect(host.textContent).toContain("Question 1 of 2");
    // Tema label: "Tema III.3 · El acto administrativo"
    expect(host.textContent).toContain("Tema III.3 · El acto administrativo");
  });

  it("I2: hides tema label during a «Simulacro oficial» sitting", async () => {
    currentExamSession = makeExamSession("simulacro", "open");
    await render(<ExamRunner />);

    // Shows question number
    expect(host.textContent).toContain("Question 1 of 2");
    // Does NOT show tema label during simulation sitting
    expect(host.textContent).not.toContain("Tema III.3");
  });

  it("I1, I2 & I3: shows question number, tema label and copyable reference in review of a Simulacro", async () => {
    currentExamSession = makeExamSession("simulacro", "submitted");
    await render(<ExamReview />, "/courses/age-administrativo-c1/exams/exam-test-1/review");

    // Question number
    expect(host.textContent).toContain("Question 1 of 2");
    // Tema label is revealed in review
    expect(host.textContent).toContain("Tema III.3 · El acto administrativo");
    // Stable copyable question reference is present
    expect(host.textContent).toContain("age-c1 · III.3 · q127");
  });

  it("I4: crypto-futures shows question number only, with no tema label or copyable reference", async () => {
    currentCourseTree = CRYPTO_COURSE;
    currentExamSession = {
      ...makeExamSession("block", "open"),
      questions: [
        {
          ...makeExamSession("block", "open").questions[0],
          lessonId: "m01-l01",
          questionId: "q1",
        },
      ],
    };
    await render(<ExamRunner />, "/courses/crypto-futures/exams/exam-test-1");

    // Question number shown
    expect(host.textContent).toContain("Question 1 of 1");
    // No tema label
    expect(host.textContent).not.toContain("Tema III.3");
    // No copyable reference
    expect(host.textContent).not.toContain("crypto-futures ·");
  });
});
