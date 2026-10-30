import { act } from "react";
import { createRoot } from "react-dom/client";
import { MemoryRouter, Route, Routes } from "react-router-dom";
import { beforeEach, describe, expect, it, vi } from "vitest";
import en from "@/i18n/en.json";
import type { NoExcerpt, SolutionExcerpt } from "@/api/exercises";
import type { ExamSession } from "@/api/exams";
import { InCourse } from "@/test/course";

/** «Ver solución» (delta F1, F5, F6): what it holds, in what order, and where it never appears. */

const EXCERPT: SolutionExcerpt = {
  heading: "Art. 122.1 LPAC",
  text: "1. El plazo para la interposición del recurso de alzada será de un mes, si el acto fuera expreso.",
  full: "Artículo 122. Plazos.\n\n1. El plazo … un mes …\n\n2. El plazo máximo para dictar y notificar la resolución será de tres meses.",
  fullTooLong: false,
  href: "/api/courses/fixture-oposiciones/sources/normativa/lpac-extracto.html#a1-22",
  attribution: null,
};

const TREE = {
  course: { lessonNoun: "tema" },
  blocks: [{ modules: [{ lessons: [{ id: "m01-l1", order: 3, title: "El recurso de alzada" }] }] }],
};

let openExam: ExamSession | null = null;
vi.mock("@tanstack/react-query", () => ({
  useQuery: ({ queryKey }: { queryKey: unknown[] }) =>
    queryKey[0] === "exam" ? { data: openExam, isLoading: false, isError: false } : { data: TREE, isLoading: false },
  useMutation: () => ({ mutate: () => {}, isPending: false }),
  useQueryClient: () => ({ invalidateQueries: () => {}, setQueryData: () => {} }),
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

const { SolutionPanel } = await import("@/features/exercises/SolutionPanel");
const { ExamRunner } = await import("@/features/exams/ExamRunner");

(globalThis as { IS_REACT_ACT_ENVIRONMENT?: boolean }).IS_REACT_ACT_ENVIRONMENT = true;

let host: HTMLDivElement;

function render(node: React.ReactNode, at = "/"): void {
  host = document.createElement("div");
  document.body.appendChild(host);
  act(() => {
    createRoot(host).render(
      <MemoryRouter initialEntries={[at]}>
        <InCourse>{node}</InCourse>
      </MemoryRouter>,
    );
  });
}

function panel(excerpt: SolutionExcerpt | null, noExcerpt: NoExcerpt | null = null): void {
  render(
    <SolutionPanel
      attemptId="attempt-1"
      correct={false}
      correctAnswer={{ optionId: "a", text: "Un mes." }}
      solutionSteps={[]}
      explanation="El artículo 122.1 fija un mes."
      excerpt={excerpt}
      noExcerpt={noExcerpt}
      lessonLink={{ lessonId: "m01-l1", anchor: "boe-a-2015-10565-art-122", citation: "art. 122.1 LPAC" }}
      reportable
    />,
  );
}

function details(): HTMLDetailsElement {
  const found = host.querySelector("details");
  if (!found) throw new Error("no panel");
  return found;
}

beforeEach(() => {
  document.body.innerHTML = "";
  openExam = null;
});

describe("the solution panel", () => {
  it("starts collapsed under the verdict, labelled «See the solution»", () => {
    panel(EXCERPT);
    expect(host.textContent).toContain(en.exercise.incorrect);
    expect(details().open).toBe(false);
    expect(details().querySelector("summary")).toHaveTextContent(en.solution.show);
  });

  it("holds the answer, the explanation, the norm's text, the links and the report, in that order", () => {
    panel(EXCERPT);
    const text = details().textContent ?? "";
    const order = [
      "Un mes.",
      "El artículo 122.1 fija un mes.",
      "Art. 122.1 LPAC",
      "1. El plazo para la interposición",
      "Tema 3: El recurso de alzada",
      en.solution.source,
      en.report.link,
    ].map((needle) => text.indexOf(needle));
    expect(order.every((at) => at >= 0)).toBe(true);
    expect([...order].sort((a, b) => a - b)).toEqual(order);
    const links = [...details().querySelectorAll("a")];
    expect(links.find((a) => a.textContent === "Tema 3: El recurso de alzada")?.getAttribute("href")).toBe(
      "/courses/crypto-futures/lessons/m01-l1#boe-a-2015-10565-art-122",
    );
    expect(links.find((a) => a.textContent === en.solution.source)?.getAttribute("href")).toBe(EXCERPT.href);
  });

  it("opens the whole article in place, and back", () => {
    panel(EXCERPT);
    const toggle = [...details().querySelectorAll("button")].find((b) => b.textContent === en.solution.showFull)!;
    act(() => toggle.click());
    expect(details().textContent).toContain("2. El plazo máximo para dictar");
    expect(toggle.textContent).toBe(en.solution.showExcerpt);
  });

  it("sends an article too long to show to its source instead", () => {
    panel({ ...EXCERPT, full: null, fullTooLong: true });
    const whole = [...details().querySelectorAll("a")].find((a) => a.textContent === en.solution.showFull);
    expect(whole?.getAttribute("href")).toBe(EXCERPT.href);
  });

  it("names a saved page with its title and date", () => {
    panel({ ...EXCERPT, heading: "Recursos administrativos", attribution: "Guía de recursos, consultado el 2026-10-28" });
    expect(details().textContent).toContain("Guía de recursos, consultado el 2026-10-28");
    expect([...details().querySelectorAll("a")].some((a) => a.textContent === en.solution.savedPage)).toBe(true);
  });

  it("says why a question of a course with norms has no excerpt, and keeps the rest", () => {
    panel(null, { reason: "no-match", href: "/api/courses/x/sources/otros/pagina.html" });
    const text = details().textContent ?? "";
    expect(text).toContain(translate("solution.noExcerpt", { reason: en.noExcerptReason["no-match"] }));
    expect(text).toContain("El artículo 122.1 fija un mes.");
    expect([...details().querySelectorAll("a")].some((a) => a.textContent === "Tema 3: El recurso de alzada")).toBe(true);
    expect([...details().querySelectorAll("button")].some((b) => b.textContent === en.report.link)).toBe(true);
    expect([...details().querySelectorAll("a")].find((a) => a.textContent === en.solution.savedPage)?.getAttribute("href")).toBe(
      "/api/courses/x/sources/otros/pagina.html",
    );
    expect(details().querySelector("figure")).toBeNull();
  });

  it("shows the explanation only in a course without norms", () => {
    panel(null);
    expect(details().querySelector("figure")).toBeNull();
    expect(details().textContent).toContain("El artículo 122.1 fija un mes.");
    expect([...details().querySelectorAll("a")].some((a) => a.textContent === en.solution.source)).toBe(false);
    expect(details().textContent).not.toContain("No excerpt");
  });
});

describe("an exam that is still running", () => {
  it("never shows the panel, whatever the question carries", () => {
    openExam = {
      id: "exam-1",
      presetId: "simulacro",
      presetVersion: 1,
      presetTitle: "Simulacro",
      target: null,
      targetTitle: null,
      status: "open",
      createdAt: "2026-10-28T09:00:00Z",
      finishedAt: null,
      deadline: null,
      pause: "between-questions",
      paused: false,
      activeSeconds: 300,
      serverNow: "2026-10-28T09:05:00Z",
      parts: [
        { id: "parte-1", title: "Part one", kind: "questions", counted: 1, reserve: 0, choose: null, penalty: "1/3", cases: [], marked: [] },
      ],
      result: null,
      byLesson: null,
      questions: [
        {
          index: 0,
          attemptId: "attempt-1",
          moduleId: "m01",
          moduleTitle: "Appeals",
          blockId: "block-a",
          blockTitle: "Procedure",
          exerciseId: "m01-ex-2",
          type: "quiz",
          prompt: "¿Plazo de la alzada?",
          payload: { kind: "single_choice", options: [{ id: "a", text: "Un mes." }] },
          answered: true,
          givenAnswer: { optionId: "a" },
          partId: "parte-1",
          lessonId: "m01-l1",
          questionId: null,
          reserve: false,
          lessonAnchor: null,
          citation: null,
          excerpt: EXCERPT,
          isCorrect: null,
          unanswered: null,
          correctAnswer: null,
          solutionSteps: [],
          explanation: null,
        },
      ],
    };
    render(
      <Routes>
        <Route path="/courses/:course/exams/:examId" element={<ExamRunner />} />
      </Routes>,
      "/courses/crypto-futures/exams/exam-1",
    );
    expect(host.textContent).toContain("¿Plazo de la alzada?");
    expect(host.querySelector("details")).toBeNull();
    expect(host.textContent).not.toContain(en.solution.show);
    expect(host.textContent).not.toContain(EXCERPT.heading);
  });
});
