import discord
import os

from .events import register_events
from dotenv import load_dotenv

load_dotenv()
groq_api_key = os.environ.get("GROQ_API_KEY")
def create_bot():
    intents = discord.Intents.default()
    intents.message_content = True
    intents.guilds = True
    intents.members = True
    client = discord.Client(intents=intents)

    register_events(groq_api_key = groq_api_key, client=client)

    return client