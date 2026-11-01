import type { ReactNode } from "react";
import { useStackedEsquema } from "@/lib/EsquemaBlock";
import { cn } from "@/lib/cn";

type Align = "left" | "right" | "center" | "justify" | "char" | undefined;

/*
 * GFM tables. Same rule as the PDF's tables and SharedLedger's data tables: horizontal rules only, the
 * header rule a step stronger than the row rules; the wrapper scrolls so a wide table never widens the
 * page. Inside a stacked esquema (J4) the same rows render as cards, one cell per line as «header: value».
 */

export function MarkdownTable({ children }: { children?: ReactNode }) {
  if (useStackedEsquema()) return <div role="list" className="space-y-2">{children}</div>;
  return (
    <div className="my-4 overflow-x-auto">
      <table className="w-full text-sm">{children}</table>
    </div>
  );
}

export function MarkdownTableHead({ children }: { children?: ReactNode }) {
  if (useStackedEsquema()) return null;
  return (
    <thead className="border-b border-gray-300 text-gray-500 dark:border-gray-700 dark:text-gray-400 oled:border-oled-line-strong">
      {children}
    </thead>
  );
}

export function MarkdownTableBody({ children }: { children?: ReactNode }) {
  if (useStackedEsquema()) return <>{children}</>;
  return <tbody className="divide-y divide-border dark:divide-gray-800 oled:divide-oled-line">{children}</tbody>;
}

export function MarkdownTableRow({ children }: { children?: ReactNode }) {
  if (!useStackedEsquema()) return <tr>{children}</tr>;
  return (
    <div
      role="listitem"
      className="space-y-1 rounded-md border border-border px-3 py-2 text-sm dark:border-gray-800 oled:border-oled-line"
    >
      {children}
    </div>
  );
}

// `align` carries a `|:---:|` column marker; left is the default only while none is set.
export function MarkdownTableHeaderCell({ align, children }: { align?: Align; children?: ReactNode }) {
  return (
    <th align={align} className={cn("py-2 pr-4 last:pr-0", !align && "text-left")}>
      {children}
    </th>
  );
}

export function MarkdownTableCell({ align, header, children }: { align?: Align; header?: string; children?: ReactNode }) {
  if (useStackedEsquema()) {
    return (
      <div className="leading-snug break-words text-gray-700 first:font-medium first:text-gray-900 dark:text-gray-300 dark:first:text-gray-100">
        {header && <span className="font-normal text-gray-500 dark:text-gray-400">{header}: </span>}
        {children}
      </div>
    );
  }
  return (
    <td align={align} className="py-2 pr-4 align-top text-gray-700 last:pr-0 dark:text-gray-300">
      {children}
    </td>
  );
}
