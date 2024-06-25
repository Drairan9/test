from pybit.unified_trading import WebSocket
from loguru import logger


class MarketServiceWS:
    def __init__(self):
        self.websocket: WebSocket | None = None

    def connect_to_websocket(self, category: str):
        self.websocket = WebSocket(
            testnet=False,
            channel_type=category,
        )

    def kill_websocket(self):
        self.websocket.exit()

    def is_connected(self) -> bool:
        return self.websocket.is_connected()

    def subscribe_to_kline_stream(self, interval: int, symbol: str, callback) -> bool:
        if self.websocket is None:
            logger.warning("Websocket subscription was attempted without an active connection.")
            return False

        self.websocket.kline_stream(
            interval=interval,
            symbol=symbol,
            callback=callback
        )
