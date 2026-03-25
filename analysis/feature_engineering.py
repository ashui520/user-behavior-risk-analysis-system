from __future__ import annotations

import pandas as pd


class FeatureEngineer:
    def build_user_features(self, df: pd.DataFrame) -> pd.DataFrame:
        working_df = df.copy()
        working_df["hour"] = working_df["timestamp"].dt.hour

        total_actions = working_df.groupby("user_id").size().rename("total_actions")
        unique_pages = (
            working_df.groupby("user_id")["page"].nunique().rename("unique_pages")
        )
        unique_ips = working_df.groupby("user_id")["ip"].nunique().rename("unique_ips")

        login_count = (
            working_df[working_df["action"] == "login"]
            .groupby("user_id")
            .size()
            .rename("login_count")
        )

        click_count = (
            working_df[working_df["action"] == "click"]
            .groupby("user_id")
            .size()
            .rename("click_count")
        )

        first_time = (
            working_df.groupby("user_id")["timestamp"].min().rename("first_time")
        )
        last_time = working_df.groupby("user_id")["timestamp"].max().rename("last_time")

        feature_df = pd.concat(
            [
                total_actions,
                unique_pages,
                unique_ips,
                login_count,
                click_count,
                first_time,
                last_time,
            ],
            axis=1,
        ).fillna(0)

        feature_df["active_seconds"] = (
            feature_df["last_time"] - feature_df["first_time"]
        ).dt.total_seconds()

        feature_df["active_seconds"] = feature_df["active_seconds"].fillna(0)

        feature_df["avg_action_per_second"] = feature_df.apply(
            lambda row: row["total_actions"] / (row["active_seconds"] + 1),
            axis=1,
        )

        return feature_df.reset_index()