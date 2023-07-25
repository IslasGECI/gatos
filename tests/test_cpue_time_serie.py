from gatos import sum_cumulative_from_column
import pandas as pd
import numpy as np


def test_sum_cumulative_from_column():
    data = pd.read_csv("tests/data/monthly_effort_and_captures.csv")
    obtained = sum_cumulative_from_column(data)
    obtained_column_names = obtained.columns
    expected_column_names = ["Fecha", "cumulative_effort", "cumulative_captures"]
    assert (obtained_column_names == expected_column_names).all()

    expected_first_cumulative = 74860
    obtained_first_cumulative = obtained.cumulative_effort[5]
    assert obtained_first_cumulative == expected_first_cumulative

    assert np.isnan(obtained.cumulative_effort[4])

    expected_first_cumulative = 78
    obtained_first_cumulative = obtained.cumulative_captures[5]
    assert obtained_first_cumulative == expected_first_cumulative
