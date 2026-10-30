// SPDX-License-Identifier: AGPL-3.0-only
/** Typesetting an exam preset into a printable PDF document (delta A, B, H). */

import type { Content, TDocumentDefinitions } from "pdfmake/interfaces";
import type { CourseScope } from "@/api/client";
import {
  getExamPrint,
  type ExamPrintCase,
  type ExamPrintData,
  type ExamPrintKey,
  type ExamPrintKeyGroup,
  type ExamPrintOption,
  type ExamPrintPart,
  type ExamPrintQuestion,
} from "@/api/exams";
import type { GeneratedPdf } from "@/lib/pdf/generate";
import { DEFAULT_STYLE, PAGE, PRINT, PRINT_STYLES } from "@/lib/pdf/page";
import { loadPdfMake } from "@/lib/pdf/runtime";

function optionRow(opt: ExamPrintOption): Content {
  return {
    columns: [
      { text: `${opt.letter})`, width: 18, color: PRINT.muted, bold: true },
      { text: opt.text, width: "*" },
    ],
    columnGap: 4,
    margin: [6, 1, 0, 2],
  };
}

function questionBlock(q: ExamPrintQuestion): Content {
  const label = q.reserve ? `${q.number} (Reserva)` : q.number;
  return {
    stack: [
      {
        columns: [
          { text: `${label}.`, width: 26, bold: true, color: PRINT.heading },
          { text: q.prompt, width: "*", bold: false },
        ],
        columnGap: 4,
        margin: [0, 4, 0, 4],
      },
      ...q.options.map(optionRow),
    ],
    unbreakable: true,
    margin: [0, 2, 0, 6],
  };
}

function caseBlock(c: ExamPrintCase, caseIdx: number): Content {
  return {
    stack: [
      {
        text: `Supuesto ${caseIdx}: ${c.title}`,
        style: "h2",
        margin: [0, 10, 0, 6],
      },
      {
        table: {
          widths: ["*"],
          body: [
            [
              {
                text: c.scenario,
                fillColor: "#f8fafc",
                margin: [8, 8, 8, 8],
                fontSize: 9.5,
                lineHeight: 1.35,
              },
            ],
          ],
        },
        layout: {
          hLineWidth: () => 1,
          vLineWidth: () => 1,
          hLineColor: () => PRINT.rule,
          vLineColor: () => PRINT.rule,
        },
        margin: [0, 0, 0, 10],
      },
      ...c.questions.map(questionBlock),
    ],
    margin: [0, 4, 0, 12],
  };
}

function partContent(part: ExamPrintPart, index: number): Content[] {
  const items: Content[] = [];
  if (index > 0) {
    items.push({ text: "", pageBreak: "before" });
  }

  items.push({
    text: part.title,
    style: "h1",
    margin: [0, index === 0 ? 8 : 0, 0, 8],
  });

  if (part.kind === "cases" && part.cases) {
    part.cases.forEach((c, idx) => {
      items.push(caseBlock(c, idx + 1));
    });
  } else if (part.questions) {
    items.push(...part.questions.map(questionBlock));
  }

  return items;
}

function keySheetTable(group: ExamPrintKeyGroup): Content {
  // 4 columns of (number, letter)
  const cols = 4;
  const rows: { number: string; letter: string; note?: string | null }[][] = [];
  const perCol = Math.ceil(group.keys.length / cols);

  for (let r = 0; r < perCol; r++) {
    const row: { number: string; letter: string; note?: string | null }[] = [];
    for (let c = 0; c < cols; c++) {
      const idx = c * perCol + r;
      if (idx < group.keys.length) {
        const k = group.keys[idx];
        row.push({
          number: k.reserve ? `${k.number} (R)` : k.number,
          letter: k.correctLetter,
          note: k.explanation,
        });
      }
    }
    rows.push(row);
  }

  const tableBody = rows.map((row) => {
    const cells = [];
    for (let c = 0; c < cols; c++) {
      const item = row[c];
      if (item) {
        cells.push({ text: item.number, bold: true, width: 28, color: PRINT.muted });
        cells.push({ text: item.letter, bold: true, width: 20, color: PRINT.primary });
      } else {
        cells.push({ text: "" });
        cells.push({ text: "" });
      }
    }
    return cells;
  });

  const notesWithKeys = group.keys.filter((k) => k.explanation);

  return {
    stack: [
      { text: group.title, style: "h2", margin: [0, 8, 0, 6] },
      {
        table: {
          widths: [28, 24, 28, 24, 28, 24, 28, 24],
          body: tableBody,
        },
        layout: "lightHorizontalLines",
        margin: [0, 0, 0, 8],
      },
      ...(notesWithKeys.length > 0
        ? ([
            { text: "Notas sobre las preguntas:", bold: true, fontSize: 9, margin: [0, 6, 0, 4] as [number, number, number, number] },
            ...notesWithKeys.map((k: ExamPrintKey) => ({
              text: `${k.number}: ${k.explanation}`,
              fontSize: 8.5,
              color: PRINT.muted,
              margin: [0, 1, 0, 2] as [number, number, number, number],
            })),
          ] as Content[])
        : []),
    ],
    margin: [0, 4, 0, 12],
  };
}

export function buildExamDocument(data: ExamPrintData): TDocumentDefinitions {
  const content: Content[] = [
    {
      text: data.title,
      style: "title",
      alignment: "center",
      margin: [0, 0, 0, 6],
    },
  ];

  if (data.description) {
    content.push({
      text: data.description,
      style: "lead",
      alignment: "center",
      margin: [0, 0, 0, 6],
    });
  }

  const metaItems = [];
  if (data.timeLimitMinutes) metaItems.push(`Tiempo: ${data.timeLimitMinutes} minutos`);
  metaItems.push("Penalización: 1/3 por respuesta errónea (blancas no restan)");

  content.push({
    text: metaItems.join(" · "),
    fontSize: 9,
    color: PRINT.muted,
    alignment: "center",
    margin: [0, 0, 0, 12],
  });

  content.push({
    canvas: [{ type: "line", x1: 0, y1: 0, x2: PAGE.width - PAGE.margins[0] - PAGE.margins[2], y2: 0, lineWidth: 1, lineColor: PRINT.rule }],
    margin: [0, 0, 0, 12],
  });

  data.parts.forEach((part, idx) => {
    content.push(...partContent(part, idx));
  });

  // Key sheet
  content.push({ text: "", pageBreak: "before" });
  content.push({
    text: "Plantilla de respuestas",
    style: "h1",
    margin: [0, 0, 0, 10],
  });

  data.keySheet.forEach((group) => {
    content.push(keySheetTable(group));
  });

  return {
    pageSize: PAGE.size,
    pageMargins: PAGE.margins,
    defaultStyle: DEFAULT_STYLE,
    styles: PRINT_STYLES,
    header: () => ({
      text: data.title,
      fontSize: 8,
      color: PRINT.muted,
      margin: [PAGE.margins[0], 24, PAGE.margins[2], 0],
    }),
    footer: (currentPage: number, pageCount: number) => ({
      columns: [
        { text: "Antigravity Curset · Oposiciones AGE", fontSize: 8, color: PRINT.muted },
        { text: `${currentPage} / ${pageCount}`, fontSize: 8, color: PRINT.muted, alignment: "right" },
      ],
      margin: [PAGE.margins[0], 20, PAGE.margins[2], 0],
    }),
    content,
  };
}

export async function generateExamPdf(course: CourseScope, presetId: string): Promise<GeneratedPdf> {
  const data = await getExamPrint(course, presetId);
  const definition = buildExamDocument(data);
  const pdfMake = await loadPdfMake();
  const blob = await pdfMake.createPdf(definition).getBlob();
  return {
    blob,
    filename: `${course.slug}-${presetId}.pdf`,
  };
}
