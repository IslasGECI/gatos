from gatos import (
    get_capture_and_effort_by_zone,
    write_effort_and_captures_by_zone,
    get_yearly_capture_and_effort_by_zone,
)

import pandas as pd
import os


input_path = "tests/data/esfuerzo_capturas_semanales_iso8601.csv"


def test_get_capture_and_effort_by_zone():
    weekly_effort_and_captures_data = pd.read_csv(input_path)
    obtained = get_capture_and_effort_by_zone(weekly_effort_and_captures_data)
    expected_columns = ["Date", "Zone", "Effort", "Captures"]
    obtained_columns = obtained.columns
    assert (obtained_columns == expected_columns).all()

    expected_dates = ["2023-01", "2023-02", "2023-03"]
    obtained_dates = obtained.Date.unique()
    assert (expected_dates == obtained_dates).all()

    expected_length = 15
    obtained_length = len(obtained)
    assert obtained_length == expected_length


def test_get_yearly_capture_and_effort_by_zone():
    weekly_effort_and_captures_data = pd.read_csv(input_path)
    obtained = get_yearly_capture_and_effort_by_zone(weekly_effort_and_captures_data)
    expected_columns = ["Date", "Zone", "Effort", "Captures"]
    obtained_columns = obtained.columns
    assert (obtained_columns == expected_columns).all()

    expected_dates = ["2023"]
    obtained_dates = obtained.Date.unique()
    assert (expected_dates == obtained_dates).all()

    expected_length = 8
    obtained_length = len(obtained)
    assert obtained_length == expected_length

    assert False


def test_write_effort_and_captures_by_zone():
    output_path = "tests/data/effort_and_captures_by_zone.csv"
    write_effort_and_captures_by_zone(input_path, output_path)
    assert os.path.exists(output_path)
