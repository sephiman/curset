import { useCallback, useState } from "react";
import { useLocation, useNavigate } from "react-router-dom";
import { useTranslation } from "react-i18next";
import type { Locale } from "@/api/auth";
import { Segmented } from "@/components/layout/controls";
import { coursePath, tabOf } from "@/components/layout/nav";
import { Sheet } from "@/components/ui/Sheet";
import { availability } from "@/features/courses/languages";
import { useCatalogue, useChooseReadingLanguage, useMyCourses } from "@/features/courses/useCourses";
import { useInterfaceLocale } from "@/i18n/locale";
import { cn } from "@/lib/cn";

/** The header's course name: tapping it opens the course sheet with the languages and the reading-language choice (J2, K1). */
export function CourseSwitcher({ className }: { className?: string }) {
  const { t } = useTranslation();
  const navigate = useNavigate();
  const { pathname } = useLocation();
  const interfaceLocale = useInterfaceLocale();
  const { data: catalogue = [] } = useCatalogue();
  const { data: mine } = useMyCourses();
  const chooseReadingLanguage = useChooseReadingLanguage();
  const [open, setOpen] = useState(false);
  const close = useCallback(() => setOpen(false), []);

  const slug = pathname.match(/^\/courses\/([^/]+)/)?.[1];
  const course = catalogue.find((entry) => entry.slug === slug);
  if (!course || !mine) return null;

  const active = catalogue.filter((entry) => mine.active.includes(entry.slug));
  const lang = mine.readingLanguages[course.slug] ?? course.languages[0];
  const tab = tabOf(pathname);

  const choose = (next: string) => {
    close();
    if (next !== course.slug) navigate(coursePath(next, tab === "exams" ? "/exams" : ""));
  };

  return (
    <>
      <button
        type="button"
        aria-haspopup="dialog"
        aria-expanded={open}
        aria-label={t("courses.openSheet", { title: course.title })}
        onClick={() => setOpen(true)}
        className={cn(
          "flex h-11 min-w-0 items-center gap-1 rounded-md px-2 text-sm font-medium md:h-9 hover:bg-gray-100 focus:outline-none focus-visible:ring-2 focus-visible:ring-primary dark:hover:bg-gray-800 oled:hover:bg-oled-hover",
          className,
        )}
      >
        <span className="truncate" lang={course.textLocale}>
          {course.title}
        </span>
        <span aria-hidden="true" className="shrink-0 text-xs text-gray-500 dark:text-gray-400">
          ▾
        </span>
      </button>
      {open && (
        <Sheet title={t("courses.sheetTitle")} onClose={close}>
          <ul className="space-y-1">
            {active.map((entry) => {
              const current = entry.slug === course.slug;
              return (
                <li key={entry.slug}>
                  <button
                    type="button"
                    aria-current={current ? "true" : undefined}
                    onClick={() => choose(entry.slug)}
                    className={cn(
                      "w-full rounded-lg border px-3 py-2.5 text-left",
                      current
                        ? "border-primary bg-primary/10"
                        : "border-border hover:bg-gray-50 dark:border-gray-800 dark:hover:bg-gray-800 oled:border-oled-line oled:hover:bg-oled-hover",
                    )}
                  >
                    <span className="block text-sm font-medium" lang={entry.textLocale}>
                      {entry.title}
                    </span>
                    <span className="block text-xs text-gray-500 dark:text-gray-400">
                      {availability(entry.languages, interfaceLocale, t)}
                    </span>
                  </button>
                </li>
              );
            })}
          </ul>
          {course.languages.length > 1 && (
            <div className="mt-4 flex items-center justify-between gap-2">
              <span className="text-xs text-gray-500 dark:text-gray-400">{t("courses.readingLanguage")}</span>
              <Segmented<Locale>
                ariaLabel={t("courses.readingLanguage")}
                value={lang}
                onChange={(next) => chooseReadingLanguage(course.slug, next)}
                options={course.languages.map((value) => ({ value, label: value.toUpperCase() }))}
              />
            </div>
          )}
        </Sheet>
      )}
    </>
  );
}
