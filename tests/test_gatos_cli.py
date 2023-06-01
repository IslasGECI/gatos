from gatos import (
    write_effort_and_captures_by_zone_for_year,
    write_effort_and_captures_with_probability,
    write_effort_and_captures_with_slopes,
    write_yearly_cummulative_effort_and_captures,
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


def test_write_yearly_cummulative_effort_and_captures():
    output_path = "tests/data/yearly_cummulative_effort_and_captures.csv"
    if os.path.exists(output_path):
        os.remove(output_path)
    write_yearly_cummulative_effort_and_captures(input_path, output_path)
    assert os.path.exists(output_path)
    expected_hash = "9a4aaa1cf8d7d30c64521ca2fe727b7b"
    obtained_hash = hashlib.md5(open(output_path, "rb").read()).hexdigest()
    assert obtained_hash == expected_hash, "Hash of csv with cumulative effort an captures"
