import psycopg2 as pg
from dotenv import load_dotenv
import os

load_dotenv()

class Database:
    def __init__(self):
        self.connection = pg.connect(
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_DATABASE")
        )

        self.cursor = self.connection.cursor()


    def close_connection(self):
        self.cursor.close()
        self.connection.close()
