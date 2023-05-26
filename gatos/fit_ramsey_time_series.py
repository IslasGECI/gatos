import numpy as np


def set_up_ramsey_time_series(data):
    data["Cumulative_captures"] = data["Captures"].cumsum()
    data["CPUE"] = data["Captures"] / data["Effort"]
    return data[["CPUE", "Cumulative_captures"]]


def fit_ramsey_plot(data):
    return np.polyfit(data["Cumulative_captures"], data["CPUE"], 1)


def calculate_six_months_slope(data):
    window_length = 6
    return [
        fit_ramsey_plot(data.iloc[(i - window_length) : i])
        for i in range(window_length, len(data) + 1)
    ]
