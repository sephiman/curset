import { expect, test, type Page } from "@playwright/test";
import { AEAT, overflowingElements, signIn } from "./session";

/** Publication of aeat-agentes-hacienda (theory only) at the two widths of the brief. */

const TITLE = "Agentes de la Hacienda Pública (C1)";
const TAX_LESSON = `/courses/${AEAT}/lessons/m03-l03`;
const WIDTHS = [
  { label: "390 px", use: { viewport: { width: 390, height: 800 }, isMobile: true, hasTouch: true, deviceScaleFactor: 2 } },
  { label: "1280 px", use: { viewport: { width: 1280, height: 800 } } },
] as const;

async function expectNothingWiderThanTheScreen(page: Page): Promise<void> {
  await page.waitForLoadState("networkidle");
  expect(await overflowingElements(page)).toEqual([]);
}

for (const { label, use } of WIDTHS) {
  test.describe(`aeat-agentes-hacienda at ${label}`, () => {
    test.use(use);

    test("the selector lists four courses and marks this one", async ({ page }) => {
      await signIn(page, AEAT);
      await page.goto(`/courses/${AEAT}`);
      await page.getByRole("button", { name: /Cambiar de curso/ }).click();
      const dialog = page.getByRole("dialog");
      await expect(dialog.getByRole("listitem")).toHaveCount(4);
      await expect(dialog.getByRole("button", { name: /Agentes de la Hacienda Pública \(C1\)/ })).toHaveAttribute(
        "aria-current",
        "true",
      );
      await expectNothingWiderThanTheScreen(page);
    });

    test("the course page lists the temas and offers no practice", async ({ page }) => {
      await signIn(page, AEAT);
      await page.goto(`/courses/${AEAT}`);
      await expect(page.getByRole("heading", { level: 1 })).toContainText(TITLE);
      await expect(page.getByText(/\d+ ejercicios/i)).toHaveCount(0);
      await expect(page.getByRole("button", { name: "Exportar PDF" })).toBeVisible();
      await expectNothingWiderThanTheScreen(page);
    });

    test("a tax lesson shows its esquemas and a worked example, with no «Practicar»", async ({ page }) => {
      await signIn(page, AEAT);
      await page.goto(TAX_LESSON);
      await expect(page.getByRole("heading", { level: 1 })).toContainText("Derecho Tributario");
      await expect(
        page.getByText("Algunas reglas del artículo 27 LGT sobre los recargos por declaración extemporánea").first(),
      ).toBeVisible();
      await expect(page.getByRole("heading", { name: "Ejemplo: recargo con menos de 12 meses de retraso" })).toBeVisible();
      await expect(page.getByRole("link", { name: "Practicar" })).toHaveCount(0);
      await expect(page.getByRole("button", { name: "Practicar" })).toHaveCount(0);
      await expectNothingWiderThanTheScreen(page);
    });

    test("Exámenes shows the default page with no button", async ({ page }) => {
      await signIn(page, AEAT);
      await page.goto(`/courses/${AEAT}/exams`);
      await expect(page.getByText("Este curso todavía no tiene exámenes")).toBeVisible();
      await expect(page.getByText("La teoría está completa.")).toBeVisible();
      await expect(page.getByRole("main").getByRole("button")).toHaveCount(0);
      await expectNothingWiderThanTheScreen(page);
    });

    test("Progreso shows reading progress only", async ({ page }) => {
      await signIn(page, AEAT);
      await page.goto(`/courses/${AEAT}/stats`);
      await expect(page.getByText("Lecciones marcadas como leídas")).toBeVisible();
      await expect(page.getByText("Por tema")).toHaveCount(0);
      await expect(page.getByText("Respuestas")).toHaveCount(0);
      await expectNothingWiderThanTheScreen(page);
    });
  });
}

test("the course PDF exports", async ({ page }) => {
  test.setTimeout(600_000);
  await signIn(page, AEAT);
  await page.goto(`/courses/${AEAT}`);
  const download = page.waitForEvent("download", { timeout: 540_000 });
  await page.getByRole("button", { name: "Exportar PDF" }).click();
  const file = await download;
  expect(file.suggestedFilename()).toMatch(/\.pdf$/);
  const path = await file.path();
  const { statSync } = await import("node:fs");
  expect(statSync(path).size).toBeGreaterThan(100_000);
});
