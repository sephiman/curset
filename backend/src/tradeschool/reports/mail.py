# SPDX-License-Identifier: AGPL-3.0-only
"""The plain-text mail a question report becomes; field labels in English, texts as the learner saw them."""

from __future__ import annotations

from tradeschool.reports.models import QuestionReport


def report_mail(report: QuestionReport) -> tuple[str, str]:
    subject = f"[Curset] Question report: {report.course_id} {report.exercise_id}"
    fields = [
        ("Course", report.course_id),
        ("Module", report.module_id),
        ("Lesson", report.lesson_id),
        ("Exercise", report.exercise_id),
        ("Variant", report.variant_id),
        ("Seed", str(report.seed)),
        ("Reading language", report.reading_locale),
        ("User", report.username),
        ("Sent at", report.created_at.isoformat(timespec="seconds")),
        ("Question", report.prompt),
        ("Their answer", report.given_answer),
        ("Correct answer", report.correct_answer),
    ]
    header = "\n".join(f"{label}: {value}" for label, value in fields)
    body = f"{report.message}\n\n---\n{header}\n\nOpen it in its lesson:\n\n{report.link}\n"
    return subject, body
