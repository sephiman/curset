import { expect, test, type Page } from "@playwright/test";
import { CRYPTO, signIn } from "./session";

/**
 * Delta N: the three export buttons, the dialog's exercise line per the Cuenta switch, and the scope each
 * one asks the server for. The PDF itself is never made here: the export request is recorded and aborted.
 */

const COURSE = `/courses/${CRYPTO}`;

async function setSwitch(page: Page, include: boolean): Promise<void> {
  const response = await page.request.patch("/api/auth/me", { data: { pdf_exercises: include } });
  expect(response.ok(), await response.text()).toBe(true);
}

/** Records the scope of the next export request and aborts it, so nothing is typeset. */
async function recordExport(page: Page): Promise<() => Promise<string | null>> {
  let resolve: (scope: string | null) => void = () => {};
  const asked = new Promise<string | null>((done) => {
    resolve = done;
  });
  await page.route(`**/api/courses/${CRYPTO}/export?**`, async (route) => {
    resolve(new URL(route.request().url()).searchParams.get("scope"));
    await route.abort();
  });
  return () => asked;
}

for (const [name, viewport, phone] of [
  ["390 px", { width: 390, height: 800 }, true],
  ["1280 px", { width: 1280, height: 800 }, false],
] as const) {
  test.describe(`PDF export at ${name}`, () => {
    test.use({ viewport });

    /** The page's own export: a page button, or on phones an entry in the avatar menu. */
    async function openPageExport(page: Page, label: string): Promise<void> {
      if (phone) {
        // The avatar button is named for the account (global-setup signs up «e2e-mobile»).
        await page.getByRole("banner").getByRole("button", { name: "e2e-mobile", exact: true }).click();
        await page.getByRole("menuitem", { name: label }).click();
      } else {
        await page.getByRole("main").getByRole("button", { name: label, exact: true }).click();
      }
    }

    test("the lesson's «Exportar PDF» says «Solo teoría» with the switch off and asks for the tema", async ({ page }) => {
      await signIn(page, CRYPTO);
      await setSwitch(page, false);
      await page.goto(`${COURSE}/lessons/m03-l1`);
      await openPageExport(page, "Exportar PDF");
      const dialog = page.getByRole("dialog", { name: "Exportar PDF" });
      await expect(dialog.getByText("Solo teoría")).toBeVisible();
      await expect(dialog.getByRole("link", { name: "Cambiar en Cuenta" })).toHaveAttribute("href", "/account");
      const scope = await recordExport(page);
      await dialog.getByRole("button", { name: "Exportar", exact: true }).click();
      expect(await scope()).toBe("m03-l1");
    });

    test("the module's «Exportar PDF del bloque» says «Con ejercicios» with the switch on and asks for the bloque", async ({
      page,
    }) => {
      await signIn(page, CRYPTO);
      await setSwitch(page, true);
      await page.goto(`${COURSE}/modules/m03`);
      await openPageExport(page, "Exportar PDF del bloque");
      const dialog = page.getByRole("dialog", { name: "Exportar PDF del bloque" });
      await expect(dialog.getByText("Con ejercicios")).toBeVisible();
      const scope = await recordExport(page);
      await dialog.getByRole("button", { name: "Exportar", exact: true }).click();
      expect(await scope()).toBe("m03");
      await setSwitch(page, false);
    });

    test("each module card's menu offers its bloque", async ({ page }) => {
      await signIn(page, CRYPTO);
      await setSwitch(page, false);
      await page.goto(COURSE);

      await page.getByRole("button", { name: "Más acciones de M03" }).click();
      await page.getByRole("menuitem", { name: "Exportar PDF del bloque" }).click();
      const dialog = page.getByRole("dialog", { name: "Exportar PDF del bloque" });
      await expect(dialog.getByText("Solo teoría")).toBeVisible();
      const scope = await recordExport(page);
      await dialog.getByRole("button", { name: "Exportar", exact: true }).click();
      expect(await scope()).toBe("m03");
    });

    test("the course page's «Exportar PDF» asks for the whole course, with no scope", async ({ page }) => {
      await signIn(page, CRYPTO);
      await setSwitch(page, false);
      await page.goto(COURSE);
      await openPageExport(page, "Exportar PDF");
      const dialog = page.getByRole("dialog", { name: "Exportar PDF" });
      await expect(dialog.getByText("Solo teoría")).toBeVisible();
      const scope = await recordExport(page);
      await dialog.getByRole("button", { name: "Exportar", exact: true }).click();
      expect(await scope()).toBeNull();
    });
  });
}
