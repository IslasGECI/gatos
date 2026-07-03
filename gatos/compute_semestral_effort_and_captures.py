import numpy as np
import pandas as pd


def compute_semestral_effort_and_captures(effort_and_captures_df):
    effort_and_captures_df.index = pd.to_datetime(effort_and_captures_df.Fecha)
    resolution = 6
    period_index = (effort_and_captures_df.index.month - 1) // resolution
    effort_and_captures_df["period"] = (
        effort_and_captures_df.index.year.astype(str) + "-P" + (period_index + 1).astype(str)
    )
    return effort_and_captures_df.groupby("period").agg({"Esfuerzo": "sum", "Capturas": "sum"})
