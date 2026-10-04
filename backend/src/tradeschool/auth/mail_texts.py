# SPDX-License-Identifier: AGPL-3.0-only
"""Plain-text mail bodies in en/es; the link sits on its own line so clients auto-link it."""

from __future__ import annotations

_RESET = {
    "en": (
        "Reset your Curset password",
        "Hello {username},\n\nSomeone asked to reset the password of your Curset account. "
        "Open this link within {minutes} minutes:\n\n{link}\n\n"
        "If you did not ask for it, ignore this message. Your password stays the same.",
    ),
    "es": (
        "Restablece tu contraseña de Curset",
        "Hola, {username}:\n\nAlguien ha pedido restablecer la contraseña de tu cuenta de Curset. "
        "Abre este enlace en los próximos {minutes} minutos:\n\n{link}\n\n"
        "Si no lo has pedido tú, ignora este mensaje. Tu contraseña no cambia.",
    ),
}

_VERIFY = {
    "en": (
        "Confirm your Curset email",
        "Hello {username},\n\nConfirm that this address belongs to your Curset account. "
        "Open this link within {hours} hours:\n\n{link}\n\n"
        "Until you confirm it, the address cannot be used to reset your password. "
        "If you did not add it, ignore this message.",
    ),
    "es": (
        "Confirma tu correo de Curset",
        "Hola, {username}:\n\nConfirma que esta dirección es de tu cuenta de Curset. "
        "Abre este enlace en las próximas {hours} horas:\n\n{link}\n\n"
        "Hasta que la confirmes, no sirve para restablecer la contraseña. "
        "Si no la has añadido tú, ignora este mensaje.",
    ),
}


def password_reset_mail(locale: str, username: str, link: str, minutes: int) -> tuple[str, str]:
    subject, body = _RESET.get(locale, _RESET["en"])
    return subject, body.format(username=username, link=link, minutes=minutes)


def verification_mail(locale: str, username: str, link: str, hours: int) -> tuple[str, str]:
    subject, body = _VERIFY.get(locale, _VERIFY["en"])
    return subject, body.format(username=username, link=link, hours=hours)
