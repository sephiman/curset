import { act, type ReactNode } from "react";
import { createRoot } from "react-dom/client";
import { MemoryRouter, Route, Routes } from "react-router-dom";
import { QueryClient, QueryClientProvider } from "@tanstack/react-query";
import { afterEach, describe, expect, it, vi } from "vitest";
import en from "@/i18n/en.json";
import { InCourse } from "@/test/course";
import { LessonWidthProvider, useLessonWidth } from "@/lib/lessonWidth";

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
    markdown: "# Lesson 1\n\nBody text.",
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

const { AppShell } = await import("@/components/layout/AppShell");
const { AccountPage } = await import("@/features/account/AccountPage");
const { LessonPage } = await import("@/features/course/LessonPage");
const { PracticePage } = await import("@/features/practice/PracticePage");

(globalThis as { IS_REACT_ACT_ENVIRONMENT?: boolean }).IS_REACT_ACT_ENVIRONMENT = true;

function stubStorage(initial?: string): Map<string, string> {
  const store = new Map<string, string>();
  if (initial !== undefined) store.set("lessonWidth", initial);
  vi.stubGlobal("localStorage", {
    getItem: (k: string) => store.get(k) ?? null,
    setItem: (k: string, v: string) => void store.set(k, v),
  });
  return store;
}

function render(node: ReactNode): HTMLDivElement {
  const host = document.createElement("div");
  document.body.appendChild(host);
  const client = new QueryClient({ defaultOptions: { queries: { retry: false } } });
  act(() => {
    createRoot(host).render(<QueryClientProvider client={client}>{node}</QueryClientProvider>);
  });
  return host;
}

async function settle(): Promise<void> {
  for (let i = 0; i < 5; i += 1) await act(async () => await new Promise((resolve) => setTimeout(resolve, 0)));
}

function Probe() {
  const { lessonWidth, lessonWidthClass, setLessonWidth } = useLessonWidth();
  return (
    <div>
      <span data-testid="state">{`${lessonWidth}:${lessonWidthClass}`}</span>
      <button type="button" onClick={() => setLessonWidth("wide")}>
        wide
      </button>
    </div>
  );
}

afterEach(() => {
  vi.unstubAllGlobals();
  document.body.innerHTML = "";
});

describe("lesson width preference", () => {
  it("defaults to normal (max-w-2xl) and ignores unknown stored values", () => {
    stubStorage("bogus");
    const host = render(
      <LessonWidthProvider>
        <Probe />
      </LessonWidthProvider>,
    );
    expect(host.querySelector('[data-testid="state"]')?.textContent).toBe("normal:max-w-2xl");
  });

  it("persists the selected width in localStorage and restores it on mount", () => {
    const store = stubStorage();
    const host = render(
      <LessonWidthProvider>
        <Probe />
      </LessonWidthProvider>,
    );
    act(() => {
      host.querySelector("button")!.click();
    });
    expect(host.querySelector('[data-testid="state"]')?.textContent).toBe("wide:max-w-4xl");
    expect(store.get("lessonWidth")).toBe("wide");

    const remounted = render(
      <LessonWidthProvider>
        <Probe />
      </LessonWidthProvider>,
    );
    expect(remounted.querySelector('[data-testid="state"]')?.textContent).toBe("wide:max-w-4xl");
  });

  it("changes the lesson and practice width from both the account page and the avatar menu, and expands the shell on Full", async () => {
    stubStorage("normal");
    const host = render(
      <LessonWidthProvider>
        <MemoryRouter initialEntries={["/courses/crypto-futures/lessons/m01-l1"]}>
          <AppShell>
            <InCourse>
              <Routes>
                <Route path="/courses/:course/lessons/:lessonId" element={<LessonPage />} />
                <Route path="/courses/:course/lessons/:lessonId/practice" element={<PracticePage />} />
                <Route path="/account" element={<AccountPage />} />
              </Routes>
            </InCourse>
          </AppShell>
        </MemoryRouter>
      </LessonWidthProvider>,
    );
    await settle();

    const article = () => host.querySelector("article")!;
    const main = () => host.querySelector("main")!;

    expect(article().className).toContain("max-w-2xl");
    expect(main().className).toContain("max-w-5xl");

    // Open avatar menu and switch to Wide.
    act(() => host.querySelector<HTMLButtonElement>('button[aria-haspopup="menu"]')!.click());
    const menuGroup = host.querySelector(`[role="menu"] [role="group"][aria-label="${en.common.lessonWidth}"]`)!;
    const wideBtn = [...menuGroup.querySelectorAll("button")].find((b) => b.textContent === en.lessonWidth.wide)!;
    act(() => wideBtn.click());

    expect(article().className).toContain("max-w-4xl");
    expect(main().className).toContain("max-w-5xl");

    // Switch to Full from the avatar menu: both the lesson article and the shell main become max-w-none.
    const fullBtn = [...menuGroup.querySelectorAll("button")].find((b) => b.textContent === en.lessonWidth.full)!;
    act(() => fullBtn.click());

    expect(article().className).toContain("max-w-none");
    expect(main().className).toContain("max-w-none");

    // Navigate to the Account page: main returns to max-w-5xl, and the Account page also renders the control.
    const accountBtn = [...host.querySelectorAll<HTMLButtonElement>('[role="menuitem"]')].find(
      (b) => b.textContent === en.account.title,
    )!;
    act(() => accountBtn.click());
    expect(main().className).toContain("max-w-5xl");

    const accountGroup = host.querySelector(`[role="group"][aria-label="${en.common.lessonWidth}"]`)!;
    expect(accountGroup).not.toBeNull();
  });

  it("applies the selected width to the lesson practice page as well", async () => {
    stubStorage("full");
    const host = render(
      <LessonWidthProvider>
        <MemoryRouter initialEntries={["/courses/crypto-futures/lessons/m01-l1/practice"]}>
          <AppShell>
            <InCourse>
              <Routes>
                <Route path="/courses/:course/lessons/:lessonId/practice" element={<PracticePage />} />
              </Routes>
            </InCourse>
          </AppShell>
        </MemoryRouter>
      </LessonWidthProvider>,
    );
    await settle();

    const main = host.querySelector("main")!;
    const practiceContainer = main.firstElementChild as HTMLElement;
    expect(main.className).toContain("max-w-none");
    expect(practiceContainer.className).toContain("max-w-none");
  });
});
