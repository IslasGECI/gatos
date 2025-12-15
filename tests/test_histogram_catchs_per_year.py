from gatos.histogram_catchs_per_year import (
    generate_histogram,
    xxgenerate_histogram,
    get_bar_positions,
    TAMANO_FUENTE,
    years_from_data,
)
import numpy as np
import os
import pandas as pd
import matplotlib as mpl


def test_constants():
    years_in_data = ["2022", "2023"]
    obtained = get_bar_positions(years_in_data)
    expected = np.linspace(1, 16, 2)
    assert np.array_equal(expected, obtained)

    expected = 15
    assert expected == TAMANO_FUENTE

    monthly_data = pd.read_csv("tests/data/esfuerzo_capturas_mensuales_gatos_socorro.csv")
    obtained = years_from_data(monthly_data)
    assert (years_in_data == obtained).all()


def test_generate_histogram():
    output_file = "tests/data/histogram.png"
    datos_gatos = pd.read_csv("tests/data/esfuerzo_capturas_mensuales_gatos_socorro.csv")
    obtained = xxgenerate_histogram(datos_gatos, output_file)
    assert os.path.exists(output_file)

    assert isinstance(obtained, mpl.figure.Figure)

    expected_childrens = 3
    assert len(obtained.get_children()) == expected_childrens

    assert isinstance(obtained.get_children()[0], mpl.patches.Rectangle)

    expected_effort_label = "Cumulative effort per year"
    assert obtained.get_children()[1].get_ylabel() == expected_effort_label

    expected_captures_label = "No. cats dispatched"
    assert obtained.get_children()[2].get_ylabel() == expected_captures_label
