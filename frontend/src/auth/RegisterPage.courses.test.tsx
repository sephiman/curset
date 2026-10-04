import { act } from "react";
import { createRoot } from "react-dom/client";
import { MemoryRouter } from "react-router-dom";
import { beforeEach, describe, expect, it, vi } from "vitest";
import type { CatalogueCourse } from "@/api/courses";
import en from "@/i18n/en.json";

/** Sign-up asks which courses interest the learner — always, with none ticked, and none is an answer. */

const ONLY: CatalogueCourse = {
  slug: "crypto-futures",
  title: "Crypto Perpetual Futures",
  subtitle: "s",
  description: "From zero to your first trading plan.",
  textLocale: "en",
  languages: ["en", "es"],
};

const register = vi.fn(async () => {});
vi.mock("@/auth/AuthContext", () => ({ useAuth: () => ({ user: null, register }) }));
vi.mock("@/features/courses/useCourses", () => ({ useCatalogue: () => ({ data: [ONLY] }) }));
vi.mock("@/auth/AuthCard", () => ({
  AuthCard: ({ children }: { children: React.ReactNode }) => <div>{children}</div>,
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

const { RegisterPage } = await import("@/auth/RegisterPage");

(globalThis as { IS_REACT_ACT_ENVIRONMENT?: boolean }).IS_REACT_ACT_ENVIRONMENT = true;

let host: HTMLDivElement;

function fill(id: string, value: string): void {
  const input = host.querySelector<HTMLInputElement>(`#${id}`)!;
  const setter = Object.getOwnPropertyDescriptor(HTMLInputElement.prototype, "value")!.set!;
  act(() => {
    setter.call(input, value);
    input.dispatchEvent(new Event("input", { bubbles: true }));
  });
}

async function submitForm(): Promise<void> {
  await act(async () => {
    host.querySelector("form")!.dispatchEvent(new Event("submit", { bubbles: true, cancelable: true }));
  });
}

beforeEach(async () => {
  document.body.innerHTML = "";
  register.mockClear();
  host = document.createElement("div");
  document.body.appendChild(host);
  act(() => {
    createRoot(host).render(
      <MemoryRouter>
        <RegisterPage />
      </MemoryRouter>,
    );
  });
  fill("username", "newcomer");
  fill("password", "correcthorse");
  await submitForm();
});

describe("the courses step of sign-up", () => {
  it("asks, even when only one course is published, with nothing ticked", () => {
    expect(host.textContent).toContain(en.courses.signupQuestion);
    const boxes = host.querySelectorAll<HTMLInputElement>('input[type="checkbox"]');
    expect(boxes).toHaveLength(1);
    expect(boxes[0].checked).toBe(false);
    expect(host.textContent).toContain(ONLY.title);
  });

  it("creates the account with no course when none is ticked", async () => {
    await submitForm();
    expect(register).toHaveBeenCalledWith("newcomer", "correcthorse", "en", null, []);
  });

  it("activates the ticked courses", async () => {
    act(() => host.querySelector<HTMLInputElement>('input[type="checkbox"]')!.click());
    await submitForm();
    expect(register).toHaveBeenCalledWith("newcomer", "correcthorse", "en", null, ["crypto-futures"]);
  });
});
