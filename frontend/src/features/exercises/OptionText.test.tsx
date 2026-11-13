import { act } from "react";
import { createRoot } from "react-dom/client";
import { describe, expect, it } from "vitest";
import { OptionText } from "@/features/exercises/OptionText";

(globalThis as { IS_REACT_ACT_ENVIRONMENT?: boolean }).IS_REACT_ACT_ENVIRONMENT = true;

function render(text: string): HTMLElement {
  const host = document.createElement("div");
  document.body.appendChild(host);
  act(() => createRoot(host).render(<OptionText text={text} />));
  return host;
}

describe("an option's text", () => {
  it("shows code as code", () => {
    const host = render("Call `list.stream()` first");
    expect(host.querySelector("code")?.textContent).toBe("list.stream()");
    expect(host.textContent).toBe("Call list.stream() first");
  });

  it("stays plain text when it holds no code, even with a lone backtick or markdown symbols", () => {
    const host = render("Ctrl+acento grave (`) and *stars*");
    expect(host.querySelector("code, em")).toBeNull();
    expect(host.textContent).toBe("Ctrl+acento grave (`) and *stars*");
  });
});
