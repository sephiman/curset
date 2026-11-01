import { useTheme, type ResolvedTheme } from "@/lib/theme";
import { cn } from "@/lib/cn";
import { PLATFORM_NAME } from "@/lib/platform";
// Imported rather than served from public/, so Vite content-hashes them and a new artwork gets a new URL.
import logoDark from "@/assets/brand/curset-logo-dark.png";
import logoLight from "@/assets/brand/curset-logo-light.png";
import logoOled from "@/assets/brand/curset-logo-oled.png";
import iconDark from "@/assets/brand/curset-icon-dark.png";
import iconLight from "@/assets/brand/curset-icon-light.png";

const LOGO_SRC: Record<ResolvedTheme, string> = { light: logoLight, dark: logoDark, oled: logoOled };

/** The Curset wordmark in the artwork drawn for the theme on screen. `decorative` when a link names it. */
export function Logo({ className, decorative = false }: { className?: string; decorative?: boolean }) {
  const { resolvedTheme } = useTheme();
  return (
    <img
      src={LOGO_SRC[resolvedTheme]}
      alt={decorative ? "" : PLATFORM_NAME}
      width={720}
      height={192}
      className={cn("h-9 w-auto select-none", className)}
    />
  );
}

const MARK_SRC: Record<ResolvedTheme, string> = { light: iconLight, dark: iconDark, oled: iconDark };

/** The compact mark plus the name, for the one-line phone header. */
export function LogoMark() {
  const { resolvedTheme } = useTheme();
  return (
    <span className="inline-flex items-center gap-1.5">
      <img src={MARK_SRC[resolvedTheme]} alt="" width={28} height={28} className="h-7 w-7 select-none" />
      <span className="text-base font-semibold tracking-tight">{PLATFORM_NAME}</span>
    </span>
  );
}
