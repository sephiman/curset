import { act } from "react";
import { createRoot } from "react-dom/client";
import { MemoryRouter, Route, Routes, useLocation } from "react-router-dom";
import { beforeEach, describe, expect, it, vi } from "vitest";
import type { Locale } from "@/api/auth";
import type { CatalogueCourse, MyCourses } from "@/api/courses";
import en from "@/i18n/en.json";
import { CourseProvider } from "@/features/courses/CourseContext";

/** The course strip above every course page: dropdown or title, languages, reading-language choice. */

const CRYPTO: CatalogueCourse = {
  slug: "crypto-futures",
  title: "Crypto Perpetual Futures",
  subtitle: "The Beginner's Guide",
  description: "d",
  textLocale: "en",
  languages: ["en", "es"],
};
const OPOS: CatalogueCourse = {
  slug: "oposiciones",
  title: "Administración pública",
  subtitle: "s",
  description: "d",
  textLocale: "es",
  languages: ["es"],
};

let mine: MyCourses;
const choose = vi.fn();
vi.mock("@/features/courses/useCourses", () => ({
  useCatalogue: () => ({ data: [OPOS, CRYPTO] }),
  useMyCourses: () => ({ data: mine }),
  useChooseReadingLanguage: () => choose,
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

const { CourseHeader } = await import("@/features/courses/CourseHeader");

(globalThis as { IS_REACT_ACT_ENVIRONMENT?: boolean }).IS_REACT_ACT_ENVIRONMENT = true;

let host: HTMLDivElement;

function Where() {
  return <p data-testid="where">{useLocation().pathname}</p>;
}

function mount(course: CatalogueCourse, path: string, lang: Locale = course.languages[0]): void {
  host = document.createElement("div");
  document.body.appendChild(host);
  act(() => {
    createRoot(host).render(
      <MemoryRouter initialEntries={[path]}>
        <Routes>
          <Route
            path="/courses/:course/*"
            element={
              <CourseProvider course={course} scope={{ slug: course.slug, lang }}>
                <CourseHeader />
                <Where />
              </CourseProvider>
            }
          />
        </Routes>
      </MemoryRouter>,
    );
  });
}

beforeEach(() => {
  document.body.innerHTML = "";
  choose.mockReset();
  mine = { active: ["crypto-futures", "oposiciones"], selected: "crypto-futures", readingLanguages: {} };
});

describe("with two active courses", () => {
  it("offers both, alphabetically, in a dropdown on the Course tab", () => {
    mount(CRYPTO, "/courses/crypto-futures");
    const select = host.querySelector("select");
    expect(select).not.toBeNull();
    expect([...select!.options].map((option) => option.value)).toEqual(["oposiciones", "crypto-futures"]);
  });

  it("keeps the reader on the Exams tab when the course changes there", () => {
    mount(CRYPTO, "/courses/crypto-futures/exams");
    const select = host.querySelector("select")!;
    act(() => {
      select.value = "oposiciones";
      select.dispatchEvent(new Event("change", { bubbles: true }));
    });
    expect(host.querySelector('[data-testid="where"]')?.textContent).toBe("/courses/oposiciones/exams");
  });

  it("has no dropdown of its own on Glossary or Progress: they follow the selection", () => {
    mount(CRYPTO, "/courses/crypto-futures/glossary");
    expect(host.querySelector("select")).toBeNull();
    expect(host.textContent).toContain(CRYPTO.title);
  });
});

it("shows the title in place of the dropdown when only one course is active", () => {
  mine = { active: ["crypto-futures"], selected: "crypto-futures", readingLanguages: {} };
  mount(CRYPTO, "/courses/crypto-futures");
  expect(host.querySelector("select")).toBeNull();
  expect(host.textContent).toContain(CRYPTO.title);
});

describe("languages", () => {
  it("says a Spanish-only course is Spanish only, and offers no reading-language choice", () => {
    mount(OPOS, "/courses/oposiciones");
    expect(host.textContent).toContain("Spanish only");
    expect(host.querySelector('[role="group"]')).toBeNull();
  });

  it("lets a two-language course be read in the other language, remembered per course", () => {
    mount(CRYPTO, "/courses/crypto-futures", "en");
    expect(host.textContent).toContain("In English and Spanish");
    const es = [...host.querySelectorAll<HTMLButtonElement>('[role="group"] button')].find(
      (button) => button.textContent === "ES",
    )!;
    act(() => es.click());
    expect(choose).toHaveBeenCalledWith("crypto-futures", "es");
  });
});
