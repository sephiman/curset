import { useTranslation } from "react-i18next";
import { Spinner } from "@/components/ui/primitives";
import { CourseSummary } from "@/features/courses/CourseSummary";
import { useCatalogue } from "@/features/courses/useCourses";

/** The sign-up question (R5.4): which courses interest you. Nothing is ticked; none is an answer. */
export function CourseChoices({ chosen, onChange }: { chosen: string[]; onChange: (chosen: string[]) => void }) {
  const { t } = useTranslation();
  const { data: catalogue } = useCatalogue();
  if (!catalogue) return <Spinner />;
  return (
    <fieldset className="space-y-3">
      <legend className="text-sm font-medium">{t("courses.signupQuestion")}</legend>
      <p className="text-xs text-gray-500 dark:text-gray-400">{t("courses.signupHint")}</p>
      {catalogue.map((course) => (
        <label key={course.slug} className="flex cursor-pointer items-start gap-3">
          <input
            type="checkbox"
            checked={chosen.includes(course.slug)}
            onChange={(event) =>
              onChange(
                event.target.checked ? [...chosen, course.slug] : chosen.filter((slug) => slug !== course.slug),
              )
            }
            className="mt-1 h-4 w-4 shrink-0 accent-primary"
          />
          <CourseSummary course={course} />
        </label>
      ))}
    </fieldset>
  );
}
