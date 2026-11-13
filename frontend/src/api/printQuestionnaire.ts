import { apiClient, courseUrl, inReadingLanguage, type CourseScope } from "@/api/client";
import type { GeneratedTable } from "@/api/exercises";

/** One drawn question as printed: options lettered A–D in the order the seed shuffled them. */
export interface QuestionnaireQuestion {
  id: string;
  number: string;
  prompt: string;
  table?: GeneratedTable;
  options: { letter: string; text: string }[];
}

/** The key-sheet line for the question printed under the same number. */
export interface QuestionnaireKey {
  number: string;
  letter: string;
  /** The article the answer rests on («art. 14 CE»); null for a generated item. */
  citation: string | null;
}

export interface QuestionnaireTema {
  lessonId: string;
  title: string;
  questions: QuestionnaireQuestion[];
  keys: QuestionnaireKey[];
}

export interface PrintQuestionnaire {
  /** Printed in the footer: the same seed and scope draw the same paper. */
  seed: number;
  locale: string;
  temas: QuestionnaireTema[];
}

/** Up to 20 questions per tema of the scope (a module or lesson id; absent: the whole course). */
export async function getPrintQuestionnaire(scope: CourseScope, part?: string): Promise<PrintQuestionnaire> {
  const { data } = await apiClient.get<PrintQuestionnaire>(
    courseUrl(scope, "/print/questionnaire"),
    inReadingLanguage(scope, part ? { scope: part } : {}),
  );
  return data;
}
