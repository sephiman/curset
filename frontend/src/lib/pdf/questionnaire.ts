import type { Content } from "pdfmake/interfaces";
import type { QuestionnaireTema } from "@/api/printQuestionnaire";
import { questionBlock } from "@/lib/pdf/questionBlock";
import { DEST, printedId, withId } from "@/lib/pdf/pagination";

/**
 * A question-bank course's exercises in print: each tema's drawn questions after its prose, and one key
 * sheet at the back citing every answer. The draw itself is the server's; this only typesets it.
 */

export interface QuestionnaireLabels {
  questionnaire: string;
  questionnaireKey: string;
  questionnaireKeyIntro: string;
  seed: (seed: number) => string;
}

/** `questionFor`/`keyFor` are not pdfmake properties; the renderer ignores them and the tests read them. */
export function questionRef(lessonId: string, number: string): string {
  return `${lessonId}#${number}`;
}

export function temaQuestionnaire(tema: QuestionnaireTema, labels: QuestionnaireLabels): Content[] {
  if (tema.questions.length === 0) return [];
  return [
    { text: labels.questionnaire, style: "h2", headlineLevel: 2 },
    ...tema.questions.map((question) => ({
      ...questionBlock(question),
      questionFor: questionRef(tema.lessonId, question.number),
    })),
  ];
}

function keyTable(tema: QuestionnaireTema): Content {
  return {
    table: {
      headerRows: 0,
      widths: [24, 18, "*"],
      body: tema.keys.map((key) => [
        { text: key.number, bold: true, keyFor: questionRef(tema.lessonId, key.number) },
        { text: key.letter, bold: true },
        { text: key.citation ?? "" },
      ]),
    },
    layout: "lightHorizontalLines",
    margin: [0, 0, 0, 10],
  };
}

export function questionnaireKeySection(
  temas: QuestionnaireTema[],
  labels: QuestionnaireLabels,
  /** Marks this heading as a top-level section, so the running footer can name it. */
  sectionId: string,
): Content | null {
  const printed = temas.filter((tema) => tema.keys.length > 0);
  if (printed.length === 0) return null;
  return {
    stack: [
      withId(
        {
          text: labels.questionnaireKey,
          style: "blockTitle",
          headlineLevel: 1,
          tocItem: true,
          tocStyle: "tocBlock",
          outline: true,
        },
        sectionId,
      ),
      { text: labels.questionnaireKeyIntro, style: "moduleSummary" },
      ...printed.flatMap((tema, index) => [
        withId(
          {
            text: `${tema.lessonId.toUpperCase()} · ${tema.title}`,
            style: "answerGroup",
            headlineLevel: 2,
            outline: true,
            outlineParentId: sectionId,
          },
          DEST.outline(printedId("qkey", tema.lessonId, index)),
        ),
        keyTable(tema),
      ]),
    ],
    pageBreak: "before",
  };
}
