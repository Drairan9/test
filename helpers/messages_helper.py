from utils.consts import *


class DiscordHelperMessages:

    def get_rsi_alert_message(self, rsi: float, min_rsi: float, max_rsi: float) -> str | None:
        if rsi > max_rsi:
            return f"{DEFAULT_SYMBOL} High rsi alert! rsi: **{rsi}**"
        elif rsi < min_rsi:
            return f"{DEFAULT_SYMBOL} Low rsi alert! rsi: **{rsi}**"

        return None
