import { act } from "react";
import { createRoot } from "react-dom/client";
import { MemoryRouter } from "react-router-dom";
import { describe, expect, it, vi } from "vitest";
import en from "@/i18n/en.json";
import { InCourse } from "@/test/course";

const READING = { lessonsCompleted: 1, lessonsTotal: 2, courseCompletion: 0.5 };
const ME = {
  coverage: { publishedModules: 1, totalModules: 1, publishedLessons: 2 },
  thresholds: { minExercisesToRank: 3 },
  reading: READING,
  exercise: { answered: 0, correct: 0, accuracy: null, firstAttemptAccuracy: null, firstSeen: 0, firstCorrect: 0, avgAttemptsToSuccess: null },
  modules: [],
  costliestSections: [],
};

vi.mock("@tanstack/react-query", () => ({
  useQuery: ({ queryKey }: { queryKey: unknown[] }) => {
    if (queryKey[0] === "course") return { data: { course: { theoryOnly: true }, blocks: [] }, isLoading: false };
    if (queryKey[1] === "me") return { data: ME, isLoading: false };
    return { data: undefined, isLoading: false };
  },
}));

function translate(key: string): string {
  const value = key.split(".").reduce<unknown>((node, part) => (node as Record<string, unknown>)?.[part], en);
  if (typeof value !== "string") throw new Error(`missing catalog key ${key}`);
  return value;
}

vi.mock("react-i18next", () => ({
  useTranslation: () => ({ t: translate, i18n: { resolvedLanguage: "en" } }),
  initReactI18next: { type: "3rdParty", init: () => {} },
}));

const { StatsPage } = await import("./StatsPage");

(globalThis as { IS_REACT_ACT_ENVIRONMENT?: boolean }).IS_REACT_ACT_ENVIRONMENT = true;

describe("Progress of a published course with no exercises", () => {
  it("shows the reading progress and nothing about answers, rankings or per-lesson tables", () => {
    const host = document.createElement("div");
    document.body.appendChild(host);
    act(() => {
      createRoot(host).render(
        <InCourse>
          <MemoryRouter>
            <StatsPage />
          </MemoryRouter>
        </InCourse>,
      );
    });
    const text = host.textContent ?? "";
    expect(text).toContain(translate("stats.theoryOnly"));
    expect(text).toContain("1/2");
    expect(text).toContain("50%");
    for (const absent of ["stats.mastery", "stats.costliest", "stats.byModule", "stats.globalTitle"]) {
      expect(text).not.toContain(translate(absent));
    }
    expect(host.querySelector("table")).toBeNull();
  });
});
