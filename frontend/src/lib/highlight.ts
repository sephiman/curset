import hljs from "highlight.js/lib/core";
import bash from "highlight.js/lib/languages/bash";
import http from "highlight.js/lib/languages/http";
import java from "highlight.js/lib/languages/java";
import json from "highlight.js/lib/languages/json";
import kotlin from "highlight.js/lib/languages/kotlin";
import plaintext from "highlight.js/lib/languages/plaintext";
import sql from "highlight.js/lib/languages/sql";
import yaml from "highlight.js/lib/languages/yaml";

const LANGUAGES = { bash, http, java, json, kotlin, plaintext, sql, yaml };
for (const [name, definition] of Object.entries(LANGUAGES)) hljs.registerLanguage(name, definition);

/** The registered language a fence's info word names (aliases included), or null for text and unknown words. */
export function languageOf(info: string | undefined): string | null {
  const name = hljs.getLanguage(info ?? "")?.name?.toLowerCase();
  return name && name !== "plain text" ? name : null;
}

/** The code as highlight.js markup (it escapes every character of the source); null when `language` is null. */
export function highlightedHtml(code: string, language: string | null): string | null {
  return language ? hljs.highlight(code, { language, ignoreIllegals: true }).value : null;
}
