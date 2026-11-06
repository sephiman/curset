// SPDX-License-Identifier: AGPL-3.0-only
// Fetches pages with the Chromium the e2e suite uses (frontend/node_modules/playwright), for sites that answer
// 403 to a plain request. Called by check_pages.py:
//   node fetch_rendered.mjs <jobs.json> <out-dir> [delay-ms]
// jobs.json is [{file, url}]; writes <out-dir>/<file> (the rendered DOM) and <out-dir>/_status.json. A page
// already fetched with a 200 in <out-dir> is kept, so a run cut short by the site's rate limit resumes.
import { createRequire } from "node:module";
import { existsSync, readFileSync, writeFileSync, mkdirSync } from "node:fs";
import { dirname, join, resolve } from "node:path";
import { fileURLToPath } from "node:url";

const repo = resolve(dirname(fileURLToPath(import.meta.url)), "../../..");
const { chromium } = createRequire(join(repo, "frontend/package.json"))("playwright");

const [jobsPath, outDir, delayArg] = process.argv.slice(2);
const delay = Number(delayArg ?? 1_500);
const jobs = JSON.parse(readFileSync(jobsPath, "utf-8"));
mkdirSync(outDir, { recursive: true });
const statusPath = join(outDir, "_status.json");
const done = new Map(
  (existsSync(statusPath) ? JSON.parse(readFileSync(statusPath, "utf-8")) : [])
    .filter((row) => row.http === 200 && existsSync(join(outDir, row.file)))
    .map((row) => [row.file, row]),
);

const browser = await chromium.launch();
const context = await browser.newContext({ locale: "es-ES" });
const status = [];
for (const { file, url } of jobs) {
  if (done.has(file)) {
    status.push(done.get(file));
    continue;
  }
  const page = await context.newPage();
  try {
    const response = await page.goto(url, { waitUntil: "domcontentloaded", timeout: 45_000 });
    // The support pages fill the article client-side; wait for it, but never longer than the cap.
    await page.waitForLoadState("networkidle", { timeout: 15_000 }).catch(() => {});
    writeFileSync(join(outDir, file), await page.content(), "utf-8");
    status.push({ file, url, http: response?.status() ?? null, final_url: page.url() });
  } catch (error) {
    status.push({ file, url, http: null, final_url: null, error: String(error).split("\n")[0] });
  } finally {
    await page.close();
  }
  await new Promise((resolve) => setTimeout(resolve, delay)); // one page at a time, spaced
}
await browser.close();
writeFileSync(statusPath, JSON.stringify(status, null, 1) + "\n", "utf-8");
