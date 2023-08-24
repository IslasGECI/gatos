from gatos import plot_progress_probability

import pandas as pd


def test_plot_progress_probability():
    data = pd.read_csv("tests/data/progress_probability_tests.csv")
    plot_progress_probability(data)
