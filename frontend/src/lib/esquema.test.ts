// @vitest-environment node
import { describe, expect, it } from "vitest";
import { unified } from "unified";
import remarkParse from "remark-parse";
import remarkGfm from "remark-gfm";
import type { Nodes, Root } from "mdast";
import type {} from "mdast-util-directive";
import { remarkBlockDirectives } from "@/lib/directives";
import { transformEsquemas, type EsquemaRowNode } from "@/lib/esquema";

const processor = unified().use(remarkParse).use(remarkGfm).use(remarkBlockDirectives);

function text(node: Nodes): string {
  if (node.type === "text") return node.value;
  return "children" in node ? node.children.map((child) => text(child as Nodes)).join("") : "";
}

function rows(markdown: string): string[][] {
  const tree = processor.runSync(processor.parse(markdown)) as Root;
  transformEsquemas(tree);
  const found: string[][] = [];
  const walk = (node: Nodes): void => {
    if (node.type === "esquemaRow") {
      found.push((node as EsquemaRowNode).children.map((cell) => text(cell)));
      return;
    }
    if ("children" in node) for (const child of node.children) walk(child as Nodes);
  };
  walk(tree);
  return found;
}

describe("a list esquema row", () => {
  it("keeps a citation that ends in a paragraph letter whole, in its own cell", () => {
    const markdown = [
      ':::esquema{kind=plazos title="Plazos"}',
      "1. Garantía definitiva — siete días hábiles (art. 159.4.f) LCSP)",
      "2. Adjudicación (anticipada) — quince días (art. 23.Uno.B) Ley 31/2022)",
      "3. Resolución — tres meses (art. 122.2 LPAC)",
      ":::",
    ].join("\n");
    expect(rows(markdown)).toEqual([
      ["Garantía definitiva", "siete días hábiles", "art. 159.4.f) LCSP"],
      ["Adjudicación (anticipada)", "quince días", "art. 23.Uno.B) Ley 31/2022"],
      ["Resolución", "tres meses", "art. 122.2 LPAC"],
    ]);
  });
});
