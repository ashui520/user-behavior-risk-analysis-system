from __future__ import annotations

import pandas as pd


class ReportGenerator:
    def generate_summary(self, feature_df: pd.DataFrame) -> None:
        print("===== 用户行为特征统计 =====")
        print(
            feature_df[
                [
                    "user_id",
                    "total_actions",
                    "unique_pages",
                    "click_count",
                    "active_seconds",
                    "avg_action_per_second",
                ]
            ].to_string(index=False)
        )
        print()

    def generate_risk_report(self, risk_df: pd.DataFrame) -> None:
        print("===== 风险检测结果 =====")
        print(
            risk_df[
                [
                    "user_id",
                    "risk_score",
                    "risk_level",
                    "risk_reason",
                ]
            ].to_string(index=False)
        )
        print()

        high_risk_users = risk_df[risk_df["risk_level"] == "高风险"]

        print("===== 高风险用户列表 =====")
        if high_risk_users.empty:
            print("无高风险用户")
        else:
            print(
                high_risk_users[
                    ["user_id", "risk_score", "risk_reason"]
                ].to_string(index=False)
            )