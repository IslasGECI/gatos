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
        remanented_cat_more_probably = self.expected_bins[self.indice_mas_probable][0]
        assert self.calculador.remanented_cat_more_probably == remanented_cat_more_probably

    def test_probability(self):
        self.__set_probability()
        expected_probabilities = [33.33333333333333, 0.0, 66.66666666666666]
        obtained_probabilities = self.calculador.probabilidades.tolist()
        assert expected_probabilities == obtained_probabilities

    def __set_up_test_calculate_high_probability_and_calculate_high_probability(self):
        self.calculador.calculate_range_remanented_cats()
        self.calculador.calculate_high_probability()
        self.expected_n_bins = max(self.calculador.datos.No.unique()) - min(
            self.calculador.datos.No.unique()
        )
        self.expected_hist, self.expected_bins = np.histogram(
            self.calculador.remanented_cats, bins=self.expected_n_bins
        )
        self.maximo = max(self.expected_hist)
        self.indice_mas_probable = np.where(self.expected_hist == self.maximo)[0]

    def __set_calculate_remanented_cat_more_probably(self):
        self.__set_up_test_calculate_high_probability_and_calculate_high_probability()
        self.calculador.calculate_remanented_cat_more_probably()

    def __set_probability(self):
        self.__set_calculate_remanented_cat_more_probably()
        self.calculador.probability()
