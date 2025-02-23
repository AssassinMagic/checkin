import os
import psycopg2
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Database:
    def __init__(self):
        self.database_url = os.getenv('DATABASE_URL')
        self.connection = self.connect_to_db()

    def connect_to_db(self):
        """Connect to the database using DATABASE_URL."""
        try:
            connection = psycopg2.connect(self.database_url)
            return connection
        except Exception as e:
            print(f"Error connecting to database: {e}")
            return None

    def get_user_by_student_id(self, student_id):
        """Retrieve user information from the database by student ID."""
        if self.connection:
            try:
                with self.connection.cursor() as cursor:
                    cursor.execute('''
                        SELECT name, user_email, skate_size, skate_time
                        FROM reservations
                        WHERE student_id = %s
                    ''', (student_id,))
                    user_info = cursor.fetchone()
                    if user_info:
                        return {
                            "name": user_info[0],
                            "user_email": user_info[1],
                            "skate_size": user_info[2],
                            "skate_time": user_info[3]
                        }
            except Exception as e:
                print(f"Error querying database: {e}")
        return None
    
    def get_user_by_email(self, email):
        """Retrieve user information from the database by email."""
        if self.connection:
            try:
                with self.connection.cursor() as cursor:
                    cursor.execute('''
                        SELECT name, user_email, student_id, skate_size, skate_time
                        FROM reservations
                        WHERE user_email = %s
                    ''', (email,))
                    user_info = cursor.fetchone()
                    if user_info:
                        return {
                            "name": user_info[0],
                            "user_email": user_info[1],
                            "student_id": user_info[2],
                            "skate_size": user_info[3],
                            "skate_time": user_info[4]
                        }
            except Exception as e:
                print(f"Error querying database: {e}")
        return None
    

    def update_user_attendance(self, identifier, check_in_time):
        """Update user attendance status in the reservations table."""
        if self.connection:
            try:
                with self.connection.cursor() as cursor:
                    if '@' in identifier:
                        cursor.execute('''
                            UPDATE reservations
                            SET attendance = TRUE
                                check_in_time = %s
                            WHERE user_email = %s
                        ''', (check_in_time, identifier))
                    else:
                        cursor.execute('''
                            UPDATE reservations
                            SET attendance = TRUE,
                                check_in_time = %s
                            WHERE student_id = %s
                        ''', (check_in_time, identifier))
                    self.connection.commit()
                    return True
            except Exception as e:
                print(f"Error updating attendance in reservations table: {e}")
                self.connection.rollback()
            return False
        
    def find_all_checkedin(self):
        print("find_all_checkedin() called!")
        if self.connection:
            try:
                with self.connection.cursor() as cursor:
                    cursor.execute('''
                        SELECT * FROM reservations
                        WHERE attendance = TRUE
                    ''')
                    data = cursor.fetchall()
                    print(data)
                    checked_in_users = []
                    for user in data:
                        checked_in_users.append({
                            "user_email": user[1],
                            "name": user[2],
                            "student_id": user[3],
                            "skate_size": user[4],
                            "skate_time": user[5],
                        })
                        print(checked_in_users)
                    return checked_in_users
            except Exception as e:
                print(f"Error fetching checked-in users: {e}")
                return []
        return []
    

    def get_all_users(self):
        """Retrieve all user information from the reservations table."""
        if self.connection:
            try:
                with self.connection.cursor() as cursor:
                    cursor.execute('''
                        SELECT name, user_email, student_id, skate_time, skate_size, song_recommendation, attendance, check_in_time
                        FROM reservations
                    ''')
                    data = cursor.fetchall()
                    all_users = []
                    for user in data:
                        all_users.append({
                            "name": user[0],
                            "user_email": user[1],
                            "student_id": user[2],
                            "skate_time": user[3],
                            "skate_size": user[4],
                            "song_recommendation": user[5],
                            "attendance": user[6],
                            "check_in_time": user[7]
                        })
                    return all_users
            except Exception as e:
                print(f"Error fetching all users: {e}")
                return []
        return []