from bot.services import Spell_checker
from bot.database.models import User
from bot.config import Config

class Event_handler():
    def __init__(self,groq_api_key):
        self.spell_checker = Spell_checker(groq_api_key=groq_api_key)

    def on_message(self,message,client) -> dict:
        if message.author == client.user:
            return False
    
        msg = message.content

        check = self.spell_checker.handle_message(msg)
        name = message.author
        mention = name.mention
        user = User()
        if check == "add":

            
            if not user.add_points(name=name):
                return False
            
            if not user.add_bad_message(name=name):
                return False
            
            points = user.get_value(name=name,value="points")[0]
            good_msg = int(user.get_value(name=name,value="goodMsg")[0])
            bad_msg = int(user.get_value(name=name,value="badMsg")[0])

            sum = good_msg + bad_msg

            if not points:
                print("error in points")
                return False
            
            
            ratiogood = good_msg / sum
            ratiobad = bad_msg / sum
            if (points/10) == int(points/10):
                return f"{mention} \nMasz już {int(points/10)}LVL!\nGood: {int(round(ratiogood,2)*100)}%\nBad: {int(round(ratiobad,2)*100)}%"
            
            return False
        

        user.add_good_message(name=name)
        return False

    
    def on_ready(self,client):
        
        Config(client=client)
        
    
    