import discord
from discord.ext import commands
from src.utils.translations import handle_message_translation

def setup(bot: commands.Bot):
    @bot.event
    async def on_message(message: discord.Message):
        if message.author == bot.user:
            return
        await handle_message_translation(message, bot)