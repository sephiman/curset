import { useLocation, useNavigate } from "react-router-dom";
import { useTranslation } from "react-i18next";
import type { Locale } from "@/api/auth";
import { Segmented } from "@/components/layout/controls";
import { coursePath, tabOf } from "@/components/layout/nav";
import { Select } from "@/components/ui/primitives";
import { useCourse } from "@/features/courses/CourseContext";
import { availability } from "@/features/courses/languages";
import { useCatalogue, useChooseReadingLanguage, useMyCourses } from "@/features/courses/useCourses";
import { useInterfaceLocale } from "@/i18n/locale";

/**
 * Which course is on screen, which languages it exists in and, when it has several, which one it is
 * read in. The course dropdown belongs to the Course and Exams tabs; Glossary and Progress follow it.
 */
export function CourseHeader() {
  const { t } = useTranslation();
  const navigate = useNavigate();
  const { pathname } = useLocation();
  const interfaceLocale = useInterfaceLocale();
  const { course, scope } = useCourse();
  const { data: catalogue = [] } = useCatalogue();
  const { data: mine } = useMyCourses();
  const chooseReadingLanguage = useChooseReadingLanguage();

  const tab = tabOf(pathname);
  const active = catalogue.filter((entry) => mine?.active.includes(entry.slug));
  const showDropdown = (tab === "course" || tab === "exams") && active.length > 1;

  return (
    <div className="mb-6 flex flex-wrap items-center justify-between gap-x-4 gap-y-2 border-b border-border pb-3 text-sm dark:border-gray-800 oled:border-oled-line">
      <div className="flex min-w-0 flex-wrap items-center gap-x-3 gap-y-1">
        {showDropdown ? (
          <Select
            aria-label={t("courses.selectorLabel")}
            value={course.slug}
            onChange={(event) => navigate(coursePath(event.target.value, tab === "exams" ? "/exams" : ""))}
            className="w-auto max-w-full"
          >
            {active.map((entry) => (
              <option key={entry.slug} value={entry.slug} lang={entry.textLocale}>
                {entry.title}
              </option>
            ))}
          </Select>
        ) : (
          <span className="truncate font-medium" lang={course.textLocale}>
            {course.title}
          </span>
        )}
        <span className="text-xs text-gray-500 dark:text-gray-400">
          {availability(course.languages, interfaceLocale, t)}
        </span>
      </div>
      {course.languages.length > 1 && (
        <div className="flex items-center gap-2">
          <span className="text-xs text-gray-500 dark:text-gray-400">{t("courses.readingLanguage")}</span>
          <Segmented<Locale>
            ariaLabel={t("courses.readingLanguage")}
            value={scope.lang}
            onChange={(lang) => chooseReadingLanguage(course.slug, lang)}
            options={course.languages.map((lang) => ({ value: lang, label: lang.toUpperCase() }))}
          />
        </div>
      )}
    </div>
  );
}
