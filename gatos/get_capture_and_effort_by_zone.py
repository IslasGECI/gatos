import pandas as pd


def get_capture_and_effort_by_zone(weekly_effort_and_captures_data: pd.DataFrame):
    weekly_effort_and_captures_data.Fecha = weekly_effort_and_captures_data.Fecha.apply(
        lambda x: x[0:7]
    )
    new_names = {"Fecha": "Date", "Zona": "Zone", "Esfuerzo": "Effort", "Capturas": "Captures"}
    weekly_effort_and_captures_data.rename(columns=new_names, inplace=True)
    capture_and_effort = weekly_effort_and_captures_data.groupby(["Date", "Zone"]).sum()
    return capture_and_effort.reset_index()
