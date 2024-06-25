import pandas as pd
from ta.momentum import RSIIndicator


class MarketUtils:
    @staticmethod
    def kline_data_to_dataframe(kline_data: list) -> pd.DataFrame:
        kline_headers = ["timestamp", "openPrice", "highPrice", "lowPrice", "closePrice", "volume", "turnover"]
        df = pd.DataFrame(kline_data, columns=kline_headers)
        df["closePrice"] = df["closePrice"].astype(float)
        df["timestamp"] = df["timestamp"].astype(int)
        return df

    @staticmethod
    def calculate_rsi(close: pd.Series) -> pd.Series:
        return round(RSIIndicator(close, 14, True).rsi(), 2)
