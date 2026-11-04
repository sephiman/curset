import type { CSSProperties } from "react";
import { glyphUrl, type CatalogueCourse } from "@/api/courses";
import { cn } from "@/lib/cn";

/**
 * The course's glyph in its accent: the SVG is a mask and the accent its fill, so the file stays
 * currentColor-only and the shade follows the theme (paper shade in light, ink shade in dark and OLED).
 */
export function CourseGlyph({
  course,
  className,
  shade,
}: {
  course: Pick<CatalogueCourse, "slug" | "glyph" | "color">;
  className?: string;
  /** Pins one shade instead of following the theme, for a surface whose paper or ink is fixed. */
  shade?: "light" | "dark";
}) {
  if (!course.glyph) return null;
  const mask = `url("${glyphUrl(course.slug)}") center / contain no-repeat`;
  const style = {
    "--accent-light": course.color?.light ?? "currentColor",
    "--accent-dark": course.color?.dark ?? "currentColor",
    mask,
    WebkitMask: mask,
  } as CSSProperties;
  return (
    <span
      aria-hidden="true"
      data-glyph={course.glyph}
      className={cn(
        "inline-block h-5 w-5 shrink-0",
        shade === "light" && "bg-(--accent-light)",
        shade === "dark" && "bg-(--accent-dark)",
        !shade && "bg-(--accent-light) dark:bg-(--accent-dark)",
        className,
      )}
      style={style}
    />
  );
}
