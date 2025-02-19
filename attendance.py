import re
import threading
import psycopg2
from PyQt6.QtCore import QObject, pyqtSignal, pyqtSlot, QVariant
from card_reader import CardReader
from database import Database

class AttendanceBackend(QObject):
    addUserSignal = pyqtSignal(QVariant, arguments=['addUser'])

    def __init__(self):
        super().__init__()
        self.card_reader = CardReader(self.process_card_info)
        self.database = Database()

    @pyqtSlot(dict)
    def addUser(self, user_info):
        """Add user information to the ListModel in QML."""
        self.addUserSignal.emit(user_info)

    @pyqtSlot(str)
    def searchUserByEmail(self, email):
        """Search for a user by email and add to the ListModel if found."""
        user_info = self.database.get_user_by_email(email)
        if user_info:
            self.addUser(user_info)

    def process_card_info(self, user_info):
        """Process the card information and interact with the database."""
        student_id = user_info.get("student_id")
        db_user_info = self.database.get_user_by_student_id(student_id)
        if db_user_info:
            print(f"User with student ID {student_id} found in the database.")
            user_info.update(db_user_info)
            print(f"Updated user info: {user_info}")
        else:
            print(f"User with student ID {student_id} not found in the database.")
            # Ensure user_info has all required fields before adding to the database
            if 'email' not in user_info:
                user_info['email'] = 'unknown@example.com'  # Default email if not provided
            if 'skate_size' not in user_info:
                user_info['skate_size'] = 'unknown'  # Default skate size if not provided
            if 'skate_time' not in user_info:
                user_info['skate_time'] = 'unknown'  # Default skate time if not provided
            print(f"Default user info: {user_info}")

        self.addUser(user_info)
        print(f"Final user info sent to addUser: {user_info}")

    def start_card_reader(self):
        """Start the card reader."""
        self.card_reader.start()

def main():
    attendance = AttendanceBackend()
    attendance.start_card_reader()

if __name__ == "__main__":
    main()
