import { useQuery } from "@tanstack/react-query";
import { getCourse, getGlossary } from "@/api/course";
import { scopeKey, useCurrentCourse } from "@/features/courses/CourseContext";

/** The course tree of the course on screen, in its reading language. */
export function useCourseTree() {
  const current = useCurrentCourse();
  return useQuery({
    queryKey: current ? ["course", ...scopeKey(current.scope)] : ["course", "none"],
    queryFn: () => (current ? getCourse(current.scope) : Promise.reject(new Error("No current course"))),
    enabled: !!current,
  });
}

/** The course's glossary in its reading language; cached for the session, it changes on deploy only. */
export function useCourseGlossary() {
  const current = useCurrentCourse();
  return useQuery({
    queryKey: current ? ["glossary", ...scopeKey(current.scope)] : ["glossary", "none"],
    queryFn: () => (current ? getGlossary(current.scope) : Promise.reject(new Error("No current course"))),
    enabled: !!current,
    staleTime: Infinity,
  });
}
