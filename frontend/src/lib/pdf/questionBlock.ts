import type { Content, ContentStack } from "pdfmake/interfaces";
import type { GeneratedTable } from "@/api/exercises";
import type { ExamPrintOption, ExamPrintQuestion } from "@/api/exams";
import { withCodeSpans } from "@/lib/pdf/codeText";
import { PRINT } from "@/lib/pdf/page";

function optionRow(opt: Pick<ExamPrintOption, "letter" | "text">): Content {
  return {
    columns: [
      { text: `${opt.letter})`, width: 18, color: PRINT.muted, bold: true },
      { text: withCodeSpans(opt.text), width: "*" },
    ],
    columnGap: 4,
    margin: [6, 1, 0, 2],
  };
}

function tableBlock(table: GeneratedTable): Content {
  return {
    stack: [
      { text: table.title, bold: true, fontSize: 8.5, margin: [30, 2, 0, 2] },
      {
        table: {
          headerRows: 1,
          widths: table.header.map(() => "auto"),
          body: [
            table.header.map((cell) => ({ text: cell, bold: true, fontSize: 8 })),
            ...table.rows.map((row) => row.map((cell) => ({ text: cell, fontSize: 8 }))),
          ],
        },
        layout: "lightHorizontalLines",
        margin: [30, 0, 0, 4],
      },
    ],
  };
}

/** A question as printed: number and stem, its table, then one lettered row per option, kept on one page. */
export function questionBlock(
  q: Pick<ExamPrintQuestion, "number" | "prompt" | "reserve" | "table"> & {
    options: Pick<ExamPrintOption, "letter" | "text">[];
  },
): ContentStack {
  const label = q.reserve ? `${q.number} (Reserva)` : q.number;
  return {
    stack: [
      {
        columns: [
          { text: `${label}.`, width: 26, bold: true, color: PRINT.heading },
          { text: withCodeSpans(q.prompt), width: "*", bold: false },
        ],
        columnGap: 4,
        margin: [0, 4, 0, 4],
      },
      ...(q.table ? [tableBlock(q.table)] : []),
      ...q.options.map(optionRow),
    ],
    unbreakable: true,
    margin: [0, 2, 0, 6],
  };
}
