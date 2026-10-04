import { useQuery } from "@tanstack/react-query";
import { getCourse, getGlossary } from "@/api/course";
import { scopeKey, useCourse } from "@/features/courses/CourseContext";

/** The course tree of the course on screen, in its reading language. */
export function useCourseTree() {
  const { scope } = useCourse();
  return useQuery({ queryKey: ["course", ...scopeKey(scope)], queryFn: () => getCourse(scope) });
}

/** The course's glossary in its reading language; cached for the session, it changes on deploy only. */
export function useCourseGlossary() {
  const { scope } = useCourse();
  return useQuery({
    queryKey: ["glossary", ...scopeKey(scope)],
    queryFn: () => getGlossary(scope),
    staleTime: Infinity,
  });
}
