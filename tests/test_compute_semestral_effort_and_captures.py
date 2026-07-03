from gatos.compute_semestral_effort_and_captures import compute_semestral_effort_and_captures
import pandas as pd


def test_compute_semestral_effort_and_captures():
    effort_and_captures_df = pd.read_csv("tests/data/esfuerzo_capturas_semanales_iso8601.csv")
    obtained = compute_semestral_effort_and_captures(effort_and_captures_df)
    expected_rows = 2
    assert len(obtained) == expected_rows, f"Expected {expected_rows} rows, but got {len(obtained)}"
    expected_columns = ["Esfuerzo", "Capturas"]
    assert obtained.columns == expected_columns
