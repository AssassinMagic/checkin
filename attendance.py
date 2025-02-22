from card_reader import CardReader
from database import Database

class AttendanceBackend():
    def __init__(self):
        super().__init__()
        self.database = Database()
        self.card_reader = CardReader()
        self.users = []

    def searchUserByEmail(self, email):
        """Search for a user by email and return the user info if found."""
        user_info = self.database.get_user_by_email(email)
        if user_info:
            return user_info

    def process_card_info(self, user_info):
        """Process the card information and interact with the database."""
        print("process_card_info() called!") 
        print(f"Received user_info: {user_info}")

        student_id = user_info.get("student_id")
        db_user_info = self.database.get_user_by_student_id(student_id)
        if db_user_info:
            print(f"User with student ID {student_id} found in the database.")
            print(f"Updated user info: {db_user_info}")
            return db_user_info
        else:
            print(f"User with student ID {student_id} not found in the database.")
            if 'user_email' not in user_info:
                user_info['user_email'] = 'unknown@example.com'  # Default email if not provided
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
        return user_data
