import { useLayoutEffect, useRef, useState } from "react";
import { useTranslation } from "react-i18next";
import { cn } from "@/lib/cn";
import { usePhoneLayout } from "@/lib/viewport";

/** A summary cut to one line with «más» when it is cut: on a phone only (cards, J5), or at every width (lesson rows, K6). */
export function OneLineSummary({
  text,
  className,
  everywhere = false,
}: {
  text: string;
  className?: string;
  everywhere?: boolean;
}) {
  const { t } = useTranslation();
  const phone = usePhoneLayout();
  const oneLine = everywhere || phone;
  const ref = useRef<HTMLParagraphElement>(null);
  const [expanded, setExpanded] = useState(false);
  const [clipped, setClipped] = useState(false);

  useLayoutEffect(() => {
    const element = ref.current;
    if (!oneLine || expanded || !element) return;
    const measure = () => setClipped(element.scrollWidth > element.clientWidth + 1);
    measure();
    const observer = typeof ResizeObserver === "function" ? new ResizeObserver(measure) : null;
    observer?.observe(element);
    return () => observer?.disconnect();
  }, [oneLine, expanded, text]);

  if (!oneLine) return <p className={className}>{text}</p>;
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
