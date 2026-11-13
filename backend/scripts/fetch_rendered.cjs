// SPDX-License-Identifier: AGPL-3.0-only
// Prints a page's HTML after headless Chromium renders it; run from frontend/ so Playwright resolves.
const { chromium } = require(require.resolve("playwright", { paths: [process.cwd()] }));

(async () => {
  const browser = await chromium.launch();
  try {
    const page = await browser.newPage();
    await page.goto(process.argv[2], { waitUntil: "networkidle", timeout: 120000 });
    process.stdout.write(await page.content());
  } finally {
    await browser.close();
  }
})().catch((error) => {
  console.error(String(error));
  process.exit(1);
});
