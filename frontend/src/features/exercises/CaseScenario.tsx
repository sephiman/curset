import { useId } from "react";
import { useTranslation } from "react-i18next";
import { Prose } from "@/lib/markdown";

/**
 * A case's scenario, kept in view while its questions are answered: sticky at the top of the column on
 * a wide screen, and a collapsible panel on a phone, where a page of text would push every question
 * off the screen. In an exam it carries the «grade this case» mark.
 */
export function CaseScenario({
  title,
  scenario,
  choice,
}: {
  title: string;
  scenario: string;
  choice?: { label: string; rule: string; checked: boolean; onChange: (checked: boolean) => void };
}) {
  const { t } = useTranslation();
  const markId = useId();
  return (
    <details
      open
      className="group z-10 rounded-lg border border-border bg-white p-4 shadow-sm md:sticky md:top-2 md:max-h-[45vh] md:overflow-y-auto dark:border-gray-800 dark:bg-gray-900 oled:border-oled-line oled:bg-oled-bg"
    >
      <summary className="cursor-pointer list-none text-sm font-semibold">
        <span className="text-xs font-medium tracking-wide text-gray-500 uppercase dark:text-gray-400">
          {t("exam.scenario")}
        </span>{" "}
        · {title}
        <span className="ml-2 text-xs font-normal text-primary group-open:hidden">{t("exam.showScenario")}</span>
      </summary>
      <div className="mt-2 text-sm">
        <Prose markdown={scenario} />
      </div>
      {choice && (
        <div className="mt-3 border-t border-border pt-3 dark:border-gray-800 oled:border-oled-line">
          <label htmlFor={markId} className="flex items-center gap-2 text-sm font-medium">
            <input
              id={markId}
              type="checkbox"
              checked={choice.checked}
              onChange={(event) => choice.onChange(event.target.checked)}
            />
            {choice.label}
          </label>
          <p className="mt-1 text-xs text-gray-500 dark:text-gray-400">{choice.rule}</p>
        </div>
      )}
    </details>
  );
}
