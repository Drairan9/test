from discord import Client
from pandas import DataFrame
from services.market_service_ws import MarketServiceWS
from services.market_service_rest import MarketServiceREST
from utils.consts import *
from utils.discord_api_rest import DiscordApiRest
from helpers.messages_helper import DiscordHelperMessages
from utils.secret_manager import SecretManager
from loguru import logger


class RsiWorker:
    def __init__(self, client):
        self.Client: Client = client
        self.MarketServiceWS = MarketServiceWS()
        self.MarketServiceREST = MarketServiceREST()
        self.DiscordApiRest = DiscordApiRest()

        self._is_running: bool = False

    async def start_worker(self):
        self.MarketServiceWS.connect_to_websocket(DEFAULT_CATEGORY)
        self.MarketServiceWS.subscribe_to_kline_stream(DEFAULT_INTERVAL,
                                                       DEFAULT_SYMBOL,
                                                       self._handle_kline_stream)
        self._is_running = True
        logger.info("RSI worker is running")

    def stop_worker(self):
        if not self.MarketServiceWS.is_connected():
            return

        self.MarketServiceWS.kill_websocket()
        self._is_running = False
        logger.info("RSI worker is stopped")

    def is_running(self):
        return self._is_running

    def _handle_kline_stream(self, data: dict):
        if not data["data"][0]["confirm"]:
            return

        latest_rsi: DataFrame = self.MarketServiceREST.get_rsi_list_with_timestamp(DEFAULT_CATEGORY,
                                                                                   DEFAULT_SYMBOL,
                                                                                   DEFAULT_INTERVAL)
        last_closed_rsi: int = latest_rsi["rsi"][1]
        message_content: str | None = DiscordHelperMessages.get_rsi_alert_message(last_closed_rsi, DEFAULT_RSI_MIN,
                                                                                  DEFAULT_RSI_MAX)
        if message_content is None:
            return

        DiscordApiRest().send_message_to_channel(SecretManager.get_channel_id(), message_content)
