from gatos.calculator_p_value import CalculatorPValue


def test_set_total_capturas():
    total_capturas = 10
    calculador = CalculatorPValue()
    calculador.set_total_capturas(total_capturas)
    assert calculador.capturas == total_capturas
