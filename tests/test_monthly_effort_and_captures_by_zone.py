from gatos import get_capture_and_effort_by_zone

import pandas as pd


def test_get_capture_and_effort_by_zone():
    weekly_effort_and_captures_data = pd.read_csv(
        "tests/data/esfuerzo_capturas_semanales_iso8601.csv"
    )
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
