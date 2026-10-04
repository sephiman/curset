import { useLocation } from "react-router-dom";
import { TABS, tabOf, tabPath, type Tab } from "@/components/layout/nav";
import { useMyCourses } from "@/features/courses/useCourses";

export interface NavItem {
  tab: Tab;
  to: string;
  labelKey: string;
  current: boolean;
}

/** The four tabs, pointing at the selected course — or at their "no course" pages when there is none. */
export function useNavItems(): NavItem[] {
  const { pathname } = useLocation();
  const { data: mine } = useMyCourses();
  const selected = mine?.selected ?? null;
  // On a course page the URL names the course; elsewhere (Settings) the selection does.
  const onCourse = pathname.match(/^\/courses\/([^/]+)/)?.[1] ?? null;
  const course = onCourse && mine?.active.includes(onCourse) ? onCourse : selected;
  const currentTab = pathname === "/account" ? null : tabOf(pathname);
  return TABS.map(({ tab, labelKey }) => ({
    tab,
    labelKey,
    to: tabPath(tab, course),
    current: tab === currentTab,
  }));
}
