// @vitest-environment node
import { existsSync, readFileSync } from "node:fs";
import { resolve } from "node:path";
import { unified } from "unified";
import remarkParse from "remark-parse";
import remarkGfm from "remark-gfm";
import type { Nodes, Root } from "mdast";
import { describe, expect, it } from "vitest";
import type { LessonCitation } from "@/api/course";
import { annotateCitations, readableText, type CitationNode } from "@/lib/citations/annotate";
import { remarkBlockDirectives } from "@/lib/directives";
import { transformEsquemas } from "@/lib/esquema";
import { annotateLesson, annotateLessonRefs } from "@/lib/glossary/annotate";
import { buildTermIndex } from "@/lib/glossary/terms";
import { buildRefRegistry } from "@/lib/refs/registry";
import { GOLDEN_COURSES, type CourseContent, type Locale } from "@/test/courseContent";

/**
 * The web marks every citation the backend found, where it stands, and changes no word doing it.
 *
 * The backend's golden `citations.<locale>.txt` lists each course's citations with their anchors
 * (`backend/tests/test_citations.py` writes it). Here every row of it is fed to the annotator over the
 * same tree `LessonMarkdown` builds — glossary and reference marks first — and every one must land.
 */

const processor = unified().use(remarkParse).use(remarkGfm).use(remarkBlockDirectives);

function parse(markdown: string): Root {
  const tree = processor.parse(markdown);
  transformEsquemas(tree);
  return tree;
}

function citation(text: string, ids: string[] = [], href: string | null = "/src.pdf#page=2"): LessonCitation {
  return { text, section: "prose", ids, href, title: null };
}

function marks(tree: Root): CitationNode[] {
  const found: CitationNode[] = [];
  const walk = (node: Nodes): void => {
    if (node.type === "citation") found.push(node);
    if ("children" in node) for (const child of node.children as Nodes[]) walk(child);
  };
  walk(tree);
  return found;
}

describe("marking a lesson's citations", () => {
  it("marks each citation's own text, inside its parentheses, and leaves every word where it was", () => {
    const tree = parse("El plazo es de un mes (art. 122.1 LPAC; m01-l1). Y otro (art. 14.2.d)\ny e) LPAC).");
    const before = readableText(tree);
    const report = annotateCitations(tree, [citation("art. 122.1 LPAC", ["lpac-art-122"]), citation("art. 14.2.d) y e) LPAC")]);
    expect(report).toEqual({ placed: 2, missing: [] });
    const markedText = (node: CitationNode) =>
      readableText({ type: "root", children: [{ type: "paragraph", children: node.children }] }).trim();
    expect(marks(tree).map(markedText)).toEqual([
      "art. 122.1 LPAC",
      "art. 14.2.d) y e) LPAC",
    ]);
    expect(marks(tree)[0].ids).toEqual(["lpac-art-122"]);
    expect(readableText(tree)).toBe(before);
  });

  it("marks a source file written as inline code", () => {
    const tree = parse("Lo resume la guía (fuente: `guia.html`, `otra.html`).");
    const report = annotateCitations(tree, [citation("guia.html"), citation("otra.html")]);
    expect(report.placed).toBe(2);
    expect(marks(tree).map((node) => node.children[0].type)).toEqual(["inlineCode", "inlineCode"]);
  });

  it("turns a glossary mark caught inside a citation into plain text, so no link sits inside a link", () => {
    const tree = parse("Según la ley (art. 53 de la Ley Orgánica 3/2007, de 22 de marzo).");
    annotateLesson(tree, {
      lessonId: "x",
      marked: new Set(),
      terms: buildTermIndex([{ id: "g-lo", term: "Ley Orgánica", origin: "y", originTitle: null }], "es"),
    });
    const before = readableText(tree);
    expect(annotateCitations(tree, [citation("art. 53 de la Ley Orgánica 3/2007, de 22 de marzo")]).missing).toEqual([]);
    const [mark] = marks(tree);
    expect(mark.children.every((child) => child.type === "text")).toBe(true);
    expect(readableText(tree)).toBe(before);
  });

  it("reports what it cannot find, and marks nothing in a heading", () => {
    const tree = parse("## Recursos (art. 1 CE)\n\nTexto sin citas.");
    const report = annotateCitations(tree, [citation("art. 1 CE")]);
    expect(report.placed).toBe(0);
    expect(report.missing.map((c) => c.text)).toEqual(["art. 1 CE"]);
  });

  it("marks the citations of every esquema kind in their own cell", () => {
    const tree = parse(
      ':::esquema{kind=plazos title="P"}\n1. Interposición — un mes (art. 122.1 LPAC)\n:::\n\n' +
        ':::esquema{kind=tabla title="T"}\n| Recurso | Artículo |\n|---|---|\n| Alzada | art. 122.1 LPAC |\n:::',
    );
    const report = annotateCitations(tree, [citation("art. 122.1 LPAC"), citation("art. 122.1 LPAC")]);
    expect(report).toEqual({ placed: 2, missing: [] });
  });
});

interface GoldenRow {
  lesson: string;
  citation: LessonCitation;
}

function goldenRows(course: CourseContent, locale: Locale): GoldenRow[] | null {
  const path = resolve(course.dir, `citations.${locale}.txt`);
  if (!existsSync(path)) return null;
  return readFileSync(path, "utf8")
    .split("\n")
    .filter((line) => line && !line.startsWith("#"))
    .map((line) => {
      const [lesson, section, , ids, , target, text] = line.split("\t");
      return {
        lesson,
        citation: {
          text,
          section: section as LessonCitation["section"],
          ids: ids === "-" ? [] : ids.split(","),
          href: target === "-" ? null : `/api/courses/${course.slug}/${target}`,
          title: null,
        },
      };
    });
}

const CASES = GOLDEN_COURSES.flatMap((course) =>
  course.languages
    .filter((locale) => goldenRows(course, locale) !== null)
    .map((locale) => [`${course.slug} ${locale}`, course, locale] as const),
);

describe.each(CASES)("the backend's citations, marked in every lesson (%s)", (_name, course, locale) => {
  it("places every citation of the golden and changes no word of any lesson", () => {
    const rows = goldenRows(course, locale) ?? [];
    const terms = buildTermIndex(course.glossary(locale), locale);
    const registry = buildRefRegistry(course.refModules(locale));
    const missing: string[] = [];
    const changed: string[] = [];
    let placed = 0;
    for (const lesson of course.lessons()) {
      const key = lesson.key ?? lesson.id;
      const citations = rows.filter((row) => row.lesson === key).map((row) => row.citation);
      if (citations.length === 0) continue;
      const tree = parse(course.lessonMarkdown(locale, lesson.id));
      annotateLesson(tree, { lessonId: lesson.id, terms, marked: new Set() });
      annotateLessonRefs(tree, { lessonId: lesson.id, registry });
      const before = readableText(tree);
      const report = annotateCitations(tree, citations);
      placed += report.placed;
      missing.push(...report.missing.map((c) => `${lesson.id}: «${c.text}»`));
      if (readableText(tree) !== before) changed.push(lesson.id);
      // Every anchor a question can target exists on the page, once.
      const ids = marks(tree).flatMap((node) => node.ids);
      expect(new Set(ids).size, `${lesson.id} repeats an anchor id`).toBe(ids.length);
    }
    expect(missing, "citations the web could not mark").toEqual([]);
    expect(changed, "lessons whose text the marking changed").toEqual([]);
    expect(placed).toBe(rows.length);
  }, 120_000);
});
