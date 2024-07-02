import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('YOUR_BOT_TOKEN')

role_to_language = {
    'English': 'en',
    'Dutch': 'nl',
    'Spanish': 'es'
}