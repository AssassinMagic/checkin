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

    def process_card_info(self, user_info):
        """Process the card information and interact with the database."""
        self.database.add_user_to_db(user_info)
        self.addUser(user_info)

    def start_card_reader(self):
        """Start the card reader."""
        self.card_reader.start()

def main():
    backend = AttendanceBackend()
    backend.start_card_reader()
    while True:
        try:
            pass  # Keep the main thread alive
        except KeyboardInterrupt:
            print("\nExiting program.")
            break  # Allows graceful exit with Ctrl+C

if __name__ == "__main__":
    main()
