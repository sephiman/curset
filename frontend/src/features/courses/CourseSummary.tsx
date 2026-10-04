import { useTranslation } from "react-i18next";
import type { CatalogueCourse } from "@/api/courses";
import { availability } from "@/features/courses/languages";
import { useInterfaceLocale } from "@/i18n/locale";

/** Title, summary and languages of a course — the same three lines in settings and at sign-up. */
export function CourseSummary({ course }: { course: CatalogueCourse }) {
  const { t } = useTranslation();
  const interfaceLocale = useInterfaceLocale();
  return (
    <span className="block min-w-0">
      <span className="block font-medium" lang={course.textLocale}>
        {course.title}
      </span>
      <span className="block text-sm text-gray-500 dark:text-gray-400" lang={course.textLocale}>
        {course.description}
      </span>
      <span className="block text-xs text-gray-500 dark:text-gray-400">
        {availability(course.languages, interfaceLocale, t)}
      </span>
    </span>
  );
}
