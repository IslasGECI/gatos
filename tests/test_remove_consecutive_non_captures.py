import pandas as pd

from gatos import get_last_cumsum, get_non_captures_index, split_non_consecutive_indexes


singular_data = pd.DataFrame(
    {"Esfuerzo": [2, 2, 2, 2, 2, 2, 1, 2, 3], "Capturas": [1, 0, 0, 0, 2, 1, 0, 0, 1]}
)


def test_get_non_captures_index():
    obtained = get_non_captures_index(singular_data)
    expected = [1, 2, 3, 6, 7]
    assert obtained == expected


def test_split_non_consecutive_indexes():
    index_list = [1, 2, 5, 6, 9]
    obtained = split_non_consecutive_indexes(index_list)
    expected = [[1, 2], [5, 6], [9]]
    assert obtained == expected


def test_get_last_cumsum():
    index_list = [[1, 2, 3], [6, 7]]
    obtained = get_last_cumsum(singular_data, index_list[0])
    expected_effort = 6
    assert obtained.Esfuerzo == expected_effort
