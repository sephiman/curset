/**
 * Page URLs are course-scoped, mirroring the API: `/courses/{course}/…`, so the address bar always
 * says which course is on screen. Each tab also has a course-less address (`/course`, `/glossary`, …):
 * it forwards to the selected course, or shows the tab's "no course" page when none is active.
 */

export type Tab = "course" | "glossary" | "exams" | "progress";

/** The primary navigation, in canonical order — header tabs at 768 px and up, the bottom tab bar below. */
export const TABS: readonly { tab: Tab; rest: string; labelKey: string }[] = [
  { tab: "course", rest: "", labelKey: "nav.course" },
  { tab: "glossary", rest: "/glossary", labelKey: "nav.glossary" },
  { tab: "exams", rest: "/exams", labelKey: "nav.exams" },
  { tab: "progress", rest: "/stats", labelKey: "nav.progress" },
];

/** Where "home" is: the wordmark and the bare root resolve it to the selected course. */
export const HOME_PATH = "/";

export function coursePath(slug: string, rest = ""): string {
  return `/courses/${slug}${rest}`;
}

/** A tab's address: under the selected course, or its course-less one when no course is active. */
export function tabPath(tab: Tab, selected: string | null): string {
  const { rest } = TABS.find((entry) => entry.tab === tab) ?? TABS[0];
  return selected ? coursePath(selected, rest) : rest || "/course";
}

/** Which tab a page belongs to; modules and lessons are the Course tab. */
export function tabOf(pathname: string): Tab {
  const rest = pathname.replace(/^\/courses\/[^/]+/, "");
  if (rest.startsWith("/glossary")) return "glossary";
  if (rest.startsWith("/exams")) return "exams";
  if (rest.startsWith("/stats")) return "progress";
  return "course";
}

/** True on a lesson or its practice page, where the reader's width preference applies. */
export function isLessonPath(pathname: string): boolean {
  const rest = pathname.replace(/^\/courses\/[^/]+/, "");
  return rest.startsWith("/lessons/");
}

/** True on a lesson's reading page (not its practice), which widens to fit the side index (K2). */
export function isLessonReadingPath(pathname: string): boolean {
  const rest = pathname.replace(/^\/courses\/[^/]+/, "");
  return /^\/lessons\/[^/]+\/?$/.test(rest);
}
