import { act } from "react";
import { createRoot } from "react-dom/client";
import { MemoryRouter, Route, Routes } from "react-router-dom";
import { beforeEach, describe, expect, it, vi } from "vitest";
import en from "@/i18n/en.json";
import type { ExamSession } from "@/api/exams";
import type { LessonTable } from "@/api/stats";
import { InCourse } from "@/test/course";

/** The results page of a submitted exam (delta A4, C1, D1–D3). */

const ROW = { correct: 0, wrong: 0, blank: 0 };
const TABLE: LessonTable = {
  threshold: 3,
  groups: [
    {
      moduleId: "m01",
      title: "Appeals",
      questions: 9,
      correct: 5,
      wrong: 2,
      blank: 2,
      pct: 0.5556,
      lessons: [
        { lessonId: "m01-l1", title: "The ordinary appeal", questions: 5, correct: 4, wrong: 1, blank: 0, pct: 0.8 },
        { lessonId: "m01-l2", title: "The reconsideration appeal", questions: 4, correct: 1, wrong: 1, blank: 2, pct: 0.25 },
      ],
    },
    {
      moduleId: "m02",
      title: "Competence",
      questions: 3,
      correct: 2,
      wrong: 1,
      blank: 0,
      pct: 0.6667,
      lessons: [{ lessonId: "m02-l1", title: "Delegation", questions: 3, correct: 2, wrong: 1, blank: 0, pct: 0.6667 }],
    },
  ],
  lists: {
    level: "lesson",
    best: [{ lessonId: "m01-l1", title: "The ordinary appeal", questions: 5, correct: 4, wrong: 1, blank: 0, pct: 0.8 }],
    worst: [{ lessonId: "m01-l2", title: "The reconsideration appeal", questions: 4, correct: 1, wrong: 1, blank: 2, pct: 0.25 }],
  },
};

function question(index: number, extra: Partial<ExamSession["questions"][number]> = {}): ExamSession["questions"][number] {
  return {
    index,
    attemptId: `attempt-${index}`,
    moduleId: "m01",
    moduleTitle: "Appeals",
    blockId: "block-a",
    blockTitle: "Procedure",
    exerciseId: "m01-ex-2",
    type: "quiz",
    prompt: `Question ${index}`,
    payload: { kind: "single_choice", options: [{ id: "a", text: "One month." }] },
    answered: true,
    givenAnswer: { optionId: "a" },
    partId: "parte-1",
    lessonId: "m01-l1",
    questionId: null,
    reserve: false,
    lessonAnchor: "lpac-art-122",
    citation: "art. 122.1 LPAC",
    isCorrect: true,
    unanswered: false,
    correctAnswer: { optionId: "a", text: "One month." },
    solutionSteps: [],
    explanation: null,
    ...extra,
  };
}

const SIMULACRO: ExamSession = {
  id: "exam-1",
  presetId: "simulacro",
  presetVersion: 1,
  presetTitle: "Simulacro",
  target: null,
  targetTitle: null,
  status: "submitted",
  createdAt: "2026-10-18T09:00:00Z",
  finishedAt: "2026-10-18T10:30:00Z",
  deadline: "2026-10-18T10:40:00Z",
  pause: "never",
  paused: false,
  activeSeconds: 5400,
  serverNow: "2026-10-18T10:30:00Z",
  parts: [
    { id: "parte-1", title: "Part one", kind: "questions", counted: 70, reserve: 2, choose: null, penalty: "1/3", cases: [], marked: [] },
    {
      id: "parte-2",
      title: "Part two",
      kind: "cases",
      counted: 20,
      reserve: 0,
      choose: 2,
      penalty: "1/3",
      cases: [{ exerciseId: "m02-ex-3", title: "The refused leave", scenario: "…" }],
      marked: [],
    },
  ],
  result: {
    score: 0.6,
    correct: 42,
    total: 70,
    blocks: [],
    modules: [],
    parts: [
      { id: "parte-1", graded: true, reason: null, case: null, correct: 50, wrong: 12, blank: 8, questions: 70, raw: 46, transformed: 32.8571, max: 50, passed: true, activeSeconds: 1800 },
      { id: "parte-2", graded: false, reason: "no-case-marked", case: null },
    ],
    raw: 46,
    transformed: 32.8571,
    max: 100,
    totalActiveSeconds: 1800,
  },
  byLesson: TABLE,
  questions: [
    question(0, { timeSeconds: 45 }),
    question(1, { reserve: true }),
    question(2, { partId: "parte-2", exerciseId: "m02-ex-3", questionId: "q01", lessonId: "m02-l1", lessonAnchor: "lrjsp-art-9", citation: "art. 9.1 LRJSP" }),
  ],
};

let exam: ExamSession = SIMULACRO;
vi.mock("@tanstack/react-query", () => ({
  useQuery: ({ queryKey }: { queryKey: unknown[] }) => {
    if (queryKey.at(-1) === "review") return { data: exam, isLoading: false, isError: false };
    return { data: { course: { lessonNoun: "tema" }, blocks: [] }, isLoading: false };
  },
  useMutation: () => ({ mutate: () => {}, isPending: false }),
}));

function translate(key: string, params?: Record<string, unknown>): string {
  const lookup = (path: string): unknown =>
    path.split(".").reduce<unknown>((node, part) => (node as Record<string, unknown>)?.[part], en);
  const count = params?.count;
  const plural = typeof count === "number" ? lookup(`${key}_${count === 1 ? "one" : "other"}`) : undefined;
  const template = plural ?? lookup(key);
  if (typeof template !== "string") return key;
  return template.replace(/\{\{(\w+)\}\}/g, (_, name: string) => String(params?.[name]));
}
vi.mock("react-i18next", () => ({
  useTranslation: () => ({ t: translate, i18n: { resolvedLanguage: "en", language: "en" } }),
  initReactI18next: { type: "3rdParty", init: () => {} },
}));

const { ExamReview } = await import("@/features/exams/ExamReview");

(globalThis as { IS_REACT_ACT_ENVIRONMENT?: boolean }).IS_REACT_ACT_ENVIRONMENT = true;

let host: HTMLDivElement;

function render(): void {
  host = document.createElement("div");
  document.body.appendChild(host);
  act(() => {
    createRoot(host).render(
      <MemoryRouter initialEntries={["/courses/crypto-futures/exams/exam-1/review"]}>
        <InCourse>
          <Routes>
            <Route path="/courses/:course/exams/:examId/review" element={<ExamReview />} />
          </Routes>
        </InCourse>
      </MemoryRouter>,
    );
  });
}

function section(name: string): HTMLElement {
  const found = host.querySelector<HTMLElement>(`section[aria-label="${name}"]`);
  if (!found) throw new Error(`no section ${name}`);
  return found;
}

beforeEach(() => {
  document.body.innerHTML = "";
  exam = SIMULACRO;
});

describe("the results page of a scored exam", () => {
  it("shows raw and transformed per part and in total, and why a part is not graded", () => {
    render();
    const rows = [...host.querySelectorAll("table")[0].querySelectorAll("tbody tr")].map((row) => row.textContent);
    expect(rows[0]).toContain("Part one");
    expect(rows[0]).toContain(translate("exam.partTally", { correct: 50, wrong: 12, blank: 8 }));
    expect(rows[0]).toContain("46");
    expect(rows[0]).toContain("32.86 / 50");
    expect(rows[0]).toContain("30:00");
    expect(rows[1]).toContain(`${en.exam.partNotGraded}: ${en.exam.notGradedNoCase}`);
    expect(rows[2]).toContain(en.exam.total);
    expect(rows[2]).toContain("32.86 / 100");
    expect(rows[2]).toContain("30:00");
  });

  it("shows per-question time on review question cards", () => {
    render();
    expect(host.textContent).toContain("00:45");
  });

  it("shows auto-submitted notice when autoSubmitted is true", () => {
    exam = { ...SIMULACRO, result: { ...SIMULACRO.result!, autoSubmitted: true } };
    render();
    expect(host.textContent).toContain(en.exam.autoSubmittedNotice);
  });

  it("lists results by tema, grouped by module, with blanks apart and each row linking to its lesson", () => {
    render();
    const table = section(translate("byLesson.title", { noun: "tema" }));
    expect(table).toHaveTextContent(en.byLesson.best);
    expect(table).toHaveTextContent(en.byLesson.worst);
    const groups = [...table.querySelectorAll('th[scope="rowgroup"]')].map((th) => th.textContent);
    expect(groups).toEqual(["Appeals", "Competence"]);
    const lessonLinks = [...table.querySelectorAll("tbody a")].map((a) => a.getAttribute("href"));
    expect(lessonLinks).toContain("/courses/crypto-futures/lessons/m01-l2");
    expect(table).toHaveTextContent(en.byLesson.blankNote);
  });

  it("sorts the lessons of each module by the column asked for", () => {
    render();
    const table = section(translate("byLesson.title", { noun: "tema" }));
    const sortBy = (column: string) =>
      [...table.querySelectorAll("button")].find((b) => b.getAttribute("aria-label") === translate("byLesson.sortBy", { column }))!;
    act(() => sortBy(en.byLesson.pct).click());
    const appeals = [...table.querySelectorAll("tbody")[0].querySelectorAll("td a")].map((a) => a.textContent);
    expect(appeals).toEqual(["The reconsideration appeal", "The ordinary appeal"]);
  });

  it("links each question to its lesson at the cited article, and names reserve and case questions", () => {
    render();
    const links = [...host.querySelectorAll("a")].filter((a) => a.textContent === en.exercise.viewInLesson);
    expect(links.map((a) => a.getAttribute("href"))).toEqual([
      "/courses/crypto-futures/lessons/m01-l1#lpac-art-122",
      "/courses/crypto-futures/lessons/m01-l1#lpac-art-122",
      "/courses/crypto-futures/lessons/m02-l1#lrjsp-art-9",
    ]);
    expect(host).toHaveTextContent(en.exam.reserve);
    expect(host).toHaveTextContent(`The refused leave · ${en.exam.caseNotChosen}`);
  });
});

describe("the results page of a tema exam", () => {
  it("shows the table without the two lists when nothing has enough questions to rank", () => {
    exam = {
      ...SIMULACRO,
      result: { score: 0.5, correct: 10, total: 20, blocks: [], modules: [], parts: [
        { id: "preguntas", graded: true, reason: null, case: null, correct: 10, wrong: 4, blank: 6, questions: 20, raw: 8.6667 },
      ], raw: 8.6667, transformed: null, max: null },
      parts: [{ id: "preguntas", title: null, kind: "questions", counted: 20, reserve: 0, choose: null, penalty: "1/3", cases: [], marked: [] }],
      byLesson: { threshold: 3, lists: null, groups: [{ ...TABLE.groups[0], lessons: [{ ...TABLE.groups[0].lessons[0], ...ROW, questions: 20, correct: 10, wrong: 4, blank: 6, pct: 0.5 }] }] },
      questions: [question(0, { partId: "preguntas" })],
    };
    render();
    const table = section(translate("byLesson.title", { noun: "tema" }));
    expect(table).not.toHaveTextContent(en.byLesson.best);
    expect(table).not.toHaveTextContent(en.byLesson.worst);
    expect(table.querySelectorAll("tbody tr")).toHaveLength(2);
  });
});
