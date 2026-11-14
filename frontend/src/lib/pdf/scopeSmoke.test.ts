// @vitest-environment node
// On request only: real pdfmake renders of a tema, a bloque and the whole course of the small Spanish
// fixture course (no figures). Skipped unless PDF_SMOKE is set, so neither CI nor close_round.sh runs it:
//   PDF_SMOKE=1 npx vitest run src/lib/pdf/scopeSmoke.test.ts
import { describe, expect, it } from "vitest";
import type { DocumentPart } from "@/lib/pdf/document";
import { generateCoursePdf } from "@/lib/pdf/generate";
import { courseContent, exportPart, FIXTURE_CONTENT_ROOT, glyphFromContent, printFontFamiliesOnDisk } from "@/test/courseContent";
import { testPdfLabels } from "@/test/printLabels";

const course = courseContent(`${FIXTURE_CONTENT_ROOT}/fixture-oposiciones`);

const SCOPES: [string, DocumentPart | undefined][] = [
  ["tema", { kind: "lesson", id: "m01-l1", title: "M01-L1" }],
  ["bloque", { kind: "module", id: "m01", title: "M01" }],
  ["course", undefined],
];

describe.runIf(process.env.PDF_SMOKE)("a real render per scope (fixture-oposiciones)", () => {
  it.each(SCOPES)("typesets the %s", async (name, part) => {
    const pdfmake = (await import("pdfmake")).default;
    pdfmake.addFonts(printFontFamiliesOnDisk());
    const meta = course.manifest().course;
    const started = performance.now();
    const generated = await generateCoursePdf({
      scope: { slug: course.slug, lang: "es" },
      part,
      exercises: "none",
      fetchGlyph: glyphFromContent,
      courseId: course.slug,
      courseTitle: meta.title.es,
      courseSubtitle: meta.subtitle.es,
      courseDescription: meta.description.es,
      labels: testPdfLabels("es"),
      date: new Date(2026, 10, 13),
      onSkipped: () => undefined,
      fetchExport: async (scope) => (part ? exportPart(course.courseExport(scope.lang), part) : course.courseExport(scope.lang)),
      captureAll: async () => {
        throw new Error("a course without figures must never reach figure capture");
      },
      renderPdf: async (definition) =>
        new Blob([new Uint8Array(await pdfmake.createPdf(definition).getBuffer())], { type: "application/pdf" }),
    });
    const seconds = ((performance.now() - started) / 1000).toFixed(2);
    console.info(`PDF smoke ${name}: ${generated.filename}, ${generated.blob.size} bytes, ${seconds}s`);
    const head = new TextDecoder().decode(new Uint8Array(await generated.blob.arrayBuffer()).subarray(0, 5));
    expect(head).toBe("%PDF-");
  }, 120_000);
});
