from groq import Groq
import json

class Spell_checker():
    def __init__(self,groq_api_key):
        self.sys_prompt = """
        JSON. Zadecyduj czy wiadomość użytkownika jest wulgarna czy nie.
        Jeżeli jest wulgarna/wyzywa kogoś/jest wątpliwa etycznie, to zwróć takiego JSONa:
        {"decision": "add"}.
        Jeżeli nie zwiera przekleństw/wulgaryzmów to takiego JSONa:
        {"decision": "keep"}.
        JĘZYK STOSOWANY W WIADOMOŚCIACH JEST POTOCZNY.
        Oto wiadomość którą masz przeanalizować:
        """
        self.client = Groq(api_key=groq_api_key) 

    def handle_message(self,msg):
        check = self.ask_checker(msg)
        return check

    def ask_checker(self,msg):
        completion = self.client.chat.completions.create(
            model="gemma2-9b-it",
            messages=[
                {
                    "role": "system",
                    "content": self.sys_prompt
                    
                },
                {
                    "role": "assistant",
                    "content": "```json"
                },
                {
                    "role": "user",
                    "content": str(msg)
                }
            ],
            temperature=0.5,
            max_tokens=1024,
            top_p=1,
            stream=False,
            response_format={"type": "json_object"},
            stop=None,
        )
        reply = completion.choices[0].message.to_dict()['content']
        reply = json.loads(reply)
        print(reply)
        return reply['decision']
    
    def check_spelling(self,msg):
        pass