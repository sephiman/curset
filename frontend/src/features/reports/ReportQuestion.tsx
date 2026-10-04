import { useId, useState } from "react";
import { useMutation } from "@tanstack/react-query";
import { useTranslation } from "react-i18next";
import { apiErrorMessage } from "@/api/client";
import { reportQuestion } from "@/api/reports";
import { Button } from "@/components/ui/primitives";
import { useCourse } from "@/features/courses/CourseContext";

export const REPORT_MIN = 5;
export const REPORT_MAX = 1000;

/**
 * "Report this question" (R8a): a red button that opens one free-text box. Rendered only where the
 * answer is already on screen — after answering, or in a submitted exam's review — so it can never ask
 * for one. The open box and the thanks take a full row, so it can sit in a row of buttons.
 */
export function ReportQuestion({ attemptId }: { attemptId: string }) {
  const { t } = useTranslation();
  const { scope } = useCourse();
  const fieldId = useId();
  const [open, setOpen] = useState(false);
  const [message, setMessage] = useState("");
  const [sent, setSent] = useState(false);

  const send = useMutation({
    mutationFn: () => reportQuestion(scope, attemptId, message.trim()),
    meta: { silentSuccess: true, silentError: true },
    onSuccess: () => {
      setOpen(false);
      setSent(true);
    },
  });

  if (sent) {
    return (
      <p role="status" className="basis-full text-xs text-gray-500 dark:text-gray-400">
        {t("report.thanks")}
      </p>
    );
  }
  if (!open) {
    return (
      <Button variant="danger" onClick={() => setOpen(true)}>
        {t("report.link")}
      </Button>
    );
  }

  const length = message.trim().length;
  const valid = length >= REPORT_MIN && length <= REPORT_MAX;
  return (
    <form
      className="basis-full space-y-2"
      onSubmit={(event) => {
        event.preventDefault();
        if (valid) send.mutate();
      }}
    >
      <label htmlFor={fieldId} className="block text-xs font-medium text-gray-600 dark:text-gray-300">
        {t("report.question")}
      </label>
      <textarea
        id={fieldId}
        value={message}
        onChange={(event) => setMessage(event.target.value)}
        required
        minLength={REPORT_MIN}
        maxLength={REPORT_MAX}
        rows={3}
        className="block w-full rounded-md border border-border bg-white px-3 py-2 text-sm shadow-sm focus:border-primary focus:outline-none focus:ring-1 focus:ring-primary dark:border-gray-600 dark:bg-gray-800 dark:text-gray-100 oled:border-oled-line-strong oled:bg-oled-bg"
      />
      <div className="flex flex-wrap items-center gap-3">
        <Button type="submit" variant="secondary" disabled={!valid || send.isPending}>
          {t("report.send")}
        </Button>
        <span className="text-xs text-gray-500 dark:text-gray-400">
          {t("report.length", { length, min: REPORT_MIN, max: REPORT_MAX })}
        </span>
      </div>
      {send.isError && (
        <p role="alert" className="text-xs text-red-600 dark:text-red-400">
          {apiErrorMessage(send.error, t)}
        </p>
      )}
    </form>
  );
}
