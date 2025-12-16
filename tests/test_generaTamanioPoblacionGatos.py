from gatos import run_population_estimator

import subprocess
import re
import json
import numpy as np
import os
import pytest
import pandas as pd
import math


@pytest.mark.slow
def tests_run_population_estimator():
    posterior_path = "tests/data/distribucion_posterior.csv"
    argumentos = {
        "resource": "tests/data/monthly_effort_and_captures.csv",
        "iterations": 100,
        "output_file": posterior_path,
        "datapackage": True,
    }

    loo_figure = "reports/figures/loo_diagnostic.png"
    predictive_figure = "reports/figures/predictive_posterior.png"
    remove_file_if_exists(loo_figure)
    remove_file_if_exists(predictive_figure)

    run_population_estimator(argumentos)

    assert os.path.exists(loo_figure)
    assert os.path.exists(predictive_figure)

    obtained_posterior = pd.read_csv(posterior_path)
    expected_columns = ["a", "b", "No"]
    assert expected_columns in obtained_posterior.columns.values
    obtained_means = obtained_posterior.mean()
    expected_mean_alpha = -9.065199
    assert math.isclose(expected_mean_alpha, obtained_means.a, rel_tol=1e-6)
    expected_mean_beta = -0.003879
    assert math.isclose(expected_mean_beta, obtained_means.b, rel_tol=1e-4)
    expected_mean_No = 14787
    assert math.isclose(expected_mean_No, obtained_means.No, rel_tol=1e-3)

    posterior_path = "tests/data/distribucion_posterior_without_datapackage.csv"
    argumentos = {
        "resource": "tests/data/helpers/monthly_effort_and_captures.csv",
        "iterations": 100,
        "output_file": posterior_path,
        "datapackage": False,
    }

    remove_file_if_exists(predictive_figure)

    run_population_estimator(argumentos)

    assert os.path.exists(predictive_figure)

    obtained_posterior = pd.read_csv(posterior_path)
    expected_columns = ["a", "b", "No"]
    assert expected_columns in obtained_posterior.columns.values
    obtained_means = obtained_posterior.mean()
    expected_mean_alpha = -9.065199
    assert math.isclose(expected_mean_alpha, obtained_means.a, rel_tol=1e-6)
    expected_mean_beta = -0.003879
    assert math.isclose(expected_mean_beta, obtained_means.b, rel_tol=1e-4)
    expected_mean_No = 14787
    assert math.isclose(expected_mean_No, obtained_means.No, rel_tol=1e-3)


def remove_file_if_exists(file_path):
    if os.path.exists(file_path):
        os.remove(file_path)


def assert_dict_equal_from_path(obtained_waic_path, expected_waic_path):
    obtained_waic_json = json.load(open(obtained_waic_path))
    expected_waic_json = json.load(open(expected_waic_path))
    assert_dict_equal(obtained_waic_json, expected_waic_json)


def assert_dict_equal(obtained_dict, expected_dict):
    np.testing.assert_allclose(list(obtained_dict.values()), list(expected_dict.values()))


@pytest.mark.slow()
def test_crea_tamagno_poblacion_gatos_help():
    expected = "inicial$"
    bash_command = "crea_tamagno_poblacion_gatos --help"
    subprocess.check_call(bash_command, shell=True)
    obtained_version = subprocess.getoutput(bash_command)
    is_there = re.search(expected, obtained_version)
    assert is_there


@pytest.mark.slow
def test_crea_tamagno_poblacion_gatos_calculate_help():
    bash_command = "crea_tamagno_poblacion_gatos calculate --help"
    subprocess.check_call(bash_command, shell=True)
    obtained_stdout = subprocess.getoutput(bash_command)
    expected = "--datapackage"
    is_there = re.search(expected, obtained_stdout)
    assert is_there
