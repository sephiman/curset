import { useMutation, useQuery, useQueryClient } from "@tanstack/react-query";
import type { Locale } from "@/api/auth";
import { getCatalogue, getMyCourses, saveMyCourses, type MyCourses, type MyCoursesUpdate } from "@/api/courses";
import { useAuth } from "@/auth/AuthContext";
import { useInterfaceLocale } from "@/i18n/locale";

export const MY_COURSES_KEY = ["courses", "mine"] as const;

/** Published courses, alphabetical by title in the interface language (the server sorts). */
export function useCatalogue() {
  const locale = useInterfaceLocale();
  return useQuery({ queryKey: ["courses", "catalogue", locale], queryFn: getCatalogue, staleTime: 5 * 60_000 });
}

export function useMyCourses() {
  const { user } = useAuth();
  return useQuery({ queryKey: MY_COURSES_KEY, queryFn: getMyCourses, enabled: user !== null });
}

/** Replace the user's choices; the response is the new truth, so nothing has to refetch it. */
export function useSaveMyCourses() {
  const queryClient = useQueryClient();
  return useMutation({
    mutationFn: (update: MyCoursesUpdate) => saveMyCourses(update),
    meta: { silentSuccess: true },
    onSuccess: (mine) => queryClient.setQueryData<MyCourses>(MY_COURSES_KEY, mine),
  });
}

/** Choose one course's reading language, keeping every other choice as it is. */
export function useChooseReadingLanguage() {
  const { data: mine } = useMyCourses();
  const save = useSaveMyCourses();
  return (slug: string, lang: Locale) => {
    if (!mine) return;
    save.mutate({ active: mine.active, selected: mine.selected, readingLanguages: { [slug]: lang } });
  };
}

/** The header's ES ↔ EN switch carries the viewed course along when that course has the language. */
export function useFollowInterfaceLanguage() {
  const { data: mine } = useMyCourses();
  const { data: catalogue } = useCatalogue();
  const choose = useChooseReadingLanguage();
  const queryClient = useQueryClient();
  return (lang: Locale) => {
    const selected = mine?.selected;
    const course = catalogue?.find((entry) => entry.slug === selected);
    if (selected && course?.languages.includes(lang)) choose(selected, lang);
    else void queryClient.invalidateQueries({ queryKey: MY_COURSES_KEY });
  };
}
