import type { ReactNode } from "react";
import { Link } from "react-router-dom";
import { useTranslation } from "react-i18next";
import type { Tab } from "@/components/layout/nav";
import { useNavItems } from "@/features/courses/useNavItems";
import { cn } from "@/lib/cn";

const ICON_PATHS: Record<Tab, ReactNode> = {
  course: <path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20V3H6.5A2.5 2.5 0 0 0 4 5.5zM4 19.5A2.5 2.5 0 0 0 6.5 22H20v-5" />,
  glossary: <path d="M4 19 9 5l5 14M5.8 14h6.4M15 19h5M15 15h5M15 11h5" />,
  exams: <path d="M9 4h6v3H9zM7 5H5v16h14V5h-2M8.5 12l2 2 4-4M8.5 17.5h7" />,
  progress: <path d="M4 20V10M10 20V4M16 20v-7M22 20H2" />,
};

/** The four main sections as a fixed bottom bar on a phone (J1); the header keeps them above 768 px. */
export function TabBar() {
  const { t } = useTranslation();
  const navItems = useNavItems();
  return (
    <nav
      aria-label={t("nav.sections")}
      className="fixed inset-x-0 bottom-0 z-40 border-t border-border bg-white pb-[env(safe-area-inset-bottom)] dark:border-gray-800 dark:bg-gray-900 oled:border-oled-line oled:bg-oled-bg"
    >
      <ul className="mx-auto flex h-14 max-w-md items-stretch">
        {navItems.map(({ tab, to, labelKey, current }) => (
          <li key={tab} className="flex-1">
            <Link
              to={to}
              aria-current={current ? "page" : undefined}
              className={cn(
                "flex h-full flex-col items-center justify-center gap-0.5 text-[11px] font-medium focus:outline-none focus-visible:ring-2 focus-visible:ring-inset focus-visible:ring-primary",
                current ? "text-primary" : "text-gray-500 dark:text-gray-400",
              )}
            >
              <svg
                aria-hidden="true"
                width="22"
                height="22"
                viewBox="0 0 24 24"
                fill="none"
                stroke="currentColor"
                strokeWidth={current ? 2.2 : 1.8}
                strokeLinecap="round"
                strokeLinejoin="round"
              >
                {ICON_PATHS[tab]}
              </svg>
              {t(labelKey)}
            </Link>
          </li>
        ))}
      </ul>
    </nav>
  );
}
