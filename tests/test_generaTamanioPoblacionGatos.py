import metadatatools
from pandas.util.testing import assert_frame_equal
from gatos.generaTamanioPoblacionGatos import *
import subprocess
import re


def test_crea_tamagno_poblacion_gatos_help():
    expected = "inicial$"
    bash_command = "crea_tamagno_poblacion_gatos --help"
    subprocess.check_call(bash_command, shell=True)
    obtained_version = subprocess.getoutput(bash_command)
    is_there = re.search(expected, obtained_version)
    assert is_there


def test_crea_tamagno_poblacion_gatos_calculate_help():
    bash_command = "crea_tamagno_poblacion_gatos calculate --help"
    subprocess.check_call(bash_command, shell=True)


def test_get_effort():
    datosSocorro = metadatatools.import_tabular_data_resource(
        "tests/data/esfuerzos_capturas_gatos_socorro/esfuerzo_capturas_mensuales_gatos_socorro.csv"
    )
    obtained_effort = get_effort("Esfuerzo", datosSocorro)
    expected_effort = 25725
    assert_frame_equal(expected_effort, obtained_effort)
