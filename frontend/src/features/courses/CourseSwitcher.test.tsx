import { act } from "react";
import { createRoot } from "react-dom/client";
import { MemoryRouter, Route, Routes, useLocation } from "react-router-dom";
import { beforeEach, describe, expect, it, vi } from "vitest";
import type { CatalogueCourse, MyCourses } from "@/api/courses";
import en from "@/i18n/en.json";

/** The header's course selector and its sheet: the courses, their languages, the reading-language choice. */

const CRYPTO: CatalogueCourse = {
  slug: "crypto-futures",
  title: "Crypto Perpetual Futures",
  subtitle: "The Beginner's Guide",
  description: "d",
  textLocale: "en",
  languages: ["en", "es"],
  glyph: "candlestick",
  color: { light: "#0f6b68", dark: "#19afaa" },
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

const { CourseSwitcher } = await import("@/features/courses/CourseSwitcher");

(globalThis as { IS_REACT_ACT_ENVIRONMENT?: boolean }).IS_REACT_ACT_ENVIRONMENT = true;

function Where() {
  return <p data-testid="where">{useLocation().pathname}</p>;
}

function openSheet(path: string): HTMLElement {
  const host = document.createElement("div");
  document.body.appendChild(host);
  act(() => {
    createRoot(host).render(
      <MemoryRouter initialEntries={[path]}>
        <Routes>
          <Route
            path="*"
            element={
              <>
                <CourseSwitcher />
                <Where />
              </>
            }
          />
        </Routes>
      </MemoryRouter>,
    );
  });
  act(() => host.querySelector<HTMLButtonElement>('button[aria-haspopup="dialog"]')!.click());
  return document.querySelector<HTMLElement>('[role="dialog"]')!;
}

function where(): string | null | undefined {
  return document.querySelector('[data-testid="where"]')?.textContent;
}

beforeEach(() => {
  document.body.innerHTML = "";
  choose.mockReset();
  mine = { active: ["crypto-futures", "oposiciones"], selected: "crypto-futures", readingLanguages: {} };
});

describe("with two active courses", () => {
  it("draws a course's glyph in its accent beside its title, in the header and in the sheet", () => {
    const sheet = openSheet("/courses/crypto-futures");
    const header = document.querySelector('button[aria-haspopup="dialog"]')!;
    for (const glyph of [header.querySelector<HTMLElement>("[data-glyph]"), sheet.querySelector<HTMLElement>('[aria-current="true"] [data-glyph]')]) {
      expect(glyph?.dataset.glyph).toBe("candlestick");
      expect(glyph?.style.getPropertyValue("--accent-light")).toBe("#0f6b68");
      expect(glyph?.style.getPropertyValue("--accent-dark")).toBe("#19afaa");
      expect(glyph?.getAttribute("style")).toContain("/api/courses/crypto-futures/glyph.svg");
    }
    // A course without a glyph shows its title alone.
    const opos = [...sheet.querySelectorAll("li button")].find((b) => b.textContent?.includes(OPOS.title))!;
    expect(opos.querySelector("[data-glyph]")).toBeNull();
  });

  it("lists both in the sheet, the current one marked", () => {
    const sheet = openSheet("/courses/crypto-futures");
    const titles = [...sheet.querySelectorAll("li button")].map((button) => button.querySelector("span")?.textContent);
    expect(titles).toEqual([OPOS.title, CRYPTO.title]);
    expect(sheet.querySelector('[aria-current="true"]')?.textContent).toContain(CRYPTO.title);
  });

  it("keeps the reader on the Exams tab when the course changes there", () => {
    const sheet = openSheet("/courses/crypto-futures/exams");
    const opos = [...sheet.querySelectorAll<HTMLButtonElement>("li button")].find((b) => b.textContent?.includes(OPOS.title))!;
    act(() => opos.click());
    expect(where()).toBe("/courses/oposiciones/exams");
  });

  it("returns to the course page when the course changes from Glossary", () => {
    const sheet = openSheet("/courses/crypto-futures/glossary");
    const opos = [...sheet.querySelectorAll<HTMLButtonElement>("li button")].find((b) => b.textContent?.includes(OPOS.title))!;
    act(() => opos.click());
    expect(where()).toBe("/courses/oposiciones");
  });
});

describe("languages", () => {
  it("says a Spanish-only course is Spanish only, and offers no reading-language choice", () => {
    const sheet = openSheet("/courses/oposiciones");
    expect(sheet.textContent).toContain("Spanish only");
    expect(sheet.querySelector('[role="group"]')).toBeNull();
  });

  it("lets a two-language course be read in the other language, remembered per course", () => {
    const sheet = openSheet("/courses/crypto-futures");
    expect(sheet.textContent).toContain("In English and Spanish");
    const es = [...sheet.querySelectorAll<HTMLButtonElement>('[role="group"] button')].find(
      (button) => button.textContent === "ES",
    )!;
    act(() => es.click());
    expect(choose).toHaveBeenCalledWith("crypto-futures", "es");
  });
});

it("renders nothing outside a course page", () => {
  const host = document.createElement("div");
  document.body.appendChild(host);
  act(() => {
    createRoot(host).render(
      <MemoryRouter initialEntries={["/account"]}>
        <CourseSwitcher />
      </MemoryRouter>,
    );
  });
  expect(host.querySelector("button")).toBeNull();
});
