import { expect, test, type Page } from "@playwright/test";

/** Delta N4: the spaced practice scheduler, through the real UI of the opted-in fixture course. */

const TECH = "fixture-tecnico";
const API = `/api/courses/${TECH}`;
const PRACTICE = `/courses/${TECH}/lessons/m01-l1/practice`;
const PROMPTS = {
  isolation: "Which isolation level does the default PostgreSQL session use?",
  failing: "What does a test that cannot fail tell you?",
  fix: "Which statement prevents a lost update in a single step?",
};
const WRONG = {
  [PROMPTS.isolation]: "Serializable.",
  [PROMPTS.failing]: "That the system is reliable.",
  [PROMPTS.fix]: "Caching the balance in the application.",
};

async function newLearner(page: Page, viewportName: string): Promise<void> {
  const email = `e2e-sched-${viewportName}-${Date.now()}@example.com`;
  const password = "E2e-scheduler-2026!";
  const register = await page.request.post("/api/auth/register", {
    data: { email, password, name: "e2e-sched", locale: "en", courses: [TECH] },
  });
  expect(register.ok(), await register.text()).toBe(true);
  const login = await page.request.post("/api/auth/login", { data: { email, password } });
  expect(login.ok(), await login.text()).toBe(true);
}

async function startRound(page: Page): Promise<void> {
  await page.goto(PRACTICE);
  await page.getByRole("radio", { name: /^All \(3\)$/ }).check({ force: true });
  await page.getByRole("button", { name: "Start" }).click();
  await expect(page.getByText(/^Question 1 of 3$/)).toBeVisible();
}

async function shownOptions(page: Page): Promise<string[]> {
  const labels = page.getByRole("radio").locator("xpath=ancestor::label");
  return (await labels.allInnerTexts()).map((text) => text.trim());
}

async function currentPrompt(page: Page): Promise<string> {
  for (const text of Object.values(PROMPTS)) {
    if ((await page.getByText(text, { exact: true }).count()) > 0) return text;
  }
  throw new Error("no known question on screen");
}

/** The question at `position`, once it is open (its four options are on screen). */
async function questionAt(page: Page, position: number): Promise<string> {
  await expect(page.getByText(`Question ${position} of 3`, { exact: true })).toBeVisible();
  await expect(page.getByRole("radio")).toHaveCount(4);
  return currentPrompt(page);
}

async function answerAndGoOn(page: Page, optionText: string | null): Promise<void> {
  const labels = page.getByRole("radio").locator("xpath=ancestor::label");
  await (optionText === null ? labels.first() : labels.filter({ hasText: optionText })).click();
  await page.getByRole("button", { name: "Submit" }).click();
  await page.getByRole("button", { name: /^(Next|Finish)/ }).click();
}

for (const [name, viewport, mobile] of [
  ["390 px", { width: 390, height: 800 }, true],
  ["1280 px", { width: 1280, height: 800 }, false],
] as const) {
  test.describe(`at ${name}`, () => {
    test.use({ viewport, isMobile: mobile, hasTouch: mobile, storageState: { cookies: [], origins: [] } });

    test("a question's options keep their order on reload", async ({ page }) => {
      await newLearner(page, `a-${viewport.width}`);
      const opened = page.waitForResponse((r) => r.request().method() === "POST" && r.url().includes("/exercises/m01-ex-1/attempts"));
      await startRound(page);
      const attempt = (await (await opened).json()) as { attemptId: string };
      const onScreen = await shownOptions(page);
      expect(onScreen).toHaveLength(4);
      // The UI drops an in-progress round on reload, so the reloaded attempt is read through the API.
      await page.reload();
      const reloaded = await page.request.get(`${API}/attempts/${attempt.attemptId}`);
      expect(reloaded.ok(), await reloaded.text()).toBe(true);
      const options = ((await reloaded.json()) as { payload: { options: { text: string }[] } }).payload.options;
      expect(options.map((option) => option.text)).toEqual(onScreen);
    });

    test("a round serves unseen questions before a failed one, which waits for its return day", async ({ page }) => {
      await newLearner(page, `b-${viewport.width}`);

      await startRound(page);
      const failed = await questionAt(page, 1);
      await answerAndGoOn(page, WRONG[failed]);
      await expect(page.getByText("Question 2 of 3", { exact: true })).toBeVisible();

      // Leave the round with two questions unseen, then draw the next one the same day.
      await startRound(page);
      const second = await questionAt(page, 1);
      await answerAndGoOn(page, null);
      const third = await questionAt(page, 2);
      await answerAndGoOn(page, null);
      expect(new Set([failed, second, third]).size).toBe(3);
      expect(await questionAt(page, 3)).toBe(failed);
    });
  });
}
