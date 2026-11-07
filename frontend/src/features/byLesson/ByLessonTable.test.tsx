import { act } from "react";
import { createRoot } from "react-dom/client";
import { MemoryRouter } from "react-router-dom";
import { afterEach, describe, expect, it, vi } from "vitest";
import type { LessonTable } from "@/api/stats";
import en from "@/i18n/en.json";
import { InCourse } from "@/test/course";
import { clearViewport, setViewportWidth } from "@/test/viewport";

/** K5: «Por tema» is one card per lesson below 640 px and the sortable table from 640 px. */

function translate(key: string, params?: Record<string, unknown>): string {
  const template = key.split(".").reduce<unknown>((node, part) => (node as Record<string, unknown>)?.[part], en);
  if (typeof template !== "string") throw new Error(`missing catalog key ${key}`);
  return template.replace(/\{\{(\w+)\}\}/g, (_, name: string) => String(params?.[name]));
}
vi.mock("react-i18next", () => ({
  useTranslation: () => ({ t: translate, i18n: { resolvedLanguage: "en" } }),
  initReactI18next: { type: "3rdParty", init: () => {} },
}));

const { ByLessonTable } = await import("@/features/byLesson/ByLessonTable");

(globalThis as { IS_REACT_ACT_ENVIRONMENT?: boolean }).IS_REACT_ACT_ENVIRONMENT = true;

const TABLE: LessonTable = {
  threshold: 3,
  lists: null,
  groups: [
    {
      moduleId: "m01",
      title: "Organización",
      questions: 8,
      correct: 5,
      wrong: 2,
      blank: 1,
      pct: 0.625,
      averageSeconds: 40,
      lessons: [
        { lessonId: "m01-l01", title: "La Constitución", questions: 5, correct: 4, wrong: 1, blank: 0, pct: 0.8, averageSeconds: 30 },
        { lessonId: "m01-l02", title: "La Corona", questions: 3, correct: 1, wrong: 1, blank: 1, pct: 1 / 3, averageSeconds: 55 },
      ],
    },
  ],
};

const WITH_TYPES: LessonTable = {
  ...TABLE,
  groups: [
    ...TABLE.groups,
    {
      moduleId: "psicotecnicos",
      title: "Psicotécnicos",
      questions: 6,
      correct: 4,
      wrong: 2,
      blank: 0,
      pct: 2 / 3,
      lessons: [
        { lessonId: "gen:serie-numerica", kind: "type", title: "Series numéricas", questions: 6, correct: 4, wrong: 2, blank: 0, pct: 2 / 3 },
      ],
    },
  ],
};

function mount(width: number, table: LessonTable = TABLE): HTMLDivElement {
  setViewportWidth(width);
  const host = document.createElement("div");
  document.body.appendChild(host);
  act(() => {
    createRoot(host).render(
      <MemoryRouter>
        <InCourse>
          <ByLessonTable table={table} noun="tema" />
        </InCourse>
      </MemoryRouter>,
    );
  });
  return host;
}

afterEach(() => {
  clearViewport();
  document.body.innerHTML = "";
});

describe("«Por tema»", () => {
  it("is a card per lesson at 639 px: title, tally, percentage and average time, with no table", () => {
    const host = mount(639);
    expect(host.querySelector("table")).toBeNull();
    const cards = [...host.querySelectorAll("li")];
    expect(cards).toHaveLength(2);
    expect(cards[0].textContent).toContain("La Constitución");
    expect(cards[0].textContent).toContain("80%");
    expect(cards[0].textContent).toContain(`${en.byLesson.correct} 4 · ${en.byLesson.wrong} 1 · ${en.byLesson.blank} 0`);
    expect(cards[0].textContent).toContain(`${en.byLesson.avgTime} 30s`);
  });

  it("still sorts on a phone, weakest percentage first", () => {
    const host = mount(639);
    const select = host.querySelector("select")!;
    act(() => {
      select.value = "pct";
      select.dispatchEvent(new Event("change", { bubbles: true }));
    });
    expect([...host.querySelectorAll("li a")].map((a) => a.textContent)).toEqual(["La Corona", "La Constitución"]);
  });

  it("is the table with sortable columns at 640 px", () => {
    const host = mount(640);
    expect(host.querySelector("table")).not.toBeNull();
    expect(host.querySelector("li")).toBeNull();
    expect(host.querySelector(`button[aria-label="${translate("byLesson.sortBy", { column: en.byLesson.pct })}"]`)).not.toBeNull();
  });
});

describe("psicotécnico types in «Por tema»", () => {
  it.each([639, 1024])("lists a type as a row with no link to a lesson, at %i px", (width) => {
    const host = mount(width, WITH_TYPES);
    expect(host.textContent).toContain("Series numéricas");
    const links = [...host.querySelectorAll("a")].map((a) => a.getAttribute("href") ?? "");
    expect(links.some((href) => href.includes("gen:"))).toBe(false);
    expect(links.some((href) => href.endsWith("/lessons/m01-l01"))).toBe(true);
  });
});
