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

    def add_good_message(self,name) -> bool:
        try:
            self.cursor.execute("UPDATE user SET goodMsg= goodMsg+1 WHERE name=:name",
                                {"name": str(name)})
            conn.commit()
            return True
                                
        except Exception as e:
            print(f"Exception occured while adding good message to user account: {e}")
    def add_bad_message(self,name) -> bool:
        try:
            self.cursor.execute("UPDATE user SET badMsg= badMsg+1 WHERE name=:name",
                                {"name": str(name)})
            conn.commit()
            return True
        except Exception as e:
            print(f"Exception occured while adding bad message to user account: {e}")

    def get_value(self,name,value):
        try:
            self.cursor.execute(f"""SELECT {value} FROM user WHERE name=:name""",{"name": str(name)})
            return self.cursor.fetchone()
        except Exception as e:
            print(f"Exception occured in fetching {value}: {e}")
            return False

    def insert_user(self,user):
        try:
            self.cursor.execute("INSERT INTO user(name,points,badMsg,goodMsg) VALUES(:name,:points,:bad,:good)",
                                {"name": str(user),
                                 "points": 0,
                                 "bad": 0,
                                 "good": 0
                                 })
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

    



        


        
