import type { ReactNode } from "react";
import type { TFunction } from "i18next";
import { useTranslation } from "react-i18next";
import type { OptionView } from "@/api/exercises";
import { useCourseTree } from "@/features/course/queries";
import { cn } from "@/lib/cn";
import { Prose } from "@/lib/markdown";

function isObj(value: unknown): value is Record<string, unknown> {
  return typeof value === "object" && value !== null;
}

function asStringArray(value: unknown): string[] | null {
  return Array.isArray(value) ? value.map((x) => String(x)) : null;
}

/** Narrow `correctAnswer`'s several server shapes and render each readably, never as raw ids. */
function renderCorrectAnswer(value: unknown, t: TFunction): ReactNode {
  if (value == null) return null;
  if (typeof value === "string") return value;
  if (!isObj(value)) return String(value);

  // matching — { pairs, readable: [{left, right}] }
  if (Array.isArray(value.readable)) {
    return (
      <ul className="mt-1 space-y-0.5">
        {value.readable.map((entry, i) => {
          const pair = isObj(entry) ? entry : {};
          return (
            <li key={i} className="flex flex-wrap items-center gap-1">
              <span>{String(pair.left ?? "")}</span>
              <span className="text-gray-400">→</span>
              <span className="font-medium">{String(pair.right ?? "")}</span>
            </li>
          );
        })}
      </ul>
    );
  }

  const texts = asStringArray(value.texts);
  // ordering — { order, texts }: sequence matters, render numbered.
  if (texts && "order" in value) {
    return (
      <ol className="mt-1 list-decimal space-y-0.5 pl-5">
        {texts.map((text, i) => (
          <li key={i}>{text}</li>
        ))}
      </ol>
    );
  }
  // multi_select — { optionIds, texts }
  if (texts) {
    return (
      <ul className="mt-1 list-disc space-y-0.5 pl-5">
        {texts.map((text, i) => (
          <li key={i}>{text}</li>
        ))}
      </ul>
    );
  }

  // single_choice / chart — { text } (and { optionId })
  if (typeof value.text === "string") return value.text;
  // true_false — { value: boolean }
  if (typeof value.value === "boolean") return value.value ? t("exercise.true") : t("exercise.false");
  // calculation — { optionId, value }
  if (value.value != null) return String(value.value);

  return null;
}

export function Verdict({ correct }: { correct: boolean }) {
  const { t } = useTranslation();
  return (
    <div
      className={cn(
        "rounded-md px-3 py-2 text-sm font-medium",
        correct
          ? "bg-emerald-100 text-emerald-800 dark:bg-emerald-950/50 dark:text-emerald-200"
          : "bg-red-100 text-red-800 dark:bg-red-950/50 dark:text-red-200",
      )}
    >
      {correct ? t("exercise.correct") : t("exercise.incorrect")}
    </div>
  );
}

/** The correct answer, the worked steps and the explanation, in that order. */
export function SolutionBody({
  correctAnswer,
  solutionSteps,
  explanation,
  options,
}: {
  correctAnswer: unknown;
  solutionSteps: string[];
  explanation: string | null;
  options?: OptionView[];
}) {
  const { t } = useTranslation();
  const { data: courseTree } = useCourseTree();
  const letters = courseTree?.course.optionLabels === "letters";

  const correctId =
    typeof correctAnswer === "object" && correctAnswer !== null && "optionId" in correctAnswer
      ? String((correctAnswer as { optionId: unknown }).optionId)
      : null;
  const optIndex =
    options && correctId != null ? options.findIndex((o) => o.id === correctId) : -1;
  const correctLetter = optIndex >= 0 ? String.fromCharCode(65 + optIndex) : null;

  const answer = renderCorrectAnswer(correctAnswer, t);
  return (
    <>
      {answer != null && (
        <div className="text-sm text-gray-700 dark:text-gray-300">
          {letters && correctLetter ? (
            <div>
              <p className="font-semibold text-emerald-700 dark:text-emerald-400">
                {t("exercise.correctOption", { letter: correctLetter })}
              </p>
              {options && options.length > 0 ? (
                <div className="mt-2 space-y-1">
                  {options.map((opt, idx) => {
                    const isCorrect = opt.id === correctId;
                    return (
                      <div
                        key={opt.id}
                        className={cn(
                          "flex items-start gap-2 rounded-md border p-2 text-sm",
                          isCorrect
                            ? "border-emerald-500 bg-emerald-50 font-medium text-emerald-950 dark:border-emerald-700 dark:bg-emerald-950/40 dark:text-emerald-100"
                            : "border-border text-gray-600 dark:border-gray-800 dark:text-gray-400 opacity-75",
                        )}
                      >
                        <span className="font-semibold">{String.fromCharCode(65 + idx)})</span>
                        <span>{opt.text}</span>
                        {isCorrect && (
                          <span className="ml-auto font-bold text-emerald-600 dark:text-emerald-400">✓</span>
                        )}
                      </div>
                    );
                  })}
                </div>
              ) : (
                typeof answer === "string" ? <span> · {answer}</span> : answer
              )}
            </div>
          ) : (
            <div>
              <span className="font-medium">{t("exercise.correctAnswer")}:</span>
              {typeof answer === "string" ? <span> {answer}</span> : answer}
            </div>
          )}
        </div>
      )}

      {solutionSteps.length > 0 && (
        <div>
          <p className="mb-1 text-xs font-semibold tracking-wide text-gray-500 uppercase dark:text-gray-400">
            {t("exercise.solution")}
          </p>
          <pre className="overflow-x-auto rounded-md bg-gray-100 p-3 font-mono text-xs leading-relaxed text-gray-800 dark:bg-gray-800 dark:text-gray-200 oled:bg-oled-bg oled:ring-1 oled:ring-oled-line">
            {solutionSteps.join("\n")}
          </pre>
        </div>
      )}

      {explanation && (
        <div className="text-sm text-gray-700 dark:text-gray-300">
          <Prose markdown={explanation} />
        </div>
      )}
    </>
  );
}

export function AttemptResult({
  correct,
  correctAnswer,
  solutionSteps,
  explanation,
  options,
  hideVerdict = false,
}: {
  correct: boolean;
  correctAnswer: unknown;
  solutionSteps: string[];
  explanation: string | null;
  options?: OptionView[];
  hideVerdict?: boolean;
}) {
  return (
    <div className="mt-4 space-y-3">
      {!hideVerdict && <Verdict correct={correct} />}
      <SolutionBody
        correctAnswer={correctAnswer}
        solutionSteps={solutionSteps}
        explanation={explanation}
        options={options}
      />
    </div>
  );
}
