import type { LessonDiagram } from "@/api/course";

/** The backend's drawing, scrolling inside its own box so a wide diagram never widens the page. */
export function DiagramFigure({ diagram }: { diagram: LessonDiagram | undefined }) {
  if (!diagram) return null;
  return (
    <figure data-diagram={diagram.kind} className="my-4">
      <div
        role="region"
        aria-label={diagram.caption}
        tabIndex={0}
        className="overflow-x-auto rounded-md border border-gray-200 p-3 dark:border-gray-700 oled:border-oled-line [&>svg]:mx-auto [&>svg]:max-w-none"
        // Trusted: drawn and escaped by the backend from the lesson file.
        dangerouslySetInnerHTML={{ __html: diagram.svg }}
      />
      <figcaption className="mt-1 text-center text-sm text-gray-600 dark:text-gray-400">{diagram.caption}</figcaption>
    </figure>
  );
}
