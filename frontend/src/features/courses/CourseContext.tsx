import { createContext, useContext, type ReactNode } from "react";
import type { CourseScope } from "@/api/client";
import type { CatalogueCourse } from "@/api/courses";
import { coursePath } from "@/components/layout/nav";

export interface CurrentCourse {
  /** What every course-owned request needs: the slug and the reading language. */
  scope: CourseScope;
  course: CatalogueCourse;
  /** A page URL inside this course. */
  path: (rest?: string) => string;
}

const CourseContext = createContext<CurrentCourse | null>(null);

export function CourseProvider({
  course,
  scope,
  children,
}: {
  course: CatalogueCourse;
  scope: CourseScope;
  children: ReactNode;
}) {
  const value: CurrentCourse = { scope, course, path: (rest = "") => coursePath(course.slug, rest) };
  return <CourseContext.Provider value={value}>{children}</CourseContext.Provider>;
}

/** The course on screen. Every page under `/courses/:course` has one; anything else is a wiring bug. */
export function useCourse(): CurrentCourse {
  const current = useContext(CourseContext);
  if (!current) throw new Error("useCourse must be used inside a course route");
  return current;
}

/** Query-key prefix for course content: the course and the language it is read in. */
export function scopeKey(scope: CourseScope): [string, string] {
  return [scope.slug, scope.lang];
}
