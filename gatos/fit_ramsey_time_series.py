import pandas as pd


def set_up_ramsey_time_series(data):
    data["Captures"] = data["Captures"].cumsum()
    data["CPUE"] = 0
    return data[["CPUE", "Captures"]]
