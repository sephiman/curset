import { useTheme, type ResolvedTheme } from "@/lib/theme";
import { cn } from "@/lib/cn";
import { PLATFORM_NAME } from "@/lib/platform";
// Imported rather than served from public/, so Vite content-hashes them and a new artwork gets a new URL.
import logoDark from "@/assets/brand/curset-logo-dark.png";
import logoLight from "@/assets/brand/curset-logo-light.png";
import logoOled from "@/assets/brand/curset-logo-oled.png";

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
