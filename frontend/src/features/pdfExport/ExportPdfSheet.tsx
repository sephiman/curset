import { Link } from "react-router-dom";
import { useTranslation } from "react-i18next";
import { Button, Spinner } from "@/components/ui/primitives";
import { Sheet } from "@/components/ui/Sheet";
import type { GenerateProgress } from "@/lib/pdf/generate";

/** The export dialog: what is printed, whether exercises come with it (the Cuenta setting), and the run. */
export function ExportPdfSheet({
  scopeLabel,
  kind,
  withExercises,
  busy,
  progress,
  error,
  onExport,
  onClose,
}: {
  scopeLabel: string;
  kind: "course" | "module" | "lesson";
  withExercises: boolean;
  busy: boolean;
  progress: GenerateProgress | null;
  error: string | null;
  onExport: () => void;
  onClose: () => void;
}) {
  const { t } = useTranslation();
  const title = kind === "module" ? t("course.pdfActionModule") : t("course.pdfAction");

  const phase = (): string => {
    if (!progress) return t("course.pdfBusy");
    const { phase: step, done, total } = progress;
    if (step === "figures" && total > 0) return t("course.pdfFigures", { done, total });
    if (step === "charts" && total > 0) return t("course.pdfCharts", { done, total });
    if (step === "exercises") return t("course.pdfExercises");
    if (step === "typeset") return t("course.pdfTypesetting");
    return t("course.pdfPreparing");
  };

  return (
    <Sheet title={title} onClose={onClose}>
      <div className="space-y-4">
        <p className="font-medium">{scopeLabel}</p>
        <p className="text-sm text-gray-600 dark:text-gray-300">
          {withExercises ? t("course.pdfWithExercises") : t("course.pdfTheoryOnly")}
          {" · "}
          <Link to="/account" onClick={onClose} className="text-primary hover:underline">
            {t("course.pdfChangeSetting")}
          </Link>
        </p>
        {busy && (
          <p role="status" className="text-sm text-gray-600 dark:text-gray-300">
            {t("course.pdfProgress", { scope: scopeLabel, phase: phase() })}
          </p>
        )}
        {error && (
          <p role="alert" className="text-sm text-red-600 dark:text-red-400">
            {t("course.pdfFailed", { reason: error })}
          </p>
        )}
        <div className="flex justify-end">
          <Button onClick={onExport} disabled={busy} aria-busy={busy}>
            {busy && <Spinner className="mr-2 h-4 w-4" />}
            {error ? t("course.pdfRetry") : t("course.pdfStart")}
          </Button>
        </div>
      </div>
    </Sheet>
  );
}
