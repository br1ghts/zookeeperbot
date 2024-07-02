import discord
from discord.ext import commands

def setup(bot: commands.Bot):
    @bot.event
    async def on_ready():
        print(f'Logged in as {bot.user}')
        try:
            await bot.tree.sync()
            print("Slash commands synced")
        except Exception as e:
            print(f"Error syncing commands: {e}")