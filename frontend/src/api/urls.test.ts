import { readFileSync, readdirSync } from "node:fs";
import { resolve } from "node:path";
import { describe, expect, it } from "vitest";
import { courseUrl } from "@/api/client";

/**
 * Every course-owned request names its course. The unscoped aliases are gone from the backend
 * (`test_course_scoped_urls.py`); this is the grep-level gate that no caller builds one by hand.
 */

const API_DIR = resolve(__dirname);
/** Endpoints that are genuinely global: the account, and the catalogue and choices that pick a course. */
const GLOBAL = ['"/auth', '"/courses"', '"/me/courses"'];
/** An actual request — `apiClient.interceptors.…` is configuration, not a call. */
const HTTP_CALL = /apiClient\.(get|post|put|patch|delete)[<(]/;

function apiCalls(): { file: string; call: string }[] {
  return readdirSync(API_DIR)
    .filter((f) => f.endsWith(".ts") && !f.endsWith(".test.ts"))
    .flatMap((file) => {
      const body = readFileSync(resolve(API_DIR, file), "utf8");
      // A call may wrap its arguments over several lines; read up to its closing parenthesis.
      return [...body.matchAll(/apiClient\.(?:get|post|put|patch|delete)[<(][\s\S]*?\);/g)].map((m) => ({
        file,
        call: m[0].replace(/\s+/g, " "),
      }));
    });
}

describe("course-owned requests name their course", () => {
  it("builds the scoped URL from the slug", () => {
    expect(courseUrl({ slug: "crypto-futures", lang: "es" }, "/glossary")).toBe("/courses/crypto-futures/glossary");
  });

  it("every call that is not global goes through courseUrl", () => {
    const calls = apiCalls().filter(({ call }) => HTTP_CALL.test(call));
    expect(calls.length).toBeGreaterThan(20);
    const offenders = calls
      .filter(({ call }) => !GLOBAL.some((g) => call.includes(g)))
      .filter(({ call }) => !call.includes("courseUrl("))
      .map(({ file, call }) => `${file}: ${call}`);
    expect(offenders).toEqual([]);
  });
});
