import os
import psycopg2
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Database:
    def __init__(self):
        self.dbname = os.getenv('PGDATABASE')
        self.user = os.getenv('PGUSER')
        self.password = os.getenv('PGPASSWORD')
        self.host = os.getenv('PGHOST')
        self.port = os.getenv('PGPORT', '5432')  # Default port for PostgreSQL is 5432
        self.connection = self.connect_to_db()

    def connect_to_db(self):
        """Connect to the Neon database."""
        try:
            connection = psycopg2.connect(
                dbname=self.dbname,
                user=self.user,
                password=self.password,
                host=self.host,
                port=self.port
            )
            return connection
        except Exception as e:
            print(f"Error connecting to database: {e}")
            return None

    def add_user_to_db(self, user_info):
        """Add user information to the database."""
        if self.connection:
            try:
                with self.connection.cursor() as cursor:
                    cursor.execute('''
                        INSERT INTO attendance (name, email, skateSize, timeSlot)
                        VALUES (%s, %s, %s, %s)
                    ''', (user_info['name'], user_info['email'], user_info['skateSize'], user_info['timeSlot']))
                    self.connection.commit()
            except Exception as e:
                print(f"Error inserting into database: {e}")