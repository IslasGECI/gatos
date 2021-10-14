import numpy as np
import pandas as pd
import pymc3 as pm3
import arviz as az
from geci_plots import geci_plot, roundup
import matplotlib.pyplot as plt

RANDOM_SEED = 22

class PopulationEstimator:
    """Clase encargada de encontrar el tamaño inicial de la población utilizando
    el método de Ramsey

    Para inicializar el estimador se le debe pasar la información necesaria para
    encontrar el tamaño de la población.

    # Parámetros
    `esfuerzo np.array`

    Esfuerzo de la erradicación

    `capturas np.array`

    Número de iteraciones utilizadas en la simulación de series de Markov Monte Carlo

    ## Nota:
    Para borrar los archivos temporales se debe llamar al método
    `remove_temporal_data()`
    """

    def __init__(self, esfuerzo: np.array, capturas: np.array, nombre_archivo):
        self.esfuerzo = esfuerzo
        self.capturas = capturas
        self.capturas_acumuladas = np.cumsum(capturas)
        self._nombre_archivo = nombre_archivo
        self.json_output_path = "reports/non-tabular/"
        self.plot_output_path = "reports/figures/" 
        self.tamanios_poblacion = None
        self.trace = None
        self.cats_model = None

    def init_model(self):
        return self._Ramsey_model_pymc3(
            self.esfuerzo, self.capturas, self.capturas_acumuladas
        )

    def run(self, iteraciones: int = 6000000, n_datos_descartados: int = 30000):
        """Método encargado de correr el modelo de Ramsey una cierta cantidad de
        repeticiones para determinar el tamaño de la población.

        En cada iteración guarda las distribuciones posteriores y a partir de estas
        se calcula el tamaño de la población.

        # Parámetros

        `iter int`

        Número de iteraciones utilizadas en la simulación de series de Markov Monte Carlo

        `burn int`

        Número de iteraciones que se van a deshechar

        ## Nota:
        Para borrar los archivos temporales se debe llamar al método
        `remove_temporal_data()`
        """
        self.cats_model = self.init_model()

        with self.cats_model:
            self.trace = pm3.sample(
                iteraciones, tune=n_datos_descartados, progressbar=True, return_inferencedata=False
            )
        results_trace = pd.DataFrame(
            {"a": self.trace["alpha"], "b": self.trace["beta"], "No": self.trace["initial_population"]}
        )
        results_trace.to_csv(self._nombre_archivo, index=False)

    def plot_Vmp_histogram(self):
        self.tamanios_poblacion.Vmp.hist()

    def _Ramsey_model_pymc3(self, v_effort, v_captures, v_cumulative_captures):
        with pm3.Model() as model_ramsey:
            effort = pm3.Data("effort", v_effort)
            captures = pm3.Data("captures", v_captures)
            cumulative_captures = pm3.Data("cumulative_captures", v_cumulative_captures)
            alpha = pm3.Normal("alpha", mu=0.00, tau=1 / 5)
            beta = pm3.Normal("beta", mu=0.00, tau=1 / 5)
            linear_logistic_link = pm3.math.invlogit(alpha + beta * effort)
            catch_probability = pm3.Deterministic("catch_probability", linear_logistic_link)
            initial_population = pm3.DiscreteUniform("initial_population", lower=500, upper=22000)
            initial_population_updated = pm3.Deterministic(
                "initial_population_updated", initial_population - cumulative_captures
            )
            captures_obs = pm3.Binomial(  # noqa
                "captures_obs", n=initial_population_updated, p=catch_probability, observed=captures
            )
        return model_ramsey

    def run_model_diagnostics(self):
        self.sample_predictive_posterior()
        self.run_loo_diagnostic()
        self.run_waic_diagnostic()
        self.plot_data_and_predictive_points()

    def run_loo_diagnostic(self, plot_name="loo_diagnostic.png"):
        df_loo = az.loo(self.trace, pointwise=True)
        print(df_loo)
        df_loo[['loo', 'loo_se', 'p_loo']].to_json(self.json_output_path + "loo_results.json")
        fig , ax = geci_plot()
        az.plot_khat(df_loo, ax=ax)
        ax.set_ylim(0,2)
        plt.savefig(self.plot_output_path + plot_name, transparent=True, dpi=300)

    def run_waic_diagnostic(self):
        df_waic = az.waic(self.trace)
        print(df_waic)
        df_waic[['waic', 'waic_se', 'p_waic']].to_json(self.json_output_path + "waic_results.json")

    def sample_predictive_posterior(self):
        self.ppc = pm3.sample_posterior_predictive(self.trace, model=self.cats_model, samples=100, random_seed=RANDOM_SEED)

    def plot_data_and_predictive_points(self, plot_name="predictive_posterior.png"):
        fig , ax = geci_plot()
        ax.plot(self.ppc['captures_obs'].T, 'o', color='k', alpha=.025)
        ax.plot(self.capturas, 'o', color='red')
        ax.set_ylabel("Captures", size=20)
        ax.set_xlabel("Months", size=20)
        ax.tick_params(labelsize=20)
        ax.set_ylim(-1,80)
        ax.set_xlim(-1, roundup(len(self.capturas),10))
        plt.savefig(self.plot_output_path + plot_name, transparent=True, dpi=300)

def calc_min_interval(x, alpha):
    """Internal method to determine the minimum interval of
    a given width
    Assumes that x is sorted numpy array.
    """
    n = len(x)
    cred_mass = 1.0 - alpha

    interval_idx_inc = int(np.floor(cred_mass * n))
    n_intervals = n - interval_idx_inc
    interval_width = x[interval_idx_inc:] - x[:n_intervals]

    if len(interval_width) == 0:
        raise ValueError("Too few elements for interval calculation")

    min_interval_width = interval_width.min()
    limite_inferior = np.array(range(x.min(), x.max() - min_interval_width + 2))
    limite_superior = limite_inferior + min_interval_width
    n_dentro = [
        ((inferior <= x) & (x <= superior)).sum()
        for inferior, superior in zip(limite_inferior, limite_superior)
    ]

    max_idx = np.argmax(n_dentro)
    hdi_min = limite_inferior[max_idx]
    hdi_max = limite_superior[max_idx]
    return hdi_min, hdi_max
