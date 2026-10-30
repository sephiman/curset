import { act } from "react";
import { createRoot } from "react-dom/client";
import { beforeEach, describe, expect, it, vi } from "vitest";
import { CopyableReference } from "@/components/ui/CopyableReference";

(globalThis as { IS_REACT_ACT_ENVIRONMENT?: boolean }).IS_REACT_ACT_ENVIRONMENT = true;

vi.mock("react-i18next", () => ({
  useTranslation: () => ({
    t: (key: string, def?: string) =>
      key === "solution.copyReference" ? "Copiar referencia" : key === "solution.copied" ? "Copiado" : (def ?? key),
  }),
}));

describe("CopyableReference", () => {
  let host: HTMLDivElement;

  beforeEach(() => {
    host = document.createElement("div");
    document.body.appendChild(host);
  });

  it("renders the reference and copies to clipboard on click", async () => {
    const writeText = vi.fn().mockResolvedValue(undefined);
    Object.assign(navigator, {
      clipboard: { writeText },
    });

    act(() => {
      createRoot(host).render(<CopyableReference reference="age-c1 · III.3 · q127" />);
    });

    expect(host.textContent).toContain("age-c1 · III.3 · q127");
    const button = host.querySelector("button");
    expect(button).not.toBeNull();

    await act(async () => {
      button?.click();
    });

    expect(writeText).toHaveBeenCalledWith("age-c1 · III.3 · q127");
    expect(button?.getAttribute("aria-label")).toContain("Copiado");
  });
});
