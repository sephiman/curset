import { Navigate, useLocation } from "react-router-dom";
import { coursePath, type Tab } from "@/components/layout/nav";
import { Spinner } from "@/components/ui/primitives";
import { NoCoursePage } from "@/features/courses/NoCoursePage";
import { useMyCourses } from "@/features/courses/useCourses";

/**
 * A course-less address (`/`, `/course`, `/glossary`, an old `/lessons/…` bookmark): the same page
 * under the selected course, or the tab's "no course" page when no course is active.
 */
export function SelectedCourseRedirect({ tab }: { tab: Tab }) {
  const { pathname, search, hash } = useLocation();
  const { data: mine, isLoading } = useMyCourses();
  if (isLoading || !mine) {
    return (
      <div className="flex justify-center py-16 text-gray-500">
        <Spinner />
      </div>
    );
  }
  if (!mine.selected) return <NoCoursePage tab={tab} />;
  const rest = pathname === "/" || pathname === "/course" ? "" : pathname;
  return <Navigate to={`${coursePath(mine.selected, rest)}${search}${hash}`} replace />;
}
