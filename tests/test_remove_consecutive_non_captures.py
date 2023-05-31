import pandas as pd

from gatos import get_non_captures_index


def test_get_non_captures_index():
    singular_data = pd.DataFrame({"Esfuerzo": [2, 2, 2, 2, 2, 2], "Capturas": [1, 0, 0, 0, 2, 1]})
    get_non_captures_index(singular_data)
