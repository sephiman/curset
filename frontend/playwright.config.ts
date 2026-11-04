import { defineConfig, devices } from "@playwright/test";

/**
 * Real-browser checks (deltas J and K): layout at real widths, which jsdom cannot measure. They run against
 * a local stack — Vite plus the backend on :8000 — never against a deploy host. Playwright starts Vite
 * (in CI too) unless one is already serving on :5173; the backend must already be up.
 */
const baseURL = process.env.E2E_BASE_URL ?? "http://localhost:5173";

export default defineConfig({
  testDir: "e2e",
  globalSetup: "./e2e/global-setup.ts",
  // One account, one open sitting at a time: the server closes a sitting when the same preset starts again.
  workers: 1,
  timeout: 60_000,
  reporter: [["list"]],
  use: {
    ...devices["Desktop Chrome"],
    baseURL,
    locale: "es-ES",
    trace: "retain-on-failure",
    storageState: "e2e/.auth/state.json",
  },
  webServer: process.env.E2E_BASE_URL
    ? undefined
    : { command: "npm run dev", url: baseURL, reuseExistingServer: true, timeout: 60_000 },
});
