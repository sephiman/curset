import { act, type ReactElement } from "react";
import { createRoot } from "react-dom/client";
import { createMemoryRouter, Outlet, RouterProvider } from "react-router-dom";
import { afterEach, beforeEach, describe, expect, it, vi } from "vitest";
import en from "@/i18n/en.json";
import { coursePath } from "@/components/layout/nav";
import { clearViewport, setViewportWidth } from "@/test/viewport";

/** Delta J1–J3: which chrome a reader gets either side of 768 px, and focus mode during a sitting. */

vi.mock("@/auth/AuthContext", () => ({
  useAuth: () => ({ user: { email: "juanjo@example.com", name: "juanjo", locale: "en" }, logout: async () => {} }),
}));
vi.mock("@/lib/theme", () => ({ useTheme: () => ({ theme: "light", resolvedTheme: "light", setTheme: () => {} }) }));
vi.mock("@/features/courses/useCourses", () => ({
  useMyCourses: () => ({
    data: { active: ["crypto-futures"], selected: "crypto-futures", readingLanguages: { "crypto-futures": "en" } },
  }),
  useCatalogue: () => ({
    data: [{ slug: "crypto-futures", title: "Crypto futures", subtitle: "", description: "", textLocale: "en", languages: ["en", "es"] }],
  }),
  useChooseReadingLanguage: () => () => {},
  useFollowInterfaceLanguage: () => () => {},
}));

function translate(key: string, params?: Record<string, unknown>): string {
  const template = key.split(".").reduce<unknown>((node, part) => (node as Record<string, unknown>)?.[part], en);
  if (typeof template !== "string") throw new Error(`missing catalog key ${key}`);
  return template.replace(/\{\{(\w+)\}\}/g, (_, name: string) => String(params?.[name]));
}
vi.mock("react-i18next", () => ({
  useTranslation: () => ({ t: translate, i18n: { resolvedLanguage: "en" } }),
  initReactI18next: { type: "3rdParty", init: () => {} },
}));

const { AppShell } = await import("./AppShell");
const { useFocusMode } = await import("./headerChrome");

(globalThis as { IS_REACT_ACT_ENVIRONMENT?: boolean }).IS_REACT_ACT_ENVIRONMENT = true;

let host: HTMLDivElement;

function SittingProbe() {
  useFocusMode();
  return <p>sitting</p>;
}

function mountAt(entry: string): ReturnType<typeof createMemoryRouter> {
  const router = createMemoryRouter(
    [
      {
        path: "/",
        element: (
          <AppShell>
            <Outlet />
          </AppShell>
        ),
        children: [
          { path: coursePath("crypto-futures").slice(1), element: <p>course page</p> },
          { path: coursePath("crypto-futures", "/exams/e1").slice(1), element: <SittingProbe /> },
          { path: coursePath("crypto-futures", "/exams/e1/review").slice(1), element: <p>review</p> },
        ],
      },
    ],
    { initialEntries: [entry] },
  );
  render(<RouterProvider router={router} />);
  return router;
}

function render(node: ReactElement): void {
  host = document.createElement("div");
  document.body.appendChild(host);
  act(() => {
    createRoot(host).render(node);
  });
}

// The header tabs (768 px and up) carry the same name; the bottom bar is the one outside the header.
const tabBar = () =>
  [...host.querySelectorAll(`nav[aria-label="${en.nav.sections}"]`)].find((nav) => !nav.closest("header")) ?? null;

beforeEach(() => {
  document.body.innerHTML = "";
});
afterEach(clearViewport);

describe("the header tabs (K1)", () => {
  const headerTabs = () => host.querySelector(`header nav[aria-label="${en.nav.sections}"]`);

  it("are in the header at 768 px, after the course selector, the current one marked", () => {
    setViewportWidth(768);
    mountAt(coursePath("crypto-futures", "/exams/e1/review"));
    const links = [...(headerTabs()?.querySelectorAll("a") ?? [])];
    expect(links.map((a) => a.textContent)).toEqual([en.nav.course, en.nav.glossary, en.nav.exams, en.nav.progress]);
    expect(links.find((a) => a.getAttribute("aria-current") === "page")?.textContent).toBe(en.nav.exams);
    const selector = host.querySelector('header button[aria-haspopup="dialog"]')!;
    expect(selector.compareDocumentPosition(headerTabs()!) & Node.DOCUMENT_POSITION_FOLLOWING).toBeTruthy();
  });

  it("are absent from the header at 767 px", () => {
    setViewportWidth(767);
    mountAt(coursePath("crypto-futures"));
    expect(headerTabs()).toBeNull();
  });
});

describe("the bottom tab bar", () => {
  it.each([360, 390, 430, 767])("is present at %i px with the four sections", (width) => {
    setViewportWidth(width);
    mountAt(coursePath("crypto-futures"));
    const labels = [...(tabBar()?.querySelectorAll("a") ?? [])].map((a) => a.textContent);
    expect(labels).toEqual([en.nav.course, en.nav.glossary, en.nav.exams, en.nav.progress]);
  });

  it.each([768, 1024])("is absent at %i px, where the header keeps the sections", (width) => {
    setViewportWidth(width);
    mountAt(coursePath("crypto-futures"));
    expect(tabBar()).toBeNull();
    expect(host.querySelector("header nav")?.textContent).toContain(en.nav.exams);
  });

  it("puts the header on one line below 768 px: home mark, course selector, avatar", () => {
    setViewportWidth(360);
    mountAt(coursePath("crypto-futures"));
    const header = host.querySelector("header");
    expect(header?.querySelector(`a[href="${coursePath("crypto-futures")}"]`)).not.toBeNull();
    expect(header?.querySelector(`button[aria-label="${translate("courses.openSheet", { title: "Crypto futures" })}"]`)).not.toBeNull();
    expect(header?.querySelector('button[aria-label="juanjo"]')).not.toBeNull();
    expect(header?.querySelector("nav")).toBeNull();
  });

  it("hides during an exam sitting and comes back on the review", () => {
    setViewportWidth(360);
    const router = mountAt(coursePath("crypto-futures", "/exams/e1"));
    expect(host.textContent).toContain("sitting");
    expect(tabBar()).toBeNull();

    act(() => {
      void router.navigate(coursePath("crypto-futures", "/exams/e1/review"));
    });
    expect(host.textContent).toContain("review");
    expect(tabBar()).not.toBeNull();
  });
});
