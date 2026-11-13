import { useEffect, useMemo, useRef, useState } from "react";
import { Link } from "react-router-dom";
import { useTranslation } from "react-i18next";
import type { CourseBlock, CourseModule } from "@/api/course";
import { flattenLessons, resumeTarget, stepLabel } from "@/features/course/courseNav";
import {
  blockLessons,
  courseLessons,
  formatReadingTime,
  moduleLessons,
  remainingSeconds,
} from "@/features/course/readingTime";
import { Badge, Button, Card, Spinner } from "@/components/ui/primitives";
import { useExportPdf, type ExportTarget } from "@/features/pdfExport/useExportPdf";
import { useHeaderAction } from "@/components/layout/headerChrome";
import { usePhoneLayout } from "@/lib/viewport";
import { cn } from "@/lib/cn";
import { OneLineSummary } from "@/features/course/OneLineSummary";
import { useCourse } from "@/features/courses/CourseContext";
import { useCourseTree } from "@/features/course/queries";

function isComplete(m: CourseModule): boolean {
  return m.hasContent && m.lessonsTotal > 0 && m.lessonsCompleted >= m.lessonsTotal;
}

function BlockReadingTime({ block }: { block: CourseBlock }) {
  const { t } = useTranslation();
  const timeLeft = formatReadingTime(remainingSeconds(blockLessons(block)), t);
  if (timeLeft === null) return null;
  return <span className="ml-2 font-normal normal-case">· {timeLeft}</span>;
}

/** A module card's «⋯» menu: its bloque's PDF export. Above the card's stretched link, so it stays tappable. */
function ModuleMenu({ module, onExport }: { module: CourseModule; onExport: (target: ExportTarget) => void }) {
  const { t } = useTranslation();
  const [open, setOpen] = useState(false);
  const ref = useRef<HTMLDivElement>(null);

  useEffect(() => {
    if (!open) return;
    const onDoc = (e: MouseEvent) => {
      if (ref.current && !ref.current.contains(e.target as Node)) setOpen(false);
    };
    const onKey = (e: KeyboardEvent) => {
      if (e.key === "Escape") setOpen(false);
    };
    document.addEventListener("mousedown", onDoc);
    document.addEventListener("keydown", onKey);
    return () => {
      document.removeEventListener("mousedown", onDoc);
      document.removeEventListener("keydown", onKey);
    };
  }, [open]);

  return (
    <div ref={ref} className="relative z-10">
      <button
        type="button"
        aria-haspopup="menu"
        aria-expanded={open}
        aria-label={t("course.moduleActions", { module: module.id.toUpperCase() })}
        onClick={() => setOpen((v) => !v)}
        className="-my-2 -mr-2 inline-flex h-11 w-11 items-center justify-center rounded-md text-lg text-gray-500 hover:bg-gray-100 focus:outline-none focus-visible:ring-2 focus-visible:ring-primary dark:text-gray-400 dark:hover:bg-gray-800 oled:hover:bg-oled-hover"
      >
        <span aria-hidden="true">⋯</span>
      </button>
      {open && (
        <div
          role="menu"
          className="absolute right-0 z-50 mt-1 w-56 max-w-[calc(100vw-2rem)] rounded-lg border border-border bg-white p-1 shadow-lg dark:border-gray-800 dark:bg-gray-900 oled:border-oled-line-strong oled:bg-oled-bg"
        >
          <button
            type="button"
            role="menuitem"
            onClick={() => {
              setOpen(false);
              onExport({ kind: "module", id: module.id, title: module.title });
            }}
            className="w-full rounded-md px-3 py-2 text-left text-sm max-md:min-h-11 hover:bg-gray-100 dark:hover:bg-gray-800 oled:hover:bg-oled-hover"
          >
            {t("course.pdfActionModule")}
          </button>
        </div>
      )}
    </div>
  );
}

function ModuleCard({
  module,
  suggested,
  onExport,
}: {
  module: CourseModule;
  suggested: boolean;
  onExport: (target: ExportTarget) => void;
}) {
  const { t } = useTranslation();
  const { path } = useCourse();
  const complete = isComplete(module);
  // Advisory prereqs are soft: muted text, and never shown once the module is done.
  const showPrereqs = module.unmetPrereqs.length > 0 && !complete;
  // Time LEFT in this module — null once every lesson is read, so a finished card says nothing
  // rather than "~0 min".
  const timeLeft = formatReadingTime(remainingSeconds(moduleLessons(module)), t);

  // A module with exactly one lesson has no useful intermediate page — jump straight to the lesson.
  // The module page is kept for the (data-model-supported) multi-lesson case.
  const target =
    module.lessonsTotal === 1 && module.lessons[0]
      ? path(`/lessons/${module.lessons[0].id}`)
      : path(`/modules/${module.id}`);
  const heading = (
    <>
      <span className="text-gray-400">{module.id.toUpperCase()}</span> · {module.title}
    </>
  );

  // The title link stretches over the whole card, so the card stays one tap target while the summary's
  // «más» (a button, which a link may not contain) sits above it.
  return (
    <Card
      className={cn(
        "relative h-full p-4 transition-colors",
        suggested ? "border-primary ring-1 ring-primary" : module.hasContent ? "hover:border-primary" : "opacity-70",
      )}
    >
      <div className="flex items-start justify-between gap-2">
        <h3 className="font-semibold">
          {module.hasContent ? (
            <Link
              to={target}
              className="after:absolute after:inset-0 after:rounded-lg focus:outline-none focus-visible:after:ring-2 focus-visible:after:ring-primary"
            >
              {heading}
            </Link>
          ) : (
            heading
          )}
        </h3>
        <div className="flex shrink-0 items-start gap-1">
          {suggested && <Badge tone="indigo">{t("course.suggestedNext")}</Badge>}
          {complete && <Badge tone="green">{t("course.completed")}</Badge>}
          {!module.hasContent && <Badge tone="neutral">{t("course.comingSoon")}</Badge>}
          {module.hasContent && <ModuleMenu module={module} onExport={onExport} />}
        </div>
      </div>
      <OneLineSummary text={module.summary} className="mt-1 text-sm text-gray-500 dark:text-gray-400" />

      {module.hasContent && (
        <p className="mt-2 text-xs text-gray-500 dark:text-gray-400">
          <span>{t("course.lessonProgress", { done: module.lessonsCompleted, total: module.lessonsTotal })}</span>
          {module.exercisesTotal > 0 && (
            <>
              {" · "}
              <span>{t("course.exerciseProgress", { done: module.exercisesPassed, total: module.exercisesTotal })}</span>
            </>
          )}
          {timeLeft !== null && (
            <>
              {" · "}
              <span>{timeLeft}</span>
            </>
          )}
        </p>
      )}

      {showPrereqs && (
        <p className="mt-2 text-xs text-gray-400 dark:text-gray-500">
          {t("course.prereqNotice", { modules: module.unmetPrereqs.map((m) => m.toUpperCase()).join(", ") })}
        </p>
      )}
    </Card>
  );
}

export function CoursePage() {
  const { t } = useTranslation();
  const { path, scope } = useCourse();
  const { data: course, isLoading } = useCourseTree();
  const pdf = useExportPdf(course);
  const phone = usePhoneLayout();
  // On phones the whole-course export sits in the header menu (N1); the module cards keep their own.
  useHeaderAction(
    phone && course ? { label: t("course.pdfAction"), run: () => pdf.open({ kind: "course", id: null, title: "" }) } : null,
  );

  // Suggested next = the first module in canonical order that isn't fully completed, whether or not
  // its content is published yet. It always points somewhere until the whole course is done.
  const suggestedModuleId = useMemo(() => {
    if (!course) return null;
    for (const block of course.blocks) {
      for (const module of block.modules) {
        if (!isComplete(module)) return module.id;
      }
    }
    return null;
  }, [course]);

  // Continue = the first not-yet-completed lesson in canonical order (same resolution as the
  // lesson-end "Next" link). Shown only once the learner has begun; fresh accounts see the
  // "Suggested next" badge instead.
  const resume = useMemo(() => (course ? resumeTarget(flattenLessons(course)) : null), [course]);

  // Compact overall progress for the header (across published content only — modules without a
  // lesson contribute 0 to both totals).
  const totals = useMemo(() => {
    let lessonsDone = 0;
    let lessonsTotal = 0;
    let exDone = 0;
    let exTotal = 0;
    for (const block of course?.blocks ?? []) {
      for (const m of block.modules) {
        lessonsTotal += m.lessonsTotal;
        lessonsDone += m.lessonsCompleted;
        exTotal += m.exercisesTotal;
        exDone += m.exercisesPassed;
      }
    }
    return { lessonsDone, lessonsTotal, exDone, exTotal };
  }, [course]);

  // Reading time left in the whole course: the sum of every unread lesson's own seconds, rounded once.
  // Same function, same per-lesson values as each block header and module card below, so the header
  // can never disagree with the numbers under it.
  const timeLeft = useMemo(
    () => (course ? formatReadingTime(remainingSeconds(courseLessons(course)), t) : null),
    [course, t],
  );

  // The header meta line. The progress fractions stay hidden until the learner has begun (a fresh
  // account has nothing to report), but the time estimate does not depend on having begun — for a new
  // reader "how long is this course?" is the question, and remaining time is simply all of it.
  const headerMeta = [
    ...(course?.started
      ? [
          t("course.lessonProgress", { done: totals.lessonsDone, total: totals.lessonsTotal }),
          ...(totals.exTotal > 0
            ? [t("course.exerciseProgress", { done: totals.exDone, total: totals.exTotal })]
            : []),
        ]
      : []),
    ...(timeLeft !== null ? [timeLeft] : []),
  ];

  if (isLoading || !course) {
    return (
      <div className="flex justify-center py-16 text-gray-500">
        <Spinner />
      </div>
    );
  }

  return (
    <div className="space-y-8">
      <div className="flex flex-col gap-3 sm:flex-row sm:items-start sm:justify-between">
        <div>
          <h1 className="text-2xl font-bold" lang={scope.lang}>
            {course.course.title}
          </h1>
          <p className="mt-1 text-sm text-gray-500 dark:text-gray-400">{course.course.description}</p>
          {headerMeta.length > 0 && (
            <p className="mt-2 text-xs font-medium text-gray-500 dark:text-gray-400">
              {headerMeta.join(" · ")}
            </p>
          )}
        </div>
        {!phone && (
          <div className="shrink-0 sm:text-right">
            <Button
              variant="secondary"
              onClick={() => pdf.open({ kind: "course", id: null, title: "" })}
              title={t("course.pdfHint")}
            >
              {t("course.pdfAction")}
            </Button>
          </div>
        )}
      </div>
      {course.started && resume && (
        <Link to={path(`/lessons/${resume.lessonId}`)} className="block">
          <Card className="flex items-center justify-between gap-3 border-primary bg-primary/5 p-4 transition-colors hover:bg-primary/10 dark:bg-primary/10 dark:hover:bg-primary/20">
            <span className="font-medium text-primary">{t("course.continue", { step: stepLabel(resume) })}</span>
            <span aria-hidden className="text-primary">→</span>
          </Card>
        </Link>
      )}
      {course.course.psicotecnicos && course.course.psicotecnicos.length > 0 && (
        <Link to={path("/practice/psicotecnicos")} className="block">
          <Card className="flex items-center justify-between gap-3 p-4 transition-colors hover:border-primary">
            <div>
              <h2 className="font-semibold">{t("psicotecnicos.entry")}</h2>
              <p className="text-sm text-gray-500 dark:text-gray-400">{t("psicotecnicos.entryHint")}</p>
            </div>
            <span aria-hidden className="text-primary">→</span>
          </Card>
        </Link>
      )}
      {course.blocks.map((block) => (
        <section key={block.id}>
          <h2 className="mb-3 text-sm font-semibold tracking-wide text-gray-500 uppercase dark:text-gray-400">
            {block.title}
            {/* The block's own remaining time, in normal case so "min" is not shouted by the uppercase heading. */}
            <BlockReadingTime block={block} />
          </h2>
          <div className="grid grid-cols-1 gap-3 sm:grid-cols-2">
            {block.modules.map((module) => (
              <ModuleCard
                key={module.id}
                module={module}
                suggested={module.id === suggestedModuleId}
                onExport={pdf.open}
              />
            ))}
          </div>
        </section>
      ))}
      <p className="border-t border-border pt-4 text-xs text-gray-400 dark:border-gray-800 dark:text-gray-500 oled:border-oled-line">
        {t("course.prereqFootnote")}
      </p>
      {pdf.dialog}
    </div>
  );
}
