import { useState } from "react";
import { useNavigate } from "react-router-dom";
import { useTranslation } from "react-i18next";
import type { Course, PracticePresetId } from "@/api/course";
import { Button, Card, Select } from "@/components/ui/primitives";
import { useCourse } from "@/features/courses/CourseContext";

const LABEL_KEYS: Record<PracticePresetId, string> = {
  lesson: "practicePresets.lesson",
  module: "practicePresets.module",
  review: "practicePresets.review",
  "code-reading": "practicePresets.codeReading",
  generators: "practicePresets.generators",
};

type Picker = "lesson" | "module";

/** Where a preset that needs no choice opens, relative to the course. */
const DIRECT: Record<Exclude<PracticePresetId, Picker>, string> = {
  review: "/practice/review",
  "code-reading": "/practice/code-reading",
  generators: "/practice/psicotecnicos",
};

function isPicker(preset: PracticePresetId): preset is Picker {
  return preset === "lesson" || preset === "module";
}

interface Target {
  id: string;
  title: string;
  group: string;
}

/** Lessons or modules with questions to practise, in course order. */
function targets(course: Course, picker: Picker): Target[] {
  return course.blocks.flatMap((block) =>
    block.modules.flatMap((module) => {
      const name = `${module.id.toUpperCase()} · ${module.title}`;
      if (picker === "module") {
        const questions = module.lessons.reduce((sum, lesson) => sum + (lesson.practiceQuestions ?? 0), 0);
        return questions > 0 ? [{ id: module.id, title: name, group: block.title }] : [];
      }
      return module.lessons
        .filter((lesson) => (lesson.practiceQuestions ?? 0) > 0)
        .map((lesson) => ({ id: lesson.id, title: lesson.title, group: name }));
    }),
  );
}

/** The course page's practice presets: one button each; «by lesson» and «by module» open a picker first. */
export function PracticePresets({ course }: { course: Course }) {
  const { t } = useTranslation();
  const navigate = useNavigate();
  const { path } = useCourse();
  const [picker, setPicker] = useState<Picker | null>(null);
  const [chosen, setChosen] = useState("");
  const presets = course.course.practicePresets ?? [];
  if (presets.length === 0) return null;

  const options = picker ? targets(course, picker) : [];
  const groups = [...new Set(options.map((option) => option.group))];
  const open = (preset: PracticePresetId) => {
    if (!isPicker(preset)) {
      navigate(path(DIRECT[preset]));
      return;
    }
    setPicker(picker === preset ? null : preset);
    setChosen(targets(course, preset)[0]?.id ?? "");
  };
  const start = () => {
    if (!picker || !chosen) return;
    navigate(path(picker === "lesson" ? `/lessons/${chosen}/practice` : `/modules/${chosen}/practice`));
  };

  return (
    <Card className="space-y-3 p-4">
      <div>
        <h2 className="font-semibold">{t("practicePresets.title")}</h2>
        <p className="text-sm text-gray-500 dark:text-gray-400">{t("practicePresets.hint")}</p>
      </div>
      <div className="grid grid-cols-1 gap-2 sm:grid-cols-2 lg:grid-cols-3">
        {presets.map((preset) => (
          <Button
            key={preset}
            variant={picker === preset ? "primary" : "secondary"}
            aria-expanded={isPicker(preset) ? picker === preset : undefined}
            onClick={() => open(preset)}
          >
            {t(LABEL_KEYS[preset])}
          </Button>
        ))}
      </div>
      {picker && (
        <div className="flex flex-col gap-2 sm:flex-row sm:items-end">
          <label className="block min-w-0 flex-1 text-sm">
            <span className="mb-1 block text-xs text-gray-500 dark:text-gray-400">
              {t(picker === "lesson" ? "practicePresets.chooseLesson" : "practicePresets.chooseModule")}
            </span>
            <Select className="min-h-11" value={chosen} onChange={(event) => setChosen(event.target.value)}>
              {groups.map((group) => (
                <optgroup key={group} label={group}>
                  {options
                    .filter((option) => option.group === group)
                    .map((option) => (
                      <option key={option.id} value={option.id}>
                        {option.title}
                      </option>
                    ))}
                </optgroup>
              ))}
            </Select>
          </label>
          <Button className="shrink-0" disabled={!chosen} onClick={start}>
            {t("practicePresets.start")}
          </Button>
        </div>
      )}
    </Card>
  );
}
