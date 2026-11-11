import type { GeneratedTable as Table } from "@/api/exercises";

/** The table of a generated item, above its options; wide tables scroll inside their own container. */
export function GeneratedTable({ table }: { table: Table }) {
  return (
    <div className="mt-3 overflow-x-auto rounded-md border border-border dark:border-gray-700">
      <table className="min-w-full text-sm">
        <caption className="bg-gray-50 px-3 py-1.5 text-left text-xs font-semibold text-gray-600 dark:bg-gray-900 dark:text-gray-300">
          {table.title}
        </caption>
        <thead>
          <tr className="border-y border-border text-left text-xs text-gray-600 dark:border-gray-700 dark:text-gray-300">
            {table.header.map((cell, column) => (
              <th key={column} scope="col" className="px-3 py-1.5 font-semibold whitespace-nowrap">
                {cell}
              </th>
            ))}
          </tr>
        </thead>
        <tbody className="divide-y divide-border dark:divide-gray-800">
          {table.rows.map((row, line) => (
            <tr key={line}>
              {row.map((cell, column) => (
                <td key={column} className="px-3 py-1.5 whitespace-nowrap tabular-nums">
                  {cell}
                </td>
              ))}
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}
