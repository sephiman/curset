# SPDX-License-Identifier: AGPL-3.0-only
"""The generators the platform knows; one that fails its property tests does not load."""

from __future__ import annotations

from functools import cache

from tradeschool.psicotecnico.backend.catalogue import BACKEND_GENERATORS
from tradeschool.psicotecnico.contract import GeneratorLoadError, ItemGenerator, verify
from tradeschool.psicotecnico.generators.administrativo_clasificacion import ClasificacionGenerator
from tradeschool.psicotecnico.generators.administrativo_ordenacion import OrdenacionGenerator
from tradeschool.psicotecnico.generators.atencion_codificacion import CodificacionGenerator
from tradeschool.psicotecnico.generators.calculo_ecuaciones import EcuacionesGenerator
from tradeschool.psicotecnico.generators.calculo_fracciones import FraccionesGenerator
from tradeschool.psicotecnico.generators.calculo_porcentajes import PorcentajesGenerator
from tradeschool.psicotecnico.generators.calculo_problemas import ProblemasGenerator
from tradeschool.psicotecnico.generators.serie_numerica import SerieNumericaGenerator
from tradeschool.psicotecnico.generators.tablas_lectura import TablasLecturaGenerator
from tradeschool.psicotecnico.generators.verbal_antonimos import AntonimosGenerator
from tradeschool.psicotecnico.generators.verbal_definicion import DefinicionGenerator
from tradeschool.psicotecnico.generators.verbal_ortografia import OrtografiaGenerator
from tradeschool.psicotecnico.generators.verbal_sinonimos import SinonimosGenerator

GENERATORS: dict[str, ItemGenerator] = {
    generator.id: generator
    for generator in (
        TablasLecturaGenerator(),
        CodificacionGenerator(),
        SinonimosGenerator(),
        AntonimosGenerator(),
        EcuacionesGenerator(),
        DefinicionGenerator(),
        OrtografiaGenerator(),
        ProblemasGenerator(),
        PorcentajesGenerator(),
        SerieNumericaGenerator(),
        ClasificacionGenerator(),
        FraccionesGenerator(),
        OrdenacionGenerator(),
    )
}


def _all_generators() -> dict[str, ItemGenerator]:
    return {**GENERATORS, **BACKEND_GENERATORS}


def is_known(generator_id: str) -> bool:
    return generator_id in _all_generators()


def load_generator(generator_id: str, generators: dict[str, ItemGenerator] | None = None) -> ItemGenerator:
    """The generator, after its property tests passed once in this process."""
    known = _all_generators() if generators is None else generators
    try:
        generator = known[generator_id]
    except KeyError as exc:
        raise GeneratorLoadError(f"no psicotécnico generator {generator_id!r}") from exc
    if generators is None:
        return _verified(generator_id)
    failures = verify(generator)
    if failures:
        raise GeneratorLoadError("; ".join(failures[:5]))
    return generator


@cache
def _verified(generator_id: str) -> ItemGenerator:
    generator = _all_generators()[generator_id]
    failures = verify(generator)
    if failures:
        raise GeneratorLoadError(f"{generator_id} failed its property tests: " + "; ".join(failures[:5]))
    return generator
