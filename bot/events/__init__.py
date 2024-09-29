from bot.services import Event_handler
from dotenv import load_dotenv
load_dotenv

import os


def register_events(client,groq_api_key):
    channel_id = os.environ.get("CHANNEL_ID")
    event_handler = Event_handler(groq_api_key=groq_api_key)

    @client.event
    async def on_ready():
        result = event_handler.on_ready(client)
        return

        

    @client.event
    async def on_message(message):
        result = event_handler.on_message(message=message,client=client)
        if result:
            

            channel = client.get_channel(channel_id)
            
            await channel.send(result)
            
    

    