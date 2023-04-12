from gatos import run_population_estimator

import hashlib
import subprocess
import re


def tests_run_population_estimatior():
    argumentos = {
        "resource": "tests/data/monthly_effort_and_captures.csv",
        "iterations": 2,
        "output_file": "tests/data/distribucion_posterior.csv",
        "datapackage": True,
    }
    run_population_estimator(argumentos)
    loo_figure = "reports/figures/loo_diagnostic.png"
    obtained_leo_hash = hashlib.md5(open(loo_figure, "rb").read()).hexdigest()
    expected_leo_hash = "c46abaa10e432dfebe5fe516ca4e5b35"
    assert obtained_leo_hash == expected_leo_hash
    predictive_figure = "reports/figures/predictive_posterior.png"
    obtained_predictive_hash = hashlib.md5(open(predictive_figure, "rb").read()).hexdigest()
    expected_predictive_hash = "d6013174542c7e938614dab98dacd23b"
    assert obtained_predictive_hash == expected_predictive_hash
    posterior_path = "tests/data/distribucion_posterior.csv"
    obtained_posterior_hash = hashlib.md5(open(posterior_path, "rb").read()).hexdigest()
    expected_posterior_hash = "5a33180e99bda7417b4e40d9330776bb"
    assert obtained_posterior_hash == expected_posterior_hash
    loo_path = "reports/non-tabular/loo_results.json"
    obtained_loo_hash = hashlib.md5(open(loo_path, "rb").read()).hexdigest()
    expected_loo_hash = "93c387c99bd41bb7c4cb9288d7a46e9c"
    assert obtained_loo_hash == expected_loo_hash
    waic_path = "reports/non-tabular/waic_results.json"
    obtained_waic_hash = hashlib.md5(open(waic_path, "rb").read()).hexdigest()
    expected_waic_hash = "c132351ac68fda1aca6b4354145de8bb"
    assert obtained_waic_hash == expected_waic_hash

    argumentos = {
        "resource": "tests/data/helpers/monthly_effort_and_captures.csv",
        "iterations": 2,
        "output_file": "tests/data/distribucion_posterior_without_datapackage.csv",
        "datapackage": False,
    }
    run_population_estimator(argumentos)
    assert False
    predictive_figure = "reports/figures/predictive_posterior.png"
    obtained_predictive_hash = hashlib.md5(open(predictive_figure, "rb").read()).hexdigest()
    expected_predictive_hash = "967d7b046bdc6f969d113be3e91a7d66"
    assert obtained_predictive_hash == expected_predictive_hash
    posterior_path = "tests/data/distribucion_posterior_without_datapackage.csv"
    obtained_posterior_hash = hashlib.md5(open(posterior_path, "rb").read()).hexdigest()
    expected_posterior_hash = "5a33180e99bda7417b4e40d9330776bb"
    assert obtained_posterior_hash == expected_posterior_hash
    loo_path = "reports/non-tabular/loo_results.json"
    obtained_loo_hash = hashlib.md5(open(loo_path, "rb").read()).hexdigest()
    expected_loo_hash = "87cbf7ed36665dbad50b0345261373c4"
    assert obtained_loo_hash == expected_loo_hash
    waic_path = "reports/non-tabular/waic_results.json"
    obtained_waic_hash = hashlib.md5(open(waic_path, "rb").read()).hexdigest()
    expected_waic_hash = "e45b2d2989895acd81f386c7b36264f3"
    assert obtained_waic_hash == expected_waic_hash


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
