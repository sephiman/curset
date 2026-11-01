import { defineConfig, devices } from "@playwright/test";

/**
 * Real-browser checks (delta J): layout at phone widths, which jsdom cannot measure. They run against a
 * live dev stack — `npm run dev` plus the backend on :8000 — never against a deploy host.
 */
export default defineConfig({
  testDir: "e2e",
  globalSetup: "./e2e/global-setup.ts",
  // One account, one open sitting at a time: the server closes a sitting when the same preset starts again.
  workers: 1,
  timeout: 60_000,
  reporter: [["list"]],
  use: {
    ...devices["Desktop Chrome"],
    baseURL: process.env.E2E_BASE_URL ?? "http://localhost:5173",
    locale: "es-ES",
    trace: "retain-on-failure",
    storageState: "e2e/.auth/state.json",
  },
});
