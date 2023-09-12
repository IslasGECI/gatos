from gatos.fit_ramsey_time_series import (
    add_slopes_to_effort_capture_data,
    get_status_probs,
)
from gatos.get_capture_and_effort_by_zone import (
    calculate_yearly_cumulative_cpue,
    get_cumulative_effort_and_captures_by_year,
    get_yearly_capture_and_effort_by_zone,
    select_effort_and_captures_by_year,
    years_from_data,
)
from gatos.plot_progress_probability import plot_progress_probability

import pandas as pd
import typer
import matplotlib.pyplot as plt

app = typer.Typer()


@app.command()
def write_progress_probability_figure(
    data_path: str = typer.Option("", help="Input file path"),
    figure_path: str = typer.Option("", help="Output file path"),
):
    monthly_progress_probability = pd.read_csv(data_path)
    plot_progress_probability(monthly_progress_probability)
    plt.savefig(figure_path)


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
def write_yearly_cumulative_effort_and_captures(
    input_path: str = typer.Option("", help="Input file path"),
    output_path: str = typer.Option("", help="Output file path"),
):
    weekly_effort_and_capture = pd.read_csv(input_path)
    cumulative_effort_and_capture = get_cumulative_effort_and_captures_by_year(
        weekly_effort_and_capture
    )
    years_in_data = years_from_data(weekly_effort_and_capture)
    cumulative_effort_and_capture["CPUE"] = calculate_yearly_cumulative_cpue(
        weekly_effort_and_capture, years_in_data
    )
    cumulative_effort_and_capture = cumulative_effort_and_capture.rename(
        columns={"Captures": "Cumulative_captures"}
    )
    cumulative_effort_and_capture.to_csv(output_path, index=False)


@app.command()
def write_effort_and_captures_with_probability(
    input_path: str = typer.Option("", help="Input file path"),
    output_path: str = typer.Option("", help="Output file path"),
):
    effort_capture_data = pd.read_csv(input_path)
    effort_captures_with_slopes = get_status_probs(effort_capture_data)
    effort_captures_with_slopes.to_csv(output_path, index=False)


@app.command()
def write_effort_and_captures_with_slopes(
    input_path: str = typer.Option("", help="Input file path"),
    output_path: str = typer.Option("", help="Output file path"),
):
    effort_capture_data = pd.read_csv(input_path)
    effort_captures_with_slopes = add_slopes_to_effort_capture_data(effort_capture_data)
    effort_captures_with_slopes.to_csv(output_path, index=False)
