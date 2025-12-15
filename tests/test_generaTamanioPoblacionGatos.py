from gatos import run_population_estimator

import hashlib
import subprocess
import re
import pandas as pd
import json
import numpy as np
import os
import pytest


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
    expected_posterior = pd.read_csv("tests/data/distribucion_posterior_reference.csv")
    # pd.testing.assert_frame_equal(obtained_posterior, expected_posterior)

    loo_path = "reports/non-tabular/loo_results.json"
    obtained_loo_hash = hashlib.md5(open(loo_path, "rb").read()).hexdigest()
    expected_loo_hash = "88b5f9b02123a9466803b1e2531aaded"
    # assert obtained_loo_hash == expected_loo_hash

    obtained_waic_path = "reports/non-tabular/waic_results.json"
    expected_waic_path = "tests/data/waic_results.json"
    # assert_dict_equal_from_path(obtained_waic_path, expected_waic_path)

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
    expected_posterior = pd.read_csv("tests/data/distribucion_posterior_reference.csv")
    # pd.testing.assert_frame_equal(obtained_posterior, expected_posterior)

    obtained_loo_hash = hashlib.md5(open(loo_path, "rb").read()).hexdigest()
    # assert obtained_loo_hash == expected_loo_hash

    # assert_dict_equal_from_path(obtained_waic_path, expected_waic_path)


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
