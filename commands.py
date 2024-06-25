from discord.ext import commands
import discord
from services.market_service_rest import MarketServiceREST
from utils.consts import *


class DiscordCommands(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def current(self, ctx, *, member: discord.Member = None):
        rsi_df = MarketServiceREST().get_rsi_list_with_timestamp(DEFAULT_CATEGORY, DEFAULT_SYMBOL, DEFAULT_INTERVAL)

        await ctx.send(f'{DEFAULT_SYMBOL} current rsi: {rsi_df["rsi"][0]}')

    @commands.command()
    async def last(self, ctx, *, member: discord.Member = None):
        rsi_df = MarketServiceREST().get_rsi_list_with_timestamp(DEFAULT_CATEGORY, DEFAULT_SYMBOL, DEFAULT_INTERVAL)

        await ctx.send(f'{DEFAULT_SYMBOL} last closed rsi: {rsi_df["rsi"][1]}')
