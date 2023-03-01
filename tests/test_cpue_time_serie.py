from gatos import sum_cummulative_from_column
import pandas as pd
import numpy as np


def test_sum_cummulative_from_column():
    data = pd.read_csv("tests/data/monthly_effort_and_captures.csv")
    obtained = sum_cummulative_from_column(data)
    obtained_column_names = obtained.columns
    expected_column_names = ["Fecha", "cummulative_effort", "cummulative_captures"]
    assert (obtained_column_names == expected_column_names).all()

    expected_first_cummulative = 74860
    obtained_first_cummulative = obtained.cummulative_effort[5]
    assert obtained_first_cummulative == expected_first_cummulative

    assert np.isnan(obtained.cummulative_effort[4])

    expected_first_cummulative = 78
    obtained_first_cummulative = obtained.cummulative_captures[5]
    assert obtained_first_cummulative == expected_first_cummulative
