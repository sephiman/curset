import { Navigate, Route, Routes } from "react-router-dom";
import { AppShell } from "@/components/layout/AppShell";
import { coursePath } from "@/components/layout/nav";
import { ToastHost } from "@/components/ui/ToastHost";
import { ForgotPasswordPage } from "@/auth/ForgotPasswordPage";
import { LoginPage } from "@/auth/LoginPage";
import { RegisterPage } from "@/auth/RegisterPage";
import { RequireAuth } from "@/auth/RequireAuth";
import { ResetPasswordPage } from "@/auth/ResetPasswordPage";
import { VerifyEmailPage } from "@/auth/VerifyEmailPage";
import { AccountPage } from "@/features/account/AccountPage";
import { CoursePage } from "@/features/course/CoursePage";
import { ModulePage } from "@/features/course/ModulePage";
import { LessonPage } from "@/features/course/LessonPage";
import { CourseRoutes } from "@/features/courses/CourseRoute";
import { SelectedCourseRedirect } from "@/features/courses/SelectedCourseRedirect";
import { GlossaryPage } from "@/features/glossary/GlossaryPage";
import { StatsPage } from "@/features/stats/StatsPage";
import { ExamPage } from "@/features/exams/ExamPage";
import { ExamRunner } from "@/features/exams/ExamRunner";
import { ExamReview } from "@/features/exams/ExamReview";
import { ChartGallery, GALLERY_COURSE } from "@/features/dev/ChartGallery";

/**
 * The pages of one course, relative to `/courses/:course`. A display id names its CURRENT holder, so
 * no content id is ever a static route here — it would shadow the live page that now owns the id.
 */
const COURSE_PAGES = [
  { path: "", element: <CoursePage /> },
  { path: "modules/:moduleId", element: <ModulePage /> },
  { path: "lessons/:lessonId", element: <LessonPage /> },
  { path: "glossary", element: <GlossaryPage /> },
  { path: "stats", element: <StatsPage /> },
  { path: "exams", element: <ExamPage /> },
  { path: "exams/:examId", element: <ExamRunner /> },
  { path: "exams/:examId/review", element: <ExamReview /> },
  // Unadvertised review route; its data comes from the DEV_MODE-gated dev endpoints.
  { path: "dev/charts", element: <ChartGallery /> },
];

export default function App() {
  return (
    <>
      <Routes>
        <Route path="/login" element={<LoginPage />} />
        <Route path="/register" element={<RegisterPage />} />
        {/* Mailed links land here, signed in or not. */}
        <Route path="/forgot-password" element={<ForgotPasswordPage />} />
        <Route path="/reset-password" element={<ResetPasswordPage />} />
        <Route path="/verify-email" element={<VerifyEmailPage />} />
        <Route
          path="/*"
          element={
            <RequireAuth>
              <AppShell>
                <Routes>
                  <Route path="/courses/:course/*" element={<CourseRoutes pages={COURSE_PAGES} />} />
                  <Route path="/account" element={<AccountPage />} />

                  {/* Course-less addresses — the home, each tab, and bookmarks from before the URLs
                      named a course — resolve to the selected course, or to the tab's "no course" page. */}
                  <Route path="/" element={<SelectedCourseRedirect tab="course" />} />
                  <Route path="/course" element={<SelectedCourseRedirect tab="course" />} />
                  <Route path="/modules/:moduleId" element={<SelectedCourseRedirect tab="course" />} />
                  <Route path="/lessons/:lessonId" element={<SelectedCourseRedirect tab="course" />} />
                  <Route path="/glossary" element={<SelectedCourseRedirect tab="glossary" />} />
                  <Route path="/stats" element={<SelectedCourseRedirect tab="progress" />} />
                  <Route path="/exams/*" element={<SelectedCourseRedirect tab="exams" />} />

                  <Route path="/dev/charts" element={<Navigate to={coursePath(GALLERY_COURSE, "/dev/charts")} replace />} />
                  <Route path="*" element={<Navigate to="/" replace />} />
                </Routes>
              </AppShell>
            </RequireAuth>
          }
        />
      </Routes>
      <ToastHost />
    </>
  );
}
