import { useTranslation } from "react-i18next";
import type { Locale } from "@/api/auth";

/** The interface language as one of the two the platform speaks. */
export function useInterfaceLocale(): Locale {
  const { i18n } = useTranslation();
  return i18n.resolvedLanguage === "es" ? "es" : "en";
}
