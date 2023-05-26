import numpy as np
import pandas as pd


def set_up_ramsey_time_series(data):
    data["Cumulative_captures"] = data["Captures"].cumsum()
    data["CPUE"] = data["Captures"] / data["Effort"]
    return data[["CPUE", "Cumulative_captures"]]


def fit_ramsey_plot(data):
    return np.polyfit(data["Cumulative_captures"], data["CPUE"], 1)


def calculate_six_months_slope(data):
    return [fit_ramsey_plot(data.iloc[(i - 6) : i]) for i in range(6, len(data) + 1)]
