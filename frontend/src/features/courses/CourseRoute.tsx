import { useEffect, useRef, type ReactNode } from "react";
import { Navigate, Route, Routes, useLocation, useParams } from "react-router-dom";
import { useTranslation } from "react-i18next";
import type { CatalogueCourse } from "@/api/courses";
import { coursePath, tabOf } from "@/components/layout/nav";
import { Button, Spinner } from "@/components/ui/primitives";
import { CourseProvider } from "@/features/courses/CourseContext";
import { CourseHeader } from "@/features/courses/CourseHeader";
import { NoCoursePage } from "@/features/courses/NoCoursePage";
import { useCatalogue, useMyCourses, useSaveMyCourses } from "@/features/courses/useCourses";

/** Why a course URL shows no course: it does not exist, or it is not active (with a way to enable it). */
function Unavailable({ slug, course, onEnable }: { slug: string; course?: CatalogueCourse; onEnable: () => void }) {
  const { t } = useTranslation();
  if (!course) {
    return <p role="status">{t("courses.unknown", { slug })}</p>;
  }
  return (
    <div role="status" className="space-y-2">
      <p>{t("courses.disabled", { title: course.title })}</p>
      <Button variant="secondary" onClick={onEnable}>
        {t("courses.enableIt")}
      </Button>
    </div>
  );
}

/**
 * `/courses/:course/*`. The slug is checked against the catalogue and the user's active courses;
 * entering an active course by URL selects it (R6.6), and the pages below read it from context.
 */
export function CourseRoute({ children }: { children: ReactNode }) {
  const { course: slug = "" } = useParams();
  const { pathname } = useLocation();
  const catalogue = useCatalogue();
  const mine = useMyCourses();
  const save = useSaveMyCourses();

  const course = catalogue.data?.find((entry) => entry.slug === slug);
  const active = mine.data?.active.includes(slug) ?? false;
  const mustSelect = course !== undefined && active && mine.data?.selected !== slug;

  // Once per slug: a failed save must not turn into a request loop.
  const selectedOnce = useRef<string | null>(null);
  useEffect(() => {
    if (!mustSelect || !mine.data || selectedOnce.current === slug) return;
    selectedOnce.current = slug;
    save.mutate({ active: mine.data.active, selected: slug });
  }, [mustSelect, mine.data, save, slug]);

  if (!catalogue.data || !mine.data) {
    return (
      <div className="flex justify-center py-16 text-gray-500">
        <Spinner />
      </div>
    );
  }
  if (!course || !active) {
    const enable = () => save.mutate({ active: [...mine.data.active, slug], selected: slug });
    return (
      <NoCoursePage tab={tabOf(pathname)} notice={<Unavailable slug={slug} course={course} onEnable={enable} />} />
    );
  }

  const lang = mine.data.readingLanguages[slug] ?? course.languages[0];
  return (
    <CourseProvider course={course} scope={{ slug, lang }}>
      <CourseHeader />
      {children}
    </CourseProvider>
  );
}

/** The pages under a course, relative to `/courses/:course`. */
export function CourseRoutes({ pages }: { pages: { path: string; element: ReactNode }[] }) {
  const { course: slug = "" } = useParams();
  return (
    <CourseRoute>
      <Routes>
        {pages.map(({ path, element }) => (
          <Route key={path} path={path} element={element} />
        ))}
        <Route path="*" element={<Navigate to={coursePath(slug)} replace />} />
      </Routes>
    </CourseRoute>
  );
}
