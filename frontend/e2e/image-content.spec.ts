import { expect, test } from "@playwright/test";
import { AEAT, AGE, AGE_C2, CRYPTO, signIn, startPracticeAndPickFirstOption } from "./session";

/** The backend image keeps serving what readers need once the unread source folders are left out of it. */

const TEMA = { course: AEAT, lesson: "m03-l04" };
const TECH = "backend-in-depth";
const DIAGRAM_CAPTION = "Changes are logged in the WAL before the data files are written";

test("a review's solution panel links a saved source the image still serves", async ({ page }) => {
  await signIn(page, TEMA.course);
  const api = page.request;
  const started = await api.post(`/api/courses/${TEMA.course}/exams`, {
    data: { presetId: "tema", target: TEMA.lesson, seed: 3 },
  });
  expect(started.ok(), await started.text()).toBe(true);
  const { id } = (await started.json()) as { id: string };
  const submit = await api.post(`/api/courses/${TEMA.course}/exams/${id}/submit`, { data: {} });
  expect(submit.ok(), await submit.text()).toBe(true);
  const review = (await (await api.get(`/api/courses/${TEMA.course}/exams/${id}/review`)).json()) as {
    questions: { index: number; excerpt?: { href: string } | null }[];
  };
  const known = review.questions.find((q) => q.excerpt?.href.startsWith(`/api/courses/${TEMA.course}/sources/`));
  if (!known?.excerpt) throw new Error(`no question of the ${TEMA.lesson} sitting links a served source`);

  await page.goto(`/courses/${TEMA.course}/exams/${id}/review`);
  const panel = page.locator("details", { has: page.getByText("Ver solución") }).nth(known.index);
  await panel.locator("summary").click();
  const link = panel.getByRole("link", { name: /^(Texto consolidado|Página guardada)$/ });
  await expect(link).toBeVisible();
  await expect(link).toHaveAttribute("href", known.excerpt.href);

  const served = await api.get(known.excerpt.href.split("#")[0]);
  expect(served.status()).toBe(200);
  expect((await served.body()).length).toBeGreaterThan(0);
});

test("backend-in-depth still renders a lesson diagram and shows a question's citation", async ({ page }) => {
  const courses = await page.request.put("/api/me/courses", {
    data: { active: [AGE, CRYPTO, AGE_C2, AEAT, TECH], selected: TECH },
  });
  expect(courses.ok(), await courses.text()).toBe(true);

  await page.goto(`/courses/${TECH}/lessons/m06-l01`);
  await expect(page.getByRole("region", { name: DIAGRAM_CAPTION }).locator("svg")).toBeVisible();

  // The drawn question's panel opens by itself and shows its cited source: an excerpt or the reason for none, plus a source link.
  await page.goto(`/courses/${TECH}/lessons/m01-l01/practice`);
  await startPracticeAndPickFirstOption(page);
  await page.getByRole("button", { name: "Enviar" }).click();
  const panel = page.locator("details", { has: page.getByText("Ver solución") });
  await expect(panel).toHaveAttribute("open", "");
  await expect(panel.locator("figcaption").or(panel.getByText(/^Sin extracto/)).first()).toBeVisible();
  const source = panel.getByRole("navigation").getByRole("link").first();
  await expect(source).toBeVisible();
  await expect(source).toHaveAttribute("href", /.+/);
});
