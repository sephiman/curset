# SPDX-License-Identifier: AGPL-3.0-only
"""SMTP over STARTTLS with crypto-ambush's variable names; all-or-nothing configuration; never raises."""

from __future__ import annotations

import logging
import smtplib
import threading
from dataclasses import dataclass
from email.message import EmailMessage
from typing import Protocol

from tradeschool.config import Settings

logger = logging.getLogger("tradeschool.auth")


@dataclass(frozen=True)
class MailSettings:
    host: str
    port: int
    username: str
    password: str
    sender: str


def mail_settings_from(settings: Settings) -> MailSettings | None:
    """None when the SMTP group is absent or only partly set; a partial group is logged."""
    values = {
        "SMTP_HOST": settings.smtp_host.strip(),
        "SMTP_USERNAME": settings.smtp_username.strip(),
        "SMTP_PASSWORD": settings.smtp_password.strip(),
        "MAIL_FROM": settings.mail_from.strip(),
    }
    missing = [name for name, value in values.items() if not value]
    if len(missing) == len(values):
        return None
    if missing:
        logger.warning("SMTP partially configured, mail disabled: missing %s", ", ".join(missing))
        return None
    return MailSettings(
        values["SMTP_HOST"],
        settings.smtp_port,
        values["SMTP_USERNAME"],
        values["SMTP_PASSWORD"],
        values["MAIL_FROM"],
    )


class Mailer(Protocol):
    enabled: bool

    def send(self, to: str, subject: str, body: str) -> None: ...


class DisabledMailer:
    enabled = False

    def send(self, to: str, subject: str, body: str) -> None:
        logger.info("mail disabled, dropped %r", subject)


class SmtpMailer:
    enabled = True

    def __init__(self, settings: MailSettings) -> None:
        self._settings = settings

    def send(self, to: str, subject: str, body: str) -> None:
        # Off the request: the response time must not tell whether a mail went out.
        threading.Thread(
            target=self._deliver, args=(to, subject, body), daemon=True, name="tradeschool-mail"
        ).start()

    def _deliver(self, to: str, subject: str, body: str) -> None:
        message = EmailMessage()
        message["From"] = self._settings.sender
        message["To"] = to
        message["Subject"] = subject
        message.set_content(body)
        try:
            with smtplib.SMTP(self._settings.host, self._settings.port, timeout=10) as smtp:
                smtp.starttls()
                smtp.login(self._settings.username, self._settings.password)
                smtp.send_message(message)
        except Exception as exc:
            logger.warning("mail %r failed: %s", subject, exc)


def build_mailer(settings: Settings) -> Mailer:
    mail = mail_settings_from(settings)
    return SmtpMailer(mail) if mail else DisabledMailer()
