import { useCallback, useEffect, useRef, useState } from "react";
import { useTranslation } from "react-i18next";
import type { Answer } from "@/api/exercises";
import type { ExamQuestion, ExamSession } from "@/api/exams";
import { Sheet } from "@/components/ui/Sheet";
import { cn } from "@/lib/cn";

interface NavigatorProps {
  exam: ExamSession;
  answers: Record<string, Answer>;
  current: number;
  disabled: boolean;
  onGo: (index: number) => void;
}

function QuestionChip({
  question,
  answered,
  current,
  disabled,
  onGo,
  chipRef,
  large,
}: {
  large: boolean;
  question: ExamQuestion;
  answered: boolean;
  current: boolean;
  disabled: boolean;
  onGo: (index: number) => void;
  chipRef?: (element: HTMLButtonElement | null) => void;
}) {
  const { t } = useTranslation();
  const number = question.index + 1;
  return (
    <button
      ref={chipRef}
      type="button"
      disabled={disabled}
      aria-label={question.reserve ? `${number} · ${t("exam.reserve")}` : `${number}`}
      aria-current={current}
      onClick={() => onGo(question.index)}
      className={cn(
        "shrink-0 rounded-md border px-1 font-medium tabular-nums transition-colors focus:outline-none focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-primary",
        large ? "h-11 min-w-11 text-sm" : "h-8 min-w-8 text-xs",
        current && "ring-2 ring-primary ring-offset-1 dark:ring-offset-gray-900 oled:ring-offset-oled-bg",
        question.reserve && "border-dashed",
        answered
          ? "border-primary bg-primary text-primary-foreground"
          : "border-border text-gray-600 hover:border-primary/60 dark:border-gray-700 dark:text-gray-300",
        disabled && "cursor-not-allowed opacity-50",
      )}
    >
      {question.reserve ? `R${number}` : number}
    </button>
  );
}

function partsWithQuestions(exam: ExamSession) {
  return exam.parts.map((part) => ({ part, questions: exam.questions.filter((q) => q.partId === part.id) }));
}

/** Every question as a wrapping grid, grouped by part; answered filled, current ringed, reserves dashed. */
export function QuestionGrid({ exam, answers, current, disabled, onGo, large = false }: NavigatorProps & { large?: boolean }) {
  const multiPart = exam.parts.length > 1;
  return (
    <>
      {partsWithQuestions(exam).map(({ part, questions }) => (
        <div key={part.id} className="space-y-1">
          {multiPart && <p className="text-xs font-medium text-gray-500 dark:text-gray-400">{part.title ?? part.id}</p>}
          <div className="flex flex-wrap gap-1.5">
            {questions.map((q) => (
              <QuestionChip
                large={large}
                key={q.attemptId}
                question={q}
                answered={answers[q.attemptId] !== undefined}
                current={q.index === current}
                disabled={disabled}
                onGo={onGo}
              />
            ))}
          </div>
        </div>
      ))}
    </>
  );
}

/**
 * The phone navigator (J3): one scrolling row of chips with the current one centred and each part's
 * label pinned at the left while its chips are in view; «Ir a…» opens the full grid as a sheet.
 */
export function QuestionChipStrip(props: NavigatorProps) {
  const { exam, answers, current, disabled, onGo } = props;
  const { t } = useTranslation();
  const strip = useRef<HTMLDivElement>(null);
  const chips = useRef(new Map<number, HTMLButtonElement>());
  const [gridOpen, setGridOpen] = useState(false);
  const closeGrid = useCallback(() => setGridOpen(false), []);
  const multiPart = exam.parts.length > 1;

  useEffect(() => {
    const container = strip.current;
    const chip = chips.current.get(current);
    if (!container || !chip) return;
    // Scrolls the strip only; scrollIntoView would also move the page under the sticky bar.
    container.scrollTo({ left: chip.offsetLeft - (container.clientWidth - chip.offsetWidth) / 2, behavior: "smooth" });
  }, [current]);

  const goFromGrid = (index: number) => {
    closeGrid();
    onGo(index);
  };

  return (
    <nav aria-label={t("exam.navigator")} className="flex items-center gap-2">
      <div ref={strip} className="relative flex min-w-0 flex-1 gap-3 overflow-x-auto py-1 [scrollbar-width:none]">
        {partsWithQuestions(exam).map(({ part, questions }) => (
          <div key={part.id} className="flex shrink-0 items-center gap-1.5">
            {multiPart && (
              <span className="sticky left-0 z-10 shrink-0 bg-gray-50 pr-1.5 text-[11px] font-semibold tracking-wide text-gray-500 uppercase dark:bg-gray-950 dark:text-gray-400 oled:bg-oled-bg">
                {part.title ?? part.id}
              </span>
            )}
            {questions.map((q) => (
              <QuestionChip
                large
                key={q.attemptId}
                question={q}
                answered={answers[q.attemptId] !== undefined}
                current={q.index === current}
                disabled={disabled}
                onGo={onGo}
                chipRef={(element) => {
                  if (element) chips.current.set(q.index, element);
                  else chips.current.delete(q.index);
                }}
              />
            ))}
          </div>
        ))}
      </div>
      <button
        type="button"
        aria-haspopup="dialog"
        disabled={disabled}
        onClick={() => setGridOpen(true)}
        className="h-11 shrink-0 rounded-md border border-border px-3 text-sm font-medium focus:outline-none focus-visible:ring-2 focus-visible:ring-primary text-gray-700 hover:bg-gray-100 disabled:opacity-50 dark:border-gray-700 dark:text-gray-200 dark:hover:bg-gray-800 oled:border-oled-line-strong oled:hover:bg-oled-hover"
      >
        {t("exam.goTo")}
      </button>
      {gridOpen && (
        <Sheet title={t("exam.questionsSheet")} onClose={closeGrid}>
          <div className="space-y-3">
            <QuestionGrid {...props} onGo={goFromGrid} large />
          </div>
        </Sheet>
      )}
    </nav>
  );
}
