import type { TFunction } from "i18next";
import type { Locale } from "@/api/auth";

/** "Spanish only" / "In English and Spanish", in the interface language (R4.4). */
export function availability(languages: readonly Locale[], interfaceLocale: Locale, t: TFunction): string {
  const names = languages.map((lang) => t(`languages.${lang}`));
  if (names.length === 1) return t("courses.onlyIn", { language: names[0] });
  const list = new Intl.ListFormat(interfaceLocale, { type: "conjunction" }).format(names);
  return t("courses.availableIn", { languages: list });
}
