import identity from "@/assets/identity/identity.json";
import markSource from "@/assets/identity/curset-mark-mono.svg?raw";

/** The cover's drawings as SVG markup, already painted: pdfmake does not resolve currentColor. */
export interface CoverArt {
  mark: string;
  /** The course glyph in its accent; absent for a course without one. */
  glyph?: string;
}

export function paint(svg: string, colour: string): string {
  return svg.replaceAll("currentColor", colour);
}

/** Paper is the page, so the mark is ink and the glyph takes the accent's paper shade. */
export function coverArt(glyphSource: string | null, accentOnPaper: string | undefined): CoverArt {
  const ink = identity.colors.ink;
  const mark = paint(markSource, ink);
  return glyphSource ? { mark, glyph: paint(glyphSource, accentOnPaper ?? ink) } : { mark };
}
