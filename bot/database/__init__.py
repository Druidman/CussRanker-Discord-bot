from .database import conn
from .migrations import *


def setup_database():
    Migrate_user(conn=conn)


    
