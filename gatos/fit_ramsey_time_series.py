import numpy as np


def add_probability_to_effort_capture_data(data):
    data["prob"] = np.nan
    samples = calculate_sample_six_months_slope(data)
    probs_status = extract_prob(samples)
    data.loc[5:, "prob"] = probs_status
    return data


def add_slopes_to_effort_capture_data(data):
    data["slope"] = np.nan
    slope_status = get_status_slopes(data)
    data.loc[5:, "slope"] = slope_status
    return data


def get_status_slopes(data):
    ramsey_time_series = set_up_ramsey_time_series(data)
    slopes_and_intercept = calculate_six_months_slope(ramsey_time_series)
    return extract_slopes(slopes_and_intercept)


def set_up_ramsey_time_series(data):
    data["Cumulative_captures"] = data["Capturas"].cumsum()
    data["CPUE"] = data["Capturas"] / data["Esfuerzo"]
    return data[["CPUE", "Cumulative_captures"]]


def fit_ramsey_plot(data):
    return np.polyfit(data["Cumulative_captures"], data["CPUE"], 1)


def sample_fit_ramsey_plot(datos):
    fits = [fit_ramsey_plot(set_up_ramsey_time_series(datos.drop(i))) for i in datos.index]
    return fits


def calculate_sample_six_months_slope(ramsey_series):
    window_length = 6
    return [
        sample_fit_ramsey_plot(ramsey_series.iloc[(i - window_length) : i])
        for i in range(window_length, len(ramsey_series) + 1)
    ]


def calculate_six_months_slope(data):
    window_length = 6
    return [
        fit_ramsey_plot(data.iloc[(i - window_length) : i])
        for i in range(window_length, len(data) + 1)
    ]


def extract_slopes(slopes_intercept_data):
    return [slope[0] for slope in slopes_intercept_data]


def extract_prob(slopes_intercept_data):
    slopes = [np.asarray(extract_slopes(sample)) for sample in slopes_intercept_data]
    return [np.mean(samples > 0) for samples in slopes]
