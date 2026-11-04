import type { Heading, Nodes, Parent, Root } from "mdast";
import type { ContainerDirective } from "mdast-util-directive";
import remarkGfm from "remark-gfm";
import remarkParse from "remark-parse";
import { unified, type Plugin } from "unified";
import { remarkBlockDirectives } from "@/lib/directives";
import { plainText, remarkEsquema } from "@/lib/esquema";

export interface OutlineEntry {
  id: string;
  text: string;
  kind: "section" | "subsection" | "esquema";
}

/** The closing sections the lesson index lists last, after the body (K2). */
const CLOSING_SECTIONS = new Set(["Lo que más cae", "Normativa"]);

export function isClosingSection(entry: OutlineEntry): boolean {
  return entry.kind === "section" && CLOSING_SECTIONS.has(entry.text);
}

function slug(text: string): string {
  const base = text
    .normalize("NFD")
    .replace(/\p{M}/gu, "")
    .toLowerCase()
    .replace(/[^a-z0-9]+/g, "-")
    .replace(/^-|-$/g, "");
  return `sec-${base || "x"}`;
}

function isEsquema(node: Nodes): node is ContainerDirective {
  return node.type === "containerDirective" && node.name === "esquema";
}

function withId(node: Heading | ContainerDirective, id: string): void {
  node.data = { ...node.data, hProperties: { ...node.data?.hProperties, id } };
}

/**
 * Gives each `##`/`###` heading and each esquema a stable id (`sec-…`, deduplicated in document order)
 * and returns them as the lesson's outline. Runs after `remarkEsquema`, whose hast hints it extends.
 */
export function assignOutlineIds(tree: Root): OutlineEntry[] {
  const entries: OutlineEntry[] = [];
  const used = new Map<string, number>();
  const unique = (text: string): string => {
    const base = slug(text);
    const seen = used.get(base) ?? 0;
    used.set(base, seen + 1);
    return seen === 0 ? base : `${base}-${seen + 1}`;
  };
  const walk = (parent: Parent): void => {
    for (const child of parent.children as Nodes[]) {
      if (child.type === "heading" && (child.depth === 2 || child.depth === 3)) {
        const text = plainText(child).trim();
        const id = unique(text);
        withId(child, id);
        entries.push({ id, text, kind: child.depth === 2 ? "section" : "subsection" });
      } else if (isEsquema(child)) {
        const text = child.attributes?.title ?? "";
        const id = unique(text);
        withId(child, id);
        entries.push({ id, text, kind: "esquema" });
      } else if ("children" in child) {
        walk(child as Parent);
      }
    }
  };
  walk(tree);
  return entries;
}

export const remarkOutline: Plugin<[], Root> = () => (tree) => {
  assignOutlineIds(tree);
};

/** The outline of a lesson's markdown, with the same ids `LessonMarkdown` puts on the page. */
export function lessonOutline(markdown: string): OutlineEntry[] {
  const processor = unified().use(remarkParse).use(remarkGfm).use(remarkBlockDirectives).use(remarkEsquema);
  const tree = processor.runSync(processor.parse(markdown)) as Root;
  return assignOutlineIds(tree);
}
