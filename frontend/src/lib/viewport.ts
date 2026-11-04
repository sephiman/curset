import { useSyncExternalStore } from "react";

/** Below the `md` breakpoint (768 px): the bottom tab bar and the one-line header. */
export const PHONE_QUERY = "(max-width: 767.98px)";
/** Below the `lg` breakpoint (1024 px): no lesson index, the J3 exam sitting, toasts as pills at the top. */
export const COMPACT_QUERY = "(max-width: 1023.98px)";
/** Below the `sm` breakpoint (640 px): esquema tables and «Por tema» become stacked cards. */
export const NARROW_QUERY = "(max-width: 639.98px)";

function mediaList(query: string): MediaQueryList | null {
  return typeof window !== "undefined" && typeof window.matchMedia === "function" ? window.matchMedia(query) : null;
}

/** Whether the media query matches now, re-rendering when it flips; false where there is no `matchMedia`. */
export function useMediaQuery(query: string): boolean {
  return useSyncExternalStore(
    (onChange) => {
      const list = mediaList(query);
      list?.addEventListener("change", onChange);
      return () => list?.removeEventListener("change", onChange);
    },
    () => mediaList(query)?.matches ?? false,
    () => false,
  );
}

/** Below 768 px: bottom tab bar and one-line header (delta J1–J2). */
export function usePhoneLayout(): boolean {
  return useMediaQuery(PHONE_QUERY);
}

/** Below 640 px: esquemas stack (J4) and «Por tema» is one card per lesson (K5). */
export function useNarrowLayout(): boolean {
  return useMediaQuery(NARROW_QUERY);
}

/** Below 1024 px: the lesson has no side index and the exam sitting is the J3 one (delta K2–K3). */
export function useCompactLayout(): boolean {
  return useMediaQuery(COMPACT_QUERY);
}
