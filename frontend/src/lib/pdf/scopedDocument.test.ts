import { describe, expect, it } from "vitest";
import type { Content, TDocumentDefinitions } from "pdfmake/interfaces";
import type { CourseExport, GlossaryEntry } from "@/api/course";
import type { PrintQuestionnaire } from "@/api/printQuestionnaire";
import { coverArt } from "@/lib/pdf/coverArt";
import {
  answerEntries,
  buildCourseDocument,
  exerciseBlocks,
  lessonSections,
  type BuildCourseDocumentOptions,
  type DocumentPart,
} from "@/lib/pdf/document";
import { DEST } from "@/lib/pdf/pagination";
import { pdfFilename } from "@/lib/pdf/generate";
import { courseExportFromContent, figureDirectives, stubFigures } from "@/test/courseContent";
import { printExercisesFromContent, stubExerciseCharts } from "@/test/printExercises";
import { testPdfLabels } from "@/test/printLabels";

/**
 * A tema or bloque printed on its own (delta N), read off the document definition — no PDF is rendered.
 * The export a scoped build receives is already cut to its part by the server.
 */

const labels = testPdfLabels("es");
const MARK = coverArt(null, undefined);

const GLOSSARY: GlossaryEntry[] = [
  { id: "g-silencio", term: "silencio administrativo", origin: "m01-l1", originTitle: "Días", definition: "d1" },
  { id: "g-alzada", term: "recurso de alzada", origin: "m02-l1", originTitle: "Recursos", definition: "d2" },
  { id: "g-reposicion", term: "recurso de reposición", origin: "m02-l1", originTitle: "Recursos", definition: "d3" },
  { id: "g-plazo", term: "plazo", origin: "m02-l1", originTitle: "Recursos", definition: "d4" },
  { id: "g-termino", term: "término", origin: "m02-l1", originTitle: "Recursos", aliasOf: { id: "g-plazo", term: "plazo" } },
];

function lesson(id: string, title: string, prose: string) {
  return {
    id,
    title,
    markdown: `# ${title}\n\n${prose}\n`,
    normativa: [{ name: "Ley 39/2015", title: "LPAC", consolidatedAsOf: id === "m01-l2" ? "2026-10-01" : "2025-06-02" }],
  };
}

/** Module m01 of a two-module course, as `/export?scope=m01` serves it. */
const BLOQUE: CourseExport = {
  locale: "es",
  glossary: GLOSSARY,
  blocks: [
    {
      id: "block-a",
      title: "Programa",
      modules: [
        {
          id: "m01",
          title: "Plazos",
          summary: "Cómo se cuentan.",
          lessons: [
            lesson("m01-l1", "Días", "El silencio administrativo opera al vencer el término. Véase m01-l2 y m02-l1."),
            lesson("m01-l2", "Meses", "El recurso de alzada se cuenta por meses, según m01-l1."),
          ],
        },
      ],
    },
  ],
};

const TEMA: CourseExport = {
  ...BLOQUE,
  blocks: [{ ...BLOQUE.blocks[0], modules: [{ ...BLOQUE.blocks[0].modules[0], lessons: [BLOQUE.blocks[0].modules[0].lessons[0]] }] }],
};

const BLOQUE_PART: DocumentPart = { kind: "module", id: "m01", title: "M01 · Plazos" };
const TEMA_PART: DocumentPart = { kind: "lesson", id: "m01-l1", title: "M01-L1 · Días" };

const QUESTIONNAIRE: PrintQuestionnaire = {
  seed: 4242,
  locale: "es",
  temas: [
    {
      lessonId: "m01-l1",
      title: "Días",
      questions: [
        {
          id: "m01-ex-1/q1",
          number: "1",
          prompt: "¿Cuándo vence?",
          options: [
            { letter: "A", text: "Al día siguiente" },
            { letter: "B", text: "El último día" },
            { letter: "C", text: "Nunca" },
            { letter: "D", text: "A los tres días" },
          ],
        },
        {
          id: "m01-ex-1/q2",
          number: "2",
          prompt: "¿Cómo se cuenta?",
          options: [
            { letter: "A", text: "Por días hábiles" },
            { letter: "B", text: "Por días naturales" },
            { letter: "C", text: "Por horas" },
            { letter: "D", text: "Por semanas" },
          ],
        },
      ],
      keys: [
        { number: "1", letter: "B", citation: "art. 30.2 LPAC" },
        { number: "2", letter: "A", citation: "art. 30.2 LPAC" },
      ],
    },
    {
      lessonId: "m01-l2",
      title: "Meses",
      questions: [
        {
          id: "m01-ex-2/q1",
          number: "1",
          prompt: "¿De fecha a fecha?",
          options: [
            { letter: "A", text: "Sí" },
            { letter: "B", text: "No" },
            { letter: "C", text: "Solo en agosto" },
            { letter: "D", text: "Solo en recursos" },
          ],
        },
      ],
      keys: [{ number: "1", letter: "A", citation: "art. 30.4 LPAC" }],
    },
  ],
};

function build(o: Partial<BuildCourseDocumentOptions> & Pick<BuildCourseDocumentOptions, "export">): TDocumentDefinitions {
  return buildCourseDocument({
    courseTitle: "Administrativo del Estado (C1)",
    courseSubtitle: "Ingreso libre",
    courseDescription: "El programa.",
    cover: MARK,
    figures: new Map(),
    exercises: { locale: "es", lessons: [], excluded: [] },
    pdfExercises: false,
    exerciseCharts: new Map(),
    labels,
    ...o,
  });
}

function contentOf(doc: TDocumentDefinitions): Content[] {
  return Array.isArray(doc.content) ? doc.content : [doc.content];
}

/** Every value a key takes anywhere in the definition, in document order. */
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

function footerAt(doc: TDocumentDefinitions, page: number, total: number): Content[] {
  const footer = doc.footer as (current: number, count: number) => { columns: Content[] };
  return footer(page, total).columns;
}

describe("the cover of a bloque", () => {
  const cover = contentOf(build({ export: BLOQUE, part: BLOQUE_PART }))[0];
  const text = textOf(cover);

  it("carries the platform mark, the course and the bloque title", () => {
    expect(valuesOf(cover, "svg")[0]).toBe(MARK.mark);
    expect(text).toContain("Administrativo del Estado (C1)");
    expect(text).toContain("M01 · Plazos");
  });

  it("names the language and the date, and the latest consolidation date of its norms", () => {
    expect(text).toContain(labels.generated);
    expect(text).toContain(labels.coverConsolidated("2026-10-01"));
  });

  it("has no consolidation line for a course that keeps no norms", () => {
    const plain = { ...BLOQUE, blocks: BLOQUE.blocks.map((b) => ({ ...b, modules: b.modules.map((m) => ({ ...m, lessons: m.lessons.map(({ normativa: _, ...l }) => l) })) })) };
    expect(textOf(contentOf(build({ export: plain, part: BLOQUE_PART }))[0])).not.toContain("consolidada");
  });
});

describe("the contents", () => {
  it("lists a bloque of more than one tema", () => {
    expect(valuesOf(contentOf(build({ export: BLOQUE, part: BLOQUE_PART })), "toc")).toHaveLength(1);
  });

  it("is left out of a tema, which has nothing to find", () => {
    expect(valuesOf(contentOf(build({ export: TEMA, part: TEMA_PART })), "toc")).toHaveLength(0);
  });
});

describe("the lessons", () => {
  it("print in course order, each on its own page, as in the whole-course book", () => {
    const sections = lessonSections(build({ export: BLOQUE, part: BLOQUE_PART }));
    expect(sections.map((s) => s.lessonId)).toEqual(["m01-l1", "m01-l2"]);
    expect(sections.every((s) => s.pageBreak === "before")).toBe(true);
    const whole = lessonSections(build({ export: BLOQUE }));
    expect(sections.map((s) => textOf(s))).toEqual(whole.map((s) => textOf(s)));
  });

  it("link a reference inside the scope to its page and print one outside it as text", () => {
    const doc = build({ export: BLOQUE, part: BLOQUE_PART });
    const links = valuesOf(contentOf(doc), "linkToDestination");
    expect(links).toContain(DEST.outline("m01-l2"));
    expect(links).toContain(DEST.outline("m01-l1"));
    expect(links).not.toContain(DEST.outline("m02-l1"));
    expect(textOf(lessonSections(doc)[0])).toContain("m02-l1");
  });

  it("in a tema print even a reference to a sibling tema of the same bloque as text", () => {
    const links = valuesOf(contentOf(build({ export: TEMA, part: TEMA_PART })), "linkToDestination");
    expect(links).not.toContain(DEST.outline("m01-l2"));
  });
});

describe("the glossary of a bloque", () => {
  const doc = build({ export: BLOQUE, part: BLOQUE_PART });
  const terms = valuesOf(contentOf(doc), "id").filter((id) => typeof id === "string" && id.startsWith("gdest-"));

  it("keeps the terms its prose uses or teaches, and the entries their aliases point to", () => {
    expect(terms).toEqual(
      expect.arrayContaining([DEST.term("g-silencio"), DEST.term("g-alzada"), DEST.term("g-termino"), DEST.term("g-plazo")]),
    );
  });

  it("leaves out the terms that never appear in it", () => {
    expect(terms).not.toContain(DEST.term("g-reposicion"));
  });

  it("prints an origin outside the scope as text, with no link", () => {
    const links = valuesOf(contentOf(doc), "linkToDestination");
    expect(textOf(contentOf(doc))).toContain("M02-L1 · Recursos");
    expect(links).not.toContain(DEST.outline("m02-l1"));
  });

  it("is the whole glossary in the whole-course book", () => {
    const whole = valuesOf(contentOf(build({ export: BLOQUE })), "id").filter((id) => typeof id === "string" && id.startsWith("gdest-"));
    expect(whole).toContain(DEST.term("g-reposicion"));
  });
});

describe("the footer of a scoped document", () => {
  const doc = build({ export: BLOQUE, part: BLOQUE_PART });

  it("is blank on the cover", () => {
    expect((doc.footer as (c: number, t: number) => { text?: string })(1, 9)).toEqual({ text: "" });
  });

  it("carries the monochrome wordmark and «N de M»", () => {
    const [wordmark, , page] = footerAt(doc, 3, 9);
    expect(valuesOf(wordmark, "svg")).toEqual([MARK.wordmark]);
    expect(textOf(page)).toBe("3 de 9");
  });

  it("is unchanged in the whole-course book", () => {
    const whole = footerAt(build({ export: BLOQUE }), 3, 9);
    expect(valuesOf(whole, "svg")).toEqual([]);
    expect(textOf(whole[1])).toBe(labels.page(3, 9));
  });
});

describe("the file name", () => {
  it("names the bloque or tema between the course and the language", () => {
    const day = new Date(2026, 10, 13);
    expect(pdfFilename("age-administrativo-c1", "es", day, "m03")).toBe("curset-age-administrativo-c1-m03-es-2026-11-13.pdf");
    expect(pdfFilename("age-administrativo-c1", "es", day, "m03-l04")).toBe("curset-age-administrativo-c1-m03-l04-es-2026-11-13.pdf");
    expect(pdfFilename("age-administrativo-c1", "es", day)).toBe("curset-age-administrativo-c1-es-2026-11-13.pdf");
  });
});

describe("with exercises on, a question-bank course", () => {
  const doc = build({ export: BLOQUE, part: BLOQUE_PART, questionnaire: QUESTIONNAIRE });

  it("prints each tema's questions after its prose, inside its section", () => {
    const sections = lessonSections(doc);
    expect(sections.map((s) => valuesOf(s, "questionFor"))).toEqual([
      ["m01-l1#1", "m01-l1#2"],
      ["m01-l2#1"],
    ]);
    expect(textOf(sections[0])).toContain(labels.questionnaire);
  });

  it("letters the options A–D in printed order", () => {
    const sections = lessonSections(doc);
    const rows = valuesOf(sections[0], "columns")
      .map((cols) => (cols as Content[]).map(textOf))
      .filter((cells) => /^[A-D]\)$/.test(cells[0] ?? ""));
    expect(rows.slice(0, 4)).toEqual([
      ["A)", "Al día siguiente"],
      ["B)", "El último día"],
      ["C)", "Nunca"],
      ["D)", "A los tres días"],
    ]);
  });

  it("ends with a key sheet giving each answer's letter and the article it rests on", () => {
    const content = contentOf(doc);
    const keySheet = content[content.length - 1];
    expect(textOf(keySheet)).toContain(labels.questionnaireKey);
    const rows = valuesOf(keySheet, "body").flat() as Content[][];
    const keyed = rows.filter((row) => Array.isArray(row) && valuesOf(row[0], "keyFor").length > 0);
    expect(keyed.map((row) => [valuesOf(row[0], "keyFor")[0], textOf(row[1]), textOf(row[2])])).toEqual([
      ["m01-l1#1", "B", "art. 30.2 LPAC"],
      ["m01-l1#2", "A", "art. 30.2 LPAC"],
      ["m01-l2#1", "A", "art. 30.4 LPAC"],
    ]);
  });

  it("keys every printed question and prints every keyed one", () => {
    const asked = valuesOf(contentOf(doc), "questionFor");
    const keyed = valuesOf(contentOf(doc), "keyFor");
    expect(new Set(asked)).toEqual(new Set(keyed));
    expect(asked).toHaveLength(keyed.length);
  });

  it("prints the seed in the footer, so the paper can be drawn again", () => {
    expect(textOf(footerAt(doc, 2, 9)[1])).toContain(labels.seed(4242));
  });

  it("builds the same definition from the same seed's draw", () => {
    const again = build({ export: BLOQUE, part: BLOQUE_PART, questionnaire: structuredClone(QUESTIONNAIRE) });
    expect(JSON.stringify(again.content)).toBe(JSON.stringify(doc.content));
    expect(JSON.stringify(footerAt(again, 4, 9))).toBe(JSON.stringify(footerAt(doc, 4, 9)));
  });
});

describe("with exercises off", () => {
  it("prints the theory only: no questions, no key sheet, no seed", () => {
    const doc = build({ export: BLOQUE, part: BLOQUE_PART });
    expect(valuesOf(contentOf(doc), "questionFor")).toEqual([]);
    expect(textOf(contentOf(doc))).not.toContain(labels.questionnaireKey);
    expect(textOf(footerAt(doc, 2, 9)[1])).not.toContain(labels.seed(4242));
  });
});

describe("crypto-futures, one module with exercises on", () => {
  // The module the server would serve for `scope=m11`, cut from the whole export.
  const whole = courseExportFromContent("en");
  const part: CourseExport = {
    ...whole,
    blocks: whole.blocks
      .map((block) => ({ ...block, modules: block.modules.filter((module) => module.id === "m11") }))
      .filter((block) => block.modules.length > 0),
  };
  const exercises = printExercisesFromContent("en");
  const doc = buildCourseDocument({
    courseTitle: "Crypto",
    courseSubtitle: "Guide",
    courseDescription: "D",
    export: part,
    figures: stubFigures(figureDirectives("en")),
    exercises,
    exerciseCharts: stubExerciseCharts(exercises, "png"),
    part: { kind: "module", id: "m11", title: "M11 · Module" },
    labels: testPdfLabels("en"),
  });
  const printedLessons = new Set(part.blocks.flatMap((b) => b.modules.flatMap((m) => m.lessons.map((l) => l.id))));
  const scoped = exercises.lessons.filter((l) => printedLessons.has(l.lessonId)).flatMap((l) => l.exercises.map((e) => e.id));

  it("prints exactly the module's exercises, each answered once at the back, and nothing else", () => {
    expect(scoped.length).toBeGreaterThan(0);
    const printed = exerciseBlocks(doc).map((e) => e.exerciseId);
    const answered = answerEntries(doc).map((a) => a.answerFor);
    expect(printed).toEqual(scoped);
    expect(answered).toEqual(scoped);
  });
});
