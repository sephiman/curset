import { useTheme, type ResolvedTheme } from "@/lib/theme";
import { cn } from "@/lib/cn";
import { PLATFORM_NAME } from "@/lib/platform";
// Imported rather than served from public/, so Vite content-hashes them and a new artwork gets a new URL.
import horizontalDark from "@/assets/identity/curset-lockup-horizontal-dark.svg";
import horizontalLight from "@/assets/identity/curset-lockup-horizontal-light.svg";
import stackedDark from "@/assets/identity/curset-lockup-stacked-dark.svg";
import stackedLight from "@/assets/identity/curset-lockup-stacked-light.svg";
import markDark from "@/assets/identity/curset-mark-dark.svg";
import markLight from "@/assets/identity/curset-mark-light.svg";

type Layout = "horizontal" | "stacked";

// OLED draws in the dark artwork: paper on black reads like paper on ink.
const LOCKUP: Record<Layout, Record<ResolvedTheme, string>> = {
  horizontal: { light: horizontalLight, dark: horizontalDark, oled: horizontalDark },
  stacked: { light: stackedLight, dark: stackedDark, oled: stackedDark },
};
const MARK: Record<ResolvedTheme, string> = { light: markLight, dark: markDark, oled: markDark };

/** The Curset lockup in the theme's artwork. `decorative` when a link names it. */
export function Logo({
  className,
  decorative = false,
  layout = "horizontal",
}: {
  className?: string;
  decorative?: boolean;
  layout?: Layout;
}) {
  const { resolvedTheme } = useTheme();
  return (
    <img
      src={LOCKUP[layout][resolvedTheme]}
      alt={decorative ? "" : PLATFORM_NAME}
      className={cn("h-9 w-auto select-none", className)}
    />
  );
}

/** The mark alone, for the one-line phone header; the link around it carries the name. */
export function LogoMark() {
  const { resolvedTheme } = useTheme();
  return <img src={MARK[resolvedTheme]} alt="" width={28} height={28} className="h-7 w-7 select-none" />;
}
