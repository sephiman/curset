// @vitest-environment node
import { describe, expect, it } from "vitest";
import type { Content } from "pdfmake/interfaces";
import { figureIds, lessonToContent } from "@/lib/pdf/markdown";

/** The print half of the dialect, over the same mdast the app renders. */

const renderers = { figure: (id: string) => ({ stack: [{ text: `FIGURE:${id}` }] }) };

/** Everything the typesetter would set, flattened — the book's text, in order. */
function printedText(content: Content[]): string {
  const out: string[] = [];
  const walk = (node: unknown): void => {
    if (typeof node === "string") out.push(node);
    else if (Array.isArray(node)) node.forEach(walk);
    else if (node && typeof node === "object") {
      const block = node as Record<string, unknown>;
      walk(block.text);
      walk(block.stack);
      walk(block.ul);
      walk(block.ol);
      walk((block.table as { body?: unknown } | undefined)?.body); // a callout is a one-cell table
    }
  };
  walk(content);
  return out.join("");
}

describe("lessonToContent", () => {
  it("prints a clock time and a ratio whole — no inline directive eats the colon", () => {
    const printed = printedText(
      lessonToContent("Tu stop está vivo a las 03:00, y el desequilibrio es 3:1.", renderers, "m01-l1"),
    );
    expect(printed).toBe("Tu stop está vivo a las 03:00, y el desequilibrio es 3:1.");
  });

  it("prints a wrapped clock-time line as one line, colons intact", () => {
    // The real shape in the prose: a source line wrapped at 100 columns mid-sentence.
    const printed = printedText(
      lessonToContent("- **Londres, de 07:00 a 16:00 UTC**, y **Nueva York, de 13:00\n  a 21:00 UTC.**", renderers, "m23-l1"),
    );
    expect(printed).toBe("Londres, de 07:00 a 16:00 UTC, y Nueva York, de 13:00 a 21:00 UTC.");
  });

  it("still renders the block directives: a note's prose, and a figure through the renderer", () => {
    const printed = printedText(
      lessonToContent(":::note{type=warning}\nCuidado.\n:::\n\n::figure{id=fig-demo}\n", renderers, "m01-l1"),
    );
    expect(printed).toContain("Cuidado.");
    expect(printed).toContain("FIGURE:fig-demo");
  });

  it("finds the figure ids a lesson embeds, in reading order", () => {
    expect(figureIds("::figure{id=fig-b}\n\ntexto\n\n::figure{id=fig-a}\n")).toEqual(["fig-b", "fig-a"]);
  });
});

describe("lessonToContent: technical content", () => {
  const judgementRenderers = { ...renderers, judgement: (source: string) => `Judgement from ${source}` };

  it("prints a code block whole, whatever its info string carries", () => {
    const printed = printedText(
      lessonToContent("```java snippet=m06-l02/LostUpdate.java\nint n = 1;\n```\n", renderers, "m06-l02"),
    );
    expect(printed).toBe("int n = 1;");
  });

  it("never prints a bullets comment", () => {
    const printed = printedText(lessonToContent("## Locks\n\n<!-- bullets: 6.2.a -->\n\nA lock.", renderers, "m06-l02"));
    expect(printed).toBe("LocksA lock.");
  });

  it("prints a judgement as a callout under a line naming its source", () => {
    const printed = printedText(
      lessonToContent(':::judgement{source="Fowler" ref="x#y"}\nPrefer composition.\n:::\n', judgementRenderers, "m01-l1"),
    );
    expect(printed).toBe("Judgement from FowlerPrefer composition.");
  });
});
