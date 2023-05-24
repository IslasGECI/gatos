import pandas as pd
import typer
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
    yearly_capture_and_effor_by_zone = get_yearly_capture_and_effort_by_zone(
        weekly_effort_and_captures_data
    )
    year_capture_and_effort = (
        yearly_capture_and_effor_by_zone.groupby(["Date"]).sum(numeric_only=True).cumsum()
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
