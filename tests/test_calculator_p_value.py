from gatos.calculator_p_value import CalculatorPValue

total_capturas = 15
archivo = "tests/data/example.csv"


def test_read_posterior():
    pass


def test_set_total_capturas():
    calculador = CalculatorPValue()
    calculador.set_total_capturas(total_capturas)
    assert calculador.capturas == total_capturas
