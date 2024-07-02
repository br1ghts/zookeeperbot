import discord
from discord import app_commands
from discord.ext import commands
from src.utils.translations import translate_message

def setup(bot: commands.Bot):
    @bot.tree.command(name="translate", description="Translate a message")
    @app_commands.describe(message="The message to translate", target_language="The language to translate the message to")
    async def translate(interaction: discord.Interaction, message: str, target_language: str):
        translated_message = await translate_message(message, target_language)
        await interaction.response.send_message(translated_message)