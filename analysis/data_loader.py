from __future__ import annotations

import pandas as pd


class DataLoader:
    def __init__(self, file_path: str) -> None:
        self.file_path = file_path

    def load_logs(self) -> pd.DataFrame:
        df = pd.read_csv(self.file_path)
        df["timestamp"] = pd.to_datetime(df["timestamp"])
        return df

    def clean_logs(self, df: pd.DataFrame) -> pd.DataFrame:
        cleaned_df = df.dropna().drop_duplicates().reset_index(drop=True)
        return cleaned_df