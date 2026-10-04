import { useEffect } from "react";
import { useLocation } from "react-router-dom";
import { useTranslation } from "react-i18next";
import { Card, Spinner } from "@/components/ui/primitives";
import { CourseSummary } from "@/features/courses/CourseSummary";
import { useCatalogue, useMyCourses, useSaveMyCourses } from "@/features/courses/useCourses";

export const COURSES_SECTION_ID = "courses";

/**
 * Settings → Courses (R5.1): every published course, alphabetical, each with its switch. Turning one
 * off hides it everywhere and deletes nothing; turning it back on brings back everything it had.
 */
export function CourseSettings() {
  const { t } = useTranslation();
  const { hash } = useLocation();
  const { data: catalogue } = useCatalogue();
  const { data: mine } = useMyCourses();
  const save = useSaveMyCourses();

  // The "no course" pages link here; the section mounts after its data, so the browser's own jump
  // to the fragment has already given up by then.
  const ready = catalogue !== undefined && mine !== undefined;
  useEffect(() => {
    if (ready && hash === `#${COURSES_SECTION_ID}`) {
      document.getElementById(COURSES_SECTION_ID)?.scrollIntoView({ block: "start" });
    }
  }, [ready, hash]);

  const toggle = (slug: string, on: boolean) => {
    if (!mine) return;
    const active = on ? [...mine.active, slug] : mine.active.filter((entry) => entry !== slug);
    save.mutate({ active, selected: mine.selected });
  };

  return (
    <Card id={COURSES_SECTION_ID} className="scroll-mt-4 space-y-3 p-4">
      <h2 className="font-semibold">{t("courses.settingsTitle")}</h2>
      {!ready ? (
        <Spinner />
      ) : (
        <ul className="space-y-3">
          {catalogue.map((course) => {
            const on = mine.active.includes(course.slug);
            return (
              <li key={course.slug}>
                <label className="flex cursor-pointer items-start justify-between gap-4">
                  <CourseSummary course={course} />
                  <input
                    type="checkbox"
                    role="switch"
                    aria-checked={on}
                    checked={on}
                    disabled={save.isPending}
                    onChange={(event) => toggle(course.slug, event.target.checked)}
                    className="mt-1 h-4 w-4 shrink-0 accent-primary"
                  />
                </label>
              </li>
            );
          })}
        </ul>
      )}
    </Card>
  );
}
