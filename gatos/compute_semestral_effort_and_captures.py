import pandas as pd


def compute_CPUE_and_cumulative_effort_and_captures_by_resolution(
    weekly_effort_and_capture, resolution
):
    resolutions_dict = {"annual": 12, "semestral": 6, "monthly": 1}
    effort_and_captures_by_resolution = compute_effort_and_captures_and_cpue_by_resolution(
        weekly_effort_and_capture, resolutions_dict[resolution]
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
    effort_and_catpures_df = sort_by_period(effort_and_catpures_df)
    effort_and_catpures_df[["Esfuerzo", "Capturas"]] = effort_and_catpures_df[
        ["Esfuerzo", "Capturas"]
    ].cumsum(numeric_only=True)
    return effort_and_catpures_df.set_index("period")


def sort_by_period(effort_and_catpures_df):
    effort_and_catpures_df["period"] = effort_and_catpures_df.index.to_series()
    effort_and_catpures_df["_year"] = effort_and_catpures_df.period.str.extract(r"(\d+)-P").astype(
        int
    )
    effort_and_catpures_df["_pnum"] = effort_and_catpures_df.period.str.extract(r"P(\d+)").astype(
        int
    )
    effort_and_catpures_df = (
        effort_and_catpures_df.sort_values(["_year", "_pnum"])
        .drop(columns=["_year", "_pnum"])
        .reset_index(drop=True)
    )
    return effort_and_catpures_df
