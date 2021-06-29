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