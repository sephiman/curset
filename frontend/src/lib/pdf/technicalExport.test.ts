import { readFileSync } from "node:fs";
import { resolve } from "node:path";
import { describe, expect, it } from "vitest";
import type { Content, ContentText, TDocumentDefinitions } from "pdfmake/interfaces";
import type { PrintQuestionnaire } from "@/api/printQuestionnaire";
import { lessonSections } from "@/lib/pdf/document";
import { generateCoursePdf } from "@/lib/pdf/generate";
import { CODE_FONT } from "@/lib/pdf/page";
import { CONTENT_ROOT, courseContent, exportPart, outlineFromManifest } from "@/test/courseContent";
import { testPdfLabels } from "@/test/printLabels";

/**
 * backend-in-depth's tema m09-l04 exported with the Cuenta switch on, read off the document definition. The
 * questionnaire is the backend's own draw for seed 2026, pinned by
 * `test_the_technical_course_prints_its_bank_with_source_anchor_citations_and_no_case`; nothing is rendered.
 */

const SLUG = "backend-in-depth";
const TEMA = "m09-l04";
const labels = testPdfLabels("en");
const pinned = JSON.parse(
  readFileSync(resolve(__dirname, "../../test/fixtures/questionnaires", `${SLUG}-${TEMA}.json`), "utf-8"),
) as PrintQuestionnaire;

function valuesOf(node: unknown, key: string, found: unknown[] = []): unknown[] {
  if (Array.isArray(node)) node.forEach((child) => valuesOf(child, key, found));
  else if (typeof node === "object" && node !== null) {
    if (key in node) found.push((node as Record<string, unknown>)[key]);
    Object.values(node).forEach((child) => valuesOf(child, key, found));
  }
  return found;
}

function textOf(node: unknown): string {
  if (typeof node === "string") return node;
  if (Array.isArray(node)) return node.map(textOf).join("");
  if (typeof node === "object" && node !== null) {
    const record = node as Record<string, unknown>;
    if ("text" in record) return textOf(record.text);
    return ["stack", "columns"].map((key) => textOf(record[key] ?? "")).join(" ");
  }
  return "";
}

async function exportTema(): Promise<TDocumentDefinitions> {
  const course = courseContent(`${CONTENT_ROOT}/${SLUG}`);
  const meta = course.manifest().course;
  let built: TDocumentDefinitions | null = null;
  await generateCoursePdf({
    scope: { slug: SLUG, lang: "en" },
    part: { kind: "lesson", id: TEMA, title: TEMA.toUpperCase() },
    outline: outlineFromManifest(course.manifest(), "en"),
    exercises: "questionnaire",
    courseId: SLUG,
    courseTitle: meta.title.en,
    courseSubtitle: meta.subtitle.en,
    courseDescription: meta.description.en,
    labels,
    date: new Date(2026, 10, 14),
    fetchGlyph: async () => null,
    fetchExport: async () => exportPart(course.courseExport("en"), { kind: "lesson", id: TEMA }),
    fetchExercises: async () => {
      throw new Error("a question-bank course never prints embedded exercises");
    },
    fetchQuestionnaire: async () => pinned,
    onSkipped: () => undefined,
    renderPdf: async (definition) => {
      built = definition;
      return new Blob(["%PDF-"]);
    },
  });
  if (!built) throw new Error("nothing was typeset");
  return built;
}

describe("backend-in-depth, tema m09-l04 with exercises on", () => {
  it("prints 20 bank questions lettered A–D, with their code spans in the code face", async () => {
    const doc = await exportTema();
    const section = lessonSections(doc)[0];
    expect(valuesOf(section, "questionFor")).toEqual(pinned.temas[0].questions.map((q) => `${TEMA}#${q.number}`));
    const letters = valuesOf(section, "columns")
      .map((cells) => textOf((cells as Content[])[0]))
      .filter((cell) => /^[A-Z]\)$/.test(cell));
    expect(letters).toEqual(Array.from({ length: 20 }, () => ["A)", "B)", "C)", "D)"]).flat());

    const spans = pinned.temas[0].questions.flatMap((q) =>
      [q.prompt, ...q.options.map((o) => o.text)].flatMap((text) => [...text.matchAll(/`([^`]+)`/g)].map((m) => m[1])),
    );
    expect(spans.length).toBeGreaterThan(0);
    const coded = (valuesOf(section, "font") as string[]).filter((font) => font === CODE_FONT);
    expect(coded.length).toBeGreaterThanOrEqual(spans.length);
    const runs = valuesOf(section, "text").flat() as (string | ContentText)[];
    const codeTexts = runs.filter((run): run is ContentText => typeof run === "object" && run.font === CODE_FONT);
    expect(codeTexts.map((run) => run.text)).toEqual(expect.arrayContaining(spans));
    expect(textOf(section)).not.toMatch(/`[^`]+`/);
  });

  it("cites each answer in the key sheet as source_id#anchor, and prints the seed", async () => {
    const doc = await exportTema();
    const content = Array.isArray(doc.content) ? doc.content : [doc.content];
    const rows = (valuesOf(content[content.length - 1], "body").flat() as Content[][]).filter(
      (row) => Array.isArray(row) && valuesOf(row[0], "keyFor").length > 0,
    );
    const citations = rows.map((row) => textOf(row[2]));
    expect(citations).toEqual(pinned.temas[0].keys.map((k) => k.citation));
    expect(citations.every((c) => /^[a-z0-9-]+#\S+/.test(c))).toBe(true);
    const footer = doc.footer as (page: number, total: number) => Content;
    expect(textOf(footer(2, 9))).toContain(labels.seed(2026));
  });
});
