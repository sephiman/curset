import type { Content, ContentStack, TDocumentDefinitions } from "pdfmake/interfaces";
import type { Parent, PhrasingContent, Root } from "mdast";
import type { CourseExport, PrintExercise, PrintExercises } from "@/api/course";
import type { PrintQuestionnaire } from "@/api/printQuestionnaire";
import {
  annotateLesson,
  annotateLessonRefs,
  LESSON_REF,
  type LessonRefNode,
} from "@/lib/glossary/annotate";
import { buildTermIndex } from "@/lib/glossary/terms";
import { buildRefRegistry, type RefModule } from "@/lib/refs/registry";
import { lessonReferenceLabel, type TemaCourse } from "@/lib/tema";
import {
  answerKeySection,
  lessonExercises,
  type AnswerKeyGroup,
  type ExerciseChartLookup,
  type ExerciseLabels,
} from "@/lib/pdf/exercises";
import { glossarySection, type GlossaryLabels } from "@/lib/pdf/glossary";
import { appendNormativa, lessonToContent, type ListEsquemaKind, type MarkdownRenderers } from "@/lib/pdf/markdown";
import { DEST, keepTogether, printedId, withId, type OversizedBlock } from "@/lib/pdf/pagination";
import { createSectionTracker, SECTION_ID, type SectionTracker } from "@/lib/pdf/sections";
import { DEFAULT_STYLE, PAGE, PRINT_FONT, PRINT_STYLES, panelWidth } from "@/lib/pdf/page";
import { PLATFORM_NAME } from "@/lib/platform";
import type { CoverArt } from "@/lib/pdf/coverArt";
import { questionnaireKeySection, temaQuestionnaire, type QuestionnaireLabels } from "@/lib/pdf/questionnaire";

/**
 * The course as a print document: a pure function of (identity, theory export, figures, exercises).
 *
 * No DOM, network or i18next — the localized chrome arrives as `labels` — so either locale is
 * assertable in a test. Two sources joined by id: prose from `/course/export`, exercises from
 * `/course/print/exercises`, whose answers make the key from the same objects.
 */

/** Who the course is by. Not translated; only the label around it, via `labels.author`. */
export const COURSE_AUTHOR = "Juan José Hernández Garrido";

/** A figure as captured from the app's chart renderer: one PNG per panel, plus its caption. */
export interface CapturedFigure {
  id: string;
  caption: string;
  panels: string[];
}

export interface PdfLabels extends ExerciseLabels, GlossaryLabels, QuestionnaireLabels {
  contents: string;
  /** Cover line crediting the author, label localized around `COURSE_AUTHOR`. */
  author: string;
  /** Cover line naming the language and the day the document was made. */
  generated: string;
  page: (current: number, total: number) => string;
  /** A scoped document's page number: «3 de 12». */
  pageOf: (current: number, total: number) => string;
  /** A scoped cover's line for a course that keeps its norms: «Normativa consolidada a 2026-10-01». */
  coverConsolidated: (date: string) => string;
  /** The header row of each list esquema printed as a table (step, plazo, article…). */
  esquemaColumns: Record<ListEsquemaKind, string[]>;
  /** After a «Normativa» norm's title: «texto consolidado a 2024-11-06». */
  consolidated: (date: string) => string;
  /** The label above a `:::judgement` callout: who the judgement is attributed to. */
  judgement: (source: string) => string;
}

/** One module (bloque) or lesson (tema) printed on its own; its title already carries the id. */
export interface DocumentPart {
  kind: "module" | "lesson";
  id: string;
  title: string;
}

export interface BuildCourseDocumentOptions {
  courseTitle: string;
  /** The book's short name, for the running footer: the full title wraps at this size. */
  courseSubtitle: string;
  courseDescription: string;
  /** The platform mark above the title and the course glyph beside it; absent: a text-only cover. */
  cover?: CoverArt;
  export: CourseExport;
  figures: Map<string, CapturedFigure>;
  /** The printed exercises and their answers. Required: there is no exercise-free variant of the book. */
  exercises: PrintExercises;
  /** Whether to print in-lesson exercises and the answer key; false for theory only. */
  pdfExercises?: boolean;
  /** One captured PNG per chart exercise, keyed by exercise id. */
  exerciseCharts: Map<string, string>;
  /** Set for a tema or bloque export; `export` then holds only that part. Absent: the whole course. */
  part?: DocumentPart;
  /** A question-bank course's drawn questions, printed after each tema, with their key at the back. */
  questionnaire?: PrintQuestionnaire;
  /**
   * The whole course's tree, which labels lesson references («tema IV.1 · <title>») — including ones to
   * lessons this document does not print. Absent: the export itself, read by lesson title.
   */
  outline?: TemaCourse;
  /** Called for a box too tall for any page, so the report can name it. Never a failure. */
  onOversizedBlock?: (block: OversizedBlock) => void;
  /** Which page each top-level section starts on, for the footer. Pass one in to read it back. */
  sections?: SectionTracker;
  labels: PdfLabels;
}

/** `lessonId`/`figureId` are not pdfmake properties; the renderer ignores them and the tests use them. */
export interface LessonSection extends ContentStack {
  lessonId: string;
  pageBreak: "before";
}

export interface FigureBlock extends ContentStack {
  figureId: string;
}

function hasKey<K extends string>(node: unknown, key: K): node is Record<K, string> {
  return typeof node === "object" && node !== null && key in node;
}

export function lessonSections(doc: TDocumentDefinitions): LessonSection[] {
  const content = Array.isArray(doc.content) ? doc.content : [doc.content];
  return content.filter((node): node is LessonSection => hasKey(node, "lessonId"));
}

function collect<T>(doc: TDocumentDefinitions, key: string): T[] {
  const found: T[] = [];
  const walk = (node: unknown): void => {
    if (Array.isArray(node)) {
      node.forEach(walk);
      return;
    }
    if (typeof node !== "object" || node === null) return;
    if (hasKey(node, key)) found.push(node as unknown as T);
    for (const value of Object.values(node)) walk(value);
  };
  walk(doc.content);
  return found;
}

export function figureBlocks(doc: TDocumentDefinitions): FigureBlock[] {
  return collect<FigureBlock>(doc, "figureId");
}

/** Every printed exercise, in document order — the half of the bijection that lives on the page. */
export function exerciseBlocks(doc: TDocumentDefinitions): { exerciseId: string; exerciseNumber: string }[] {
  return collect(doc, "exerciseId");
}

/** Every answer-key entry, in document order — the other half. */
export function answerEntries(doc: TDocumentDefinitions): { answerFor: string; exerciseNumber: string }[] {
  return collect(doc, "answerFor");
}

function coverTitle(o: BuildCourseDocumentOptions): Content {
  const title: Content = { text: o.courseTitle, style: "courseTitle" };
  if (!o.cover?.glyph) return title;
  return { columns: [{ svg: o.cover.glyph, width: 30, margin: [0, 2, 0, 0] }, { ...title, width: "*" }], columnGap: 12 };
}

function cover(o: BuildCourseDocumentOptions): Content {
  return {
    stack: [
      ...(o.cover ? [{ svg: o.cover.mark, width: 44, margin: [0, 0, 0, 40] } satisfies Content] : []),
      coverTitle(o),
      { text: o.labels.author, style: "coverMeta" },
      { text: o.courseDescription, style: "courseDescription" },
      { text: o.labels.generated, style: "coverMeta" },
    ],
    // With the mark on top the title still lands where a text-only cover puts it.
    margin: [0, o.cover ? 86 : 170, 0, 0],
  };
}

/** The latest consolidation date among the part's norms; null for a course that keeps none. */
export function consolidatedAsOf(doc: CourseExport): string | null {
  const dates = doc.blocks.flatMap((b) =>
    b.modules.flatMap((m) => m.lessons.flatMap((l) => (l.normativa ?? []).map((n) => n.consolidatedAsOf))),
  );
  const known = dates.filter((date): date is string => typeof date === "string").sort();
  return known.at(-1) ?? null;
}

function partCover(o: BuildCourseDocumentOptions, part: DocumentPart): Content {
  const consolidated = consolidatedAsOf(o.export);
  return {
    stack: [
      ...(o.cover ? [{ svg: o.cover.mark, width: 44, margin: [0, 0, 0, 40] } satisfies Content] : []),
      coverTitle(o),
      { text: part.title, style: "partTitle" },
      { text: o.labels.generated, style: "coverMeta" },
      ...(consolidated ? [{ text: o.labels.coverConsolidated(consolidated), style: "coverMetaNext" }] : []),
    ],
    margin: [0, o.cover ? 86 : 170, 0, 0],
  };
}

function lessonCount(doc: CourseExport): number {
  return doc.blocks.reduce((n, b) => n + b.modules.reduce((k, m) => k + m.lessons.length, 0), 0);
}

function toc(o: BuildCourseDocumentOptions): Content[] {
  // A tema prints on its own pages with nothing to find; only the book and a bloque get contents.
  if (o.part && lessonCount(o.export) <= 1) return [];
  return [{ toc: { title: { text: o.labels.contents, style: "tocTitle" } }, pageBreak: "before" }];
}

/** Panels two-up as in the app, then the caption, kept together on one page. */
function figureContent(figure: CapturedFigure): FigureBlock {
  const perRow = figure.panels.length > 1 ? 2 : 1;
  const width = panelWidth(perRow);
  const rows: Content[] = [];
  for (let i = 0; i < figure.panels.length; i += perRow) {
    const row = figure.panels.slice(i, i + perRow).map((image) => ({ image, width }));
    rows.push(perRow === 1 ? row[0] : { columns: row, columnGap: 10 });
  }
  return {
    stack: [...rows, { text: figure.caption, style: "caption" }],
    margin: [0, 8, 0, 12],
    unbreakable: true,
    figureId: figure.id,
  };
}

function renderers(figures: Map<string, CapturedFigure>, labels: PdfLabels): MarkdownRenderers {
  return {
    figure: (id) => {
      const figure = figures.get(id);
      if (!figure) throw new Error(`figure ${id} was not rendered for this export`);
      return figureContent(figure);
    },
    esquemaColumns: labels.esquemaColumns,
    judgement: labels.judgement,
  };
}

/**
 * The footer's left side: the platform and the book, plus the current section once the first block
 * has started. The book is its subtitle, not its full title — one line at footer size, on every page.
 */
export function runningTitle(courseSubtitle: string, section: string | undefined): string {
  const book = `${PLATFORM_NAME} · ${courseSubtitle}`;
  return section ? `${book} · ${section}` : book;
}

/** A tema's or bloque's footer: the wordmark, the book and section, the seed when it drew questions, «N de M». */
function partFooter(o: BuildCourseDocumentOptions, section: string | undefined, current: number, total: number): Content {
  const seed = o.questionnaire ? ` · ${o.labels.seed(o.questionnaire.seed)}` : "";
  return {
    columns: [
      ...(o.cover?.wordmark ? [{ svg: o.cover.wordmark, width: 38, margin: [0, 1, 0, 0] } satisfies Content] : []),
      { text: `${o.courseSubtitle}${section ? ` · ${section}` : ""}${seed}`, style: "footer", width: "*" },
      { text: o.labels.pageOf(current, total), style: "footer", alignment: "right", width: "auto" },
    ],
    columnGap: 8,
    margin: [PAGE.margins[0], 18, PAGE.margins[2], 0],
  };
}

/** The captured chart for one exercise, or a stop — a chartless question is unanswerable. */
function exerciseChart(charts: Map<string, string>): ExerciseChartLookup {
  return (exerciseId) => {
    const image = charts.get(exerciseId);
    if (!image) throw new Error(`exercise ${exerciseId}'s chart was not rendered for this export`);
    return image;
  };
}

/**
 * The book's prose links, both mark types in one annotate step, terms first as the app runs them.
 *
 * Glossary links are one pass over the course in reading order with one shared `marked` set — that
 * shared set IS the PDF's policy, the first occurrence of a term in the whole book claims its slot.
 * A course with no glossary still gets its lesson references; only the term half stands down, so the
 * book never carries a link to a glossary page it does not print.
 */
function proseAnnotator(o: BuildCourseDocumentOptions, marked: Set<string>) {
  const doc = o.export;
  const terms = doc.glossary.length > 0 ? buildTermIndex(doc.glossary, doc.locale) : null;
  const outline = o.outline ?? outlineFromExport(doc);
  // References resolve against the whole course, so one to a lesson this document leaves out is still
  // recognised — and printed as its label, as text.
  const registry = buildRefRegistry(refModulesFromOutline(outline));
  const relabel = refRelabeler(outline, printedLessonIds(doc), printedModuleIds(doc, o.part));
  const norms = new Map(
    doc.blocks.flatMap((b) => b.modules.flatMap((m) => m.lessons.map((l) => [l.id, l.normativa ?? []] as const))),
  );
  return (lessonId: string) => (tree: Root) => {
    if (terms) annotateLesson(tree, { lessonId, terms, marked });
    annotateLessonRefs(tree, { lessonId, registry });
    relabel(tree);
    appendNormativa(tree, norms.get(lessonId) ?? [], o.labels.consolidated);
  };
}

/** The whole-course export is its own outline; a course without a lesson noun reads its lessons by title. */
function outlineFromExport(doc: CourseExport): TemaCourse {
  return {
    course: { lessonNoun: null },
    blocks: doc.blocks.map((block) => ({
      modules: block.modules.map((module, m) => ({
        id: module.id,
        order: m + 1,
        lessons: module.lessons.map((lesson, l) => ({ id: lesson.id, order: l + 1, title: lesson.title })),
      })),
    })),
  };
}

function refModulesFromOutline(outline: TemaCourse): RefModule[] {
  return outline.blocks.flatMap((block) =>
    block.modules.map((module) => ({
      id: module.id,
      // A module reference keeps its authored text in print, so its target's title is never read.
      title: module.id,
      lessons: module.lessons.map((lesson) => ({ id: lesson.id, title: lesson.title })),
    })),
  );
}

/** Modules whose heading this document prints; a tema prints its module's heading but not the module. */
function printedModuleIds(doc: CourseExport, part: DocumentPart | undefined): Set<string> {
  if (part?.kind === "lesson") return new Set();
  return new Set(doc.blocks.flatMap((b) => b.modules.map((m) => m.id)));
}

/**
 * N5: a lesson reference prints as the lesson's label («tema IV.1 · <title>», or its title), never as the
 * id the prose was written with; it stays a link when this document prints that lesson and becomes plain
 * text otherwise. A module reference keeps its authored text and links only to a module printed whole.
 */
function refRelabeler(outline: TemaCourse, lessons: Set<string>, modules: Set<string>) {
  const rewrite = (node: LessonRefNode): PhrasingContent => {
    if (node.refKind === "lesson") {
      const label = lessonReferenceLabel(outline, node.refId) ?? node.children.map((c) => c.value).join("");
      if (!lessons.has(node.refId)) return { type: "text", value: label };
      return { ...node, children: [{ type: "text", value: label }] };
    }
    return modules.has(node.refId) ? node : { type: "text", value: node.children.map((c) => c.value).join("") };
  };
  const walk = (parent: Parent): void => {
    parent.children = parent.children.map((child) => {
      if (child.type === LESSON_REF) return rewrite(child as LessonRefNode);
      if ("children" in child) walk(child as Parent);
      return child;
    }) as Parent["children"];
  };
  return (tree: Root) => walk(tree);
}

function printedLessonIds(doc: CourseExport): Set<string> {
  return new Set(doc.blocks.flatMap((b) => b.modules.flatMap((m) => m.lessons.map((l) => l.id))));
}

/**
 * A scoped glossary: the terms the part's prose marked, the terms one of its lessons teaches (a term is
 * never marked in its own origin), and the entries their aliases point to.
 */
function scopedGlossary(doc: CourseExport, marked: Set<string>): CourseExport["glossary"] {
  const printed = printedLessonIds(doc);
  const taughtHere = (entry: CourseExport["glossary"][number]) =>
    [entry.origin, ...(entry.senses ?? []).map((sense) => sense.origin)].some((id) => id !== null && printed.has(id));
  const kept = new Set(doc.glossary.filter((entry) => marked.has(entry.id) || taughtHere(entry)).map((e) => e.id));
  for (const entry of doc.glossary) if (kept.has(entry.id) && entry.aliasOf) kept.add(entry.aliasOf.id);
  return doc.glossary.filter((entry) => kept.has(entry.id));
}

export function buildCourseDocument(o: BuildCourseDocumentOptions): TDocumentDefinitions {
  const sections = o.sections ?? createSectionTracker();
  const keepPagesTogether = keepTogether({ onOversizedBlock: o.onOversizedBlock });
  const render = renderers(o.figures, o.labels);
  const marked = new Set<string>();
  const annotator = proseAnnotator(o, marked);
  const questionnaire = new Map((o.questionnaire?.temas ?? []).map((tema) => [tema.lessonId, tema]));
  const questionnaireFor = (lessonId: string): Content[] => {
    const tema = questionnaire.get(lessonId);
    return tema ? temaQuestionnaire(tema, o.labels) : [];
  };
  const chart = exerciseChart(o.exerciseCharts);
  const printExercises = o.pdfExercises ?? true;
  const byLesson = printExercises
    ? new Map(o.exercises.lessons.map((lesson) => [lesson.lessonId, lesson.exercises]))
    : new Map<string, PrintExercise[]>();
  const excludedByLesson = new Map<string, number>();
  if (printExercises) {
    for (const exclusion of o.exercises.excluded) {
      excludedByLesson.set(exclusion.lessonId, (excludedByLesson.get(exclusion.lessonId) ?? 0) + 1);
    }
  }
  // The key follows the book: grouped by module, in the order the exercises were printed.
  const keyGroups: AnswerKeyGroup[] = [];
  const content: Content[] = [o.part ? partCover(o, o.part) : cover(o), ...toc(o)];

  for (const block of o.export.blocks) {
    let blockOpened = false;
    for (const module of block.modules) {
      // Block and module headings open the page their first lesson starts on, rather than taking a
      // mostly empty page of their own: the lesson still begins on a fresh page.
      const opening: Content[] = [];
      const moduleTitle = `${module.id.toUpperCase()} · ${module.title}`;
      // The outline nests exactly as the manifest does — block › module › lesson — and each level
      // parents the next by id, so a reader's bookmark pane is the course tree.
      const blockOutlineId = printedId(SECTION_ID, block.id, 0);
      if (!blockOpened) {
        // The block heading opens a top-level section, and the footer names it from here on.
        sections.declare(blockOutlineId, block.title);
        opening.push(
          withId(
            {
              text: block.title,
              style: "blockTitle",
              headlineLevel: 1,
              tocItem: true,
              tocStyle: "tocBlock",
              outline: true,
              outlineExpanded: true,
            },
            blockOutlineId,
          ),
        );
        blockOpened = true;
      }
      opening.push(
        withId(
          {
            text: moduleTitle,
            style: "moduleTitle",
            headlineLevel: 2,
            tocItem: true,
            tocStyle: "tocModule",
            tocMargin: [12, 0, 0, 0],
            outline: true,
            outlineParentId: blockOutlineId,
          },
          DEST.outline(module.id),
        ),
        { text: module.summary, style: "moduleSummary" },
      );

      if (module.lessons.length === 0) {
        // The manifest allows a module with no lesson yet; it still gets its heading.
        content.push({ stack: opening, pageBreak: "before" });
        continue;
      }

      const moduleExercises: PrintExercise[] = [];

      module.lessons.forEach((lesson, index) => {
        const body = lessonToContent(lesson.markdown, render, lesson.id, annotator?.(lesson.id));
        const exercises = byLesson.get(lesson.id) ?? [];
        if (printExercises) {
          moduleExercises.push(...exercises);
        }
        // A lesson's prose opens with its own `# title` — the string the manifest carries and the app
        // shows. Promote it to the TOC entry rather than printing the title twice; a body without one
        // falls back to the manifest title, so the TOC is never short an entry.
        //
        // `outlineText` is not optional here: the parsed title is an ARRAY of styled runs, and
        // pdfmake would hand that array to the bookmark as its label.
        const nav = {
          tocItem: true,
          tocStyle: "tocLesson",
          tocMargin: [24, 0, 0, 0],
          outline: true,
          outlineText: lesson.title,
          outlineParentId: DEST.outline(module.id),
          id: DEST.outline(lesson.id),
        };
        const first = body[0] as { style?: string } | undefined;
        if (first?.style === "lessonTitle") {
          Object.assign(first, nav);
        } else {
          body.unshift({ text: lesson.title, style: "lessonTitle", headlineLevel: 1, ...nav });
        }
        const section: LessonSection = {
          stack: [
            ...(index === 0 ? opening : []),
            ...body,
            // The prose is unchanged; the exercises follow it, inside the lesson's own section.
            ...(printExercises
              ? lessonExercises(exercises, excludedByLesson.get(lesson.id) ?? 0, o.labels, chart)
              : []),
            ...questionnaireFor(lesson.id),
          ],
          pageBreak: "before",
          lessonId: lesson.id,
        };
        content.push(section);
      });

      if (printExercises) {
        keyGroups.push({ title: moduleTitle, exercises: moduleExercises });
      }
    }
  }

  // The glossary sits between the course and the answer key: a reference you consult while reading,
  // ahead of the solutions you consult after.
  const glossaryId = printedId(SECTION_ID, "glossary", 0);
  sections.declare(glossaryId, o.labels.glossary);
  const printed = printedLessonIds(o.export);
  const glossary = glossarySection(
    o.part ? scopedGlossary(o.export, marked) : o.export.glossary,
    o.export.locale,
    o.labels,
    glossaryId,
    o.part ? (lessonId) => printed.has(lessonId) : undefined,
  );
  if (glossary) content.push(glossary);

  if (printExercises) {
    const answerKeyId = printedId(SECTION_ID, "answer-key", 0);
    sections.declare(answerKeyId, o.labels.answerKey);
    const key = answerKeySection(keyGroups, o.labels, answerKeyId);
    if (key) content.push(key);
  }

  if (o.questionnaire) {
    const questionnaireKeyId = printedId(SECTION_ID, "questionnaire-key", 0);
    sections.declare(questionnaireKeyId, o.labels.questionnaireKey);
    const key = questionnaireKeySection(o.questionnaire.temas, o.labels, questionnaireKeyId);
    if (key) content.push(key);
  }

  return {
    info: {
      title: o.courseTitle,
      subject: o.courseDescription,
      author: COURSE_AUTHOR,
      creator: PLATFORM_NAME,
    },
    pageSize: PAGE.size,
    pageMargins: PAGE.margins,
    content,
    footer: (currentPage: number, pageCount: number) =>
      currentPage === 1 // the cover carries no number; every page after it does
        ? { text: "" }
        : o.part
          ? partFooter(o, sections.at(currentPage), currentPage, pageCount)
          : {
              columns: [
                { text: runningTitle(o.courseSubtitle, sections.at(currentPage)), style: "footer" },
                { text: o.labels.page(currentPage, pageCount), style: "footer", alignment: "right" },
              ],
              margin: [PAGE.margins[0], 18, PAGE.margins[2], 0],
            },
    styles: PRINT_STYLES,
    defaultStyle: DEFAULT_STYLE,
    // Where pages may break: headings stay with their body, callouts print whole. The same hook is
    // pdfmake's only view of a laid-out node, so the footer's section tracking rides along with it.
    pageBreakBefore: (node, near) => {
      sections.observe(node);
      return keepPagesTogether(node, near);
    },
  };
}

/** One family, four variants, resolved from pdfmake's vfs by file name. */
export const PRINT_FONTS = {
  [PRINT_FONT]: {
    normal: "LiberationSans-Regular.ttf",
    bold: "LiberationSans-Bold.ttf",
    italics: "LiberationSans-Italic.ttf",
    bolditalics: "LiberationSans-BoldItalic.ttf",
  },
} as const;
