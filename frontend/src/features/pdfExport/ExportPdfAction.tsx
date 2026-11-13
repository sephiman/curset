import type { Course } from "@/api/course";
import { useHeaderAction } from "@/components/layout/headerChrome";
import { Button } from "@/components/ui/primitives";
import { useExportPdf, type ExportTarget } from "@/features/pdfExport/useExportPdf";
import { usePhoneLayout } from "@/lib/viewport";

/** A lesson's or module's export: a button on the page, or an entry in the header menu on phones. */
export function ExportPdfAction({
  course,
  target,
  label,
}: {
  course: Course | undefined;
  target: ExportTarget;
  label: string;
}) {
  const phone = usePhoneLayout();
  const { open, dialog } = useExportPdf(course);
  useHeaderAction(phone && course ? { label, run: () => open(target) } : null);
  return (
    <>
      {!phone && course && (
        <Button variant="secondary" onClick={() => open(target)}>
          {label}
        </Button>
      )}
      {dialog}
    </>
  );
}
