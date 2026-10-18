import { act } from "react";
import { createRoot } from "react-dom/client";
import { beforeEach, describe, expect, it } from "vitest";
import type { LessonCitation } from "@/api/course";
import { LessonMarkdown } from "@/lib/markdown";

/** Citation links (delta C2–C3) and the four esquema kinds (E1–E2) as a lesson renders them. */

(globalThis as { IS_REACT_ACT_ENVIRONMENT?: boolean }).IS_REACT_ACT_ENVIRONMENT = true;

const LPAC = "/api/courses/fixture-oposiciones/sources/normativa/lpac-extracto.html";

function cite(text: string, section: LessonCitation["section"], ids: string[] = [], href: string | null = `${LPAC}#a1-22`): LessonCitation {
  return { text, section, ids, href, title: "Ley 39/2015 (texto consolidado a 2024-11-06)" };
}

const LESSON = `# Los plazos

El plazo es de un mes (art. 122.1 LPAC). Se resuelve en tres meses (art. 122.2 LPAC).

:::esquema{kind=tabla title="Los dos recursos"}
| Recurso | Plazo | Artículo |
|---|---|---|
| Alzada | Un mes | art. 122.1 LPAC |
:::

:::esquema{kind=plazos title="Plazos de la alzada"}
1. Interposición — un mes (art. 122.1 LPAC)
2. Resolución — tres meses (art. 122.2 LPAC)
:::

:::esquema{kind=pasos title="Cómo se interpone"}
1. Presentación — escrito de recurso — órgano que dictó el acto (art. 122.1 LPAC)
:::

:::esquema{kind=arbol title="Quién decide"}
- Órgano delegante (art. 122.1 LPAC)
  - Órgano delegado — resuelve por delegación (art. 122.2 LPAC)
:::
`;

const CITATIONS = [
  cite("art. 122.1 LPAC", "prose", ["lpac-art-122"]),
  cite("art. 122.2 LPAC", "prose"),
  ...["art. 122.1 LPAC", "art. 122.1 LPAC", "art. 122.2 LPAC", "art. 122.1 LPAC", "art. 122.1 LPAC", "art. 122.2 LPAC"].map((text) =>
    cite(text, "esquema"),
  ),
];

let host: HTMLDivElement;

function render(citations: LessonCitation[]): void {
  host = document.createElement("div");
  document.body.appendChild(host);
  act(() => {
    createRoot(host).render(
      <LessonMarkdown markdown={LESSON} citations={citations} renderExercise={() => null} renderFigure={() => null} />,
    );
  });
}

function esquema(kind: string): HTMLElement {
  const found = host.querySelector<HTMLElement>(`figure[data-esquema="${kind}"]`);
  if (!found) throw new Error(`no ${kind} esquema`);
  return found;
}

beforeEach(() => {
  document.body.innerHTML = "";
});

describe("citations in a lesson", () => {
  it("render as links that open the source beside the lesson, the first one carrying the anchor", () => {
    render(CITATIONS);
    const prose = host.querySelector("p")!;
    const [first, second] = [...prose.querySelectorAll("a")];
    expect(first.textContent).toBe("art. 122.1 LPAC");
    expect(first.getAttribute("href")).toBe(`${LPAC}#a1-22`);
    expect(first.getAttribute("target")).toBe("_blank");
    expect(first.id).toBe("lpac-art-122");
    expect(second.id).toBe("");
    // The parentheses stay text: only the citation is the link.
    expect(prose.textContent).toContain("(art. 122.1 LPAC)");
  });

  it("are plain text in a course that ships none", () => {
    render([]);
    expect(host.querySelectorAll("a")).toHaveLength(0);
    expect(host.textContent).toContain("(art. 122.1 LPAC)");
  });
});

describe("esquemas", () => {
  it("render each of the four kinds under its title", () => {
    render(CITATIONS);
    for (const [kind, title] of [
      ["tabla", "Los dos recursos"],
      ["plazos", "Plazos de la alzada"],
      ["pasos", "Cómo se interpone"],
      ["arbol", "Quién decide"],
    ]) {
      expect(esquema(kind).querySelector("figcaption")).toHaveTextContent(title);
    }
  });

  it("keep a tabla a table that scrolls inside its own box", () => {
    render(CITATIONS);
    const table = esquema("tabla").querySelector("table")!;
    expect(table.parentElement!.className).toContain("overflow-x-auto");
    expect([...table.querySelectorAll("th")].map((th) => th.textContent)).toEqual(["Recurso", "Plazo", "Artículo"]);
    expect(table.querySelector("td:last-child a")).toHaveTextContent("art. 122.1 LPAC");
  });

  it("lay a timeline, a stepper and a tree out as rows of their fields, each row's citation a link", () => {
    render(CITATIONS);
    const steps = [...esquema("plazos").querySelectorAll('[role="group"]')];
    expect(steps.map((row) => [...row.children].map((cell) => cell.textContent))).toEqual([
      ["Interposición", "un mes", "art. 122.1 LPAC"],
      ["Resolución", "tres meses", "art. 122.2 LPAC"],
    ]);
    expect(steps.every((row) => row.querySelector("a")?.getAttribute("href") === `${LPAC}#a1-22`)).toBe(true);

    const [paso] = esquema("pasos").querySelectorAll('[role="group"]');
    expect([...paso.children].map((cell) => cell.textContent)).toEqual([
      "Presentación",
      "escrito de recurso",
      "órgano que dictó el acto",
      "art. 122.1 LPAC",
    ]);

    const [root, child] = [...esquema("arbol").querySelectorAll<HTMLElement>('[role="group"]')];
    expect(root.style.paddingLeft).toBe("0rem");
    expect(child.style.paddingLeft).toBe("1.25rem");
    expect(child).toHaveTextContent("resuelve por delegación");
  });
});
