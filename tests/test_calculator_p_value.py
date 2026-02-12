from gatos.calculator_p_value import CalculatorPValue
from pandas.testing import assert_frame_equal
import pandas as pd  # type: ignore
import numpy as np  # type: ignore
import pytest

total_capturas = 1
archivo = "tests/data/example.csv"


class Test_CalculatorPValue:
    def setup_method(self):
        self.calculador = CalculatorPValue()
        self.calculador.set_total_capturas(total_capturas)
        self.calculador.read_posterior(archivo)

    def test_read_posterior(self):
        expected_datos = pd.read_csv(archivo)
        assert_frame_equal(expected_datos, self.calculador.datos)
        expected_remanented_cats = expected_datos.No + total_capturas
        assert expected_remanented_cats[0] != self.calculador.remanented_cats[0]

    def test_set_total_capturas(self):
        assert self.calculador.capturas == total_capturas

    def test_calculate_range_remanented_cats(self):
        calculador = CalculatorPValue()
        calculador.set_total_capturas(total_capturas)
        calculador.read_posterior(archivo)
        calculador.calculate_range_remanented_cats()
        expected_hist = np.array([1, 0, 0, 0, 1, 0, 0, 2])
        expected_bins = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8])
        np.testing.assert_array_equal(calculador.bins, expected_bins)
        np.testing.assert_array_equal(calculador.hist, expected_hist)

    def test_calculate_high_probability(self):
        calculador = CalculatorPValue()
        calculador.set_total_capturas(total_capturas)
        calculador.read_posterior(archivo)
        calculador.calculate_range_remanented_cats()
        calculador.calculate_high_probability()
        expected_indice_mas_probable = [7]
        expected_maximo = 2
        assert calculador.maximo == expected_maximo
        assert calculador.indice_mas_probable[0] == expected_indice_mas_probable[0]

    def test_calculate_remanented_cat_more_probably(self):
        self.__set_calculate_remanented_cat_more_probably()
        expected_remanented_cat_more_probably = 8
        assert self.calculador.remanented_cat_more_probably == expected_remanented_cat_more_probably

    def test_posterior_distribution_probabilities_in_intervals(self):
        calculador = CalculatorPValue()
        calculador.remanented_cat_more_probably = 10_100
        calculador.bins = np.array([i for i in range(10_101)])
        calculador.remanented_cats = [
            0,
            4,
            10_101,
            10_101,
        ]
        calculador.probability()
        obtained_probabilities = calculador.probabilidades.tolist()
        interval_0_1 = 25.0
        interval_1_remaining_minus_one = 25.0
        interval_remanent_to_infinity = 50.0
        expected_probabilities = [
            interval_0_1,
            interval_1_remaining_minus_one,
            interval_remanent_to_infinity,
        ]
        assert expected_probabilities == obtained_probabilities

        calculador.remanented_cat_more_probably = 1
        posterior_distribution = np.array([1, 5, 9])
        calculador.remanented_cats = posterior_distribution - total_capturas
        calculador.probability()
        obtained_probabilities = calculador.probabilidades.tolist()
        interval_0_1 = 33.33
        interval_1_remaining_minus_one = 0
        interval_remanent_to_infinity = 66.66
        expected_probabilities = [
            interval_0_1,
            interval_1_remaining_minus_one,
            interval_remanent_to_infinity,
        ]
        assert obtained_probabilities == pytest.approx(expected_probabilities, 0.1)

    def __set_up_test_calculate_high_probability_and_calculate_high_probability(self):
        self.calculador.calculate_range_remanented_cats()
        self.calculador.calculate_high_probability()
        self.expected_hist = np.array([1, 0, 0, 0, 1, 0, 0, 2])

    def __set_calculate_remanented_cat_more_probably(self):
        self.__set_up_test_calculate_high_probability_and_calculate_high_probability()
        self.calculador.calculate_remanented_cat_more_probably()
