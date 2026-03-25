from __future__ import annotations

import pandas as pd


class RiskDetector:
    def __init__(self) -> None:
        self.rules = {
            "high_frequency_actions": 8,
            "high_action_speed": 0.8,
            "single_page_repeated_click": 1,
        }

    def score_risk(self, feature_df: pd.DataFrame) -> pd.DataFrame:
        result_df = feature_df.copy()
        result_df["risk_score"] = 0
        result_df["risk_reason"] = ""

        for idx, row in result_df.iterrows():
            score = 0
            reasons: list[str] = []

            if row["total_actions"] >= self.rules["high_frequency_actions"]:
                score += 40
                reasons.append("高频操作")

            if row["avg_action_per_second"] >= self.rules["high_action_speed"]:
                score += 35
                reasons.append("单位时间操作过快")

            if (
                row["unique_pages"] <= self.rules["single_page_repeated_click"]
                and row["click_count"] >= 5
            ):
                score += 25
                reasons.append("页面行为单一且重复点击明显")

            result_df.at[idx, "risk_score"] = score
            result_df.at[idx, "risk_reason"] = "、".join(reasons) if reasons else "正常"

        result_df["risk_level"] = result_df["risk_score"].apply(self._risk_level)
        return result_df

    @staticmethod
    def _risk_level(score: int) -> str:
        if score >= 70:
            return "高风险"
        if score >= 40:
            return "中风险"
        return "低风险"