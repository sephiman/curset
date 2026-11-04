import { useEffect, useRef, type ReactNode } from "react";
import { createPortal } from "react-dom";
import { useTranslation } from "react-i18next";

/** A bottom sheet over a dimmed page (a centred dialog from 768 px): Escape, the backdrop and the close button dismiss it. */
export function Sheet({ title, onClose, children }: { title: string; onClose: () => void; children: ReactNode }) {
  const { t } = useTranslation();
  const panel = useRef<HTMLDivElement>(null);

  useEffect(() => {
    const opener = document.activeElement instanceof HTMLElement ? document.activeElement : null;
    panel.current?.focus();
    const onKey = (event: KeyboardEvent) => {
      if (event.key === "Escape") onClose();
    };
    document.addEventListener("keydown", onKey);
    const { overflow } = document.body.style;
    document.body.style.overflow = "hidden";
    return () => {
      document.removeEventListener("keydown", onKey);
      document.body.style.overflow = overflow;
      opener?.focus();
    };
  }, [onClose]);

  return createPortal(
    <div className="fixed inset-0 z-[90] flex flex-col justify-end md:items-center md:justify-center md:p-6">
      <div aria-hidden="true" onClick={onClose} className="absolute inset-0 bg-black/50" />
      <div
        ref={panel}
        role="dialog"
        aria-modal="true"
        aria-label={title}
        tabIndex={-1}
        className="relative max-h-[85dvh] overflow-y-auto rounded-t-2xl border-t border-border md:w-full md:max-w-md md:rounded-2xl md:border md:pb-4 bg-white px-4 pt-3 pb-[calc(1rem+env(safe-area-inset-bottom))] focus:outline-none dark:border-gray-800 dark:bg-gray-900 oled:border-oled-line-strong oled:bg-oled-bg"
      >
        <div className="mb-3 flex items-center justify-between gap-3">
          <h2 className="text-base font-semibold">{title}</h2>
          <button
            type="button"
            onClick={onClose}
            aria-label={t("common.close")}
            className="-mr-2 inline-flex h-11 w-11 items-center justify-center rounded-md text-xl text-gray-500 hover:bg-gray-100 focus:outline-none focus-visible:ring-2 focus-visible:ring-primary dark:text-gray-400 dark:hover:bg-gray-800 oled:hover:bg-oled-hover"
          >
            ×
          </button>
        </div>
        {children}
      </div>
    </div>,
    document.body,
  );
}
