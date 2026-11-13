import { expect, test, type Locator, type Page } from "@playwright/test";
import { AGE, AGE_C2, CRYPTO, abandonSitting, overflowingElements, signIn, startSitting, submittedSitting } from "./session";

/** Delta J at real widths: what jsdom cannot measure — fit, scrolling and what is on screen without it. */

const PHONES = [360, 390, 430] as const;
const ESQUEMA_LESSON = `/courses/${AGE}/lessons/m01-l03`;
// The header tabs (768 px and up) carry the same name; the bottom bar is the one outside the header.
const tabBar = (page: Page) => page.locator('nav[aria-label="Secciones"]:not(header nav)');

function phone(width: number) {
  return { viewport: { width, height: 800 }, isMobile: true, hasTouch: true, deviceScaleFactor: 2 };
}

const TYPICAL_FIRST_QUESTION_SEED = 7;
// This draw includes m06-l05-q158, whose stem holds an Excel formula with no break opportunity.
const LONG_FORMULA_SEED = 1;
const LONG_FORMULA = "=SI(Y(NO(B14<B7);NO(C14<B5));B14*B8;0)";

/** The question's stem on screen, found by its opening words. */
function stem(page: Page, prompt: string): Locator {
  return page.locator("main p").filter({ hasText: prompt.slice(0, 40) }).first();
}

/** Where Anterior/Siguiente begin: everything the reader sees without scrolling sits above this line. */
async function buttonsTop(page: Page): Promise<number> {
  const box = await page.getByRole("button", { name: /Siguiente/ }).boundingBox();
  expect(box).not.toBeNull();
  return box!.y;
}

async function expectAbove(locator: Locator, line: number): Promise<void> {
  await expect(locator).toBeVisible();
  const box = await locator.boundingBox();
  expect(box!.y + box!.height).toBeLessThanOrEqual(line);
}

async function expectNothingWiderThanTheScreen(page: Page): Promise<void> {
  await page.waitForLoadState("networkidle");
  expect(await overflowingElements(page)).toEqual([]);
}

test.describe("tab bar", () => {
  for (const course of [AGE, AGE_C2, CRYPTO]) {
    test.describe(`on ${course}`, () => {
      test.use(phone(360));
      test("is at the bottom at 360 px", async ({ page }) => {
        await signIn(page, course);
        await page.goto(`/courses/${course}`);
        const bar = tabBar(page);
        await expect(bar).toBeVisible();
        expect((await bar.boundingBox())?.y).toBeGreaterThan(700);
      });
    });
    test.describe(`on ${course} at desktop width`, () => {
      test.use({ viewport: { width: 1024, height: 800 } });
      test("is absent at 1024 px", async ({ page }) => {
        await signIn(page, course);
        await page.goto(`/courses/${course}`);
        await expect(page.getByRole("banner").getByRole("link", { name: "Exámenes" })).toBeVisible();
        await expect(tabBar(page)).toHaveCount(0);
      });
    });
  }
});

test.describe("esquema", () => {
  test.describe("at 800 px", () => {
    test.use({ viewport: { width: 800, height: 900 } });
    test("tabla stays a table", async ({ page }) => {
      await signIn(page);
      await page.goto(ESQUEMA_LESSON);
      await expect(page.locator('figure[data-esquema="tabla"]').first().locator("table")).toBeVisible();
    });
  });
  test.describe("at 360 px", () => {
    test.use(phone(360));
    test("tabla becomes stacked cards, nothing clipped", async ({ page }) => {
      await signIn(page);
      await page.goto(ESQUEMA_LESSON);
      const esquema = page.locator('figure[data-esquema="tabla"]').first();
      await expect(esquema.getByRole("listitem").first()).toContainText("Acuerdo: ");
      await expect(esquema.locator("table")).toHaveCount(0);
      await expectNothingWiderThanTheScreen(page);
    });
  });
});

test.describe("simulation sitting at 360 px", () => {
  test.use(phone(360));

  test("shows the whole first question of a 70-question sitting without scrolling, with no tab bar", async ({ page }) => {
    await signIn(page);
    // A pinned draw whose first question is of median length among seeds 1–40 (the longest do not fit at
    // 360 × 800). A bank edit changes the draw: re-pick the seed then (re-picked 2026-11-06, was 27).
    const sitting = await startSitting(page.request, AGE, "parte-1", TYPICAL_FIRST_QUESTION_SEED);
    try {
      expect(sitting.questions.filter((q) => !q.reserve)).toHaveLength(70);
      await page.goto(`/courses/${AGE}/exams/${sitting.id}`);
      const options = page.getByRole("radio");
      await expect(options).toHaveCount(4);
      const navTop = await buttonsTop(page);
      await expectAbove(stem(page, sitting.questions[0].prompt), navTop);
      for (let i = 0; i < 4; i += 1) await expectAbove(options.nth(i).locator("xpath=ancestor::label"), navTop);
      expect(await page.evaluate(() => window.scrollY)).toBe(0);
      await expect(tabBar(page)).toHaveCount(0);
    } finally {
      await abandonSitting(page.request, AGE, sitting.id);
    }
  });

  test("shows the stem and the first two options of any first question without scrolling", async ({ page }) => {
    await signIn(page);
    const sitting = await startSitting(page.request, AGE, "parte-1");
    try {
      await page.goto(`/courses/${AGE}/exams/${sitting.id}`);
      const options = page.getByRole("radio");
      await expect(options).toHaveCount(4);
      const navTop = await buttonsTop(page);
      await expectAbove(stem(page, sitting.questions[0].prompt), navTop);
      for (let i = 0; i < 2; i += 1) await expectAbove(options.nth(i).locator("xpath=ancestor::label"), navTop);
      expect(await page.evaluate(() => window.scrollY)).toBe(0);
    } finally {
      await abandonSitting(page.request, AGE, sitting.id);
    }
  });

  test("brings the tab bar back on the results", async ({ page }) => {
    await signIn(page);
    const id = await submittedSitting(page.request, AGE, "parte-1");
    await page.goto(`/courses/${AGE}/exams/${id}/review`);
    await expect(tabBar(page)).toBeVisible();
  });
});

test.describe("nothing wider than the screen", () => {
  for (const width of PHONES) {
    test.describe(`at ${width} px`, () => {
      test.use(phone(width));

      test("Exámenes, every course", async ({ page }) => {
        for (const course of [AGE, AGE_C2, CRYPTO]) {
          await signIn(page, course);
          await page.goto(`/courses/${course}/exams`);
          await expect(page.getByRole("heading", { level: 1 })).toBeVisible();
          await expectNothingWiderThanTheScreen(page);
        }
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
        await page.getByRole("button", { name: "Empezar" }).click();
        await page.getByRole("radio").first().locator("xpath=ancestor::label").click();
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

      test("a stem with a long formula wraps in the CI runner's wider font", async ({ page }) => {
        await signIn(page);
        const id = await submittedSitting(page.request, AGE, "simulacro", { seed: LONG_FORMULA_SEED });
        await page.goto(`/courses/${AGE}/exams/${id}/review`);
        await page.addStyleTag({ content: '* { font-family: "DejaVu Sans" !important; }' });
        await expect(page.getByText(LONG_FORMULA).first()).toBeVisible();
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
