import { expect, test, type Locator, type Page } from "@playwright/test";
import { AEAT, AGE, AGE_C2, CRYPTO, overflowingElements } from "./session";

/** Deltas N1 and N2 at real widths: highlighted code that scrolls inside its box, and the judgement callout. */

const TECH = "fixture-tecnico";
const LESSON = `/courses/${TECH}/lessons/m01-l1`;
const SOURCE = "Google, Site Reliability Engineering, ch. 17";

async function openLesson(page: Page): Promise<void> {
  const courses = await page.request.put("/api/me/courses", {
    data: { active: [AGE, CRYPTO, AGE_C2, AEAT, TECH], selected: TECH },
  });
  expect(courses.ok(), await courses.text()).toBe(true);
  await page.goto(LESSON);
  await expect(page.getByRole("heading", { level: 1 })).toContainText("Lost updates");
}

/** The block's own horizontal scroll: wider inside than outside, and it moves when scrolled. */
async function scrollsInsideItsBox(block: Locator): Promise<void> {
  const widths = await block.evaluate((element) => ({ inner: element.scrollWidth, outer: element.clientWidth }));
  expect(widths.inner).toBeGreaterThan(widths.outer);
  const moved = await block.evaluate((element) => {
    element.scrollLeft = 120;
    return element.scrollLeft;
  });
  expect(moved).toBeGreaterThan(0);
}

for (const [name, viewport, mobile] of [
  ["390 px", { width: 390, height: 800 }, true],
  ["1280 px", { width: 1280, height: 800 }, false],
] as const) {
  test.describe(`at ${name}`, () => {
    test.use({ viewport, isMobile: mobile, hasTouch: mobile });

    test("a code block is highlighted and scrolls inside its box while the page stays put", async ({ page }) => {
      await openLesson(page);
      const block = page.getByRole("region", { name: "Código, java" });
      await expect(block).toBeVisible();
      const colours = await block.evaluate((element) => {
        const keyword = element.querySelector(".hljs-keyword");
        if (!keyword) throw new Error("no keyword token");
        return { keyword: getComputedStyle(keyword).color, plain: getComputedStyle(element).color };
      });
      expect(colours.keyword).not.toBe(colours.plain);
      await scrollsInsideItsBox(block);
      const page_ = await page.evaluate(() => ({
        scroll: document.documentElement.scrollWidth,
        client: document.documentElement.clientWidth,
      }));
      expect(page_.scroll).toBeLessThanOrEqual(page_.client);
      expect(await overflowingElements(page)).toEqual([]);
    });

    test("the info string's meta and the bullets comment stay off the page", async ({ page }) => {
      await openLesson(page);
      const text = (await page.getByRole("main").innerText()).toLowerCase();
      expect(text).not.toContain("snippet=");
      expect(text).not.toContain("bullets");
    });

    test("a judgement is a callout naming its source", async ({ page }) => {
      await openLesson(page);
      const callout = page.getByRole("complementary", { name: `Juicio de ${SOURCE}` });
      await expect(callout).toBeVisible();
      await expect(callout).toContainText(SOURCE);
      await expect(callout).toContainText("According to the SRE book");
      await expect(callout).toContainText("sre-book#ch17");
      await page.waitForLoadState("networkidle");
      expect(await overflowingElements(page)).toEqual([]);
    });
  });
}
