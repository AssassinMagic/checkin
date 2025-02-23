from card_reader import CardReader
from database import Database
import datetime
from log import log_user

class AttendanceBackend():
    def __init__(self):
        super().__init__()
        self.database = Database()
        self.card_reader = CardReader()
        self.users = []

    def search_user_by_email(self, email):
        """Search for a user by email and return the user info if found."""
        user_data = self.database.get_user_by_email(email)
        if user_data:
            print(f"User with email {email} found in the database.")
            print(f"Updated user info: {user_data}")
            if 'user_email' not in user_data:
                user_data['user_email'] = 'unknown'  # Default email if not provided
            if 'skate_size' not in user_data:
                user_data['skate_size'] = 'unknown'  # Default skate size if not provided
            if 'skate_time' not in user_data:
                user_data['skate_time'] = 'unknown'  # Default skate time if not provided
        else:
            print(f"User with email {email} not found in the database.")
            user_data = {"user_email": email, "student_id": "N/A", "skate_size": "unknown", "skate_time": "unknown"}
        
        if user_data["student_id"] == "N/A":
            if user_data["user_email"] != "unknown":
                self.database.update_user_attendance(user_data["user_email"], datetime.datetime.now())
                log_user(user_data)
            else:
                print("Can't find user to update attendance.")
        else:
            self.database.update_user_attendance(user_data["student_id"], datetime.datetime.now())
            log_user(user_data)
        
        return user_data

    def process_card_info(self, user_info):
        """Process the card information and interact with the database."""
        print("process_card_info() called!") 
        print(f"Received user_info: {user_info}")

        student_id = user_info.get("student_id")
        db_user_info = self.database.get_user_by_student_id(student_id)
        if db_user_info:
            print(f"User with student ID {student_id} found in the database.")
            print(f"Updated user info: {db_user_info}")
            db_user_info["student_id"] = student_id
            return db_user_info
        else:
            print(f"User with student ID {student_id} not found in the database.")
            if 'user_email' not in user_info:
                user_info['user_email'] = 'unknown'  # Default email if not provided
            if 'skate_size' not in user_info:
                user_info['skate_size'] = 'unknown'  # Default skate size if not provided
            if 'skate_time' not in user_info:
                user_info['skate_time'] = 'unknown'  # Default skate time if not provided
            print(f"Default user info: {user_info}")
            return user_info

    def start_card_reader(self):
        """Start the card reader."""
        self.card_reader.start()

    def swipe_card(self, card_id):
        student_id, name = CardReader.parse(card_id)
        user_data = self.process_card_info({"student_id": student_id, "name": name})
        if user_data["student_id"] == "N/A":
            if user_data["user_email"] != "unknown":
                self.database.update_user_attendance(user_data["user_email"], datetime.datetime.now())
                log_user(user_data)
            else:
                print("Can't find user to update attendance.")
        else:
            self.database.update_user_attendance(user_data["student_id"], datetime.datetime.now())
            log_user(user_data)
        return user_data

    def initalize_attendance(self):
        checkedIn = self.database.find_all_checkedin()
        if checkedIn:
            return checkedIn
        else:
            return []
        
    def get_all_users(self):
        return self.database.get_all_users()