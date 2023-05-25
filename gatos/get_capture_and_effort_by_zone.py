import pandas as pd
import typer
import numpy as np
import warnings

app = typer.Typer()


@app.command()
def write_effort_and_captures_by_zone_for_year(
    input_path: str = typer.Option("", help="Input file path"),
    output_path: str = typer.Option("", help="Output file path"),
    year: str = typer.Option("2022", help="Year of interest"),
):
    weekly_effort_and_capture = pd.read_csv(input_path)
    grouped_data = get_yearly_capture_and_effort_by_zone(weekly_effort_and_capture)
    data_for_year = select_effort_and_captures_by_year(grouped_data, year)
    data_for_year.to_csv(output_path, index=False)


@app.command()
def write_yearly_cummulative_effort_and_captures(
    input_path: str = typer.Option("", help="Input file path"),
    output_path: str = typer.Option("", help="Output file path"),
):
    weekly_effort_and_capture = pd.read_csv(input_path)
    cummulatie_effort_and_capture = get_cummulative_effort_and_captures_by_year(
        weekly_effort_and_capture
    )
    cummulatie_effort_and_capture.to_csv(output_path, index=False)


def select_effort_and_captures_by_year(multiyear_data, year):
    return multiyear_data[multiyear_data["Date"].str.contains(year)]


def get_capture_and_effort_by_zone(weekly_effort_and_captures_data: pd.DataFrame):
    warnings.warn(
        "Use get_monthly_capture_and_effort_by_zone() instead of get_capture_and_effort_by_zone()",
        DeprecationWarning,
    )
    return get_monthly_capture_and_effort_by_zone(weekly_effort_and_captures_data)


def get_monthly_capture_and_effort_by_zone(weekly_effort_and_captures_data):
    string_length = 7
    return get_capture_and_effort_by_period_and_zone(weekly_effort_and_captures_data, string_length)


def get_cummulative_effort_and_captures_by_year(weekly_effort_and_captures_data):
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


def calculate_yearly_cumulative_effort_and_captures(datos_gatos_socorro, years_in_data):
    masks = [datos_gatos_socorro["Fecha"].str.contains(i) for i in years_in_data]
    esfuerzo_acumulado_anual = [
        calculate_yearly_cumulative_effort(datos_gatos_socorro, mask) for mask in masks
    ]
    gatos_erradicados = [
        calculate_yearly_cumulative_captures(datos_gatos_socorro, mask) for mask in masks
    ]
    return esfuerzo_acumulado_anual, gatos_erradicados


def calculate_yearly_cumulative_effort(data, mask):
    return np.sum(data["Esfuerzo"].values[mask])


def calculate_yearly_cumulative_captures(data, mask):
    return np.sum(data["Capturas"].values[mask])


def years_from_data(dataframe):
    years = dataframe.Fecha.str.slice(stop=4)
    return years.unique()