import pandas as pd
import numpy as np

from gatos import (
    add_slopes_to_effort_capture_data,
    calculate_six_months_slope,
    extract_slopes,
    fit_ramsey_plot,
    get_status_slopes,
    set_up_ramsey_time_series,
)


data = pd.DataFrame({"Esfuerzo": [1, 2, 3, 4, 5, 6], "Capturas": [1, 1, 1, 1, 1, 1]})


def test_add_slopes_to_effort_capture_data():
    obtained = add_slopes_to_effort_capture_data(data)
    contains_slope_column = "slope" in obtained.columns
    assert contains_slope_column == True
    obtained_no_nan = obtained.slope.count()
    expected_no_nan = 1
    assert obtained_no_nan == expected_no_nan

    effort_and_capture_data = pd.read_csv(
        "tests/data/esfuerzo_capturas_mensuales_gatos_socorro.csv"
    )
    obtained = add_slopes_to_effort_capture_data(effort_and_capture_data)
    obtained_first_slope = obtained.slope.iloc[5]
    expected_first_slope = 0.000005
    print(obtained_first_slope)
    assert obtained_first_slope == expected_first_slope


def test_get_status_slopes():
    obtained = get_status_slopes(data)
    obtained_len = len(obtained)
    expected_len = 1
    assert obtained_len == expected_len


def test_set_up_ramsey_time_series():
    expected = pd.DataFrame(
        {"CPUE": [1, 1 / 2, 1 / 3, 1 / 4, 1 / 5, 1 / 6], "Cumulative_captures": [1, 2, 3, 4, 5, 6]}
    )
    obtained = set_up_ramsey_time_series(data)
    assert (obtained.columns == ["CPUE", "Cumulative_captures"]).all()
    assert (obtained.Cumulative_captures == expected.Cumulative_captures).all()
    assert (obtained.CPUE == expected.CPUE).all()

    data_2 = pd.DataFrame({"Esfuerzo": [2, 2, 2, 2, 2, 2], "Capturas": [1, 2, 1, 1, 2, 1]})
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


def test_calculate_six_months_slope():
    ramsey_time_series = pd.DataFrame(
        {
            "CPUE": [
                1,
                1 / 2,
                1 / 3,
                1 / 4,
                1 / 5,
                1 / 6,
                1 / 2,
                2 / 2,
                1 / 2,
                1 / 2,
                2 / 2,
                1 / 2,
            ],
            "Cumulative_captures": [1, 2, 3, 4, 5, 6, 7, 9, 10, 11, 13, 14],
        }
    )
    obtained_slopes = calculate_six_months_slope(ramsey_time_series)
    expected_number_slopes = 7
    obtained_number_slopes = len(obtained_slopes)
    assert obtained_number_slopes == expected_number_slopes


def test_extract_slopes():
    slopes_and_intercept = [np.array([1, 2]), np.array([3, 4]), np.array([5, 6])]
    expected_slopes = [1, 3, 5]
    obtained_slopes = extract_slopes(slopes_and_intercept)
    assert obtained_slopes == expected_slopes
