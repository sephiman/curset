import { act, type ReactElement } from "react";
import { createRoot } from "react-dom/client";
import { MemoryRouter } from "react-router-dom";
import { QueryClient, QueryClientProvider } from "@tanstack/react-query";
import { beforeEach, describe, expect, it, vi } from "vitest";
import type { Course, CourseMeta } from "@/api/course";
import en from "@/i18n/en.json";
import type { GenerateProgress } from "@/lib/pdf/generate";
import { InCourse } from "@/test/course";

/** The export dialog: what it says it will print, what it hands the generator, and what it shows while it runs. */

interface Generated {
  onProgress?: (p: GenerateProgress) => void;
}
const generateCoursePdf = vi.fn<(o: Generated) => Promise<unknown>>();
const downloadPdf = vi.fn();
let includeExercises = false;
let phone = false;

vi.mock("@/lib/pdf/generate", () => ({
  generateCoursePdf: (o: Generated) => generateCoursePdf(o),
  downloadPdf: (generated: unknown) => downloadPdf(generated),
}));
vi.mock("@/auth/AuthContext", () => ({
  useAuth: () => ({ user: { pdf_exercises: includeExercises } }),
}));
vi.mock("@/lib/viewport", () => ({ usePhoneLayout: () => phone }));

/** The real EN catalog, interpolated: the test asserts the strings a reader actually sees. */
function translate(key: string, params?: Record<string, unknown>): string {
  const template = key
    .split(".")
    .reduce<unknown>((node, part) => (node as Record<string, unknown>)?.[part], en);
  if (typeof template !== "string") throw new Error(`missing catalog key ${key}`);
  return template.replace(/\{\{(\w+)\}\}/g, (_, name: string) => String(params?.[name]));
}

vi.mock("react-i18next", () => ({
  useTranslation: () => ({ t: translate, i18n: { resolvedLanguage: "en" } }),
  initReactI18next: { type: "3rdParty", init: () => {} },
}));

const { ExportPdfAction } = await import("@/features/pdfExport/ExportPdfAction");
const { HeaderChromeProvider, useHeaderActionTarget } = await import("@/components/layout/headerChrome");

(globalThis as { IS_REACT_ACT_ENVIRONMENT?: boolean }).IS_REACT_ACT_ENVIRONMENT = true;

const META: CourseMeta = {
  id: "crypto-futures",
  title: "Crypto Perpetual Futures: The Beginner's Guide",
  subtitle: "The Beginner's Guide",
  description: "From zero.",
};

function tree(meta: CourseMeta): Course {
  return { locale: "en", started: false, course: meta, blocks: [] };
}

const COURSE = tree(META);
const MODULE = { kind: "module", id: "m03", title: "Funding" } as const;

function mount(node: ReactElement): void {
  const host = document.createElement("div");
  document.body.appendChild(host);
  const client = new QueryClient({ defaultOptions: { mutations: { retry: false } } });
  act(() => {
    createRoot(host).render(
      <QueryClientProvider client={client}>
        <MemoryRouter>
          <HeaderChromeProvider>
            <InCourse>{node}</InCourse>
          </HeaderChromeProvider>
        </MemoryRouter>
      </QueryClientProvider>,
    );
  });
}

function buttonNamed(name: string): HTMLButtonElement {
  const found = [...document.querySelectorAll("button")].find((b) => b.textContent?.trim() === name);
  if (!found) throw new Error(`no button ${name}`);
  return found;
}

function dialog(): HTMLElement | null {
  return document.querySelector('[role="dialog"]');
}

async function click(button: HTMLElement): Promise<void> {
  await act(async () => {
    button.click();
  });
}

/** The mutation's state lands over several ticks, not one microtask. */
async function waitUntil(ready: () => boolean, what: string): Promise<void> {
  for (let attempt = 0; attempt < 50; attempt++) {
    await act(async () => {
      await new Promise((resolve) => setTimeout(resolve, 0));
    });
    if (ready()) return;
  }
  throw new Error(`timed out waiting for ${what}`);
}

beforeEach(() => {
  generateCoursePdf.mockReset();
  downloadPdf.mockReset();
  includeExercises = false;
  phone = false;
  document.body.innerHTML = "";
});

describe("the export dialog", () => {
  it("says «theory only» while the account switch is off, and links to the setting", async () => {
    mount(<ExportPdfAction course={COURSE} target={MODULE} label={en.course.pdfActionModule} />);
    await click(buttonNamed(en.course.pdfActionModule));
    expect(dialog()?.textContent).toContain("M03 · Funding");
    expect(dialog()?.textContent).toContain(en.course.pdfTheoryOnly);
    expect(dialog()?.querySelector('a[href="/account"]')?.textContent).toBe(en.course.pdfChangeSetting);
  });

  it("says «with exercises» when the switch is on and the course can print them", async () => {
    includeExercises = true;
    mount(<ExportPdfAction course={COURSE} target={MODULE} label={en.course.pdfActionModule} />);
    await click(buttonNamed(en.course.pdfActionModule));
    expect(dialog()?.textContent).toContain(en.course.pdfWithExercises);
  });

  it("stays «theory only» for a course that cannot print exercises, whatever the switch says", async () => {
    includeExercises = true;
    mount(
      <ExportPdfAction course={tree({ ...META, pdfExercises: false })} target={MODULE} label={en.course.pdfActionModule} />,
    );
    await click(buttonNamed(en.course.pdfActionModule));
    expect(dialog()?.textContent).toContain(en.course.pdfTheoryOnly);
  });

  it("hands the generator the scope and the exercise mode, then the file to the browser", async () => {
    includeExercises = true;
    const generated = { blob: new Blob(["%PDF-"]), filename: "curset-crypto-futures-m03-en-2026-11-13.pdf" };
    generateCoursePdf.mockResolvedValue(generated);
    mount(<ExportPdfAction course={COURSE} target={MODULE} label={en.course.pdfActionModule} />);
    await click(buttonNamed(en.course.pdfActionModule));
    await click(buttonNamed(en.course.pdfStart));
    await waitUntil(() => downloadPdf.mock.calls.length > 0, "the download");

    expect(generateCoursePdf).toHaveBeenCalledWith(
      expect.objectContaining({
        part: { kind: "module", id: "m03", title: "M03 · Funding" },
        exercises: "inline",
        scope: { slug: "crypto-futures", lang: "en" },
        // The course tree, so the builder can label every lesson reference (N5).
        outline: COURSE,
      }),
    );
    expect(downloadPdf).toHaveBeenCalledWith(generated);
    expect(dialog()).toBeNull();
  });

  it("names the scope and the phase while it runs", async () => {
    let report: (p: GenerateProgress) => void = () => {};
    let finish: () => void = () => {};
    generateCoursePdf.mockImplementation(async (o) => {
      report = (p) => o.onProgress?.(p);
      await new Promise<void>((resolve) => {
        finish = resolve;
      });
      return { blob: new Blob([]), filename: "f.pdf" };
    });
    mount(<ExportPdfAction course={COURSE} target={MODULE} label={en.course.pdfActionModule} />);
    await click(buttonNamed(en.course.pdfActionModule));
    await click(buttonNamed(en.course.pdfStart));
    const status = () => document.querySelector('[role="status"]')?.textContent ?? "";

    await act(async () => {
      report({ phase: "figures", done: 12, total: 29 });
    });
    expect(status()).toBe("M03 · Funding: Drawing figures 12/29…");
    await act(async () => {
      report({ phase: "typeset", done: 0, total: 0 });
    });
    expect(status()).toBe(`M03 · Funding: ${en.course.pdfTypesetting}`);
    await act(async () => {
      finish();
    });
    await waitUntil(() => dialog() === null, "the dialog to close");
  });

  it("keeps the failure in the dialog, naming the reason, and offers a retry", async () => {
    generateCoursePdf.mockRejectedValue(new Error("figure fig-m09-accumulation could not be loaded"));
    mount(<ExportPdfAction course={COURSE} target={MODULE} label={en.course.pdfActionModule} />);
    await click(buttonNamed(en.course.pdfActionModule));
    await click(buttonNamed(en.course.pdfStart));
    await waitUntil(() => document.querySelector('[role="alert"]') !== null, "the error state");
    expect(document.querySelector('[role="alert"]')?.textContent).toContain("fig-m09-accumulation");

    generateCoursePdf.mockResolvedValue({ blob: new Blob([]), filename: "f.pdf" });
    await click(buttonNamed(en.course.pdfRetry));
    await waitUntil(() => downloadPdf.mock.calls.length > 0, "the retry to succeed");
    expect(document.querySelector('[role="alert"]')).toBeNull();
  });
});

describe("on a phone", () => {
  it("offers the export in the header menu rather than as a page button", async () => {
    phone = true;
    let offered: string | undefined;
    function MenuProbe() {
      offered = useHeaderActionTarget()?.label;
      return null;
    }
    mount(
      <>
        <ExportPdfAction course={COURSE} target={MODULE} label={en.course.pdfActionModule} />
        <MenuProbe />
      </>,
    );
    expect(offered).toBe(en.course.pdfActionModule);
    expect([...document.querySelectorAll("button")].some((b) => b.textContent === en.course.pdfActionModule)).toBe(
      false,
    );
  });
});
