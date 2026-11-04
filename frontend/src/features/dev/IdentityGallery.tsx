import type { CSSProperties, ReactNode } from "react";
import { useQuery } from "@tanstack/react-query";
import { getDevFigures } from "@/api/dev";
import type { CatalogueCourse } from "@/api/courses";
import { Card, Spinner } from "@/components/ui/primitives";
import identity from "@/assets/identity/identity.json";
import favicon from "@/assets/identity/favicon.svg";
import favicon16 from "@/assets/identity/favicon-16.png";
import favicon32 from "@/assets/identity/favicon-32.png";
import favicon180 from "@/assets/identity/favicon-180.png";
import favicon512 from "@/assets/identity/favicon-512.png";
import { CourseGlyph } from "@/features/courses/CourseGlyph";
import { useCatalogue } from "@/features/courses/useCourses";
import { GALLERY_COURSE } from "@/features/dev/ChartGallery";

type Theme = "light" | "dark" | "oled";
const THEMES: Theme[] = ["light", "dark", "oled"];
type Piece = "lockup-horizontal" | "lockup-stacked" | "wordmark" | "mark";

const FILES = import.meta.glob<string>("/src/assets/identity/curset-*.svg", { eager: true, query: "?url", import: "default" });

function art(piece: Piece, variant: "light" | "dark" | "mono"): string {
  return FILES[`/src/assets/identity/curset-${piece}-${variant}.svg`];
}

/** The artwork a theme draws with: OLED uses the dark files, paper on black. */
const variantOf = (theme: Theme) => (theme === "light" ? "light" : "dark");

function Row({ label, children }: { label: string; children: ReactNode }) {
  return (
    <div>
      <p className="mb-1.5 text-[11px] uppercase tracking-wide opacity-60">{label}</p>
      <div className="flex flex-wrap items-end gap-4">{children}</div>
    </div>
  );
}

/** A mono file drawn the way an inline one would be: the SVG as a mask, the text colour as its fill. */
function Mono({ piece, className }: { piece: Piece; className: string }) {
  const mask = `url("${art(piece, "mono")}") left center / contain no-repeat`;
  return <span aria-hidden="true" className={`block bg-current ${className}`} style={{ mask, WebkitMask: mask } as CSSProperties} />;
}

function ThemePanel({ theme, courses }: { theme: Theme; courses: CatalogueCourse[] }) {
  const tokens = identity.themes[theme];
  const variant = variantOf(theme);
  const shade = theme === "light" ? "light" : "dark";
  return (
    <div className="space-y-5 rounded-md p-4" style={{ background: tokens.bg, color: tokens.fg }}>
      <p className="text-sm font-semibold">{theme}</p>
      <Row label="Lockups: header 36 px, auth card 96 px">
        <img src={art("lockup-horizontal", variant)} alt="" className="h-9 w-auto" />
        <img src={art("lockup-stacked", variant)} alt="" className="h-24 w-auto" />
      </Row>
      <Row label="Wordmark, and the mark at 16, 28 and 96 px">
        <img src={art("wordmark", variant)} alt="" className="h-10 w-auto" />
        <img src={art("mark", variant)} alt="" width={16} height={16} />
        <img src={art("mark", variant)} alt="" width={28} height={28} />
        <img src={art("mark", variant)} alt="" width={96} height={96} />
      </Row>
      <Row label="Monochrome (currentColor), each piece">
        <Mono piece="lockup-horizontal" className="h-9 w-40" />
        <Mono piece="lockup-stacked" className="h-16 w-16" />
        <Mono piece="wordmark" className="h-6 w-28" />
        <Mono piece="mark" className="h-8 w-8" />
      </Row>
      <Row label="Favicon: SVG, then PNG 16, 32, 180 and 512 (the last two at 64)">
        <img src={favicon} alt="" width={32} height={32} />
        <img src={favicon16} alt="" width={16} height={16} />
        <img src={favicon32} alt="" width={32} height={32} />
        <img src={favicon180} alt="" width={64} height={64} />
        <img src={favicon512} alt="" width={64} height={64} />
      </Row>
      <Row label="Course glyphs beside their titles, dropdown size">
        <div className="space-y-2">
          {courses.map((course) => (
            <span key={course.slug} className="flex flex-wrap items-center gap-2 text-sm font-medium">
              <CourseGlyph course={course} shade={shade} />
              <span lang={course.textLocale}>{course.title}</span>
              <span className="text-xs font-normal" style={{ color: course.color?.[shade] }}>
                accent as text
              </span>
            </span>
          ))}
        </div>
      </Row>
    </div>
  );
}

/** The PDF cover at a sixth of A4: the mark on top, the glyph beside the title, as `document.ts` lays it out. */
function CoverMock({ course }: { course: CatalogueCourse }) {
  return (
    <div className="aspect-[210/297] w-64 bg-white p-6 text-gray-800 shadow-md">
      <img src={art("mark", "light")} alt="" className="mt-6 mb-8 h-7 w-7" />
      <div className="flex items-start gap-2">
        <CourseGlyph course={course} shade="light" className="mt-0.5" />
        <p className="text-lg leading-tight font-bold" lang={course.textLocale}>
          {course.title}
        </p>
      </div>
      <p className="mt-4 text-[9px] text-gray-500">Autor: Juan José Hernández Garrido</p>
      <p className="mt-2 text-[10px] text-gray-500" lang={course.textLocale}>
        {course.description}
      </p>
    </div>
  );
}

/** Dev-only review page: every identity piece in the three themes, plus the PDF cover. */
export function IdentityGallery() {
  // The dev router is mounted only under DEV_MODE; its answer (or 404) is the gate.
  const probe = useQuery({
    queryKey: ["dev-mode-probe"],
    queryFn: () => getDevFigures({ slug: GALLERY_COURSE, lang: "es" }),
    retry: false,
    meta: { silentError: true },
  });
  const { data: courses = [] } = useCatalogue();

  if (probe.isLoading) {
    return (
      <div className="flex justify-center py-16 text-gray-500">
        <Spinner />
      </div>
    );
  }
  if (probe.isError) {
    return (
      <Card className="p-6 text-sm">
        This page needs <code className="font-mono">DEV_MODE=true</code> on the backend.
      </Card>
    );
  }

  return (
    <div className="space-y-6">
      <header>
        <h1 className="text-xl font-semibold">Identity</h1>
        <p className="text-sm text-gray-500 dark:text-gray-400">
          Every Curset piece in the light, dark and OLED themes, the course glyphs and the PDF cover. Decisions are
          in docs/identity.md.
        </p>
      </header>
      <div className="grid grid-cols-1 gap-3 xl:grid-cols-3">
        {THEMES.map((theme) => (
          <ThemePanel key={theme} theme={theme} courses={courses} />
        ))}
      </div>
      <Card className="space-y-3 p-4">
        <h2 className="text-lg font-semibold">PDF cover</h2>
        <div className="flex flex-wrap gap-4">
          {courses.map((course) => (
            <CoverMock key={course.slug} course={course} />
          ))}
        </div>
      </Card>
    </div>
  );
}
