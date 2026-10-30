import { useMemo, useState } from "react";
import { Link } from "react-router-dom";
import { useTranslation } from "react-i18next";
import type { LessonTable, LessonTableLists, LessonTableRow } from "@/api/stats";
import { useCourse } from "@/features/courses/CourseContext";
import { cn } from "@/lib/cn";

type SortColumn = "order" | "questions" | "correct" | "wrong" | "blank" | "pct" | "avgTime";

function pct(value: number | null): string {
  return value == null ? "—" : `${Math.round(value * 100)}%`;
}

function formatAvgTime(seconds: number | null | undefined): string {
  if (seconds == null) return "—";
  const s = Math.round(seconds);
  const m = Math.floor(s / 60);
  const rem = s % 60;
  return m > 0 ? `${m}m ${rem}s` : `${rem}s`;
}

function sortRows<T extends LessonTableRow>(rows: T[], column: SortColumn): T[] {
  if (column === "order") return rows;
  if (column === "avgTime") {
    return [...rows].sort((a, b) => (b.averageSeconds ?? 0) - (a.averageSeconds ?? 0));
  }
  // Highest first, except the percentage, where the weakest lesson is the one worth seeing first.
  const sign = column === "pct" ? 1 : -1;
  return [...rows].sort((a, b) => sign * ((a[column] ?? 0) - (b[column] ?? 0)));
}

function Lists({ lists, threshold }: { lists: LessonTableLists; threshold: number }) {
  const { t } = useTranslation();
  const { path } = useCourse();
  const entry = (row: LessonTableLists["best"][number]) => (
    <li key={row.lessonId ?? row.moduleId} className="flex items-baseline justify-between gap-3 text-sm">
      {row.lessonId ? (
        <Link to={path(`/lessons/${row.lessonId}`)} className="truncate text-primary hover:underline">
          {row.title}
        </Link>
      ) : (
        <span className="truncate">{row.title}</span>
      )}
      <span className="shrink-0 tabular-nums text-gray-500 dark:text-gray-400">
        {pct(row.pct)} <span className="text-xs">({row.correct}/{row.questions})</span>
      </span>
    </li>
  );
  return (
    <div className="space-y-2">
      <div className="grid gap-4 sm:grid-cols-2">
        <section>
          <h3 className="text-xs font-semibold tracking-wide text-gray-500 uppercase dark:text-gray-400">{t("byLesson.best")}</h3>
          <ul className="mt-1 space-y-1">{lists.best.map(entry)}</ul>
        </section>
        <section>
          <h3 className="text-xs font-semibold tracking-wide text-gray-500 uppercase dark:text-gray-400">{t("byLesson.worst")}</h3>
          <ul className="mt-1 space-y-1">{lists.worst.map(entry)}</ul>
        </section>
      </div>
      <p className="text-xs text-gray-500 dark:text-gray-400">
        {lists.level === "module" ? t("byLesson.byModule") : t("byLesson.threshold", { count: threshold })}
      </p>
    </div>
  );
}

/**
 * «Por tema» (or «Por lección»): every lesson with questions, grouped under its module with the module's
 * totals, and the two short lists above when three lessons — or, failing that, three modules — have
 * enough questions to rank. Blanks are their own column.
 */
export function ByLessonTable({ table, noun }: { table: LessonTable; noun?: string | null }) {
  const { t } = useTranslation();
  const { path } = useCourse();
  const [sort, setSort] = useState<SortColumn>("order");
  const hasAvgTime = useMemo(
    () => table.groups.some((g) => g.averageSeconds != null || g.lessons.some((l) => l.averageSeconds != null)),
    [table],
  );
  const groups = useMemo(
    () => table.groups.map((group) => ({ ...group, lessons: sortRows(group.lessons, sort) })),
    [table, sort],
  );
  const columns: { key: SortColumn; label: string }[] = useMemo(() => {
    const cols: { key: SortColumn; label: string }[] = [
      { key: "questions", label: t("byLesson.questions") },
      { key: "correct", label: t("byLesson.correct") },
      { key: "wrong", label: t("byLesson.wrong") },
      { key: "blank", label: t("byLesson.blank") },
      { key: "pct", label: t("byLesson.pct") },
    ];
    if (hasAvgTime) {
      cols.push({ key: "avgTime", label: t("byLesson.avgTime") });
    }
    return cols;
  }, [hasAvgTime, t]);
  const numbers = (row: LessonTableRow) => (
    <>
      <td className="py-1.5 pr-3 text-right tabular-nums">{row.questions}</td>
      <td className="py-1.5 pr-3 text-right tabular-nums">{row.correct}</td>
      <td className="py-1.5 pr-3 text-right tabular-nums">{row.wrong}</td>
      <td className="py-1.5 pr-3 text-right tabular-nums">{row.blank}</td>
      <td className={cn("py-1.5 text-right tabular-nums", hasAvgTime && "pr-3")}>{pct(row.pct)}</td>
      {hasAvgTime && (
        <td className="py-1.5 text-right font-mono text-xs text-gray-500 tabular-nums dark:text-gray-400">
          {formatAvgTime(row.averageSeconds)}
        </td>
      )}
    </>
  );

  return (
    <section className="space-y-4" aria-label={t("byLesson.title", { noun: noun ?? t("byLesson.lesson") })}>
      <h2 className="text-sm font-semibold tracking-wide text-gray-500 uppercase dark:text-gray-400">
        {t("byLesson.title", { noun: noun ?? t("byLesson.lesson") })}
      </h2>
      {table.lists && <Lists lists={table.lists} threshold={table.threshold} />}
      {table.groups.length === 0 ? (
        <p className="text-sm text-gray-500 dark:text-gray-400">{t("byLesson.empty")}</p>
      ) : (
        <div className="overflow-x-auto">
          <table className="w-full min-w-[32rem] text-sm">
            <thead className="border-b border-gray-300 text-gray-500 dark:border-gray-700 dark:text-gray-400">
              <tr>
                <th className="py-2 pr-3 text-left">
                  <button type="button" onClick={() => setSort("order")} className="hover:underline">
                    {noun ?? t("byLesson.lesson")}
                  </button>
                </th>
                {columns.map((column) => (
                  <th key={column.key} className="py-2 pr-3 text-right last:pr-0">
                    <button
                      type="button"
                      aria-label={t("byLesson.sortBy", { column: column.label })}
                      aria-pressed={sort === column.key}
                      onClick={() => setSort(column.key)}
                      className={cn("hover:underline", sort === column.key && "text-gray-900 dark:text-gray-100")}
                    >
                      {column.label}
                    </button>
                  </th>
                ))}
              </tr>
            </thead>
            {groups.map((group) => (
              <tbody key={group.moduleId} className="divide-y divide-border dark:divide-gray-800">
                <tr className="font-semibold text-gray-900 dark:text-gray-100">
                  <th scope="rowgroup" className="py-1.5 pr-3 text-left">{group.title}</th>
                  {numbers(group)}
                </tr>
                {group.lessons.map((row) => (
                  <tr key={row.lessonId} className="text-gray-700 dark:text-gray-300">
                    <td className="py-1.5 pr-3 pl-3">
                      <Link to={path(`/lessons/${row.lessonId}`)} className="text-primary hover:underline">
                        {row.title}
                      </Link>
                    </td>
                    {numbers(row)}
                  </tr>
                ))}
              </tbody>
            ))}
          </table>
        </div>
      )}
      <p className="text-xs text-gray-500 dark:text-gray-400">{t("byLesson.blankNote")}</p>
    </section>
  );
}
