import axios, { type AxiosError } from "axios";
import i18n from "@/i18n";
import type { Locale } from "@/api/auth";

// Cookie auth uses fastapi-users cookie transport with SameSite=Lax, which blocks cross-site
// state-changing requests at the browser — so no XSRF double-submit token is needed. We only
// need cookies to travel with same-origin requests.
export const apiClient = axios.create({
  baseURL: "/api",
  withCredentials: true,
  headers: { "Content-Type": "application/json" },
});

// Default every request to the interface language (the catalogue's titles, for one). Course content
// overrides it with the course's reading language through `inReadingLanguage`.
apiClient.interceptors.request.use((config) => {
  const lang = i18n.resolvedLanguage?.startsWith("es") ? "es" : "en";
  config.params = { lang, ...(config.params ?? {}) };
  return config;
});

export interface ApiError {
  code: string;
  message: string;
  fields?: Record<string, string>;
}

export function asApiError(err: unknown): ApiError {
  const ax = err as AxiosError<ApiError>;
  if (ax?.response?.data?.code) return ax.response.data;
  return { code: "UNKNOWN", message: ax?.message ?? "Unknown error" };
}

/** Localized message for a failed request: the `errors.<code>` translation, falling back to the server message. */
export function apiErrorMessage(err: unknown, t: (key: string, fallback: string) => string): string {
  const api = asApiError(err);
  return t(`errors.${api.code}`, api.message);
}

/**
 * The course a request is about and the language its content is read in.
 *
 * Every course-owned call takes one: the slug picks the course, `lang` is the course's reading
 * language — which is not always the interface's, since a course may exist in Spanish only.
 */
export interface CourseScope {
  slug: string;
  lang: Locale;
}

/** A course-owned endpoint. The ONE way such a URL is built, so none can forget its course. */
export function courseUrl(scope: CourseScope, rest = ""): string {
  return `/courses/${encodeURIComponent(scope.slug)}${rest}`;
}

/** Request config carrying the reading language, which wins over the interceptor's interface one. */
export function inReadingLanguage(scope: CourseScope, params: Record<string, unknown> = {}) {
  return { params: { ...params, lang: scope.lang } };
}
