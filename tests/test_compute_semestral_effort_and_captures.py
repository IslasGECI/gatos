from gatos.compute_semestral_effort_and_captures import (
    compute_effort_and_captures_and_cpue_by_resolution,
    compute_cumulative_effort_and_captures,
)
from gatos.gatos_cli import compute_CPUE_and_cumulative_effort_and_captures_by_resolution
import pandas as pd


def test_compute_semestral_CPUE_and_cumulative_effort_and_captures():
    effort_and_captures_df = pd.DataFrame(
        {
            "Capturas": [10, 20, 30],
            "Esfuerzo": [100, 200, 300],
            "Fecha": ["2022-01-02", "2022-07-08", "2023-01-02"],
        }
    )
    resolution = "semestral"
    obtained = compute_CPUE_and_cumulative_effort_and_captures_by_resolution(
        effort_and_captures_df, resolution
    )
    expected_rows = 3
    assert len(obtained) == expected_rows, f"Expected {expected_rows} rows, but got {len(obtained)}"
    expected_columns = ["Esfuerzo", "Capturas", "CPUE"]
    assert all(obtained.columns == expected_columns)
    assert obtained.index[0] == "2022-P1"
    expected_effort = [100, 300, 600]
    assert list(obtained["Esfuerzo"]) == expected_effort
    expected_cpue_values = [0.1, 0.1, 0.1]
    assert list(obtained["CPUE"]) == expected_cpue_values


def test_compute_semestral_effort_and_captures():
    effort_and_captures_df = pd.read_csv("tests/data/esfuerzo_capturas_semanales_iso8601.csv")
    resolution = 6
    obtained = compute_effort_and_captures_and_cpue_by_resolution(
        effort_and_captures_df, resolution
    )
    expected_rows = 2
    assert len(obtained) == expected_rows, f"Expected {expected_rows} rows, but got {len(obtained)}"
    expected_columns = ["Esfuerzo", "Capturas", "CPUE"]
    assert all(obtained.columns == expected_columns)
    assert obtained.index[0] == "2022-P1"


def test_compute_semestral_cumulative_effort_and_captures():
    cpue_values = [0.1, 0.1, 0.1]
    semestral_effort_and_captures = pd.DataFrame(
        {"Capturas": [10, 20, 30], "Esfuerzo": [100, 200, 300], "CPUE": cpue_values},
        index=["2022-P1", "2022-P2", "2022-P3"],
    )
    obtained = compute_cumulative_effort_and_captures(semestral_effort_and_captures)
    expected_effort = [100, 300, 600]
    assert list(obtained["Esfuerzo"]) == expected_effort
    assert list(obtained["CPUE"]) == cpue_values
