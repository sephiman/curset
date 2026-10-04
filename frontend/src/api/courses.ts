import { apiClient } from "@/api/client";
import type { Locale } from "@/api/auth";

/** A published course as the catalogue lists it, its own texts in `textLocale`. */
export interface CatalogueCourse {
  slug: string;
  title: string;
  subtitle: string;
  description: string;
  /** The account's language when the course has it, else the course's first. */
  textLocale: Locale;
  languages: Locale[];
}

/** The signed-in user's course choices; `selected` is already the server's fallback when needed. */
export interface MyCourses {
  active: string[];
  selected: string | null;
  /** Effective reading language for every published course. */
  readingLanguages: Record<string, Locale>;
}

export interface MyCoursesUpdate {
  active: string[];
  selected: string | null;
  /** Only the courses whose reading language the user is choosing now. */
  readingLanguages?: Record<string, Locale>;
}

/** Public: the sign-up screen lists it before there is an account. */
export async function getCatalogue(): Promise<CatalogueCourse[]> {
  const { data } = await apiClient.get<CatalogueCourse[]>("/courses");
  return data;
}

export async function getMyCourses(): Promise<MyCourses> {
  const { data } = await apiClient.get<MyCourses>("/me/courses");
  return data;
}

export async function saveMyCourses(update: MyCoursesUpdate): Promise<MyCourses> {
  const { data } = await apiClient.put<MyCourses>("/me/courses", update);
  return data;
}
