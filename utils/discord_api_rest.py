import json
import requests
from utils.secret_manager import SecretManager
from utils.consts import *
from loguru import logger


class DiscordApiRest:
    def send_message_to_channel(self, channel_id: int, content: str):
        try:
            url = f"{DISCORD_API_URL}/channels/{channel_id}/messages"
            headers = {"Authorization": f"Bot {SecretManager.get_bot_token()}",
                       "Content-Type": "application/json", }

            prepared_json = json.dumps({"content": content})
            x = requests.post(url, headers=headers, data=prepared_json)

            if x.status_code != 200:
                logger.error(f"Failed to send message -> code: {x.status_code} text: {x.text}")
                return False

            return True
        except Exception as e:
            logger.error(f"API request failed -> {e}")
