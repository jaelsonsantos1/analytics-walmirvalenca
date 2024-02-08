import psycopg2 as pg
from dotenv import load_dotenv
import os

load_dotenv()

class Database:
    def __init__(self):
        self.connection = pg.connect(
            os.getenv('DATABASE_URL')
        )

        self.cursor = self.connection.cursor()


    def close_connection(self):
        self.cursor.close()
        self.connection.close()
