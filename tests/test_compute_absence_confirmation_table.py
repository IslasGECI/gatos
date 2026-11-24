import pandas as pd

from gatos.compute_absence_confirmation_table import compute_absence_confirmation_table


def test_compute_absence_confirmation_table():
    effort_captures = pd.read_csv("tests/data/esfuerzo_capturas_mensuales_gatos_socorro.csv")
    model_iterations = 100
    months_to_iterate = 10
    obtained = compute_absence_confirmation_table(
        effort_captures, model_iterations, months_to_iterate
    )

    assert isinstance(obtained, pd.DataFrame)
    columns = ["Fecha", "absence_probability", "remanents"]
    assert list(obtained.columns) == columns
    assert obtained.shape == (months_to_iterate, len(columns))
