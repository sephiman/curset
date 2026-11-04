import { Link } from "react-router-dom";
import { useTranslation } from "react-i18next";
import { useNavItems } from "@/features/courses/useNavItems";
import { cn } from "@/lib/cn";

/** The four main sections as header tabs at 768 px and up (K1); the current one carries an underline. */
export function HeaderTabs() {
  const { t } = useTranslation();
  const navItems = useNavItems();
  return (
    <nav aria-label={t("nav.sections")} className="flex h-full items-stretch">
      <ul className="flex items-stretch gap-1">
        {navItems.map(({ tab, to, labelKey, current }) => (
          <li key={tab} className="flex">
            <Link
              to={to}
              aria-current={current ? "page" : undefined}
              className={cn(
                // -mb-px lays the underline over the header's own bottom rule.
                "-mb-px flex items-center border-b-2 px-3 text-sm transition-colors focus:outline-none focus-visible:ring-2 focus-visible:ring-inset focus-visible:ring-primary",
                current
                  ? "border-primary font-semibold text-primary"
                  : "border-transparent text-gray-600 hover:border-gray-300 hover:text-gray-900 dark:text-gray-300 dark:hover:border-gray-600 dark:hover:text-gray-100 oled:hover:border-oled-line-strong",
              )}
            >
              {t(labelKey)}
            </Link>
          </li>
        ))}
      </ul>
    </nav>
  );
}
