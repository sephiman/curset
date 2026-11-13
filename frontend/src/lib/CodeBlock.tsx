import { useTranslation } from "react-i18next";
import { highlightedHtml, languageOf } from "@/lib/highlight";

/**
 * A fenced block: highlighted by the one registered grammar its info word names, scrolled sideways inside
 * its own box so a long line never widens the page. The info string's meta (`snippet=…`) never reaches here.
 */
export function CodeBlock({ code, info }: { code: string; info?: string }) {
  const { t } = useTranslation();
  const language = languageOf(info);
  const source = code.replace(/\n$/, "");
  const html = highlightedHtml(source, language);
  return (
    <pre
      tabIndex={0}
      role="region"
      aria-label={language ? t("markdown.codeLabel", { language }) : t("markdown.code")}
      className="my-4 max-w-full overflow-x-auto rounded-md border border-border bg-gray-50 p-3 font-mono text-[0.8125rem] leading-relaxed text-gray-800 dark:border-gray-800 dark:bg-gray-900 dark:text-gray-200 oled:border-oled-line oled:bg-oled-bg"
    >
      {html === null ? (
        <code>{source}</code>
      ) : (
        <code className={`hljs language-${language}`} dangerouslySetInnerHTML={{ __html: html }} />
      )}
    </pre>
  );
}
