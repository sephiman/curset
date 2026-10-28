import { act } from "react";
import { createRoot } from "react-dom/client";
import { MemoryRouter, Route, Routes } from "react-router-dom";
import { beforeEach, describe, expect, it, vi } from "vitest";
import en from "@/i18n/en.json";

/** The avatar menu's way to the account page: a button, first in the menu so a phone shows it at once. */

vi.mock("@/auth/AuthContext", () => ({ useAuth: () => ({ logout: async () => {} }) }));
vi.mock("@/lib/theme", () => ({ useTheme: () => ({ theme: "light", resolvedTheme: "light", setTheme: () => {} }) }));
vi.mock("@/features/courses/useCourses", () => ({ useFollowInterfaceLanguage: () => () => {} }));
vi.mock("@/features/courses/useNavItems", () => ({
  useNavItems: () => [{ tab: "course", to: "/courses/crypto-futures", labelKey: "nav.course", current: true }],
}));

function translate(key: string): string {
  const template = key.split(".").reduce<unknown>((node, part) => (node as Record<string, unknown>)?.[part], en);
  if (typeof template !== "string") throw new Error(`missing catalog key ${key}`);
  return template;
}
vi.mock("react-i18next", () => ({
  useTranslation: () => ({ t: translate, i18n: { resolvedLanguage: "en", changeLanguage: async () => {} } }),
  initReactI18next: { type: "3rdParty", init: () => {} },
}));

const { AccountMenu } = await import("./AccountMenu");

(globalThis as { IS_REACT_ACT_ENVIRONMENT?: boolean }).IS_REACT_ACT_ENVIRONMENT = true;

let host: HTMLDivElement;

beforeEach(() => {
  document.body.innerHTML = "";
  host = document.createElement("div");
  document.body.appendChild(host);
  act(() => {
    createRoot(host).render(
      <MemoryRouter initialEntries={["/courses/crypto-futures"]}>
        <Routes>
          <Route path="/account" element={<h1>account page</h1>} />
          <Route path="*" element={<AccountMenu user={{ username: "juanjo", locale: "en" } as never} />} />
        </Routes>
      </MemoryRouter>,
    );
  });
  act(() => host.querySelector<HTMLButtonElement>('button[aria-haspopup="menu"]')!.click());
});

function menuItems(): HTMLElement[] {
  return [...host.querySelectorAll<HTMLElement>('[role="menu"] [role="menuitem"], [role="menu"] nav a')];
}

describe("the account entry of the avatar menu", () => {
  it("is a button, not a link", () => {
    const account = menuItems().find((item) => item.textContent === en.account.title);
    expect(account?.tagName).toBe("BUTTON");
  });

  it("comes before the primary nav that folds into the menu on a phone", () => {
    expect(menuItems()[0].textContent).toBe(en.account.title);
  });

  it("opens the account page and closes the menu", () => {
    const account = menuItems().find((item) => item.textContent === en.account.title)!;
    act(() => account.click());
    expect(host.querySelector("h1")?.textContent).toBe("account page");
    expect(host.querySelector('[role="menu"]')).toBeNull();
  });
});
