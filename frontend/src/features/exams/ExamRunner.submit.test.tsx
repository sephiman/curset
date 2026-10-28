import { act, type ReactNode } from "react";
import { createRoot } from "react-dom/client";
import { MemoryRouter, Route, Routes } from "react-router-dom";
import { QueryClient, QueryClientProvider } from "@tanstack/react-query";
import { afterEach, beforeEach, describe, expect, it, vi } from "vitest";
import en from "@/i18n/en.json";
import { InCourse } from "@/test/course";

/**
 * Handing in while an answer is still being saved.
 *
 * Each choice is saved as it is made. A reader who picks the last answer and hands in at once used to
 * send the hand-in before that save landed: the server closed the sitting, refused the save
 * («This exam is not in progress.», in English) and graded the question as blank.
 */

const calls: string[] = [];
let examFetches = 0;
let releaseSave: () => void = () => {};

const EXAM = {
  id: "exam-1",
  presetId: "tema",
  presetVersion: 1,
  presetTitle: "Tema",
  target: "m01-l01",
  targetTitle: "La Constitución",
  status: "open",
  deadline: null,
  serverNow: "2026-10-28T10:00:00Z",
  parts: [{ id: "preguntas", title: null, kind: "questions", counted: 1, reserve: 0, choose: null, penalty: "0", cases: [], marked: [] }],
  questions: [
    {
      index: 0,
      attemptId: "a-1",
      moduleId: "m01",
      moduleTitle: "Organización del Estado",
      blockId: "b",
      blockTitle: "B",
      exerciseId: "m01-l01-ex-1",
      type: "quiz",
      prompt: "¿Quién sanciona las leyes?",
      payload: { kind: "single_choice", options: [{ id: "a", text: "El Rey" }, { id: "b", text: "El Senado" }] },
      answered: false,
      givenAnswer: null,
      partId: "preguntas",
      lessonId: "m01-l01",
      questionId: null,
      reserve: false,
    },
  ],
};

vi.mock("@/api/exams", () => ({
  getExam: async () => {
    examFetches += 1;
    return EXAM;
  },
  answerExamQuestion: (_scope: unknown, _exam: string, attemptId: string) => {
    calls.push(`save ${attemptId}`);
    return new Promise<void>((resolve) => {
      releaseSave = () => {
        calls.push(`saved ${attemptId}`);
        resolve();
      };
    });
  },
  submitExam: async () => {
    calls.push("submit");
    return EXAM;
  },
  markExamCases: async () => undefined,
  abandonExam: async () => undefined,
}));

vi.mock("@/features/references/ProseReferenceHost", () => ({
  ProseReferenceHost: ({ children }: { children: ReactNode }) => children,
}));

function translate(key: string, params?: Record<string, unknown>): string {
  const template = key.split(".").reduce<unknown>((node, part) => (node as Record<string, unknown>)?.[part], en);
  if (typeof template !== "string") return key;
  return template.replace(/\{\{(\w+)\}\}/g, (_, name: string) => String(params?.[name]));
}
vi.mock("react-i18next", () => ({
  useTranslation: () => ({ t: translate, i18n: { resolvedLanguage: "en" } }),
  initReactI18next: { type: "3rdParty", init: () => {} },
}));

const { ExamRunner } = await import("./ExamRunner");

(globalThis as { IS_REACT_ACT_ENVIRONMENT?: boolean }).IS_REACT_ACT_ENVIRONMENT = true;

let host: HTMLDivElement;

async function settle(): Promise<void> {
  for (let i = 0; i < 5; i += 1) await act(async () => await new Promise((resolve) => setTimeout(resolve, 0)));
}

function submitButton(): HTMLButtonElement {
  return [...host.querySelectorAll("button")].find((b) => b.textContent === en.exam.submit)!;
}

beforeEach(async () => {
  calls.length = 0;
  examFetches = 0;
  vi.spyOn(window, "confirm").mockReturnValue(true);
  host = document.createElement("div");
  document.body.appendChild(host);
  const client = new QueryClient({ defaultOptions: { queries: { retry: false } } });
  act(() => {
    createRoot(host).render(
      <QueryClientProvider client={client}>
        <MemoryRouter initialEntries={["/courses/crypto-futures/exams/exam-1"]}>
          <InCourse>
            <Routes>
              <Route path="/courses/:course/exams/:examId" element={<ExamRunner />} />
              <Route path="*" element={<p>review</p>} />
            </Routes>
          </InCourse>
        </MemoryRouter>
      </QueryClientProvider>,
    );
  });
  await settle();
});

afterEach(() => {
  document.body.innerHTML = "";
  vi.restoreAllMocks();
});

describe("handing in an exam", () => {
  it("waits for the answer still being saved, then hands in", async () => {
    act(() => host.querySelector<HTMLInputElement>('input[type="radio"]')!.click());
    act(() => submitButton().click());
    await settle();
    expect(calls).toEqual(["save a-1"]);

    act(() => releaseSave());
    await settle();
    expect(calls).toEqual(["save a-1", "saved a-1", "submit"]);
  });

  it("saves no answer changed after handing in began", async () => {
    const radios = host.querySelectorAll<HTMLInputElement>('input[type="radio"]');
    act(() => radios[0].click());
    act(() => submitButton().click());
    act(() => radios[1].click());
    await settle();
    expect(calls).toEqual(["save a-1"]);
    act(() => releaseSave());
    await settle();
    expect(calls).toEqual(["save a-1", "saved a-1", "submit"]);
  });

  it("does not fetch the sitting it just closed, which the server refuses as no longer in progress", async () => {
    act(() => host.querySelector<HTMLInputElement>('input[type="radio"]')!.click());
    await settle();
    act(() => releaseSave());
    await settle();
    act(() => submitButton().click());
    await settle();
    expect(calls).toEqual(["save a-1", "saved a-1", "submit"]);
    expect(examFetches).toBe(1);
  });
});
