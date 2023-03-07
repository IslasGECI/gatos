import pandas as pd
import typer
import warnings

app = typer.Typer()


@app.command()
def write_effort_and_captures_by_zone(
    input_path: str = typer.Option("", help="Input file path"),
    output_path: str = typer.Option("", help="Output file path"),
):
    weekly_effort_and_capture = pd.read_csv(input_path)
    grouped_data = get_monthly_capture_and_effort_by_zone(weekly_effort_and_capture)
    grouped_data.to_csv(output_path, index=False)


def get_capture_and_effort_by_zone(weekly_effort_and_captures_data: pd.DataFrame):
    warnings.warn(
        "Use get_monthly_capture_and_effort_by_zone() instead of get_capture_and_effort_by_zone()",
        DeprecationWarning,
    )
    return get_monthly_capture_and_effort_by_zone(weekly_effort_and_captures_data)


def get_monthly_capture_and_effort_by_zone(weekly_effort_and_captures_data: pd.DataFrame):
    return get_year_and_month_from_date(weekly_effort_and_captures_data)


def get_yearly_capture_and_effort_by_zone(weekly_effort_and_captures_data: pd.DataFrame):
    return get_year_from_date(weekly_effort_and_captures_data)


def get_year_and_month_from_date(weekly_effort_and_captures_data):
    string_length = 7
    return cut_date_string(weekly_effort_and_captures_data, string_length)


def get_year_from_date(weekly_effort_and_captures_data):
    string_length = 4
    return cut_date_string(weekly_effort_and_captures_data, string_length)


def cut_date_string(weekly_effort_and_captures_data, string_length):
    weekly_effort_and_captures_data.Fecha = weekly_effort_and_captures_data.Fecha.apply(
        lambda x: x[0:string_length]
    )
    return sum_captures_and_effort_by_date_and_zone(weekly_effort_and_captures_data)


def sum_captures_and_effort_by_date_and_zone(weekly_effort_and_captures_data):
    new_names = {"Fecha": "Date", "Zona": "Zone", "Esfuerzo": "Effort", "Capturas": "Captures"}
    weekly_effort_and_captures_data.rename(columns=new_names, inplace=True)
    capture_and_effort = weekly_effort_and_captures_data.groupby(["Date", "Zone"]).sum()
    return capture_and_effort.reset_index()
