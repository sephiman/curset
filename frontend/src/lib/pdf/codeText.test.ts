import { describe, expect, it } from "vitest";
import { withCodeSpans } from "@/lib/pdf/codeText";
import { CODE_FONT, PRINT } from "@/lib/pdf/page";

describe("withCodeSpans", () => {
  it("returns text with no code span as the same string, an unpaired backtick included", () => {
    expect(withCodeSpans("Ctrl+acento grave (`)")).toBe("Ctrl+acento grave (`)");
  });

  it("sets each code span as a tinted run in the code face, the prose around it untouched", () => {
    expect(withCodeSpans("Calls `this.b()` inside `a()`.")).toEqual([
      { text: "Calls " },
      { text: "this.b()", font: CODE_FONT, color: PRINT.codeText, background: PRINT.codeFill },
      { text: " inside " },
      { text: "a()", font: CODE_FONT, color: PRINT.codeText, background: PRINT.codeFill },
      { text: "." },
    ]);
  });
});
