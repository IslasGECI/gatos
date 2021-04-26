from gatos.calculator_p_value import CalculatorPValue
from pandas.util.testing import assert_frame_equal
import pandas as pd


total_capturas = 2
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
