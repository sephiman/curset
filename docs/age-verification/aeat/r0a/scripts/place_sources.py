"""Copy the downloaded AEAT files into sources/examenes-oficiales under the C1 naming scheme and write the manifest."""

import csv
import hashlib
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
DEST = ROOT / "content/aeat-agentes-hacienda/sources/examenes-oficiales"
MANIFEST = ROOT / "docs/age-verification/aeat/r0a/sources-manifest.tsv"
DOWNLOAD_DATE = "2026-11-11"

# raw path (OEP year / original name) -> repo name: <exam date>_conv<OEP>_<piece>.pdf
PLACEMENT: dict[str, str] = {
    # OEP 2020: first exercise 2021-09-25, second 2021-11-13
    "2020/Cuest_1er_ejer_tipo_A_TL.pdf": "2021-09-25_conv2020_tipoA_cuestionario.pdf",
    "2020/Cuest_1er_ejer_tipo_B_TL.pdf": "2021-09-25_conv2020_tipoB_cuestionario.pdf",
    "2020/Plantilla_def_tipo_A_TL.pdf": "2021-09-25_conv2020_tipoA_plantilla-definitiva.pdf",
    "2020/Plantilla_def_tipo_B_TL.pdf": "2021-09-25_conv2020_tipoB_plantilla-definitiva.pdf",
    "2020/Criterios_correccion_TL.pdf": "2021-09-25_conv2020_criterios-correccion.pdf",
    "2020/Nota_infor_puntuaciones_TL.002.002.pdf": "2021-09-25_conv2020_nota-puntuaciones.pdf",
    "2020/Res_aprob_TL.002.pdf": "2021-09-25_conv2020_res-aprobados-1ej.pdf",
    "2020/Sup_practico_2ejer_TL.pdf": "2021-11-13_conv2020_2ej_supuesto.pdf",
    "2020/Normas_generales_ejer2_sede_Madrid.pdf": "2021-11-13_conv2020_2ej_normas-generales-madrid.pdf",
    # OEP 2021: first exercise 2022-05-28, second 2022-07-09
    "2021/CUESTIONARIO_LIBRE_TIPO_A.pdf": "2022-05-28_conv2021_tipoA_cuestionario.pdf",
    "2021/CUESTIONARIO_LIBRE_TIPO_B.pdf": "2022-05-28_conv2021_tipoB_cuestionario.pdf",
    "2021/Plantilla_def_TL_tipoA.pdf": "2022-05-28_conv2021_tipoA_plantilla-definitiva.pdf",
    "2021/Plantilla_def_TL_tipoB.pdf": "2022-05-28_conv2021_tipoB_plantilla-definitiva.pdf",
    "2021/Criterios_correccion_TL.pdf": "2022-05-28_conv2021_criterios-correccion.pdf",
    "2021/Nota_inf_puntuaciones_TL.pdf": "2022-05-28_conv2021_nota-puntuaciones.pdf",
    "2021/Res_aprob_1ejer_TL_WEB.pdf": "2022-05-28_conv2021_res-aprobados-1ej.pdf",
    "2021/Sup_practico_2ejer_TL.pdf": "2022-07-09_conv2021_2ej_supuesto.pdf",
    "2021/Normas_gen_2ejer_Madrid.pdf": "2022-07-09_conv2021_2ej_normas-generales-madrid.pdf",
    # OEP 2022: first exercise 2023-04-22, extraordinario 2023-07-18, second 2023-05-27
    "2022/Cuestionario_tipo_A.pdf": "2023-04-22_conv2022_tipoA_cuestionario.pdf",
    "2022/Cuestionario_tipo_B.pdf": "2023-04-22_conv2022_tipoB_cuestionario.pdf",
    "2022/Plantilla_def_tipo_A.pdf": "2023-04-22_conv2022_tipoA_plantilla-definitiva.pdf",
    "2022/Plantilla_def_tipo_B.pdf": "2023-04-22_conv2022_tipoB_plantilla-definitiva.pdf",
    "2022/Criterios_correc_1ejer_TL.pdf": "2023-04-22_conv2022_criterios-correccion.pdf",
    "2022/Aviso_Correc_criterios_1ejer_TL.pdf": "2023-04-22_conv2022_criterios-correccion-aviso-error.pdf",
    "2022/Rectif_criterios_correc_1ejer_TL.pdf": "2023-04-22_conv2022_criterios-correccion-rectificacion.pdf",
    "2022/Nota_infor_puntuaciones.pdf": "2023-04-22_conv2022_nota-puntuaciones.pdf",
    "2022/Res_aprob_1ej.pdf": "2023-04-22_conv2022_res-aprobados-1ej.pdf",
    "2022/Cuestionario_tipo_A_Ext_22_TL.pdf": "2023-07-18_conv2022_extraordinario_tipoA_cuestionario.pdf",
    "2022/Plantilla_prov_tipo_A_Ext_22_TL.pdf": "2023-07-18_conv2022_extraordinario_tipoA_plantilla-provisional.pdf",
    "2022/Res_aprob_ejercc1_extraordinario_con_anexo.pdf": "2023-07-18_conv2022_extraordinario_res-aprobados-1ej.pdf",
    "2022/Supuesto_2ejer_TL.pdf": "2023-05-27_conv2022_2ej_supuesto.pdf",
    "2022/Normas_grales_2ej.pdf": "2023-05-27_conv2022_2ej_normas-generales.pdf",
    # OEP 2023: first exercise 2024-04-20, second 2024-06-01 (extraordinario: date not published)
    "2023/Cuestionario_tipo_A.pdf": "2024-04-20_conv2023_tipoA_cuestionario.pdf",
    "2023/Cuestionario_tipo_B.pdf": "2024-04-20_conv2023_tipoB_cuestionario.pdf",
    "2023/Plantilla_def_tipo_A_TL.pdf": "2024-04-20_conv2023_tipoA_plantilla-definitiva.pdf",
    "2023/Plantilla_def_tipo_B_TL.pdf": "2024-04-20_conv2023_tipoB_plantilla-definitiva.pdf",
    "2023/Criterios_correccion_TL.pdf": "2024-04-20_conv2023_criterios-correccion.pdf",
    "2023/Nota_inf_puntuaciones.pdf": "2024-04-20_conv2023_nota-puntuaciones.pdf",
    "2023/Res_aprob_1ejer_conv_2ejer.pdf": "2024-04-20_conv2023_res-aprobados-1ej.pdf",
    "2023/Cuestionario_ejer2_TL.pdf": "2024-06-01_conv2023_2ej_cuestionario.pdf",
    "2023/Plantilla_def_2do_ejer_TL.pdf": "2024-06-01_conv2023_2ej_plantilla-definitiva.pdf",
    "2023/Normas_gen_2_ejer_TL.pdf": "2024-06-01_conv2023_2ej_normas-generales.pdf",
    "2023/Nota_informativa_2do_ejer.pdf": "2024-06-01_conv2023_2ej_nota-puntuaciones.pdf",
    "2023/Res_aprob_2ejer_y_fase_opos_TL.pdf": "2024-06-01_conv2023_2ej_res-aprobados.pdf",
    "2023/Cuestionario_ejer2_TL_extra.pdf": "conv2023_2ej_extraordinario_cuestionario.pdf",
    "2023/Plantilla_def_2do_ejer_extraordinario_TL.pdf": "conv2023_2ej_extraordinario_plantilla-definitiva.pdf",
    # OEP 2024: first exercise 2025-04-05, second 2025-05-24 (extraordinario: date not published)
    "2024/Cuestionario_A.pdf": "2025-04-05_conv2024_tipoA_cuestionario.pdf",
    "2024/Cuestionario_B.pdf": "2025-04-05_conv2024_tipoB_cuestionario.pdf",
    "2024/Plantilla_def_A.pdf": "2025-04-05_conv2024_tipoA_plantilla-definitiva.pdf",
    "2024/Plantilla_def_B.pdf": "2025-04-05_conv2024_tipoB_plantilla-definitiva.pdf",
    "2024/Criterios_correccion_tl.pdf": "2025-04-05_conv2024_criterios-correccion.pdf",
    "2024/Nota_informativa_puntuaciones.pdf": "2025-04-05_conv2024_nota-puntuaciones.pdf",
    "2024/Res_aprobados_y_convo2.pdf": "2025-04-05_conv2024_res-aprobados-1ej.pdf",
    "2024/TL_cuestionario_2do_ejerc.pdf": "2025-05-24_conv2024_2ej_cuestionario.pdf",
    "2024/Normas_generales.pdf": "2025-05-24_conv2024_2ej_normas-generales.pdf",
    "2024/nota_infor.pdf": "2025-05-24_conv2024_2ej_nota-puntuaciones.pdf",
    "2024/Cuestionario_2do_ejerc_extraordinario.pdf": "conv2024_2ej_extraordinario_cuestionario.pdf",
    # OEP 2025: first exercise 2026-03-21, second 2026-04-18
    "2025/Primer_ejercicio_AHP_Tipo_A.pdf": "2026-03-21_conv2025_tipoA_cuestionario.pdf",
    "2025/Primer_ejercicio_AHP_Tipo_B.pdf": "2026-03-21_conv2025_tipoB_cuestionario.pdf",
    "2025/Plantilla_Definitiva_TipoA.pdf": "2026-03-21_conv2025_tipoA_plantilla-definitiva.pdf",
    "2025/Plantilla_Definitiva_TipoB.pdf": "2026-03-21_conv2025_tipoB_plantilla-definitiva.pdf",
    "2025/Criterios_correccion_LIBRE_2025.pdf": "2026-03-21_conv2025_criterios-correccion.pdf",
    "2025/Instrucciones_primer_ejerTL.pdf": "2026-03-21_conv2025_instrucciones-1ej.pdf",
    "2025/NOTA_PUNTUACIONES_LIBRE.pdf": "2026-03-21_conv2025_nota-puntuaciones.pdf",
    "2025/Reso_aprobados_1er_eje_convo_2do_TL.pdf": "2026-03-21_conv2025_res-aprobados-1ej.pdf",
    "2025/Cuestionario_2do_ej_AHP_2025.pdf": "2026-04-18_conv2025_2ej_cuestionario.pdf",
    "2025/Normas_instrucciones_AHP2025.pdf": "2026-04-18_conv2025_2ej_normas-instrucciones.pdf",
    "2025/TL_Nota_informativa_pun_2ejer.pdf": "2026-04-18_conv2025_2ej_nota-puntuaciones.pdf",
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main(raw_dir: Path, url_map: Path) -> None:
    urls = dict(line.rstrip("\n").split("\t") for line in url_map.read_text().splitlines())
    DEST.mkdir(parents=True, exist_ok=True)
    rows = []
    for raw, name in PLACEMENT.items():
        src = raw_dir / raw
        shutil.copyfile(src, DEST / name)
        rows.append((name, DOWNLOAD_DATE, sha256(DEST / name), urls[raw]))
    with MANIFEST.open("w", newline="") as fh:
        writer = csv.writer(fh, delimiter="\t", lineterminator="\n")
        writer.writerow(("file", "download_date", "sha256", "url"))
        writer.writerows(sorted(rows))


if __name__ == "__main__":
    main(Path(sys.argv[1]), Path(sys.argv[2]))
