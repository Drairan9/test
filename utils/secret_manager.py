from dotenv import load_dotenv
import os

load_dotenv()


class SecretManager:
    @staticmethod
    def get_bot_token() -> str:
        if os.getenv('TOKEN') is None:
            raise Exception("Missing environment variable: TOKEN")

        return os.getenv('TOKEN')

    @staticmethod
    def get_channel_id() -> int:
        if os.getenv('CHANNEL_ID') is None:
            raise Exception("Missing environment variable: CHANNEL_ID")

        return int(os.getenv('CHANNEL_ID'))
