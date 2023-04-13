from gatos import run_population_estimator

import hashlib
import subprocess
import re
import pandas as pd
import json


def tests_run_population_estimator():
    posterior_path = "tests/data/distribucion_posterior.csv"
    argumentos = {
        "resource": "tests/data/monthly_effort_and_captures.csv",
        "iterations": 100,
        "output_file": posterior_path,
        "datapackage": True,
    }
    run_population_estimator(argumentos)
    loo_figure = "reports/figures/loo_diagnostic.png"
    obtained_loo_hash = hashlib.md5(open(loo_figure, "rb").read()).hexdigest()
    expected_loo_hash = "c46abaa10e432dfebe5fe516ca4e5b35"
    assert obtained_loo_hash == expected_loo_hash

    predictive_figure = "reports/figures/predictive_posterior.png"
    obtained_predictive_hash = hashlib.md5(open(predictive_figure, "rb").read()).hexdigest()
    expected_predictive_hash = "d17e1fba7eba6f76ea75c88f3c83daa4"
    assert obtained_predictive_hash == expected_predictive_hash

    obtained_posterior = pd.read_csv(posterior_path)
    expected_posterior = pd.read_csv("tests/data/distribucion_posterior_reference.csv")
    pd.testing.assert_frame_equal(obtained_posterior, expected_posterior)

    loo_path = "reports/non-tabular/loo_results.json"
    obtained_loo_hash = hashlib.md5(open(loo_path, "rb").read()).hexdigest()
    expected_loo_hash = "88b5f9b02123a9466803b1e2531aaded"
    assert obtained_loo_hash == expected_loo_hash

    waic_path = "reports/non-tabular/waic_results.json"
    obtained_waic_json = json.load(open(waic_path))
    expected_waic_json = json.load(open("tests/data/waic_results.json"))
    assert obtained_waic_json == expected_waic_json

    posterior_path = "tests/data/distribucion_posterior_without_datapackage.csv"
    argumentos = {
        "resource": "tests/data/helpers/monthly_effort_and_captures.csv",
        "iterations": 100,
        "output_file": posterior_path,
        "datapackage": False,
    }
    run_population_estimator(argumentos)
    obtained_predictive_hash = hashlib.md5(open(predictive_figure, "rb").read()).hexdigest()
    assert obtained_predictive_hash == expected_predictive_hash

    obtained_posterior = pd.read_csv(posterior_path)
    expected_posterior = pd.read_csv("tests/data/distribucion_posterior_reference.csv")
    pd.testing.assert_frame_equal(obtained_posterior, expected_posterior)

    obtained_loo_hash = hashlib.md5(open(loo_path, "rb").read()).hexdigest()
    assert obtained_loo_hash == expected_loo_hash

    obtained_waic_json = json.load(open(waic_path))
    expected_waic_json = json.load(open("tests/data/waic_results.json"))
    assert obtained_waic_json == expected_waic_json


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
    obtained_stdout = subprocess.getoutput(bash_command)
    expected = "--datapackage"
    is_there = re.search(expected, obtained_stdout)
    assert is_there
