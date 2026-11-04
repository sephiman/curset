import { createContext, useContext, useEffect, useState, type ReactNode } from "react";

export interface HeaderBack {
  to: string;
  label: string;
  /** Shown beside the back link in the desktop header (a lesson's reading time, K2); the phone header has no room. */
  note?: string | null;
}

interface HeaderChrome {
  back: HeaderBack | null;
  setBack: (back: HeaderBack | null) => void;
  focused: boolean;
  setFocused: (focused: boolean) => void;
}

const HeaderChromeContext = createContext<HeaderChrome>({
  back: null,
  setBack: () => undefined,
  focused: false,
  setFocused: () => undefined,
});

/** What a page asks of the app chrome: a back link in the header bar, or focus mode (no tab bar). */
export function HeaderChromeProvider({ children }: { children: ReactNode }) {
  const [back, setBack] = useState<HeaderBack | null>(null);
  const [focused, setFocused] = useState(false);
  return (
    <HeaderChromeContext.Provider value={{ back, setBack, focused, setFocused }}>{children}</HeaderChromeContext.Provider>
  );
}

export function useHeaderBackTarget(): HeaderBack | null {
  return useContext(HeaderChromeContext).back;
}

/** Registers the page's «← parent» as the header's back link while it is mounted. */
export function useHeaderBack(to: string, label: string, note: string | null = null): void {
  const { setBack } = useContext(HeaderChromeContext);
  useEffect(() => {
    setBack({ to, label, note });
    return () => setBack(null);
  }, [setBack, to, label, note]);
}

export function useIsFocusMode(): boolean {
  return useContext(HeaderChromeContext).focused;
}

/** An exam sitting is focus mode: the tab bar is hidden so it can neither crowd the page nor be tapped away. */
export function useFocusMode(): void {
  const { setFocused } = useContext(HeaderChromeContext);
  useEffect(() => {
    setFocused(true);
    return () => setFocused(false);
  }, [setFocused]);
}
