import regular from "@/assets/fonts/liberation-sans/LiberationSans-Regular.ttf?url";
import bold from "@/assets/fonts/liberation-sans/LiberationSans-Bold.ttf?url";
import italic from "@/assets/fonts/liberation-sans/LiberationSans-Italic.ttf?url";
import boldItalic from "@/assets/fonts/liberation-sans/LiberationSans-BoldItalic.ttf?url";
import mono from "@/assets/fonts/liberation-mono/LiberationMono-Regular.ttf?url";
import monoBold from "@/assets/fonts/liberation-mono/LiberationMono-Bold.ttf?url";
import symbol from "@/assets/fonts/dejavu-sans/DejaVuSans.ttf?url";

/** The print font as build assets: hashed URLs, fetched on demand, never in the app's JS chunks. */
export const PRINT_FONT_URLS: Record<string, string> = {
  "LiberationSans-Regular.ttf": regular,
  "LiberationSans-Bold.ttf": bold,
  "LiberationSans-Italic.ttf": italic,
  "LiberationSans-BoldItalic.ttf": boldItalic,
  "LiberationMono-Regular.ttf": mono,
  "LiberationMono-Bold.ttf": monoBold,
  "DejaVuSans.ttf": symbol,
};
