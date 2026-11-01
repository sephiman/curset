import { expect, test, type Page } from "@playwright/test";
import { AGE, CRYPTO, abandonSitting, overflowingElements, signIn, startSitting, submittedSitting } from "./session";

/** Delta J at real widths: what jsdom cannot measure — fit, scrolling and what is on screen without it. */

const PHONES = [360, 390, 430] as const;
const ESQUEMA_LESSON = `/courses/${AGE}/lessons/m01-l03`;
const tabBar = (page: Page) => page.getByRole("navigation", { name: "Secciones" });

function phone(width: number) {
  return { viewport: { width, height: 800 }, isMobile: true, hasTouch: true, deviceScaleFactor: 2 };
}

async function expectNothingWiderThanTheScreen(page: Page): Promise<void> {
  await page.waitForLoadState("networkidle");
  expect(await overflowingElements(page)).toEqual([]);
}

test.describe("tab bar", () => {
  for (const course of [AGE, CRYPTO]) {
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
    const sitting = await startSitting(page.request, AGE, "parte-1");
    try {
      expect(sitting.questions.filter((q) => !q.reserve)).toHaveLength(70);
      await page.goto(`/courses/${AGE}/exams/${sitting.id}`);
      const options = page.getByRole("radio");
      await expect(options).toHaveCount(4);
      const navigation = page.getByRole("button", { name: /Siguiente/ });
      const lastOption = await options.last().locator("xpath=ancestor::label").boundingBox();
      const navTop = (await navigation.boundingBox())?.y ?? 0;
      expect(lastOption).not.toBeNull();
      expect(lastOption!.y + lastOption!.height).toBeLessThanOrEqual(navTop);
      expect(await page.evaluate(() => window.scrollY)).toBe(0);
      await expect(tabBar(page)).toHaveCount(0);
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

      test("Exámenes, both courses", async ({ page }) => {
        for (const course of [AGE, CRYPTO]) {
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
