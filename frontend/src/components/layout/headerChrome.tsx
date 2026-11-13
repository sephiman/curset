import { createContext, useContext, useEffect, useRef, useState, type ReactNode } from "react";

export interface HeaderBack {
  to: string;
  label: string;
  /** Shown beside the back link in the desktop header (a lesson's reading time, K2); the phone header has no room. */
  note?: string | null;
}

/** A page's own action, offered in the avatar menu on phones (the page's PDF export). */
export interface HeaderAction {
  label: string;
  run: () => void;
}

interface HeaderChrome {
  back: HeaderBack | null;
  setBack: (back: HeaderBack | null) => void;
  action: HeaderAction | null;
  setAction: (action: HeaderAction | null) => void;
  focused: boolean;
  setFocused: (focused: boolean) => void;
}

const HeaderChromeContext = createContext<HeaderChrome>({
  back: null,
  setBack: () => undefined,
  action: null,
  setAction: () => undefined,
  focused: false,
  setFocused: () => undefined,
});

/** What a page asks of the app chrome: a back link in the header bar, or focus mode (no tab bar). */
export function HeaderChromeProvider({ children }: { children: ReactNode }) {
  const [back, setBack] = useState<HeaderBack | null>(null);
  const [action, setAction] = useState<HeaderAction | null>(null);
  const [focused, setFocused] = useState(false);
  return (
    <HeaderChromeContext.Provider value={{ back, setBack, action, setAction, focused, setFocused }}>
      {children}
    </HeaderChromeContext.Provider>
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

export function useHeaderActionTarget(): HeaderAction | null {
  return useContext(HeaderChromeContext).action;
}

/** Offers the page's action in the header menu while it is mounted; null offers nothing. */
export function useHeaderAction(action: HeaderAction | null): void {
  const { setAction } = useContext(HeaderChromeContext);
  const run = useRef(action?.run);
  const label = action?.label ?? null;
  useEffect(() => {
    run.current = action?.run;
  });
  useEffect(() => {
    if (label === null) return;
    setAction({ label, run: () => run.current?.() });
    return () => setAction(null);
  }, [setAction, label]);
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
