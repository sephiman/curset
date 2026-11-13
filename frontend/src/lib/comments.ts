import type { Root, RootContent } from "mdast";
import type { Plugin } from "unified";

const COMMENT = /^<!--[\s\S]*-->\s*$/;

function withoutComments(nodes: RootContent[]): RootContent[] {
  return nodes
    .filter((node) => !(node.type === "html" && COMMENT.test(node.value)))
    .map((node) => ("children" in node ? { ...node, children: withoutComments(node.children as RootContent[]) } : node) as RootContent);
}

/** Drops HTML comments (`<!-- bullets: 6.2.a -->`), which are authoring metadata; other raw HTML stays as text. */
export const remarkHideComments: Plugin<[], Root> = () => (tree) => {
  tree.children = withoutComments(tree.children);
};
