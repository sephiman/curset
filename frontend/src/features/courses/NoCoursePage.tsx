import type { ReactNode } from "react";
import { Link } from "react-router-dom";
import { useTranslation } from "react-i18next";
import type { Tab } from "@/components/layout/nav";

export const COURSE_SETTINGS_PATH = "/account#courses";

const BUTTON =
  "inline-flex items-center justify-center rounded-md bg-primary px-4 py-2 text-sm font-medium text-primary-foreground transition-colors hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-primary focus:ring-offset-1 dark:focus:ring-offset-gray-900 oled:focus:ring-offset-oled-bg";

/** A tab with no course behind it: one sentence, one line for this tab, one button (R7). */
export function NoCoursePage({ tab, notice }: { tab: Tab; notice?: ReactNode }) {
  const { t } = useTranslation();
  return (
    <section className="mx-auto max-w-md space-y-3 py-12 text-center">
      {notice}
      <h1 className="text-lg font-semibold">{t("noCourse.lead")}</h1>
      <p className="text-sm text-gray-500 dark:text-gray-400">{t(`noCourse.${tab}`)}</p>
      <Link to={COURSE_SETTINGS_PATH} className={BUTTON}>
        {t("noCourse.action")}
      </Link>
    </section>
  );
}
