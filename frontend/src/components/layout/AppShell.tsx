import { type ReactNode } from "react";
import { Link, useLocation } from "react-router-dom";
import { useTranslation } from "react-i18next";
import { useAuth } from "@/auth/AuthContext";
import { AccountMenu } from "@/components/layout/AccountMenu";
import { Logo } from "@/components/layout/Logo";
import {
  HeaderChromeProvider,
  useHeaderBackTarget,
  useIsFocusMode,
  type HeaderBack,
} from "@/components/layout/headerChrome";
import { HeaderTabs } from "@/components/layout/HeaderTabs";
import { HOME_PATH, isLessonPath, isLessonReadingPath } from "@/components/layout/nav";
import { PhoneHeader } from "@/components/layout/PhoneHeader";
import { TabBar } from "@/components/layout/TabBar";
import { CourseSwitcher } from "@/features/courses/CourseSwitcher";
import { useNavItems } from "@/features/courses/useNavItems";
import { cn } from "@/lib/cn";
import { useLessonWidth, type LessonWidth } from "@/lib/lessonWidth";
import { useCompactLayout, usePhoneLayout } from "@/lib/viewport";

export function AppShell({ children }: { children: ReactNode }) {
  return (
    <HeaderChromeProvider>
      <Shell>{children}</Shell>
    </HeaderChromeProvider>
  );
}

function Shell({ children }: { children: ReactNode }) {
  const { t } = useTranslation();
  const { user } = useAuth();
  const { pathname } = useLocation();
  const { lessonWidth } = useLessonWidth();
  const navItems = useNavItems();
  const phone = usePhoneLayout();
  const focused = useIsFocusMode();
  // Home is the Course tab: the selected course's root, or the "no course" page when there is none.
  const home = navItems.find((item) => item.tab === "course")?.to ?? HOME_PATH;
  const compact = useCompactLayout();
  const back = useHeaderBackTarget();
  const width = shellWidth(pathname, lessonWidth, compact);

  if (phone) {
    return (
      <div className="flex min-h-full flex-col">
        <PhoneHeader home={home} user={user} />
        {/* Clear of the fixed tab bar (3.5 rem plus the home-indicator inset); in focus mode the page owns the bottom. */}
        <main className={cn("w-full flex-1 px-4 pt-3", focused ? "pb-6" : "pb-[calc(5rem+env(safe-area-inset-bottom))]")}>
          {children}
        </main>
        {user && !focused && <TabBar />}
      </div>
    );
  }

  return (
    <div className="flex min-h-full flex-col">
      {/* In OLED the header no longer sits a shade above the page, so its bottom rule is the only
          thing dividing chrome from content — it steps up with the rest of the seams. */}
      <header className="border-b border-border bg-white dark:border-gray-800 dark:bg-gray-900 oled:border-oled-line oled:bg-oled-bg">
        {/* K1: mark, course selector, the four tabs; the lesson's back link and the avatar at the right. */}
        {/* One width on every page, so the mark never moves; only the page below widens. */}
        <div className="mx-auto flex h-14 max-w-5xl items-center gap-4 px-4">
          {/* The wordmark is the way back to the start from anywhere. A plain `Link`, deliberately
              with no `replace` prop: react-router replaces only when the target already IS the
              current location, so clicking it on the course page adds no history entry while
              clicking it on a lesson leaves that lesson for Back to return to. The accessible name
              keeps the name the logo shows ("Curset — home"), which is what lets someone driving by
              voice say what they can read; the image itself is then decorative. */}
          <Link
            to={home}
            aria-label={t("nav.homeLabel", { name: t("app.name") })}
            className="inline-flex shrink-0 rounded-md transition-opacity hover:opacity-90 focus:outline-none focus:ring-2 focus:ring-primary focus:ring-offset-1 dark:focus:ring-offset-gray-900 oled:focus:ring-offset-oled-bg"
          >
            <Logo decorative />
          </Link>
          {user && <CourseSwitcher className="max-w-[16rem] min-w-0 shrink" />}
          {user && <HeaderTabs />}
          <div className="ml-auto flex min-w-0 items-center gap-4">
            {back && <HeaderBackLink back={back} />}
            {user && <AccountMenu user={user} />}
          </div>
        </div>
      </header>
      <main className={cn("mx-auto w-full flex-1 px-4 py-6", width)}>{children}</main>
    </div>
  );
}

/** A lesson's «← module» and reading time, in the header bar at 1024 px and up (K2). */
function HeaderBackLink({ back }: { back: HeaderBack }) {
  return (
    <div className="flex min-w-0 items-baseline gap-2 text-sm">
      <Link to={back.to} className="truncate text-primary hover:underline">
        ← {back.label}
      </Link>
      {back.note && <span className="shrink-0 text-xs text-gray-500 dark:text-gray-400">{back.note}</span>}
    </div>
  );
}

/** The page's column: the reader's full width, the lesson with its index, or the default the header also uses. */
function shellWidth(pathname: string, lessonWidth: LessonWidth, compact: boolean): string {
  if (isLessonPath(pathname) && lessonWidth === "full") return "max-w-none";
  if (!compact && isLessonReadingPath(pathname)) return "max-w-7xl";
  return "max-w-5xl";
}
