import { act } from "react";
import { createRoot } from "react-dom/client";
import { MemoryRouter, Route, Routes } from "react-router-dom";
import { QueryClient, QueryClientProvider } from "@tanstack/react-query";
import { afterEach, beforeEach, describe, expect, it, vi } from "vitest";
import en from "@/i18n/en.json";
import { InCourse } from "@/test/course";

/** A lesson's practice: a round of its questions, one at a time, the solution open after each answer. */

const opened: string[] = [];
let attemptCounter = 0;

vi.mock("@/api/course", () => ({
  getLesson: async () => ({ id: "m01-l1", title: "Lost updates", practiceQuestions: 3 }),
  getCourse: async () => ({ course: {}, blocks: [] }),
}));
vi.mock("@/api/practice", () => ({
  drawPracticeRound: async (_scope: unknown, lessonId: string) => ({
    lessonId,
    questions: [
      { exerciseId: "m01-ex-1", questionId: "iso-a" },
      { exerciseId: "gen:capacity-estimation", questionId: "" },
      { exerciseId: "gen:capacity-estimation", questionId: "" },
    ],
  }),
}));
vi.mock("@/api/exercises", () => ({
  createAttempt: async (_scope: unknown, exerciseId: string, variantId?: string) => {
    opened.push(`${exerciseId}/${variantId ?? "seed"}`);
    attemptCounter += 1;
    return {
      attemptId: `attempt-${attemptCounter}`,
      questionId: variantId ?? `seed-${attemptCounter}`,
      exerciseId,
      type: "quiz",
      prompt: `Question ${attemptCounter}`,
      payload: { kind: "single_choice", options: [{ id: "a", text: "Sí" }, { id: "b", text: "No" }] },
      state: "open",
    };
  },
  answerAttempt: async (_scope: unknown, attemptId: string) => ({
    attemptId,
    correct: true,
    correctAnswer: { optionId: "a", text: "Sí" },
    solutionSteps: [],
    explanation: "Because the lesson says so.",
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


function render(element: React.ReactElement, at = "/courses/fixture-familias/lessons/m01-l1/practice") {
  const client = new QueryClient({ defaultOptions: { queries: { retry: false } } });
  act(() => {
    createRoot(host).render(
      <QueryClientProvider client={client}>
        <MemoryRouter initialEntries={[at]}>
          <InCourse>
            <Routes>
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
  attemptCounter = 0;
  host = document.createElement("div");
  document.body.appendChild(host);
});

afterEach(() => {
  document.body.innerHTML = "";
});

describe("a practice set that mixes stored and generated questions", () => {
  it("opens a stored question by its id and a generated one by the seed the server draws", async () => {
    render(<PracticePage />);
    await settle();
    act(() => button(en.practice.begin).click());
    await settle();
    expect(opened).toEqual(["m01-ex-1/iso-a"]);
    await answer();
    act(() => button(`${en.practice.next} →`).click());
    await settle();
    expect(opened).toEqual(["m01-ex-1/iso-a", "gen:capacity-estimation/seed"]);
  });

  it("opens each of two generated questions in a row as its own attempt, with no report link on them", async () => {
    render(<PracticePage />);
    await settle();
    act(() => button(en.practice.begin).click());
    await settle();
    await answer();
    act(() => button(`${en.practice.next} →`).click());
    await settle();
    await answer();
    expect(host.querySelector("details")?.textContent).not.toContain(en.report.link);
    act(() => button(`${en.practice.next} →`).click());
    await settle();
    expect(host.textContent).toContain("Question 3 of 3");
    expect(opened).toEqual(["m01-ex-1/iso-a", "gen:capacity-estimation/seed", "gen:capacity-estimation/seed"]);
  });
});

describe("the lesson page's entry to practice", () => {
  const families = [
    { id: "capacity-estimation", title: "Capacity estimation" },
    { id: "loop-complexity", title: "Loop complexity" },
  ];

  it("names the generated families that practise the lesson", () => {
    render(<PracticeEntry to="/lessons/m01-l1/practice" questions={7} families={families} />, "/x");
    expect(host.textContent).toContain("Capacity estimation, Loop complexity");
  });

  it("still opens for a lesson whose only practice is generated", () => {
    render(<PracticeEntry to="/lessons/m01-l1/practice" questions={undefined} families={families} />, "/x");
    expect(button(en.practice.entry)).toBeTruthy();
  });
});
