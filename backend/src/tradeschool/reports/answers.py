# SPDX-License-Identifier: AGPL-3.0-only
"""A quiz answer written out the way the learner saw it: option texts, not option ids."""

from __future__ import annotations

from collections.abc import Mapping

_TRUE_FALSE = {"en": ("True", "False"), "es": ("Verdadero", "Falso")}
_NO_ANSWER = {"en": "(no answer)", "es": "(sin respuesta)"}


def _texts(entries: object) -> dict[str, str]:
    if not isinstance(entries, list):
        return {}
    return {str(e["id"]): str(e["text"]) for e in entries if isinstance(e, dict)}


def _boolean(value: object, locale: str) -> str:
    yes, no = _TRUE_FALSE.get(locale, _TRUE_FALSE["en"])
    return yes if value is True else no


def describe_given(payload: Mapping[str, object], answer: Mapping[str, object] | None, locale: str) -> str:
    """The learner's answer, in the texts the instance showed them."""
    if not answer:
        return _NO_ANSWER.get(locale, _NO_ANSWER["en"])
    options = _texts(payload.get("options"))
    if "optionId" in answer:
        return options.get(str(answer["optionId"]), str(answer["optionId"]))
    if "optionIds" in answer and isinstance(answer["optionIds"], list):
        return "; ".join(options.get(str(i), str(i)) for i in answer["optionIds"]) or _NO_ANSWER[locale]
    if "value" in answer:
        return _boolean(answer["value"], locale)
    if "order" in answer and isinstance(answer["order"], list):
        items = _texts(payload.get("items"))
        return " → ".join(items.get(str(i), str(i)) for i in answer["order"])
    if "pairs" in answer and isinstance(answer["pairs"], dict):
        lefts, rights = _texts(payload.get("lefts")), _texts(payload.get("rights"))
        return "; ".join(
            f"{lefts.get(str(left), str(left))} = {rights.get(str(right), str(right))}"
            for left, right in answer["pairs"].items()
        )
    return str(dict(answer))


def describe_correct(correct_answer: object, locale: str) -> str:
    """The solution as the review screen prints it."""
    if not isinstance(correct_answer, dict):
        return str(correct_answer)
    if "text" in correct_answer:
        return str(correct_answer["text"])
    if "readable" in correct_answer and isinstance(correct_answer["readable"], list):
        return "; ".join(f"{p['left']} = {p['right']}" for p in correct_answer["readable"])
    if "order" in correct_answer and isinstance(correct_answer.get("texts"), list):
        return " → ".join(str(t) for t in correct_answer["texts"])
    if "texts" in correct_answer and isinstance(correct_answer["texts"], list):
        return "; ".join(str(t) for t in correct_answer["texts"])
    if "value" in correct_answer:
        return _boolean(correct_answer["value"], locale)
    return str(correct_answer)
