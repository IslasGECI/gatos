import pandas as pd


def compute_CPUE_and_cumulative_effort_and_captures_by_resolution(
    effort_and_captures_df, resolution
):
    effort_and_captures_by_resolution = compute_effort_and_captures_and_cpue_by_resolution(
        effort_and_captures_df, resolution
    )
    cumulative_effort_and_captures_by_resolution = compute_cumulative_effort_and_captures(
        effort_and_captures_by_resolution
    )
    return cumulative_effort_and_captures_by_resolution


def compute_effort_and_captures_and_cpue_by_resolution(effort_and_captures_df, resolution):
    effort_and_captures_df.index = pd.to_datetime(effort_and_captures_df.Fecha)
    effort_and_captures_by_period = compute_effort_and_captures_by_resolution(
        effort_and_captures_df, resolution
    )
    effort_and_captures_by_period["CPUE"] = (
        effort_and_captures_by_period["Capturas"] / effort_and_captures_by_period["Esfuerzo"]
    )
    return effort_and_captures_by_period


def compute_effort_and_captures_by_resolution(effort_and_captures_df, resolution):
    period_index = (effort_and_captures_df.index.month - 1) // resolution
    effort_and_captures_df["period"] = (
        effort_and_captures_df.index.year.astype(str) + "-P" + (period_index + 1).astype(str)
    )
    return effort_and_captures_df.groupby("period").agg({"Esfuerzo": "sum", "Capturas": "sum"})


def compute_cumulative_effort_and_captures(effort_and_catpures_df):
    effort_and_catpures_df[["Esfuerzo", "Capturas"]] = effort_and_catpures_df[
        ["Esfuerzo", "Capturas"]
    ].cumsum(numeric_only=True)
    return effort_and_catpures_df
