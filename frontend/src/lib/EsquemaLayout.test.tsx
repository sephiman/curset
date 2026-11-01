import { act } from "react";
import { createRoot } from "react-dom/client";
import { afterEach, beforeEach, describe, expect, it } from "vitest";
import { LessonMarkdown } from "@/lib/markdown";
import { clearViewport, setViewportWidth } from "@/test/viewport";

/** Delta J4: a `tabla` esquema is a table at 640 px and above, stacked cards below, with nothing lost. */

(globalThis as { IS_REACT_ACT_ENVIRONMENT?: boolean }).IS_REACT_ACT_ENVIRONMENT = true;

const MARKDOWN = `:::esquema{kind=tabla title="Algunos quórum"}
| Acuerdo | Quórum o mayoría | Artículo |
|---|---|---|
| Reglamentos de las Cámaras | Mayoría absoluta | art. 72.1 CE |
| Sesiones extraordinarias | Mayoría absoluta de los miembros | art. 73.2 CE |
:::
`;

let host: HTMLDivElement;

function mount(): void {
  host = document.createElement("div");
  document.body.appendChild(host);
  act(() => {
    createRoot(host).render(<LessonMarkdown markdown={MARKDOWN} renderExercise={() => null} renderFigure={() => null} />);
  });
}

const esquema = () => host.querySelector('figure[data-esquema="tabla"]');

beforeEach(() => {
  document.body.innerHTML = "";
});
afterEach(clearViewport);

describe("a tabla esquema", () => {
  it.each([640, 1024])("is a table with a header row at %i px", (width) => {
    setViewportWidth(width);
    mount();
    const table = esquema()?.querySelector("table");
    expect([...(table?.querySelectorAll("th") ?? [])].map((th) => th.textContent)).toEqual(["Acuerdo", "Quórum o mayoría", "Artículo"]);
    expect(table?.querySelectorAll("tbody tr")).toHaveLength(2);
    expect(esquema()?.querySelector('[role="list"]')).toBeNull();
  });

  it.each([360, 639])("is one card per row at %i px, each cell as «header: value»", (width) => {
    setViewportWidth(width);
    mount();
    expect(esquema()?.querySelector("table")).toBeNull();
    const cards = [...(esquema()?.querySelectorAll('[role="listitem"]') ?? [])];
    expect(cards.map((card) => [...card.children].map((cell) => cell.textContent))).toEqual([
      ["Acuerdo: Reglamentos de las Cámaras", "Quórum o mayoría: Mayoría absoluta", "Artículo: art. 72.1 CE"],
      ["Acuerdo: Sesiones extraordinarias", "Quórum o mayoría: Mayoría absoluta de los miembros", "Artículo: art. 73.2 CE"],
    ]);
    expect(esquema()?.querySelector("figcaption")?.textContent).toBe("Algunos quórum");
  });
});
