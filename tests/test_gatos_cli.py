from gatos import (
    write_effort_and_captures_by_zone_for_year,
    write_yearly_cumulative_effort_and_captures,
)
from gatos.gatos_cli import app

import pandas as pd
import os
import hashlib
from typer.testing import CliRunner

runner = CliRunner()


def test_cli():
    result = runner.invoke(
        app,
        ["--help"],
    )
    assert "plot-annual-effort-and-captures" in result.stdout


input_path = "tests/data/esfuerzo_capturas_semanales_iso8601.csv"


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
    write_yearly_cumulative_effort_and_captures(input_path, output_path)
    assert os.path.exists(output_path)
    obtained_csv = pd.read_csv(output_path)
    obtained_columns = obtained_csv.columns
    expected_columns = ["Date", "Effort", "Cumulative_captures", "CPUE"]
    assert (obtained_columns == expected_columns).all()
    expected_hash = "f91474bc36b1cf3c78174a9ad2f202ba"
    obtained_hash = hashlib.md5(open(output_path, "rb").read()).hexdigest()
    assert obtained_hash == expected_hash, "Hash of csv with cumulative effort an captures"
