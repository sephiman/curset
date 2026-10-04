import { readFileSync } from "node:fs";
import { resolve } from "node:path";
import { act, type ReactElement } from "react";
import { createRoot } from "react-dom/client";
import { MemoryRouter, Route, Routes, useLocation } from "react-router-dom";
import { beforeEach, describe, expect, it, vi } from "vitest";
import en from "@/i18n/en.json";
import type { MyCourses } from "@/api/courses";
import { coursePath, tabOf, tabPath, type Tab } from "@/components/layout/nav";
import { manifestLessons, manifestModules } from "@/test/courseContent";

/**
 * Page URLs name their course, and every course-less address — a tab, the home, a bookmark from
 * before the URLs carried a course — lands on the selected course, or on the tab's "no course" page.
 */

let mine: MyCourses = { active: [], selected: null, readingLanguages: {} };
vi.mock("@/features/courses/useCourses", () => ({
  useMyCourses: () => ({ data: mine, isLoading: false }),
}));

function translate(key: string): string {
  const template = key
    .split(".")
    .reduce<unknown>((node, part) => (node as Record<string, unknown>)?.[part], en);
  if (typeof template !== "string") throw new Error(`missing catalog key ${key}`);
  return template;
}
vi.mock("react-i18next", () => ({
  useTranslation: () => ({ t: translate, i18n: { resolvedLanguage: "en" } }),
  initReactI18next: { type: "3rdParty", init: () => {} },
}));

const { SelectedCourseRedirect } = await import("@/features/courses/SelectedCourseRedirect");

(globalThis as { IS_REACT_ACT_ENVIRONMENT?: boolean }).IS_REACT_ACT_ENVIRONMENT = true;

function Where() {
  const { pathname, search, hash } = useLocation();
  return <p data-testid="where">{pathname + search + hash}</p>;
}

let host: HTMLDivElement;

function mountAt(entry: string): void {
  host = document.createElement("div");
  document.body.appendChild(host);
  const legacy: [string, Tab][] = [
    ["/", "course"],
    ["/course", "course"],
    ["/modules/:moduleId", "course"],
    ["/lessons/:lessonId", "course"],
    ["/glossary", "glossary"],
    ["/stats", "progress"],
    ["/exams/*", "exams"],
  ];
  const tree: ReactElement = (
    <MemoryRouter initialEntries={[entry]}>
      <Routes>
        <Route path="/courses/:course/*" element={<Where />} />
        {legacy.map(([path, tab]) => (
          <Route key={path} path={path} element={<SelectedCourseRedirect tab={tab} />} />
        ))}
      </Routes>
    </MemoryRouter>
  );
  act(() => {
    createRoot(host).render(tree);
  });
}

const where = () => host.querySelector('[data-testid="where"]')?.textContent ?? "";

beforeEach(() => {
  document.body.innerHTML = "";
});

describe("a course-less address with a selected course", () => {
  beforeEach(() => {
    mine = { active: ["crypto-futures"], selected: "crypto-futures", readingLanguages: { "crypto-futures": "en" } };
  });

  it.each([
    ["/", "/courses/crypto-futures"],
    ["/course", "/courses/crypto-futures"],
    ["/glossary", "/courses/crypto-futures/glossary"],
    ["/stats", "/courses/crypto-futures/stats"],
    ["/lessons/m03-l1", "/courses/crypto-futures/lessons/m03-l1"],
    ["/modules/m09", "/courses/crypto-futures/modules/m09"],
    ["/exams", "/courses/crypto-futures/exams"],
    ["/exams/abc/review", "/courses/crypto-futures/exams/abc/review"],
  ])("%s lands on %s", (old, scoped) => {
    mountAt(old);
    expect(where()).toBe(scoped);
  });

  it("keeps the query string and the fragment across the redirect", () => {
    mountAt("/glossary?q=funding#g-funding");
    expect(where()).toBe("/courses/crypto-futures/glossary?q=funding#g-funding");
  });
});

describe("a course-less address with no active course", () => {
  beforeEach(() => {
    mine = { active: [], selected: null, readingLanguages: {} };
  });

  it.each([
    ["/", "course"],
    ["/glossary", "glossary"],
    ["/exams", "exams"],
    ["/stats", "progress"],
  ])("%s shows the %s tab's default page, whose one control leads to the course settings", (path, tab) => {
    mountAt(path);
    expect(where()).toBe("");
    expect(host.textContent).toContain(en.noCourse.lead);
    expect(host.textContent).toContain(en.noCourse[tab as keyof typeof en.noCourse]);
    const controls = host.querySelectorAll("a, button, input, select, textarea");
    expect(controls).toHaveLength(1);
    expect(controls[0].getAttribute("href")).toBe("/account#courses");
  });
});

describe("tab addresses", () => {
  it("hang off the selected course, or fall back to the course-less ones", () => {
    expect(tabPath("glossary", "crypto-futures")).toBe("/courses/crypto-futures/glossary");
    expect(tabPath("course", "crypto-futures")).toBe("/courses/crypto-futures");
    expect(tabPath("progress", null)).toBe("/stats");
    expect(tabPath("course", null)).toBe("/course");
  });

  it("tell modules and lessons apart from the other tabs", () => {
    expect(tabOf("/courses/x/lessons/m01-l1")).toBe("course");
    expect(tabOf("/courses/x/modules/m01")).toBe("course");
    expect(tabOf("/courses/x/exams/abc/review")).toBe("exams");
    expect(tabOf("/courses/x/stats")).toBe("progress");
    expect(tabOf("/glossary")).toBe("glossary");
  });
});

describe("a display id names its current holder", () => {
  it("App.tsx hard-codes no content id, which a static route would shadow", () => {
    const source = readFileSync(resolve(__dirname, "App.tsx"), "utf8");
    // Any id, not just a live one: ids are append-only, so today's vacant id is tomorrow's module.
    const hardCoded = [...source.matchAll(/\bm\d\d(-(l|ex-)\d+)?\b/g)].map((m) => m[0]);
    const live = new Set([...manifestModules(), ...manifestLessons()].map((entry) => entry.id));
    expect(hardCoded.map((id) => (live.has(id) ? `${id} (live)` : id))).toEqual([]);
  });

  it("course pages are params under the course, never a literal slug", () => {
    expect(coursePath("fixture", "/lessons/m31-l1")).toBe("/courses/fixture/lessons/m31-l1");
    const source = readFileSync(resolve(__dirname, "App.tsx"), "utf8");
    expect(source).toContain('path="/courses/:course/*"');
  });
});
