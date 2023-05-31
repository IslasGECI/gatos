import pandas as pd

from gatos import get_non_captures_index


def test_get_non_captures_index():
    singular_data = pd.DataFrame(
        {"Esfuerzo": [2, 2, 2, 2, 2, 2, 1, 2, 3], "Capturas": [1, 0, 0, 0, 2, 1, 0, 0, 1]}
    )
    obtained = get_non_captures_index(singular_data)
    expected = [1, 2, 3, 6, 7]
    assert obtained == expected
