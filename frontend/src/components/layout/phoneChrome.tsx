import { createContext, useContext, useEffect, useState, type ReactNode } from "react";

export interface HeaderBack {
  to: string;
  label: string;
}

interface PhoneChrome {
  back: HeaderBack | null;
  setBack: (back: HeaderBack | null) => void;
  focused: boolean;
  setFocused: (focused: boolean) => void;
}

const PhoneChromeContext = createContext<PhoneChrome>({
  back: null,
  setBack: () => undefined,
  focused: false,
  setFocused: () => undefined,
});

/** What a page asks of the phone chrome: a back arrow in the header, or focus mode (no tab bar). */
export function PhoneChromeProvider({ children }: { children: ReactNode }) {
  const [back, setBack] = useState<HeaderBack | null>(null);
  const [focused, setFocused] = useState(false);
  return (
    <PhoneChromeContext.Provider value={{ back, setBack, focused, setFocused }}>{children}</PhoneChromeContext.Provider>
  );
}

export function useHeaderBackTarget(): HeaderBack | null {
  return useContext(PhoneChromeContext).back;
}

/** Registers the page's «← parent» as the header's back arrow while it is mounted. */
export function useHeaderBack(to: string, label: string): void {
  const { setBack } = useContext(PhoneChromeContext);
  useEffect(() => {
    setBack({ to, label });
    return () => setBack(null);
  }, [setBack, to, label]);
}

export function useIsFocusMode(): boolean {
  return useContext(PhoneChromeContext).focused;
}

/** An exam sitting is focus mode: the tab bar is hidden so it can neither crowd the page nor be tapped away. */
export function useFocusMode(): void {
  const { setFocused } = useContext(PhoneChromeContext);
  useEffect(() => {
    setFocused(true);
    return () => setFocused(false);
  }, [setFocused]);
}
