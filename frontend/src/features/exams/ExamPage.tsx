import { useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import { useMutation, useQuery, useQueryClient } from "@tanstack/react-query";
import { useTranslation } from "react-i18next";
import type { TFunction } from "i18next";
import {
  examHistory,
  getExamPresets,
  getOpenExams,
  startExam,
  type ExamHistoryItem,
  type ExamPreset,
  type ExamSession,
} from "@/api/exams";
import { Badge, Button, Card, Spinner } from "@/components/ui/primitives";
import { ConfirmDialog } from "@/components/ui/ConfirmDialog";
import { scopeKey, useCourse } from "@/features/courses/CourseContext";
import { examScore, sittingName } from "@/features/exams/format";
import { generateExamPdf } from "@/lib/pdf/examDocument";
import { downloadPdf } from "@/lib/pdf/generate";

/** One line per part: what it draws, how many questions, how many in reserve. */
function partLine(preset: ExamPreset, t: TFunction): string[] {
  return preset.parts.map((part) => {
    const title = part.title ?? preset.title;
    const base =
      part.kind === "cases"
        ? t("exam.partCases", { title, choose: part.choose, count: part.questions })
        : t("exam.partQuestions", { title, count: part.questions });
    return part.reserve ? `${base}, ${t("exam.reserveCount", { count: part.reserve })}` : base;
  });
}

function penaltyLine(preset: ExamPreset, t: TFunction): string {
  const penalties = new Set(preset.parts.map((part) => part.penalty));
  const [only] = [...penalties];
  return penalties.size === 1 && only === "0" ? t("exam.noPenalty") : t("exam.penalty", { fraction: only });
}

function PresetCard({
  preset,
  disabled,
  onStart,
}: {
  preset: ExamPreset;
  disabled: boolean;
  onStart: (target?: string) => void;
}) {
  const { t } = useTranslation();
  const { scope: courseScope } = useCourse();
  const [downloading, setDownloading] = useState(false);

  const handlePdf = async () => {
    try {
      setDownloading(true);
      const generated = await generateExamPdf(courseScope, preset.id);
      downloadPdf(generated);
    } catch (e) {
      console.error("PDF export failed:", e);
    } finally {
      setDownloading(false);
    }
  };

  const time = preset.timeLimitMinutes ? t("exam.minutes", { count: preset.timeLimitMinutes }) : t("exam.untimed");
  return (
    <Card className="space-y-3 p-4">
      <div className="flex flex-wrap items-baseline justify-between gap-2">
        <h3 className="font-semibold">{preset.title}</h3>
        <span className="text-xs text-gray-500 dark:text-gray-400">
          {preset.targets ? time : `${t("exam.questions", { count: preset.questions })} · ${time}`}
        </span>
      </div>
      {preset.description && (
        <p className="text-xs text-gray-600 dark:text-gray-300">{preset.description}</p>
      )}
      {preset.parts.length > 1 && (
        <ul className="space-y-0.5 text-sm text-gray-600 dark:text-gray-300">
          {partLine(preset, t).map((line) => (
            <li key={line}>{line}</li>
          ))}
        </ul>
      )}
      <p className="text-xs text-gray-500 dark:text-gray-400">{penaltyLine(preset, t)}</p>
      {preset.targets ? (
        <div>
          <p className="mb-2 text-sm font-medium">{t("exam.chooseTarget")}</p>
          <div className="grid gap-2 sm:grid-cols-2">
            {preset.targets.map((target) => (
              <Button
                key={target.id}
                variant="secondary"
                disabled={disabled}
                onClick={() => onStart(target.id)}
                className="justify-between text-left"
              >
                <span className="truncate">{target.title}</span>
                <span className="shrink-0 text-xs text-gray-500">{t("exam.questions", { count: target.questions })}</span>
              </Button>
            ))}
          </div>
        </div>
      ) : (
        <div className="flex flex-wrap items-center gap-2">
          <Button disabled={disabled} onClick={() => onStart()}>
            {t("exam.start")}
          </Button>
          <Button
            variant="secondary"
            disabled={downloading}
            onClick={handlePdf}
            title={t("exam.exportPdf")}
          >
            {downloading && <Spinner className="mr-1.5 h-3.5 w-3.5" />}
            {t("exam.exportPdf")}
          </Button>
        </div>
      )}
    </Card>
  );
}

function HistoryRow({ item }: { item: ExamHistoryItem }) {
  const { i18n } = useTranslation();
  const { path } = useCourse();
  return (
    <Link to={path(`/exams/${item.id}/review`)} className="block">
      <Card className="flex items-center justify-between gap-3 p-3 hover:border-primary">
        <div className="min-w-0">
          <p className="truncate text-sm font-medium">{sittingName(item)}</p>
          <p className="text-xs text-gray-500 dark:text-gray-400">
            {item.finishedAt ? new Date(item.finishedAt).toLocaleDateString(i18n.resolvedLanguage) : "—"}
          </p>
        </div>
        <div className="flex shrink-0 items-center gap-2">
          {item.transformed == null && (
            <span className="text-xs text-gray-500 dark:text-gray-400">
              {item.correct}/{item.total}
            </span>
          )}
          <Badge tone="indigo">{examScore(item, i18n.resolvedLanguage)}</Badge>
        </div>
      </Card>
    </Link>
  );
}

export function ExamPage() {
  const { t } = useTranslation();
  const navigate = useNavigate();
  const qc = useQueryClient();
  const { scope: courseScope, path } = useCourse();

  const { data: presets } = useQuery({
    queryKey: ["exam", ...scopeKey(courseScope), "presets"],
    queryFn: () => getExamPresets(courseScope),
  });
  const { data: open } = useQuery({
    queryKey: ["exam", ...scopeKey(courseScope), "open"],
    queryFn: () => getOpenExams(courseScope),
  });
  const { data: history, isLoading } = useQuery({
    queryKey: ["exam", ...scopeKey(courseScope), "history"],
    queryFn: () => examHistory(courseScope),
  });

  const start = useMutation({
    mutationFn: ({ presetId, target }: { presetId: string; target?: string }) =>
      startExam(courseScope, presetId, target),
    onSuccess: (s: ExamSession) => {
      void qc.invalidateQueries({ queryKey: ["exam", courseScope.slug] });
      navigate(path(`/exams/${s.id}`));
    },
  });

  // What the reader asked to start, held back while they answer for the sitting it would abandon.
  const [pending, setPending] = useState<{ presetId: string; target?: string } | null>(null);

  /**
   * The open sitting a start would destroy. The server abandons an open sitting of the SAME preset and
   * target and only that one, so this asks exactly when something is at stake and never otherwise — a
   * confirmation that fires when nothing would be lost is one readers learn to dismiss unread.
   */
  const conflicting = (presetId: string, target?: string): ExamSession | null =>
    (open ?? []).find((s) => s.presetId === presetId && (s.target ?? undefined) === target) ?? null;

  const requestStart = (presetId: string, target?: string): void => {
    if (conflicting(presetId, target)) setPending({ presetId, target });
    else start.mutate({ presetId, target });
  };

  const doomed = pending ? conflicting(pending.presetId, pending.target) : null;

  const answered = (session: ExamSession): string =>
    t("exam.conflictAnswered", {
      done: session.questions.filter((q) => q.answered).length,
      total: session.questions.length,
    });

  return (
    <div className="space-y-8">
      {pending && doomed && (
        <ConfirmDialog
          title={t("exam.conflictTitle")}
          confirmLabel={t("exam.conflictStartNew")}
          cancelLabel={t("exam.conflictResume")}
          onConfirm={() => {
            const request = pending;
            setPending(null);
            start.mutate(request);
          }}
          onCancel={() => {
            setPending(null);
            navigate(path(`/exams/${doomed.id}`));
          }}
          // Escape and the backdrop mean "I did not mean to press that", not "take me to the exam".
          onDismiss={() => setPending(null)}
        >
          <p className="font-medium text-gray-900 dark:text-gray-100">
            {sittingName(doomed)} · {answered(doomed)}
          </p>
          <p>{t("exam.conflictBody")}</p>
        </ConfirmDialog>
      )}
      <div>
        <h1 className="text-2xl font-bold">{t("nav.exams")}</h1>
        <p className="mt-1 text-sm text-gray-500 dark:text-gray-400">{t("exam.intro")}</p>
      </div>

      {/* One card per open sitting: two can be open at once, and each needs a way back in. */}
      {(open ?? []).map((sitting) => (
        <Card
          key={sitting.id}
          className="flex flex-wrap items-center justify-between gap-3 border-primary bg-primary/5 p-4 dark:bg-primary/10"
        >
          <div>
            <p className="text-xs font-medium tracking-wide text-primary uppercase">{t("exam.inProgress")}</p>
            <p className="text-sm text-gray-600 dark:text-gray-300">{sittingName(sitting)}</p>
          </div>
          <Button onClick={() => navigate(path(`/exams/${sitting.id}`))}>{t("exam.resume")}</Button>
        </Card>
      ))}

      <section className="space-y-3">
        <h2 className="text-sm font-semibold tracking-wide text-gray-500 uppercase dark:text-gray-400">
          {t("exam.startTitle")}
        </h2>
        {presets && presets.length === 0 && (
          <p className="text-sm text-gray-500 dark:text-gray-400">{t("exam.noPresets")}</p>
        )}
        {(presets ?? []).map((preset) => (
          <PresetCard
            key={preset.id}
            preset={preset}
            disabled={start.isPending}
            onStart={(target) => requestStart(preset.id, target)}
          />
        ))}
      </section>

      <section className="space-y-3">
        <h2 className="text-sm font-semibold tracking-wide text-gray-500 uppercase dark:text-gray-400">
          {t("exam.historyTitle")}
        </h2>
        {isLoading ? (
          <div className="flex justify-center py-8 text-gray-500">
            <Spinner />
          </div>
        ) : !history?.length ? (
          <p className="text-sm text-gray-500 dark:text-gray-400">{t("exam.noHistory")}</p>
        ) : (
          <div className="space-y-2">
            {history.map((item) => (
              <HistoryRow key={item.id} item={item} />
            ))}
          </div>
        )}
      </section>
    </div>
  );
}
