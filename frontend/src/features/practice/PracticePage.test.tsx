import { act } from "react";
import { createRoot } from "react-dom/client";
import { MemoryRouter, Route, Routes } from "react-router-dom";
import { QueryClient, QueryClientProvider } from "@tanstack/react-query";
import { afterEach, beforeEach, describe, expect, it, vi } from "vitest";
import en from "@/i18n/en.json";
import { InCourse } from "@/test/course";

/** A lesson's practice: a round of its questions, one at a time, the solution open after each answer. */

const opened: string[] = [];
const draws: boolean[] = [];

vi.mock("@/api/course", () => ({
  getLesson: async () => ({ id: "m01-l01", title: "La Constitución", practiceQuestions: 41 }),
  getCourse: async () => ({ course: { lessonNoun: "tema" }, blocks: [] }),
}));
vi.mock("@/api/practice", () => ({
  drawPracticeRound: async (_scope: unknown, lessonId: string, all: boolean) => {
    draws.push(all);
    return {
      lessonId,
      questions: [
        { exerciseId: "m01-l01-ex-1", questionId: "m01-l01-q001" },
        { exerciseId: "m01-l01-ex-2", questionId: "m01-l01-q030" },
      ],
    };
  },
}));
vi.mock("@/api/exercises", () => ({
  createAttempt: async (_scope: unknown, exerciseId: string, variantId: string) => {
    opened.push(`${exerciseId}/${variantId}`);
    return {
      attemptId: `attempt-${variantId}`,
      exerciseId,
      type: "quiz",
      prompt: `Pregunta ${variantId}`,
      payload: { kind: "single_choice", options: [{ id: "a", text: "Sí" }, { id: "b", text: "No" }] },
      state: "open",
    };
  },
  answerAttempt: async (_scope: unknown, attemptId: string) => ({
    attemptId,
    correct: true,
    correctAnswer: { optionId: "a", text: "Sí" },
    solutionSteps: [],
    explanation: "Porque lo dice el artículo 1.",
    lessonLink: null,
    excerpt: null,
    noExcerpt: null,
  }),
}));

function translate(key: string, params?: Record<string, unknown>): string {
  const lookup = (path: string): unknown =>
    path.split(".").reduce<unknown>((node, part) => (node as Record<string, unknown>)?.[part], en);
  const count = params?.count;
  const plural = typeof count === "number" ? lookup(`${key}_${count === 1 ? "one" : "other"}`) : undefined;
  const template = plural ?? lookup(key);
  if (typeof template !== "string") throw new Error(`missing catalog key ${key}`);
  return template.replace(/\{\{(\w+)\}\}/g, (_, name: string) => String(params?.[name]));
}
vi.mock("react-i18next", () => ({
  useTranslation: () => ({ t: translate, i18n: { resolvedLanguage: "en" } }),
  initReactI18next: { type: "3rdParty", init: () => {} },
}));

const { PracticePage } = await import("./PracticePage");
const { PracticeEntry } = await import("./PracticeEntry");

(globalThis as { IS_REACT_ACT_ENVIRONMENT?: boolean }).IS_REACT_ACT_ENVIRONMENT = true;

let host: HTMLDivElement;

async function settle(): Promise<void> {
  for (let i = 0; i < 5; i += 1) await act(async () => await new Promise((resolve) => setTimeout(resolve, 0)));
}

function button(name: string): HTMLButtonElement {
  const found = [...host.querySelectorAll("button")].find((b) => b.textContent?.trim() === name);
  if (!found) throw new Error(`no button ${name}`);
  return found;
}

async function answer(): Promise<void> {
  act(() => host.querySelector<HTMLInputElement>('input[type="radio"]')!.click());
  act(() => button(en.exercise.submit).click());
  await settle();
}

function render(element: React.ReactElement, at = "/courses/crypto-futures/lessons/m01-l01/practice") {
  const client = new QueryClient({ defaultOptions: { queries: { retry: false } } });
  act(() => {
    createRoot(host).render(
      <QueryClientProvider client={client}>
        <MemoryRouter initialEntries={[at]}>
          <InCourse>
            <Routes>
              <Route path="/courses/:course/lessons/:lessonId/practice" element={element} />
              <Route path="*" element={element} />
            </Routes>
          </InCourse>
        </MemoryRouter>
      </QueryClientProvider>,
    );
  });
}

beforeEach(() => {
  opened.length = 0;
  draws.length = 0;
  host = document.createElement("div");
  document.body.appendChild(host);
});

afterEach(() => {
  document.body.innerHTML = "";
});

describe("practising a lesson", () => {
  it("offers twenty at random by default, or all of the lesson's questions", async () => {
    render(<PracticePage />);
    await settle();
    expect(host.textContent).toContain(en.practice.twenty);
    expect(host.textContent).toContain("All (41)");
    act(() => button(en.practice.begin).click());
    await settle();
    expect(draws).toEqual([false]);
  });

  it("serves the round one question at a time, by its own id", async () => {
    render(<PracticePage />);
    await settle();
    act(() => button(en.practice.begin).click());
    await settle();
    expect(host.textContent).toContain("Question 1 of 2");
    expect(opened).toEqual(["m01-l01-ex-1/m01-l01-q001"]);
  });

  it("opens the solution after each answer, with the report link inside it", async () => {
    render(<PracticePage />);
    await settle();
    act(() => button(en.practice.begin).click());
    await settle();
    await answer();
    const details = host.querySelector("details");
    expect(details?.open).toBe(true);
    expect(details?.textContent).toContain("Porque lo dice el artículo 1.");
    expect(details?.textContent).toContain(en.report.link);
  });

  it("moves on to the next question and ends the round after the last", async () => {
    render(<PracticePage />);
    await settle();
    act(() => button(en.practice.begin).click());
    await settle();
    await answer();
    act(() => button(`${en.practice.next} →`).click());
    await settle();
    expect(opened).toEqual(["m01-l01-ex-1/m01-l01-q001", "m01-l01-ex-2/m01-l01-q030"]);
    await answer();
    act(() => button(en.practice.finish).click());
    expect(host.textContent).toContain(en.practice.done);
    expect(host.textContent).toContain(en.practice.again);
  });
});

describe("the way into practice", () => {
  it("shows nothing for a lesson without practice (crypto-futures keeps its embedded quizzes)", () => {
    render(<PracticeEntry lessonId="m01-l1" questions={undefined} />, "/x");
    expect(host.textContent).toBe("");
  });

  it("leads to the lesson's practice page", () => {
    render(<PracticeEntry lessonId="m01-l01" questions={41} />, "/x");
    expect(host.textContent).toContain("41 questions");
    expect(button(en.practice.entry)).toBeTruthy();
  });
});
