import { act } from "react";
import { createRoot } from "react-dom/client";
import { MemoryRouter } from "react-router-dom";
import { QueryClient, QueryClientProvider } from "@tanstack/react-query";
import { beforeEach, describe, expect, it, vi } from "vitest";
import en from "@/i18n/en.json";
import { InCourse } from "@/test/course";

/** A case in practice (delta B2): the scenario in view, its questions in order, each graded on its own. */

const options = [
  { id: "a", text: "One month." },
  { id: "b", text: "Three months." },
];
const CASE = {
  exerciseId: "m02-ex-3",
  title: "The refused leave",
  scenario: "A civil servant receives an express decision that refuses a leave.",
  questions: [1, 2, 3].map((n) => ({
    attemptId: `attempt-${n}`,
    questionId: `q0${n}`,
    lessonId: "m02-l1",
    prompt: `Question ${n} about the case.`,
    payload: { kind: "single_choice", options },
  })),
};

const answered: string[] = [];
vi.mock("@/api/exercises", () => ({
  openCase: async () => CASE,
  answerAttempt: async (_scope: unknown, attemptId: string) => {
    answered.push(attemptId);
    return {
      attemptId,
      correct: true,
      correctAnswer: { optionId: "a", text: "One month." },
      solutionSteps: [],
      explanation: null,
      lessonLink: { lessonId: "m02-l1", anchor: "lpac-art-122", citation: "art. 122.1 LPAC" },
    };
  },
}));

function translate(key: string, params?: Record<string, unknown>): string {
  const template = key.split(".").reduce<unknown>((node, part) => (node as Record<string, unknown>)?.[part], en);
  if (typeof template !== "string") return key;
  return template.replace(/\{\{(\w+)\}\}/g, (_, name: string) => String(params?.[name]));
}
vi.mock("react-i18next", () => ({
  useTranslation: () => ({ t: translate, i18n: { resolvedLanguage: "en", language: "en" } }),
  initReactI18next: { type: "3rdParty", init: () => {} },
}));

const { CaseExercise } = await import("@/features/exercises/CaseExercise");

(globalThis as { IS_REACT_ACT_ENVIRONMENT?: boolean }).IS_REACT_ACT_ENVIRONMENT = true;

let host: HTMLDivElement;

async function settle(): Promise<void> {
  await act(async () => {
    await new Promise((resolve) => setTimeout(resolve, 0));
  });
}

function buttons(label: string): HTMLButtonElement[] {
  return [...host.querySelectorAll("button")].filter((b) => b.textContent === label);
}

async function click(element: HTMLElement): Promise<void> {
  await act(async () => element.click());
  await settle();
}

function questionItems(): HTMLLIElement[] {
  return [...host.querySelectorAll("ol > li")] as HTMLLIElement[];
}

function radios(item: HTMLElement): HTMLInputElement[] {
  return [...item.querySelectorAll<HTMLInputElement>('input[type="radio"]')];
}

async function open(): Promise<void> {
  host = document.createElement("div");
  document.body.appendChild(host);
  act(() => {
    createRoot(host).render(
      <QueryClientProvider client={new QueryClient()}>
        <MemoryRouter>
          <InCourse>
            <CaseExercise exerciseId="m02-ex-3" />
          </InCourse>
        </MemoryRouter>
      </QueryClientProvider>,
    );
  });
  await click(buttons(en.exercise.startCase)[0]);
}

beforeEach(() => {
  document.body.innerHTML = "";
  answered.length = 0;
});

describe("a case in practice", () => {
  it("shows the scenario first, kept open, then every question in order", async () => {
    await open();
    const scenario = host.querySelector("details");
    expect(scenario).not.toBeNull();
    expect(scenario!.open).toBe(true);
    expect(scenario).toHaveTextContent(CASE.scenario);
    expect(questionItems().map((item) => item.textContent?.match(/Question \d/)?.[0])).toEqual([
      "Question 1",
      "Question 2",
      "Question 3",
    ]);
  });

  it("keeps one question's choice when another question is answered beside it", async () => {
    await open();
    const [first, second] = questionItems();
    await click(radios(first)[0]);
    await click(radios(second)[1]);
    // Every question used to share one radio group, so choosing in the second cleared the first.
    expect(radios(first)[0].checked).toBe(true);
    expect(radios(second)[1].checked).toBe(true);
  });

  it("grades each question on its own and links it to the paragraph that cites its article", async () => {
    await open();
    const [first] = questionItems();
    await click(radios(first)[0]);
    await click(buttons(en.exercise.submit)[0]);
    expect(answered).toEqual(["attempt-1"]);

    const link = [...questionItems()[0].querySelectorAll("a")].find((a) => a.textContent === en.exercise.viewInLesson);
    expect(link?.getAttribute("href")).toBe("/courses/crypto-futures/lessons/m02-l1#lpac-art-122");
    expect(questionItems()[0]).toHaveTextContent("art. 122.1 LPAC");
    expect(buttons(en.report.link)).toHaveLength(1);
    expect(host.querySelector('[role="status"]')).toHaveTextContent(translate("exercise.caseProgress", { done: 1, total: 3 }));
  });

  it("is done when every question is answered", async () => {
    await open();
    for (const item of questionItems()) {
      await click(radios(item)[0]);
      await click(buttons(en.exercise.submit)[0]);
    }
    expect(answered).toEqual(["attempt-1", "attempt-2", "attempt-3"]);
    expect(host.querySelector('[role="status"]')).toHaveTextContent(en.exercise.caseDone);
  });
});
