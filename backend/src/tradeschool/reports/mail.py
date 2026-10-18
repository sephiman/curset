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
    # A case question names its case; a cited question its citation, so it can be checked at the source.
    if report.case_title:
        fields.insert(4, ("Case", f"{report.exercise_id}: {report.case_title}"))
    if report.citation:
        fields.append(("Citation", report.citation))
    header = "\n".join(f"{label}: {value}" for label, value in fields)
    body = f"{report.message}\n\n---\n{header}\n\nOpen it in its lesson:\n\n{report.link}\n"
    if report.lesson_anchor:
        body += f"\nWhere the lesson cites it:\n\n{report.lesson_anchor}\n"
    return subject, body
