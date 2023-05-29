import numpy as np


def get_status_slopes(data):
    ramsey_time_series = set_up_ramsey_time_series(data)
    slopes_and_origin = calculate_six_months_slope(ramsey_time_series)
    return extract_slopes(slopes_and_origin)


def set_up_ramsey_time_series(data):
    data["Cumulative_captures"] = data["Capturas"].cumsum()
    data["CPUE"] = data["Capturas"] / data["Esfuerzo"]
    return data[["CPUE", "Cumulative_captures"]]


def fit_ramsey_plot(data):
    return np.polyfit(data["Cumulative_captures"], data["CPUE"], 1)


def calculate_six_months_slope(data):
    window_length = 6
    return [
        fit_ramsey_plot(data.iloc[(i - window_length) : i])
        for i in range(window_length, len(data) + 1)
    ]


def extract_slopes(slopes_origin_data):
    return [slope[0] for slope in slopes_origin_data]
