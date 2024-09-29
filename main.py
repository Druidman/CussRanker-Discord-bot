import os

from dotenv import load_dotenv
from bot import create_bot

load_dotenv()

discord_token = os.environ.get("DISCORD_TOKEN")

bot = create_bot()

bot.run(token=str(discord_token))

