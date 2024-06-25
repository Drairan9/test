from discord.ext import commands
import discord
from utils.market_utils import MarketUtils


class DiscordCommands(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def hello(self, ctx, *, member: discord.Member = None):
        """Says hello"""
        member = member or ctx.author
        await ctx.send(f'Hello {member.name}~')

    @commands.command()
    async def current(self, ctx, *, member: discord.Member = None):
        symbol = "SOLUSDT"

        rsi_list = await MarketUtils().get_latest_rsi_list(symbol=symbol)

        await ctx.send(f'{symbol} current RSI: {rsi_list[0]}')

    @commands.command()
    async def last(self, ctx, *, member: discord.Member = None):
        symbol = "SOLUSDT"
        rsi_list = await MarketUtils().get_latest_rsi_list(symbol=symbol)

        await ctx.send(f'{symbol} last closed RSI: {rsi_list[1]}')
