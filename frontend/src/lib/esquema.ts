import type { List, ListItem, Nodes, Paragraph, Parent, PhrasingContent, Root, Text } from "mdast";
import type { ContainerDirective } from "mdast-util-directive";
import type { Plugin } from "unified";

/**
 * The `:::esquema` block, restructured for the two renderers.
 *
 * A `tabla` keeps its GFM table (the last column is the citation). The list kinds become rows of
 * typed cells, split at « — » with the trailing «(cita)» as the last cell, so the screen can lay a
 * row out as a timeline step, a tree node or a stepper row and the PDF as a table row — from one
 * parse. The words do not change; only where they sit. The backend reads the same block with its own
 * parser (`content/esquema.py`) for the checks; the format is the same one either way.
 */

export const ESQUEMA_KINDS = ["tabla", "plazos", "arbol", "pasos"] as const;
export type EsquemaKind = (typeof ESQUEMA_KINDS)[number];

export type EsquemaCellRole = "label" | "detail" | "plazo" | "document" | "organ" | "citation";

/** The fields of a list row, in order, before its citation. */
export const ROW_FIELDS: Record<Exclude<EsquemaKind, "tabla">, EsquemaCellRole[]> = {
  plazos: ["label", "plazo"],
  pasos: ["label", "document", "organ"],
  arbol: ["label", "detail"],
};

export interface EsquemaCellNode extends Parent {
  type: "esquemaCell";
  role: EsquemaCellRole;
  children: PhrasingContent[];
  data: { hName: "span"; hProperties: { "data-esquema-cell": EsquemaCellRole } };
}

export interface EsquemaRowNode extends Parent {
  type: "esquemaRow";
  /** 0 for a root; an arbol's nesting depth otherwise. */
  depth: number;
  children: EsquemaCellNode[];
  data: { hName: "div"; hProperties: { "data-esquema-row": string } };
}

declare module "mdast" {
  interface RootContentMap {
    esquemaRow: EsquemaRowNode;
    esquemaCell: EsquemaCellNode;
  }
  interface PhrasingContentMap {
    esquemaCell: EsquemaCellNode;
  }
}

const SEPARATOR = " — ";
const TRAILING_CITATION = /\s*\(([^()]*(?:\([^()]*\)[^()]*)*)\)\s*$/;

function cell(role: EsquemaCellRole, children: PhrasingContent[]): EsquemaCellNode {
  return { type: "esquemaCell", role, children, data: { hName: "span", hProperties: { "data-esquema-cell": role } } };
}

/** Phrasing content split at « — » in its text nodes. */
function fields(content: PhrasingContent[]): PhrasingContent[][] {
  const out: PhrasingContent[][] = [[]];
  for (const node of content) {
    if (node.type !== "text") {
      out[out.length - 1].push(node);
      continue;
    }
    node.value.split(SEPARATOR).forEach((piece, index) => {
      if (index > 0) out.push([]);
      if (piece) out[out.length - 1].push({ type: "text", value: piece } as Text);
    });
  }
  return out;
}

/** Takes the trailing «(cita)» off the last field; the citation cell holds its inside. */
function splitCitation(last: PhrasingContent[]): PhrasingContent[] {
  const tail = last[last.length - 1];
  if (!tail || tail.type !== "text") return [];
  const match = TRAILING_CITATION.exec(tail.value);
  if (!match) return [];
  tail.value = tail.value.slice(0, match.index);
  if (!tail.value) last.pop();
  return [{ type: "text", value: match[1] } as Text];
}

function rows(list: List, kind: Exclude<EsquemaKind, "tabla">, depth: number): EsquemaRowNode[] {
  return list.children.flatMap((item: ListItem) => {
    const paragraph = item.children.find((child): child is Paragraph => child.type === "paragraph");
    const parts = fields(paragraph ? paragraph.children : []);
    const citation = splitCitation(parts[parts.length - 1]);
    const roles = ROW_FIELDS[kind];
    const cells = parts.map((content, index) => cell(roles[Math.min(index, roles.length - 1)], content));
    cells.push(cell("citation", citation));
    const row: EsquemaRowNode = {
      type: "esquemaRow",
      depth,
      children: cells,
      data: { hName: "div", hProperties: { "data-esquema-row": String(depth) } },
    };
    const nested = item.children.filter((child): child is List => child.type === "list");
    return [row, ...nested.flatMap((sub) => rows(sub, kind, depth + 1))];
  });
}

function isEsquema(node: Nodes): node is ContainerDirective {
  return node.type === "containerDirective" && node.name === "esquema";
}

export function transformEsquemas(tree: Root): void {
  const walk = (parent: Parent): void => {
    for (const child of parent.children as Nodes[]) {
      if (isEsquema(child)) {
        const kind = (child.attributes?.kind ?? "") as EsquemaKind;
        const title = child.attributes?.title ?? "";
        child.data = {
          ...child.data,
          hName: "div",
          hProperties: { "data-esquema-kind": kind, "data-esquema-title": title },
        };
        if (kind !== "tabla" && ESQUEMA_KINDS.includes(kind)) {
          const list = child.children.find((c): c is List => c.type === "list");
          if (list) child.children = rows(list, kind, 0) as never;
        }
      } else if ("children" in child) {
        walk(child as Parent);
      }
    }
  };
  walk(tree);
}

export const remarkEsquema: Plugin<[], Root> = () => (tree) => transformEsquemas(tree);
