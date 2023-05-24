from gatos import (
    get_capture_and_effort_by_zone,
    get_cummulative_effort_and_captures_by_year,
    get_yearly_capture_and_effort_by_zone,
    select_effort_and_captures_by_year,
    write_effort_and_captures_by_zone_for_year,
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

    expected_dates = ["2022-03", "2023-01", "2023-02", "2023-03"]
    obtained_dates = obtained.Date.unique()
    assert (expected_dates == obtained_dates).all()

    expected_length = 18
    obtained_length = len(obtained)
    assert obtained_length == expected_length


weekly_effort_and_captures_data = pd.read_csv(input_path)


def test_get_yearly_capture_and_effort_by_zone():
    obtained = get_yearly_capture_and_effort_by_zone(weekly_effort_and_captures_data)
    expected_columns = ["Date", "Zone", "Effort", "Captures"]
    obtained_columns = obtained.columns
    assert (obtained_columns == expected_columns).all()

    expected_dates = ["2022", "2023"]
    obtained_dates = obtained.Date.unique()
    assert (expected_dates == obtained_dates).all()

    expected_length = 11
    obtained_length = len(obtained)
    assert obtained_length == expected_length


def test_get_cummulative_effort_and_captures_by_year():
    weekly_effort_and_captures_data = pd.read_csv(input_path)
    obtained = get_cummulative_effort_and_captures_by_year(weekly_effort_and_captures_data)
    obtained_captures_2022 = obtained[obtained.Date == "2022"].Captures[0]
    expected_captures_2022 = 6
    assert obtained_captures_2022 == expected_captures_2022


def test_select_effort_and_captures_by_year():
    multiyear_data = pd.read_csv(
        "tests/data/yearly_capture_and_effort_by_zone.csv", dtype={"Date": str}
    )
    year = "2022"
    selected_data = select_effort_and_captures_by_year(multiyear_data, year)
    expected_length = 8
    obtained_length = len(selected_data)
    assert obtained_length == expected_length


def test_write_effort_and_captures_by_zone():
    output_path = "tests/data/effort_and_captures_by_zone.csv"
    if os.path.exists(output_path):
        os.remove(output_path)
    year = "2022"
    write_effort_and_captures_by_zone_for_year(input_path, output_path, year)
    assert os.path.exists(output_path)
