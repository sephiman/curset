import { readFileSync } from "node:fs";
import { resolve } from "node:path";
import { describe, expect, it } from "vitest";
import type { Content, TDocumentDefinitions } from "pdfmake/interfaces";
import type { PrintQuestionnaire } from "@/api/printQuestionnaire";
import { lessonSections } from "@/lib/pdf/document";
import { pdfExerciseMode } from "@/lib/pdf/exerciseMode";
import { generateCoursePdf } from "@/lib/pdf/generate";
import { CONTENT_ROOT, courseContent, exportPart, outlineFromManifest } from "@/test/courseContent";
import { testPdfLabels } from "@/test/printLabels";

/**
 * One tema of each oposiciones course exported with the Cuenta switch off and on (delta N9), read off the
 * document definition. The questionnaires are the backend's own draw for seed 2026, pinned by
 * `test_the_pinned_questionnaire_the_frontend_prints_is_this_seeds_draw`; nothing is rendered.
 */

const TEMA = "m01-l01";
const COURSES = ["age-administrativo-c1", "age-auxiliar-c2", "aeat-agentes-hacienda"] as const;
const labels = testPdfLabels("es");

function pinned(slug: string): PrintQuestionnaire {
  const file = resolve(__dirname, "../../test/fixtures/questionnaires", `${slug}-${TEMA}.json`);
  return JSON.parse(readFileSync(file, "utf-8")) as PrintQuestionnaire;
}

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
  if (Array.isArray(node)) return node.map(textOf).join(" ");
  if (typeof node === "object" && node !== null) {
    const record = node as Record<string, unknown>;
    if ("text" in record) return textOf(record.text);
    return ["stack", "columns"].map((key) => textOf(record[key] ?? "")).join(" ");
  }
  return "";
}

async function exportTema(slug: string, include: boolean): Promise<TDocumentDefinitions> {
  const course = courseContent(`${CONTENT_ROOT}/${slug}`);
  const meta = course.manifest().course;
  let built: TDocumentDefinitions | null = null;
  await generateCoursePdf({
    scope: { slug, lang: "es" },
    part: { kind: "lesson", id: TEMA, title: TEMA.toUpperCase() },
    outline: outlineFromManifest(course.manifest(), "es"),
    exercises: pdfExerciseMode({ pdfExercises: meta.pdf_exercises, lessonPractice: meta.lesson_practice }, include),
    courseId: slug,
    courseTitle: meta.title.es,
    courseSubtitle: meta.subtitle.es,
    courseDescription: meta.description.es,
    labels,
    date: new Date(2026, 10, 14),
    fetchGlyph: async () => null,
    fetchExport: async () => exportPart(course.courseExport("es"), { kind: "lesson", id: TEMA }),
    fetchExercises: async () => {
      throw new Error("an oposiciones course never prints embedded exercises");
    },
    fetchQuestionnaire: async (_scope, part) => {
      expect(part).toBe(TEMA);
      return pinned(slug);
    },
    onSkipped: () => undefined,
    renderPdf: async (definition) => {
      built = definition;
      return new Blob(["%PDF-"]);
    },
  });
  if (!built) throw new Error("nothing was typeset");
  return built;
}

function footerText(doc: TDocumentDefinitions): string {
  const footer = doc.footer as (page: number, total: number) => Content;
  return textOf(footer(2, 9));
}

describe.each(COURSES)("%s, tema m01-l01", (slug) => {
  it("prints theory only with the switch off", async () => {
    const doc = await exportTema(slug, false);
    expect(lessonSections(doc).map((s) => s.lessonId)).toEqual([TEMA]);
    expect(valuesOf(doc.content, "questionFor")).toEqual([]);
    expect(valuesOf(doc.content, "keyFor")).toEqual([]);
    expect(footerText(doc)).not.toContain(labels.seed(2026));
  });

  it("prints its 20-question questionnaire lettered A–D, the key sheet with citations and the seed, with the switch on", async () => {
    const doc = await exportTema(slug, true);
    const paper = pinned(slug).temas[0];
    const section = lessonSections(doc)[0];
    const asked = valuesOf(section, "questionFor");
    expect(asked).toHaveLength(20);
    expect(asked).toEqual(paper.questions.map((q) => `${TEMA}#${q.number}`));

    const letters = valuesOf(section, "columns")
      .map((cells) => textOf((cells as Content[])[0]))
      .filter((cell) => /^[A-Z]\)$/.test(cell));
    expect(letters).toEqual(Array.from({ length: 20 }, () => ["A)", "B)", "C)", "D)"]).flat());

    const content = Array.isArray(doc.content) ? doc.content : [doc.content];
    const keySheet = content[content.length - 1];
    const rows = (valuesOf(keySheet, "body").flat() as Content[][]).filter(
      (row) => Array.isArray(row) && valuesOf(row[0], "keyFor").length > 0,
    );
    expect(rows.map((row) => [textOf(row[1]), textOf(row[2])])).toEqual(paper.keys.map((k) => [k.letter, k.citation]));
    expect(rows.every((row) => textOf(row[2]).length > 0)).toBe(true);

    expect(footerText(doc)).toContain(labels.seed(2026));
  });
});
