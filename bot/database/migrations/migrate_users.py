class Migrate_user():
    def __init__(self, conn):
        self.cursor = conn.cursor()

        self.cursor.execute("""CREATE TABLE IF NOT EXISTS user(
                            name TEXT,
                            points INTERER,
                            badMsg INTEGER,
                            goodMsg INTEGER

                            )
                            """)
        
        conn.commit()
        print("User succesfully migrated to the database")

        