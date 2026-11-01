import { useSyncExternalStore } from "react";

/** Below the `md` breakpoint (768 px): the bottom tab bar, the one-line header, the phone exam sitting. */
export const PHONE_QUERY = "(max-width: 767.98px)";
/** Below the `sm` breakpoint (640 px): esquema tables become stacked cards. */
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

/** Below 768 px: bottom tab bar, one-line header, phone exam sitting (delta J1–J3). */
export function usePhoneLayout(): boolean {
  return useMediaQuery(PHONE_QUERY);
}

/** Below 640 px: esquemas stack, tables as cards and lists vertical (delta J4). */
export function useStackedEsquemas(): boolean {
  return useMediaQuery(NARROW_QUERY);
}
