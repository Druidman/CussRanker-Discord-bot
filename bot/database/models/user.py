from bot.database import conn

class User():
    def __init__(self):
        self.cursor = conn.cursor()

    def add_points(self,name) -> bool:
        try:
            self.cursor.execute("""UPDATE user SET points= points +1 WHERE name=:name

            """, {"name": str(name)}
            )

            conn.commit()

            return True
        
        except Exception as e:
            print(f"Exception occured in user adding model: {e}")

            return False

    def get_points(self,name):
        try:
            self.cursor.execute("""SELECT points FROM user WHERE name=:name""",{"name": str(name)})
            return self.cursor.fetchone()
        except Exception as e:
            print(f"Exception occured in fetching points: {e}")
            return False

    def insert_user(self,user):
        try:
            self.cursor.execute("INSERT INTO user(name,points) VALUES(:name,:points)",{"name": str(user),"points": 0})
            conn.commit()
            return True
        except Exception as e:
            print(f'Exception occured in inserting user to database: {e}')
            return False
        
    def check_existance(self,user):
        try:
            self.cursor.execute("SELECT name FROM user WHERE name=:name",{"name": str(user)})
            return self.cursor.fetchone()
        except Exception as e:
            print(f'Exception in checking existance: {e}')
            return False

    



        


        
