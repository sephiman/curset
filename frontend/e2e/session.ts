import { expect, type APIRequestContext, type Page } from "@playwright/test";

export const AGE = "age-administrativo-c1";
export const AGE_C2 = "age-auxiliar-c2";
export const AEAT = "aeat-agentes-hacienda";
export const CRYPTO = "crypto-futures";

// One fixed account, so repeated runs reuse it instead of filling the local database with users.
export const USER = { email: "e2e-mobile@example.com", password: "E2e-mobile-layout-2026!" };
export const STATE_FILE = "e2e/.auth/state.json";

/** All four real courses active, `selected` the current one; the session itself comes from the global setup. */
export async function signIn(page: Page, selected: string = AGE): Promise<void> {
  const courses = await page.request.put("/api/me/courses", { data: { active: [AGE, CRYPTO, AGE_C2, AEAT], selected } });
  expect(courses.ok(), await courses.text()).toBe(true);
}

interface Sitting {
  id: string;
  questions: {
    attemptId: string;
    partId: string;
    reserve: boolean;
    prompt: string;
    payload: { options?: { id: string; text?: string }[] };
  }[];
}

/** A new sitting; with a `seed` the draw is repeatable (the backend takes one only in dev mode). */
export async function startSitting(
  api: APIRequestContext,
  course: string,
  presetId: string,
  seed?: number,
): Promise<Sitting> {
  const response = await api.post(`/api/courses/${course}/exams`, { data: { presetId, target: null, seed } });
  expect(response.ok(), await response.text()).toBe(true);
  return (await response.json()) as Sitting;
}

/** A submitted sitting with every counted question answered (first option, or the one whose text is `prefer`),
 * so the results have a «Por tema». */
export async function submittedSitting(
  api: APIRequestContext,
  course: string,
  presetId: string,
  draw: { seed?: number; prefer?: string } = {},
): Promise<string> {
  const sitting = await startSitting(api, course, presetId, draw.seed);
  for (const question of sitting.questions.filter((q) => !q.reserve)) {
    const options = question.payload.options ?? [];
    const optionId = (options.find((option) => option.text === draw.prefer) ?? options[0])?.id;
    if (!optionId) continue;
    await api.post(`/api/courses/${course}/exams/${sitting.id}/questions/${question.attemptId}/answer`, {
      data: { answer: { optionId }, timeSeconds: 5 },
    });
  }
  const submit = await api.post(`/api/courses/${course}/exams/${sitting.id}/submit`, { data: {} });
  expect(submit.ok(), await submit.text()).toBe(true);
  return sitting.id;
}

export async function abandonSitting(api: APIRequestContext, course: string, id: string): Promise<void> {
  await api.post(`/api/courses/${course}/exams/${id}/abandon`);
}

/**
 * Everything on the page that reaches past the viewport's edges. Content inside a container that
 * scrolls or clips sideways (the chip strip) is that container's business, not the page's.
 */
export async function overflowingElements(page: Page): Promise<string[]> {
  return page.evaluate(() => {
    const width = document.documentElement.clientWidth;
    const clipsSideways = (element: Element): boolean => {
      for (let node = element.parentElement; node && node !== document.body; node = node.parentElement) {
        if (["auto", "scroll", "hidden", "clip"].includes(getComputedStyle(node).overflowX)) return true;
      }
      return false;
    };
    const found: string[] = [];
    if (window.innerWidth !== width) found.push(`layout viewport ${window.innerWidth}px for a ${width}px screen`);
    for (const element of document.body.querySelectorAll("*")) {
      const box = element.getBoundingClientRect();
      if (box.width === 0 || (box.right <= width + 0.5 && box.left >= -0.5)) continue;
      if (clipsSideways(element)) continue;
      const label = (element.textContent ?? "").trim().slice(0, 40);
      found.push(`${element.tagName.toLowerCase()} ${Math.round(box.left)}→${Math.round(box.right)} «${label}»`);
    }
    return found;
  });
}
