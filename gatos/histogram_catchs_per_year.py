import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from geci_plots import geci_plot, roundup, order_magnitude
from gatos.get_capture_and_effort_by_zone import (
    calculate_yearly_cumulative_effort_and_captures,
    years_from_data,
)


TAMANO_FUENTE = 15


def generate_histogram(datos_gatos):
    years_in_data = years_from_data(datos_gatos)
    bar_positions = get_bar_positions(years_in_data)

    esfuerzo_acumulado_anual, gatos_erradicados = calculate_yearly_cumulative_effort_and_captures(
        datos_gatos, years_in_data
    )

    mean_effort = np.mean(esfuerzo_acumulado_anual)
    max_effort = np.max(esfuerzo_acumulado_anual)
    fig, ax = geci_plot()
    plt.bar(bar_positions, esfuerzo_acumulado_anual, alpha=1, width=1)
    plt.xticks(bar_positions, years_in_data)
    plt.plot([-10, 100], [mean_effort, mean_effort], "-r", label="Mean effort")
    ax.set_ylabel("Cumulative effort per year", fontsize=TAMANO_FUENTE)
    ax.set_ylim(0, roundup(max_effort * 1.2, 10 ** order_magnitude(max_effort)))
    ax.set_xlim(bar_positions.min() - 1, bar_positions.max() + 1)
    ax.spines["top"].set_visible(False)
    for i in range(len(esfuerzo_acumulado_anual)):
        plt.text(
            x=bar_positions[i] - 0.6,
            y=esfuerzo_acumulado_anual[i] + 500,
            s=format(esfuerzo_acumulado_anual[i], ","),
            size=12,
        )
    ax.tick_params(labelsize=TAMANO_FUENTE)
    ax.get_yaxis().set_major_formatter(
        matplotlib.ticker.FuncFormatter(lambda x, p: format(int(x), ","))
    )
    ax2 = ax.twinx()
    ax2.set_ylabel("No. cats dispatched", fontsize=TAMANO_FUENTE)
    ax2.plot(bar_positions, gatos_erradicados, c="black", marker="D")
    ax2.set_ylim(0, 140)
    for i in range(len(gatos_erradicados)):
        plt.text(
            x=bar_positions[i] - 0.25,
            y=gatos_erradicados[i] + 5,
            s=gatos_erradicados[i],
            size=12,
        )
    ax2.tick_params(labelsize=TAMANO_FUENTE)
    ax2.spines["top"].set_visible(False)
    return fig


def get_bar_positions(array_of_years):
    return np.linspace(1, 16, len(array_of_years))
