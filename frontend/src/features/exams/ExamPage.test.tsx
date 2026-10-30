import { act, type ReactElement } from "react";
import { createRoot } from "react-dom/client";
import { MemoryRouter } from "react-router-dom";
import { beforeEach, describe, expect, it, vi } from "vitest";
import en from "@/i18n/en.json";
import { InCourse } from "@/test/course";

/**
 * Starting an exam when one is already open.
 *
 * The server abandons an open sitting of the SAME preset and target when a new one starts, and says
 * nothing about it. That is a destructive act performed on a button press meant to be constructive,
 * so the page asks first — and only for the sitting that would actually be lost. A different preset or
 * a different target touches nothing, so it must not ask: a confirmation that fires when nothing is at
 * stake is one readers learn to dismiss without reading.
 */

const GLOBAL_SITTING = {
  id: "exam-global",
  presetId: "global",
  presetTitle: "Global exam",
  target: null,
  targetTitle: null,
  status: "open" as const,
  createdAt: "2026-09-01T10:00:00Z",
  finishedAt: null,
  result: null,
  questions: Array.from({ length: 34 }, (_, index) => ({ answered: index < 3 })),
};

const BLOCK_A_SITTING = {
  ...GLOBAL_SITTING,
  id: "exam-block-a",
  presetId: "block",
  presetTitle: "Block exam",
  target: "block-a",
  targetTitle: "Foundations",
  questions: Array.from({ length: 8 }, (_, index) => ({ answered: index < 1 })),
};

const free = { reserve: 0, choose: null, penalty: "0", max: null, title: null };
let presets: unknown[] = [];
const CRYPTO_PRESETS = [
  {
    id: "global",
    version: 1,
    title: "Global exam",
    timeLimitMinutes: null,
    questions: 34,
    parts: [{ id: "main", kind: "questions", questions: 34, ...free }],
    targets: null,
  },
  {
    id: "block",
    version: 1,
    title: "Block exam",
    timeLimitMinutes: null,
    questions: 0,
    parts: [{ id: "main", kind: "questions", questions: 0, ...free }],
    targets: [
      { id: "block-a", title: "Foundations", questions: 8 },
      { id: "block-b", title: "Instruments", questions: 5 },
    ],
  },
];
const SIMULACRO = {
  id: "simulacro",
  version: 1,
  title: "Simulacro",
  timeLimitMinutes: 100,
  questions: 90,
  parts: [
    { id: "parte-1", title: "Primera parte", kind: "questions", questions: 70, reserve: 2, choose: null, penalty: "1/3", max: 50 },
    { id: "parte-2", title: "Segunda parte", kind: "cases", questions: 20, reserve: 0, choose: 2, penalty: "1/3", max: 50 },
  ],
  targets: null,
};

let openSittings: unknown[] = [];
const startMutate = vi.fn();
const navigate = vi.fn();

vi.mock("@tanstack/react-query", () => ({
  useQuery: ({ queryKey }: { queryKey: unknown[] }) => {
    const which = queryKey.at(-1);
    if (which === "open") return { data: openSittings, isLoading: false };
    if (which === "history") return { data: [], isLoading: false };
    return { data: presets, isLoading: false };
  },
  useMutation: () => ({ mutate: startMutate, isPending: false }),
  useQueryClient: () => ({ invalidateQueries: () => {} }),
}));

vi.mock("react-router-dom", async (original) => ({
  ...(await original<typeof import("react-router-dom")>()),
  useNavigate: () => navigate,
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

const { ExamPage } = await import("./ExamPage");

(globalThis as { IS_REACT_ACT_ENVIRONMENT?: boolean }).IS_REACT_ACT_ENVIRONMENT = true;

let host: HTMLDivElement;

function mount(node: ReactElement): void {
  host = document.createElement("div");
  document.body.appendChild(host);
  act(() => {
    createRoot(host).render(<InCourse>{node}</InCourse>);
  });
}

function page(): void {
  document.body.innerHTML = "";
  mount(
    <MemoryRouter>
      <ExamPage />
    </MemoryRouter>,
  );
}

/** A button whose text is the label, or starts with it (a target button also says how many questions). */
function button(label: string): HTMLButtonElement {
  const found = [...document.querySelectorAll("button")].find((b) => b.textContent?.trim().startsWith(label));
  if (!found) throw new Error(`no button labelled "${label}"`);
  return found as HTMLButtonElement;
}

function dialog(): HTMLElement | null {
  return document.querySelector<HTMLElement>('[role="alertdialog"]');
}

function click(el: Element): void {
  act(() => {
    el.dispatchEvent(new MouseEvent("click", { bubbles: true, cancelable: true }));
  });
}

/** The global preset's own Start button: the first card's. */
function startGlobal(): HTMLButtonElement {
  return button(translate("exam.start"));
}

beforeEach(() => {
  presets = CRYPTO_PRESETS;
  openSittings = [];
  startMutate.mockClear();
  navigate.mockClear();
  document.body.innerHTML = "";
});

describe("starting an exam that would abandon an open one", () => {
  it("asks first, naming the sitting and how far into it the reader is", () => {
    openSittings = [GLOBAL_SITTING];
    page();
    click(startGlobal());

    expect(startMutate).not.toHaveBeenCalled();
    expect(dialog()).not.toBeNull();
    expect(dialog()).toHaveTextContent("Global exam");
    expect(dialog()).toHaveTextContent(translate("exam.conflictAnswered", { done: 3, total: 34 }));
  });

  it("offers continuing as the primary action, and starting over as the destructive one", () => {
    openSittings = [GLOBAL_SITTING];
    page();
    click(startGlobal());

    const resume = button(translate("exam.conflictResume"));
    const fresh = button(translate("exam.conflictStartNew"));
    expect(resume.className).toContain("bg-primary");
    expect(fresh.className).toContain("text-red");

    click(resume);
    expect(navigate).toHaveBeenCalledWith("/courses/crypto-futures/exams/exam-global");
    expect(startMutate).not.toHaveBeenCalled();
  });

  it("dismisses without starting anything and without moving the reader", () => {
    openSittings = [GLOBAL_SITTING];
    page();
    click(startGlobal());
    act(() => {
      document.dispatchEvent(new KeyboardEvent("keydown", { key: "Escape", bubbles: true }));
    });

    expect(dialog()).toBeNull();
    expect(startMutate).not.toHaveBeenCalled();
    // Escape is not the primary action: it must not navigate to the open sitting either.
    expect(navigate).not.toHaveBeenCalled();
  });

  it("starts the new one only when that is explicitly chosen", () => {
    openSittings = [GLOBAL_SITTING];
    page();
    click(startGlobal());
    click(button(translate("exam.conflictStartNew")));

    expect(startMutate).toHaveBeenCalledWith({ presetId: "global", target: undefined });
    expect(dialog()).toBeNull();
  });
});

describe("starting an exam that would abandon nothing", () => {
  it("does not ask when the open sitting is a different preset", () => {
    openSittings = [GLOBAL_SITTING];
    page();
    click(button("Foundations"));

    expect(dialog()).toBeNull();
    expect(startMutate).toHaveBeenCalledWith({ presetId: "block", target: "block-a" });
  });

  it("does not ask when the open sitting is a different block of the same preset", () => {
    openSittings = [BLOCK_A_SITTING];
    page();
    click(button("Instruments"));

    expect(dialog()).toBeNull();
    expect(startMutate).toHaveBeenCalledWith({ presetId: "block", target: "block-b" });
  });

  it("does ask when it is the same block", () => {
    openSittings = [BLOCK_A_SITTING];
    page();
    click(button("Foundations"));

    expect(startMutate).not.toHaveBeenCalled();
    expect(dialog()).toHaveTextContent("Foundations");
    expect(dialog()).toHaveTextContent(translate("exam.conflictAnswered", { done: 1, total: 8 }));
  });

  it("does not ask when nothing is open at all", () => {
    page();
    click(startGlobal());
    expect(dialog()).toBeNull();
    expect(startMutate).toHaveBeenCalledWith({ presetId: "global", target: undefined });
  });
});

describe("the exam list", () => {
  it("shows each preset with its title, parts, question count and time", () => {
    presets = [{ ...SIMULACRO, description: "Official simulation description" }];
    page();
    const text = document.body.textContent ?? "";
    expect(text).toContain("Simulacro");
    expect(text).toContain("Official simulation description");
    expect(text).toContain(translate("exam.questions_other", { count: 90 }));
    expect(text).toContain(translate("exam.minutes", { count: 100 }));
    expect(text).toContain(`${translate("exam.partQuestions", { title: "Primera parte", count: 70 })}, ${translate("exam.reserveCount", { count: 2 })}`);
    expect(text).toContain(translate("exam.partCases", { title: "Segunda parte", choose: 2, count: 20 }));
    expect(text).toContain(translate("exam.penalty", { fraction: "1/3" }));
    expect(button(translate("exam.exportPdf"))).not.toBeNull();
  });

  it("offers a parametric preset once per target, with each one's question count", () => {
    page();
    expect(button("Foundations")).toHaveTextContent(translate("exam.questions_other", { count: 8 }));
    click(button("Instruments"));
    expect(startMutate).toHaveBeenCalledWith({ presetId: "block", target: "block-b" });
  });
});
