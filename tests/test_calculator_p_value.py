from gatos.calculator_p_value import CalculatorPValue
from pandas.testing import assert_frame_equal
import pandas as pd  # type: ignore
import numpy as np  # type: ignore


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
        self.__set_up_test_calculate_high_probability_and_calculate_high_probability()
        np.testing.assert_array_equal(self.calculador.bins, self.expected_bins)
        np.testing.assert_array_equal(self.calculador.hist, self.expected_hist)

    def test_calculate_high_probability(self):
        self.__set_up_test_calculate_high_probability_and_calculate_high_probability()
        assert self.calculador.maximo == self.maximo
        assert self.calculador.indice_mas_probable[0] == self.indice_mas_probable[0]

    def test_calculate_remanented_cat_more_probably(self):
        self.__set_calculate_remanented_cat_more_probably()
        expected_remanented_cat_more_probably = 8
        assert self.calculador.remanented_cat_more_probably == expected_remanented_cat_more_probably

    def test_posterior_distribution_probabilities_in_intervals(self):
        """
        La probabilidad de que un elemento de la distribución posterior esté en los intervalos:
        - de 0 a 1
        - de 1 a población remamnente
        - de la población remamnente hasta 10,000,000,000 ("infinito")
        """
        self.__set_probability()
        interval_0_1 = 25.0
        interval_1_remaining = 25.0
        interval_remanent_to_infinity = 50.0
        expected_probabilities = [interval_0_1, interval_1_remaining, interval_remanent_to_infinity]
        obtained_probabilities = self.calculador.probabilidades.tolist()
        assert expected_probabilities == obtained_probabilities

    def __set_up_test_calculate_high_probability_and_calculate_high_probability(self):
        self.calculador.calculate_range_remanented_cats()
        self.calculador.calculate_high_probability()
        self.expected_n_bins = 8
        self.expected_hist, _ = np.histogram(
            self.calculador.remanented_cats, bins=self.expected_n_bins
        )
        self.expected_bins = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8])
        self.maximo = max(self.expected_hist)
        self.indice_mas_probable = np.where(self.expected_hist == self.maximo)[0]

    def __set_calculate_remanented_cat_more_probably(self):
        self.__set_up_test_calculate_high_probability_and_calculate_high_probability()
        self.calculador.calculate_remanented_cat_more_probably()

    def __set_probability(self):
        self.__set_calculate_remanented_cat_more_probably()
        self.calculador.probability()
