import { expect, test, type Page } from "@playwright/test";

/** Question families: one practice set that mixes stored, variant-family and generated questions, capped per family. */

const COURSE = "fixture-familias";
const LESSON = `/courses/${COURSE}/lessons/m01-l1`;
const FAMILIES = {
  iso: [
    "Which isolation level lets a transaction read only committed rows?",
    "Which isolation level forbids a non-repeatable read of the same row?",
    "Which isolation level also forbids phantom rows in the standard?",
  ],
  tracing: [
    "What does the first fragment print after both writers ran?",
    "What does the second fragment print after the retry?",
    "What does the third fragment print after the rollback?",
  ],
};
const PLAIN = "What does a test that cannot fail tell you?";
const SET_SIZE = 9; // iso 2 + tracing 2 + plain 1 + two generated families x 2

const LEARNER = {
  email: `e2e-fam-${Date.now()}@example.com`,
  password: "E2e-families-2026!",
};

// One registration for both viewports: sign-up is rate limited (5 a minute) and the other specs register too.
test.beforeAll(async ({ playwright, baseURL }) => {
  const api = await playwright.request.newContext({ baseURL });
  const register = await api.post("/api/auth/register", {
    data: { ...LEARNER, name: "e2e-fam", locale: "en", courses: [COURSE] },
  });
  expect(register.ok(), await register.text()).toBe(true);
  await api.dispose();
});

async function signIn(page: Page): Promise<void> {
  const login = await page.request.post("/api/auth/login", { data: LEARNER });
  expect(login.ok(), await login.text()).toBe(true);
}

type Kind = "iso" | "tracing" | "plain" | "generated";

/** The family of the question on screen: a stored family, the unfamilied one, or (no known prompt) a generated item. */
async function kindOnScreen(page: Page): Promise<Kind> {
  const known: [Kind, string][] = [
    ...FAMILIES.iso.map((prompt): [Kind, string] => ["iso", prompt]),
    ...FAMILIES.tracing.map((prompt): [Kind, string] => ["tracing", prompt]),
    ["plain", PLAIN],
  ];
  for (const [kind, prompt] of known) {
    if ((await page.getByText(prompt, { exact: true }).count()) > 0) return kind;
  }
  return "generated";
}

async function answerRound(page: Page): Promise<Kind[]> {
  const kinds: Kind[] = [];
  for (let position = 1; position <= SET_SIZE; position += 1) {
    await expect(page.getByText(`Question ${position} of ${SET_SIZE}`, { exact: true })).toBeVisible();
    const options = page.getByRole("radio").locator("xpath=ancestor::label");
    await expect(options.first()).toBeVisible();
    kinds.push(await kindOnScreen(page));
    await options.first().click();
    await page.getByRole("button", { name: "Submit" }).click();
    await page.getByRole("button", { name: /^(Next|Finish)/ }).click();
  }
  return kinds;
}

for (const [name, viewport, mobile] of [
  ["390 px", { width: 390, height: 800 }, true],
  ["1280 px", { width: 1280, height: 800 }, false],
] as const) {
  test.describe(`at ${name}`, () => {
    test.use({ viewport, isMobile: mobile, hasTouch: mobile, storageState: { cookies: [], origins: [] } });

    test("a set mixes stored, family and generated questions and serves at most two of a family", async ({ page }) => {
      await signIn(page);
      await page.goto(LESSON);
      await expect(
        page.getByText("Generated questions that practise this lesson: Capacity estimation, Loop complexity."),
      ).toBeVisible();
      await page.goto(`${LESSON}/practice`);
      await page.getByRole("radio", { name: /^All \(7\)$/ }).check({ force: true });
      await page.getByRole("button", { name: "Start" }).click();

      const kinds = await answerRound(page);
      const count = (kind: Kind) => kinds.filter((k) => k === kind).length;
      expect(count("iso")).toBe(2);
      expect(count("tracing")).toBe(2);
      expect(count("plain")).toBe(1);
      expect(count("generated")).toBe(4);
      await expect(page.getByText("You have finished this round.")).toBeVisible();
      expect(await page.evaluate(() => document.documentElement.scrollWidth <= window.innerWidth)).toBe(true);
    });
  });
}
