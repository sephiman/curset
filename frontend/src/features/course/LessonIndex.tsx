import { useEffect, useState, type MouseEvent } from "react";
import { useTranslation } from "react-i18next";
import { cn } from "@/lib/cn";
import { isClosingSection, type OutlineEntry } from "@/lib/outline";

// A section is current once its heading has scrolled within this distance of the top.
const READING_LINE_PX = 96;

/** Which entry the reader is in: the last one whose anchor has passed the reading line. */
function useCurrentEntry(entries: OutlineEntry[]): string | null {
  const [current, setCurrent] = useState<string | null>(entries[0]?.id ?? null);
  useEffect(() => {
    let frame = 0;
    const update = () => {
      frame = 0;
      let found = entries[0]?.id ?? null;
      for (const entry of entries) {
        const element = document.getElementById(entry.id);
        if (element && element.getBoundingClientRect().top <= READING_LINE_PX) found = entry.id;
      }
      setCurrent(found);
    };
    const schedule = () => {
      if (frame === 0) frame = window.requestAnimationFrame(update);
    };
    update();
    window.addEventListener("scroll", schedule, { passive: true });
    window.addEventListener("resize", schedule);
    return () => {
      window.removeEventListener("scroll", schedule);
      window.removeEventListener("resize", schedule);
      if (frame !== 0) window.cancelAnimationFrame(frame);
    };
  }, [entries]);
  return current;
}

function IndexLink({ entry, current }: { entry: OutlineEntry; current: boolean }) {
  const go = (event: MouseEvent<HTMLAnchorElement>) => {
    const target = document.getElementById(entry.id);
    if (!target) return;
    event.preventDefault();
    target.scrollIntoView({ block: "start", behavior: "smooth" });
    window.history.replaceState(window.history.state, "", `#${entry.id}`);
  };
  return (
    <a
      href={`#${entry.id}`}
      onClick={go}
      aria-current={current ? "location" : undefined}
      className={cn(
        "-ml-px block border-l-2 pr-2 leading-snug transition-colors focus:outline-none focus-visible:ring-2 focus-visible:ring-primary",
        entry.kind === "section" ? "py-1 pl-3" : "py-0.5 pl-6 text-[13px]",
        entry.kind === "esquema" && "italic",
        current
          ? "border-primary font-medium text-primary"
          : "border-transparent text-gray-600 hover:border-gray-300 hover:text-gray-900 dark:text-gray-400 dark:hover:border-gray-600 dark:hover:text-gray-100 oled:hover:border-oled-line-strong",
      )}
    >
      {entry.text}
    </a>
  );
}

interface IndexSection {
  /** Null for whatever comes before the first `##`. */
  heading: OutlineEntry | null;
  children: OutlineEntry[];
}

function bySection(entries: OutlineEntry[]): IndexSection[] {
  const sections: IndexSection[] = [];
  for (const entry of entries) {
    if (entry.kind === "section") sections.push({ heading: entry, children: [] });
    else if (sections.length === 0) sections.push({ heading: null, children: [entry] });
    else sections[sections.length - 1].children.push(entry);
  }
  return sections;
}

function SectionList({ sections, current }: { sections: IndexSection[]; current: string | null }) {
  return (
    <ul className="border-l border-border dark:border-gray-800 oled:border-oled-line">
      {sections.map(({ heading, children }) => {
        const open = heading === null || heading.id === current || children.some((child) => child.id === current);
        // Esquema titles always show under their section; its `###` only while the reader is in it.
        const visible = children.filter((child) => open || child.kind === "esquema");
        return (
          <li key={heading?.id ?? "lead"}>
            {heading && <IndexLink entry={heading} current={heading.id === current} />}
            {visible.length > 0 && (
              <ul>
                {visible.map((child) => (
                  <li key={child.id}>
                    <IndexLink entry={child} current={child.id === current} />
                  </li>
                ))}
              </ul>
            )}
          </li>
        );
      })}
    </ul>
  );
}

/** K2: the lesson's sections and esquema titles beside the reading column; the closing sections come last. */
export function LessonIndex({ entries }: { entries: OutlineEntry[] }) {
  const { t } = useTranslation();
  const current = useCurrentEntry(entries);
  if (entries.length === 0) return null;
  const sections = bySection(entries);
  const closing = (section: IndexSection) => section.heading !== null && isClosingSection(section.heading);
  const body = sections.filter((section) => !closing(section));
  const closingSections = sections.filter(closing);
  return (
    <nav
      aria-label={t("course.lessonIndex")}
      className="sticky top-6 max-h-[calc(100dvh-3rem)] space-y-3 overflow-y-auto overscroll-contain pb-6 text-sm"
    >
      <p className="pl-3 text-xs font-semibold tracking-wide text-gray-500 uppercase dark:text-gray-400">
        {t("course.lessonIndex")}
      </p>
      <SectionList sections={body} current={current} />
      {closingSections.length > 0 && <SectionList sections={closingSections} current={current} />}
    </nav>
  );
}
