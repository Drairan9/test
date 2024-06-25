from pandas import DataFrame
from pybit.unified_trading import HTTP
from loguru import logger

from utils.market_utils import MarketUtils


class MarketServiceREST:
    def __init__(self):
        self.http_session: HTTP = HTTP(
            testnet=False,
        )

    def get_historical_klines(self, category: str, symbol: str, interval: int) -> list | bool:
        try:
            klines_data = self.http_session.get_kline(
                category=category,
                symbol=symbol,
                interval=interval,
            )
        except Exception as e:
            logger.error(f"Get Kline request failed - {str(e)}")
            return False

        if klines_data["retCode"] != 0:
            logger.error(
                f"Get Kline request returned status {klines_data["retCode"]} with message {klines_data["retMsg"]}")
            return False

        if len(klines_data["result"]["list"]) <= 0:
            logger.warning("Bybit kline endpoint returned empty list!")
            return False

        return klines_data["result"]["list"]

    def get_rsi_list_with_timestamp(self, category: str, symbol: str, interval: int) -> DataFrame | bool:
        kline_data = MarketServiceREST().get_historical_klines(
            category=category,
            symbol=symbol,
            interval=interval
        )
        if not kline_data:
            logger.warning("get_latest_rsi_list returned empty list!")
            return False

        df = MarketUtils.kline_data_to_dataframe(kline_data)

        df = df.iloc[::-1]  # Reverse the dataframe to calculate rsi from newest
        df["rsi"] = MarketUtils.calculate_rsi(df["closePrice"])

        return df[["timestamp", "rsi"]]
