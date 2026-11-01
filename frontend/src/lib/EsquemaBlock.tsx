import { createContext, useContext, type ReactNode } from "react";
import type { EsquemaCellRole, EsquemaKind } from "@/lib/esquema";
import { cn } from "@/lib/cn";
import { useStackedEsquemas } from "@/lib/viewport";

/**
 * An esquema on screen. `tabla` is its table (it scrolls inside its own box on a phone); `plazos` a
 * timeline, `pasos` a numbered stepper with document and organ columns, `arbol` an indented tree. On a
 * phone the timeline, the stepper and the tree stack their cells; the order of the words never changes.
 */

const KindContext = createContext<EsquemaKind>("tabla");
/** True inside an esquema laid out for a narrow screen (J4): tables as cards, lists vertical. */
const StackedContext = createContext(false);

export function useStackedEsquema(): boolean {
  return useContext(StackedContext);
}

const CELL_STYLE: Record<EsquemaCellRole, string> = {
  label: "font-medium text-gray-900 dark:text-gray-100",
  plazo: "tabular-nums",
  detail: "",
  document: "",
  organ: "",
  citation: "text-xs text-gray-500 dark:text-gray-400 sm:text-right",
};

const ROW_GRID: Record<EsquemaKind, string> = {
  tabla: "",
  plazos: "sm:grid-cols-[1fr_auto_auto]",
  pasos: "sm:grid-cols-[1.2fr_1fr_1fr_auto]",
  arbol: "sm:grid-cols-[1fr_1.4fr_auto]",
};

export function EsquemaBlock({ kind, title, children }: { kind: EsquemaKind; title: string; children: ReactNode }) {
  const stacked = useStackedEsquemas();
  return (
    <figure
      data-esquema={kind}
      className="my-5 rounded-lg border border-border p-3 dark:border-gray-800 oled:border-oled-line"
    >
      <figcaption className="mb-2 text-sm font-semibold text-gray-900 dark:text-gray-100">{title}</figcaption>
      <KindContext.Provider value={kind}>
        <StackedContext.Provider value={stacked}>
          <div
            className={cn(
              kind === "plazos" && "border-l-2 border-primary/40 pl-3",
              (kind === "pasos" || (stacked && kind === "plazos")) && "[counter-reset:paso]",
            )}
          >
            {children}
          </div>
        </StackedContext.Provider>
      </KindContext.Provider>
    </figure>
  );
}

export function EsquemaRow({ depth, children }: { depth: number; children: ReactNode }) {
  const kind = useContext(KindContext);
  const stacked = useContext(StackedContext);
  const numbered = kind === "pasos" || (stacked && kind === "plazos");
  const branch = kind === "arbol" && depth > 0;
  const indent = stacked ? 0.875 : 1.25;
  return (
    <div
      role="group"
      style={kind === "arbol" ? { [stacked ? "marginLeft" : "paddingLeft"]: `${depth * indent}rem` } : undefined}
      className={cn(
        "grid grid-cols-1 gap-x-4 gap-y-0.5 border-b border-border py-2 text-sm last:border-b-0 dark:border-gray-800 oled:border-oled-line",
        ROW_GRID[kind],
        numbered && "[counter-increment:paso] before:font-semibold before:text-primary before:content-[counter(paso)'.'] sm:before:hidden",
        branch && !stacked && "border-l border-l-gray-300 dark:border-l-gray-700",
        // A connector from the parent's rail into this node: the left rule plus a short tick.
        branch && stacked && "relative border-l border-l-gray-300 pl-4 after:absolute after:top-[1.05rem] after:left-0 after:w-3 after:border-t after:border-gray-300 dark:border-l-gray-700 dark:after:border-gray-700 oled:border-l-oled-line-strong oled:after:border-oled-line-strong",
      )}
    >
      {children}
    </div>
  );
}

export function EsquemaCell({ role, children }: { role: EsquemaCellRole; children: ReactNode }) {
  return <span className={cn("leading-snug", CELL_STYLE[role])}>{children}</span>;
}
