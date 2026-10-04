import { act } from "react";
import { createRoot } from "react-dom/client";
import { QueryClient, QueryClientProvider } from "@tanstack/react-query";
import { beforeEach, describe, expect, it, vi } from "vitest";
import en from "@/i18n/en.json";
import { InCourse } from "@/test/course";

/** "Report this question": one text box, a send button, a one-sentence thanks and nothing more. */

const reportQuestion = vi.fn<(scope: unknown, attemptId: string, message: string) => Promise<void>>();
vi.mock("@/api/reports", () => ({
  reportQuestion: (scope: unknown, attemptId: string, message: string) => reportQuestion(scope, attemptId, message),
}));

function translate(key: string, params?: Record<string, unknown>): string {
  const template = key
    .split(".")
    .reduce<unknown>((node, part) => (node as Record<string, unknown>)?.[part], en);
  if (typeof template !== "string") return String(params?.defaultValue ?? key);
  return template.replace(/\{\{(\w+)\}\}/g, (_, name: string) => String(params?.[name]));
}
vi.mock("react-i18next", () => ({
  useTranslation: () => ({ t: translate, i18n: { resolvedLanguage: "en" } }),
  initReactI18next: { type: "3rdParty", init: () => {} },
}));

const { ReportQuestion } = await import("@/features/reports/ReportQuestion");

(globalThis as { IS_REACT_ACT_ENVIRONMENT?: boolean }).IS_REACT_ACT_ENVIRONMENT = true;

let host: HTMLDivElement;

function mount(): void {
  host = document.createElement("div");
  document.body.appendChild(host);
  const client = new QueryClient({ defaultOptions: { mutations: { retry: false } } });
  act(() => {
    createRoot(host).render(
      <QueryClientProvider client={client}>
        <InCourse>
          <ReportQuestion attemptId="attempt-1" />
        </InCourse>
      </QueryClientProvider>,
    );
  });
}

function type(text: string): void {
  const field = host.querySelector("textarea")!;
  const setter = Object.getOwnPropertyDescriptor(HTMLTextAreaElement.prototype, "value")!.set!;
  act(() => {
    setter.call(field, text);
    field.dispatchEvent(new Event("input", { bubbles: true }));
  });
}

async function submit(): Promise<void> {
  await act(async () => {
    host.querySelector("form")!.dispatchEvent(new Event("submit", { bubbles: true, cancelable: true }));
  });
  // The mutation settles a tick after the request does.
  await act(async () => {
    await new Promise((resolve) => setTimeout(resolve, 0));
  });
}

const send = () => [...host.querySelectorAll("button")].find((b) => b.textContent === en.report.send)!;
const reportButton = () => [...host.querySelectorAll("button")].find((b) => b.textContent === en.report.link)!;

beforeEach(() => {
  document.body.innerHTML = "";
  reportQuestion.mockReset();
  mount();
  act(() => reportButton().click());
});

describe("reporting a question", () => {
  it("opens a single text box asking what is wrong, with nothing else to fill in", () => {
    expect(host.textContent).toContain(en.report.question);
    expect(host.querySelectorAll("textarea")).toHaveLength(1);
    expect(host.querySelectorAll("input, select")).toHaveLength(0);
  });

  it("will not send fewer than five characters", () => {
    type("Bad");
    expect(send().disabled).toBe(true);
  });

  it("sends the text for this attempt, then closes and thanks the reader in one sentence", async () => {
    reportQuestion.mockResolvedValue();
    type("The second option is also correct.");
    await submit();
    expect(reportQuestion).toHaveBeenCalledWith(
      { slug: "crypto-futures", lang: "en" },
      "attempt-1",
      "The second option is also correct.",
    );
    expect(host.querySelector("textarea")).toBeNull();
    expect(host.textContent).toBe(en.report.thanks);
  });

  it("says so plainly when the day's limit is reached", async () => {
    reportQuestion.mockRejectedValue({ response: { data: { code: "REPORT_LIMIT_REACHED", message: "x" } } });
    type("The second option is also correct.");
    await submit();
    expect(host.querySelector('[role="alert"]')?.textContent).toBe(en.errors.REPORT_LIMIT_REACHED);
  });
});
