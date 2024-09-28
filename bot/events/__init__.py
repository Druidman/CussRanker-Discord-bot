from bot.services import Event_handler

def register_events(client,groq_api_key):
    event_handler = Event_handler(groq_api_key=groq_api_key)

    @client.event
    async def on_ready():
        result = event_handler.on_ready(client)
        return

        

    @client.event
    async def on_message(message):
        result = event_handler.on_message(message=message,client=client)
        if result:
            await message.channel.send(result)
    

    