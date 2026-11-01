import { beforeEach, describe, expect, it, vi } from "vitest";
import type { FigureData } from "@/api/course";
import { downloadPdf, generateCoursePdf, pdfFilename, type GenerateProgress } from "@/lib/pdf/generate";
import { testPdfLabels } from "@/test/printLabels";

/**
 * What the export does when a figure will not come out: it stops, naming the figure — the prose quotes
 * the numbers that figure draws.
 */

const getFigure = vi.fn<(id: string) => Promise<FigureData>>();
vi.mock("@/api/course", () => ({ getFigure: (_scope: unknown, id: string) => getFigure(id) }));

const { captureFigures } = await import("@/lib/pdf/figures");
const SCOPE = { slug: "crypto-futures", lang: "en" } as const;

/** Read at module scope on purpose: reading it inside a test would compare a leaked ratio to itself. */
const PRISTINE_PIXEL_RATIO = window.devicePixelRatio;

beforeEach(() => {
  getFigure.mockReset();
});

describe("capturing figures", () => {
  it("stops, naming the figure, when it cannot be loaded", async () => {
    getFigure.mockRejectedValue(new Error("503"));
    await expect(captureFigures(SCOPE, ["fig-m09-accumulation"])).rejects.toThrowError(
      /figure fig-m09-accumulation could not be loaded/,
    );
  });

  it("stops when a hand-drawn figure names a drawing the print renderer does not have", async () => {
    getFigure.mockResolvedValue({ id: "fig-x", kind: "svg", caption: "c", svg: "not-a-drawing" });
    await expect(captureFigures(SCOPE, ["fig-x"])).rejects.toThrowError(
      /figure fig-x: no print renderer for svg "not-a-drawing"/,
    );
  });

  it("stops when a chart figure arrives with no panels", async () => {
    getFigure.mockResolvedValue({ id: "fig-y", kind: "chart", caption: "c", panels: [] });
    await expect(captureFigures(SCOPE, ["fig-y"])).rejects.toThrowError(/figure fig-y: chart figure has no panels/);
  });

  it("leaves the page's pixel ratio as it found it, even when it fails", async () => {
    getFigure.mockRejectedValue(new Error("503"));
    await expect(captureFigures(SCOPE, ["fig-z"])).rejects.toThrow();
    expect(window.devicePixelRatio).toBe(PRISTINE_PIXEL_RATIO);
  });

  it("reports progress per distinct figure, drawing a repeated one once", async () => {
    // Both ids fail on load; this only has to prove the total the button counts down from.
    const seen: { done: number; total: number }[] = [];
    getFigure.mockRejectedValue(new Error("503"));
    await expect(
      captureFigures(SCOPE, ["a", "b", "a"], ({ done, total }) => seen.push({ done, total })),
    ).rejects.toThrow();
    expect(seen).toEqual([{ done: 0, total: 2 }]);
  });
});

describe("the file the reader gets", () => {
  it("is named for the platform, the course slug, the locale and the day, zero-padded", () => {
    expect(pdfFilename("crypto-futures", "es", new Date(2026, 0, 5))).toBe(
      "curset-crypto-futures-es-2026-01-05.pdf",
    );
  });

  it("downloads under that name", () => {
    const created: string[] = [];
    vi.stubGlobal("URL", {
      createObjectURL: () => {
        created.push("blob:x");
        return "blob:x";
      },
      revokeObjectURL: () => {},
    });
    const clicks: HTMLAnchorElement[] = [];
    const click = vi
      .spyOn(HTMLAnchorElement.prototype, "click")
      .mockImplementation(function (this: HTMLAnchorElement) {
        clicks.push(this);
      });
    try {
      downloadPdf({ blob: new Blob(["%PDF-"]), filename: "curset-x-en-2026-08-03.pdf" });
    } finally {
      click.mockRestore();
      vi.unstubAllGlobals();
    }
    expect(created).toHaveLength(1);
    expect(clicks[0]?.download).toBe("curset-x-en-2026-08-03.pdf");
    expect(document.querySelector("a[download]")).toBeNull(); // and it cleans up after itself
  });
});

describe("generating course PDF with pdfExercises: false", () => {
  it("skips fetching exercises and passes pdfExercises to buildCourseDocument", async () => {
    const fetchExercises = vi.fn();
    const fetchExport = vi.fn().mockResolvedValue({
      locale: "es",
      blocks: [],
      glossary: [],
    });
    const renderPdf = vi.fn().mockResolvedValue(new Blob(["%PDF-"]));
    const progress: GenerateProgress[] = [];

    const generated = await generateCoursePdf({
      scope: SCOPE,
      courseId: "age-administrativo-c1",
      courseTitle: "Admin",
      courseSubtitle: "Subtitle",
      courseDescription: "Desc",
      pdfExercises: false,
      labels: testPdfLabels("es"),
      date: new Date(2026, 9, 4),
      onProgress: (p) => progress.push(p),
      fetchExport,
      fetchExercises,
      renderPdf,
    });

    expect(fetchExercises).not.toHaveBeenCalled();
    expect(progress.map((p) => p.phase)).toEqual(["export", "typeset"]);
    expect(generated.filename).toBe("curset-age-administrativo-c1-en-2026-10-04.pdf");
  });
});
