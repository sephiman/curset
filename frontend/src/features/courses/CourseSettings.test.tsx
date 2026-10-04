import { act } from "react";
import { createRoot } from "react-dom/client";
import { MemoryRouter } from "react-router-dom";
import { beforeEach, describe, expect, it, vi } from "vitest";
import type { CatalogueCourse, MyCourses } from "@/api/courses";
import en from "@/i18n/en.json";

/** Settings → Courses: every published course with its switch; a switch changes only the active set. */

const course = (slug: string, title: string, languages: ("en" | "es")[]): CatalogueCourse => ({
  slug,
  title,
  subtitle: "s",
  description: `${title}, summarised.`,
  textLocale: languages.includes("en") ? "en" : "es",
  languages,
});
const CATALOGUE = [course("opos", "Administración pública", ["es"]), course("crypto", "Crypto futures", ["en", "es"])];

let mine: MyCourses;
const mutate = vi.fn();
vi.mock("@/features/courses/useCourses", () => ({
  useCatalogue: () => ({ data: CATALOGUE }),
  useMyCourses: () => ({ data: mine }),
  useSaveMyCourses: () => ({ mutate, isPending: false }),
}));

function translate(key: string, params?: Record<string, unknown>): string {
  const template = key
    .split(".")
    .reduce<unknown>((node, part) => (node as Record<string, unknown>)?.[part], en);
  if (typeof template !== "string") return key;
  return template.replace(/\{\{(\w+)\}\}/g, (_, name: string) => String(params?.[name]));
}
vi.mock("react-i18next", () => ({
  useTranslation: () => ({ t: translate, i18n: { resolvedLanguage: "en" } }),
  initReactI18next: { type: "3rdParty", init: () => {} },
}));

const { CourseSettings } = await import("@/features/courses/CourseSettings");

(globalThis as { IS_REACT_ACT_ENVIRONMENT?: boolean }).IS_REACT_ACT_ENVIRONMENT = true;

let host: HTMLDivElement;

beforeEach(() => {
  document.body.innerHTML = "";
  mutate.mockClear();
  mine = { active: ["crypto"], selected: "crypto", readingLanguages: {} };
  host = document.createElement("div");
  document.body.appendChild(host);
  act(() => {
    createRoot(host).render(
      <MemoryRouter>
        <CourseSettings />
      </MemoryRouter>,
    );
  });
});

const switches = () => [...host.querySelectorAll<HTMLInputElement>('input[role="switch"]')];

describe("the Courses section", () => {
  it("lists every published course in catalogue order, each with its languages and its state", () => {
    expect(host.textContent).toContain("Administración pública");
    expect(host.textContent).toContain("Spanish only");
    expect(host.textContent).toContain("In English and Spanish");
    expect(switches().map((s) => s.checked)).toEqual([false, true]);
  });

  it("enables a course without touching the selection", () => {
    act(() => switches()[0].click());
    expect(mutate).toHaveBeenCalledWith({ active: ["crypto", "opos"], selected: "crypto" });
  });

  it("disables a course, leaving the server to move the selection on", () => {
    act(() => switches()[1].click());
    expect(mutate).toHaveBeenCalledWith({ active: [], selected: "crypto" });
  });
});
