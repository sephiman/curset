import { act } from "react";
import { createRoot } from "react-dom/client";
import { QueryClient, QueryClientProvider } from "@tanstack/react-query";
import { beforeEach, describe, expect, it, vi } from "vitest";
import en from "@/i18n/en.json";
import { InCourse } from "@/test/course";

/** The report link exists only where the answer already is: never before answering (R8a.1). */

const QUIZ = {
  attemptId: "attempt-1",
  exerciseId: "m01-ex-1",
  type: "quiz",
  prompt: "Which statement best describes a stablecoin?",
  payload: { kind: "single_choice", options: [{ id: "a", text: "A token" }, { id: "b", text: "A share" }] },
  state: "open",
};
const CALCULATION = {
  ...QUIZ,
  attemptId: "attempt-2",
  type: "calculation",
  payload: { options: [{ id: "a", text: "10" }, { id: "b", text: "20" }] },
};
const GRADED = { attemptId: "attempt-1", correct: false, correctAnswer: { optionId: "a", text: "A token" }, solutionSteps: [], explanation: null };

let opened: typeof QUIZ | typeof CALCULATION = QUIZ;
vi.mock("@/api/exercises", () => ({
  createAttempt: async () => opened,
  answerAttempt: async () => GRADED,
  listAttempts: async () => [],
  getAttempt: async () => null,
}));

function translate(key: string, params?: Record<string, unknown>): string {
  const template = key
    .split(".")
    .reduce<unknown>((node, part) => (node as Record<string, unknown>)?.[part], en);
  if (typeof template !== "string") return key;
  return template.replace(/\{\{(\w+)\}\}/g, (_, name: string) => String(params?.[name]));
}
vi.mock("react-i18next", () => ({
  useTranslation: () => ({ t: translate, i18n: { resolvedLanguage: "en", language: "en" } }),
  initReactI18next: { type: "3rdParty", init: () => {} },
}));

const { ExercisePlayer } = await import("@/features/exercises/ExercisePlayer");

(globalThis as { IS_REACT_ACT_ENVIRONMENT?: boolean }).IS_REACT_ACT_ENVIRONMENT = true;

let host: HTMLDivElement;

async function settle(): Promise<void> {
  await act(async () => {
    await new Promise((resolve) => setTimeout(resolve, 0));
  });
}

async function clickButton(label: string): Promise<void> {
  const button = [...host.querySelectorAll("button")].find((b) => b.textContent === label);
  if (!button) throw new Error(`no button ${label}`);
  await act(async () => button.click());
  await settle();
}

async function mount(type: "quiz" | "calculation"): Promise<void> {
  host = document.createElement("div");
  document.body.appendChild(host);
  const client = new QueryClient();
  act(() => {
    createRoot(host).render(
      <QueryClientProvider client={client}>
        <InCourse>
          <ExercisePlayer exerciseId="m01-ex-1" type={type} />
        </InCourse>
      </QueryClientProvider>,
    );
  });
  await clickButton(en.exercise.start);
}

const hasReportLink = () => [...host.querySelectorAll("button")].some((b) => b.textContent === en.report.link);

beforeEach(() => {
  document.body.innerHTML = "";
});

describe("the report link on a practice exercise", () => {
  it("is absent while the question is unanswered, and appears once it is answered", async () => {
    opened = QUIZ;
    await mount("quiz");
    expect(hasReportLink()).toBe(false);

    await act(async () => host.querySelector<HTMLInputElement>('input[type="radio"]')!.click());
    await clickButton(en.exercise.submit);
    expect(hasReportLink()).toBe(true);
  });

  it("is a red button in the same row as Try again, where a reader looks after answering", async () => {
    opened = QUIZ;
    await mount("quiz");
    await act(async () => host.querySelector<HTMLInputElement>('input[type="radio"]')!.click());
    await clickButton(en.exercise.submit);
    const buttons = [...host.querySelectorAll("button")];
    const report = buttons.find((b) => b.textContent === en.report.link)!;
    const tryAgain = buttons.find((b) => b.textContent === en.exercise.tryAgain)!;
    expect(report.parentElement).toBe(tryAgain.parentElement);
    expect(report.className).toContain("bg-red-600");
  });

  it("is never offered on a calculation, which is not a multiple-choice question", async () => {
    opened = CALCULATION;
    await mount("calculation");
    expect(hasReportLink()).toBe(false);
  });
});
