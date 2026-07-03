import numpy as np
import pandas as pd


def compute_semestral_effort_and_captures(effort_and_captures_df):
    effort_and_captures_df.index = pd.to_datetime(effort_and_captures_df.Fecha)
    effort_and_captures_df["semestral"] = (
        effort_and_captures_df.index.year.astype(str)
        + "-S"
        + np.where(effort_and_captures_df.index.month <= 6, "1", "2")
    )
    return effort_and_captures_df.groupby("semestral").agg({"Esfuerzo": "sum", "Capturas": "sum"})
