import { act, type ReactNode } from "react";
import { createRoot } from "react-dom/client";
import { MemoryRouter, Route, Routes } from "react-router-dom";
import { QueryClient, QueryClientProvider } from "@tanstack/react-query";
import { afterEach, beforeEach, describe, expect, it, vi } from "vitest";
import en from "@/i18n/en.json";
import { InCourse } from "@/test/course";
import { clearViewport, setViewportWidth } from "@/test/viewport";

let examData: Record<string, unknown> = {};
const calls: string[] = [];

/** K3 against J3: the sitting's navigator either side of 1024 px. */

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
  clearViewport();
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

// jsdom lays nothing out, so it has no element scrolling for the strip to centre its chip with.
Element.prototype.scrollTo = () => undefined;

const navigator = () => host.querySelector<HTMLElement>(`nav[aria-label="${en.exam.navigator}"]`);
const goTo = () => [...host.querySelectorAll("button")].find((button) => button.textContent === en.exam.goTo);

describe("the exam sitting's question navigator", () => {
  it("is the full grid in a side panel at 1024 px, with Previous/Next under the question", async () => {
    setViewportWidth(1024);
    await mount();
    expect(navigator()?.textContent).toContain(en.exam.questionsSheet);
    expect(navigator()?.querySelectorAll("button")).toHaveLength(2);
    expect(goTo()).toBeUndefined();
    const next = [...host.querySelectorAll("button")].find((button) => button.textContent?.includes(en.exam.next))!;
    expect(next.closest(".fixed")).toBeNull();
  });

  it("is the chip strip with «Go to…» at 1023 px, with Previous/Next fixed at the bottom", async () => {
    setViewportWidth(1023);
    await mount();
    expect(navigator()?.textContent).not.toContain(en.exam.questionsSheet);
    expect(goTo()).toBeDefined();
    const next = [...host.querySelectorAll("button")].find((button) => button.textContent?.includes(en.exam.next))!;
    expect(next.closest(".fixed")).not.toBeNull();
  });
});
