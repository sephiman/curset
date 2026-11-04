import { act } from "react";
import { createRoot } from "react-dom/client";
import { MemoryRouter, Route, Routes } from "react-router-dom";
import { QueryClient, QueryClientProvider } from "@tanstack/react-query";
import { afterEach, beforeEach, describe, expect, it, vi } from "vitest";
import en from "@/i18n/en.json";
import { InCourse } from "@/test/course";
import { clearViewport, setViewportWidth } from "@/test/viewport";

/** K2: the lesson's side index from 1024 px — which entries it lists, and which stay folded. */

const LESSON = [
  "# Lesson 1",
  "Intro.",
  "## First section",
  "Text.",
  "### First detail",
  "Text.",
  ':::esquema{kind=tabla title="First table"}',
  "| A | B |\n|---|---|\n| 1 | 2 |",
  ":::",
  "## Second section",
  ':::esquema{kind=tabla title="Second table"}',
  "| A | B |\n|---|---|\n| 3 | 4 |",
  ":::",
  "### Second detail",
  "Text.",
  "## Lo que más cae",
  "- x",
  "## Normativa",
  "- y",
].join("\n\n");

vi.mock("@/auth/AuthContext", () => ({
  useAuth: () => ({
    user: { id: "u1", email: "juanjo@example.com", name: "juanjo", locale: "en", email_verified: true },
    logout: async () => {},
    setLocale: async () => {},
  }),
}));
vi.mock("@/auth/useMailFeature", () => ({ useMailFeature: () => false }));
vi.mock("@/lib/theme", () => ({ useTheme: () => ({ theme: "light", resolvedTheme: "light", setTheme: () => {} }) }));
vi.mock("@/features/courses/useCourses", () => ({
  useCatalogue: () => ({
    data: [{ slug: "crypto-futures", title: "Crypto futures", subtitle: "", description: "", textLocale: "en", languages: ["en", "es"] }],
  }),
  useMyCourses: () => ({
    data: { active: ["crypto-futures"], selected: "crypto-futures", readingLanguages: { "crypto-futures": "en" } },
  }),
  useSaveMyCourses: () => ({ mutate: () => {}, isPending: false }),
  useFollowInterfaceLanguage: () => () => {},
  useChooseReadingLanguage: () => () => {},
}));
vi.mock("@/api/course", () => ({
  getLesson: async () => ({
    id: "m01-l1",
    moduleId: "m01",
    moduleTitle: "Foundations",
    title: "Lesson 1",
    markdown: LESSON,
    completed: false,
    readingSeconds: 120,
    exercises: [],
    citations: [],
    practiceQuestions: 10,
  }),
  getCourse: async () => ({ course: { title: "Crypto futures", lessonNoun: "lesson" }, blocks: [] }),
  getGlossary: async () => ({ terms: [] }),
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
  useTranslation: () => ({ t: translate, i18n: { resolvedLanguage: "en", changeLanguage: async () => {} } }),
  initReactI18next: { type: "3rdParty", init: () => {} },
}));

const { LessonPage } = await import("@/features/course/LessonPage");

(globalThis as { IS_REACT_ACT_ENVIRONMENT?: boolean }).IS_REACT_ACT_ENVIRONMENT = true;

// jsdom lays nothing out: each anchor gets a page position in document order, and «scrolling» shifts them all.
let scrolled = 0;
beforeEach(() => {
  scrolled = 0;
  vi.spyOn(Element.prototype, "getBoundingClientRect").mockImplementation(function (this: Element) {
    const anchors = [...document.querySelectorAll("[id^='sec-']")];
    const top = anchors.indexOf(this) * 1000 - scrolled;
    return { top, bottom: top + 20, left: 0, right: 0, width: 0, height: 20, x: 0, y: top, toJSON: () => ({}) };
  });
  vi.stubGlobal("requestAnimationFrame", (callback: FrameRequestCallback) => {
    callback(0);
    return 1;
  });
});

afterEach(() => {
  vi.restoreAllMocks();
  vi.unstubAllGlobals();
  clearViewport();
  document.body.innerHTML = "";
});

async function mountLesson(width: number): Promise<HTMLDivElement> {
  setViewportWidth(width);
  const host = document.createElement("div");
  document.body.appendChild(host);
  const client = new QueryClient({ defaultOptions: { queries: { retry: false } } });
  act(() => {
    createRoot(host).render(
      <QueryClientProvider client={client}>
        <MemoryRouter initialEntries={["/courses/crypto-futures/lessons/m01-l1"]}>
          <InCourse>
            <Routes>
              <Route path="/courses/:course/lessons/:lessonId" element={<LessonPage />} />
            </Routes>
          </InCourse>
        </MemoryRouter>
      </QueryClientProvider>,
    );
  });
  for (let i = 0; i < 5; i += 1) await act(async () => await new Promise((resolve) => setTimeout(resolve, 0)));
  return host;
}

const index = (host: HTMLElement) => host.querySelector<HTMLElement>(`nav[aria-label="${en.course.lessonIndex}"]`);
const entries = (host: HTMLElement) => [...(index(host)?.querySelectorAll("a") ?? [])].map((a) => a.textContent);

describe("the lesson index", () => {
  it("is beside the lesson at 1024 px", async () => {
    const host = await mountLesson(1024);
    expect(index(host)).not.toBeNull();
  });

  it("is absent at 1023 px", async () => {
    const host = await mountLesson(1023);
    expect(index(host)).toBeNull();
    expect(host.querySelector("article")?.textContent).toContain("First section");
  });

  it("lists every section and esquema title, but only the current section's subsections", async () => {
    const host = await mountLesson(1280);
    expect(entries(host)).toEqual([
      "First section",
      "First detail",
      "First table",
      "Second section",
      "Second table",
      "Lo que más cae",
      "Normativa",
    ]);
    expect(index(host)?.querySelector('[aria-current="location"]')?.textContent).toBe("First section");
  });

  it("unfolds the section the reader scrolls into and folds the one left behind", async () => {
    const host = await mountLesson(1280);
    // «Second detail» is the sixth anchor: put it on the reading line.
    scrolled = 5 * 1000;
    act(() => {
      window.dispatchEvent(new Event("scroll"));
    });
    expect(entries(host)).toEqual([
      "First section",
      "First table",
      "Second section",
      "Second table",
      "Second detail",
      "Lo que más cae",
      "Normativa",
    ]);
    expect(index(host)?.querySelector('[aria-current="location"]')?.textContent).toBe("Second detail");
  });

  it("puts «Lo que más cae» and «Normativa» in their own list after the body", async () => {
    const host = await mountLesson(1280);
    const lists = [...(index(host)?.querySelectorAll(":scope > ul") ?? [])];
    expect(lists).toHaveLength(2);
    expect([...lists[1].querySelectorAll("a")].map((a) => a.textContent)).toEqual(["Lo que más cae", "Normativa"]);
  });

  it("points each entry at the heading or esquema with that id on the page", async () => {
    const host = await mountLesson(1280);
    for (const link of index(host)?.querySelectorAll("a") ?? []) {
      const target = host.querySelector(link.getAttribute("href")!);
      expect(target?.textContent).toContain(link.textContent!);
    }
  });
});
