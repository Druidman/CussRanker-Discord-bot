from bot.services import Spell_checker
from bot.database.models import User
from bot.config import Config

class Event_handler():
    def __init__(self,groq_api_key):
        self.spell_checker = Spell_checker(groq_api_key=groq_api_key)

    def on_message(self,message,client) -> dict:
        messages = []
        if message.author == client.user:
            return False
    
        msg = message.content

        check = self.spell_checker.handle_message(msg)
        name = message.author
        mention = name.mention
        if check == "add":
            user = User()
            
            if not user.add_points(name=name):
                return False
            points = user.get_points(name=name)[0]

            if not points:
                print("error in points")
                return False

            return f"{mention} \nMasz już {points}punktów!"
        
        
        return f'Nie dodajemy {name}'

    
    def on_ready(self,client):
        
        Config(client=client)
        
    
    