import subprocess
import re
import pytest


@pytest.mark.slow
def test_crea_tabla_pvalor():
    expected = "gatos$"
    bash_command = "crea_tabla_pvalor --help"
    subprocess.check_call(bash_command, shell=True)
    obtained_version = subprocess.getoutput(bash_command)
    is_there = re.search(expected, obtained_version)
    assert is_there
