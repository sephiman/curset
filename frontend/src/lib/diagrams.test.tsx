import { act } from "react";
import { createRoot } from "react-dom/client";
import { beforeEach, describe, expect, it, vi } from "vitest";
import type { LessonDiagram } from "@/api/course";
import { buildCourseDocument, type PdfLabels } from "@/lib/pdf/document";
import { testPdfLabels } from "@/test/printLabels";

vi.mock("react-i18next", () => ({
  useTranslation: () => ({ t: (key: string) => key, i18n: { resolvedLanguage: "en", language: "en" } }),
  initReactI18next: { type: "3rdParty", init: () => {} },
}));

const { LessonMarkdown } = await import("@/lib/markdown");
const { DiagramFigure } = await import("@/lib/DiagramFigure");

(globalThis as { IS_REACT_ACT_ENVIRONMENT?: boolean }).IS_REACT_ACT_ENVIRONMENT = true;

const diagram: LessonDiagram = {
  id: "m01-l1-d1",
  kind: "state",
  caption: "Row version lifecycle",
  description: "A live row version becomes dead when a delete commits.",
  svg: '<svg width="900" height="120" role="img"><title>Row version lifecycle</title><rect width="900" height="120"/></svg>',
  svgPrint: '<svg width="300" height="120" role="img"><title>Row version lifecycle</title><rect width="300" height="120"/></svg>',
};
const markdown = "Before.\n\n::diagram{id=m01-l1-d1}\n\nAfter.";

describe("a diagram in the lesson view", () => {
  let host: HTMLDivElement;
  beforeEach(() => {
    host = document.createElement("div");
    document.body.appendChild(host);
  });

  function render(diagrams: LessonDiagram[]): void {
    act(() => {
      createRoot(host).render(
        <LessonMarkdown
          markdown={markdown}
          renderExercise={() => null}
          renderFigure={() => null}
          renderDiagram={(id) => <DiagramFigure diagram={diagrams.find((d) => d.id === id)} />}
        />,
      );
    });
  }

  it("is a captioned figure whose drawing scrolls inside its own labelled region", () => {
    render([diagram]);
    const figure = host.querySelector("figure[data-diagram='state']");
    expect(figure?.querySelector("figcaption")?.textContent).toBe("Row version lifecycle");
    const region = figure?.querySelector("[role='region']");
    expect(region?.getAttribute("aria-label")).toBe("Row version lifecycle");
    expect(region?.className).toContain("overflow-x-auto");
    expect(region?.querySelector("svg title")?.textContent).toBe("Row version lifecycle");
  });

  it("prints nothing for a diagram the lesson did not send, and nothing when no renderer is given", () => {
    render([]);
    expect(host.querySelector("figure")).toBeNull();
    expect(host.textContent).toContain("Before.");
  });
});

describe("a diagram in the PDF document definition", () => {
  const labels: PdfLabels = testPdfLabels("en");

  function build(diagrams: LessonDiagram[], text = markdown) {
    return buildCourseDocument({
      courseTitle: "T",
      courseSubtitle: "S",
      courseDescription: "D",
      export: {
        locale: "en",
        glossary: [],
        blocks: [
          {
            id: "b",
            title: "B",
            modules: [{ id: "m", title: "M", summary: "S", lessons: [{ id: "m01-l1", title: "L", markdown: text, diagrams }] }],
          },
        ],
      },
      figures: new Map(),
      exercises: { locale: "en", lessons: [], excluded: [] },
      exerciseCharts: new Map(),
      labels,
    });
  }

  const found = (doc: unknown, key: string): unknown[] => {
    const hits: unknown[] = [];
    const walk = (node: unknown): void => {
      if (Array.isArray(node)) return node.forEach(walk);
      if (typeof node !== "object" || node === null) return;
      if (key in node) hits.push(node);
      Object.values(node).forEach(walk);
    };
    walk(doc);
    return hits;
  };

  it("is vector graphics at the drawing's own width, kept with its caption", () => {
    const [block] = found(build([diagram]).content, "diagramId") as { stack: unknown[]; unbreakable: boolean }[];
    expect(block.unbreakable).toBe(true);
    expect(block.stack[0]).toMatchObject({ svg: diagram.svgPrint, width: 300 });
    expect(block.stack[1]).toMatchObject({ text: "Row version lifecycle", style: "caption" });
  });

  it("is shrunk to the page width when the drawing is wider", () => {
    const wide = { ...diagram, svgPrint: diagram.svgPrint.replace('width="300"', 'width="900"') };
    const [block] = found(build([wide]).content, "diagramId") as { stack: { width: number }[] }[];
    expect(block.stack[0].width).toBeLessThan(900);
  });

  it("falls back to the plain-text description when there is no drawing", () => {
    const [block] = found(build([{ ...diagram, svgPrint: "" }]).content, "diagramId") as { stack: unknown[] }[];
    expect(block.stack[0]).toMatchObject({ text: diagram.description });
  });

  it("fails the export when the prose names a diagram the export lacks", () => {
    expect(() => build([])).toThrowError(/diagram m01-l1-d1 is not in this export/);
  });
});
