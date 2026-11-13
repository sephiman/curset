import { expect, test, type Page } from "@playwright/test";
import { AEAT, AGE, AGE_C2, abandonSitting, overflowingElements, signIn, startSitting, submittedSitting, startPracticeAndPickFirstOption } from "./session";

/** Round R5 of age-auxiliar-c2 at the two widths of the brief: what jsdom cannot measure. */

const WIDTHS = [
  { label: "390 px", use: { viewport: { width: 390, height: 800 }, isMobile: true, hasTouch: true, deviceScaleFactor: 2 } },
  { label: "1280 px", use: { viewport: { width: 1280, height: 800 } } },
] as const;

async function expectNothingWiderThanTheScreen(page: Page): Promise<void> {
  await page.waitForLoadState("networkidle");
  expect(await overflowingElements(page)).toEqual([]);
}

for (const { label, use } of WIDTHS) {
  test.describe(`age-auxiliar-c2 at ${label}`, () => {
    test.use(use);

    test("the selector shows four courses and marks the three Spanish-only ones", async ({ page }) => {
      await signIn(page, AGE_C2);
      await page.goto(`/courses/${AGE_C2}`);
      await page.getByRole("button", { name: /Cambiar de curso/ }).click();
      const dialog = page.getByRole("dialog");
      await expect(dialog.getByRole("listitem")).toHaveCount(4);
      await expect(dialog.getByRole("button", { name: /Auxiliar Administrativo del Estado \(C2\)/ })).toHaveAttribute(
        "aria-current",
        "true",
      );
      await expect(dialog.getByText("Solo en español")).toHaveCount(3);
      await expectNothingWiderThanTheScreen(page);
    });

    test("the course page offers the Psicotécnicos practice and fits the screen", async ({ page }) => {
      await signIn(page, AGE_C2);
      await page.goto(`/courses/${AGE_C2}`);
      await expect(page.getByRole("heading", { level: 1 })).toContainText("Auxiliar Administrativo del Estado (C2)");
      await expect(page.getByRole("link", { name: /Psicotécnicos/ }).first()).toBeVisible();
      await expectNothingWiderThanTheScreen(page);
    });

    test("a Psicotécnicos round shows the rule after the answer", async ({ page }) => {
      await signIn(page, AGE_C2);
      await page.goto(`/courses/${AGE_C2}/practice/psicotecnicos`);
      await startPracticeAndPickFirstOption(page);
      await page.getByRole("button", { name: "Enviar" }).click();
      await expect(page.getByText("Ver solución")).toBeVisible();
      await expectNothingWiderThanTheScreen(page);
    });

    test("a tema's practice opens the solution panel", async ({ page }) => {
      await signIn(page, AGE_C2);
      await page.goto(`/courses/${AGE_C2}/lessons/m01-l01/practice`);
      await startPracticeAndPickFirstOption(page);
      await page.getByRole("button", { name: "Enviar" }).click();
      await expect(page.getByText("Ver solución")).toBeVisible();
      await expectNothingWiderThanTheScreen(page);
    });

    test("the simulation sitting hides the tema, labels options A to D and has no pause", async ({ page }) => {
      await signIn(page, AGE_C2);
      const sitting = await startSitting(page.request, AGE_C2, "simulacro");
      try {
        await page.goto(`/courses/${AGE_C2}/exams/${sitting.id}`);
        await expect(page.getByRole("radio").first()).toBeVisible();
        await expect(page.getByText(/Tema [IVX]+\./)).toHaveCount(0);
        for (const letter of ["A", "B", "C", "D"]) {
          await expect(page.getByRole("radio", { name: new RegExp(`^${letter}\\)`) })).toBeVisible();
        }
        await expect(page.getByRole("button", { name: /Pausa|Pausar/ })).toHaveCount(0);
        await expectNothingWiderThanTheScreen(page);
      } finally {
        await abandonSitting(page.request, AGE_C2, sitting.id);
      }
    });

    test("the results list the psicotécnico types in «Por tema»", async ({ page }) => {
      await signIn(page, AGE_C2);
      const id = await submittedSitting(page.request, AGE_C2, "simulacro");
      await page.goto(`/courses/${AGE_C2}/exams/${id}/review`);
      await expect(page.getByRole("heading", { name: "Por tema" })).toBeVisible();
      await expect(page.getByText("Lectura de tablas").first()).toBeVisible();
      // The review names what the sitting hid: the tema of a bloque question, the type of a psicotécnico.
      await expect(page.getByText(/· Tema I\.\d+ · /).first()).toBeVisible();
      await expect(page.getByText(/^· (Lectura de tablas|Sinónimos|Antónimos|Series numéricas)/).first()).toBeVisible();
      await expectNothingWiderThanTheScreen(page);
    });
  });
}

interface ReviewedQuestion {
  index: number;
  questionId: string | null;
  excerpt?: { heading: string } | null;
}

// A pinned «Tema» sitting per oposiciones course: its first question with an excerpt is the known one. A bank edit
// may change the draw; the test then still finds the first question with an excerpt in the same tema.
for (const { course, lesson } of [
  { course: AGE, lesson: "m01-l01" },
  { course: AGE_C2, lesson: "m01-l01" },
  { course: AEAT, lesson: "m03-l04" },
]) {
  test(`the review's solution panel shows the excerpt of a known question in ${course}`, async ({ page }) => {
    await signIn(page, course);
    const api = page.request;
    const started = await api.post(`/api/courses/${course}/exams`, { data: { presetId: "tema", target: lesson, seed: 3 } });
    expect(started.ok(), await started.text()).toBe(true);
    const { id } = (await started.json()) as { id: string };
    const submit = await api.post(`/api/courses/${course}/exams/${id}/submit`, { data: {} });
    expect(submit.ok(), await submit.text()).toBe(true);
    const review = (await (await api.get(`/api/courses/${course}/exams/${id}/review`)).json()) as {
      questions: ReviewedQuestion[];
    };
    const known = review.questions.find((q) => q.excerpt);
    if (!known?.excerpt) throw new Error(`no question of the ${lesson} sitting carries an excerpt`);

    await page.goto(`/courses/${course}/exams/${id}/review`);
    const panel = page.locator("details", { has: page.getByText("Ver solución") }).nth(known.index);
    await panel.locator("summary").click();
    await expect(panel.locator("figcaption")).toHaveText(known.excerpt.heading);
  });
}

test("sign-up offers the five courses", async ({ browser }) => {
  const context = await browser.newContext({ storageState: { cookies: [], origins: [] } });
  const page = await context.newPage();
  await page.goto("/register");
  await page.getByLabel("Correo electrónico").fill("e2e-signup-list@example.com");
  await page.getByLabel("Contraseña").fill("E2e-signup-list-2026!");
  await page.getByRole("button", { name: "Continuar" }).click();
  const choices = page.getByRole("group", { name: "¿Qué cursos te interesan?" });
  await expect(choices.getByRole("checkbox")).toHaveCount(5);
  await expect(choices).toContainText("Auxiliar Administrativo del Estado (C2)");
  await expect(choices).toContainText("Administrativo del Estado (C1)");
  await expect(choices.getByText("Solo en español")).toHaveCount(4);
  await context.close();
});

test("Cuenta › Cursos lists the five courses, four of them active", async ({ page }) => {
  await signIn(page, AGE_C2);
  await page.goto("/account");
  const section = page.locator("#courses");
  await expect(section.getByRole("heading", { name: "Cursos" })).toBeVisible();
  await expect(section.getByRole("switch")).toHaveCount(5);
  // The theory-only test course is served beside the four real ones, and `signIn` leaves it inactive.
  await expect(section.getByRole("switch", { checked: true })).toHaveCount(4);
  await expect(section).toContainText("Auxiliar Administrativo del Estado (C2)");
});
