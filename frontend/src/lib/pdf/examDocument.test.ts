// SPDX-License-Identifier: AGPL-3.0-only
import { describe, expect, it } from "vitest";
import type { TDocumentDefinitions } from "pdfmake/interfaces";
import { buildExamDocument } from "@/lib/pdf/examDocument";
import type { ExamPrintData, ExamPrintKey, ExamPrintQuestion } from "@/api/exams";

const LETTERS = ["A", "B", "C", "D"];
const OPTION_IDS = ["a", "b", "c", "d"];

interface PrintedQuestion {
  label: string;
  options: { letter: string; text: string }[];
}

interface PrintedCase {
  heading: string;
  scenario: string | undefined;
  questions: PrintedQuestion[];
}

interface PrintedKey {
  number: string;
  letter: string;
}

function isRecord(value: unknown): value is Record<string, unknown> {
  return typeof value === "object" && value !== null && !Array.isArray(value);
}

function textOf(value: unknown): string | undefined {
  return isRecord(value) && typeof value.text === "string" ? value.text : undefined;
}

function listOf(value: unknown, key: "stack" | "columns"): unknown[] | undefined {
  return isRecord(value) && Array.isArray(value[key]) ? value[key] : undefined;
}

function tableBodyOf(value: unknown): unknown[][] | undefined {
  if (!isRecord(value) || !isRecord(value.table) || !Array.isArray(value.table.body)) return undefined;
  return value.table.body.filter((row): row is unknown[] => Array.isArray(row));
}

/** A question block is a stack: a (label, prompt) row, then one (letter, text) row per option. */
function asQuestion(value: unknown): PrintedQuestion | undefined {
  const stack = listOf(value, "stack");
  const head = stack ? listOf(stack[0], "columns") : undefined;
  if (!stack || !head) return undefined;
  const label = textOf(head[0]);
  if (!label?.endsWith(".")) return undefined;
  const options = stack.slice(1).map((row) => {
    const cells = listOf(row, "columns") ?? [];
    return { letter: (textOf(cells[0]) ?? "").replace(/\)$/, ""), text: textOf(cells[1]) ?? "" };
  });
  return { label: label.slice(0, -1), options };
}

/** A case block is a stack: its heading, its scenario in a one-cell table, then its questions. */
function asCase(value: unknown): PrintedCase | undefined {
  const stack = listOf(value, "stack");
  const heading = stack ? textOf(stack[0]) : undefined;
  if (!stack || !heading?.startsWith("Supuesto ")) return undefined;
  const scenarioCell = tableBodyOf(stack[1])?.[0]?.[0];
  const questions = stack.slice(2).map(asQuestion);
  return {
    heading,
    scenario: textOf(scenarioCell),
    questions: questions.filter((q): q is PrintedQuestion => q !== undefined),
  };
}

/** The key table lays (number, letter) pairs out column by column; read them back in that order. */
function asKeys(value: unknown): PrintedKey[] | undefined {
  const stack = listOf(value, "stack");
  const body = stack ? tableBodyOf(stack[1]) : undefined;
  if (!body) return undefined;
  const columns: PrintedKey[][] = [[], [], [], []];
  for (const row of body) {
    for (let c = 0; c < 4; c++) {
      const number = textOf(row[2 * c]);
      const letter = textOf(row[2 * c + 1]);
      if (number) columns[c].push({ number: number.replace(/ \(R\)$/, ""), letter: letter ?? "" });
    }
  }
  return columns.flat();
}

interface PrintedDocument {
  parts: Map<string, unknown[]>;
}

/** Splits the top-level content at each part heading (style h1). */
function sections(doc: TDocumentDefinitions): PrintedDocument {
  const content: unknown[] = Array.isArray(doc.content) ? doc.content : [doc.content];
  const parts = new Map<string, unknown[]>();
  let current: unknown[] | undefined;
  for (const item of content) {
    if (isRecord(item) && item.style === "h1" && typeof item.text === "string") {
      current = [];
      parts.set(item.text, current);
    } else {
      current?.push(item);
    }
  }
  return { parts };
}

function question(number: string, correct: number, reserve = false): [ExamPrintQuestion, ExamPrintKey] {
  return [
    {
      id: `q-${number}`,
      number,
      reserve,
      prompt: `Enunciado ${number}`,
      options: OPTION_IDS.map((id, i) => ({ id, letter: LETTERS[i], text: `Respuesta ${id} de ${number}` })),
    },
    { number, reserve, correctOptionId: OPTION_IDS[correct], correctLetter: LETTERS[correct], explanation: null },
  ];
}

function simulationPrint(): ExamPrintData {
  const first = Array.from({ length: 75 }, (_, i) => question(String(i + 1), (i * 3) % 4, i >= 70));
  const cases = [1, 2].map((c) => ({
    id: `sp-0${c}`,
    title: `Caso ${c}`,
    scenario: `Escenario del caso ${c}.`,
    rows: Array.from({ length: 20 }, (_, i) => question(`S${c}.${i + 1}`, (i + c) % 4)),
  }));
  return {
    presetId: "simulacro",
    title: "Simulacro oficial",
    description: null,
    timeLimitMinutes: 100,
    pause: "never",
    parts: [
      { id: "parte-1", title: "Primera parte", kind: "questions", questions: first.map(([q]) => q) },
      {
        id: "parte-2",
        title: "Segunda parte",
        kind: "cases",
        cases: cases.map((c) => ({ id: c.id, title: c.title, scenario: c.scenario, questions: c.rows.map(([q]) => q) })),
      },
    ],
    keySheet: [
      { partId: "parte-1", title: "Primera parte", keys: first.map(([, k]) => k) },
      ...cases.map((c, i) => ({
        partId: "parte-2",
        title: `Supuesto ${i + 1}: ${c.title}`,
        keys: c.rows.map(([, k]) => k),
      })),
    ],
  };
}

describe("buildExamDocument", () => {
  const data = simulationPrint();
  const doc = buildExamDocument(data);
  const { parts } = sections(doc);

  it("prints the title first and the key sheet after the parts", () => {
    expect(doc.pageSize).toBe("A4");
    const content = Array.isArray(doc.content) ? doc.content : [doc.content];
    expect(textOf(content[0])).toBe("Simulacro oficial");
    expect([...parts.keys()]).toEqual(["Primera parte", "Segunda parte", "Plantilla de respuestas"]);
  });

  it("prints the 70 questions and 5 reserves of the first part, reserves last and marked", () => {
    const printed = (parts.get("Primera parte") ?? []).map(asQuestion).filter((q) => q !== undefined);
    expect(printed).toHaveLength(75);
    expect(printed.slice(0, 70).every((q) => /^\d+$/.test(q.label))).toBe(true);
    expect(printed.slice(70).map((q) => q.label)).toEqual(["71", "72", "73", "74", "75"].map((n) => `${n} (Reserva)`));
  });

  it("prints both cases, each scenario followed by its own 20 questions", () => {
    const printed = (parts.get("Segunda parte") ?? []).map(asCase).filter((c) => c !== undefined);
    expect(printed.map((c) => c.heading)).toEqual(["Supuesto 1: Caso 1", "Supuesto 2: Caso 2"]);
    printed.forEach((c, i) => {
      expect(c.scenario).toBe(`Escenario del caso ${i + 1}.`);
      expect(c.questions.map((q) => q.label)).toEqual(Array.from({ length: 20 }, (_, n) => `S${i + 1}.${n + 1}`));
    });
  });

  it("keys every printed question once, with the letter printed beside its correct option", () => {
    const printedQuestions = [
      ...(parts.get("Primera parte") ?? []).map(asQuestion),
      ...(parts.get("Segunda parte") ?? []).flatMap((c) => asCase(c)?.questions ?? []),
    ].filter((q) => q !== undefined);
    const keys = (parts.get("Plantilla de respuestas") ?? []).flatMap((group) => asKeys(group) ?? []);
    const correctText = new Map(
      data.keySheet.flatMap((g) => g.keys).map((k) => [k.number, `Respuesta ${k.correctOptionId} de ${k.number}`]),
    );

    expect(keys).toHaveLength(115);
    expect(keys.map((k) => k.number)).toEqual(printedQuestions.map((q) => q.label.replace(/ \(Reserva\)$/, "")));
    keys.forEach((key, i) => {
      const beside = printedQuestions[i].options.find((o) => o.text === correctText.get(key.number));
      expect(key.letter, key.number).toBe(beside?.letter);
    });
  });
});
