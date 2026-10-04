import { act } from "react";
import { createRoot } from "react-dom/client";
import { QueryClient, QueryClientProvider } from "@tanstack/react-query";
import { beforeEach, describe, expect, it, vi } from "vitest";
import en from "@/i18n/en.json";
import { InCourse } from "@/test/course";

/** A past answer reopened from the history can be reported, like a fresh one. */

const SUMMARY = {
  attemptId: "past-1",
  exerciseId: "m01-ex-1",
  state: "answered",
  isCorrect: false,
  createdAt: "2026-10-04T10:00:00Z",
  answeredAt: "2026-10-04T10:01:00Z",
};
let review: Record<string, unknown>;

vi.mock("@/api/exercises", () => ({
  listAttempts: async () => [SUMMARY],
  getAttempt: async () => review,
}));

function translate(key: string, params?: Record<string, unknown>): string {
  const template = key
    .split(".")
    .reduce<unknown>((node, part) => (node as Record<string, unknown>)?.[part], en);
  if (typeof template !== "string") return key;
  return template.replace(/\{\{(\w+)\}\}/g, (_, name: string) => String(params?.[name]));
}
vi.mock("react-i18next", () => ({
  useTranslation: () => ({ t: translate, i18n: { resolvedLanguage: "en", language: "en" } }),
  initReactI18next: { type: "3rdParty", init: () => {} },
}));

const { AttemptHistory } = await import("@/features/exercises/AttemptHistory");

(globalThis as { IS_REACT_ACT_ENVIRONMENT?: boolean }).IS_REACT_ACT_ENVIRONMENT = true;

let host: HTMLDivElement;

async function settle(): Promise<void> {
  await act(async () => {
    await new Promise((resolve) => setTimeout(resolve, 0));
  });
}

/** Under a full parallel run the queries resolve later than one tick; wait for what the test needs. */
async function until(ready: () => boolean): Promise<void> {
  for (let tries = 0; tries < 100 && !ready(); tries++) await settle();
}

async function openPastAttempt(): Promise<void> {
  host = document.createElement("div");
  document.body.appendChild(host);
  act(() => {
    createRoot(host).render(
      <QueryClientProvider client={new QueryClient()}>
        <InCourse>
          <AttemptHistory exerciseId="m01-ex-1" />
        </InCourse>
      </QueryClientProvider>,
    );
  });
  await until(() => host.querySelector("li button") !== null);
  await act(async () => host.querySelector<HTMLButtonElement>("li button")!.click());
  await until(() => host.textContent?.includes(String(review.prompt)) ?? false);
}

const reportButton = () =>
  [...host.querySelectorAll("button")].find((b) => b.textContent === en.report.link) ?? null;

beforeEach(() => {
  document.body.innerHTML = "";
});

describe("the attempt history", () => {
  it("offers the report on a reopened multiple-choice answer", async () => {
    review = {
      ...SUMMARY,
      type: "quiz",
      prompt: "Which statement best describes a stablecoin?",
      payload: { kind: "single_choice", options: [{ id: "a", text: "A token" }] },
      givenAnswer: { optionId: "a" },
      correctAnswer: { optionId: "a", text: "A token" },
      solutionSteps: [],
      explanation: null,
    };
    await openPastAttempt();
    expect(reportButton()).not.toBeNull();
  });

  it("does not offer it on a calculation", async () => {
    review = {
      ...SUMMARY,
      type: "calculation",
      prompt: "How much margin?",
      payload: { options: [{ id: "a", text: "10" }] },
      givenAnswer: { optionId: "a" },
      correctAnswer: { optionId: "a", value: 10 },
      solutionSteps: [],
      explanation: null,
    };
    await openPastAttempt();
    expect(host.textContent).toContain("How much margin?");
    expect(reportButton()).toBeNull();
  });
});
