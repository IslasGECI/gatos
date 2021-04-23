import subprocess


def test_nothing():
    bash_command = f"python gatos/tabla_p_valor_erradicacion_gatos.py --help"
    subprocess.check_call(bash_command, shell=True)
