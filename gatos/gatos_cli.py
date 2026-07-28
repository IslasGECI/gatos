from gatos.get_capture_and_effort_by_zone import (
    get_monthly_capture_and_effort_by_zone,
    get_yearly_capture_and_effort_by_zone,
    select_effort_and_captures_by_year,
)
from gatos.histogram_catchs_per_year import generate_histogram
from gatos.compute_semestral_effort_and_captures import (
    xxcompute_CPUE_and_cumulative_effort_and_captures_by_resolution,
)

import matplotlib.pyplot as plt
import pandas as pd
import typer
import warnings

from gatos import __version__

app = typer.Typer()


@app.command()
def write_cpue_and_cumulative_effort_and_captures(
    input_path: str = typer.Option("", help="Input file path"),
    resolution: str = typer.Option("anual", help="Resolution for CPUE calculation"),
    output_path: str = typer.Option("", help="Output file path"),
):
    weekly_effort_and_capture = pd.read_csv(input_path)
    CPUE_and_cumulative_effort_and_captures_df = (
        xxcompute_CPUE_and_cumulative_effort_and_captures_by_resolution(
            weekly_effort_and_capture, resolution
        )
    )
    CPUE_and_cumulative_effort_and_captures_df.reset_index(inplace=True, names=["Date"])
    renamed_df = CPUE_and_cumulative_effort_and_captures_df.rename(
        columns={"Esfuerzo": "Effort", "Capturas": "Cumulative_captures"}
    )

    renamed_df.to_csv(output_path, index=False)


@app.command()
def plot_annual_effort_and_captures(
    input_path: str = typer.Option("", help="Input file path"),
    output_path: str = typer.Option("", help="Output file path"),
    show_mean_line: bool = typer.Option(False, help="Whether to show mean line"),
):
    cat_data = pd.read_csv(input_path)
    generate_histogram(cat_data, show_mean_line)
    plt.savefig(output_path, dpi=300, transparent=True)


@app.command()
def write_monthly_effort_and_captures_by_zone(
    input_path: str = typer.Option("", help="Input file path"),
    output_path: str = typer.Option("", help="Output file path"),
):
    weekly_effort_and_capture = pd.read_csv(input_path)
    monthly_df = get_monthly_capture_and_effort_by_zone(weekly_effort_and_capture)
    monthly_df.to_csv(output_path, index=False)


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
def version():
    typer.echo(__version__)


@app.command(deprecated=True)
def write_yearly_cumulative_effort_and_captures(
    input_path: str = typer.Option("", help="Input file path"),
    output_path: str = typer.Option("", help="Output file path"),
):
    warnings.warn(
        "Use write-cpue-and-cumulative-effort-and-captures with resolution=annual instead",
        DeprecationWarning,
        stacklevel=2,
    )
    weekly_effort_and_capture = pd.read_csv(input_path)
    resolution = "annual"
    yearly_cumulative_effort_and_captures = (
        xxcompute_CPUE_and_cumulative_effort_and_captures_by_resolution(
            weekly_effort_and_capture, resolution
        )
    )

    yearly_cumulative_effort_and_captures.reset_index(inplace=True, names=["Date"])
    renamed_df = yearly_cumulative_effort_and_captures.rename(
        columns={"Esfuerzo": "Effort", "Capturas": "Cumulative_captures"}
    )

    renamed_df.to_csv(output_path, index=False)
