import { expect, test, type Page } from "@playwright/test";
import { AEAT, AGE, AGE_C2, CRYPTO, overflowingElements } from "./session";

/** Delta v2.1 section M: a published course with no exercises and no exams, at 390 and 1280 px. */

const THEORY = "fixture-teoria";
const TITLE = "Teoría sin ejercicios de prueba";
const LESSON = `/courses/${THEORY}/lessons/m01-l1`;

async function selectTheoryCourse(page: Page): Promise<void> {
  const courses = await page.request.put("/api/me/courses", {
    data: { active: [AGE, CRYPTO, AGE_C2, AEAT, THEORY], selected: THEORY },
  });
  expect(courses.ok(), await courses.text()).toBe(true);
}

async function expectNothingWiderThanTheScreen(page: Page): Promise<void> {
  await page.waitForLoadState("networkidle");
  expect(await overflowingElements(page)).toEqual([]);
}

for (const [name, viewport] of [
  ["390 px", { width: 390, height: 800 }],
  ["1280 px", { width: 1280, height: 800 }],
] as const) {
  test.describe(`at ${name}`, () => {
    test.use({ viewport });

    test("the course page lists its lessons and offers no practice", async ({ page }) => {
      await selectTheoryCourse(page);
      await page.goto(`/courses/${THEORY}`);
      await expect(page.getByRole("heading", { level: 1 })).toContainText(TITLE);
      await expect(page.getByRole("link", { name: "M01 · Los plazos" })).toBeVisible();
      await expect(page.getByText(/\d+ ejercicios/i)).toHaveCount(0);
      await expect(page.getByRole("link", { name: /Psicotécnicos/ })).toHaveCount(0);
      await expectNothingWiderThanTheScreen(page);
    });

    test("a lesson has no «Practicar»", async ({ page }) => {
      await selectTheoryCourse(page);
      await page.goto(LESSON);
      await expect(page.getByRole("heading", { level: 1 })).toContainText("Plazos por días");
      await expect(page.getByText("Practicar")).toHaveCount(0);
      await expectNothingWiderThanTheScreen(page);
    });

    test("Exámenes says there are no exams yet and the theory is complete, with no button", async ({ page }) => {
      await selectTheoryCourse(page);
      await page.goto(`/courses/${THEORY}/exams`);
      await expect(page.getByText("Este curso todavía no tiene exámenes")).toBeVisible();
      await expect(page.getByText("La teoría está completa.")).toBeVisible();
      await expect(page.getByRole("main").getByRole("button")).toHaveCount(0);
      await expectNothingWiderThanTheScreen(page);
    });

    test("Progreso shows reading progress only", async ({ page }) => {
      await selectTheoryCourse(page);
      await page.goto(`/courses/${THEORY}/stats`);
      await expect(page.getByText("Lecciones marcadas como leídas")).toBeVisible();
      await expect(page.getByText("0/2")).toBeVisible();
      await expect(page.getByText("Por tema")).toHaveCount(0);
      await expect(page.getByText("Respuestas")).toHaveCount(0);
      await expect(page.getByRole("table")).toHaveCount(0);
      await expectNothingWiderThanTheScreen(page);
    });

    test("the course selector and the account list it", async ({ page }) => {
      await selectTheoryCourse(page);
      await page.goto(`/courses/${THEORY}`);
      await page.getByRole("button", { name: new RegExp(`Curso: ${TITLE}`) }).click();
      await expect(page.getByRole("dialog").getByText(TITLE)).toBeVisible();
      await page.keyboard.press("Escape");
      await page.goto("/account");
      await expect(page.getByText(TITLE).first()).toBeVisible();
      await expectNothingWiderThanTheScreen(page);
    });
  });
}

test.describe("signing up", () => {
  test.use({ storageState: { cookies: [], origins: [] } });

  for (const width of [390, 1280]) {
    test(`lists it among the courses at ${width} px`, async ({ page }) => {
      await page.setViewportSize({ width, height: 800 });
      await page.goto("/register");
      await page.getByLabel("Correo electrónico").fill(`e2e-theory-${width}@example.com`);
      await page.getByLabel("Contraseña").fill("E2e-theory-list-2026!");
      await page.getByRole("button", { name: "Continuar" }).click();
      await expect(page.getByRole("checkbox", { name: new RegExp(TITLE) })).toBeVisible();
      await expectNothingWiderThanTheScreen(page);
    });
  }
});
