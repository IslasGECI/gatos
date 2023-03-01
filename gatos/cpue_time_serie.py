import pandas as pd


def sum_cummulative_from_column(monthly_effort_capture: pd.DataFrame):
    monthly_effort_capture["cummulative_effort"] = rolling_sum(monthly_effort_capture, "Esfuerzo")
    monthly_effort_capture["cummulative_captures"] = rolling_sum(monthly_effort_capture, "Capturas")
    return drop_effort_captures_and_trappers(monthly_effort_capture)


def drop_effort_captures_and_trappers(data):
    return data.drop(["Esfuerzo", "Capturas", "Tramperos"], axis=1)


def rolling_sum(data, column, rolling_months=6):
    return data[column].rolling(rolling_months).sum()
