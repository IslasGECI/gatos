from gatos import (
    write_effort_and_captures_by_zone_for_year,
    write_effort_and_captures_with_probability,
    write_effort_and_captures_with_slopes,
    write_progress_probability_figure,
    write_yearly_cumulative_effort_and_captures,
)

import numpy as np
import pandas as pd
import os
import hashlib

np.reshape
input_path = "tests/data/esfuerzo_capturas_semanales_iso8601.csv"


def test_write_effort_and_captures_by_zone():
    output_path = "tests/data/effort_and_captures_by_zone.csv"
    if os.path.exists(output_path):
        os.remove(output_path)
    year = "2022"
    write_effort_and_captures_by_zone_for_year(input_path, output_path, year)
    assert os.path.exists(output_path)


def test_write_effort_and_capture_with_probability():
    output_path = "tests/data/probability_time_series.csv"
    monthly_path = "tests/data/esfuerzo_capturas_mensuales_gatos_socorro.csv"
    if os.path.exists(output_path):
        os.remove(output_path)
    write_effort_and_captures_with_probability(monthly_path, output_path)
    assert os.path.exists(output_path)
    obtained = pd.read_csv(output_path)

    obtained_probability = obtained.prob
    expected_probability = pd.Series(
        [
            np.nan,
            np.nan,
            np.nan,
            np.nan,
            np.nan,
            1 / 6,
            1.0,
            1.0,
            5 / 6,
            1 / 2,
        ],
        name="prob",
    )
    pd.testing.assert_series_equal(obtained_probability, expected_probability)


def test_write_effort_and_capture_with_slopes():
    output_path = "tests/data/slope_time_series.csv"
    monthly_path = "tests/data/esfuerzo_capturas_mensuales_gatos_socorro.csv"
    if os.path.exists(output_path):
        os.remove(output_path)
    write_effort_and_captures_with_slopes(monthly_path, output_path)
    assert os.path.exists(output_path)
    obtained = pd.read_csv(output_path)

    obtained_slopes = obtained.slope
    expected_slopes = pd.Series(
        [
            np.nan,
            np.nan,
            np.nan,
            np.nan,
            np.nan,
            4.739e-6,
            -1.117e-5,
            -9.646e-6,
            -5.082e-5,
            -2.781e-6,
        ],
        name="slope",
    )
    pd.testing.assert_series_equal(obtained_slopes, expected_slopes)


def test_write_yearly_cumulative_effort_and_captures():
    output_path = "tests/data/yearly_cumulative_effort_and_captures.csv"
    if os.path.exists(output_path):
        os.remove(output_path)
    write_yearly_cumulative_effort_and_captures(input_path, output_path)
    assert os.path.exists(output_path)
    obtained_csv = pd.read_csv(output_path)
    obtained_columns = obtained_csv.columns
    expected_columns = ["Date", "Effort", "Cumulative_captures", "CPUE"]
    assert (obtained_columns == expected_columns).all()
    expected_hash = "f91474bc36b1cf3c78174a9ad2f202ba"
    obtained_hash = hashlib.md5(open(output_path, "rb").read()).hexdigest()
    assert obtained_hash == expected_hash, "Hash of csv with cumulative effort an captures"


def test_write_progress_probability_figure():
    data_path = "tests/data/progress_probability_tests.csv"
    figure_path = "tests/data/progress_probability_tests.png"

    if os.path.exists(figure_path):
        os.remove(figure_path)

    write_progress_probability_figure(data_path, figure_path)

    os.path.exists(figure_path)
    os.remove(figure_path)
