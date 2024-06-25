from utils.secret_manager import SecretManager
from discord import Intents
from discord.ext import commands
from events import DiscordEvents
from commands import DiscordCommands
from helpers.messages_helper import DiscordHelperMessages
from workers.rsi_worker import RsiWorker


class DiscordBot:
    def __init__(self):
        self.intents: Intents = Intents.default()
        self.intents.message_content = True  # NOQA

        self.client = commands.Bot(command_prefix="!", intents=self.intents)

        self.SecretManager = SecretManager
        self.MessagesHelper = DiscordHelperMessages()
        self.RsiWorker = RsiWorker(self.client)

    async def start(self) -> None:
        await self.load_modules()
        self.client.run(token=self.SecretManager.get_bot_token())

    async def load_modules(self) -> None:
        await self.client.add_cog(DiscordEvents(self.client, self.RsiWorker))
        await self.client.add_cog(DiscordCommands(self.client))
