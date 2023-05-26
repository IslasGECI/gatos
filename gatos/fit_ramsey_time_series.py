import pandas as pd


def set_up_ramsey_time_series(data):
    data["Cumulative_captures"] = data["Captures"].cumsum()
    data["CPUE"] = data["Captures"] / data["Effort"]
    return data[["CPUE", "Cumulative_captures"]]
