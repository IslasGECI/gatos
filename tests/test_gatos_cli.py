from gatos import (
    write_effort_and_captures_by_zone_for_year,
    write_yearly_cumulative_effort_and_captures,
)
from gatos.gatos_cli import app

import pandas as pd
import pytest
import os
from typer.testing import CliRunner

runner = CliRunner()


def test_cli():
    result = runner.invoke(
        app,
        ["--help"],
    )
    assert "plot-annual-effort-and-captures" in result.stdout


input_path = "tests/data/esfuerzo_capturas_semanales_iso8601.csv"


def test_write_CPUE_and_cumulative_effort_and_captures():
    output_path = "tests/data/CPUE_and_cumulative_effort_and_captures.csv"
    if os.path.exists(output_path):
        os.remove(output_path)
    resolution = "semestral"
    result = runner.invoke(
        app,
        [
            "write-cpue-and-cumulative-effort-and-captures",
            "--input-path",
            input_path,
            "--resolution",
            resolution,
            "--output-path",
            output_path,
        ],
    )
    assert result.exit_code == 0
    assert os.path.exists(output_path)
    resolution = "annual"
    result = runner.invoke(
        app,
        [
            "write-cpue-and-cumulative-effort-and-captures",
            "--input-path",
            input_path,
            "--resolution",
            resolution,
            "--output-path",
            output_path,
        ],
    )
    assert result.exit_code == 0
    assert os.path.exists(output_path)


def test_write_monthly_effort_and_captures_by_zone():
    output_path = "tests/data/monthly_effort_and_captures_by_zone.csv"
    if os.path.exists(output_path):
        os.remove(output_path)
    result = runner.invoke(
        app,
        [
            "write-monthly-effort-and-captures-by-zone",
            "--input-path",
            input_path,
            "--output-path",
            output_path,
        ],
    )
    assert result.exit_code == 0
    assert os.path.exists(output_path)


def test_plot_annual_effort_and_captures():
    output_path = "tests/data/annual_effort_and_captures.png"
    if os.path.exists(output_path):
        os.remove(output_path)
    result = runner.invoke(
        app,
        [
            "plot-annual-effort-and-captures",
            "--input-path",
            input_path,
            "--output-path",
            output_path,
            "--show-mean-line",
        ],
    )
    assert result.exit_code == 0
    assert os.path.exists(output_path)


def test_write_effort_and_captures_by_zone():
    output_path = "tests/data/effort_and_captures_by_zone.csv"
    if os.path.exists(output_path):
        os.remove(output_path)
    year = "2022"
    write_effort_and_captures_by_zone_for_year(input_path, output_path, year)
    assert os.path.exists(output_path)


def test_write_yearly_cumulative_effort_and_captures():
    output_path = "tests/data/yearly_cumulative_effort_and_captures.csv"
    if os.path.exists(output_path):
        os.remove(output_path)
    with pytest.warns(DeprecationWarning):
        write_yearly_cumulative_effort_and_captures(input_path, output_path)
    assert os.path.exists(output_path)
    obtained_csv = pd.read_csv(output_path)
    obtained_columns = obtained_csv.columns
    expected_columns = ["Date", "Effort", "Cumulative_captures", "CPUE"]
    assert (obtained_columns == expected_columns).all()
