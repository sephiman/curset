import type { ReactNode } from "react";
import type { Locale } from "@/api/auth";
import type { CatalogueCourse } from "@/api/courses";
import { CourseProvider } from "@/features/courses/CourseContext";

/** The course a component test renders inside, as the catalogue would describe crypto-futures. */
export const TEST_COURSE: CatalogueCourse = {
  slug: "crypto-futures",
  title: "Crypto Perpetual Futures: The Beginner's Guide",
  subtitle: "The Beginner's Guide",
  description: "From zero to your first trading plan.",
  textLocale: "en",
  languages: ["en", "es"],
};

/** What `/courses/:course/*` provides to every page below it. */
export function InCourse({ children, lang = "en" }: { children: ReactNode; lang?: Locale }) {
  return (
    <CourseProvider course={TEST_COURSE} scope={{ slug: TEST_COURSE.slug, lang }}>
      {children}
    </CourseProvider>
  );
}
