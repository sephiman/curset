import type { InlineCode, Nodes, Parent, PhrasingContent, Root, Text } from "mdast";
import type { LessonCitation } from "@/api/course";

/**
 * The third mark type: a citation («art. 67 CE») the backend found in the lesson.
 *
 * The backend's grammar is the ONE parser of citations (`backend/src/tradeschool/citations/`). This
 * module never detects one: it receives each citation's exact text, in reading order, and marks that
 * span where it stands — the same text the reader sees, so marking it changes no word of the lesson.
 * What it cannot place is reported, and the suite asserts that list is empty for every course.
 *
 * It runs after the glossary and reference annotator, over the same mdast. A glossary term or a
 * reference that falls inside a citation becomes plain text inside it: a link inside a link is a
 * control nobody can operate.
 */

export const CITATION = "citation";

export interface CitationNode extends Parent {
  type: "citation";
  href: string | null;
  ids: string[];
  title: string | null;
  children: PhrasingContent[];
  data: { hName: "span"; hProperties: { "data-citation": string } };
}

declare module "mdast" {
  interface PhrasingContentMap {
    citation: CitationNode;
  }
  interface RootContentMap {
    citation: CitationNode;
  }
}

/** Never read for citations: the backend's scan skips headings and code too. */
const SKIP = new Set(["heading", "code", "html", "yaml", "toml", "definition", "image", "imageReference"]);
/** Blocks and cells: a match never runs from one into the next. */
const BOUNDARIES = new Set(["paragraph", "tableCell", "listItem", "esquemaCell", "esquemaRow"]);
/** Marks that become plain text when a citation swallows them. */
const FLATTEN = new Set(["glossaryTerm", "lessonRef"]);

type Leaf = Text | InlineCode;

interface Located {
  leaf: Leaf;
  parent: Parent;
  /** Offset inside the leaf's value. */
  at: number;
}

interface Flattened {
  /** The lesson's readable text, whitespace runs collapsed to one space. */
  text: string;
  /** For each character of `text`, the leaf and the offset it came from. */
  origin: Located[];
}

function flatten(tree: Root): Flattened {
  let text = "";
  const origin: Located[] = [];
  const walk = (parent: Parent): void => {
    for (const child of parent.children as Nodes[]) {
      if (SKIP.has(child.type)) continue;
      if (child.type === "text" || child.type === "inlineCode") {
        for (let at = 0; at < child.value.length; at++) {
          const char = child.value[at];
          if (/\s/.test(char)) {
            if (text.endsWith(" ")) continue;
            text += " ";
          } else {
            text += char;
          }
          origin.push({ leaf: child, parent, at });
        }
      } else if ("children" in child) {
        walk(child as Parent);
        // A block boundary is a word boundary: never let a match run from one block into the next.
        if (BOUNDARIES.has(child.type)) {
          if (!text.endsWith(" ")) {
            text += " ";
            origin.push({ leaf: { type: "text", value: " " }, parent: child as Parent, at: 0 });
          }
        }
      }
    }
  };
  walk(tree);
  return { text, origin };
}

const WORD = /[\p{L}\p{N}_]/u;

function find(haystack: string, needle: string, from: number): number {
  let at = haystack.indexOf(needle, from);
  while (at >= 0) {
    const before = haystack[at - 1];
    const after = haystack[at + needle.length];
    const clean = (!before || !WORD.test(before) || !WORD.test(needle[0])) &&
      (!after || !WORD.test(after) || !WORD.test(needle[needle.length - 1]));
    if (clean) return at;
    at = haystack.indexOf(needle, at + 1);
  }
  return -1;
}

/** The chain of ancestors from the root down to `leaf`'s parent, found by identity. */
function pathTo(tree: Root, target: Nodes): Parent[] {
  const found: Parent[] = [];
  const walk = (parent: Parent): boolean => {
    for (const child of parent.children as Nodes[]) {
      if (child === target) {
        found.unshift(parent);
        return true;
      }
      if ("children" in child && walk(child as Parent)) {
        found.unshift(parent);
        return true;
      }
    }
    return false;
  };
  walk(tree);
  return found;
}

/** Splits `leaf` (a text node) at `at`, returning the node that now starts there. */
function splitText(parent: Parent, leaf: Text, at: number): Text {
  if (at === 0) return leaf;
  const index = parent.children.indexOf(leaf as never);
  const tail: Text = { type: "text", value: leaf.value.slice(at) };
  leaf.value = leaf.value.slice(0, at);
  parent.children.splice(index + 1, 0, tail as never);
  return tail;
}

function plain(nodes: PhrasingContent[]): PhrasingContent[] {
  return nodes.flatMap((node) =>
    FLATTEN.has(node.type) ? (plain((node as Parent).children as PhrasingContent[]) as PhrasingContent[]) : [node],
  );
}

function citationNode(citation: LessonCitation, children: PhrasingContent[]): CitationNode {
  return {
    type: CITATION,
    href: citation.href,
    ids: citation.ids,
    title: citation.title,
    children: plain(children),
    data: { hName: "span", hProperties: { "data-citation": JSON.stringify([citation.href, citation.ids, citation.title]) } },
  };
}

function edgeLeaf(node: Nodes, side: "first" | "last"): Nodes {
  let current = node;
  while ("children" in current && (current as Parent).children.length > 0) {
    const children = (current as Parent).children as Nodes[];
    current = side === "first" ? children[0] : children[children.length - 1];
  }
  return current;
}

/**
 * Wraps the characters [start, end) of the flattened text. Under their common parent, each end is
 * either a text node (split there) or a whole node (an inline code, a glossary mark) the range covers
 * entirely; anything else — a citation half inside emphasis — is left unmarked and reported.
 */
function wrap(tree: Root, flat: Flattened, start: number, end: number, citation: LessonCitation): boolean {
  const first = flat.origin[start];
  const last = flat.origin[end - 1];
  const firstPath = pathTo(tree, first.leaf);
  const lastPath = pathTo(tree, last.leaf);
  let depth = 0;
  while (depth < firstPath.length && depth < lastPath.length && firstPath[depth] === lastPath[depth]) depth++;
  const common = firstPath[depth - 1];
  if (!common) return false;
  let startNode = (firstPath[depth] ?? first.leaf) as Nodes;
  const endNode = (lastPath[depth] ?? last.leaf) as Nodes;

  // The end first, so an offset into a leaf both ends share stays where it was.
  if (endNode === last.leaf && last.leaf.type === "text") {
    if (last.at + 1 < last.leaf.value.length) splitText(common, last.leaf, last.at + 1);
  } else if (edgeLeaf(endNode, "last") !== last.leaf || last.at + 1 !== last.leaf.value.length) {
    return false;
  }
  if (startNode === first.leaf && first.leaf.type === "text") {
    const tail = splitText(common, first.leaf, first.at);
    if (endNode === first.leaf) {
      const covered = [tail] as PhrasingContent[];
      common.children.splice(common.children.indexOf(tail as never), 1, citationNode(citation, covered) as never);
      return true;
    }
    startNode = tail;
  } else if (edgeLeaf(startNode, "first") !== first.leaf || first.at !== 0) {
    return false;
  }
  const from = common.children.indexOf(startNode as never);
  const to = common.children.indexOf(endNode as never);
  if (from < 0 || to < from) return false;
  const covered = common.children.slice(from, to + 1) as PhrasingContent[];
  common.children.splice(from, to - from + 1, citationNode(citation, covered) as never);
  return true;
}

export interface CitationReport {
  placed: number;
  /** Citations whose text was not found, or not markable where it stands. The suite wants none. */
  missing: LessonCitation[];
}

export function annotateCitations(tree: Root, citations: LessonCitation[]): CitationReport {
  const report: CitationReport = { placed: 0, missing: [] };
  const flat = flatten(tree);
  const found: { start: number; end: number; citation: LessonCitation }[] = [];
  let cursor = 0;
  for (const citation of citations) {
    const needle = citation.text.replace(/\s+/g, " ");
    const start = find(flat.text, needle, cursor);
    if (start < 0) {
      report.missing.push(citation);
      continue;
    }
    found.push({ start, end: start + needle.length, citation });
    cursor = start + needle.length;
  }
  // Last first: a wrap splits and moves only nodes at or after its own start, so every position
  // found before it still points at the leaf and offset it was found at.
  for (const { start, end, citation } of found.reverse()) {
    if (wrap(tree, flat, start, end, citation)) report.placed += 1;
    else report.missing.push(citation);
  }
  return report;
}

/** Every character a reader sees, in order — what marking must leave untouched. */
export function readableText(tree: Root): string {
  return flatten(tree).text;
}
