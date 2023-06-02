import numpy as np
import pandas as pd


from gatos.remove_consecutive_non_captures import remove_consecutive_non_captures
from eradication_data_requirements import fit_ramsey_plot


def add_probability_to_effort_capture_data(data):
    data_copy = set_up_effort_capture_data(data)
    probs_status = get_status_probs(data_copy)
    data_copy.loc[5:, "prob"] = probs_status
    return data_copy


def set_up_effort_capture_data(data):
    data_copy = data.copy()
    data_copy = remove_consecutive_non_captures(data_copy)
    add_empty_column(data_copy)
    return data_copy


def add_empty_column(data_copy):
    xxadd_empty_column(data_copy)


def xxadd_empty_column(data_copy):
    data_copy["prob"] = np.nan


def add_slopes_to_effort_capture_data(data):
    data_copy = data.copy()
    data_copy = remove_consecutive_non_captures(data_copy)
    data_copy["slope"] = np.nan
    slope_status = get_status_slopes(data_copy)
    data_copy.loc[5:, "slope"] = slope_status
    return data_copy


def get_status_slopes(data):
    ramsey_time_series = set_up_ramsey_time_series(data)
    slopes_and_intercept = calculate_six_months_slope(ramsey_time_series)
    return extract_slopes(slopes_and_intercept)


def get_status_probs(data_copy):
    samples = calculate_sample_six_months_slope(data_copy)
    probs_status = extract_prob(samples)
    return probs_status


def set_up_ramsey_time_series(data):
    resized_data = remove_consecutive_non_captures(data)
    cumulative_captures = pd.DataFrame()
    cumulative_captures["Cumulative_captures"] = resized_data["Capturas"].cumsum()
    cumulative_captures["CPUE"] = resized_data["Capturas"] / resized_data["Esfuerzo"]
    return cumulative_captures[["CPUE", "Cumulative_captures"]]


def xxfit_ramsey_plotxx(data):
    fit = np.polynomial.polynomial.Polynomial.fit(data["Cumulative_captures"], data["CPUE"], deg=1)
    intercept_and_slope = fit.convert().coef
    idx = [1, 0]
    slope_and_intercept = intercept_and_slope[idx]
    return slope_and_intercept


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
    return [np.mean(samples < 0) for samples in slopes]
