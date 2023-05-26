import pandas as pd
import numpy as np

from gatos import fit_ramsey_plot, set_up_ramsey_time_series


data = pd.DataFrame({"Effort": [1, 2, 3, 4, 5, 6], "Captures": [1, 1, 1, 1, 1, 1]})


def test_set_up_ramsey_time_series():
    expected = pd.DataFrame(
        {"CPUE": [1, 1 / 2, 1 / 3, 1 / 4, 1 / 5, 1 / 6], "Cumulative_captures": [1, 2, 3, 4, 5, 6]}
    )
    obtained = set_up_ramsey_time_series(data)
    assert (obtained.columns == ["CPUE", "Cumulative_captures"]).all()
    assert (obtained.Cumulative_captures == expected.Cumulative_captures).all()
    assert (obtained.CPUE == expected.CPUE).all()

    data_2 = pd.DataFrame({"Effort": [2, 2, 2, 2, 2, 2], "Captures": [1, 2, 1, 1, 2, 1]})
    obtained = set_up_ramsey_time_series(data_2)

    expected = pd.DataFrame(
        {
            "CPUE": [1 / 2, 2 / 2, 1 / 2, 1 / 2, 2 / 2, 1 / 2],
            "Cumulative_captures": [1, 3, 4, 5, 7, 8],
        }
    )
    assert (obtained.Cumulative_captures == expected.Cumulative_captures).all()


def test_fit_ramsey_plot():
    data = pd.DataFrame(
        {"CPUE": [19.5, 19, 18.5, 18, 17.5, 17], "Cumulative_captures": [1, 2, 3, 4, 5, 6]}
    )
    obtained_parameters = fit_ramsey_plot(data)
    expected_parameters = np.array([-0.5, 20.0])
    np.testing.assert_array_almost_equal(obtained_parameters, expected_parameters)
