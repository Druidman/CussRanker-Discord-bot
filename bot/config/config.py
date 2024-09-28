class Config():
    def __init__(self,client):
        from bot.database import setup_database
        from bot.database.models import User
        print(f"Hello, I am logged in as {client.user}")
        members = []
        for guild in client.guilds:
            for member in guild.members:
                if member.bot:
                    continue
                members.append(member.name)

        setup_database()
        for member in members:
            user = User()
            if user.check_existance(user=member):
                continue

            user.insert_user(user=member)