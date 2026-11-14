import { act } from "react";
import { createRoot } from "react-dom/client";
import { MemoryRouter, Route, Routes, useLocation } from "react-router-dom";
import { QueryClient, QueryClientProvider } from "@tanstack/react-query";
import { getAllByRole, getByRole, queryByRole, queryByText } from "@testing-library/dom";
import { afterEach, beforeEach, describe, expect, it, vi } from "vitest";
import en from "@/i18n/en.json";
import { InCourse } from "@/test/course";
import { clearViewport, setViewportWidth } from "@/test/viewport";

/** Requirements 6.6: the course page offers each practice preset, and each preset page draws its own round. */

let presets: string[] | undefined;
const draws: string[] = [];

function lesson(id: string, practiceQuestions: number) {
  return { id, order: 1, title: `Lesson ${id}`, summary: "", completed: false, readingSeconds: 60, exercises: [], practiceQuestions };
}

function module(id: string, lessons: ReturnType<typeof lesson>[]) {
  return {
    id,
    order: 1,
    title: `Module ${id}`,
    summary: "",
    assumes: [],
    unmetPrereqs: [],
    hasContent: true,
    lessonsTotal: lessons.length,
    lessonsCompleted: 0,
    exercisesTotal: lessons.length,
    exercisesPassed: 0,
    lessons,
  };
}

vi.mock("@/api/course", () => ({
  getCourse: async () => ({
    locale: "en",
    started: false,
    course: {
      id: "backend-in-depth",
      title: "Backend Engineering in Depth",
      subtitle: "",
      description: "",
      lessonPractice: true,
      practiceScheduler: "spaced",
      psicotecnicos: [{ generator: "quorum-reads", exerciseId: "gen:quorum-reads", title: "Quorums" }],
      ...(presets ? { practicePresets: presets } : {}),
    },
    blocks: [
      {
        id: "block-a",
        order: 1,
        title: "About this course",
        modules: [module("m00", [lesson("m00-l01", 0)])],
      },
      {
        id: "block-b",
        order: 2,
        title: "Languages",
        modules: [module("m01", [lesson("m01-l01", 30), lesson("m01-l02", 24)])],
      },
    ],
  }),
  getModule: async () => ({
    id: "m01",
    title: "Module m01",
    summary: "",
    assumes: [],
    unmetPrereqs: [],
    lessons: [
      { id: "m01-l01", order: 1, title: "Lesson m01-l01", completed: false, readingSeconds: 60, practiceQuestions: 30 },
      { id: "m01-l02", order: 2, title: "Lesson m01-l02", completed: false, readingSeconds: 60, practiceQuestions: 24 },
    ],
  }),
}));
vi.mock("@/api/practice", () => ({
  drawModuleRound: async (_scope: unknown, moduleId: string, all: boolean) => {
    draws.push(`module ${moduleId} all=${all}`);
    return { questions: [{ exerciseId: "m01-l01-ex-1", questionId: "m01-l01-q01" }] };
  },
  drawCourseRound: async (_scope: unknown, preset: string, count: number) => {
    draws.push(`${preset} ${count}`);
    return { questions: [{ exerciseId: "m01-l01-ex-1", questionId: "m01-l01-q28" }] };
  },
}));
vi.mock("@/api/exercises", () => ({
  createAttempt: async (_scope: unknown, exerciseId: string, variantId: string) => ({
    attemptId: `attempt-${variantId}`,
    exerciseId,
    type: "quiz",
    prompt: `Question ${variantId}`,
    payload: { kind: "single_choice", options: [{ id: "a", text: "Yes" }] },
    state: "open",
  }),
  answerAttempt: vi.fn(),
}));
vi.mock("@/features/pdfExport/useExportPdf", () => ({
  useExportPdf: () => ({ open: () => undefined, dialog: null }),
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

const { CoursePage } = await import("@/features/course/CoursePage");
const { ModulePracticePage } = await import("./ModulePracticePage");
const { CoursePracticePage } = await import("./CoursePracticePage");

(globalThis as { IS_REACT_ACT_ENVIRONMENT?: boolean }).IS_REACT_ACT_ENVIRONMENT = true;

let host: HTMLDivElement;

function Here() {
  return <p data-testid="location">{useLocation().pathname}</p>;
}

async function settle(): Promise<void> {
  for (let i = 0; i < 5; i += 1) await act(async () => await new Promise((resolve) => setTimeout(resolve, 0)));
}

async function render(at: string): Promise<void> {
  const client = new QueryClient({ defaultOptions: { queries: { retry: false } } });
  act(() => {
    createRoot(host).render(
      <QueryClientProvider client={client}>
        <MemoryRouter initialEntries={[at]}>
          <InCourse>
            <Routes>
              <Route path="/courses/:course" element={<CoursePage />} />
              <Route path="/courses/:course/modules/:moduleId/practice" element={<ModulePracticePage />} />
              <Route path="/courses/:course/practice/review" element={<CoursePracticePage preset="review" />} />
              <Route
                path="/courses/:course/practice/code-reading"
                element={<CoursePracticePage preset="code-reading" />}
              />
              <Route path="*" element={<Here />} />
            </Routes>
          </InCourse>
        </MemoryRouter>
      </QueryClientProvider>,
    );
  });
  await settle();
}

async function click(element: HTMLElement): Promise<void> {
  act(() => element.click());
  await settle();
}

function location(): string {
  return host.querySelector('[data-testid="location"]')?.textContent ?? "";
}

const COURSE = "/courses/crypto-futures";
const ALL = ["lesson", "module", "review", "code-reading", "generators"];

beforeEach(() => {
  presets = ALL;
  draws.length = 0;
  host = document.createElement("div");
  document.body.appendChild(host);
});

afterEach(() => {
  document.body.innerHTML = "";
  clearViewport();
});

describe.each([390, 1280])("the course page's practice presets at %i px", (width) => {
  beforeEach(() => setViewportWidth(width));

  it("offers the five presets in the declared order", async () => {
    await render(COURSE);
    const card = getByRole(host, "heading", { name: en.practicePresets.title }).closest("div")!.parentElement!;
    expect(getAllByRole(card, "button").map((b) => b.textContent)).toEqual([
      en.practicePresets.lesson,
      en.practicePresets.module,
      en.practicePresets.review,
      en.practicePresets.codeReading,
      en.practicePresets.generators,
    ]);
  });

  it.each([en.practicePresets.review, en.practicePresets.codeReading])("opens %s directly", async (label) => {
    await render(COURSE);
    await click(getByRole(host, "button", { name: label }));
    expect(getByRole(host, "heading", { level: 1 }).textContent).toBe(label);
  });

  it("opens the generators' page directly", async () => {
    await render(COURSE);
    await click(getByRole(host, "button", { name: en.practicePresets.generators }));
    expect(location()).toBe(`${COURSE}/practice/psicotecnicos`);
  });

  it("asks which lesson, offering only lessons with questions, and opens its practice", async () => {
    await render(COURSE);
    await click(getByRole(host, "button", { name: en.practicePresets.lesson }));
    const picker = getByRole(host, "combobox", { name: en.practicePresets.chooseLesson });
    expect([...picker.querySelectorAll("option")].map((o) => o.value)).toEqual(["m01-l01", "m01-l02"]);
    act(() => {
      (picker as HTMLSelectElement).value = "m01-l02";
      picker.dispatchEvent(new Event("change", { bubbles: true }));
    });
    await click(getByRole(host, "button", { name: en.practicePresets.start }));
    expect(location()).toBe(`${COURSE}/lessons/m01-l02/practice`);
  });

  it("asks which module, offering only modules with questions, and draws that module's round", async () => {
    await render(COURSE);
    await click(getByRole(host, "button", { name: en.practicePresets.module }));
    const picker = getByRole(host, "combobox", { name: en.practicePresets.chooseModule });
    expect([...picker.querySelectorAll("option")].map((o) => o.value)).toEqual(["m01"]);
    await click(getByRole(host, "button", { name: en.practicePresets.start }));
    expect(getByRole(host, "heading", { level: 1 }).textContent).toBe("Practise: Module m01");
    expect(queryByText(host, "All (54)")).toBeTruthy();
    await click(getByRole(host, "button", { name: en.practice.begin }));
    expect(draws).toEqual(["module m01 all=false"]);
  });
});

describe("a course without presets", () => {
  it("keeps the card it had and shows no presets", async () => {
    presets = undefined;
    await render(COURSE);
    expect(queryByRole(host, "heading", { name: en.practicePresets.title })).toBeNull();
    expect(queryByText(host, en.psicotecnicos.entry)).toBeTruthy();
  });
});

describe("the course-wide presets", () => {
  it.each([
    ["review", en.practicePresets.reviewLead],
    ["code-reading", en.practicePresets.codeReadingLead],
  ])("%s draws twenty questions, ordered by the scheduler", async (preset, lead) => {
    await render(`${COURSE}/practice/${preset}`);
    expect(host.textContent).toContain(`${lead} ${en.practice.introSpaced}`);
    await click(getByRole(host, "button", { name: en.practice.begin }));
    expect(draws).toEqual([`${preset} 20`]);
    expect(host.textContent).toContain("Question 1 of 1");
  });
});
