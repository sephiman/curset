import { useEffect, useRef, useState } from "react";
import { useLocation, useNavigate } from "react-router-dom";
import { useTranslation } from "react-i18next";
import type { Me } from "@/api/auth";
import { useAuth } from "@/auth/AuthContext";
import { LanguageControl, LessonWidthControl, ThemeControl } from "@/components/layout/controls";
import { useHeaderActionTarget } from "@/components/layout/headerChrome";
import { usePhoneLayout } from "@/lib/viewport";
import { Button } from "@/components/ui/primitives";

function displayName(user: Me): string {
  return user.name?.trim() || user.email.split("@")[0] || user.email;
}

function initials(user: Me): string {
  return displayName(user).slice(0, 2).toUpperCase();
}

/** Account, language, theme, lesson width and sign-out behind an avatar button (SharedLedger pattern); the sections live in the tabs. */
export function AccountMenu({ user }: { user: Me }) {
  const { t } = useTranslation();
  const { logout } = useAuth();
  const navigate = useNavigate();
  const { pathname } = useLocation();
  const [open, setOpen] = useState(false);
  const ref = useRef<HTMLDivElement>(null);
  // On phones the page's own action (its PDF export) lives here rather than on the page.
  const pageAction = useHeaderActionTarget();
  const phone = usePhoneLayout();

  useEffect(() => {
    if (!open) return;
    function onDoc(e: MouseEvent) {
      if (ref.current && !ref.current.contains(e.target as Node)) setOpen(false);
    }
    function onKey(e: KeyboardEvent) {
      if (e.key === "Escape") setOpen(false);
    }
    document.addEventListener("mousedown", onDoc);
    document.addEventListener("keydown", onKey);
    return () => {
      document.removeEventListener("mousedown", onDoc);
      document.removeEventListener("keydown", onKey);
    };
  }, [open]);

  return (
    <div ref={ref} className="relative">
      <button
        type="button"
        aria-haspopup="menu"
        aria-expanded={open}
        aria-label={displayName(user)}
        onClick={() => setOpen((v) => !v)}
        className="flex h-9 w-9 max-md:h-11 max-md:w-11 items-center justify-center rounded-full bg-primary text-sm font-semibold text-primary-foreground transition-opacity hover:opacity-90 focus:outline-none focus:ring-2 focus:ring-primary focus:ring-offset-1 dark:focus:ring-offset-gray-900 oled:focus:ring-offset-oled-bg"
      >
        {initials(user)}
      </button>

      {/* The one floating panel in the app, and the case the OLED brief calls a modal: it is told
          apart from the page underneath by `shadow-lg` and a lighter fill, neither of which survives
          #000-on-#000. It gets the strong border — a menu overlapping content has to read as being
          *in front of* it, which a hairline seam does not do. */}
      {open && (
        <div
          role="menu"
          className="absolute right-0 z-50 mt-2 w-64 max-w-[calc(100vw-2rem)] rounded-lg border border-border bg-white p-3 shadow-lg dark:border-gray-800 dark:bg-gray-900 oled:border-oled-line-strong oled:bg-oled-bg"
        >
          {/* Who is signed in and the way to their account come first. */}
          <div className="mb-3 border-b border-border px-1 pb-3 dark:border-gray-800 oled:border-oled-line">
            <p className="text-xs text-gray-500 dark:text-gray-400">{t("auth.signedInAs")}</p>
            <p className="truncate font-semibold">{displayName(user)}</p>
            <p className="truncate text-xs text-gray-500 dark:text-gray-400">{user.email}</p>
            <Button
              role="menuitem"
              variant="secondary"
              aria-current={pathname === "/account" ? "page" : undefined}
              onClick={() => {
                setOpen(false);
                navigate("/account");
              }}
              className="mt-2 w-full"
            >
              {t("account.title")}
            </Button>
          </div>

          <div className="space-y-3">
            {phone && pageAction && (
              <Button
                role="menuitem"
                variant="secondary"
                onClick={() => {
                  setOpen(false);
                  pageAction.run();
                }}
                className="w-full"
              >
                {pageAction.label}
              </Button>
            )}
            <div>
              <p className="mb-1 px-1 text-xs text-gray-500 dark:text-gray-400">{t("common.language")}</p>
              <LanguageControl block />
            </div>

            <div>
              <p className="mb-1 px-1 text-xs text-gray-500 dark:text-gray-400">{t("common.theme")}</p>
              <ThemeControl block />
            </div>

            <div>
              <p className="mb-1 px-1 text-xs text-gray-500 dark:text-gray-400">{t("common.lessonWidth")}</p>
              <LessonWidthControl block />
            </div>

            <button
              type="button"
              role="menuitem"
              onClick={() => {
                setOpen(false);
                void logout();
              }}
              className="w-full rounded-md border border-border px-3 py-2 text-sm font-medium max-md:min-h-11 text-gray-700 transition-colors hover:bg-gray-100 dark:border-gray-700 dark:text-gray-200 dark:hover:bg-gray-800 oled:border-oled-line-strong oled:hover:bg-oled-hover"
            >
              {t("auth.logout")}
            </button>
          </div>
        </div>
      )}
    </div>
  );
}
