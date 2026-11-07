import { act } from "react";
import { createRoot } from "react-dom/client";
import { MemoryRouter, Route, Routes } from "react-router-dom";
import { QueryClient, QueryClientProvider } from "@tanstack/react-query";
import { afterEach, beforeEach, describe, expect, it, vi } from "vitest";
import en from "@/i18n/en.json";
import { InCourse } from "@/test/course";

/** «Psicotécnicos» practice: a round of generated items by type or all, timed or not, the rule after each answer. */

const opened: string[] = [];
const draws: { count: number; generator?: string }[] = [];

vi.mock("@/api/course", () => ({
  getCourse: async () => ({
    course: {
      lessonNoun: "tema",
      psicotecnicos: [
        { generator: "calculo-ecuaciones", exerciseId: "gen:calculo-ecuaciones", title: "Ecuaciones" },
        { generator: "tablas-lectura", exerciseId: "gen:tablas-lectura", title: "Lectura de tablas" },
      ],
    },
    blocks: [],
  }),
}));
vi.mock("@/api/practice", () => ({
  drawPsicotecnicoRound: async (_scope: unknown, count: number, generator?: string) => {
    draws.push({ count, generator });
    return { exerciseIds: ["gen:tablas-lectura", "gen:calculo-ecuaciones"] };
  },
}));
vi.mock("@/api/exercises", () => ({
  createAttempt: async (_scope: unknown, exerciseId: string) => {
    opened.push(exerciseId);
    return {
      attemptId: `attempt-${opened.length}`,
      exerciseId,
      questionId: `${exerciseId}:123`,
      type: "psicotecnico",
      prompt: `Pregunta de ${exerciseId}`,
      payload: {
        kind: "single_choice",
        options: [{ id: "o0", text: "3" }, { id: "o1", text: "4" }],
        ...(exerciseId === "gen:tablas-lectura"
          ? { table: { title: "Préstamos", header: ["Título", "Año"], rows: [["Aranmanoth", "2000"], ["Entre visillos", "1998"]] } }
          : {}),
      },
      state: "open",
    };
  },
  answerAttempt: async (_scope: unknown, attemptId: string) => ({
    attemptId,
    correct: true,
    correctAnswer: { optionId: "o0", text: "3" },
    solutionSteps: [],
    explanation: "x = 6 / 2 = 3.",
    lessonLink: null,
    excerpt: null,
    noExcerpt: null,
  }),
}));

function translate(key: string, params?: Record<string, unknown>): string {
  const template = key
    .split(".")
    .reduce<unknown>((node, part) => (node as Record<string, unknown>)?.[part], en);
  if (typeof template !== "string") throw new Error(`missing catalog key ${key}`);
  return template.replace(/\{\{(\w+)\}\}/g, (_, name: string) => String(params?.[name]));
}
vi.mock("react-i18next", () => ({
  useTranslation: () => ({ t: translate, i18n: { resolvedLanguage: "en" } }),
  initReactI18next: { type: "3rdParty", init: () => {} },
}));

const { PsicotecnicoPracticePage } = await import("./PsicotecnicoPracticePage");

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

function render() {
  const client = new QueryClient({ defaultOptions: { queries: { retry: false } } });
  act(() => {
    createRoot(host).render(
      <QueryClientProvider client={client}>
        <MemoryRouter initialEntries={["/courses/age-auxiliar-c2/practice/psicotecnicos"]}>
          <InCourse>
            <Routes>
              <Route path="*" element={<PsicotecnicoPracticePage />} />
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

describe("practising psicotécnicos", () => {
  it("offers every type in the exam's weights, or one type", async () => {
    render();
    await settle();
    const options = [...host.querySelectorAll("option")].map((o) => o.textContent);
    expect(options).toEqual([en.psicotecnicos.allTypes, "Ecuaciones", "Lectura de tablas"]);
    act(() => button(en.practice.begin).click());
    await settle();
    expect(draws).toEqual([{ count: 20, generator: undefined }]);
  });

  it("draws the chosen type", async () => {
    render();
    await settle();
    const select = host.querySelector("select")!;
    act(() => {
      select.value = "calculo-ecuaciones";
      select.dispatchEvent(new Event("change", { bubbles: true }));
    });
    act(() => button(en.practice.begin).click());
    await settle();
    expect(draws).toEqual([{ count: 20, generator: "calculo-ecuaciones" }]);
  });

  it("opens each generated item as an attempt and shows its table above the options", async () => {
    render();
    await settle();
    act(() => button(en.practice.begin).click());
    await settle();
    expect(opened).toEqual(["gen:tablas-lectura"]);
    const table = host.querySelector("table")!;
    expect(table.querySelector("caption")?.textContent).toBe("Préstamos");
    expect([...table.querySelectorAll("th")].map((c) => c.textContent)).toEqual(["Título", "Año"]);
    expect(host.textContent).toContain("Question 1 of 2");
  });

  it("opens the rule after each answer with the item's stable id, and ends the round with the score", async () => {
    render();
    await settle();
    act(() => button(en.practice.begin).click());
    await settle();
    await answer();
    const details = host.querySelector("details");
    expect(details?.open).toBe(true);
    expect(details?.textContent).toContain("x = 6 / 2 = 3.");
    expect(details?.textContent).toContain("gen:tablas-lectura:123");
    expect(details?.textContent).not.toContain(en.report.link);
    act(() => button(`${en.practice.next} →`).click());
    await settle();
    await answer();
    act(() => button(en.practice.finish).click());
    expect(host.querySelector('[role="status"]')?.textContent).toContain("2 of 2 correct");
  });

  it("counts down a timed round and ends it when the time is up", async () => {
    vi.useFakeTimers({ shouldAdvanceTime: true });
    try {
      render();
      await settle();
      act(() => host.querySelector<HTMLInputElement>('input[type="checkbox"]')!.click());
      act(() => button(en.practice.begin).click());
      await settle();
      expect(host.textContent).toContain("01:40 / 01:40");
      await act(async () => {
        vi.advanceTimersByTime(101_000);
      });
      expect(host.querySelector('[role="status"]')?.textContent).toContain("0 of 2 correct");
    } finally {
      vi.useRealTimers();
    }
  });
});
