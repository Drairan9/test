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
            response = requests.post(url, headers=headers, data=prepared_json)

            if response.status_code != 200:
                logger.error(f"Failed to send message -> code: {response.status_code} text: {response.text}")
                return False

            return True
        except Exception as e:
            logger.error(f"API request failed -> {e}")
            return False
