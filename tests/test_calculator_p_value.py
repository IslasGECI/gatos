from gatos.calculator_p_value import CalculatorPValue
from pandas.util.testing import assert_frame_equal
import pandas as pd
import numpy as np  # type: ignore


total_capturas = 15
archivo = "tests/data/example.csv"


def test_read_posterior():
    calculador = CalculatorPValue()
    calculador.set_total_capturas(total_capturas)
    calculador.read_posterior(archivo)
    expected_datos = pd.read_csv(archivo)
    assert_frame_equal(expected_datos, calculador.datos)
    expected_remanented_cats = expected_datos.No + total_capturas
    assert expected_remanented_cats[0] != calculador.remanented_cats[0]


def test_set_total_capturas():
    calculador = CalculatorPValue()
    calculador.set_total_capturas(total_capturas)
    assert calculador.capturas == total_capturas


def test_calculate_range_remanented_cats():
    calculador = CalculatorPValue()
    calculador.set_total_capturas(total_capturas)
    calculador.read_posterior(archivo)
    calculador.calculate_range_remanented_cats()

    expected_n_bins = max(calculador.datos.No.unique()) - min(calculador.datos.No.unique())
    expected_hist, expected_bins = np.histogram(calculador.remanented_cats, bins=expected_n_bins)

    np.testing.assert_array_equal(calculador.bins, expected_bins)
    np.testing.assert_array_equal(calculador.hist, expected_hist)


def test_calculate_high_probability():
    calculador = CalculatorPValue()
    calculador.set_total_capturas(total_capturas)
    calculador.read_posterior(archivo)
    calculador.calculate_range_remanented_cats()
    calculador.calculate_high_probability()

    expected_n_bins = max(calculador.datos.No.unique()) - min(calculador.datos.No.unique())
    expected_hist, expected_bins = np.histogram(calculador.remanented_cats, bins=expected_n_bins)

    maximo = max(expected_hist)
    indice_mas_probable = np.where(expected_hist == maximo)[0]

    assert calculador.maximo == maximo
    assert calculador.indice_mas_probable[0] == indice_mas_probable[0]


def test_calculate_remanented_cat_more_probably():
    calculador = CalculatorPValue()
    calculador.set_total_capturas(total_capturas)
    calculador.read_posterior(archivo)
    calculador.calculate_range_remanented_cats()
    calculador.calculate_high_probability()
    calculador.calculate_remanented_cat_more_probably()

    expected_n_bins = max(calculador.datos.No.unique()) - min(calculador.datos.No.unique())
    expected_hist, expected_bins = np.histogram(calculador.remanented_cats, bins=expected_n_bins)

    maximo = max(expected_hist)
    indice_mas_probable = np.where(expected_hist == maximo)[0]

    remanented_cat_more_probably = expected_bins[indice_mas_probable][0]

    assert calculador.remanented_cat_more_probably == remanented_cat_more_probably
