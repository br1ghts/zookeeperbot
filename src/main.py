import os
import sys
import discord
from discord.ext import commands
from dotenv import load_dotenv
import certifi

# Ensure the SSL_CERT_FILE environment variable is set correctly
os.environ['SSL_CERT_FILE'] = certifi.where()

# Add the project root to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from config.config import TOKEN

load_dotenv()

intents = discord.Intents.default()
intents.messages = True
intents.guilds = True
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

# Import and register commands
from src.commands.translate import setup as translate_setup
translate_setup(bot)

# Import and register events
from src.events.on_ready import setup as ready_setup
from src.events.on_message import setup as message_setup

ready_setup(bot)
message_setup(bot)

bot.run(TOKEN)