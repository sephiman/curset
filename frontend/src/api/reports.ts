import { apiClient, courseUrl, inReadingLanguage, type CourseScope } from "@/api/client";

/** Report an answered question. The server fills in everything else; the learner gets no status back. */
export async function reportQuestion(scope: CourseScope, attemptId: string, message: string): Promise<void> {
  await apiClient.post(courseUrl(scope, `/attempts/${attemptId}/report`), { message }, inReadingLanguage(scope));
}
