import { Link } from "react-router-dom";
import { useTranslation } from "react-i18next";
import { drawCourseRound, type CourseRoundPreset } from "@/api/practice";
import { useCourse } from "@/features/courses/CourseContext";
import { PracticeRound } from "@/features/practice/PracticeRound";
import { cn } from "@/lib/cn";
import { useLessonWidth } from "@/lib/lessonWidth";

/** The default round the course-wide presets draw. */
const ROUND_SIZE = 20;

const TEXT_KEYS: Record<CourseRoundPreset, { title: string; lead: string }> = {
  review: { title: "practicePresets.review", lead: "practicePresets.reviewLead" },
  "code-reading": { title: "practicePresets.codeReading", lead: "practicePresets.codeReadingLead" },
};

/** A course-wide preset: the scheduler's mixed review, or the code-reading questions only. */
export function CoursePracticePage({ preset }: { preset: CourseRoundPreset }) {
  const { t } = useTranslation();
  const { scope, path } = useCourse();
  const { lessonWidthClass } = useLessonWidth();
  const keys = TEXT_KEYS[preset];
  return (
    <div className={cn("mx-auto space-y-4", lessonWidthClass)}>
      <div>
        <Link to={path()} className="text-sm text-primary hover:underline">
          ← {t("psicotecnicos.back")}
        </Link>
        <h1 className="mt-2 text-xl font-bold">{t(keys.title)}</h1>
      </div>
      <PracticeRound
        key={preset}
        draw={() => drawCourseRound(scope, preset, ROUND_SIZE)}
        lead={t(keys.lead)}
      />
    </div>
  );
}
