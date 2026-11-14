import type { ContentText } from "pdfmake/interfaces";
import { CODE_FONT, PRINT, SYMBOL_FONT } from "@/lib/pdf/page";

/** pdfmake has no per-glyph fallback: a character the code face cannot draw (above U+FFFF) is routed by hand. */
export function isSymbolChar(char: string): boolean {
  return (char.codePointAt(0) ?? 0) > 0xffff;
}

type Marks = Omit<ContentText, "text">;

/** Code as runs in the code face, each character it cannot draw set in the symbol face. */
export function codeRuns(code: string, marks: Marks = {}): ContentText[] {
  const runs: ContentText[] = [];
  for (const char of code) {
    const font = isSymbolChar(char) ? SYMBOL_FONT : CODE_FONT;
    const last = runs.at(-1);
    if (last?.font === font) last.text = `${last.text as string}${char}`;
    else runs.push({ ...marks, text: char, font });
  }
  return runs;
}

const CODE_SPAN = /`([^`]+)`/g;

/**
 * A question's plain text with its `code` spans set as tinted code runs. An unpaired backtick («acento
 * grave (`)») stays literal, and text with no span comes back as the same string.
 */
export function withCodeSpans(text: string): string | ContentText[] {
  if (!/`[^`]+`/.test(text)) return text;
  const runs: ContentText[] = [];
  let at = 0;
  for (const match of text.matchAll(CODE_SPAN)) {
    if (match.index > at) runs.push({ text: text.slice(at, match.index) });
    runs.push(...codeRuns(match[1] ?? "", { color: PRINT.codeText, background: PRINT.codeFill }));
    at = match.index + match[0].length;
  }
  if (at < text.length) runs.push({ text: text.slice(at) });
  return runs;
}
