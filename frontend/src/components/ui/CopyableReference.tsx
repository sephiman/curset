import { useState } from "react";
import { useTranslation } from "react-i18next";
import { cn } from "@/lib/cn";

/**
 * A copyable pill showing the stable question reference (e.g. «age-c1 · III.3 · q127»).
 * Clicking copies the reference to the clipboard and gives brief visual feedback.
 */
export function CopyableReference({
  reference,
  className,
}: {
  reference: string;
  className?: string;
}) {
  const { t } = useTranslation();
  const [copied, setCopied] = useState(false);

  const copy = async () => {
    try {
      if (typeof navigator !== "undefined" && navigator.clipboard?.writeText) {
        await navigator.clipboard.writeText(reference);
      }
      setCopied(true);
      setTimeout(() => setCopied(false), 2000);
    } catch {
      // Clipboard write failed or denied
    }
  };

  return (
    <button
      type="button"
      onClick={copy}
      title={t("solution.copyReference", "Copiar referencia")}
      aria-label={`${reference} · ${copied ? t("solution.copied", "Copiado") : t("solution.copyReference", "Copiar referencia")}`}
      className={cn(
        "inline-flex items-center gap-1.5 rounded border border-border bg-gray-50 px-2 py-0.5 font-mono text-xs text-gray-600 transition-colors hover:border-primary/60 hover:text-gray-900 dark:border-gray-700 dark:bg-gray-800 dark:text-gray-300 dark:hover:text-gray-100 oled:border-oled-line oled:bg-oled-bg",
        copied && "border-emerald-500 text-emerald-600 dark:text-emerald-400",
        className,
      )}
    >
      <span>{reference}</span>
      <span aria-hidden className="text-[10px] text-gray-400 dark:text-gray-500">
        {copied ? "✓" : "📋"}
      </span>
    </button>
  );
}
