import discord
from discord import Client
from discord.ext import commands
from loguru import logger
from utils.secret_manager import SecretManager


class DiscordEvents(commands.Cog):
    def __init__(self, client, rsiworker):
        self.client: Client = client
        self._is_routine_running = False
        self.RsiWorker = rsiworker

    @commands.Cog.listener()
    async def on_ready(self):
        logger.info(f"{self.client.user} is running.")
        if not self._is_routine_running:
            await self._start_routines()

    # Gateway can fail, but RsiWorker is independent
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error) -> None:
        if isinstance(error, commands.CommandNotFound):
            await ctx.send("Unknown command")

    async def _start_routines(self):
        if self.client.get_channel(SecretManager.get_channel_id()).type != discord.ChannelType.text:
            raise Exception("Environment variable CHANNEL_ID does not point to a text channel.")

        await self.RsiWorker.start_worker()
        self._is_routine_running = True

    async def _stop_routines(self):
        await self.RsiWorker.stop_worker()
        self._is_routine_running = False
