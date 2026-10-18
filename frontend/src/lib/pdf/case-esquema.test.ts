// @vitest-environment node
import type { Content } from "pdfmake/interfaces";
import { describe, expect, it } from "vitest";
import type { PrintExercise } from "@/api/course";
import { answerEntry, answerLines, exerciseBlock } from "@/lib/pdf/exercises";
import { appendNormativa, lessonToContent } from "@/lib/pdf/markdown";
import { FIXTURE_CONTENT_ROOT, courseContent } from "@/test/courseContent";
import { testPdfLabels } from "@/test/printLabels";

/** The book's case (delta B5), esquemas (E3) and «Normativa» block (C5). */

const labels = testPdfLabels("es");
const fixture = courseContent(`${FIXTURE_CONTENT_ROOT}/fixture-oposiciones`);
const lesson = fixture.lessonMarkdown("es", "m02-l1");

/** Every string the content prints, in order — what a reader would find on the page. */
function texts(node: unknown, out: string[] = []): string[] {
  if (typeof node === "string") out.push(node);
  else if (Array.isArray(node)) node.forEach((child) => texts(child, out));
  else if (node && typeof node === "object") {
    const record = node as Record<string, unknown>;
    for (const key of ["text", "stack", "columns", "ul", "ol", "table", "body"]) if (key in record) texts(record[key], out);
  }
  return out;
}

function tables(node: unknown, out: { body: Content[][] }[] = []): { body: Content[][] }[] {
  if (Array.isArray(node)) node.forEach((child) => tables(child, out));
  else if (node && typeof node === "object") {
    const record = node as Record<string, unknown>;
    if (record.table) out.push(record.table as { body: Content[][] });
    for (const value of Object.values(record)) if (typeof value === "object") tables(value, out);
  }
  return out;
}

function links(node: unknown, out: string[] = []): string[] {
  if (Array.isArray(node)) node.forEach((child) => links(child, out));
  else if (node && typeof node === "object") {
    const record = node as Record<string, unknown>;
    if (typeof record.link === "string") out.push(record.link);
    for (const value of Object.values(record)) if (typeof value === "object") links(value, out);
  }
  return out;
}

const rendered = lessonToContent(
  lesson,
  { figure: () => ({ text: "" }), esquemaColumns: labels.esquemaColumns },
  "m02-l1",
  // What the backend's export carries for this lesson (`normativa`, from the course's normativa.yaml).
  (tree) =>
    appendNormativa(
      tree,
      [
        {
          name: "Ley 39/2015 (LPAC)",
          title: "Ley 39/2015, de 1 de octubre, del Procedimiento Administrativo Común de las Administraciones Públicas",
          consolidatedAsOf: "2024-11-06",
        },
        {
          name: "Ley 40/2015 (LRJSP)",
          title: "Ley 40/2015, de 1 de octubre, de Régimen Jurídico del Sector Público",
          consolidatedAsOf: "2024-08-02",
        },
      ],
      labels.consolidated,
    ),
);

describe("an esquema in the book", () => {
  it("prints every kind as a table, the list kinds under a header row", () => {
    const [arbol, tabla, plazos, pasos] = tables(rendered);
    expect(texts(tabla.body[0])).toEqual(["Recurso", "Ante quién se presenta", "Plazo con acto expreso", "Artículo"]);
    expect(texts(plazos.body)).toEqual([...labels.esquemaColumns.plazos, "Interposición", "un mes", "art. 122.1 LPAC", "Resolución", "tres meses", "art. 122.2 LPAC"]);
    expect(texts(pasos.body[0])).toEqual(labels.esquemaColumns.pasos);
    expect(pasos.body[1]).toHaveLength(4);
    // A tree keeps its shape as indentation in the first column.
    const margins = arbol.body.slice(1).map((row) => (row[0] as { margin: number[] }).margin[0]);
    expect(margins).toEqual([0, 12, 0]);
  });

  it("prints citations as text, never as a link to a local file", () => {
    expect(texts(rendered).join(" ")).toContain("art. 9.1 LRJSP");
    expect(links(rendered)).toEqual([]);
  });
});

describe("the «Normativa» block in the book", () => {
  it("prints each norm's title and the date of the consolidated text", () => {
    const printed = texts(rendered).join("");
    expect(printed).toContain(
      "Ley 39/2015, de 1 de octubre, del Procedimiento Administrativo Común de las Administraciones Públicas (texto consolidado a 2024-11-06).",
    );
    expect(printed).toContain("(texto consolidado a 2024-08-02).");
  });
});

const CASE: PrintExercise = {
  id: "m02-ex-4",
  number: "2.4",
  type: "case",
  isChart: false,
  seed: 1,
  prompt: "La sanción recurrida",
  payload: {
    scenario: "Una empresa recibe una resolución expresa del Ministro.",
    questions: [1, 2, 3].map((n) => ({
      id: `q0${n}`,
      number: `2.4.${n}`,
      prompt: `Pregunta ${n} del supuesto.`,
      payload: { kind: "single_choice", options: [{ id: "b", text: `B${n}` }, { id: "a", text: `A${n}` }] },
    })),
  },
  answer: {
    kind: "case",
    questions: [1, 2, 3].map((n) => ({ kind: "single_choice", id: `q0${n}`, number: `2.4.${n}`, optionIds: ["a"], explanation: `Por el artículo ${n}.` })),
    explanation: null,
  },
};

describe("a case in the book", () => {
  it("prints the scenario first, then each question under its own number with lettered options", () => {
    const block = exerciseBlock(CASE, labels, () => "");
    const printed = texts(block.stack);
    const scenario = printed.indexOf("Una empresa recibe una resolución expresa del Ministro.");
    const first = printed.indexOf(labels.caseQuestion("2.4.1"));
    expect(scenario).toBeGreaterThan(-1);
    expect(first).toBeGreaterThan(scenario);
    expect(printed.slice(first, first + 6)).toEqual([labels.caseQuestion("2.4.1"), "Pregunta 1 del supuesto.", "a)", "B1", "b)", "A1"]);
  });

  it("answers every printed question in the key, citing the letter the page printed", () => {
    expect(answerLines(CASE, labels)).toEqual(["2.4.1  b)  A1", "2.4.2  b)  A2", "2.4.3  b)  A3"]);
    const entry = answerEntry(CASE, labels);
    expect(texts(entry.stack).join(" ")).toContain("2.4.2 · ");
  });

  it("holds the question ↔ key bijection inside the case, not only between exercise and entry", () => {
    const block = exerciseBlock(CASE, labels, () => "");
    const entry = answerEntry(CASE, labels);
    expect(block.exerciseId).toBe(entry.answerFor);
    expect(block.caseQuestions).toEqual(["2.4.1", "2.4.2", "2.4.3"]);
    expect(entry.caseAnswers).toEqual(block.caseQuestions);
  });
});
