import { expect, test, type Page } from "@playwright/test";
import { AEAT, AGE, AGE_C2, CRYPTO, overflowingElements } from "./session";

/** Amendment 12 at real widths: a lesson diagram scrolls inside its own box and never widens the page. */

const COURSE = "backend-in-depth";
const CAPTION = "Changes are logged in the WAL before the data files are written";

async function openLesson(page: Page): Promise<void> {
  const courses = await page.request.put("/api/me/courses", {
    data: { active: [AGE, CRYPTO, AGE_C2, AEAT, COURSE], selected: COURSE },
  });
  expect(courses.ok(), await courses.text()).toBe(true);
  await page.goto(`/courses/${COURSE}/lessons/m06-l01`);
  await expect(page.getByRole("heading", { level: 1 })).toContainText("MVCC");
}

for (const [name, viewport, mobile] of [
  ["390 px", { width: 390, height: 800 }, true],
  ["1280 px", { width: 1280, height: 800 }, false],
] as const) {
  test.describe(`at ${name}`, () => {
    test.use({ viewport, isMobile: mobile, hasTouch: mobile });

    test("a diagram is a captioned figure in its own scrolling region and the page does not scroll sideways", async ({
      page,
    }) => {
      await openLesson(page);
      const region = page.getByRole("region", { name: CAPTION });
      await expect(region).toBeVisible();
      await expect(region.locator("svg")).toBeVisible();
      await expect(page.getByText(CAPTION, { exact: true }).last()).toBeVisible();
      expect(await region.evaluate((element) => getComputedStyle(element).overflowX)).toBe("auto");
      const widths = await page.evaluate(() => ({
        scroll: document.documentElement.scrollWidth,
        client: document.documentElement.clientWidth,
      }));
      expect(widths.scroll).toBeLessThanOrEqual(widths.client);
      expect(await overflowingElements(page)).toEqual([]);
    });

    test("the diagram's marker text and block syntax stay off the page", async ({ page }) => {
      await openLesson(page);
      const text = await page.getByRole("main").innerText();
      expect(text).not.toContain(":::diagram");
      expect(text).not.toContain("description:");
    });
  });
}
