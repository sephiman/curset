# SPDX-License-Identifier: AGPL-3.0-only
from __future__ import annotations

import re
from datetime import timedelta

from httpx import AsyncClient
from sqlalchemy import update

from conftest import RecordingMailer
from tradeschool.auth.models import EmailToken
from tradeschool.db import get_sessionmaker

REG = {"username": "learner", "password": "correcthorse"}
EMAIL = "learner@example.com"


def _token(mailer: RecordingMailer, path: str) -> str:
    match = re.search(rf"/{path}\?token=(\S+)", mailer.outbox[-1].body)
    assert match, mailer.outbox[-1].body
    return match.group(1)


async def _signed_in(client: AsyncClient, **over: object) -> None:
    resp = await client.post("/api/auth/register", json={**REG, **over})
    assert resp.status_code == 201, resp.text
    assert (await client.post("/api/auth/login", json=REG)).status_code == 200


async def _age_tokens(by: timedelta) -> None:
    """Move every issued link into the past, as if `by` had elapsed."""
    async with get_sessionmaker()() as db:
        await db.execute(
            update(EmailToken).values(
                created_at=EmailToken.created_at - by, expires_at=EmailToken.expires_at - by
            )
        )
        await db.commit()


async def _verified(client: AsyncClient, mailer: RecordingMailer) -> None:
    await _signed_in(client, email=EMAIL)
    token = _token(mailer, "verify-email")
    resp = await client.post("/api/auth/email/verification/confirm", json={"token": token})
    assert resp.status_code == 200, resp.text


async def test_features_reports_mail_off_without_smtp(client: AsyncClient) -> None:
    assert (await client.get("/api/auth/features")).json() == {"mail": False}


async def test_features_reports_mail_on(mail_client: AsyncClient) -> None:
    assert (await mail_client.get("/api/auth/features")).json() == {"mail": True}


async def test_register_with_email_mails_a_verification_link(
    mail_client: AsyncClient, mailer: RecordingMailer
) -> None:
    resp = await mail_client.post("/api/auth/register", json={**REG, "email": " Learner@Example.COM "})
    assert resp.status_code == 201
    assert resp.json()["email"] == EMAIL
    assert resp.json()["email_verified"] is False
    assert [m.to for m in mailer.outbox] == [EMAIL]
    assert "/verify-email?token=" in mailer.outbox[0].body


async def test_verification_link_marks_the_email_verified(
    mail_client: AsyncClient, mailer: RecordingMailer
) -> None:
    await _verified(mail_client, mailer)
    assert (await mail_client.get("/api/auth/me")).json()["email_verified"] is True


async def test_verification_link_is_single_use(mail_client: AsyncClient, mailer: RecordingMailer) -> None:
    await _verified(mail_client, mailer)
    token = _token(mailer, "verify-email")
    resp = await mail_client.post("/api/auth/email/verification/confirm", json={"token": token})
    assert resp.status_code == 400
    assert resp.json()["code"] == "VERIFY_TOKEN_INVALID"


async def test_changing_email_unverifies_and_kills_the_old_link(
    mail_client: AsyncClient, mailer: RecordingMailer
) -> None:
    await _signed_in(mail_client, email=EMAIL)
    old_token = _token(mailer, "verify-email")
    resp = await mail_client.patch("/api/auth/me", json={"email": "other@example.com"})
    assert resp.json()["email"] == "other@example.com"
    assert resp.json()["email_verified"] is False

    resp = await mail_client.post("/api/auth/email/verification/confirm", json={"token": old_token})
    assert resp.status_code == 400


async def test_changing_a_verified_email_unverifies_it(
    mail_client: AsyncClient, mailer: RecordingMailer
) -> None:
    await _verified(mail_client, mailer)
    await _age_tokens(timedelta(minutes=5))
    resp = await mail_client.patch("/api/auth/me", json={"email": "new@example.com"})
    assert resp.json()["email_verified"] is False
    assert mailer.outbox[-1].to == "new@example.com"


async def test_email_null_removes_the_address(mail_client: AsyncClient, mailer: RecordingMailer) -> None:
    await _verified(mail_client, mailer)
    resp = await mail_client.patch("/api/auth/me", json={"email": None})
    assert resp.json()["email"] is None
    assert resp.json()["email_verified"] is False


async def test_patch_without_email_keeps_it(mail_client: AsyncClient, mailer: RecordingMailer) -> None:
    await _verified(mail_client, mailer)
    resp = await mail_client.patch("/api/auth/me", json={"locale": "es"})
    assert resp.json()["email"] == EMAIL
    assert resp.json()["email_verified"] is True


async def test_rejects_malformed_email(client: AsyncClient) -> None:
    await _signed_in(client)
    resp = await client.patch("/api/auth/me", json={"email": "not-an-address"})
    assert resp.status_code == 422


async def test_rejects_email_verified_by_another_account(
    mail_client: AsyncClient, mailer: RecordingMailer
) -> None:
    await _verified(mail_client, mailer)
    await mail_client.post("/api/auth/logout")
    resp = await mail_client.post(
        "/api/auth/register", json={"username": "squatter", "password": "correcthorse", "email": EMAIL}
    )
    assert resp.status_code == 409
    assert resp.json()["code"] == "EMAIL_ALREADY_USED"


async def test_unverified_claim_does_not_block_the_owner(
    mail_client: AsyncClient, mailer: RecordingMailer
) -> None:
    resp = await mail_client.post(
        "/api/auth/register", json={"username": "squatter", "password": "correcthorse", "email": EMAIL}
    )
    assert resp.status_code == 201
    await _verified(mail_client, mailer)


async def test_resend_is_throttled_per_account(mail_client: AsyncClient, mailer: RecordingMailer) -> None:
    await _signed_in(mail_client, email=EMAIL)
    resp = await mail_client.post("/api/auth/email/verification")
    assert resp.status_code == 202
    assert len(mailer.outbox) == 1

    await _age_tokens(timedelta(minutes=2))
    await mail_client.post("/api/auth/email/verification")
    assert len(mailer.outbox) == 2


async def test_resend_without_email_is_rejected(mail_client: AsyncClient) -> None:
    await _signed_in(mail_client)
    resp = await mail_client.post("/api/auth/email/verification")
    assert resp.status_code == 400
    assert resp.json()["code"] == "EMAIL_MISSING"


async def test_password_reset_is_404_when_mail_is_off(client: AsyncClient) -> None:
    resp = await client.post("/api/auth/password-reset", json={"email": EMAIL})
    assert resp.status_code == 404


async def test_password_reset_is_silent_for_unknown_address(
    mail_client: AsyncClient, mailer: RecordingMailer
) -> None:
    resp = await mail_client.post("/api/auth/password-reset", json={"email": "nobody@example.com"})
    assert resp.status_code == 202
    assert mailer.outbox == []


async def test_password_reset_ignores_an_unverified_address(
    mail_client: AsyncClient, mailer: RecordingMailer
) -> None:
    await _signed_in(mail_client, email=EMAIL)
    sent = len(mailer.outbox)
    resp = await mail_client.post("/api/auth/password-reset", json={"email": EMAIL})
    assert resp.status_code == 202
    assert len(mailer.outbox) == sent


async def test_password_reset_changes_password_and_ends_every_session(
    mail_client: AsyncClient, mailer: RecordingMailer
) -> None:
    await _verified(mail_client, mailer)
    await _age_tokens(timedelta(minutes=5))
    resp = await mail_client.post("/api/auth/password-reset", json={"email": EMAIL.upper()})
    assert resp.status_code == 202
    token = _token(mailer, "reset-password")

    assert (
        await mail_client.post("/api/auth/password-reset/validate", json={"token": token})
    ).status_code == 200
    resp = await mail_client.post(
        "/api/auth/password-reset/confirm", json={"token": token, "new_password": "batterystaple"}
    )
    assert resp.status_code == 200

    assert (await mail_client.get("/api/auth/me")).status_code == 401
    old = await mail_client.post("/api/auth/login", json=REG)
    assert old.status_code == 400
    new = await mail_client.post("/api/auth/login", json={**REG, "password": "batterystaple"})
    assert new.status_code == 200


async def test_reset_link_is_single_use(mail_client: AsyncClient, mailer: RecordingMailer) -> None:
    await _verified(mail_client, mailer)
    await _age_tokens(timedelta(minutes=5))
    await mail_client.post("/api/auth/password-reset", json={"email": EMAIL})
    token = _token(mailer, "reset-password")
    body = {"token": token, "new_password": "batterystaple"}
    assert (await mail_client.post("/api/auth/password-reset/confirm", json=body)).status_code == 200
    again = await mail_client.post("/api/auth/password-reset/confirm", json=body)
    assert again.status_code == 400
    assert again.json()["code"] == "RESET_TOKEN_INVALID"


async def test_reset_link_expires_after_an_hour(mail_client: AsyncClient, mailer: RecordingMailer) -> None:
    await _verified(mail_client, mailer)
    await _age_tokens(timedelta(minutes=5))
    await mail_client.post("/api/auth/password-reset", json={"email": EMAIL})
    token = _token(mailer, "reset-password")
    await _age_tokens(timedelta(minutes=61))
    resp = await mail_client.post("/api/auth/password-reset/validate", json={"token": token})
    assert resp.status_code == 400


async def test_only_the_newest_reset_link_works(mail_client: AsyncClient, mailer: RecordingMailer) -> None:
    await _verified(mail_client, mailer)
    await _age_tokens(timedelta(minutes=5))
    await mail_client.post("/api/auth/password-reset", json={"email": EMAIL})
    first = _token(mailer, "reset-password")
    await _age_tokens(timedelta(minutes=2))
    await mail_client.post("/api/auth/password-reset", json={"email": EMAIL})
    second = _token(mailer, "reset-password")
    assert first != second
    assert (
        await mail_client.post("/api/auth/password-reset/validate", json={"token": first})
    ).status_code == 400
    assert (
        await mail_client.post("/api/auth/password-reset/validate", json={"token": second})
    ).status_code == 200


async def test_reset_rejects_a_weak_password_and_keeps_the_link(
    mail_client: AsyncClient, mailer: RecordingMailer
) -> None:
    await _verified(mail_client, mailer)
    await _age_tokens(timedelta(minutes=5))
    await mail_client.post("/api/auth/password-reset", json={"email": EMAIL})
    token = _token(mailer, "reset-password")
    resp = await mail_client.post(
        "/api/auth/password-reset/confirm", json={"token": token, "new_password": "short"}
    )
    assert resp.status_code == 400
    assert resp.json()["code"] == "INVALID_PASSWORD"
    assert (
        await mail_client.post("/api/auth/password-reset/validate", json={"token": token})
    ).status_code == 200


async def test_mail_follows_the_user_locale(mail_client: AsyncClient, mailer: RecordingMailer) -> None:
    await _signed_in(mail_client, email=EMAIL, locale="es")
    assert mailer.outbox[0].subject == "Confirma tu correo de Curset"
