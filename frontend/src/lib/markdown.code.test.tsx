import { act } from "react";
import { createRoot } from "react-dom/client";
import { beforeEach, describe, expect, it, vi } from "vitest";
import en from "@/i18n/en.json";

/** Deltas N1 and N2: fenced code is highlighted and scrolls inside its box; a judgement is a labelled callout. */

function translate(key: string, params?: Record<string, unknown>): string {
  const template = key.split(".").reduce<unknown>((node, part) => (node as Record<string, unknown>)?.[part], en);
  if (typeof template !== "string") return key;
  return template.replace(/\{\{(\w+)\}\}/g, (_, name: string) => String(params?.[name]));
}
vi.mock("react-i18next", () => ({
  useTranslation: () => ({ t: translate, i18n: { resolvedLanguage: "en", language: "en" } }),
  initReactI18next: { type: "3rdParty", init: () => {} },
}));

const { LessonMarkdown, Prose } = await import("@/lib/markdown");

(globalThis as { IS_REACT_ACT_ENVIRONMENT?: boolean }).IS_REACT_ACT_ENVIRONMENT = true;

let host: HTMLDivElement;

function lesson(markdown: string): void {
  host = document.createElement("div");
  document.body.appendChild(host);
  act(() => {
    createRoot(host).render(<LessonMarkdown markdown={markdown} renderExercise={() => null} renderFigure={() => null} />);
  });
}

function prose(markdown: string): void {
  host = document.createElement("div");
  document.body.appendChild(host);
  act(() => {
    createRoot(host).render(<Prose markdown={markdown} />);
  });
}

const JAVA = 'public class Demo {\n  static final String NAME = "x"; // a comment\n  int count = 42;\n}';

beforeEach(() => {
  document.body.innerHTML = "";
});

describe("a fenced code block", () => {
  it.each([
    ["java", "public class Demo", "keyword"],
    ["kotlin", "fun main() { val n = 1 }", "keyword"],
    ["sql", "SELECT id FROM account WHERE id = 1;", "keyword"],
    ["yaml", "name: demo\nreplicas: 3", "attr"],
    ["json", '{"id": 1, "ok": true}', "attr"],
    ["http", "GET /orders HTTP/1.1\nHost: example.org", "keyword"],
    ["bash", "if [ -f a ]; then echo hi; fi", "keyword"],
  ])("highlights %s", (language, code, tokenClass) => {
    lesson(`\`\`\`${language}\n${code}\n\`\`\``);
    const block = host.querySelector(`pre code.language-${language}`);
    expect(block).not.toBeNull();
    expect(block?.querySelector(`.hljs-${tokenClass}`)).not.toBeNull();
    expect(block?.textContent).toBe(code);
  });

  it("keeps text and unknown languages as plain code", () => {
    lesson("```text\nSELECT 1\n```\n\n```cobol\nMOVE 1 TO X\n```");
    const blocks = host.querySelectorAll("pre code");
    expect(blocks).toHaveLength(2);
    for (const block of blocks) expect(block.querySelector("span")).toBeNull();
    expect(host.textContent).toContain("MOVE 1 TO X");
  });

  it("hides the info string's meta and still highlights", () => {
    lesson("```java snippet=m06-l02/LostUpdate.java\n" + JAVA + "\n```");
    expect(host.textContent).not.toContain("snippet=");
    expect(host.textContent).not.toContain("LostUpdate.java");
    expect(host.querySelector("pre code.language-java .hljs-keyword")).not.toBeNull();
    expect(host.querySelector("pre code")?.textContent).toBe(JAVA);
  });

  it("scrolls sideways inside a keyboard-reachable region named for its language", () => {
    lesson("```java\n" + JAVA + "\n```");
    const region = host.querySelector("pre");
    expect(region?.className).toContain("overflow-x-auto");
    expect(region?.getAttribute("tabindex")).toBe("0");
    expect(region?.getAttribute("role")).toBe("region");
    expect(region?.getAttribute("aria-label")).toBe("Code, java");
  });

  it("escapes markup in the source instead of rendering it", () => {
    lesson('```java\nString s = "<b>bold</b>";\n```');
    expect(host.querySelector("pre b")).toBeNull();
    expect(host.querySelector("pre")?.textContent).toContain("<b>bold</b>");
  });

  it("leaves inline code as a chip, not a block", () => {
    lesson("Use `READ COMMITTED` here.");
    expect(host.querySelector("pre")).toBeNull();
    expect(host.querySelector("code")?.textContent).toBe("READ COMMITTED");
  });

  it("highlights in question stems, options and explanations, which share Prose", () => {
    prose("What does this print?\n\n```java\nclass Demo {}\n```");
    expect(host.querySelector("pre code.language-java .hljs-keyword")).not.toBeNull();
  });
});

describe("a bullets comment", () => {
  it("never reaches the reader", () => {
    lesson("## Locks\n\n<!-- bullets: 6.2.a 6.2.b -->\n\nA lock blocks writers.");
    expect(host.textContent).not.toContain("bullets");
    expect(host.textContent).not.toContain("6.2.a");
    expect(host.textContent).toContain("A lock blocks writers.");
  });
});

describe("a judgement block", () => {
  const JUDGEMENT =
    ':::judgement{source="Google, Site Reliability Engineering, ch. 17" ref="sre-book#ch17"}\nAccording to the SRE book, a test that cannot fail tells you nothing.\n:::';

  it("is a callout labelled as judgement with its source and its text", () => {
    lesson(JUDGEMENT);
    const callout = host.querySelector("aside[data-judgement]");
    expect(callout).not.toBeNull();
    expect(callout?.getAttribute("aria-label")).toBe("Judgement from Google, Site Reliability Engineering, ch. 17");
    expect(callout?.textContent).toContain("Judgement");
    expect(callout?.querySelector("cite")?.textContent).toBe("Google, Site Reliability Engineering, ch. 17");
    expect(callout?.textContent).toContain("sre-book#ch17");
    expect(callout?.textContent).toContain("a test that cannot fail tells you nothing.");
  });

  it("needs no ref", () => {
    lesson(':::judgement{source="Fowler"}\nAccording to Fowler, prefer composition.\n:::');
    expect(host.querySelector("aside[data-judgement] code")).toBeNull();
    expect(host.querySelector("aside[data-judgement] cite")?.textContent).toBe("Fowler");
  });

  it("is not drawn like a note", () => {
    lesson(`${JUDGEMENT}\n\n:::note{type=tip}\nA tip.\n:::`);
    expect(host.querySelectorAll("aside[data-judgement]")).toHaveLength(1);
    expect(host.textContent).toContain("A tip.");
  });
});
