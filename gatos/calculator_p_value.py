import pandas as pd  # type: ignore
import numpy as np  # type: ignore


class CalculatorPValue:
    def __init__(self):
        pass

    def read_posterior(self, archivo):
        self.datos = pd.read_csv(archivo)
        self.remanented_cats = self.datos.No - self.capturas

    def set_total_capturas(self, capturas):
        self.capturas = capturas

    def calculate_range_remanented_cats(self):
        n_bins = int(np.ceil(max(self.datos.No.unique()) - min(self.datos.No.unique())))
        self.hist, self.bins = np.histogram(self.remanented_cats, bins=n_bins)

    def calculate_high_probability(self):
        self.maximo = max(self.hist)
        self.indice_mas_probable = np.where(self.hist == self.maximo)[0]

    def calculate_remanented_cat_more_probably(self):
        self.remanented_cat_more_probably = self.bins[self.indice_mas_probable][0] + 1

    def probability(self):
        maximum_remanented_cats = self.bins[-1] + 1
        hist, _ = np.histogram(
            self.remanented_cats,
            bins=[0, 1, self.remanented_cat_more_probably, maximum_remanented_cats],
        )
        self.probabilidades = (hist / hist.sum()) * 100
