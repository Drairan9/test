from bot import DiscordBot
import asyncio
import nest_asyncio


async def main():
    nest_asyncio.apply()
    discord_bot = DiscordBot()
    await discord_bot.start()


if __name__ == "__main__":
    loop = asyncio.new_event_loop()
    loop.run_until_complete(main())
