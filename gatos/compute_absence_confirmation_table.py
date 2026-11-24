import numpy as np
import pandas as pd

from gatos.calculator_p_value import CalculatorPValue
from gatos.PopulationEstimator import PopulationEstimator


def compute_absence_confirmation_table(effort_captures_df, model_iterations, months_to_iterate):
    effort_captures_df_copy = effort_captures_df.copy()
    median_effort = effort_captures_df_copy.Esfuerzo.median()
    output_df = pd.DataFrame(columns=["Fecha", "absence_probability", "remanents"])
    for i in range(months_to_iterate):
        estimador_poblacion_inicial: PopulationEstimator = PopulationEstimator(
            effort_captures_df_copy.Esfuerzo, effort_captures_df_copy.Capturas, "posterior.csv"
        )
        estimador_poblacion_inicial.run(
            iteraciones=model_iterations,
            n_datos_descartados=int(np.ceil(model_iterations * 0.1)),
        )
        estimador_poblacion_inicial.run_model_diagnostics()

        total_capturas = effort_captures_df_copy.Capturas.sum()

        calculador = CalculatorPValue()
        calculador.set_total_capturas(total_capturas)
        calculador.read_posterior("posterior.csv")
        calculador.calculate_range_remanented_cats()
        calculador.calculate_high_probability()
        calculador.calculate_remanented_cat_more_probably()
        calculador.probability()

        output_df.loc[len(output_df)] = {
            "Fecha": effort_captures_df_copy.Fecha.iloc[-1],
            "absence_probability": calculador.probabilidades.tolist()[0],
            "remanents": int(calculador.remanented_cat_more_probably),
        }

        effort_captures_df_copy["Fecha"] = pd.to_datetime(effort_captures_df_copy["Fecha"])
        next_month = effort_captures_df_copy["Fecha"].max() + pd.DateOffset(months=1)
        new_row = {"Fecha": next_month, "Esfuerzo": median_effort, "Capturas": 0}
        effort_captures_df_copy.loc[len(effort_captures_df_copy)] = new_row
    return output_df
