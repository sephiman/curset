import { act, StrictMode, type ReactElement } from "react";
import { createRoot } from "react-dom/client";
import { createMemoryRouter, RouterProvider } from "react-router-dom";
import { beforeEach, describe, expect, it, vi } from "vitest";
import en from "@/i18n/en.json";

const api = vi.hoisted(() => ({
  confirmVerification: vi.fn<(token: string) => Promise<void>>(),
  validateReset: vi.fn<(token: string) => Promise<void>>(),
  confirmReset: vi.fn<(token: string, password: string) => Promise<void>>(),
}));
const refresh = vi.fn(async () => {});

vi.mock("@/api/auth", () => api);
vi.mock("@/auth/AuthContext", () => ({ useAuth: () => ({ user: null, refresh }) }));
vi.mock("@/components/layout/controls", () => ({
  LanguageControl: () => null,
  ThemeControl: () => null,
  ThemeCycleButton: () => null,
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

const { VerifyEmailPage } = await import("./VerifyEmailPage");
const { ResetPasswordPage } = await import("./ResetPasswordPage");

(globalThis as { IS_REACT_ACT_ENVIRONMENT?: boolean }).IS_REACT_ACT_ENVIRONMENT = true;

let host: HTMLDivElement;

async function mount(path: string, element: ReactElement): Promise<void> {
  const router = createMemoryRouter([{ path: path.split("?")[0], element }], { initialEntries: [path] });
  host = document.createElement("div");
  document.body.appendChild(host);
  await act(async () => {
    createRoot(host).render(
      <StrictMode>
        <RouterProvider router={router} />
      </StrictMode>,
    );
  });
}

function rejection(code: string): Promise<never> {
  return Promise.reject({ response: { data: { code, message: code } } });
}

beforeEach(() => {
  document.body.innerHTML = "";
  vi.clearAllMocks();
});

describe("the email verification link", () => {
  it("is spent once even though StrictMode runs effects twice", async () => {
    api.confirmVerification.mockResolvedValue();
    await mount("/verify-email?token=abc", <VerifyEmailPage />);

    expect(api.confirmVerification).toHaveBeenCalledTimes(1);
    expect(api.confirmVerification).toHaveBeenCalledWith("abc");
    expect(host.textContent).toContain(en.auth.verifyDone);
    expect(refresh).toHaveBeenCalled();
  });

  it("explains a used or expired link", async () => {
    api.confirmVerification.mockImplementation(() => rejection("VERIFY_TOKEN_INVALID"));
    await mount("/verify-email?token=used", <VerifyEmailPage />);
    expect(host.textContent).toContain(en.errors.VERIFY_TOKEN_INVALID);
  });

  it("fails without calling the server when the token is missing", async () => {
    await mount("/verify-email", <VerifyEmailPage />);
    expect(api.confirmVerification).not.toHaveBeenCalled();
    expect(host.textContent).toContain(en.errors.VERIFY_TOKEN_INVALID);
  });
});

describe("the password reset link", () => {
  it("offers a new link instead of the form when the token is no longer valid", async () => {
    api.validateReset.mockImplementation(() => rejection("RESET_TOKEN_INVALID"));
    await mount("/reset-password?token=old", <ResetPasswordPage />);

    expect(host.textContent).toContain(en.errors.RESET_TOKEN_INVALID);
    expect(host.querySelector('a[href="/forgot-password"]')?.textContent).toBe(en.auth.requestAnother);
    expect(host.querySelector("form")).toBeNull();
  });

  it("shows the form for a valid token", async () => {
    api.validateReset.mockResolvedValue();
    await mount("/reset-password?token=fresh", <ResetPasswordPage />);
    expect(api.validateReset).toHaveBeenCalledWith("fresh");
    expect(host.querySelector('input[autocomplete="new-password"]')).not.toBeNull();
  });
});
