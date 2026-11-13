import { expect, test, type Page } from "@playwright/test";
import { AGE, abandonSitting, overflowingElements, signIn, startSitting, submittedSitting, startPracticeAndPickFirstOption } from "./session";

/** Delta K at real widths: the desktop layout, and the «Por tema» cards on a phone. */

const WIDTHS = [768, 1024, 1280, 1440] as const;
const LONG_PATH_ANSWER_SEED = 73;
const LONG_PATH = "C:\\Documents\\Newsletters\\Summer2018.pdf";
const ESQUEMA_LESSON = `/courses/${AGE}/lessons/m01-l03`;
const lessonIndex = (page: Page) => page.getByRole("navigation", { name: "En esta lección" });
const headerTabs = (page: Page) => page.getByRole("banner").getByRole("navigation", { name: "Secciones" });

async function expectNothingWiderThanTheScreen(page: Page): Promise<void> {
  await page.waitForLoadState("networkidle");
  expect(await overflowingElements(page)).toEqual([]);
}

test.describe("at 1280 px", () => {
  test.use({ viewport: { width: 1280, height: 800 } });

  test("the four tabs are in the header, the current one marked", async ({ page }) => {
    await signIn(page);
    await page.goto(`/courses/${AGE}/exams`);
    await expect(headerTabs(page).getByRole("link")).toHaveText(["Curso", "Glosario", "Exámenes", "Progreso"]);
    await expect(headerTabs(page).getByRole("link", { name: "Exámenes" })).toHaveAttribute("aria-current", "page");
  });

  test("the mark does not move between the course page and a lesson", async ({ page }) => {
    await signIn(page);
    const mark = page.getByRole("banner").getByRole("link", { name: /Curset/ });
    await page.goto(`/courses/${AGE}`);
    const onCourse = await mark.boundingBox();
    await page.goto(ESQUEMA_LESSON);
    await lessonIndex(page).waitFor();
    expect(await mark.boundingBox()).toEqual(onCourse);
  });

  test("a lesson shows its index beside a centred reading column of about 70 characters", async ({ page }) => {
    await signIn(page);
    await page.goto(ESQUEMA_LESSON);
    const index = await lessonIndex(page).boundingBox();
    const column = await page.locator("article").boundingBox();
    expect(index!.x + index!.width).toBeLessThanOrEqual(column!.x);
    expect(Math.abs(column!.x + column!.width / 2 - 640)).toBeLessThan(24);
    // The longest line of the longest paragraph: what the measure lets through.
    const longest = await page.evaluate(() => {
      const paragraph = [...document.querySelectorAll("article p")].sort(
        (a, b) => (b.textContent ?? "").length - (a.textContent ?? "").length,
      )[0];
      const lines = new Map<number, number>();
      const walker = document.createTreeWalker(paragraph, NodeFilter.SHOW_TEXT);
      for (let node = walker.nextNode(); node; node = walker.nextNode()) {
        for (let i = 0; i < (node.textContent ?? "").length; i += 1) {
          const range = document.createRange();
          range.setStart(node, i);
          range.setEnd(node, i + 1);
          const top = Math.round(range.getBoundingClientRect().top);
          lines.set(top, (lines.get(top) ?? 0) + 1);
        }
      }
      return Math.max(...lines.values());
    });
    expect(longest).toBeGreaterThanOrEqual(66);
    expect(longest).toBeLessThanOrEqual(76);
    await expect(page.locator('figure[data-esquema="tabla"]').first().locator("table")).toBeVisible();
  });

  test("the sitting shows the full grid in a side panel", async ({ page }) => {
    await signIn(page);
    const sitting = await startSitting(page.request, AGE, "simulacro");
    try {
      await page.goto(`/courses/${AGE}/exams/${sitting.id}`);
      const panel = page.getByRole("navigation", { name: "Navegación entre preguntas" });
      await expect(panel.getByText("Preguntas", { exact: true })).toBeVisible();
      // Reserves are named «71 · Reserva» and printed «R71».
      await expect(panel.getByRole("button", { name: /^71 · / })).toHaveText("R71");
      await expect(page.getByRole("button", { name: "Ir a…" })).toHaveCount(0);
      const question = await page.getByRole("radio").first().boundingBox();
      expect((await panel.boundingBox())!.x).toBeGreaterThan(question!.x);
    } finally {
      await abandonSitting(page.request, AGE, sitting.id);
    }
  });

  test("the results show the two lists side by side, «Por tema» full width below", async ({ page }) => {
    await signIn(page);
    const id = await submittedSitting(page.request, AGE, "simulacro");
    await page.goto(`/courses/${AGE}/exams/${id}/review`);
    // boundingBox() does not wait: the lists render after the results load.
    const bestHeading = page.getByRole("heading", { name: "Donde más brillas" });
    const worstHeading = page.getByRole("heading", { name: "Donde más tienes que preparar" });
    await expect(bestHeading).toBeVisible();
    await expect(worstHeading).toBeVisible();
    const best = await bestHeading.boundingBox();
    const worst = await worstHeading.boundingBox();
    expect(worst!.y).toBe(best!.y);
    expect(worst!.x).toBeGreaterThan(best!.x);
    const table = await page.getByRole("region", { name: "Por tema" }).locator("table").boundingBox();
    expect(table!.width).toBeGreaterThan(900);
  });
});

test.describe("«Por tema» at 360 px", () => {
  test.use({ viewport: { width: 360, height: 800 }, isMobile: true, hasTouch: true, deviceScaleFactor: 2 });

  test("is a card per lesson, with no table", async ({ page }) => {
    await signIn(page);
    const id = await submittedSitting(page.request, AGE, "simulacro");
    await page.goto(`/courses/${AGE}/exams/${id}/review`);
    const section = page.getByRole("region", { name: "Por tema" });
    // The best/worst lists are list items too; the cards are the ones with a tally.
    await expect(section.getByRole("listitem").filter({ hasText: "Aciertos" }).first()).toBeVisible();
    await expect(section.locator("table")).toHaveCount(0);
    await expectNothingWiderThanTheScreen(page);
  });

  test("wraps an answer that is one long unbreakable path instead of widening the page", async ({ page }) => {
    await signIn(page);
    // A pinned draw that counts m06-l03-q050, answered with its «C:\Documents\Newsletters\Summer2018.pdf» option.
    // A bank edit changes the draw: the visibility check below then fails, and the seed is re-picked.
    const id = await submittedSitting(page.request, AGE, "simulacro", {
      seed: LONG_PATH_ANSWER_SEED,
      prefer: LONG_PATH,
    });
    await page.goto(`/courses/${AGE}/exams/${id}/review`);
    await expect(page.getByText("Tu respuesta:").first()).toBeVisible();
    await expect(page.getByText(LONG_PATH).filter({ visible: true }).first()).toBeVisible();
    await expectNothingWiderThanTheScreen(page);
  });
});

test.describe("nothing wider than the screen", () => {
  for (const width of WIDTHS) {
    test.describe(`at ${width} px`, () => {
      test.use({ viewport: { width, height: 800 } });

      test("course page", async ({ page }) => {
        await signIn(page);
        await page.goto(`/courses/${AGE}`);
        await expect(page.getByRole("heading", { level: 1 })).toBeVisible();
        await expectNothingWiderThanTheScreen(page);
      });

      test("lesson with esquema", async ({ page }) => {
        await signIn(page);
        await page.goto(ESQUEMA_LESSON);
        await page.locator('figure[data-esquema="tabla"]').first().waitFor();
        await expectNothingWiderThanTheScreen(page);
      });

      test("practice with the solution panel open", async ({ page }) => {
        await signIn(page);
        await page.goto(`${ESQUEMA_LESSON}/practice`);
        await startPracticeAndPickFirstOption(page);
        await page.getByRole("button", { name: "Enviar" }).click();
        await expect(page.getByText("Ver solución")).toBeVisible();
        await expectNothingWiderThanTheScreen(page);
      });

      test("simulation sitting", async ({ page }) => {
        await signIn(page);
        const sitting = await startSitting(page.request, AGE, "simulacro");
        try {
          await page.goto(`/courses/${AGE}/exams/${sitting.id}`);
          await expect(page.getByRole("radio").first()).toBeVisible();
          await expectNothingWiderThanTheScreen(page);
        } finally {
          await abandonSitting(page.request, AGE, sitting.id);
        }
      });

      test("results by tema", async ({ page }) => {
        await signIn(page);
        const id = await submittedSitting(page.request, AGE, "simulacro");
        await page.goto(`/courses/${AGE}/exams/${id}/review`);
        await expect(page.getByRole("heading", { name: "Por tema" })).toBeVisible();
        await expectNothingWiderThanTheScreen(page);
      });

      test("course selector open", async ({ page }) => {
        await signIn(page);
        await page.goto(`/courses/${AGE}`);
        await page.getByRole("button", { name: /Cambiar de curso/ }).click();
        await expect(page.getByRole("dialog")).toBeVisible();
        await expectNothingWiderThanTheScreen(page);
      });
    });
  }
});
