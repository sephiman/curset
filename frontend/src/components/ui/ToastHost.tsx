import { useEffect, useState } from "react";
import { cn } from "@/lib/cn";
import { usePhoneLayout } from "@/lib/viewport";
import { dismissToast, subscribeToasts, type Toast } from "@/lib/toastBus";

export function ToastHost() {
  const [toasts, setToasts] = useState<Toast[]>([]);
  useEffect(() => subscribeToasts(setToasts), []);
  // On the phone layout toasts are small pills at the top, clear of the bottom bars (J3).
  const phone = usePhoneLayout();

  if (toasts.length === 0) return null;

  return (
    <div
      aria-live="polite"
      aria-atomic="true"
      className={cn(
        "pointer-events-none fixed z-[100] flex flex-col gap-2",
        phone
          ? "inset-x-0 top-[calc(0.5rem+env(safe-area-inset-top))] items-center px-4"
          : "right-4 bottom-4 w-80 max-w-[calc(100vw-2rem)]",
      )}
    >
      {toasts.map((t) => (
        <button
          key={t.id}
          type="button"
          onClick={() => dismissToast(t.id)}
          className={cn(
            // The tinted fills carry themselves on black; the hairline does not — `ring-black/10`
            // over a black page is black on black, and `shadow-lg` has nothing to fall on, so the
            // one floating element in the app would lose its edge. It flips to a light ring instead.
            "pointer-events-auto flex items-start gap-2 text-left font-medium text-white shadow-lg ring-1 ring-black/10 oled:ring-white/15",
            phone ? "max-w-full rounded-full px-3 py-1 text-xs" : "w-full rounded-md px-3 py-2 text-sm",
            t.kind === "success" && "bg-emerald-600 hover:bg-emerald-700",
            t.kind === "error" && "bg-red-600 hover:bg-red-700",
            t.kind === "info" && "bg-gray-700 hover:bg-gray-800",
          )}
        >
          <span className="flex-1">{t.message}</span>
          <span aria-hidden="true" className="opacity-70">×</span>
        </button>
      ))}
    </div>
  );
}
