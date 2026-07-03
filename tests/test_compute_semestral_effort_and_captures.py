from gatos.compute_semestral_effort_and_captures import (
    compute_semestral_effort_and_captures,
    compute_semestral_cumulative_effort_and_captures,
)
import pandas as pd


def test_compute_semestral_effort_and_captures():
    effort_and_captures_df = pd.read_csv("tests/data/esfuerzo_capturas_semanales_iso8601.csv")
    obtained = compute_semestral_effort_and_captures(effort_and_captures_df)
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
    obtained = compute_semestral_cumulative_effort_and_captures(semestral_effort_and_captures)
    expected_effort = [100, 300, 600]
    assert list(obtained["Esfuerzo"]) == expected_effort
    assert list(obtained["CPUE"]) == cpue_values
