import { act, type ReactNode } from "react";
import { createRoot } from "react-dom/client";
import { MemoryRouter, Route, Routes } from "react-router-dom";
import { QueryClient, QueryClientProvider } from "@tanstack/react-query";
import { afterEach, beforeEach, describe, expect, it, vi } from "vitest";
import en from "@/i18n/en.json";
import { InCourse } from "@/test/course";

let examData: Record<string, unknown> = {};
const calls: string[] = [];

vi.mock("@/api/exams", () => ({
  getExam: async () => examData,
  answerExamQuestion: vi.fn(async (_scope, _exam, attemptId, _ans, timing) => {
    calls.push(`answer ${attemptId} time=${timing?.timeSeconds}`);
  }),
  pauseExam: vi.fn(async (_scope, _exam, attemptId) => {
    calls.push(`pause ${attemptId}`);
  }),
  resumeExam: vi.fn(async () => {
    calls.push("resume");
  }),
  submitExam: vi.fn(async () => {
    calls.push("submit");
    return examData;
  }),
  markExamCases: vi.fn(),
  abandonExam: vi.fn(),
}));

vi.mock("@/features/references/ProseReferenceHost", () => ({
  ProseReferenceHost: ({ children }: { children: ReactNode }) => children,
}));

function translate(key: string, params?: Record<string, unknown>): string {
  const parts = key.split(".");
  let cur: unknown = en;
  for (const part of parts) {
    if (typeof cur !== "object" || cur === null) return key;
    cur = (cur as Record<string, unknown>)[part];
  }
  if (typeof cur !== "string") return key;
  return params
    ? Object.entries(params).reduce((acc, [k, v]) => acc.replace(`{{${k}}}`, String(v)), cur)
    : cur;
}

vi.mock("react-i18next", () => ({
  useTranslation: () => ({ t: translate, i18n: { resolvedLanguage: "en", language: "en" } }),
  initReactI18next: { type: "3rdParty", init: () => {} },
}));

const { ExamRunner } = await import("@/features/exams/ExamRunner");

(globalThis as { IS_REACT_ACT_ENVIRONMENT?: boolean }).IS_REACT_ACT_ENVIRONMENT = true;

let host: HTMLDivElement;
let qc: QueryClient;

beforeEach(() => {
  calls.length = 0;
  qc = new QueryClient({ defaultOptions: { queries: { retry: false } } });
  host = document.createElement("div");
  document.body.appendChild(host);

  examData = {
    id: "exam-1",
    presetId: "tema",
    presetVersion: 1,
    presetTitle: "Tema",
    target: "m01-l01",
    targetTitle: "La Constitución",
    status: "open",
    deadline: null,
    pause: "between-questions",
    paused: false,
    activeSeconds: 15,
    serverNow: "2026-10-28T10:00:00Z",
    parts: [{ id: "preguntas", title: null, kind: "questions", counted: 2, reserve: 0, choose: null, penalty: "0", cases: [], marked: [] }],
    questions: [
      {
        index: 0,
        attemptId: "a-1",
        moduleId: "m01",
        moduleTitle: "Organización",
        blockId: "b",
        blockTitle: "B",
        exerciseId: "q1",
        type: "quiz",
        prompt: "First question?",
        payload: { kind: "single_choice", options: [{ id: "o0", text: "Alpha" }, { id: "o1", text: "Beta" }] },
        answered: false,
        givenAnswer: null,
        partId: "preguntas",
        lessonId: "m01-l01",
        questionId: null,
        reserve: false,
      },
      {
        index: 1,
        attemptId: "a-2",
        moduleId: "m01",
        moduleTitle: "Organización",
        blockId: "b",
        blockTitle: "B",
        exerciseId: "q2",
        type: "quiz",
        prompt: "Second question?",
        payload: { kind: "single_choice", options: [{ id: "o0", text: "Gamma" }, { id: "o1", text: "Delta" }] },
        answered: false,
        givenAnswer: null,
        partId: "preguntas",
        lessonId: "m01-l01",
        questionId: null,
        reserve: false,
      },
    ],
  };
});

afterEach(() => {
  host.remove();
  qc.clear();
});

async function settle(): Promise<void> {
  for (let i = 0; i < 5; i += 1) await act(async () => await new Promise((resolve) => setTimeout(resolve, 0)));
}

async function mount(): Promise<void> {
  act(() => {
    createRoot(host).render(
      <MemoryRouter initialEntries={["/courses/crypto-futures/exams/exam-1"]}>
        <InCourse>
          <QueryClientProvider client={qc}>
            <Routes>
              <Route path="/courses/:course/exams/:examId" element={<ExamRunner />} />
              <Route path="/courses/:course/exams/:examId/review" element={<div>Review page</div>} />
            </Routes>
          </QueryClientProvider>
        </InCourse>
      </MemoryRouter>,
    );
  });
  await settle();
}

describe("exam runner clock and pause", () => {
  it("displays time used from server activeSeconds", async () => {
    await mount();
    expect(host.textContent).toContain("Time: 00:15");
  });

  it("pause button is disabled until current question is answered", async () => {
    await mount();
    const pauseBtn = [...host.querySelectorAll("button")].find((b) => b.textContent?.includes("Pause"));
    expect(pauseBtn).toBeDefined();
    expect(pauseBtn?.disabled).toBe(true);

    // Answer the question
    const radio = host.querySelector("input[type=radio]") as HTMLInputElement;
    act(() => radio.click());
    await settle();

    // Now pause button should be enabled
    expect(pauseBtn?.disabled).toBe(false);
  });

  it("pausing hides questions and shows resume cover; resuming advances to next question", async () => {
    await mount();
    expect(host.textContent).toContain("First question?");

    // Answer
    const radio = host.querySelector("input[type=radio]") as HTMLInputElement;
    act(() => radio.click());
    await settle();

    const pauseBtn = [...host.querySelectorAll("button")].find((b) => b.textContent?.includes("Pause"))!;
    act(() => pauseBtn.click());
    await settle();

    expect(calls).toContain("pause a-1");
    // Questions are covered
    expect(host.textContent).not.toContain("First question?");
    expect(host.textContent).toContain("Exam paused");

    // Click resume
    const resumeBtn = [...host.querySelectorAll("button")].find((b) => b.textContent?.includes("Resume"))!;
    act(() => resumeBtn.click());
    await settle();

    expect(calls).toContain("resume");
    // Uncovered and advanced to question 2
    expect(host.textContent).toContain("Second question?");
  });

  it("never preset does not render pause button", async () => {
    examData.pause = "never";
    await mount();
    const pauseBtn = [...host.querySelectorAll("button")].find((b) => b.textContent?.includes("Pause"));
    expect(pauseBtn).toBeUndefined();
  });

  it("auto-submits when deadline passes", async () => {
    // Deadline in the past, matching serverNow
    const now = new Date();
    examData.serverNow = now.toISOString();
    examData.deadline = new Date(now.getTime() - 5000).toISOString();
    await mount();
    await settle();
    expect(calls).toContain("submit");
  });

  it("moving to next question when blank records elapsed time for the blank question", async () => {
    await mount();
    // Initially on question 1 (a-1). Click Next without answering.
    const nextBtn = [...host.querySelectorAll("button")].find((b) => b.textContent?.includes("Next"))!;
    act(() => nextBtn.click());
    await settle();

    // Now on question 2. Moving from blank question 1 should have called answerExamQuestion with a-1
    const blankAnswerCall = calls.find((c) => c.startsWith("answer a-1"));
    expect(blankAnswerCall).toBeDefined();
    expect(host.textContent).toContain("Second question?");
  });
});

