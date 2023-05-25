import pandas as pd

data = pd.DataFrame({"Effort": [1, 2, 3, 4, 5, 6], "Captures": [1, 1, 1, 1, 1, 1]})


def test_set_up_ramsey_time_series():
    expected = pd.DataFrame(
        {"CPUE": [1, 1 / 2, 1 / 3, 1 / 4, 1 / 5, 1 / 6], "Captures": [1, 2, 3, 4, 5, 6]}
    )
    obtained = set_up_ramsey_time_series(data)
