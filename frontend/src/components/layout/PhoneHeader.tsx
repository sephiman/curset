import { Link } from "react-router-dom";
import { useTranslation } from "react-i18next";
import type { Me } from "@/api/auth";
import { AccountMenu } from "@/components/layout/AccountMenu";
import { useHeaderBackTarget } from "@/components/layout/headerChrome";
import { LogoMark } from "@/components/layout/Logo";
import { CourseSwitcher } from "@/features/courses/CourseSwitcher";

const FOCUS_RING = "focus:outline-none focus-visible:ring-2 focus-visible:ring-primary";

/** J2: one line — mark (or the page's back arrow), the course as a compact selector, the avatar. */
export function PhoneHeader({ home, user }: { home: string; user: Me | null }) {
  const { t } = useTranslation();
  const back = useHeaderBackTarget();
  return (
    <header className="bg-white dark:bg-gray-900 oled:bg-oled-bg">
      <div className="flex h-14 items-center gap-2 px-3">
        {back ? (
          <Link
            to={back.to}
            aria-label={t("nav.backTo", { label: back.label })}
            className={`-ml-1 inline-flex h-11 w-11 shrink-0 items-center justify-center rounded-md text-xl text-primary ${FOCUS_RING}`}
          >
            <span aria-hidden="true">←</span>
          </Link>
        ) : (
          <Link to={home} aria-label={t("nav.homeLabel", { name: t("app.name") })} className={`flex h-11 shrink-0 items-center rounded-md ${FOCUS_RING}`}>
            <LogoMark />
          </Link>
        )}
        <div className="flex min-w-0 flex-1 justify-center">{user && <CourseSwitcher className="flex-1" />}</div>
        <div className="shrink-0">{user && <AccountMenu user={user} />}</div>
      </div>
    </header>
  );
}
