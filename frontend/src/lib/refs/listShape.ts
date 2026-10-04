import { unified } from "unified";
import remarkParse from "remark-parse";
import remarkGfm from "remark-gfm";
import type { List, ListItem, Nodes, Root, Text } from "mdast";
import { remarkBlockDirectives } from "@/lib/directives";

/**
 * A lesson's list structure as the reader sees it, and the list markers that leaked into prose.
 *
 * A re-wrap that pulls `2.` or `- At 5×:` off the start of its line turns a list item into words in
 * the previous paragraph. The page still renders and every word is still there, so the bundle's text
 * checks cannot see it — they compare the bundle with the page, and both carry the same damage.
 */

const processor = unified().use(remarkParse).use(remarkGfm).use(remarkBlockDirectives);

export interface ListShape {
  items: number;
  nestedItems: number;
  numberedItems: number;
}

export interface StrayMarker {
  line: number;
  marker: string;
  context: string;
}

// A marker right after a sentence ends, followed by a space or the end of the text node (`2.` then
// `**bold**`). Code spans are not text nodes, so formulas like `a - b` never reach it.
const STRAY_MARKER = /(?<=[.:;!?»”")]\s+)(\d+\.|[-*])(?=\s|$)/g;

export function parseLesson(markdown: string): Root {
  return processor.parse(markdown);
}

export function listShape(tree: Root): ListShape {
  const shape: ListShape = { items: 0, nestedItems: 0, numberedItems: 0 };
  const walk = (node: Nodes, listDepth: number): void => {
    if (node.type === "list") {
      for (const item of node.children) countItem(item, node, listDepth + 1);
      return;
    }
    if ("children" in node) for (const child of node.children as Nodes[]) walk(child, listDepth);
  };
  const countItem = (item: ListItem, list: List, depth: number): void => {
    shape.items += 1;
    if (depth > 1) shape.nestedItems += 1;
    if (list.ordered) shape.numberedItems += 1;
    for (const child of item.children) walk(child, depth);
  };
  walk(tree, 0);
  return shape;
}

export function strayMarkers(tree: Root): StrayMarker[] {
  const found: StrayMarker[] = [];
  const walk = (node: Nodes): void => {
    if (node.type === "text") found.push(...markersIn(node));
    if ("children" in node) for (const child of node.children as Nodes[]) walk(child);
  };
  walk(tree);
  return found;
}

function markersIn(node: Text): StrayMarker[] {
  const startLine = node.position?.start.line ?? 0;
  return [...node.value.matchAll(STRAY_MARKER)].map((match) => {
    const at = match.index;
    const line = startLine + (node.value.slice(0, at).match(/\n/g)?.length ?? 0);
    const context = node.value.slice(Math.max(0, at - 40), at + 30).replace(/\s+/g, " ");
    return { line, marker: match[0], context };
  });
}
