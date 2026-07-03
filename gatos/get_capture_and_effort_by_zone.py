import numpy as np


def select_effort_and_captures_by_year(multiyear_data, year):
    return multiyear_data[multiyear_data["Date"].str.contains(year)]


def get_monthly_capture_and_effort_by_zone(weekly_effort_and_captures_data):
    string_length = 7
    return get_capture_and_effort_by_period_and_zone(weekly_effort_and_captures_data, string_length)


def get_cumulative_effort_and_captures_by_year(weekly_effort_and_captures_data):
    yearly_capture_and_effort = get_yearly_capture_and_effort_by_zone(
        weekly_effort_and_captures_data
    ).drop(columns=["Zone"])
    year_capture_and_effort = (
        yearly_capture_and_effort.groupby(["Date"]).sum(numeric_only=True).cumsum()
    )
    return year_capture_and_effort.reset_index()


def get_yearly_capture_and_effort_by_zone(weekly_effort_and_captures_data):
    string_length = 4
    return get_capture_and_effort_by_period_and_zone(weekly_effort_and_captures_data, string_length)


def get_capture_and_effort_by_period_and_zone(weekly_effort_and_captures_data, string_length):
    weekly_effort_and_captures_data.Fecha = cut_date_string(
        weekly_effort_and_captures_data, string_length
    )
    return sum_captures_and_effort_by_date_and_zone(weekly_effort_and_captures_data)


def cut_date_string(weekly_effort_and_captures_data, string_length):
    return weekly_effort_and_captures_data.Fecha.apply(lambda x: x[0:string_length])


def sum_captures_and_effort_by_date_and_zone(weekly_effort_and_captures_data):
    new_names = {"Fecha": "Date", "Zona": "Zone", "Esfuerzo": "Effort", "Capturas": "Captures"}
    weekly_effort_and_captures_data_copy = weekly_effort_and_captures_data.copy()
    weekly_effort_and_captures_data_renamed = weekly_effort_and_captures_data_copy.rename(
        columns=new_names
    )
    capture_and_effort = weekly_effort_and_captures_data_renamed.groupby(["Date", "Zone"]).sum()
    return capture_and_effort.reset_index()


def calculate_yearly_cumulative_cpue(data, years_in_data):
    effort, captures = calculate_yearly_cumulative_effort_and_captures(data, years_in_data)
    return [c / e for c, e in zip(captures, effort)]


def calculate_yearly_cumulative_effort_and_captures(datos_gatos_socorro, years_in_data):
    return xxcalculate_yearly_cumulative_effort_and_captures(datos_gatos_socorro)


def xxcalculate_yearly_cumulative_effort_and_captures(datos_gatos_socorro):
    years_in_data = years_from_data(datos_gatos_socorro)
    masks = [datos_gatos_socorro["Fecha"].str.contains(i) for i in years_in_data]
    esfuerzo_acumulado_anual = [
        calculate_cumulative_effort_by_mask(datos_gatos_socorro, mask) for mask in masks
    ]
    gatos_erradicados = [
        calculate_cumulative_captures_by_mask(datos_gatos_socorro, mask) for mask in masks
    ]
    return esfuerzo_acumulado_anual, gatos_erradicados


def calculate_cumulative_effort_by_mask(data, mask):
    return np.sum(data["Esfuerzo"].values[mask])


def calculate_cumulative_captures_by_mask(data, mask):
    return np.sum(data["Capturas"].values[mask])


def years_from_data(dataframe):
    years = dataframe.Fecha.str.slice(stop=4)
    return years.unique()
