import { expect, test, type Page } from "@playwright/test";
import { AEAT, abandonSitting, activeCourses, catalogue, overflowingElements, signIn, startSitting, submittedSitting, startPracticeAndPickFirstOption } from "./session";

/** aeat-agentes-hacienda at the two widths of the brief: theory, and since round R5 the first-exercise bank, presets and official sets. */

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

    test("the selector lists the active courses and marks this one", async ({ page }) => {
      await signIn(page, AEAT);
      const active = activeCourses(await catalogue(page.request));
      await page.goto(`/courses/${AEAT}`);
      await page.getByRole("button", { name: /Cambiar de curso/ }).click();
      const dialog = page.getByRole("dialog");
      await expect(dialog.getByRole("listitem")).toHaveCount(active.length);
      await expect(dialog.getByRole("button", { name: /Agentes de la Hacienda Pública \(C1\)/ })).toHaveAttribute(
        "aria-current",
        "true",
      );
      await expectNothingWiderThanTheScreen(page);
    });

    test("the course page lists the temas and fits the screen", async ({ page }) => {
      await signIn(page, AEAT);
      await page.goto(`/courses/${AEAT}`);
      await expect(page.getByRole("heading", { level: 1 })).toContainText(TITLE);
      // The whole-course export: on the page from 768 px, in the avatar menu on phones (N1).
      if (label === "390 px") {
        await page.getByRole("banner").getByRole("button", { name: "e2e-mobile", exact: true }).click();
        await expect(page.getByRole("menuitem", { name: "Exportar PDF" })).toBeVisible();
        await page.keyboard.press("Escape");
      } else {
        await expect(page.getByRole("main").getByRole("button", { name: "Exportar PDF", exact: true })).toBeVisible();
      }
      await expectNothingWiderThanTheScreen(page);
    });

    test("a tax lesson shows its esquemas and a worked example, and offers «Practicar»", async ({ page }) => {
      await signIn(page, AEAT);
      await page.goto(TAX_LESSON);
      await expect(page.getByRole("heading", { level: 1 })).toContainText("Derecho Tributario");
      await expect(
        page.getByText("Algunas reglas del artículo 27 LGT sobre los recargos por declaración extemporánea").first(),
      ).toBeVisible();
      await expect(page.getByRole("heading", { name: "Ejemplo: recargo con menos de 12 meses de retraso" })).toBeVisible();
      await expect(page.getByRole("button", { name: "Practicar" }).first()).toBeVisible();
      await expectNothingWiderThanTheScreen(page);
    });

    test("a tema's practice opens the solution panel", async ({ page }) => {
      await signIn(page, AEAT);
      await page.goto(`/courses/${AEAT}/lessons/m03-l03/practice`);
      await startPracticeAndPickFirstOption(page);
      await page.getByRole("button", { name: "Enviar" }).click();
      await expect(page.getByText("Ver solución")).toBeVisible();
      await expectNothingWiderThanTheScreen(page);
    });

    test("Exámenes lists «Primer ejercicio», «Bloque», «Tema» and the official sets", async ({ page }) => {
      await signIn(page, AEAT);
      await page.goto(`/courses/${AEAT}/exams`);
      await expect(page.getByText("Este curso todavía no tiene exámenes")).toHaveCount(0);
      for (const title of ["Primer ejercicio", "Bloque", "Tema", "OEP 2025 · Tipo A", "OEP 2022 · Extraordinario", "OEP 2020 · Tipo B"]) {
        await expect(page.getByRole("heading", { level: 3, name: title, exact: true })).toBeVisible();
      }
      await expect(page.getByText("En 2025 el Tribunal fijó la nota de corte del sistema general en 41,00 puntos directos.")).toBeVisible();
      await expect(page.getByText(/Agencia Estatal de Administración Tributaria · Tribunal Calificador/).first()).toBeVisible();
      await expect(page.getByRole("button", { name: "Empezar" })).toHaveCount(14);
      await expectNothingWiderThanTheScreen(page);
    });

    test("the «Primer ejercicio» sitting has 80 questions, hides the tema, labels options A to D and has no pause", async ({
      page,
    }) => {
      await signIn(page, AEAT);
      const sitting = await startSitting(page.request, AEAT, "primer-ejercicio");
      try {
        expect(sitting.questions.filter((q) => !q.reserve)).toHaveLength(80);
        await page.goto(`/courses/${AEAT}/exams/${sitting.id}`);
        await expect(page.getByRole("radio").first()).toBeVisible();
        await expect(page.getByText(/Pregunta 1 de 80/)).toBeVisible();
        await expect(page.getByText(/Tema [IVX]+\./)).toHaveCount(0);
        for (const letter of ["A", "B", "C", "D"]) {
          await expect(page.getByRole("radio", { name: new RegExp(`^${letter}\\)`) })).toBeVisible();
        }
        await expect(page.getByRole("button", { name: /Pausa|Pausar/ })).toHaveCount(0);
        await expectNothingWiderThanTheScreen(page);
      } finally {
        await abandonSitting(page.request, AEAT, sitting.id);
      }
    });

    test("the results show the raw score, the mark out of 10 and «Por tema», and the review names the tema", async ({
      page,
    }) => {
      await signIn(page, AEAT);
      const id = await submittedSitting(page.request, AEAT, "primer-ejercicio");
      await page.goto(`/courses/${AEAT}/exams/${id}/review`);
      await expect(page.getByRole("heading", { name: "Por tema" })).toBeVisible();
      await expect(page.getByRole("columnheader", { name: "Directa" }).first()).toBeVisible();
      await expect(page.getByText(/ \/ 10$/).first()).toBeVisible();
      await expect(page.getByText(/· Tema (I|II|III)\.\d+ · /).first()).toBeVisible();
      await expectNothingWiderThanTheScreen(page);
    });

    test("an official set is sat as printed, with letters A to D, no tema and no pause, and its notes show in the review", async ({
      page,
    }) => {
      await signIn(page, AEAT);
      const sitting = await startSitting(page.request, AEAT, "conv2025-a");
      try {
        await page.goto(`/courses/${AEAT}/exams/${sitting.id}`);
        await expect(page.getByText(/Pregunta 1 de 79/)).toBeVisible();
        await expect(page.getByText(/El procedimiento legislativo ordinario/)).toBeVisible();
        await expect(page.getByText(/Tema [IVX]+\./)).toHaveCount(0);
        for (const letter of ["A", "B", "C", "D"]) {
          await expect(page.getByRole("radio", { name: new RegExp(`^${letter}\\)`) })).toBeVisible();
        }
        await expect(page.getByRole("button", { name: /Pausa|Pausar/ })).toHaveCount(0);
        await expectNothingWiderThanTheScreen(page);
      } finally {
        await abandonSitting(page.request, AEAT, sitting.id);
      }
      const id = await submittedSitting(page.request, AEAT, "conv2025-a");
      await page.goto(`/courses/${AEAT}/exams/${id}/review`);
      await expect(page.getByText("Clave oficial discutida").first()).toBeAttached();
      await expectNothingWiderThanTheScreen(page);
    });

    test("the first-exercise paper downloads as a PDF", async ({ page }) => {
      test.setTimeout(180_000);
      await signIn(page, AEAT);
      await page.goto(`/courses/${AEAT}/exams`);
      const download = page.waitForEvent("download", { timeout: 150_000 });
      await page.getByRole("button", { name: "Descargar PDF" }).first().click();
      const file = await download;
      expect(file.suggestedFilename()).toMatch(/\.pdf$/);
      const { statSync } = await import("node:fs");
      expect(statSync((await file.path()) ?? "").size).toBeGreaterThan(20_000);
    });

    test("Progreso shows the reading progress", async ({ page }) => {
      await signIn(page, AEAT);
      await page.goto(`/courses/${AEAT}/stats`);
      await expect(page.getByText("Lecciones marcadas como leídas")).toBeVisible();
      await expectNothingWiderThanTheScreen(page);
    });
  });
}

test("the course PDF export asks for the whole course, theory only", async ({ page }) => {
  // The PDF itself is never made in e2e (delta N8): the export request is recorded and aborted.
  await signIn(page, AEAT);
  const off = await page.request.patch("/api/auth/me", { data: { pdf_exercises: false } });
  expect(off.ok(), await off.text()).toBe(true);
  await page.goto(`/courses/${AEAT}`);
  await page.getByRole("main").getByRole("button", { name: "Exportar PDF", exact: true }).click();
  const dialog = page.getByRole("dialog", { name: "Exportar PDF" });
  await expect(dialog.getByText("Solo teoría")).toBeVisible();
  const asked = page.waitForRequest(`**/api/courses/${AEAT}/export?**`);
  await page.route(`**/api/courses/${AEAT}/export?**`, (route) => route.abort());
  await dialog.getByRole("button", { name: "Exportar", exact: true }).click();
  expect(new URL((await asked).url()).searchParams.get("scope")).toBeNull();
});
