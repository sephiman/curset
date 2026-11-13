import { useCallback, useState, type ReactNode } from "react";
import { useMutation } from "@tanstack/react-query";
import type { Course } from "@/api/course";
import { useAuth } from "@/auth/AuthContext";
import { useCourse } from "@/features/courses/CourseContext";
import { useCatalogue } from "@/features/courses/useCourses";
import { ExportPdfSheet } from "@/features/pdfExport/ExportPdfSheet";
import i18n from "@/i18n";
import { pdfExerciseMode } from "@/lib/pdf/exerciseMode";
import { downloadPdf, generateCoursePdf, type GenerateProgress } from "@/lib/pdf/generate";
import { pdfLabels } from "@/lib/pdf/labels";

/** What one export prints: the whole course, one module (bloque) or one lesson (tema). */
export interface ExportTarget {
  kind: "course" | "module" | "lesson";
  /** The module or lesson id; null for the whole course. */
  id: string | null;
  /** The module's or lesson's own title (unused for the course). */
  title: string;
}

/** `M03 · Derecho administrativo` — how the cover, the dialog and the progress name a scope. */
export function targetLabel(target: ExportTarget, courseTitle: string): string {
  return target.id ? `${target.id.toUpperCase()} · ${target.title}` : courseTitle;
}

/**
 * One export dialog for a page: `open(target)` from any of its buttons or menus, `dialog` rendered once.
 *
 * Every printed word is resolved here and handed over as `labels`, which keeps `lib/pdf/` free of i18next.
 */
export function useExportPdf(tree: Course | undefined): {
  open: (target: ExportTarget) => void;
  dialog: ReactNode;
} {
  const course = tree?.course;
  const { user } = useAuth();
  const { scope } = useCourse();
  const { data: catalogue } = useCatalogue();
  const [target, setTarget] = useState<ExportTarget | null>(null);
  const [progress, setProgress] = useState<GenerateProgress | null>(null);
  const accentOnPaper = catalogue?.find((entry) => entry.slug === scope.slug)?.color?.light;
  const mode = course ? pdfExerciseMode(course, user?.pdf_exercises ?? false) : "none";

  const exportPdf = useMutation({
    // Success is the file landing in the downloads folder; failure is reported in the dialog.
    meta: { silentSuccess: true, silentError: true },
    mutationFn: async (chosen: ExportTarget) => {
      if (!course || !tree) throw new Error("the course is still loading");
      // The book is printed in the course's reading language, labels and all (R4.5).
      const locale = scope.lang;
      const print = i18n.getFixedT(locale);
      const date = new Date();
      const labels = pdfLabels(
        print,
        print("course.pdfGenerated", {
          language: print("course.pdfLanguage"),
          date: date.toLocaleDateString(locale === "es" ? "es-ES" : "en-GB"),
        }),
      );
      const generated = await generateCoursePdf({
        scope,
        part:
          chosen.kind === "course" || !chosen.id
            ? undefined
            : { kind: chosen.kind, id: chosen.id, title: targetLabel(chosen, course.title) },
        outline: tree,
        courseId: course.id,
        courseTitle: course.title,
        courseSubtitle: course.subtitle,
        courseDescription: course.description,
        accentOnPaper,
        exercises: mode,
        labels,
        date,
        onProgress: setProgress,
      });
      downloadPdf(generated);
    },
    onSettled: () => setProgress(null),
    onSuccess: () => setTarget(null),
  });

  const open = useCallback(
    (chosen: ExportTarget) => {
      exportPdf.reset();
      setTarget(chosen);
    },
    [exportPdf],
  );

  const dialog =
    target && course ? (
      <ExportPdfSheet
        scopeLabel={targetLabel(target, course.title)}
        kind={target.kind}
        withExercises={mode !== "none"}
        busy={exportPdf.isPending}
        progress={progress}
        error={exportPdf.isError ? errorReason(exportPdf.error) : null}
        onExport={() => exportPdf.mutate(target)}
        onClose={() => {
          if (!exportPdf.isPending) setTarget(null);
        }}
      />
    ) : null;

  return { open, dialog };
}

function errorReason(error: unknown): string {
  return error instanceof Error ? error.message : String(error);
}

