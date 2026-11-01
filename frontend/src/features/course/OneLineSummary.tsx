import { useLayoutEffect, useRef, useState } from "react";
import { useTranslation } from "react-i18next";
import { cn } from "@/lib/cn";
import { usePhoneLayout } from "@/lib/viewport";

/** A card summary: one line on a phone, with «más» when it is cut (J5); above 768 px in full, or not at all with `phoneOnly`. */
export function OneLineSummary({ text, className, phoneOnly = false }: { text: string; className?: string; phoneOnly?: boolean }) {
  const { t } = useTranslation();
  const phone = usePhoneLayout();
  const ref = useRef<HTMLParagraphElement>(null);
  const [expanded, setExpanded] = useState(false);
  const [clipped, setClipped] = useState(false);

  useLayoutEffect(() => {
    const element = ref.current;
    if (!phone || expanded || !element) return;
    const measure = () => setClipped(element.scrollWidth > element.clientWidth + 1);
    measure();
    const observer = typeof ResizeObserver === "function" ? new ResizeObserver(measure) : null;
    observer?.observe(element);
    return () => observer?.disconnect();
  }, [phone, expanded, text]);

  if (!phone) return phoneOnly ? null : <p className={className}>{text}</p>;
  return (
    <div className={cn("relative z-10 flex items-baseline gap-1", className)}>
      <p ref={ref} className={cn("min-w-0 flex-1", !expanded && "truncate")}>
        {text}
      </p>
      {(clipped || expanded) && (
        <button
          type="button"
          aria-expanded={expanded}
          onClick={() => setExpanded((open) => !open)}
          className="-my-3 inline-flex min-h-11 shrink-0 items-center px-1 font-medium text-primary focus:outline-none focus-visible:ring-2 focus-visible:ring-primary"
        >
          {expanded ? t("course.summaryLess") : t("course.summaryMore")}
        </button>
      )}
    </div>
  );
}
