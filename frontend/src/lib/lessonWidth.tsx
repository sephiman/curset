import { createContext, useContext, useEffect, useMemo, useState, type ReactNode } from "react";

export type LessonWidth = "normal" | "wide" | "full";

const STORAGE_KEY = "lessonWidth";

export const LESSON_WIDTH_CLASS: Record<LessonWidth, string> = {
  normal: "max-w-2xl",
  wide: "max-w-4xl",
  full: "max-w-none",
};

interface LessonWidthContextValue {
  lessonWidth: LessonWidth;
  lessonWidthClass: string;
  setLessonWidth: (width: LessonWidth) => void;
}

const DEFAULT_VALUE: LessonWidthContextValue = {
  lessonWidth: "normal",
  lessonWidthClass: LESSON_WIDTH_CLASS.normal,
  setLessonWidth: () => undefined,
};

const LessonWidthContext = createContext<LessonWidthContextValue>(DEFAULT_VALUE);

function readStored(): LessonWidth {
  try {
    const v = localStorage.getItem(STORAGE_KEY);
    if (v === "normal" || v === "wide" || v === "full") return v;
  } catch {
    /* ignore */
  }
  return "normal";
}

export function LessonWidthProvider({ children }: { children: ReactNode }) {
  const [lessonWidth, setLessonWidth] = useState<LessonWidth>(() => readStored());

  useEffect(() => {
    try {
      localStorage.setItem(STORAGE_KEY, lessonWidth);
    } catch {
      /* ignore */
    }
  }, [lessonWidth]);

  const value = useMemo<LessonWidthContextValue>(
    () => ({
      lessonWidth,
      lessonWidthClass: LESSON_WIDTH_CLASS[lessonWidth],
      setLessonWidth,
    }),
    [lessonWidth],
  );

  return <LessonWidthContext.Provider value={value}>{children}</LessonWidthContext.Provider>;
}

export function useLessonWidth(): LessonWidthContextValue {
  return useContext(LessonWidthContext);
}
